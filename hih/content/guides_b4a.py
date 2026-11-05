"""Batch 4A: one new guide per category (kitchen faucet, seal grout, quarter round, cut in, fill valve,
outlet, door knob, seal deck, closet shelf, dryer vent). Same shape as guides.py."""
def step(title, body, fig=None):
    return {"title": title, "body": body, "fig": fig}

GUIDES_B4A = [
{
 "blog": "kitchen", "blog_title": "Kitchen",
 "handle": "how-to-replace-a-kitchen-faucet",
 "title": "How to Replace a Kitchen Faucet (Step by Step)",
 "summary": "Replace a kitchen faucet in an afternoon: shut off the water, free the old one with a basin wrench, mount the new faucet and test for leaks.",
 "tags": ["Intermediate", "Kitchen", "Plumbing", "Faucet"],
 "difficulty": "Intermediate", "time": "1.5–3 hours", "cost": "$100–$350 (faucet) + $15 parts",
 "tools": ["Basin wrench", "Adjustable wrench (2)", "Flashlight or headlamp", "Bucket and towels", "Putty knife", "Phone camera"],
 "materials": ["New kitchen faucet", "Two 3/8 in compression supply lines (if not included)", "Plumber's putty or silicone (per faucet instructions)", "Thread seal tape", "Rubbing alcohol"],
 "video": "https://www.youtube.com/watch?v=riDY_Juwqr4",
 "intro": "Swapping a kitchen faucet is mostly a matter of reaching the nuts under the sink. This guide covers a standard top-mount faucet on a sink with working shut-off valves, including single-handle, two-handle and pull-down models.",
 "safety": "<strong>Safety:</strong> wear safety glasses when you work under the sink, because grit and old corrosion fall into your eyes. If the sink has a garbage disposal, unplug it or switch off its breaker before you reach near it.",
 "steps": [
  step("Check the hole count and buy the right faucet",
   "<p>Look under the sink and count the holes in the sink deck: one, two, three or four. A faucet with a deck plate can cover extra holes; a one-hole faucet can't fill a three-hole sink without one. Note whether you need a sprayer, soap dispenser or a pull-down spout that needs clearance under a window.</p>"
   "<p><strong>Done right:</strong> the new faucet's box lists your hole count and it fits under any window or shelf above the sink.</p>"),
  step("Shut off the water and relieve pressure",
   "<p>Close both shut-off valves under the sink by turning them clockwise. Open the faucet to drain the lines. If a valve won't close fully or drips, close the main water valve instead and plan to replace that valve. Take a photo of all connections before you disconnect anything.</p>"
   "<p><strong>Done right:</strong> with the faucet open, no water comes out.</p>"),
  step("Disconnect and remove the old faucet",
   "<p>Put a bucket under the valves and loosen the supply line nuts at the valves with an adjustable wrench. Unclip a pull-down hose's weight and quick-connect. Reach up behind the sink with a basin wrench to loosen the mounting nuts, then lift the faucet out from the top. Scrape old putty and grime off the sink deck and wipe it with rubbing alcohol.</p>"
   "<p><strong>Done right:</strong> the sink deck is clean and dry, and the valves have only their bare outlets left.</p>"),
  step("Mount the new faucet",
   "<p>Follow the faucet's instructions for the seal: most use a rubber or plastic gasket under the base, some call for plumber's putty or silicone. Feed the lines through the hole, set the faucet straight, and have a helper hold it while you tighten the mounting nut or bracket from below. Snug it so the faucet can't twist, but don't crush the gasket.</p>"
   "<p><strong>Done right:</strong> the faucet sits square to the back of the sink and doesn't rotate when you push the handle.</p>"),
  step("Connect the water lines",
   "<p>Connect hot to the left valve and cold to the right. Most new faucets have attached lines with 3/8 in compression ends; tighten each nut hand-tight plus a quarter to half turn with a wrench, holding the valve body steady with a second wrench. Compression fittings don't need thread tape. For a pull-down, click the hose into the quick-connect and clip on the weight at the mark shown in the instructions.</p>"
   "<p><strong>Done right:</strong> no line is kinked, and the pull-down hose slides out and retracts smoothly.</p>"),
  step("Flush, test and check for leaks",
   "<p>Remove the aerator or spray head, open the valves slowly, and run water for a minute to flush out debris. Reinstall the aerator. Run hot and cold for a few minutes, then wipe each connection with a dry paper towel and check again an hour later.</p>"
   "<p><strong>Done right:</strong> the paper towel stays dry at every joint and the spray pattern is even.</p>"),
 ],
 "pro": "<strong>Call a plumber if:</strong> the shut-off valves are frozen or leaking, the supply pipes are corroded or soldered straight to the old faucet, or the sink is cracked around the faucet holes. A plumber can replace the valves in the same visit.",
 "faq": [
  ["How long does it take to replace a kitchen faucet?", "About 1.5 to 3 hours for a first-timer. Most of the time goes into loosening old mounting nuts in a tight space."],
  ["Do I need a basin wrench?", "Usually, yes. The mounting nuts sit behind the sink bowl where a normal wrench can't reach. A basin wrench costs about $15 to $25."],
  ["Can I install a single-hole faucet on a three-hole sink?", "Yes, if the faucet comes with or accepts a deck plate (escutcheon) that covers the extra holes."],
  ["Should I replace the supply lines?", "If the old lines are more than a few years old or are rigid copper, use new braided stainless lines. Many faucets now come with lines attached."],
 ],
},
{
 "blog": "bathroom", "blog_title": "Bathroom",
 "handle": "how-to-seal-grout",
 "title": "How to Seal Grout in a Shower or Bathroom Floor",
 "summary": "Seal tile grout to block stains and mildew: deep-clean the joints, let them dry, apply a penetrating sealer, wipe the excess and test with water.",
 "tags": ["Beginner", "Bathroom", "Tile", "Maintenance"],
 "difficulty": "Beginner", "time": "1–3 hours + cure time", "cost": "$15–$35",
 "tools": ["Stiff nylon grout brush", "Small foam brush or applicator-tip bottle", "Microfiber cloths", "Spray bottle", "Fan"],
 "materials": ["Penetrating grout sealer", "pH-neutral tile and grout cleaner", "Oxygen bleach (for stains)", "Painter's tape (optional)"],
 "video": "https://www.youtube.com/watch?v=Whnu6lmcPzI",
 "intro": "Cement grout is porous, so it soaks up soap, dirt and water, which leads to stains and mildew. A penetrating sealer fills those pores. This guide covers sanded and unsanded cement grout in showers, backsplashes and floors.",
 "safety": "<strong>Safety:</strong> run the bathroom fan and open a window. Wear nitrile gloves. Never mix bleach cleaners with ammonia or acidic cleaners.",
 "steps": [
  step("Check whether your grout needs sealing",
   "<p>Drip a few drops of water on several grout lines. If the grout darkens within a few minutes, it's absorbing water and needs sealer. If the water beads up, the existing sealer is still working. Epoxy and urethane grouts don't need sealing at all.</p>"
   "<p><strong>Done right:</strong> you know which areas absorb water, usually the shower floor and the lower walls.</p>"),
  step("Wait for new grout to cure",
   "<p>New grout needs to cure before sealing. Many grout makers say 48 to 72 hours; check your grout bag. On older grout, repair any cracked or crumbling joints first, because sealer doesn't fill gaps.</p>"
   "<p><strong>Done right:</strong> the grout is fully cured and every joint is intact.</p>"),
  step("Deep-clean the grout lines",
   "<p>Scrub the joints with a pH-neutral cleaner and a stiff nylon brush. For dark stains or mildew, use an oxygen bleach solution, let it sit 10 minutes, scrub, and rinse well with clean water. Sealing over dirt locks it in.</p>"
   "<p><strong>Done right:</strong> the grout is an even color with no gray film or spots.</p>"),
  step("Let it dry completely",
   "<p>Run the fan and don't use the shower for at least 24 hours, or as long as the sealer label says. Water trapped under the sealer can cause a cloudy look and weak protection.</p>"
   "<p><strong>Done right:</strong> the grout looks uniformly light and dry, with no darker damp patches.</p>"),
  step("Apply the sealer to the joints",
   "<p>Work in sections of a few square feet. Run an applicator-tip bottle or small foam brush along each grout line, putting the sealer on the grout rather than across the tile. Let it soak in for the time on the label, usually 5 to 15 minutes, then wipe any sealer off the tile faces with a clean microfiber cloth before it dries. Apply a second coat if the label calls for it.</p>"
   "<p><strong>Done right:</strong> there is no sticky or hazy film on the tile surface.</p>"),
  step("Let it cure and test",
   "<p>Keep water off for the full cure time on the label, often 24 to 72 hours. Then repeat the water-drop test on the same spots you tested at the start.</p>"
   "<p><strong>Done right:</strong> water beads up on the grout and wipes away without darkening it.</p>"),
 ],
 "pro": "<strong>Call a tile pro if:</strong> grout is cracked or missing in a shower, tiles sound hollow when tapped, or the wall behind the tile feels soft. Those point to water behind the tile, and sealer won't fix it.",
 "faq": [
  ["How often should you seal grout?", "It depends on use and the sealer, but many sealers last 1 to 3 years. Do the water-drop test every few months on the shower floor, which wears fastest."],
  ["Can you seal old grout?", "Yes, once it's deep-cleaned and fully dry. Repair cracked joints first."],
  ["Does grout sealer prevent mold?", "It slows it down by keeping water and soap out of the grout, but it doesn't make grout mold-proof. Good ventilation matters just as much."],
  ["What happens if sealer dries on the tile?", "It leaves a hazy film. Most manufacturers sell a remover, or you can rub it off with more sealer and a cloth while it's still fresh."],
 ],
},
{
 "blog": "flooring", "blog_title": "Flooring",
 "handle": "how-to-install-quarter-round",
 "title": "How to Install Quarter Round Molding",
 "summary": "Install quarter round to hide flooring gaps: measure, cope or miter the corners, nail it to the baseboard (not the floor), then fill, caulk and paint.",
 "tags": ["Beginner", "Flooring", "Trim", "Weekend project"],
 "difficulty": "Beginner", "time": "3–5 hours per room", "cost": "$40–$120 per room",
 "tools": ["Miter saw or miter box and saw", "Coping saw (for inside corners)", "18-gauge brad nailer or hammer and nail set", "Tape measure", "Pencil", "Utility knife", "Caulk gun"],
 "materials": ["Quarter round or shoe molding (room perimeter + 10%)", "1-1/4 in 18-gauge brad nails or finish nails", "Wood filler", "Paintable caulk", "Paint or stain to match"],
 "video": "https://www.youtube.com/watch?v=YrkdraLWlR0",
 "intro": "Quarter round covers the expansion gap between new flooring and the baseboard without pulling the baseboards off. This guide is for floating floors (vinyl plank, laminate) and nail-down hardwood alike.",
 "safety": "<strong>Safety:</strong> wear safety glasses when you cut and nail. Keep fingers well clear of the blade: quarter round is small, so clamp short pieces or cut them from a longer stick.",
 "steps": [
  step("Prime and paint the stock first",
   "<p>Paint or stain the full lengths before you cut them. It's far faster than painting along the floor afterward, and you'll only need touch-ups at the joints.</p>"
   "<p><strong>Done right:</strong> every stick is finished and dry before the first cut.</p>"),
  step("Measure each wall",
   "<p>Measure along the bottom of the baseboard from corner to corner. Mark whether each end is an inside corner, outside corner or a stop at a door casing. Cut pieces in order around the room so the grain and color match.</p>"
   "<p><strong>Done right:</strong> you have a list of lengths with corner types marked.</p>"),
  step("Cut the corners",
   "<p>For outside corners, cut both pieces at 45 degrees so they wrap the corner. For inside corners, run the first piece square into the corner, then cope the second: cut a 45-degree inside miter, then follow the profile line with a coping saw so it fits over the first piece. Where molding ends at a door casing, cut a small return or a 45-degree end.</p>"
   "<p><strong>Done right:</strong> dry-fit corners close tight with no visible gap.</p>"),
  step("Nail it to the baseboard, not the floor",
   "<p>Press the piece down lightly to the floor and against the baseboard. Nail every 12 to 16 in, angling the nail into the baseboard. On floating floors this matters: nailing into the floor pins it and stops it from expanding, which leads to buckling.</p>"
   "<p><strong>Done right:</strong> the molding sits tight to both surfaces, and no nail goes into the flooring.</p>",
   ),
  step("Fill, caulk and touch up",
   "<p>Fill nail holes with wood filler. Run a thin bead of paintable caulk along the top edge where it meets the baseboard, and at corner joints on painted trim. Touch up the paint once the caulk is dry. Don't caulk the bottom edge to a floating floor.</p>"
   "<p><strong>Done right:</strong> from standing height, you can't see nail holes or gaps.</p>"),
 ],
 "pro": "<strong>Hire a finish carpenter if:</strong> baseboards are badly out of plumb or walls are very wavy, so gaps open up along the whole run. A carpenter can scribe the trim to fit.",
 "faq": [
  ["Should quarter round be nailed to the floor or the baseboard?", "To the baseboard. Nailing into a floating floor stops it from expanding and contracting and can cause buckling."],
  ["Quarter round vs. shoe molding: what's the difference?", "Quarter round is a true quarter circle, usually 3/4 in. Shoe molding is taller than it is deep, so it covers the gap with a slimmer look."],
  ["Do you need to cope inside corners?", "A coped joint stays tight when the wood moves, so it's the better choice. A mitered inside corner works but tends to open up over time."],
  ["Can you glue quarter round instead of nailing?", "Yes, with construction adhesive or trim glue on the baseboard side only, which works well on tile or masonry baseboards."],
 ],
},
{
 "blog": "painting-walls", "blog_title": "Painting & Walls",
 "handle": "how-to-cut-in-paint",
 "title": "How to Cut In Paint Without Tape",
 "summary": "Cut in clean paint lines at ceilings and trim without tape: pick the right brush, load it correctly, and use the two-pass method pro painters use.",
 "tags": ["Beginner", "Painting & Walls", "Painting", "Technique"],
 "difficulty": "Beginner", "time": "30–60 minutes per room", "cost": "$15–$30",
 "tools": ["2 to 2-1/2 in angled sash brush", "Small paint pail or cup", "Damp rag", "Step ladder", "Good light (work light)"],
 "materials": ["Wall paint", "Paintable caulk (to fill gaps first)"],
 "video": "https://www.youtube.com/watch?v=Oiw9BY7_K9s",
 "intro": "Cutting in means brushing a clean band of paint along ceilings, corners and trim before you roll the wall. With the right brush and a steady two-pass method, you'll get straighter lines than tape gives you, and finish faster.",
 "safety": "",
 "steps": [
  step("Use the right brush and a small pail",
   "<p>Use a 2 to 2-1/2 in angled sash brush with soft, flagged bristles. Pour about an inch of paint into a small pail you can hold in one hand. Working from the gallon can overloads the brush.</p>"
   "<p><strong>Done right:</strong> you can carry the pail up the ladder and the paint is no deeper than about 1 in.</p>"),
  step("Load the brush correctly",
   "<p>Dip only the bottom third of the bristles, then tap both sides against the inside of the pail. Don't wipe it on the rim. The brush should be full but not dripping.</p>"
   "<p><strong>Done right:</strong> you can hold the brush sideways for a few seconds without a drip.</p>"),
  step("First pass: lay paint away from the line",
   "<p>Start about 1/2 in below the ceiling or away from the trim. Brush a few strokes to unload paint onto the wall in a band 2 to 3 in wide. This gets paint where you need it without risking the edge.</p>"
   "<p><strong>Done right:</strong> you have a wet band that stops just short of the edge.</p>"),
  step("Second pass: draw the line",
   "<p>With the brush now partly unloaded, place the long tip of the angled bristles about 1/8 in from the edge and press lightly so the bristles fan into a fine edge. Pull a long, steady stroke, moving your whole arm, not just your wrist. Let the bristle tips push the paint into the corner.</p>"
   "<p><strong>Done right:</strong> the line is straight and paint meets the edge without touching the ceiling or trim.</p>"),
  step("Feather the band and keep a wet edge",
   "<p>Lightly brush out the inner edge of the band so it doesn't leave a ridge. Cut in one wall, then roll it while the cut-in band is still wet, so the two blend without a visible frame.</p>"
   "<p><strong>Done right:</strong> after rolling, you can't see where the brushed band ends.</p>"),
  step("Fix slips right away",
   "<p>Wipe a slip off trim or ceiling immediately with a damp rag wrapped around a finger. On a textured ceiling, a quick wipe is better than touch-up paint later.</p>"
   "<p><strong>Done right:</strong> no paint is left on the trim or ceiling once the wall is dry.</p>"),
 ],
 "pro": "<strong>Consider a painter if:</strong> you have very high ceilings, stairwells or ornate trim. Working safely at height on a ladder or plank needs the right equipment.",
 "faq": [
  ["Is cutting in better than using painter's tape?", "With practice, yes. It's faster, and you avoid paint bleeding under the tape or peeling off when you remove it."],
  ["What is the best brush for cutting in?", "A 2 to 2-1/2 in angled sash brush. Nylon-polyester blends work well with latex paint."],
  ["Should I cut in before or after rolling?", "Before, one wall at a time, then roll while the cut-in is still wet so the two blend."],
  ["How many coats do I cut in?", "Cut in for each coat of wall paint, usually two."],
 ],
},
{
 "blog": "plumbing", "blog_title": "Plumbing Basics",
 "handle": "how-to-replace-a-toilet-fill-valve",
 "title": "How to Replace a Toilet Fill Valve",
 "summary": "Fix a toilet that runs, hisses or refills slowly by replacing the fill valve: drain the tank, swap the valve, set the height and adjust the water level.",
 "tags": ["Beginner", "Plumbing", "Toilet", "Repair"],
 "difficulty": "Beginner", "time": "30–60 minutes", "cost": "$10–$25",
 "tools": ["Adjustable wrench or channel-lock pliers", "Sponge", "Small bucket", "Towels"],
 "materials": ["Universal toilet fill valve", "New toilet supply line (if the old one is more than a few years old)"],
 "video": "https://www.youtube.com/watch?v=7d7uZYFu_ZA",
 "intro": "The fill valve is the tall part on the left side of the tank that refills it after a flush. When it hisses, keeps running or refills slowly, replacing it costs a few dollars and takes under an hour. Most universal fill valves fit standard two-piece toilets.",
 "safety": "",
 "steps": [
  step("Shut off the water and drain the tank",
   "<p>Turn the shut-off valve behind the toilet clockwise until it stops. Flush and hold the handle down to empty the tank, then sponge out the last inch of water into a bucket.</p>"
   "<p><strong>Done right:</strong> the tank is empty and doesn't refill.</p>"),
  step("Disconnect the supply line",
   "<p>Put a towel under the tank. Unscrew the supply line's nut from the bottom of the tank, where the fill valve's shank comes through. A little water will drip out.</p>"
   "<p><strong>Done right:</strong> the supply line is off and the towel catches the drips.</p>"),
  step("Remove the old fill valve",
   "<p>Under the tank, unscrew the plastic locknut that holds the fill valve. Pull the refill tube off the overflow tube and lift the old valve straight out.</p>"
   "<p><strong>Done right:</strong> the hole in the tank bottom is clean, with no old washer stuck to it.</p>"),
  step("Set the new valve's height",
   "<p>Adjust the new valve's height (most twist to lengthen or shorten) so its critical level mark, usually labeled CL, sits at least 1 in above the top of the overflow tube. This anti-siphon gap is required by plumbing code.</p>"
   "<p><strong>Done right:</strong> the CL mark is at least 1 in above the overflow tube, and the top of the valve clears the tank lid.</p>"),
  step("Install the new valve",
   "<p>Push the valve through the hole with its rubber washer inside the tank, then hand-tighten the locknut underneath, plus a quarter turn with pliers. Clip the refill tube to the overflow tube so its end points into the tube, not down inside it. Reconnect the supply line hand-tight plus a quarter turn.</p>"
   "<p><strong>Done right:</strong> the valve stands straight and doesn't rotate when you push on it.</p>"),
  step("Turn on the water and set the level",
   "<p>Open the shut-off valve slowly. Let the tank fill, then adjust the float (a clip or screw on the valve) so the water stops about 1/2 in below the top of the overflow tube, or at the waterline mark inside the tank. Flush a few times and check underneath for drips.</p>"
   "<p><strong>Done right:</strong> the tank refills quietly, stops at the right level, and the floor under the tank stays dry.</p>"),
 ],
 "pro": "<strong>Call a plumber if:</strong> the shut-off valve won't close or leaks, the tank is cracked, or water seeps from the bolts that hold the tank to the bowl after you've finished.",
 "faq": [
  ["How do I know if the fill valve is bad?", "Signs include hissing, a tank that refills on its own every so often, slow refilling, or water that keeps running into the overflow tube."],
  ["Are toilet fill valves universal?", "Most adjustable fill valves fit standard two-piece toilets. Some low-profile or one-piece toilets need the maker's own part."],
  ["What is the critical level on a fill valve?", "A mark (CL) on the valve that must sit at least 1 in above the overflow tube, so tank water can't siphon back into your drinking water."],
  ["Where should the water level be in a toilet tank?", "About 1/2 in below the top of the overflow tube, or at the waterline mark molded inside the tank."],
 ],
},
{
 "blog": "electrical", "blog_title": "Electrical Basics",
 "handle": "how-to-replace-an-outlet",
 "title": "How to Replace an Electrical Outlet Safely",
 "summary": "Replace a worn or broken outlet on an existing circuit: kill the power, verify it's dead, wire the new receptacle correctly and test it before you finish.",
 "tags": ["Intermediate", "Electrical", "Outlet", "Repair"],
 "difficulty": "Intermediate", "time": "20–45 minutes", "cost": "$3–$30",
 "tools": ["Non-contact voltage tester", "Plug-in outlet tester", "Insulated screwdrivers (flat and #2 Phillips)", "Wire stripper", "Needle-nose pliers", "Phone camera"],
 "materials": ["New receptacle matching the old rating (15 A or 20 A)", "Tamper-resistant receptacle where required", "Wire nuts and pigtail wire (if needed)", "Cover plate"],
 "video": "https://www.youtube.com/watch?v=WC7F-Ag9fXQ",
 "intro": "A loose, cracked or scorched outlet should be replaced, not taped. This guide covers swapping a standard three-prong receptacle on an existing grounded circuit. It doesn't cover adding new outlets or circuits, which typically needs a permit and an electrician.",
 "safety": "<strong>Safety:</strong> switch off the breaker for the outlet and confirm it's dead with a non-contact tester on every wire in the box, not just one slot. Stop if you find aluminum wiring (dull silver wire), cloth-covered wiring that crumbles, or scorch marks on the wires. Many areas allow homeowners to replace devices, but check your local rules.",
 "steps": [
  step("Turn off the power and confirm it's off",
   "<p>Plug a lamp or outlet tester into the outlet, then switch off breakers until it goes dead. Remove the cover plate and the two device screws, and pull the outlet out gently. Touch a non-contact voltage tester to every wire in the box, because a box can hold wires from a second circuit.</p>"
   "<p><strong>Done right:</strong> the tester stays silent on every wire, and you've confirmed the tester works on a known live outlet.</p>"),
  step("Photograph and note the wiring",
   "<p>Take a clear photo of which wire goes to which screw. Black (hot) wires go to the brass screws, white (neutral) to the silver screws, and bare or green (ground) to the green screw. If two sets of wires connect to the outlet, it is passing power downstream to other outlets.</p>"
   "<p><strong>Done right:</strong> you have a photo showing every connection.</p>"),
  step("Choose the right replacement",
   "<p>Match the amp rating stamped on the old outlet (15 A or 20 A). Under current electrical code, a replacement outlet must meet today's rules for that location: GFCI protection in kitchens, bathrooms, laundry areas, garages and outdoors, and tamper-resistant receptacles in most living spaces. Buy the right type before you open the wall.</p>"
   "<p><strong>Done right:</strong> the new outlet matches the old rating and the location's requirements.</p>"),
  step("Wire the new outlet",
   "<p>Loosen the wires from the old outlet. Use the side screws, not the push-in holes on the back: bend each wire into a hook, wrap it clockwise around its screw, and tighten firmly. Connect the ground wire to the green screw. If there are two wires per terminal, use the second set of screws or join them with a short pigtail under a wire nut.</p>"
   "<p><strong>Done right:</strong> no bare copper shows beyond the screws, and each wire is tight when you tug it.</p>"),
  step("Mount the outlet and test it",
   "<p>Fold the wires neatly into the box, screw the outlet in straight, and attach the cover plate. Turn the breaker on and plug in an outlet tester.</p>"
   "<p><strong>Done right:</strong> the tester shows the \"correct\" pattern, and the cover plate sits flat and isn't cracked.</p>"),
 ],
 "pro": "<strong>Call a licensed electrician if:</strong> the box has no ground wire, you find aluminum or crumbling old wiring, wires are scorched or melted, the breaker trips again, or you want to add an outlet or move one. Two-prong outlets on ungrounded circuits have specific code options an electrician should handle.",
 "faq": [
  ["Can I replace an outlet myself?", "In many U.S. areas homeowners may replace an outlet like-for-like on their own home, but rules vary. Check with your local building department."],
  ["Do I need a 15 A or 20 A outlet?", "Match the old outlet's rating. A 20 A outlet has a sideways T-shaped slot. Never install a 20 A outlet on a circuit with a 15 A breaker."],
  ["Should I use the push-in holes on the back of the outlet?", "It's better to use the side screws. Push-in (backstab) connections loosen over time and are a common cause of outlets that stop working."],
  ["Why does my new outlet not work?", "Check the breaker, then any GFCI outlet upstream that may have tripped. If it still doesn't work, turn the power off and check that every wire is tight."],
 ],
},
{
 "blog": "doors-windows", "blog_title": "Doors & Windows",
 "handle": "how-to-replace-a-door-knob",
 "title": "How to Replace a Door Knob (Interior or Exterior)",
 "summary": "Replace an interior or exterior door knob in about 15 minutes: pick the right function and backset, swap the latch, and align it with the strike plate.",
 "tags": ["Beginner", "Doors & Windows", "Hardware", "Quick fix"],
 "difficulty": "Beginner", "time": "15–30 minutes", "cost": "$15–$60",
 "tools": ["#2 Phillips screwdriver (long shank)", "Flathead screwdriver or small pick", "Tape measure", "Chisel (only if the latch plate doesn't fit)"],
 "materials": ["New door knob or lever set", "Wood glue and toothpicks (for stripped screw holes)"],
 "video": "https://www.youtube.com/watch?v=vGZ2GUi02G0",
 "intro": "A sticky, loose or dated door knob is a quick swap with one screwdriver. Most new knobs fit standard U.S. door holes. This guide covers passage, privacy and keyed knobs and levers.",
 "safety": "",
 "steps": [
  step("Pick the right function and measure the backset",
   "<p>Choose the function: <strong>passage</strong> (no lock, for halls and closets), <strong>privacy</strong> (push-button lock, for bedrooms and baths) or <strong>keyed entry</strong> (exterior doors). Measure from the door edge to the center of the knob hole. That's the backset, usually 2-3/8 in or 2-3/4 in; most new latches adjust to both.</p>"
   "<p><strong>Done right:</strong> the box lists your function and backset, and the hole in the door is the standard 2-1/8 in.</p>"),
  step("Remove the old knob",
   "<p>On the inside knob, look for two screws on the rose (round plate). Remove them and pull both knobs apart. If you see no screws, find a small slot or hole on the knob's neck, press it with a small screwdriver, and slide the knob off; the rose then pops or twists off to reveal the screws.</p>"
   "<p><strong>Done right:</strong> both knobs are off and only the latch remains in the door edge.</p>"),
  step("Swap the latch",
   "<p>Remove the two screws on the door edge and pull out the old latch. Set the new latch to your backset, then slide it in with the angled side of the bolt facing the direction the door closes. Screw it in flush with the door edge.</p>"
   "<p><strong>Done right:</strong> the latch plate sits flush, and the slanted bolt faces the door frame when you close the door.</p>"),
  step("Install the new knobs",
   "<p>Slide the exterior (or keyed) knob in from the outside so its spindle passes through the latch. Line up the interior knob on the other side and drive in the two long screws, alternating so the knobs pull together evenly. Snug them, but don't overtighten or the knob will bind.</p>"
   "<p><strong>Done right:</strong> both knobs turn smoothly and the latch snaps back on its own when released.</p>"),
  step("Test the latch and adjust the strike",
   "<p>Close the door gently. The latch should click into the strike plate on the frame without you pushing. If it catches, loosen the strike plate and shift it up or down, or file the opening slightly. Fill stripped screw holes with glue-dipped toothpicks and redrive the screws.</p>"
   "<p><strong>Done right:</strong> the door latches with a light push and doesn't rattle when closed.</p>"),
 ],
 "pro": "<strong>Call a locksmith or carpenter if:</strong> the door has a non-standard bore, a mortise lock (a large rectangular lock body inside the door), or the door has sagged so much that the latch misses the strike by more than 1/4 in.",
 "faq": [
  ["Are door knobs universal?", "Most U.S. knobs fit a standard 2-1/8 in bore hole with a 2-3/8 or 2-3/4 in backset. Older or European doors may differ."],
  ["How do I remove a door knob with no visible screws?", "Find the small slot or pinhole on the knob's neck, press it with a small screwdriver or pick, and pull the knob off. The rose then comes off to reveal the screws."],
  ["Which way does the latch go?", "The slanted side of the latch bolt faces the direction the door closes, so it slides along the strike plate."],
  ["Can I replace a knob with a lever?", "Yes, levers fit the same standard holes, and they're easier for kids, older adults and anyone carrying something."],
 ],
},
{
 "blog": "outdoor-garden", "blog_title": "Outdoor & Garden",
 "handle": "how-to-seal-a-deck",
 "title": "How to Clean and Seal a Wood Deck",
 "summary": "Clean, brighten and seal a wood deck so it repels water: test the old finish, wash gently, let it dry, and apply thin coats in the right weather.",
 "tags": ["Intermediate", "Outdoor & Garden", "Deck", "Weekend project"],
 "difficulty": "Intermediate", "time": "2 days (cleaning, drying, sealing)", "cost": "$80–$250",
 "tools": ["Stiff deck brush on a pole", "Garden hose with spray nozzle (or pressure washer with a 25–40° tip)", "Pump sprayer", "Stain pad applicator or roller", "Natural or synthetic stain brush", "Painter's tape and plastic sheeting"],
 "materials": ["Oxygen-based deck cleaner", "Wood brightener (oxalic acid type)", "Exterior deck sealer or semi-transparent stain", "Exterior screws (to replace popped nails)"],
 "video": "https://www.youtube.com/watch?v=Endync6z3XM",
 "intro": "Sealing keeps water out of the wood, which slows cracking, rot and graying. Done every couple of years, it keeps a deck looking good for much longer. This guide covers pressure-treated, cedar and redwood decks with a clear sealer or semi-transparent stain.",
 "safety": "<strong>Safety:</strong> wear eye protection and gloves when using cleaners and brighteners. Pressure washers can cut skin and gouge wood; keep the tip moving and at least 12 in from the surface. Oil-based finish rags can catch fire on their own: lay them flat to dry outdoors or soak them in water before disposal.",
 "steps": [
  step("Test whether the deck needs sealing",
   "<p>Sprinkle water on a few boards in sunny and shaded spots. If it soaks in within a few minutes and darkens the wood, it's time to seal. If it beads, the old finish still works. Brand-new pressure-treated wood often needs to dry for weeks or months first; check the lumber tag and the sealer label.</p>"
   "<p><strong>Done right:</strong> you know the deck is absorbing water and the wood is dry enough to take a finish.</p>"),
  step("Make repairs and protect the area",
   "<p>Drive down or replace popped nails with exterior screws, and replace any soft boards. Sweep the deck and clear the gaps between boards with a putty knife. Cover plants with plastic sheeting and tape off siding where the deck meets the house.</p>"
   "<p><strong>Done right:</strong> no nail heads stick up and the gaps are clear.</p>"),
  step("Clean the wood",
   "<p>Wet the deck, apply an oxygen-based deck cleaner with a pump sprayer, and let it work for the time on the label. Scrub with a deck brush along the grain, then rinse thoroughly with a hose. If you use a pressure washer, use low pressure and a wide fan tip, keep it moving with the grain, and stay at least 12 in away.</p>"
   "<p><strong>Done right:</strong> the wood is an even color, with no gray film or furry, raised fibers.</p>"),
  step("Brighten and let the deck dry",
   "<p>Apply a wood brightener to neutralize the cleaner and bring back the wood's color, then rinse. Let the deck dry for at least 48 hours of dry weather, or as long as the sealer label says.</p>"
   "<p><strong>Done right:</strong> the wood looks uniformly light and feels dry to the touch, even in the shaded areas.</p>"),
  step("Apply a thin coat in the right weather",
   "<p>Pick a dry, mild day: most finishes want temperatures roughly between 50 and 90°F and no rain for at least 24 hours. Stir the finish (don't shake it). Coat two or three boards at a time along their full length with a pad or roller, then back-brush to work it in. Do railings and stair treads first, then the floor, working toward the exit.</p>"
   "<p><strong>Done right:</strong> the finish soaks in evenly with no puddles, drips or shiny spots after 15 minutes.</p>"),
  step("Wipe the excess and let it cure",
   "<p>Wipe up any finish that hasn't soaked in after the time on the label, because puddles turn sticky. Apply a second coat only if the product calls for it. Keep foot traffic off for about a day and furniture off for the time on the can.</p>"
   "<p><strong>Done right:</strong> the deck is dry to the touch with no tacky spots, and water beads on it.</p>"),
 ],
 "pro": "<strong>Call a deck contractor if:</strong> you find soft or rotted joists, posts or ledger board (where the deck attaches to the house), loose railings, or rusted structural hardware. Those are safety issues that sealing won't fix.",
 "faq": [
  ["How often should you seal a deck?", "Typically every 1 to 3 years, depending on the product, sun exposure and foot traffic. Use the water test each spring."],
  ["What's the difference between deck sealer and stain?", "A clear sealer protects against water but not much against UV graying. A semi-transparent or solid stain adds pigment that blocks UV, so it usually lasts longer on sunny decks."],
  ["Can I seal a new pressure-treated deck right away?", "Usually not. The wood needs to dry first, often for several weeks or months. Do the water test and follow the lumber and sealer labels."],
  ["Should I pressure wash my deck?", "Only on low pressure with a wide tip, held at least 12 in away. A deck cleaner and a scrub brush work well and are gentler on the wood."],
 ],
},
{
 "blog": "storage", "blog_title": "Storage & Organization",
 "handle": "how-to-install-a-closet-shelf-and-rod",
 "title": "How to Install a Closet Shelf and Rod",
 "summary": "Install a sturdy closet shelf and hanging rod: set the right heights, screw cleats into studs, add a center bracket for long spans, and level everything.",
 "tags": ["Beginner", "Storage & Organization", "Closet", "Weekend project"],
 "difficulty": "Beginner", "time": "2–3 hours", "cost": "$40–$100",
 "tools": ["Stud finder", "4 ft level", "Tape measure", "Drill/driver with bits", "Circular saw or miter saw (or have the store cut boards)", "Pencil"],
 "materials": ["1x4 boards for cleats", "3/4 in plywood, MDF or 1x12 board for the shelf", "1-5/16 in closet rod (wood or metal)", "Closet rod sockets (2)", "Shelf-and-rod support bracket (1 per 4 ft of span)", "2-1/2 in wood screws", "1-1/4 in screws"],
 "video": "https://www.youtube.com/watch?v=MdcgsWb-S_c",
 "intro": "A wood shelf and rod on cleats screwed into studs holds far more than wire shelving clipped into drywall. This guide covers a standard reach-in closet with a single shelf and one hanging rod.",
 "safety": "<strong>Safety:</strong> wear safety glasses when cutting and drilling. Check for wires and pipes before you drill: outlets, switches and plumbing on the other side of the wall are clues.",
 "steps": [
  step("Mark the heights",
   "<p>For a single rod, a common layout puts the rod about 66 in off the floor and the shelf just above it, around 68 to 70 in. Draw a level line at the shelf height on the back wall and both side walls. Mark the stud locations on the back wall with a stud finder.</p>"
   "<p><strong>Done right:</strong> a level line runs around the three walls and studs are marked on the back wall.</p>"),
  step("Install the cleats",
   "<p>Cut 1x4 cleats to fit the back wall and both side walls. Hold their top edge on your line and screw them into each stud with two 2-1/2 in screws. On side walls without studs at the right spot, use heavy-duty drywall anchors rated for the load.</p>"
   "<p><strong>Done right:</strong> the cleats don't move when you pull down on them hard.</p>"),
  step("Mount the rod sockets",
   "<p>Screw a closet rod socket to each side cleat, centered about 12 in out from the back wall. That distance lets hangers swing freely.</p>"
   "<p><strong>Done right:</strong> both sockets are at the same height and the same distance from the back wall.</p>"),
  step("Add a center support for long spans",
   "<p>If the rod spans more than about 4 ft, add a shelf-and-rod bracket into a stud near the middle. Without it, the rod and shelf will sag under the weight of clothes.</p>"
   "<p><strong>Done right:</strong> no part of the rod spans more than about 4 ft without support.</p>"),
  step("Set the shelf and rod",
   "<p>Cut the shelf to the closet width, 1/8 in short so it drops in easily. Rest it on the cleats and bracket, and drive 1-1/4 in screws down through it into the cleats. Cut the rod to length and drop it into the sockets and bracket.</p>"
   "<p><strong>Done right:</strong> the shelf is level and the rod doesn't rattle in its sockets.</p>"),
 ],
 "pro": "<strong>Hire a carpenter or closet company if:</strong> you want a full custom system with drawers and towers, or the walls are plaster over lath where finding studs and drilling is harder.",
 "faq": [
  ["How high should a closet rod be?", "About 66 in for a single rod. For a double-hang closet, about 80 to 84 in for the top rod and 40 to 42 in for the bottom rod."],
  ["How far should a closet rod be from the back wall?", "About 12 in from the back wall to the center of the rod, so hangers don't hit the wall."],
  ["How long can a closet rod span without support?", "Plan for a support bracket about every 4 ft. Longer spans sag with a full load of clothes."],
  ["Wood or wire closet shelving?", "Wood or plywood shelves on stud-mounted cleats are stronger and don't leave marks on folded clothes. Wire is cheaper and lets air circulate."],
 ],
},
{
 "blog": "maintenance", "blog_title": "Home Maintenance",
 "handle": "how-to-clean-a-dryer-vent",
 "title": "How to Clean a Dryer Vent (and Prevent Fires)",
 "summary": "Clean your dryer vent to dry clothes faster and cut fire risk: disconnect the duct, brush the lint out from both ends, and check the outside flap.",
 "tags": ["Beginner", "Home Maintenance", "Laundry", "Safety"],
 "difficulty": "Beginner", "time": "1–2 hours", "cost": "$20–$40",
 "tools": ["Dryer vent brush kit with extension rods", "Vacuum with hose attachment", "Screwdriver or nut driver", "Flashlight", "Work gloves"],
 "materials": ["Foil tape (UL 181 rated) for duct joints", "Replacement semi-rigid or rigid metal duct (if needed)", "Hose clamps (if needed)"],
 "video": "https://www.youtube.com/watch?v=hWdj3-OvVEc",
 "intro": "Lint that builds up in the dryer duct slows drying and is a leading cause of dryer fires. Cleaning the full vent run once a year takes about an hour. This guide covers electric and gas dryers venting to the outside.",
 "safety": "<strong>Safety:</strong> unplug an electric dryer before you pull it out. For a gas dryer, close the gas valve behind it before moving it, and be careful not to kink or strain the flexible gas line. If you smell gas after you're done, leave the house and call your gas utility.",
 "steps": [
  step("Spot the warning signs",
   "<p>Clean the vent now if clothes need more than one cycle to dry, the dryer or laundry room gets very hot, you smell burning, or the outside flap barely opens when the dryer runs. Otherwise, plan to clean it at least once a year.</p>"
   "<p><strong>Done right:</strong> you've noted how long a normal load takes to dry, so you can compare after cleaning.</p>"),
  step("Pull the dryer out and disconnect the duct",
   "<p>Unplug the dryer (and close the gas valve for a gas dryer). Slide it away from the wall slowly. Loosen the clamp and pull the duct off the dryer's exhaust outlet and off the wall connection.</p>"
   "<p><strong>Done right:</strong> the duct is off at both ends and the power is disconnected.</p>"),
  step("Clean the lint screen housing and dryer outlet",
   "<p>Remove the lint screen and vacuum the slot it sits in. Then vacuum the exhaust outlet on the back of the dryer as far as the hose reaches.</p>"
   "<p><strong>Done right:</strong> no lint is visible in the screen slot or the exhaust outlet.</p>"),
  step("Brush the vent run from inside and outside",
   "<p>Feed the vent brush into the wall duct, adding rods as you go and turning it clockwise (counterclockwise can unscrew the rods). Work it back and forth, then pull it out with the lint. Repeat from the outside vent hood. Vacuum up what comes out.</p>"
   "<p><strong>Done right:</strong> the brush comes out clean on the last pass and you can see daylight or feel airflow through the duct.</p>"),
  step("Check the duct and the outside hood",
   "<p>Replace any plastic or thin foil duct with rigid or semi-rigid metal duct, which is what dryer makers and building codes call for. Keep the run as short and straight as possible. Make sure the outside flap opens freely and has no screen, because screens trap lint.</p>"
   "<p><strong>Done right:</strong> the duct is metal with no crushed sections, and the outside flap swings freely.</p>"),
  step("Reconnect and test",
   "<p>Reattach the duct to the wall and dryer with clamps, and seal joints with foil tape, not screws (screws catch lint). Push the dryer back without crushing the duct. Plug it in (open the gas valve), run it on high heat, and check that air blows strongly out of the outside hood.</p>"
   "<p><strong>Done right:</strong> the outside flap opens wide and a normal load dries in one cycle.</p>"),
 ],
 "pro": "<strong>Call a dryer vent cleaning pro if:</strong> the vent runs a long way through the attic or roof, the duct is crushed inside a wall, a bird or rodent nest blocks it, or airflow is still weak after cleaning.",
 "faq": [
  ["How often should you clean a dryer vent?", "At least once a year, and more often for large households or long vent runs. Clean the lint screen before every load."],
  ["What are signs of a clogged dryer vent?", "Clothes take longer than one cycle to dry, the dryer gets very hot, a burning smell, or a weak flow of air at the outside vent."],
  ["Can I use a leaf blower to clean a dryer vent?", "Some people do, but a brush kit is more thorough and doesn't risk blowing lint into the laundry room. Disconnect the duct either way."],
  ["What kind of dryer duct should I use?", "Rigid or semi-rigid metal duct. Plastic and thin foil accordion ducts crush easily, trap lint and aren't allowed by most dryer makers or building codes."],
 ],
},
]

AFFILIATE_B4A = {
 "how-to-replace-a-kitchen-faucet": ["basin wrench"],
 "how-to-seal-grout": ["applicator-tip bottle"],
 "how-to-install-quarter-round": ["coping saw"],
 "how-to-cut-in-paint": ["angled sash brush"],
 "how-to-replace-an-outlet": ["outlet tester"],
 "how-to-seal-a-deck": ["oxygen-based deck cleaner"],
 "how-to-install-a-closet-shelf-and-rod": ["shelf-and-rod bracket"],
 "how-to-clean-a-dryer-vent": ["vent brush"],
}
