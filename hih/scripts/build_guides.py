#!/usr/bin/env python3
"""Build Guide-contract HTML + article JSON from content/guides.py, and validate the contract mechanically.

Output: content/out/<handle>.json  (articleCreate input + metafields + media slots)
Fails (exit 1) on any contract violation, so a malformed guide never reaches Shopify.
"""
import html, json, re, sys, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "content"))
from guides import GUIDES, AFFILIATE  # noqa: E402

AFFILIATE_HREF = "#add-affiliate-link"
DISCLOSURE = ("<strong>Affiliate disclosure:</strong> some links in this guide are affiliate links. "
              "If you buy through them, we may earn a commission at no extra cost to you. "
              "We only recommend products we'd use ourselves.")

def linkify(g):
    """Turn the first occurrence of each affiliate phrase in the step text into a sponsored placeholder link."""
    missing = []
    for s in g['steps']:
        if '<a ' in s['body']:
            missing.append(f"inline <a> in step '{s['title']}' (affiliate links come only from AFFILIATE)")
    for phrase in AFFILIATE.get(g['handle'], []):
        for s in g['steps']:
            if phrase in s['body']:
                s['body'] = s['body'].replace(phrase, f'<a href="{AFFILIATE_HREF}" rel="sponsored noopener" target="_blank">{phrase}</a>', 1)
                break
        else:
            missing.append(phrase)
    if AFFILIATE.get(g['handle']):
        g['disclosure'] = DISCLOSURE
    return missing

OUT = ROOT / "content" / "out"
OUT.mkdir(parents=True, exist_ok=True)
ALLOWED_CLASSES = {"guide-intro", "callout", "callout--disclosure", "callout--safety", "callout--pro", "guide-steps"}
DIFFICULTY = {"Beginner", "Intermediate", "Advanced"}

def body_html(g):
    p = [f'<p class="guide-intro">{g["intro"]}</p>']
    if g.get("disclosure"):
        p.append(f'<aside class="callout callout--disclosure"><p>{g["disclosure"]}</p></aside>')
    if g.get("safety"):
        p.append(f'<aside class="callout callout--safety"><p>{g["safety"]}</p></aside>')
    p.append("<h2>Steps</h2>")
    p.append('<ol class="guide-steps">')
    for s in g["steps"]:
        li = [f"<h3>{html.escape(s['title'])}</h3>"]
        if s.get("fig"):
            f = s["fig"]
            li.append(f'<figure><img src="hih-media://{f["stem"]}" alt="{html.escape(f["alt"], quote=True)}" width="1200" height="900" loading="lazy"><figcaption>{html.escape(f["caption"])}</figcaption></figure>')
        li.append(s["body"])
        p.append("<li>" + "".join(li) + "</li>")
    p.append("</ol>")
    p.append(f'<aside class="callout callout--pro"><p>{g["pro"]}</p></aside>')
    p.append("<h2>FAQ</h2>")
    for q, a in g["faq"]:
        p.append(f"<h3>{html.escape(q)}</h3><p>{html.escape(a)}</p>")
    return "\n".join(p)

def validate(g, body):
    errs = []
    if len(g["title"]) > 60: errs.append(f"title {len(g['title'])} chars > 60")
    if len(g["summary"]) > 155: errs.append(f"summary {len(g['summary'])} chars > 155")
    if g["difficulty"] not in DIFFICULTY: errs.append("difficulty not in enum")
    if g["difficulty"] not in g["tags"]: errs.append("tags must include difficulty")
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", g["handle"]): errs.append("bad handle")
    if not (3 <= len(g["faq"]) <= 5): errs.append("FAQ must have 3–5 questions")
    used = set(re.findall(r'class="([^"]+)"', body))
    for c in used:
        for part in c.split():
            if part not in ALLOWED_CLASSES: errs.append(f"class not in contract: {part}")
    if "sponsored" in body and "callout--disclosure" not in body: errs.append("affiliate link without disclosure")
    if body.find("callout--disclosure") > -1 and body.find('rel="sponsored') > -1 and body.find("callout--disclosure") > body.find('rel="sponsored'):
        errs.append("disclosure must come before first affiliate link")
    for s in g["steps"]:
        if "<strong>Done right:</strong>" not in s["body"]: errs.append(f"step '{s['title']}' lacks a 'Done right' check")
    if not g.get("video", "").startswith("https://www.youtube.com/watch?v="): errs.append("video_url missing or not a YouTube watch URL")
    return errs

failed = False
index = []
for g in GUIDES:
    missing = linkify(g)
    body = body_html(g)
    errs = validate(g, body) + [m if m.startswith("inline") else f"affiliate phrase not found in steps: {m}" for m in missing]
    if errs:
        failed = True
        print(f"✗ {g['handle']}: " + "; ".join(errs))
        continue
    media = [s["fig"] for s in g["steps"] if s.get("fig")]
    record = {
        "blog_handle": g["blog"], "blog_title": g["blog_title"],
        "article": {"title": g["title"], "handle": g["handle"], "summary": g["summary"], "tags": g["tags"],
                    "body": body, "isPublished": False, "author": {"name": "Home Improvement Hub"}},
        "metafields": [
            {"namespace": "guide", "key": "difficulty", "type": "single_line_text_field", "value": g["difficulty"]},
            {"namespace": "guide", "key": "time_required", "type": "single_line_text_field", "value": g["time"]},
            {"namespace": "guide", "key": "cost_range", "type": "single_line_text_field", "value": g["cost"]},
            {"namespace": "guide", "key": "tools", "type": "list.single_line_text_field", "value": json.dumps(g["tools"])},
            {"namespace": "guide", "key": "materials", "type": "list.single_line_text_field", "value": json.dumps(g["materials"])},
            {"namespace": "guide", "key": "video_url", "type": "url", "value": g["video"]},
        ],
        "media": media,
        "hero_slot": f"{g['handle']}-hero",
    }
    (OUT / f"{g['handle']}.json").write_text(json.dumps(record, indent=2, ensure_ascii=False))
    index.append({"handle": g["handle"], "blog": g["blog"], "title": g["title"], "figures": len(media), "steps": len(g["steps"])})
    print(f"✓ {g['handle']}: {len(g['steps'])} steps, {len(media)} diagrams, {len(g['faq'])} FAQ, {body.count(AFFILIATE_HREF)} affiliate placeholders")

(OUT / "index.json").write_text(json.dumps(index, indent=2))
sys.exit(1 if failed else 0)
