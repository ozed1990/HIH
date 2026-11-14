"""Build hih/content/pages/tools-we-recommend.html.

Every product link is taken from a live guide body (/tmp/arts.json, pulled from Shopify),
matched by (guide handle, anchor text), so the page never carries a link the guides don't.
Run: python3 hih/scripts/build_tools_page.py /tmp/arts.json
"""
import html
import json
import re
import sys
from pathlib import Path

# (section title, section intro, [(product name, guide handle, anchor text in that guide, why)])
SECTIONS = [
    ("Start here: the starter kit", "A handful of tools that show up in guide after guide. Buy these first.", [
        ("Non-contact voltage tester", "how-to-replace-a-light-fixture", "non-contact voltage tester",
         "Confirms a wire is dead before you touch it. Non-negotiable for any switch, outlet or fixture job."),
        ("Plug-in outlet tester", "how-to-replace-an-outlet", "outlet tester",
         "Plug it in and the lights tell you if an outlet is wired right, reversed or missing a ground."),
        ("Stud finder", "how-to-install-floating-shelves", "stud finder",
         "Finds framing behind drywall so shelves, TVs and towel bars hold."),
        ("Magnetic stud finder", "how-to-find-a-stud-without-a-stud-finder", "magnet",
         "No batteries: it finds the drywall screws, and the screws mark the studs."),
        ("Thread seal tape", "how-to-replace-a-showerhead", "thread seal tape",
         "Seals threaded plumbing joints. Cheap, and you'll use it more than you expect."),
        ("Silicone lubricant", "fix-a-sliding-door-that-sticks", "silicone lubricant",
         "Quiets and frees sliding doors, tracks and hinges without attracting dirt like oil does."),
    ]),
    ("Winter prep", "Do these before the first hard freeze.", [
        ("Insulated faucet cover", "how-to-winterize-outdoor-faucets", "insulated faucet cover",
         "Slips over an outdoor spigot so it doesn't freeze and crack."),
        ("Foam pipe insulation", "how-to-keep-pipes-from-freezing", "foam pipe insulation",
         "Pre-slit sleeves for exposed pipes in crawl spaces, garages and basements."),
        ("Pipe heat cable", "how-to-keep-pipes-from-freezing", "pipe heat cable",
         "For pipes that freeze every year even with insulation."),
        ("Door sweep", "how-to-install-a-door-sweep", "screw-on door sweep",
         "Closes the gap under an exterior door, which is one of the biggest drafts in most homes."),
        ("Kerf-in weatherstrip", "how-to-weatherstrip-a-door", "kerf-in strip",
         "Replaces worn weatherstripping on door jambs that have a slot (kerf) for it."),
        ("Foam backer rod", "how-to-caulk-exterior-windows", "foam backer rod",
         "Fills deep gaps before you caulk, so the caulk bead lasts instead of sinking."),
        ("10-year sealed smoke alarm", "how-to-test-and-replace-smoke-alarms", "10-year sealed battery smoke alarm",
         "No battery swaps for a decade. A good upgrade when an old alarm hits its replacement date."),
    ]),
    ("Plumbing and drains", "Fix most clogs, drips and running toilets without a service call.", [
        ("Hand drain auger", "how-to-unclog-a-kitchen-sink", "hand drain auger",
         "Reaches clogs past the trap that a plunger can't move."),
        ("Toilet auger", "unclog-a-toilet-without-a-plunger", "toilet auger",
         "Made for the toilet's curve, with a guard that protects the porcelain."),
        ("Plastic drain-cleaning tool", "slow-draining-bathroom-sink", "plastic drain-cleaning tool",
         "Pulls hair out of a slow bathroom drain in a minute, no chemicals."),
        ("Toilet flapper", "how-to-fix-a-running-toilet", "new flapper",
         "The usual cause of a running toilet. Match it to your flush valve size."),
        ("Toilet fill valve", "how-to-fix-a-running-toilet", "new fill valve",
         "Replace it when the tank keeps refilling or fills slowly."),
        ("Basin wrench", "how-to-replace-a-kitchen-faucet", "basin wrench",
         "Reaches faucet nuts up behind the sink where no other wrench fits."),
        ("Cartridge puller", "how-to-fix-a-leaky-faucet", "cartridge puller",
         "Pulls a stuck faucet cartridge without damaging the valve body."),
        ("Water meter key", "how-to-find-main-water-shut-off-valve", "water meter key",
         "Turns the curb-side shutoff when the valve inside the house won't."),
    ]),
    ("Painting and drywall", "Cleaner lines and patches you can't see.", [
        ("Angled sash brush", "how-to-cut-in-paint", "angled sash brush",
         "The brush for cutting in crisp lines at ceilings, corners and trim."),
        ("Roller cover", "how-to-paint-a-room", "roller cover",
         "A good cover holds more paint and leaves less lint on the wall."),
        ("Paint shield", "how-to-paint-baseboards", "paint shield",
         "Hold it against the floor or carpet while you paint baseboards."),
        ("Spackle", "how-to-patch-a-hole-in-drywall", "spackle",
         "Fills nail holes and small dents. Sand, prime, paint."),
        ("Self-adhesive drywall patch", "how-to-patch-a-hole-in-drywall", "self-adhesive patch",
         "Covers holes up to a few inches without cutting new drywall."),
        ("Bonding primer", "how-to-paint-kitchen-cabinets", "bonding primer",
         "Gets paint to stick to slick surfaces like cabinet finishes."),
        ("Wallpaper steamer", "how-to-remove-wallpaper", "wallpaper steamer",
         "Softens old paste so wallpaper comes off in sheets instead of shreds."),
    ]),
    ("Flooring and trim", "Tools that make floors and trim look professionally done.", [
        ("Tapping block", "how-to-install-vinyl-plank-flooring", "tapping block",
         "Locks planks together without chipping the edges."),
        ("Jamb saw", "how-to-undercut-a-door-jamb", "jamb saw",
         "Undercuts door casing so new flooring slides underneath."),
        ("Coping saw", "how-to-install-quarter-round", "coping saw",
         "Cuts tight inside corners on quarter round and baseboard."),
        ("Floor leveling compound", "how-to-install-vinyl-plank-flooring", "leveling compound",
         "Fills low spots in the subfloor before you lay planks."),
        ("Squeaky floor repair screws", "how-to-fix-squeaky-floors", "breakaway screw",
         "Screws through carpet or hardwood, then snaps off below the surface."),
        ("3-in-1 transition molding", "how-to-install-floor-transition-strips", "3-in-1 transition molding",
         "One strip that works as a T-molding, reducer or end cap."),
    ]),
    ("Kitchen and bath", "Small fixes that make the most-used rooms look new.", [
        ("Caulk removal tool", "how-to-recaulk-a-bathtub", "caulk removal tool",
         "Scrapes old caulk out of the joint without scratching the tub."),
        ("Caulk finishing tool", "how-to-recaulk-a-bathtub", "caulk-finishing tool",
         "Smooths a new bead into a clean, even line."),
        ("Grout saw", "how-to-regrout-a-backsplash", "grout saw",
         "Cuts out cracked grout so new grout has room to bond."),
        ("Grout sealer applicator bottle", "how-to-seal-grout", "applicator-tip bottle",
         "Puts sealer on the grout lines, not all over the tile."),
        ("Cabinet hardware jig", "how-to-install-cabinet-hardware", "cabinet hardware jig",
         "Drills every knob and pull hole in the same spot."),
        ("Garbage disposal wrench", "garbage-disposal-humming-not-working", "disposal wrench",
         "Frees a jammed disposal from underneath, no hands in the drain."),
        ("Degreasing cleaner", "peel-and-stick-tile-backsplash", "degreasing cleaner",
         "Cleans the wall first so peel-and-stick tile actually sticks."),
    ]),
    ("Outdoor and garden", "Yard, deck and exterior projects.", [
        ("Oxygen-based deck cleaner", "how-to-seal-a-deck", "oxygen-based deck cleaner",
         "Cleans grayed wood before sealing without the harshness of bleach."),
        ("End-cut wood preservative", "how-to-replace-a-deck-board", "end-cut preservative",
         "Protects fresh cuts on treated lumber, where rot starts first."),
        ("Pressure washer surface cleaner", "how-to-pressure-wash-concrete", "surface cleaner attachment",
         "Cleans driveways and patios evenly, without wand stripes."),
        ("Gate anti-sag kit", "how-to-fix-a-sagging-gate", "anti-sag kit",
         "A cable and turnbuckle that pulls a sagging gate back into square."),
        ("Low-voltage path light kit", "how-to-install-low-voltage-path-lights", "path light kit",
         "Plug-in landscape lighting with no electrician needed."),
        ("Half-moon edger", "how-to-edge-a-flower-bed", "half-moon edger",
         "Cuts a clean, crisp edge between lawn and beds."),
        ("Rechargeable batteries for solar lights", "how-to-install-solar-path-lights", "rechargeable batteries",
         "Fresh batteries bring dim solar lights back to life."),
    ]),
    ("Home maintenance and storage", "The routine jobs that prevent expensive repairs.", [
        ("Dryer vent brush", "how-to-clean-a-dryer-vent", "vent brush",
         "Clears lint from the full length of the duct, a top cause of dryer fires."),
        ("Refrigerator coil brush", "how-to-clean-refrigerator-coils", "refrigerator coil brush",
         "Long and thin to reach the coils under or behind the fridge."),
        ("Gutter sealant", "how-to-clean-gutters", "gutter sealant",
         "Seals leaking seams and corners once the gutters are clean."),
        ("Snap toggle anchors", "how-to-choose-and-install-drywall-anchors", "snap toggle anchors",
         "The strongest drywall anchor for heavy shelves and mirrors when there's no stud."),
        ("Closet shelf and rod bracket", "how-to-install-a-closet-shelf-and-rod", "shelf-and-rod bracket",
         "Supports the shelf and rod in the middle of long spans."),
        ("Pegboard locking hooks", "how-to-install-pegboard", "locking hooks",
         "Hooks that stay put when you grab a tool."),
    ]),
]

