"""Batch 5: guide + Pinterest package. Frozen pipes (Plumbing)."""

def step(title, body, fig=None):
    return {"title": title, "body": body, "fig": fig}

H = "how-to-keep-pipes-from-freezing"

GUIDES_B5 = [
{
 "blog": "plumbing", "blog_title": "Plumbing Basics",
 "handle": H,
 "title": "How to Keep Pipes From Freezing This Winter",
 "summary": "Stop frozen and burst pipes: find the at-risk pipes, seal drafts, add foam insulation, and know what to do on nights below 20°F.",
 "tags": ["Beginner", "Plumbing", "Pipes", "Winter prep"],
 "difficulty": "Beginner", "time": "1–3 hours", "cost": "$15–$60",
 "tools": ["Utility knife or sharp scissors", "Tape measure", "Caulk gun", "Flashlight", "Step ladder"],
 "materials": [
  "Foam pipe insulation, 6 ft lengths sized to your pipe (1/2 in or 3/4 in)",
  "Foam insulation tape or duct tape for seams and elbows",
  "Exterior caulk or low-expansion spray foam",
  "Insulated outdoor faucet covers",
  "UL- or CSA-listed plug-in pipe heat cable (optional, for problem pipes)",
 ],
 "video": "https://www.youtube.com/watch?v=gKoQHqVwxrA",
 "intro": "When water freezes inside a pipe, it expands and builds pressure until the pipe splits, and the flood starts when the ice thaws. A couple of hours of prep in the fall protects the pipes most likely to freeze. This guide is for homeowners with copper, PEX or CPVC supply lines in basements, crawl spaces, garages and outside walls.",
 "safety": "<strong>Safety:</strong> never thaw a pipe with a torch or any open flame. Use only heat cable that is UL- or CSA-listed for water pipes, plug it into a GFCI outlet, and follow its instructions exactly: misused heat cable is a fire risk. Keep space heaters away from anything that can burn and never leave them running unattended.",
 "steps": [
  step("Find the pipes most at risk",
   "<p>With a flashlight, follow the water lines in unheated spaces: the crawl space, basement rim joist, garage, attic, and any cabinet on an outside wall. Mark pipes that run along exterior walls, pass near vents or gaps, or have frozen before. Also find and label your <a href=\"/blogs/plumbing/how-to-find-main-water-shut-off-valve\">main water shut-off</a> now, so you can stop the water fast if a pipe ever bursts.</p>"
   "<p><strong>Done right:</strong> you have a short list of exposed pipe runs, and everyone in the house knows where the main shut-off is.</p>"),
  step("Seal drafts near the pipes",
   "<p>Cold moving air freezes pipes much faster than still air. Fill gaps where pipes, cables and dryer vents pass through exterior walls and the rim joist with exterior caulk (gaps up to 1/4 in) or low-expansion spray foam (larger gaps). Close crawl-space vents or cover them for winter if your local building code allows it.</p>"
   "<p><strong>Done right:</strong> holding the back of your hand near each pipe penetration on a windy day, you feel no draft.</p>"),
  step("Insulate exposed pipes",
   "<p>Measure the pipe's outside diameter and buy foam pipe insulation to match: most 1/2 in copper and PEX lines take 1/2 in sleeves, and 3/4 in lines take 3/4 in sleeves. Open the slit, push the sleeve over the pipe, and press the self-seal edges together. At elbows, cut each end at 45 degrees so the two pieces meet without a gap, then wrap the joint with tape. Insulate cold lines as well as hot ones.</p>"
   "<p><strong>Done right:</strong> every exposed run is covered end to end, with no bare pipe showing at elbows, valves or seams.</p>",
   {"stem": f"{H}-step-3", "alt": "Diagram: foam sleeve sized to the pipe, with 45-degree cuts meeting at an elbow and taped", "caption": "Match the sleeve to the pipe size and miter the elbows so no pipe is exposed."}),
  step("Add heat cable to pipes that still freeze",
   "<p>For a pipe that has frozen before or runs where insulation alone isn't enough, use a plug-in pipe heat cable with a built-in thermostat. Lay or spiral it along the pipe exactly as its instructions say, fasten it with the tape or ties it specifies, and plug it into a GFCI outlet without an extension cord. Most cables must never touch, cross or overlap themselves, and some limit what insulation can go over them, so read the label before you insulate over it.</p>"
   "<p><strong>Done right:</strong> the cable's indicator light comes on in cold weather, the cable doesn't cross itself anywhere, and it is plugged straight into a GFCI outlet.</p>"),
  step("Shut off and drain outdoor faucets",
   "<p>Disconnect every garden hose, close the indoor shut-off valve for each outdoor spigot, and open the spigot outside to let it drain. Leave it open and add an insulated faucet cover. Our <a href=\"/blogs/plumbing/how-to-winterize-outdoor-faucets\">outdoor faucet guide</a> covers each step.</p>"
   "<p><strong>Done right:</strong> no hoses are attached, the spigots are drained and covered, and the indoor valves are closed.</p>"),
  step("Prepare for nights below 20°F",
   "<p>Research from the University of Illinois found that pipes in unheated spaces start to freeze when it drops to about 20°F outside, sooner in wind. On those nights, keep the thermostat at the same temperature day and night, and never lower than 55°F if you're away. Open the cabinet doors under sinks on outside walls, keep the garage door closed, and let the faucet farthest from your main shut-off drip slowly. On a single-handle faucet, set it to the middle so both hot and cold lines move.</p>"
   "<p><strong>Done right:</strong> a steady drip (not a stream) from the farthest faucet, cabinet doors open, and the thermostat holding at 55°F or higher.</p>",
   {"stem": f"{H}-step-6", "alt": "Diagram of a cold-night checklist: thermostat at 55°F, cabinet doors open, farthest faucet dripping, garage closed", "caption": "Four quick moves on any night forecast at 20°F or colder."}),
  step("Know the signs of a frozen pipe",
   "<p>If a faucet gives only a trickle or nothing on a cold morning, assume a frozen pipe. Leave that faucet open, find the cold section, and warm it with a hair dryer, a heating pad or warm towels, starting at the faucet end and working back. Check other faucets too: if one pipe froze, others may have.</p>"
   "<p><strong>Done right:</strong> full flow returns, and you find no wet spots or drips along the pipe once it thaws.</p>"),
 ],
 "pro": "<strong>Call a licensed plumber if:</strong> a pipe has split or is leaking (shut off the main water first), you can't find or reach the frozen section, the pipe runs inside an exterior wall and freezes every winter, or you need pipes rerouted or a crawl space insulated.",
 "faq": [
  ["At what temperature do pipes freeze?", "Water freezes at 32°F, but pipes in unheated spaces usually start to freeze when it's around 20°F or colder outside, and sooner in windy or drafty spots."],
  ["Should I drip hot or cold water to keep pipes from freezing?", "Drip the faucet farthest from your main shut-off. On a single-handle faucet, set it to the middle so both hot and cold lines keep moving."],
  ["What temperature should I keep my house at to prevent frozen pipes?", "Keep it the same day and night, and never below 55°F, even when you're away."],
  ["Does pipe insulation stop pipes from freezing?", "It slows heat loss and helps a lot, but it can't keep a pipe warm indefinitely in extreme cold. On problem pipes, pair it with a listed heat cable and the cold-night steps."],
 ],
},
]

AFFILIATE_B5 = {
 H: ["foam pipe insulation", "pipe heat cable", "faucet cover"],
}
