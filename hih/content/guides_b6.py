"""Batch 6 (content plan, week 1): outdoor faucet with no indoor shut-off; water softener not using salt."""

def step(title, body, fig=None):
    return {"title": title, "body": body, "fig": fig}

def fig(stem, alt, caption):
    return {"stem": stem, "alt": alt, "caption": caption}

GUIDES_B6 = [
{
 "blog": "plumbing", "blog_title": "Plumbing Basics",
 "handle": "winterize-outdoor-faucet-without-shut-off-valve",
 "title": "Winterize an Outdoor Faucet With No Shut-Off Valve",
 "summary": "No indoor shut-off for your outdoor faucet? Check if it's frost-free, find a hidden valve, insulate it, drain it on hard freezes, then fix it for good.",
 "tags": ["Beginner", "Plumbing", "Seasonal", "Under 1 hour"],
 "difficulty": "Beginner", "time": "20–45 minutes", "cost": "$5–$40",
 "tools": ["Flashlight", "Bucket", "Utility knife or scissors", "Caulk gun"],
 "materials": ["Insulated faucet cover", "Foam pipe insulation sized to your pipe", "Foam insulation tape", "Exterior caulk or low-expansion spray foam"],
 "video": "https://www.youtube.com/watch?v=ewZfmojYgEg",
 "intro": "Many older homes have outdoor faucets with no shut-off valve of their own inside, so you can't simply close it and drain the line before winter. You still have good options. This guide shows how to check what you have, protect the faucet this winter, and fix the problem for good.",
 "safety": "<strong>Safety:</strong> never thaw a frozen faucet or pipe with a torch or any open flame. If you use pipe heat cable, choose one that is UL- or CSA-listed for water pipes, plug it into a GFCI outlet and follow its instructions exactly.",
 "steps": [
  step("Disconnect the hose",
   "<p>Unscrew the garden hose and any splitter, timer or quick-connect from the faucet. A hose left on traps water in the faucet and can split it, even on a frost-free model. Drain the hose and store it.</p>"
   "<p><strong>Done right:</strong> nothing is attached to the faucet.</p>"),
  step("Check whether it's frost-free",
   "<p>Look at the pipe where it comes through the wall inside, in the basement, crawl space or garage. A <em>frost-free</em> faucet has a long body, usually 6 to 12 in, that reaches through the wall, so it closes in the warm part of the house and drains itself. If yours is frost-free, removing the hose is the main job: you can skip to the cover step. A <em>standard</em> faucet closes right at the outside wall, so the water behind it sits in the cold.</p>"
   "<p><strong>Done right:</strong> you know whether you have a frost-free or a standard faucet.</p>",
   fig("how-to-winterize-outdoor-faucets-step-2", "Cross-section comparing a standard outdoor faucet that seals at the outside wall with a frost-free faucet that seals inside the heated house", "A frost-free faucet closes inside the warm wall; a standard one closes outside.")),
  step("Look once more for a hidden shut-off",
   "<p>Follow the faucet's pipe inward with a flashlight. In older homes the valve is often in the basement ceiling near the outside wall; in newer homes it's often next to the main shut-off. Also check behind access panels, in the crawl space and in the garage. A round handle is a gate valve; a lever is a ball valve. If you find one, close it and follow our <a href=\"/blogs/plumbing/how-to-winterize-outdoor-faucets\">standard winterizing steps</a> instead.</p>"
   "<p><strong>Done right:</strong> you have traced the pipe from the wall until it joins another line, and you're sure there's no valve on it.</p>"),
  step("Fit an insulated faucet cover",
   "<p>Push an insulated faucet cover over the faucet and tighten its loop or strap so the cover seals flat against the siding. A cover traps heat coming from the house and helps through short, mild freezes. On its own it won't protect a standard faucet through a long, hard freeze.</p>"
   "<p><strong>Done right:</strong> the cover sits tight against the wall with no gap around its edge.</p>"),
  step("Insulate and seal on the inside",
   "<p>Where the faucet's pipe runs through a cold rim joist, crawl space or garage, wrap it with foam pipe insulation and tape the seams. Seal any gap around the pipe where it passes through the wall with exterior caulk or low-expansion spray foam, so cold air can't blow on it.</p>"
   "<p><strong>Done right:</strong> no bare pipe is exposed in the cold space, and you feel no draft around the wall opening.</p>"),
  step("Drain it from the main on hard freezes",
   "<p>Before a forecast below about 20°F, or if you'll be away, turn off the <a href=\"/blogs/plumbing/how-to-find-main-water-shut-off-valve\">main water shut-off</a>. Open the outdoor faucet and the lowest faucet in the house to drain the line, and leave them open. With no branch valve, the line refills as soon as the main is back on, so keep the main off until the cold passes, then close the faucets and turn it on slowly.</p>"
   "<p><strong>Done right:</strong> the outdoor faucet stops dripping, and the house water stays off until the hard freeze is over.</p>"),
  step("Fix it for good before next winter",
   "<p>The lasting fix is either a shut-off valve with a bleeder cap on the faucet's branch line, or replacing the faucet with a <strong>frost-free sillcock</strong>. Both mean cutting into the supply pipe with the main off. A plumber can usually do either in one visit; a confident DIYer can add a push-to-connect valve on copper or PEX by following the fitting's instructions.</p>"
   "<p><strong>Done right:</strong> the outdoor faucet has its own shut-off, or it's frost-free.</p>"),
 ],
 "pro": "<strong>Call a licensed plumber if:</strong> the faucet or its pipe is already frozen or leaking (turn off the main first), you see water inside the wall when the faucet runs, the main shut-off is stuck, or you want a shut-off valve or frost-free sillcock installed.",
 "faq": [
  ("Can I winterize an outdoor faucet without a shut-off valve?", "Yes. Remove the hose, insulate the faucet and its pipe, and before hard freezes turn off the main water and drain the line. Long term, add a shut-off valve or a frost-free faucet."),
  ("Do outdoor faucet covers really work?", "They help through short, mild freezes by trapping heat from the house. On a standard faucet with water in the line, a cover alone isn't enough for a long, hard freeze."),
  ("Should I leave the outdoor faucet dripping?", "A slow drip can help on one very cold night, but it can freeze into ice on steps and patios. Draining the line with the main off is safer when you can do it."),
  ("How do I know if my outdoor faucet is frost-free?", "Check inside where the pipe comes through the wall. A frost-free faucet has a long body, usually 6 to 12 in, that reaches into the house, and the handle often sits at a slight downward angle."),
  ("What temperature will freeze an outdoor faucet?", "Water freezes at 32°F, but pipes are most at risk when it stays around 20°F or colder for several hours, especially on walls that face the wind."),
 ],
},
{
 "blog": "maintenance", "blog_title": "Home Maintenance",
 "handle": "water-softener-not-using-salt",
 "title": "Water Softener Not Using Salt? Causes and Fixes",
 "summary": "Water softener not using salt? Check the bypass, clock and settings, break a salt bridge or mush, clean the injector and test a manual regeneration.",
 "tags": ["Beginner", "Home Maintenance", "Water", "Troubleshooting"],
 "difficulty": "Beginner", "time": "30–90 minutes", "cost": "$0–$25",
 "tools": ["Broom handle or long wooden dowel", "Bucket and a plastic scoop", "Wet-dry vacuum", "Flashlight", "Water hardness test strips"],
 "materials": ["Water softener salt (pellets or crystals)", "Silicone grease (for injector O-rings)"],
 "video": "https://www.youtube.com/watch?v=ZG93k-_4pkA",
 "intro": "A water softener turns salt into brine to recharge its resin. If the salt level hasn't dropped in weeks and your water feels hard again, something is stopping that. Most causes are quick to check yourself. This guide covers salt-based softeners with a separate brine tank; use your manual for model-specific steps.",
 "safety": "<strong>Safety:</strong> salt bags are heavy; lift with your legs. Unplug the softener and put it in bypass before you reach into the valve, and release pressure the way your manual shows before opening any cap.",
 "steps": [
  step("Confirm it's really not using salt",
   "<p>Mark the salt level inside the brine tank with tape or a marker. Check it again after a week of normal water use, and test water from a cold kitchen faucet with hardness test strips. A level that hasn't moved plus hard water means the softener isn't making brine.</p>"
   "<p><strong>Done right:</strong> you know the salt level is stuck and the water tests hard.</p>"),
  step("Check the power, clock and bypass",
   "<p>Make sure the softener is plugged in and the display is on. After a power outage, many units lose the time and regenerate at the wrong hour, so reset the clock. Then check the bypass valve on the head: it must be in the service position, not bypass.</p>"
   "<p><strong>Done right:</strong> the display shows the correct time and water flows through the softener, not around it.</p>"),
  step("Check the settings",
   "<p>Look up the hardness and regeneration settings in your manual. If the hardness is set too low or regeneration is set too far apart, the softener rarely regenerates and uses little salt. Set the hardness to match a recent water test.</p>"
   "<p><strong>Done right:</strong> the hardness setting matches your water test.</p>"),
  step("Break up a salt bridge",
   "<p>A salt bridge is a hard crust that forms above the water, so the tank looks full but the salt never reaches the water. Push a broom handle straight down through the salt in a few spots. If it stops on a hard layer, gently break it up without hitting the tank walls. See our <a href=\"/blogs/maintenance/water-softener-maintenance\">water softener maintenance guide</a> for the full routine.</p>"
   "<p><strong>Done right:</strong> the handle slides all the way to the bottom of the tank.</p>"),
  step("Clear salt mush from the bottom",
   "<p>Salt mush is a thick sludge of recrystallized salt at the bottom of the tank that can block the brine well. If the handle hits mush, put the softener in bypass, scoop out the salt, vacuum out the water and sludge, and refill with fresh salt and a few inches of water, as your manual says.</p>"
   "<p><strong>Done right:</strong> the bottom of the tank is clear, and the brine well is free of sludge.</p>"),
  step("Clean the injector and screen",
   "<p>The injector (venturi) is a small nozzle in the valve head that pulls brine out of the tank. With the softener in bypass and pressure released, remove the injector cap, then rinse the screen and nozzle in warm water and clear the openings with a soft brush or a toothpick. Put a little silicone grease on the O-rings and reassemble. Also check that the brine line isn't kinked or loose.</p>"
   "<p><strong>Done right:</strong> the screen and nozzle are clean, and the brine line is firmly connected.</p>"),
  step("Run a manual regeneration and watch",
   "<p>Take the softener out of bypass and start a manual regeneration. During the brine draw, the water level in the brine tank should drop. Test your water the next day.</p>"
   "<p><strong>Done right:</strong> the brine level drops during regeneration, the salt level falls over the next week, and the water tests soft.</p>"),
 ],
 "pro": "<strong>Call a water treatment technician if:</strong> the softener won't start or stops partway through a regeneration, the brine level never drops after cleaning the injector, the control valve leaks, or the unit is 10 to 15 years old and the water stays hard.",
 "faq": [
  ("Why is my water softener not using salt?", "The most common causes are a salt bridge, salt mush, a clogged injector or brine line, the softener sitting in bypass, or a clock or setting that keeps it from regenerating. A failed valve motor is less common."),
  ("What's the difference between a salt bridge and salt mush?", "A salt bridge is a hard crust above the water with an empty gap below it. Salt mush is a sludge at the bottom of the tank. Both stop the softener from making brine."),
  ("Should there be water in my brine tank?", "On most softeners, yes: a few inches of water sit in the bottom of the tank. Some models only add water before a regeneration. Check your manual for what's normal on yours."),
  ("Can I use rock salt in a water softener?", "It's not recommended. Rock salt has more insoluble material that builds up as sludge. Use pellets or crystals made for water softeners."),
  ("How do I force my water softener to regenerate?", "Most softeners have a button or dial for a manual or immediate regeneration. Check your manual for the exact steps on your model."),
 ],
},
]

AFFILIATE_B6 = {
 "winterize-outdoor-faucet-without-shut-off-valve": [("insulated faucet cover", "https://link.amazon/B09OMF804"), "frost-free sillcock"],
 "water-softener-not-using-salt": ["hardness test strips"],
}
