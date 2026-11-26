"""Cut the next Pinterest bulk-upload CSV from pinterest_queue.json.

Pinterest's bulk create only keeps pins scheduled up to about 2 weeks ahead and silently drops later rows
(found 2026-11-26: the 30-day CSVs uploaded Nov 14 stopped on Nov 27). So the queue is uploaded in chunks
of at most 13 days, and the uploaded rows are removed from the queue.

Pinterest also refuses a second row with the same link in one file ("Duplicate Pin link", found 2026-11-26),
so every link gets utm parameters naming its pin image, which makes each link unique (and trackable).

Usage: python3 next_pin_chunk.py START_DATE [DAYS]   e.g. python3 next_pin_chunk.py 2026-11-28 13
Writes pinterest_chunk_<start>.csv and rewrites pinterest_queue.json without the rows it used.
"""
import csv
import datetime as dt
import json
import os
import sys
from urllib.parse import urlencode

SLOTS = [(13, 7), (14, 33), (15, 22), (17, 41), (20, 3), (21, 48), (23, 18)]  # UTC, 7 pins/day
MAX_DAYS = 13

start = dt.date.fromisoformat(sys.argv[1])
days = min(int(sys.argv[2]) if len(sys.argv) > 2 else MAX_DAYS, MAX_DAYS)
data = json.load(open("pinterest_queue.json"))
rows = data["rows"]
n = min(len(rows), days * len(SLOTS))
out = f"pinterest_chunk_{start.isoformat()}.csv"
with open(out, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(data["header"])
    for i, r in enumerate(rows[:n]):
        d = start + dt.timedelta(days=i // len(SLOTS))
        h, m = SLOTS[i % len(SLOTS)]
        stem = os.path.splitext(os.path.basename(r[1]))[0]
        link = r[5].split("?")[0] + "?" + urlencode({"utm_source": "pinterest", "utm_medium": "social", "utm_content": stem})
        w.writerow(r[:5] + [link, f"{d.isoformat()}T{h:02d}:{m:02d}:00"] + r[7:])
data["rows"] = rows[n:]
json.dump(data, open("pinterest_queue.json", "w"))
last = start + dt.timedelta(days=(n - 1) // len(SLOTS))
print(f"{out}: {n} pins, {start} to {last}; {len(data['rows'])} left in queue; next chunk starts {last + dt.timedelta(days=1)}")