AMAZON = ("https://link.amazon/", "https://amzn.to/", "https://www.amazon.com/")


def main(arts_path):
    arts = json.load(open(arts_path))
    by_handle = {a["handle"]: a for a in arts}
    out = [
        '<p class="guide-intro">These are the tools and supplies our guides actually call for, grouped by project. '
        'Each one links to the guide that uses it, so you can see exactly how it’s used before you buy.</p>',
        '<aside class="callout callout--disclosure"><p>As an Amazon Associate we earn from qualifying purchases. '
        'Buying through these links costs you nothing extra. <a href="/pages/about">How we make money</a>.</p></aside>',
    ]
    seen = set()
    for title, intro, items in SECTIONS:
        out.append(f"<h2>{html.escape(title)}</h2>")
        out.append(f"<p>{html.escape(intro)}</p>")
        out.append('<ul class="hih-picks">')
        for name, handle, anchor, why in items:
            art = by_handle[handle]  # KeyError = guide not published
            links = [
                m.group(1)
                for m in re.finditer(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', art["body"])
                if m.group(1).startswith(AMAZON) and html.unescape(re.sub("<[^>]+>", "", m.group(2))).strip() == anchor
            ]
            assert len(set(links)) == 1, (handle, anchor, links)
            href = links[0]
            assert "link.amazon" in href or "tag=babyunivers0f-20" in href, href
            assert name not in seen, name
            seen.add(name)
            guide = f"/blogs/{art['blog']['handle']}/{handle}"
            out.append(
                f'<li><a href="{html.escape(href)}" rel="sponsored noopener" target="_blank">{html.escape(name)}</a>'
                f"<span>{html.escape(why)}</span>"
                f'<a class="hih-picks__guide" href="{guide}">Used in: {html.escape(art["title"])}</a></li>'
            )
        out.append("</ul>")
    out.append(
        '<p class="page-updated">We only list products for jobs our guides cover. '
        "Prices and availability change on Amazon, so check the listing before you buy.</p>"
    )
    dest = Path(__file__).resolve().parents[1] / "content/pages/tools-we-recommend.html"
    dest.write_text("\n".join(out) + "\n")
    print(dest, len(seen), "products")


if __name__ == "__main__":
    main(sys.argv[1])
