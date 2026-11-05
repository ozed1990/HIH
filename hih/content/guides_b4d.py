"""Batch 4D: paint kitchen cabinets, replace a vanity, basement flooring, remove wallpaper,
fix a leaky faucet cartridge, smart switch, smart lock, replace a deck board, French cleat wall,
spring maintenance checklist."""

def step(title, body, fig=None):
    return {"title": title, "body": body, "fig": fig}

GUIDES_B4D = [
{
 "blog": "kitchen", "blog_title": "Kitchen",
 "handle": "how-to-paint-kitchen-cabinets",
 "title": "How to Paint Kitchen Cabinets That Last",
 "summary": "Paint kitchen cabinets with a hard, smooth finish: label and remove doors, degrease, scuff-sand, apply a bonding primer, then thin coats of enamel.",
 "tags": ["Intermediate", "Kitchen", "Cabinets", "Painting"],
 "difficulty": "Intermediate", "time": "3–5 days (including drying)", "cost": "$150–$400",
 "tools": ["Screwdriver or drill", "Painter's tape and marker (for labels)", "Sanding sponges (180 and 220 grit)", "Tack cloth or microfiber", "2 in angled brush", "4 in foam or microfiber mini roller", "Drying racks or painter's pyramids", "Vacuum"],
 "materials": ["Degreasing cleaner (TSP substitute)", "Bonding primer", "Cabinet and trim enamel (waterborne alkyd or urethane-modified acrylic)", "Wood filler", "Paintable caulk", "Cabinet door bumpers"],
 "video": "https://www.youtube.com/watch?v=ZY4634tikUY",
 "intro": "Painted cabinets can transform a kitchen for a fraction of the cost of new ones, but they get handled every day, so prep and paint choice decide how long they last. This guide covers wood and MDF cabinets with a factory or old painted finish.",
 "safety": "<strong>Safety:</strong> wear a dust mask while sanding and ventilate while priming and painting. If your home was built before 1978 and the cabinets have old paint, test for lead before sanding.",
 "steps": [
  step("Label and remove doors, drawers and hardware",
   "<p>Number each door and its cabinet opening with tape before you take anything off. Remove doors, hinges, drawer fronts and pulls, and keep each set of screws in a labeled bag.</p>"
   "<p><strong>Done right:</strong> every door and drawer has a number that matches its opening, and no hardware is loose.</p>"),
  step("Degrease every surface",
   "<p>Kitchen cabinets carry a film of cooking grease, especially near the stove. Scrub all surfaces with a degreasing cleaner, rinse with clean water and let them dry. Paint won't bond to grease.</p>"
   "<p><strong>Done right:</strong> the surfaces feel squeaky clean, not tacky.</p>"),
  step("Repair, scuff-sand and clean the dust",
   "<p>Fill dents and old hardware holes you won't reuse with wood filler. Scuff-sand everything with a 180 to 220 grit sponge to dull the existing finish; you don't need to sand to bare wood. Vacuum, then wipe with a tack cloth or damp microfiber.</p>"
   "<p><strong>Done right:</strong> the old finish is dull all over and no dust comes off on a dark cloth.</p>"),
  step("Prime with a bonding primer",
   "<p>Apply a thin, even coat of <strong>bonding primer</strong> made for glossy surfaces. Brush the profiles first, then roll the flat panels. Lay doors flat on racks and do the backs first, then the fronts. Lightly sand any rough spots once it's dry.</p>"
   "<p><strong>Done right:</strong> the primer coat is even, with no bare spots, drips or puddles in corners.</p>"),
  step("Apply two thin coats of enamel",
   "<p>Use a cabinet and trim enamel, which levels out brush marks and dries hard. Brush the recessed edges, roll the flat areas, and finish each panel with light strokes in one direction. Respect the recoat time on the can. Apply a second coat after a light sanding with 220 grit.</p>"
   "<p><strong>Done right:</strong> the finish is smooth and even, with no brush ridges you can feel.</p>"),
  step("Let it cure before heavy use",
   "<p>Rehang doors once they're dry to the touch and the can's recoat time has passed, and add small bumpers so doors don't stick to the frames. Most enamels take several weeks to fully cure: open and close doors gently and avoid scrubbing until then.</p>"
   "<p><strong>Done right:</strong> doors close without sticking and the finish doesn't show fingernail marks.</p>"),
 ],
 "pro": "<strong>Hire a cabinet painter if:</strong> you want a sprayed factory-smooth finish, the cabinets are laminate or thermofoil that's peeling, or you can't be without a working kitchen for a week.",
 "faq": [
  ["Do I need to sand cabinets before painting?", "A scuff-sand to dull the old finish is enough when you use a bonding primer. Sanding to bare wood isn't necessary."],
  ["What paint is best for kitchen cabinets?", "A cabinet and trim enamel, such as a waterborne alkyd or urethane-modified acrylic, which levels well and dries hard."],
  ["Should I paint cabinet doors on or off?", "Off. Painting doors flat gives a smoother finish, lets you do both sides, and avoids paint in the hinges."],
  ["How long does painted cabinet finish take to cure?", "It's dry to handle within a day, but most enamels take several weeks to reach full hardness. Be gentle until then."],
 ],
},
{
 "blog": "bathroom", "blog_title": "Bathroom",
 "handle": "how-to-replace-a-bathroom-vanity",
 "title": "How to Replace a Bathroom Vanity",
 "summary": "Replace a bathroom vanity yourself: measure plumbing, shut off water, remove the old unit, level and secure the new cabinet, then reconnect and seal.",
 "tags": ["Intermediate", "Bathroom", "Plumbing", "Weekend project"],
 "difficulty": "Intermediate", "time": "4–8 hours", "cost": "$250–$1,200 (vanity) + $30 parts",
 "tools": ["Adjustable wrenches (2)", "Channel-lock pliers", "Utility knife", "Pry bar", "Drill/driver", "Stud finder", "4 ft level", "Jigsaw or hole saw", "Bucket and towels"],
 "materials": ["New vanity cabinet and top", "Faucet (if not included)", "Two braided supply lines", "P-trap kit and tailpiece", "Wood shims", "2-1/2 in cabinet screws", "Silicone caulk", "Construction adhesive or silicone for the top (per maker)"],
 "video": "https://www.youtube.com/watch?v=Oq1pkZD7DGo",
 "intro": "A new vanity is one of the biggest visual upgrades in a bathroom, and with the plumbing already in place it's a weekend job. This guide covers swapping a freestanding vanity for one of similar size on existing supply and drain lines.",
 "safety": "<strong>Safety:</strong> vanity tops, especially stone, are heavy; lift with a helper. Wear eye protection when cutting and prying. Check for wires in the wall before driving screws.",
 "steps": [
  step("Measure before you buy",
   "<p>Measure the width, depth and height you have, plus the positions of the water lines and drain from the floor and from the side wall. Check that the new cabinet's open back or cutouts line up with them. Note door swing and toilet clearance; many codes call for at least 15 in from the toilet's center to the vanity side.</p>"
   "<p><strong>Done right:</strong> the new vanity fits the space and its back clears the pipes.</p>"),
  step("Disconnect the old vanity",
   "<p>Close the shut-off valves and open the faucet to relieve pressure. Disconnect the supply lines at the valves and loosen the P-trap slip nuts over a bucket. Stuff a rag in the drain arm to block sewer gas.</p>"
   "<p><strong>Done right:</strong> the valves are closed and dry, and the drain is plugged with a rag.</p>"),
  step("Remove the top and cabinet",
   "<p>Cut the caulk between the top and the wall with a utility knife, and lift the top off with a helper. Find and remove the screws holding the cabinet to the wall, then pull it out. Check the floor and wall for soft spots or water damage.</p>"
   "<p><strong>Done right:</strong> the space is clear, and the floor and wall are solid and dry.</p>"),
  step("Set and level the new cabinet",
   "<p>Mark the studs. If the cabinet has a solid back, cut holes for the pipes with a hole saw or jigsaw. Slide the cabinet in, shim it level front to back and side to side, and screw it to at least two studs through its back rail.</p>"
   "<p><strong>Done right:</strong> the level reads true in both directions and the cabinet doesn't rock.</p>"),
  step("Install the faucet and top",
   "<p>Mount the faucet and drain assembly on the top while it's on a table; it's much easier than working under the sink. Apply adhesive or silicone to the cabinet's top edges as the maker says, then lower the top in place with a helper.</p>"
   "<p><strong>Done right:</strong> the top sits flat with an even overhang and doesn't shift.</p>"),
  step("Reconnect, test and caulk",
   "<p>Connect new supply lines from the valves to the faucet, and assemble the P-trap. Open the valves slowly, run water hot and cold, fill and drain the sink, and check every joint with a paper towel. Run a bead of silicone where the top meets the wall.</p>"
   "<p><strong>Done right:</strong> every joint stays dry after several fills, and the backsplash joint is sealed.</p>"),
 ],
 "pro": "<strong>Call a plumber if:</strong> the shut-off valves won't close, the new vanity needs the drain or supply lines moved, or you find rot or mold in the floor or wall. Moving plumbing usually needs a permit.",
 "faq": [
  ["Can I replace a vanity without a plumber?", "Yes, if the new one fits the existing water and drain lines. If the pipes need moving, hire a plumber."],
  ["How do I attach a vanity to the wall?", "Screw through the cabinet's back rail into at least two studs, after leveling it with shims."],
  ["Do I need new supply lines?", "It's a good idea. Braided stainless lines are inexpensive and much less likely to fail than old ones."],
  ["How much clearance does a vanity need from a toilet?", "Many codes require at least 15 in from the toilet's centerline to the side of the vanity. Check your local code."],
 ],
},
{
 "blog": "flooring", "blog_title": "Flooring",
 "handle": "best-flooring-for-basement",
 "title": "Best Flooring for a Basement: How to Choose",
 "summary": "Choose the right basement flooring: test for moisture, check flatness, compare vinyl plank, tile, carpet tile and laminate, and plan the subfloor.",
 "tags": ["Beginner", "Flooring", "Basement", "Buying guide"],
 "difficulty": "Beginner", "time": "1–3 days for testing and planning", "cost": "$2–$10 per sq ft (materials)",
 "tools": ["Clear plastic sheeting (2 x 2 ft)", "Duct tape", "6 ft straightedge or level", "Tape measure", "Moisture meter (optional)"],
 "materials": ["Floor samples", "Underlayment with vapor barrier (as the floor requires)", "Floor patch or self-leveler (if needed)"],
 "video": "https://www.youtube.com/watch?v=Nch1DwAlTZ8",
 "intro": "Basements are damp, cool and built on concrete, so the floor that works upstairs can fail down here. This guide walks you through testing the slab and picking a floor that handles moisture, before you buy anything.",
 "safety": "<strong>Safety:</strong> if the basement has a musty smell, visible mold or standing water, fix the moisture problem before any new floor goes in.",
 "steps": [
  step("Test the slab for moisture",
   "<p>Tape a 2 x 2 ft square of clear plastic sheeting tightly to the bare concrete on all four sides and leave it for 24 to 72 hours. Moisture droplets under the plastic mean water is coming up through the slab; a damp top means humid air.</p>"
   "<p><strong>Done right:</strong> you know whether the slab, the air, or neither is the moisture source.</p>"),
  step("Check that the floor is flat",
   "<p>Lay a 6 ft straightedge across the slab in several directions and look for gaps. Many click floors allow only about 3/16 in of variation over 10 ft; check your product's spec. Grind high spots and fill low spots with floor patch.</p>"
   "<p><strong>Done right:</strong> the slab meets your chosen floor's flatness spec everywhere.</p>"),
  step("Compare the main options",
   "<p><strong>Rigid-core vinyl plank (SPC/WPC):</strong> waterproof, warm-looking, and the most popular choice. <strong>Porcelain tile:</strong> unaffected by water and very durable, but cold and hard underfoot. <strong>Carpet tiles:</strong> warm and replaceable one square at a time if a section gets wet. <strong>Waterproof laminate:</strong> scratch-resistant but check the water rating carefully. Avoid solid hardwood below grade.</p>"
   "<p><strong>Done right:</strong> you've narrowed it to one or two types that suit your moisture test results.</p>"),
  step("Plan the underlayment and subfloor",
   "<p>Follow the flooring maker's rules for concrete: most floating floors need a vapor barrier underlayment, and some include one. A raised subfloor panel system can add warmth and an air gap on a cold slab, but it raises the floor height.</p>"
   "<p><strong>Done right:</strong> you know which underlayment the warranty requires and how much the floor height will rise.</p>"),
  step("Check heights at stairs and doors",
   "<p>Measure how the new floor height affects the bottom stair riser, door clearances and transitions to other rooms. Stair risers should stay within code limits, typically no more than 3/8 in difference between risers.</p>"
   "<p><strong>Done right:</strong> doors still swing freely and the bottom step stays within code once the floor is in.</p>"),
 ],
 "pro": "<strong>Call a waterproofing contractor if:</strong> the plastic test shows water coming through the slab, walls weep after rain, or the basement has flooded before. Fix drainage and waterproofing first, then choose the floor.",
 "faq": [
  ["What is the best flooring for a basement?", "For most basements, rigid-core luxury vinyl plank is the best balance of waterproofing, comfort, looks and price. Porcelain tile is the most moisture-proof."],
  ["Can you put laminate flooring in a basement?", "Only waterproof-rated laminate, with the vapor barrier the maker requires, and only in a basement with no water coming up through the slab."],
  ["Do I need a subfloor in my basement?", "Not always. Many vinyl floors go directly over a flat, dry slab with the right underlayment. A raised subfloor adds warmth and an air gap."],
  ["How do I test my basement floor for moisture?", "Tape a 2 x 2 ft piece of plastic to the slab for 24 to 72 hours. Moisture under the plastic means water is coming through the concrete."],
 ],
},
{
 "blog": "painting-walls", "blog_title": "Painting & Walls",
 "handle": "how-to-remove-wallpaper",
 "title": "How to Remove Wallpaper (Without Wrecking the Wall)",
 "summary": "Remove wallpaper cleanly: find out what type you have, peel the face, soak the backing, scrape at a low angle, then wash off every trace of glue.",
 "tags": ["Intermediate", "Painting & Walls", "Wallpaper", "Weekend project"],
 "difficulty": "Intermediate", "time": "4–8 hours per room", "cost": "$20–$60",
 "tools": ["Wide flexible putty knife or wallpaper scraper", "Garden pump sprayer or spray bottle", "Wallpaper steamer (for stubborn paper)", "Sponges and buckets", "Drop cloths and painter's tape", "Screwdriver"],
 "materials": ["Hot water", "Wallpaper remover solution or white vinegar (optional)", "Oil-based or shellac primer (for torn drywall paper)", "Joint compound"],
 "video": "https://www.youtube.com/watch?v=37oM46zhivo",
 "intro": "Removing wallpaper is mostly patience: getting the glue wet enough that the paper slides off instead of tearing the wall. This guide covers strippable, peelable and traditional wallpaper on drywall or plaster.",
 "safety": "<strong>Safety:</strong> you'll be using water near outlets and switches: switch off the breaker for the room's outlets, remove the cover plates and tape over the boxes. If the house was built before 1978, the paint under the paper may contain lead.",
 "steps": [
  step("Prep the room",
   "<p>Move furniture out, lay drop cloths and tape plastic along the baseboards. Switch off power to the walls you'll wet, remove cover plates and tape over outlets and switches.</p>"
   "<p><strong>Done right:</strong> floors are covered and no electrical box is exposed to water.</p>"),
  step("Find out what kind of wallpaper you have",
   "<p>Lift a corner with a putty knife and pull. Strippable paper comes off in whole sheets with little residue. Peelable paper lets the vinyl face come off but leaves a paper backing. Traditional paper tears and needs soaking.</p>"
   "<p><strong>Done right:</strong> you know whether the paper peels off dry or needs soaking.</p>"),
  step("Peel the face layer",
   "<p>Peel off as much of the top layer as you can, pulling slowly at a low angle. Removing the face lets water reach the glue underneath.</p>"
   "<p><strong>Done right:</strong> only the paper backing or bare paper remains on the wall.</p>"),
  step("Soak the backing",
   "<p>Spray a section with hot water, optionally mixed with wallpaper remover or a little white vinegar. Keep it wet for about 15 minutes, re-spraying so it never dries. The paper is ready when it turns dark and soft.</p>"
   "<p><strong>Done right:</strong> a corner of the backing slides off with light pressure from the scraper.</p>"),
  step("Scrape at a low angle",
   "<p>Hold the scraper almost flat to the wall and push gently under the paper. If you're gouging the wall, the paper isn't wet enough: soak it again. For stubborn paper, use a wallpaper steamer, holding the plate on one spot until the paper softens.</p>"
   "<p><strong>Done right:</strong> the paper comes off in large pieces and the wall surface isn't torn.</p>"),
  step("Wash off the glue and repair",
   "<p>Wash the walls with hot water and a sponge until they no longer feel slippery or sticky. Glue left on the wall causes paint to crack. Let the wall dry for a day. If the drywall's paper face tore, seal it with an oil-based or shellac primer before patching, so it doesn't bubble.</p>"
   "<p><strong>Done right:</strong> the wall feels smooth and not tacky, and torn spots are sealed and patched.</p>"),
 ],
 "pro": "<strong>Hire a painter if:</strong> there are several layers of old paper, the paper was hung directly on unprimed drywall and the wall is tearing badly, or you suspect lead paint underneath.",
 "faq": [
  ["What is the easiest way to remove wallpaper?", "Peel off the top layer, then soak the backing with hot water until it softens, and scrape at a low angle. Strippable paper may come off dry."],
  ["Does vinegar remove wallpaper?", "A mix of hot water and white vinegar can help soften the glue. Plain hot water often works as well if you keep the paper wet long enough."],
  ["Should I use a wallpaper scoring tool?", "Use it gently, if at all. Scoring helps water reach the glue through vinyl paper, but pressing hard can damage the drywall underneath."],
  ["Can you paint over wallpaper glue?", "No. Remaining glue causes paint to crack and peel. Wash it off completely and prime before painting."],
 ],
},
{
 "blog": "plumbing", "blog_title": "Plumbing Basics",
 "handle": "how-to-fix-a-leaky-faucet",
 "title": "How to Fix a Leaky Faucet by Replacing the Cartridge",
 "summary": "Stop a dripping single-handle faucet: identify the cartridge, shut off the water, remove the handle, swap the cartridge in the right position and test.",
 "tags": ["Intermediate", "Plumbing", "Faucet", "Repair"],
 "difficulty": "Intermediate", "time": "30–90 minutes", "cost": "$15–$50",
 "tools": ["Hex keys (Allen wrenches)", "Phillips and flat screwdrivers", "Adjustable wrench or channel-lock pliers", "Cartridge puller (for some Moen faucets)", "Needle-nose pliers", "Towel and phone camera"],
 "materials": ["Replacement cartridge for your faucet model", "Silicone faucet grease", "Rag or drain plug"],
 "video": "https://www.youtube.com/watch?v=1Q0PmvTk7os",
 "intro": "A drip from a single-handle kitchen or bathroom faucet usually means a worn cartridge, the part inside that mixes hot and cold. Replacing it fixes the drip and makes the handle feel new. This guide covers the common cartridge faucets from brands like Moen, Delta and Pfister.",
 "safety": "<strong>Safety:</strong> shut off both water supply valves and open the faucet to relieve pressure before you take anything apart. Plug the drain so small parts can't fall in.",
 "steps": [
  step("Identify the faucet and cartridge",
   "<p>Look for the brand name on the faucet and find the model in the paperwork, the maker's website or by photo. Many manufacturers offer lifetime warranties on cartridges for the original owner, so contact them before buying one.</p>"
   "<p><strong>Done right:</strong> you know the exact cartridge your faucet uses.</p>"),
  step("Shut off the water and protect the sink",
   "<p>Close both shut-off valves under the sink, open the faucet to drain it, and put a rag in the drain. Lay a towel in the sink to cushion dropped parts.</p>"
   "<p><strong>Done right:</strong> the faucet is open and no water flows.</p>"),
  step("Remove the handle and cap",
   "<p>Pop off the decorative cap with a small flat screwdriver to reveal the handle screw, or find the hex set screw under the handle. Remove the screw and lift off the handle. Unscrew the dome cap or bonnet nut to expose the cartridge. Photograph every step.</p>"
   "<p><strong>Done right:</strong> you can see the top of the cartridge and any retaining clip or nut.</p>"),
  step("Pull out the old cartridge",
   "<p>Note which way the cartridge's stem or tabs face; the new one must go in the same way or hot and cold will be reversed. Remove the retaining clip with needle-nose pliers or unscrew the retaining nut, then pull the cartridge straight up. Some Moen cartridges need a cartridge puller.</p>"
   "<p><strong>Done right:</strong> the old cartridge is out and you have a photo of its orientation.</p>"),
  step("Install the new cartridge",
   "<p>Coat the new cartridge's O-rings with silicone faucet grease. Push it in with the same orientation as the old one, and reinstall the clip or nut. Put back the cap, handle and screw.</p>"
   "<p><strong>Done right:</strong> the cartridge is seated fully and the handle moves smoothly through its full range.</p>"),
  step("Turn the water on and test",
   "<p>Open the shut-off valves slowly. Run the faucet hot and cold, then turn it off and watch the spout for a few minutes. If hot and cold are reversed, the cartridge stem needs to be turned 180 degrees.</p>"
   "<p><strong>Done right:</strong> hot is on the left, cold on the right, and the spout doesn't drip.</p>"),
 ],
 "pro": "<strong>Call a plumber if:</strong> the faucet leaks from its base or under the sink, the handle parts are corroded solid, or the faucet is old enough that parts aren't available. Replacing the whole faucet may then be the better option.",
 "faq": [
  ["Why does my single-handle faucet drip?", "Most often the cartridge's seals are worn or mineral deposits have built up inside it. Replacing the cartridge usually stops the drip."],
  ["How do I know which cartridge to buy?", "Identify the faucet brand and model, then match the cartridge part number. Bringing the old cartridge to the store also works."],
  ["Why are my hot and cold reversed after replacing the cartridge?", "The cartridge went in rotated. Turn the water off, remove it, rotate it 180 degrees and reinstall."],
  ["Are faucet cartridges covered by warranty?", "Many major brands offer lifetime warranties on cartridges for the original owner. Check with the manufacturer before buying a replacement."],
 ],
},
{
 "blog": "electrical", "blog_title": "Electrical Basics",
 "handle": "how-to-install-a-smart-switch",
 "title": "How to Install a Smart Light Switch (With Neutral)",
 "summary": "Install a Wi-Fi smart switch on an existing single-pole switch: check for a neutral, kill the power, identify line and load, wire it and set up the app.",
 "tags": ["Intermediate", "Electrical", "Smart home", "Upgrade"],
 "difficulty": "Intermediate", "time": "30–60 minutes", "cost": "$20–$60",
 "tools": ["Non-contact voltage tester", "Insulated screwdrivers", "Wire stripper", "Needle-nose pliers", "Painter's tape and marker (to label wires)", "Phone with the switch's app"],
 "materials": ["Smart switch (single-pole, or a 3-way kit for two-switch circuits)", "Wire nuts and a short pigtail of matching wire", "New wall plate (if needed)"],
 "video": "https://www.youtube.com/watch?v=dyglyuk4bzo",
 "intro": "A smart switch lets you control a light from your phone, a voice assistant or a schedule, while still working like a normal switch. Most Wi-Fi smart switches need a neutral wire in the switch box. This guide covers replacing a standard single-pole switch.",
 "safety": "<strong>Safety:</strong> switch off the breaker and verify the wires are dead with a non-contact tester before touching anything. Smart switches are bulkier than regular switches; if the box is crowded, it can overheat or damage wires. Check your local rules on homeowner electrical work.",
 "steps": [
  step("Check for a neutral wire",
   "<p>With the breaker off, remove the cover plate and switch screws and pull the switch out gently. Look in the back of the box for a bundle of white wires joined by a wire nut, not connected to the switch. That's the neutral.</p>"
   "<p><strong>Done right:</strong> you've found a neutral bundle, or you know you need a no-neutral smart switch instead.</p>"),
  step("Confirm the power is off",
   "<p>Touch a non-contact tester to every wire in the box, including the neutral bundle, after confirming the tester works on a live outlet. Boxes can hold more than one circuit.</p>"
   "<p><strong>Done right:</strong> the tester stays silent on every wire in the box.</p>"),
  step("Identify the line and load wires",
   "<p>A smart switch has separate line (power in) and load (to the light) terminals. If the box has only one cable, see the switch's instructions. If you can't tell which black wire brings power, separate and cap both, turn the breaker on briefly, test which one is hot with the non-contact tester, label it \"line\", and turn the breaker back off.</p>"
   "<p><strong>Done right:</strong> the line wire is labeled and the power is off again.</p>"),
  step("Wire the smart switch",
   "<p>Connect the line wire to the switch's line terminal and the other black wire to load. Join the switch's neutral lead to the neutral bundle with a short pigtail under the wire nut. Connect the ground wire to the green screw. Follow the color codes in the instructions, which vary between brands.</p>"
   "<p><strong>Done right:</strong> every connection is tight, no bare copper shows, and each wire stays put when tugged.</p>"),
  step("Mount it and set it up",
   "<p>Fold the wires carefully into the box, screw the switch in straight and attach the plate. Turn the breaker on, and follow the app to connect the switch to your Wi-Fi. Many switches need a 2.4 GHz network.</p>"
   "<p><strong>Done right:</strong> the light works from the switch and from the app.</p>"),
 ],
 "pro": "<strong>Call a licensed electrician if:</strong> there's no neutral and you don't want a no-neutral model, the box is too crowded, you find aluminum wiring, or the light is controlled from two or more switches and the wiring doesn't match the 3-way kit's instructions.",
 "faq": [
  ["Do smart switches need a neutral wire?", "Most Wi-Fi smart switches do. Some brands make no-neutral models that work in older homes without a neutral in the switch box."],
  ["How do I know if I have a neutral wire?", "With the power off, look for a bundle of white wires joined in the back of the switch box that isn't connected to the switch."],
  ["Can I install a smart switch on a 3-way circuit?", "Yes, with a 3-way smart switch kit, usually one smart switch plus a companion switch. Follow the kit's wiring diagram exactly."],
  ["Why won't my smart switch connect to Wi-Fi?", "Many need a 2.4 GHz network. Check the app's requirements and that the switch is within range of your router."],
 ],
},
{
 "blog": "doors-windows", "blog_title": "Doors & Windows",
 "handle": "how-to-install-a-smart-lock",
 "title": "How to Install a Smart Lock Deadbolt",
 "summary": "Install a smart deadbolt on your existing door: check the bore and backset, make sure the bolt throws freely, mount both halves and set up codes.",
 "tags": ["Beginner", "Doors & Windows", "Smart home", "Security"],
 "difficulty": "Beginner", "time": "30–60 minutes", "cost": "$100–$300",
 "tools": ["#2 Phillips screwdriver", "Tape measure", "Chisel and hammer (only if the strike needs adjusting)", "Phone with the lock's app"],
 "materials": ["Smart deadbolt", "Fresh batteries (usually AA, included)", "3 in strike plate screws (often included)"],
 "video": "https://www.youtube.com/watch?v=MSG2yPSAB40",
 "intro": "A smart deadbolt replaces your existing deadbolt and adds a keypad, phone access or both. Most fit standard U.S. door holes with just a screwdriver. The most common cause of problems is a bolt that drags in the strike, so this guide covers alignment first.",
 "safety": "<strong>Safety:</strong> keep the physical key or a backup entry method until the lock is fully set up and tested, so you can't lock yourself out.",
 "steps": [
  step("Check that your door fits",
   "<p>Measure the bore hole (usually 2-1/8 in), the backset from the door edge to the hole's center (2-3/8 or 2-3/4 in), and the door thickness (most smart locks fit about 1-3/8 to 2-1/4 in). Compare with the lock's specifications.</p>"
   "<p><strong>Done right:</strong> your door's measurements fall within the lock's listed range.</p>"),
  step("Make sure the bolt throws freely",
   "<p>With the old lock still on and the door closed, turn the deadbolt by hand. It should slide fully in and out without you pushing or pulling on the door. If it drags, adjust the strike plate or deepen the strike hole with a chisel. A motorized lock will jam on a bolt that drags.</p>"
   "<p><strong>Done right:</strong> the bolt extends and retracts with two fingers while the door is closed.</p>"),
  step("Remove the old deadbolt",
   "<p>Unscrew the interior thumb-turn, pull both halves off, and remove the bolt from the door edge. While you're there, replace the short strike plate screws with 3 in screws that reach the framing, for better security.</p>"
   "<p><strong>Done right:</strong> the door holes are empty and the strike is secured with long screws.</p>"),
  step("Install the bolt and both halves",
   "<p>Insert the new bolt with the side marked \"up\" facing up. Feed the exterior keypad's cable under or through the bolt as the instructions show, and mount the interior unit so its spindle engages the bolt. Tighten the screws evenly.</p>"
   "<p><strong>Done right:</strong> the cable isn't pinched and both halves sit flush against the door.</p>"),
  step("Add batteries, set up and test",
   "<p>Install the batteries and follow the app or manual to calibrate the door's handing, pair the lock and add user codes. Lock and unlock it with the door open, then closed, using the keypad, app and key.</p>"
   "<p><strong>Done right:</strong> every method locks and unlocks smoothly with the door closed.</p>"),
 ],
 "pro": "<strong>Call a locksmith if:</strong> the door has no deadbolt hole yet, it's a metal or glass door, the door sags so the bolt can't be aligned, or you have a mortise lock.",
 "faq": [
  ["Will a smart lock fit my door?", "Most fit standard U.S. deadbolt holes: a 2-1/8 in bore with a 2-3/8 or 2-3/4 in backset, on doors about 1-3/8 to 2-1/4 in thick. Check the lock's specs."],
  ["Why does my smart lock jam?", "Usually the bolt is dragging in the strike plate. Adjust the strike until the bolt moves freely by hand with the door closed."],
  ["What happens if the smart lock battery dies?", "Most give low-battery warnings well ahead of time and include a backup key or external battery contacts."],
  ["Do smart locks need Wi-Fi?", "Some connect directly over Wi-Fi; others use Bluetooth or a hub. Check which your lock uses and what features need a connection."],
 ],
},
{
 "blog": "outdoor-garden", "blog_title": "Outdoor & Garden",
 "handle": "how-to-replace-a-deck-board",
 "title": "How to Replace a Rotted Deck Board",
 "summary": "Replace a rotted or cracked deck board: check the joists underneath, remove the fasteners, cut new boards to land on joists and screw them down.",
 "tags": ["Intermediate", "Outdoor & Garden", "Deck", "Repair"],
 "difficulty": "Intermediate", "time": "1–3 hours", "cost": "$20–$60 per board",
 "tools": ["Circular saw", "Oscillating multi-tool", "Pry bar and cat's paw", "Drill/driver", "Tape measure and speed square", "Screwdriver or awl (to test for rot)", "Safety glasses"],
 "materials": ["Replacement deck board (match the size and species)", "Exterior deck screws rated for treated lumber", "2x lumber for cleats (if needed)", "End-cut wood preservative"],
 "video": "https://www.youtube.com/watch?v=vGKuQbH_wIQ",
 "intro": "One soft or split deck board is a trip hazard and a sign to check what's underneath. Replacing a board is a few hours' work. This guide covers wood decks with boards nailed or screwed to wood joists.",
 "safety": "<strong>Safety:</strong> wear safety glasses and gloves. Set the circular saw depth to the board thickness so you don't cut into the joist. Treated lumber dust is irritating; wear a dust mask and don't burn the scraps.",
 "steps": [
  step("Check the joists under the board",
   "<p>Before cutting anything, push a screwdriver into the joists under the damaged board and the boards around it. If the tip sinks in easily, the joist is rotted and needs repair first.</p>"
   "<p><strong>Done right:</strong> the joists are solid, or you've identified which need a pro's repair.</p>"),
  step("Remove the fasteners",
   "<p>Back out screws with a drill. Pull nails with a cat's paw and pry bar, or cut them with an oscillating tool slipped between the boards if they won't budge.</p>"
   "<p><strong>Done right:</strong> the damaged board is loose and the neighboring boards aren't damaged.</p>"),
  step("Cut out the damaged section",
   "<p>If only part of a long board is bad, cut it out so each new end lands over the center of a joist. If the cut falls next to a joist, screw a 2x cleat to the side of the joist to support the new board's end.</p>"
   "<p><strong>Done right:</strong> every board end will rest on a joist or cleat.</p>"),
  step("Fit the new board",
   "<p>Cut the new board to length and brush end-cut preservative on any cut ends of treated lumber. Match the gap between boards: dry boards get about 1/8 in, while wet pressure-treated boards can be laid tight because they shrink as they dry.</p>"
   "<p><strong>Done right:</strong> the board sits flat, its ends are tight to the neighbors, and the spacing matches the rest of the deck.</p>"),
  step("Screw it down",
   "<p>Drive two exterior deck screws at each joist, about 3/4 in from each edge, slightly below the surface. Pre-drill near board ends so they don't split.</p>"
   "<p><strong>Done right:</strong> the board doesn't move or squeak when you walk on it, and no screw heads stick up.</p>"),
 ],
 "pro": "<strong>Call a deck contractor if:</strong> the joists, beams, posts or the ledger board where the deck attaches to the house are soft, or many boards are failing at once. Those are structural safety problems.",
 "faq": [
  ["Can I replace just one deck board?", "Yes. Remove the fasteners, cut the board so its ends land on joists, and screw the new one down."],
  ["What screws should I use for deck boards?", "Exterior deck screws coated or made of stainless steel and rated for pressure-treated lumber."],
  ["How far apart should deck boards be?", "Usually about 1/8 in for dry boards. Wet pressure-treated boards can go tight because they shrink as they dry. Follow the board maker's spacing for composites."],
  ["Will a new board match the old ones?", "Not right away. New wood weathers over months; sealing or staining the whole deck helps it blend."],
 ],
},
{
 "blog": "storage", "blog_title": "Storage & Organization",
 "handle": "how-to-build-a-french-cleat-wall",
 "title": "How to Build a French Cleat Wall for Garage Storage",
 "summary": "Build a French cleat wall that holds tools you can rearrange anytime: rip 45-degree cleats from plywood, screw them into studs and make matching holders.",
 "tags": ["Intermediate", "Storage & Organization", "Garage", "Weekend project"],
 "difficulty": "Intermediate", "time": "4–8 hours", "cost": "$60–$150",
 "tools": ["Table saw or circular saw with a guide", "Stud finder", "Level or laser level", "Drill/driver", "Tape measure", "Clamps", "Safety glasses and hearing protection"],
 "materials": ["3/4 in plywood (one 4 x 8 ft sheet makes many cleats)", "2-1/2 to 3 in wood screws", "1-1/4 in screws and wood glue (for holders)", "Scrap plywood for holders"],
 "video": "https://www.youtube.com/watch?v=E-vpLAvUt_Q",
 "intro": "A French cleat wall is rows of angled wooden strips screwed to the studs. Tool holders with a matching angled strip hook onto them and can be moved anywhere. It's stronger and more flexible than pegboard. This guide covers a garage or shop wall.",
 "safety": "<strong>Safety:</strong> ripping plywood at an angle on a table saw is an advanced cut: use a push stick, keep the blade guard on if possible, and never stand directly behind the blade. If you're not comfortable, ask the lumber store to rip strips for you or use a circular saw with a clamped guide.",
 "steps": [
  step("Rip the cleats",
   "<p>Rip 3/4 in plywood into strips about 3-1/2 to 4 in wide with the blade tilted to 45 degrees, so each strip has one beveled edge. Cut more than you think you need; leftovers become cleats on tool holders.</p>"
   "<p><strong>Done right:</strong> every strip has a clean 45-degree bevel along one long edge.</p>"),
  step("Mark studs and a level start line",
   "<p>Mark every stud along the wall. Draw a level line for the lowest cleat, usually 24 to 36 in off the floor or just above your workbench.</p>"
   "<p><strong>Done right:</strong> studs are marked and the first line is level end to end.</p>"),
  step("Screw the wall cleats into studs",
   "<p>Hold the first cleat on the line with the bevel facing up and sloping toward the wall, so it forms a pocket. Drive two 2-1/2 to 3 in screws into every stud. Add more rows above, spacing them about 6 to 8 in apart.</p>"
   "<p><strong>Done right:</strong> each cleat is level, screwed into every stud, and the bevels all slope down toward the wall.</p>"),
  step("Build the tool holders",
   "<p>Glue and screw a short cleat to the back of each holder with its bevel facing down and toward the wall, so it hooks into the wall cleat. Build simple shelves, hooks or tool racks from scrap plywood.</p>"
   "<p><strong>Done right:</strong> each holder drops onto a wall cleat and locks in without wobbling.</p>"),
  step("Load the wall",
   "<p>Hang the holders and tools, putting heavier items on the lower rows and near the center of a stud. Rearrange whenever your tools change.</p>"
   "<p><strong>Done right:</strong> holders stay put when you take tools off them, and the wall cleats don't flex.</p>"),
 ],
 "pro": "<strong>Hire a carpenter if:</strong> the wall is concrete or block and you don't have a hammer drill, or you want a full built-in workshop system.",
 "faq": [
  ["What angle should French cleats be?", "45 degrees is standard and makes the cleats easy to cut and strong."],
  ["How far apart should French cleats be?", "About 6 to 8 in apart vertically works for most tool holders. Some people space them closer for small items."],
  ["What wood is best for French cleats?", "3/4 in plywood is strong and stable and won't split like solid boards can."],
  ["How much weight can a French cleat hold?", "When the wall cleats are screwed into every stud, they hold heavy tools well. Strength depends on the screws, studs and the holder's construction."],
 ],
},
{
 "blog": "maintenance", "blog_title": "Home Maintenance",
 "handle": "spring-home-maintenance-checklist",
 "title": "Spring Home Maintenance Checklist (After Winter)",
 "summary": "Check your home after winter with this spring checklist: roof, gutters, foundation, AC, outdoor water, deck, windows, attic and safety alarms.",
 "tags": ["Beginner", "Home Maintenance", "Checklist", "Seasonal"],
 "difficulty": "Beginner", "time": "1–2 weekends", "cost": "$50–$300 + any service calls",
 "tools": ["Binoculars", "Ladder", "Flashlight", "Garden hose", "Screwdriver set", "Work gloves"],
 "materials": ["HVAC air filters", "Exterior caulk", "Replacement window screen and spline (if needed)", "Smoke and CO alarm batteries"],
 "video": "https://www.youtube.com/watch?v=3merrzo5PIU",
 "intro": "Winter is hard on a house: ice, wind and freeze-thaw cycles cause damage you won't notice until it leaks. A spring walk-through catches it early. Work through this list once the ground thaws, before the summer heat.",
 "safety": "<strong>Safety:</strong> inspect the roof from the ground with binoculars rather than climbing on it. Use a stable ladder on firm ground for gutters.",
 "steps": [
  step("Inspect the roof from the ground",
   "<p>Scan the roof with binoculars for missing, curled or cracked shingles, damaged flashing around the chimney and vents, and debris in the valleys. Our <a href=\"/blogs/maintenance/signs-your-roof-needs-replacement\">roof warning signs guide</a> shows what to look for.</p>"
   "<p><strong>Done right:</strong> you've noted any damage to show a roofer.</p>"),
  step("Clean gutters and check drainage",
   "<p>Clear what winter left in the gutters and confirm downspouts send water at least 4 to 6 ft away from the house. Look for low spots in the soil next to the foundation where water pools. See our <a href=\"/blogs/maintenance/how-to-clean-gutters\">gutter cleaning guide</a>.</p>"
   "<p><strong>Done right:</strong> water flows away from the foundation on every side.</p>"),
  step("Check the foundation and basement",
   "<p>Walk around the foundation looking for new cracks, and check the basement for damp spots, efflorescence (white powder) or musty smells. Pour a bucket of water into the sump pit to test that the pump starts.</p>"
   "<p><strong>Done right:</strong> the basement is dry and the sump pump runs and shuts off on its own.</p>"),
  step("Get the AC ready",
   "<p>Replace the air filter, clear leaves and debris from around the outdoor unit, and test the cooling before the first hot day. Schedule a tune-up if it hasn't been serviced in a year. See our <a href=\"/blogs/maintenance/how-to-change-hvac-air-filter\">HVAC filter guide</a>.</p>"
   "<p><strong>Done right:</strong> cool air flows from the vents and the outdoor unit has at least 2 ft of clear space around it.</p>"),
  step("Test outdoor faucets and irrigation",
   "<p>Turn outdoor faucets back on and check for leaks, both outside and on the pipe inside the wall. A pipe that froze over winter may only leak once the faucet is opened. Start irrigation zones one at a time and look for broken heads.</p>"
   "<p><strong>Done right:</strong> no water drips inside the house when outdoor faucets run.</p>"),
  step("Check the deck, windows and screens",
   "<p>Look for loose railings, popped fasteners and soft boards on the deck, and do the water test to see whether it needs sealing. Repair torn window screens and recaulk gaps in exterior trim. Our <a href=\"/blogs/outdoor-garden/how-to-seal-a-deck\">deck sealing guide</a> and <a href=\"/blogs/doors-windows/how-to-rescreen-a-window\">rescreening guide</a> can help.</p>"
   "<p><strong>Done right:</strong> railings are solid, screens are intact and the deck repels water.</p>"),
  step("Look in the attic and test alarms",
   "<p>With a flashlight, check the attic for water stains, wet insulation and signs of pests. Test every smoke and CO alarm and replace batteries if they're not sealed 10-year units. See our <a href=\"/blogs/maintenance/how-to-test-and-replace-smoke-alarms\">smoke alarm guide</a>.</p>"
   "<p><strong>Done right:</strong> the attic is dry and every alarm sounds when tested.</p>"),
 ],
 "pro": "<strong>Call a pro for:</strong> roof damage, new or widening foundation cracks, water in the basement, AC tune-ups, and leaks inside walls from outdoor faucets.",
 "faq": [
  ["When should I do spring home maintenance?", "Once the ground has thawed and freezing nights are over, usually March to May depending on where you live."],
  ["What should I check after winter?", "The roof, gutters, foundation and basement, outdoor water lines, the AC, the deck and windows, the attic, and your safety alarms."],
  ["How do I know if an outdoor faucet pipe froze?", "Turn it on and check inside the house where the pipe comes through the wall. A split pipe often only leaks while the faucet is running."],
  ["How often should I test my sump pump?", "At least once a year, ideally in spring before heavy rains, by pouring water into the pit."],
 ],
},
]

AFFILIATE_B4D = {
 "how-to-paint-kitchen-cabinets": ["bonding primer"],
 "how-to-replace-a-bathroom-vanity": [],
 "best-flooring-for-basement": [],
 "how-to-remove-wallpaper": ["wallpaper steamer"],
 "how-to-fix-a-leaky-faucet": ["cartridge puller"],
 "how-to-install-a-smart-switch": [],
 "how-to-install-a-smart-lock": [],
 "how-to-replace-a-deck-board": ["end-cut preservative"],
 "how-to-build-a-french-cleat-wall": [],
 "spring-home-maintenance-checklist": [],
}
