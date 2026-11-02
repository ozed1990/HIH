#!/usr/bin/env python3
"""Original HIH step diagrams. Colors are read from theme/assets/hih-tokens.css so diagrams match the site.
Writes content/media/<stem>.svg; scripts/render_diagrams.js turns them into 1200x900 WebP."""
import re, pathlib
ROOT = pathlib.Path(__file__).resolve().parents[1]
tok = dict(re.findall(r"--hih-color-([a-z-]+):\s*(#[0-9a-fA-F]{6})", (ROOT.parent / "assets/hih-tokens.css").read_text()))
INK, PRI, MUTED, PAPER, MIST, SAGE, SAGE2, LINE, BRASS = (tok[k] for k in ["ink", "primary", "muted", "paper", "mist", "sage", "sage-strong", "line", "brass"])
WARN = tok["warn-ink"]
OUT = ROOT / "content/media"; OUT.mkdir(parents=True, exist_ok=True)
W, H = 1200, 900

def svg(body, title):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="{title}">
<defs><marker id="a" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{BRASS}"/></marker>
<marker id="p" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0 0L10 5L0 10z" fill="{PRI}"/></marker>
<pattern id="hatch" width="14" height="14" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="14" stroke="{LINE}" stroke-width="4"/></pattern></defs>
<rect width="{W}" height="{H}" fill="{MIST}"/>
<g font-family="Manrope, sans-serif" fill="{INK}">{body}</g></svg>'''

def T(x, y, s, size=30, w=600, fill=None, anchor="start"):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{w}" fill="{fill or INK}" text-anchor="{anchor}">{s}</text>'
def L(x1, y1, x2, y2, c=None, sw=4, dash=None, mk=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-start="url(#{mk})" marker-end="url(#{mk})"' if mk else ""
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c or PRI}" stroke-width="{sw}" stroke-linecap="round"{d}{m}/>'
def R(x, y, w, h, fill=None, stroke=None, sw=4, rx=0):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill or "none"}" stroke="{stroke or "none"}" stroke-width="{sw}"/>'
def DIM(x1, y1, x2, y2, label, lx, ly, anchor="middle", size=28):
    return L(x1, y1, x2, y2, BRASS, 3, mk="a") + T(lx, ly, label, size, 700, BRASS, anchor)
def LEAD(x1, y1, x2, y2, label, anchor="start", dx=10):
    return L(x1, y1, x2, y2, MUTED, 2) + f'<circle cx="{x1}" cy="{y1}" r="6" fill="{PRI}"/>' + T(x2 + (dx if anchor == "start" else -dx), y2 + 10, label, 28, 600, INK, anchor)
def HEAD(s):
    return T(60, 90, s, 40, 700, PRI)
def OK(x, y): return f'<circle cx="{x}" cy="{y}" r="26" fill="{PRI}"/><path d="M{x-12} {y}l8 9 16-18" stroke="{PAPER}" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>'
def NO(x, y): return f'<circle cx="{x}" cy="{y}" r="26" fill="{WARN}"/><path d="M{x-10} {y-10}l20 20M{x+10} {y-10}l-20 20" stroke="{PAPER}" stroke-width="5" stroke-linecap="round"/>'

D = {}

# Backsplash 3: level line above an out-of-level counter
D["peel-and-stick-tile-backsplash-step-3"] = svg(
    HEAD("Start from a level line, not the counter")
    + R(120, 160, 960, 470, PAPER, LINE, 3)
    + R(180, 200, 220, 140, SAGE, PRI, 3) + R(800, 200, 220, 140, SAGE, PRI, 3) + T(290, 280, "Cabinet", 26, 600, PRI, "middle") + T(910, 280, "Cabinet", 26, 600, PRI, "middle")
    + '<polygon points="120,630 1080,600 1080,680 120,710" fill="' + SAGE2 + '" stroke="' + PRI + '" stroke-width="4"/>'
    + T(600, 680, "Countertop (not level)", 28, 600, PRI, "middle")
    + L(130, 596, 1070, 596, BRASS, 5, "18 10")
    + T(140, 580, "Level line", 28, 700, BRASS)
    + DIM(1110, 596, 1110, 628, "", 0, 0) + T(1100, 560, "1/8 in", 28, 700, BRASS, "end")
    + DIM(140, 596, 140, 625, "", 0, 0)
    + T(140, 770, "Measure up 1/8 in from the counter's LOWEST point, then draw level across the wall.", 28, 500, INK)
    + T(140, 815, "Tiles sit on the line; the small gap is caulked at the end.", 28, 500, MUTED), "Level start line diagram")

# Backsplash 6: outlet cutout
D["peel-and-stick-tile-backsplash-step-6"] = svg(
    HEAD("Cutting around an outlet")
    + R(160, 170, 420, 560, PAPER, LINE, 3) + T(370, 210, "1. Mark", 30, 700, PRI, "middle")
    + R(250, 300, 240, 300, "url(#hatch)", MUTED, 3, 8) + R(290, 340, 160, 220, PAPER, PRI, 4, 6)
    + L(300, 350, 440, 350, BRASS, 3, "8 8") + L(300, 550, 440, 550, BRASS, 3, "8 8") + L(300, 350, 300, 550, BRASS, 3, "8 8") + L(440, 350, 440, 550, BRASS, 3, "8 8")
    + T(370, 660, "Cut ~1/16 in inside the box outline", 24, 600, MUTED, "middle")
    + R(640, 170, 420, 560, PAPER, LINE, 3) + T(850, 210, "2. Cover", 30, 700, PRI, "middle")
    + R(720, 280, 260, 340, PAPER, PRI, 5, 14) + R(800, 340, 100, 70, MIST, PRI, 3, 10) + R(800, 480, 100, 70, MIST, PRI, 3, 10)
    + '<circle cx="850" cy="450" r="9" fill="' + PRI + '"/>'
    + T(850, 660, "Cover plate hides every cut edge", 24, 600, MUTED, "middle")
    + T(160, 800, "Power off at the breaker and verified dead before you remove the cover.", 28, 600, WARN), "Outlet cutout diagram")

# Recaulk 4: taped joint cross-section
D["how-to-recaulk-a-bathtub-step-4"] = svg(
    HEAD("Tape both sides of the joint")
    + R(200, 150, 160, 520, SAGE2, PRI, 4) + T(280, 140, "Wall tile", 28, 700, PRI, "middle")
    + '<path d="M200 670 L200 700 Q200 760 260 760 L1000 760 L1000 690 L380 690 Q370 690 370 680" fill="' + PAPER + '" stroke="' + PRI + '" stroke-width="4"/>'
    + T(700, 740, "Tub rim", 28, 700, PRI, "middle")
    + R(360, 300, 14, 360, BRASS) + T(390, 330, "Tape on wall", 28, 600, INK)
    + R(420, 676, 300, 14, BRASS) + T(560, 650, "Tape on tub", 28, 600, INK, "middle")
    + DIM(360, 600, 360, 676, "", 0, 0) + DIM(360, 640, 420, 640, "", 0, 0) + T(480, 590, "~1/4 in bead", 28, 700, BRASS)
    + T(200, 840, "Tape sets the bead width. Pull it while the silicone is still wet.", 28, 500, INK), "Taped caulk joint diagram")

# Recaulk 6: concave vs bulging bead
D["how-to-recaulk-a-bathtub-step-6"] = svg(
    HEAD("Tool the bead into a slight curve")
    + R(140, 200, 60, 380, SAGE2, PRI, 4) + R(140, 580, 400, 60, PAPER, PRI, 4)
    + f'<path d="M200 470 L200 580 L310 580 Q215 565 200 470z" fill="{BRASS}"/>' + OK(400, 300) + T(340, 380, "Concave: sheds water,", 28, 600) + T(340, 420, "bonds both faces", 28, 600)
    + R(660, 200, 60, 380, SAGE2, PRI, 4) + R(660, 580, 400, 60, PAPER, PRI, 4)
    + f'<path d="M720 470 Q830 470 830 580 L720 580z" fill="{BRASS}"/>' + NO(920, 300) + T(860, 380, "Bulging: traps water,", 28, 600) + T(860, 420, "peels at the edges", 28, 600)
    + T(140, 760, "One smooth pass with a wet fingertip or finishing tool per section.", 28, 500, INK), "Concave versus bulging caulk bead")

# LVP 3: layout plan
rows = ""
for i in range(7):
    y = 180 + i * 70
    off = [0, 180, 360, 90, 270, 450, 150][i]
    for x in range(140 + off % 360 - 360, 1080, 360):
        x0 = max(140, x); x1 = min(1060, x + 360)
        if x1 > x0: rows += R(x0, y, x1 - x0, 70, PAPER if i % 2 == 0 else SAGE, PRI, 2)
D["how-to-install-vinyl-plank-flooring-step-3"] = svg(
    HEAD("Plan the layout before the first click")
    + R(140, 180, 920, 490, None, PRI, 6) + rows
    + DIM(1100, 180, 1100, 250, "", 0, 0) + DIM(1100, 600, 1100, 670, "", 0, 0) + R(800, 392, 250, 80, PAPER, BRASS, 2, 6) + T(925, 425, "Edge rows", 24, 700, BRASS, "middle") + T(925, 457, "≥ ½ plank, matched", 24, 700, BRASS, "middle")
    + R(500, 262, 200, 40, PAPER, BRASS, 2, 6) + T(600, 291, "≥ 6 in stagger", 24, 700, BRASS, "middle")
    + T(140, 740, "Divide room width by plank width. If the last row is under half a plank,", 28, 500)
    + T(140, 785, "rip the first row so both edges match. Stagger end joints at least 6 in.", 28, 500), "Vinyl plank layout plan")

# LVP 4: expansion gap section
D["how-to-install-vinyl-plank-flooring-step-4"] = svg(
    HEAD("Leave the expansion gap")
    + R(120, 640, 960, 70, "url(#hatch)", MUTED, 3) + T(600, 760, "Subfloor", 28, 600, MUTED, "middle")
    + R(160, 150, 120, 490, SAGE2, PRI, 4) + T(220, 140, "Wall", 28, 700, PRI, "middle")
    + R(280, 470, 46, 170, PAPER, PRI, 4) + T(340, 400, "Baseboard", 28, 600, INK)
    + R(310, 600, 770, 40, SAGE, PRI, 4) + T(700, 590, "Vinyl plank (floating)", 28, 600, PRI, "middle")
    + DIM(280, 560, 310, 560, "", 0, 0) + L(320, 555, 420, 500, BRASS, 2) + T(430, 505, "~1/4 in gap", 28, 700, BRASS)
    + T(120, 830, "Nail trim into the wall, never into the floor, so the floor can move.", 28, 500), "Expansion gap section")

# Drywall 1: method by size
def hole(cx, cy, r): return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{PAPER}" stroke="{PRI}" stroke-width="4" stroke-dasharray="6 6"/>'
D["how-to-patch-a-hole-in-drywall-step-1"] = svg(
    HEAD("Match the method to the hole")
    + R(80, 160, 320, 560, PAPER, LINE, 3) + hole(240, 330, 14) + T(240, 470, "Up to 1/2 in", 30, 700, PRI, "middle") + T(240, 520, "Nails, screws,", 26, 500, MUTED, "middle") + T(240, 555, "anchors", 26, 500, MUTED, "middle") + T(240, 640, "Spackle", 32, 700, BRASS, "middle")
    + R(440, 160, 320, 560, PAPER, LINE, 3) + R(520, 250, 160, 160, SAGE, PRI, 3) + hole(600, 330, 48) + T(600, 470, "1/2 in to 4 in", 30, 700, PRI, "middle") + T(600, 520, "Doorknobs, dings", 26, 500, MUTED, "middle") + T(600, 640, "Mesh patch", 32, 700, BRASS, "middle")
    + R(800, 160, 320, 560, PAPER, LINE, 3) + R(880, 240, 160, 180, SAGE2, PRI, 4) + hole(960, 330, 72) + T(960, 470, "Over 4 in", 30, 700, PRI, "middle") + T(960, 520, "Big holes", 26, 500, MUTED, "middle") + T(960, 640, "Drywall piece", 32, 700, BRASS, "middle")
    + T(80, 800, "Every method finishes the same way: thin coats, feathered wide, then prime.", 28, 500), "Drywall repair methods by hole size")

# Drywall 6: feathered coats
D["how-to-patch-a-hole-in-drywall-step-6"] = svg(
    HEAD("Wider and thinner with every coat")
    + R(80, 520, 1040, 80, SAGE2, PRI, 4) + T(600, 650, "Wall", 28, 600, MUTED, "middle")
    + R(520, 500, 160, 20, PRI) + T(600, 480, "Patch", 26, 700, PRI, "middle")
    + f'<path d="M420 520 Q600 488 780 520" fill="none" stroke="{BRASS}" stroke-width="5"/>' + T(600, 430, "Coat 1: about 6 in", 26, 600, INK, "middle")
    + f'<path d="M300 520 Q600 470 900 520" fill="none" stroke="{BRASS}" stroke-width="5" stroke-dasharray="14 8"/>' + T(600, 380, "Coat 2: about 10 in", 26, 600, INK, "middle")
    + f'<path d="M160 520 Q600 455 1040 520" fill="none" stroke="{BRASS}" stroke-width="5" stroke-dasharray="4 8"/>' + T(600, 330, "Coat 3: about 14 in", 26, 600, INK, "middle")
    + T(80, 760, "Let each coat dry fully. Press the knife edges hard so the coat fades to nothing.", 28, 500), "Feathered joint compound coats")

# Toilet 1: tank anatomy
D["how-to-fix-a-running-toilet-step-1"] = svg(
    HEAD("Inside the toilet tank")
    + f'<path d="M260 170 L940 170 L920 720 Q920 760 880 760 L320 760 Q280 760 280 720z" fill="{PAPER}" stroke="{PRI}" stroke-width="5"/>'
    + R(284, 330, 632, 425, SAGE) + L(284, 330, 916, 330, PRI, 3, "12 8")
    + R(360, 230, 34, 520, PAPER, PRI, 4) + R(340, 380, 74, 80, SAGE2, PRI, 4) + T(220, 260, "Fill valve", 28, 700, INK, "end") + L(230, 252, 356, 252, MUTED, 2)
    + T(220, 425, "Float", 28, 700, INK, "end") + L(230, 418, 336, 418, MUTED, 2)
    + R(600, 300, 40, 400, PAPER, PRI, 4) + T(960, 300, "Overflow tube", 28, 700, INK) + L(645, 292, 952, 292, MUTED, 2)
    + f'<ellipse cx="660" cy="712" rx="90" ry="22" fill="{PRI}"/>' + T(960, 720, "Flapper", 28, 700, INK) + L(752, 712, 952, 712, MUTED, 2)
    + L(800, 230, 740, 690, MUTED, 3, "4 6") + R(760, 210, 140, 20, PRI, None, 0, 6) + T(830, 200, "Handle lever", 22, 600, MUTED, "middle") + T(960, 520, "Chain", 28, 700, INK) + T(960, 556, "~1/2 in slack", 24, 600, MUTED) + L(775, 520, 952, 512, MUTED, 2)
    + DIM(660, 300, 660, 330, "", 0, 0) + T(960, 345, "Water line ~1 in", 26, 700, BRASS) + T(960, 380, "below tube top", 26, 700, BRASS), "Toilet tank anatomy")

# Switch 3: single-pole switch
D["how-to-replace-a-light-switch-step-3"] = svg(
    HEAD("Single-pole switch terminals")
    + R(470, 140, 260, 620, PAPER, PRI, 5, 16) + R(555, 360, 90, 180, SAGE, PRI, 4, 10) + T(600, 330, "OFF", 24, 700, MUTED, "middle") + T(600, 580, "ON", 24, 700, MUTED, "middle")
    + f'<circle cx="730" cy="300" r="26" fill="{BRASS}" stroke="{PRI}" stroke-width="3"/><circle cx="730" cy="600" r="26" fill="{BRASS}" stroke="{PRI}" stroke-width="3"/><circle cx="470" cy="690" r="24" fill="#3f7a4a" stroke="{PRI}" stroke-width="3"/>'
    + T(790, 290, "Brass terminal", 30, 700) + T(790, 330, "hot wire (either one)", 26, 500, MUTED)
    + T(790, 590, "Brass terminal", 30, 700) + T(790, 630, "hot wire (either one)", 26, 500, MUTED)
    + T(420, 680, "Green screw", 30, 700, INK, "end") + T(420, 720, "bare copper ground", 26, 500, MUTED, "end")
    + T(100, 830, "Three or more terminals besides ground? It's a 3-way or 4-way switch. Stop here.", 28, 600, WARN), "Single-pole switch terminals")

# Switch 4: clockwise wrap
def screw(cx, cy): return f'<circle cx="{cx}" cy="{cy}" r="60" fill="{BRASS}" stroke="{PRI}" stroke-width="4"/><path d="M{cx-30} {cy}h60M{cx} {cy-30}v60" stroke="{PRI}" stroke-width="6"/>'
D["how-to-replace-a-light-switch-step-4"] = svg(
    HEAD("Wrap wires clockwise")
    + screw(330, 400) + f'<path d="M80 400 L250 400 A82 82 0 1 1 330 482" fill="none" stroke="{PRI}" stroke-width="12" stroke-linecap="round"/>'
    + f'<path d="M420 340 A100 100 0 0 1 380 490" fill="none" stroke="{BRASS}" stroke-width="4" marker-end="url(#a)"/>' + OK(330, 600) + T(330, 680, "Clockwise: tightening pulls", 28, 600, INK, "middle") + T(330, 720, "the loop in", 28, 600, INK, "middle")
    + screw(870, 400) + f'<path d="M1120 400 L950 400 A82 82 0 1 0 870 482" fill="none" stroke="{PRI}" stroke-width="12" stroke-linecap="round"/>'
    + NO(870, 600) + T(870, 680, "Counter-clockwise: tightening", 28, 600, INK, "middle") + T(870, 720, "pushes the wire out", 28, 600, INK, "middle")
    + T(100, 830, "Insulation should reach close to the screw; no bare copper past the screw head.", 28, 500), "Clockwise wire wrap on a terminal screw")

# Weatherstrip 1: leak zones
D["how-to-weatherstrip-a-door-step-1"] = svg(
    HEAD("Where doors usually leak")
    + R(380, 140, 440, 640, None, PRI, 10) + R(400, 160, 400, 610, PAPER, LINE, 3) + f'<circle cx="760" cy="470" r="14" fill="{PRI}"/>'
    + R(780, 200, 24, 540, BRASS) + R(395, 150, 410, 22, BRASS) + R(400, 752, 400, 22, BRASS)
    + T(850, 470, "Latch side", 30, 700) + T(850, 510, "(most common)", 26, 500, MUTED)
    + T(600, 125, "Top + corners", 30, 700, INK, "middle") + T(600, 830, "Bottom: sweep and threshold", 30, 700, INK, "middle")
    + T(100, 300, "Paper test:", 28, 700, PRI) + T(100, 340, "close the door on", 26, 500) + T(100, 375, "a sheet of paper.", 26, 500) + T(100, 410, "Slides out easily?", 26, 500) + T(100, 445, "Seal is too weak.", 26, 500), "Door air leak zones")

# Weatherstrip 2: kerf vs adhesive
D["how-to-weatherstrip-a-door-step-2"] = svg(
    HEAD("Know your weatherstrip type")
    + R(120, 220, 160, 380, SAGE2, PRI, 4) + R(280, 300, 70, 300, SAGE2, PRI, 4) + R(340, 400, 14, 50, MIST) + f'<path d="M354 410 q60 15 0 35" fill="{BRASS}" stroke="{PRI}" stroke-width="3"/>' + R(420, 220, 50, 380, PAPER, PRI, 4)
    + T(300, 680, "Kerf-in", 32, 700, PRI, "middle") + T(300, 720, "Flange pushes into a slot", 26, 500, MUTED, "middle") + T(300, 755, "in the doorstop. Pulls out.", 26, 500, MUTED, "middle")
    + R(700, 220, 160, 380, SAGE2, PRI, 4) + R(860, 300, 70, 300, SAGE2, PRI, 4) + R(930, 380, 28, 90, BRASS, PRI, 3) + R(1000, 220, 50, 380, PAPER, PRI, 4)
    + T(880, 680, "Adhesive foam", 32, 700, PRI, "middle") + T(880, 720, "Sticks to the face of the stop.", 26, 500, MUTED, "middle") + T(880, 755, "Clean with alcohol first.", 26, 500, MUTED, "middle")
    + T(445, 200, "Door", 24, 600, MUTED, "middle") + T(1025, 200, "Door", 24, 600, MUTED, "middle"), "Kerf-in versus adhesive weatherstrip")

# Raised bed 1: reach plan
D["how-to-build-a-raised-garden-bed-step-1"] = svg(
    HEAD("4 ft wide = everything in reach")
    + R(160, 260, 880, 440, SAGE, PRI, 8) + R(160, 260, 880, 220, None, None) + L(170, 480, 1030, 480, BRASS, 3, "14 10")
    + T(600, 380, "Reach from this side", 28, 600, PRI, "middle") + T(600, 600, "Reach from this side", 28, 600, PRI, "middle")
    + DIM(160, 220, 1040, 220, "8 ft", 600, 205) + DIM(1080, 260, 1080, 700, "", 0, 0) + T(1095, 490, "4 ft", 30, 700, BRASS)
    + DIM(120, 260, 120, 480, "", 0, 0) + T(105, 380, "2 ft", 28, 700, BRASS, "end")
    + T(160, 790, "Leave about 2 ft of path around the bed. Pick a spot with 6–8 hours of sun.", 28, 500), "Raised bed reach plan")

# Raised bed 6: section
D["how-to-build-a-raised-garden-bed-step-6"] = svg(
    HEAD("What goes in the bed")
    + R(80, 640, 1040, 120, "url(#hatch)", MUTED, 3) + T(600, 800, "Native soil (grass skimmed off)", 26, 600, MUTED, "middle")
    + R(160, 300, 60, 340, SAGE2, PRI, 4) + R(980, 300, 60, 340, SAGE2, PRI, 4)
    + R(220, 330, 760, 300, "#8a6f4d") + T(600, 470, "~60% topsoil + 40% compost", 32, 700, PAPER, "middle")
    + R(220, 620, 760, 12, "#b9a27c") + L(220, 636, 980, 636, MUTED, 3, "6 6")
    + T(600, 590, "Cardboard over hardware cloth (optional)", 26, 700, PAPER, "middle")
    + DIM(130, 300, 130, 640, "", 0, 0) + T(115, 480, "11 in", 28, 700, BRASS, "end")
    + DIM(240, 300, 240, 330, "", 0, 0) + T(260, 290, "Fill to 1–2 in below the rim", 26, 700, BRASS), "Raised bed cross-section")

# Floating shelf 2: studs
studs = "".join(R(200 + i * 240, 160, 50, 520, SAGE2, PRI, 3) for i in range(4))
D["how-to-install-floating-shelves-step-2"] = svg(
    HEAD("Find the studs behind the drywall")
    + R(120, 160, 960, 520, None, LINE, 3) + studs
    + R(180, 400, 830, 34, PRI, None, 0, 6) + "".join(f'<circle cx="{225 + i*240}" cy="417" r="9" fill="{BRASS}"/>' for i in range(4))
    + R(250, 190, 190, 44, PAPER) + DIM(225, 245, 465, 245, "", 0, 0) + T(345, 222, "16 in on center", 26, 700, BRASS, "middle")
    + R(900, 448, 120, 40, PAPER) + T(960, 476, "Bracket", 26, 700, PRI, "middle")
    + T(120, 760, "Mark both edges of each stud and confirm with a finish nail.", 28, 500)
    + T(120, 805, "Avoid drilling straight above or below outlets and switches.", 28, 600, WARN), "Studs behind drywall with bracket")

# Floating shelf 4: section
D["how-to-install-floating-shelves-step-4"] = svg(
    HEAD("Let the studs carry the load")
    + R(240, 150, 100, 600, SAGE2, PRI, 4) + T(290, 140, "Stud", 26, 700, PRI, "middle")
    + R(340, 150, 30, 600, PAPER, PRI, 3) + T(355, 790, "Drywall", 24, 600, MUTED, "middle")
    + R(370, 390, 24, 90, PRI) + L(260, 435, 394, 435, BRASS, 8) + T(150, 430, "Screw", 26, 700, BRASS, "end")
    + R(394, 410, 400, 16, PRI, None, 0, 4) + R(394, 450, 400, 16, PRI, None, 0, 4)
    + R(400, 380, 520, 110, "none", BRASS, 4, 6) + T(660, 360, "Shelf slides over the rods", 26, 600, INK, "middle")
    + f'<path d="M700 520 v100" stroke="{PRI}" stroke-width="4" marker-end="url(#p)"/>' + T(720, 600, "Load", 26, 600, PRI)
    + T(140, 860, "Anchors only where no stud lands, rated for the load. Never the plastic plugs in the box.", 26, 500), "Floating shelf bracket into stud")

# Gutters 1: ladder 4:1
D["how-to-clean-gutters-step-1"] = svg(
    HEAD("Set the ladder at 4 to 1")
    + R(120, 300, 360, 470, PAPER, PRI, 4) + f'<polygon points="100,300 500,300 300,170" fill="{SAGE2}" stroke="{PRI}" stroke-width="4"/>'
    + R(480, 290, 40, 26, PAPER, PRI, 3) + T(470, 340, "Gutter", 24, 600, MUTED, "end")
    + L(80, 770, 1120, 770, PRI, 4)
    + L(640, 770, 480, 200, PRI, 8) + L(660, 770, 500, 200, PRI, 8)
    + DIM(700, 300, 700, 770, "", 0, 0) + T(720, 545, "4 ft up", 30, 700, BRASS)
    + DIM(490, 810, 650, 810, "1 ft out", 570, 860)
    + DIM(540, 300, 520, 200, "", 0, 0) + T(560, 225, "3 ft above edge", 26, 700, BRASS) + T(560, 255, "(only if stepping off)", 22, 600, MUTED)
    + T(780, 420, "Use a stabilizer so the", 26, 500) + T(780, 455, "ladder rests on the wall,", 26, 500) + T(780, 490, "not the gutter.", 26, 500), "Ladder 4 to 1 setup")

# Gutters 4: downspout
D["how-to-clean-gutters-step-4"] = svg(
    HEAD("Send water away from the foundation")
    + R(100, 160, 260, 600, PAPER, PRI, 4) + T(230, 470, "House", 28, 600, MUTED, "middle")
    + R(100, 140, 380, 40, SAGE2, PRI, 4) + R(400, 180, 40, 520, SAGE2, PRI, 4)
    + f'<path d="M400 700 L440 700 L520 740 L1060 740 L1060 770 L500 770 L400 730z" fill="{SAGE2}" stroke="{PRI}" stroke-width="4"/>'
    + L(80, 770, 1140, 770, PRI, 4) + R(80, 770, 1060, 60, "url(#hatch)")
    + f'<path d="M1070 760 q40 10 70 30" stroke="{BRASS}" stroke-width="5" fill="none" marker-end="url(#a)"/>'
    + DIM(360, 700, 1060, 700, "4–6 ft minimum", 710, 685)
    + T(500, 172, "Gutter pitches toward the downspout", 24, 700, BRASS), "Downspout extension diagram")

# ─────────────── Batch 2
D["how-to-winterize-outdoor-faucets-step-2"] = svg(
    HEAD("Where each faucet type closes")
    + R(560, 150, 80, 330, "url(#hatch)", MUTED, 3) + T(600, 140, "Wall", 24, 700, MUTED, "middle") + T(330, 140, "Outside (freezing)", 26, 700, INK, "middle") + T(880, 140, "Inside (heated)", 26, 700, INK, "middle")
    + R(440, 230, 130, 40, SAGE2, PRI, 4) + R(630, 238, 440, 24, SAGE, PRI, 3) + f'<circle cx="575" cy="250" r="20" fill="{WARN}"/>' + T(330, 320, "Standard: closes here", 26, 700, WARN, "middle") + T(330, 355, "water sits at the cold wall", 24, 500, MUTED, "middle")
    + R(440, 560, 130, 40, SAGE2, PRI, 4) + R(570, 568, 260, 24, SAGE2, PRI, 3) + R(830, 568, 240, 24, SAGE, PRI, 3) + f'<circle cx="830" cy="580" r="20" fill="{PRI}"/>'
    + R(560, 500, 80, 160, "url(#hatch)", MUTED, 3) + T(330, 650, "Frost-free: closes here", 26, 700, PRI, "middle") + T(330, 685, "long body reaches inside", 24, 500, MUTED, "middle")
    + T(60, 800, "Either way: disconnect the hose so the faucet body can drain.", 28, 600, INK), "Standard versus frost-free outdoor faucet")
D["how-to-install-a-door-sweep-step-3"] = svg(
    HEAD("Set the sweep height")
    + R(420, 140, 120, 560, PAPER, PRI, 5) + T(480, 130, "Door", 26, 700, PRI, "middle")
    + R(540, 560, 40, 120, SAGE2, PRI, 4) + f'<path d="M560 680 q10 30 30 34" stroke="{BRASS}" stroke-width="10" fill="none" stroke-linecap="round"/>'
    + '<circle cx="560" cy="590" r="6" fill="' + PRI + '"/><circle cx="560" cy="640" r="6" fill="' + PRI + '"/>'
    + R(300, 712, 600, 36, SAGE, PRI, 4) + T(600, 790, "Threshold", 26, 600, MUTED, "middle")
    + T(620, 600, "Screw-on sweep", 28, 700) + T(620, 640, "on the inside face", 24, 500, MUTED) + T(640, 700, "Seal brushes the threshold", 26, 700, BRASS)
    + T(60, 860, "Use the slotted holes so you can raise it if the door drags.", 26, 500), "Door sweep height diagram")
D["how-to-change-hvac-air-filter-step-4"] = svg(
    HEAD("Point the arrow toward the furnace")
    + R(700, 180, 300, 560, SAGE2, PRI, 5) + T(850, 460, "Furnace /", 30, 700, PRI, "middle") + T(850, 500, "air handler", 30, 700, PRI, "middle")
    + R(160, 380, 470, 160, SAGE, PRI, 4) + T(300, 580, "Return duct (from the room)", 26, 600, PRI, "middle")
    + R(630, 360, 40, 200, PAPER, BRASS, 5) + T(650, 600, "Filter", 26, 700, BRASS, "middle")
    + f'<path d="M520 300 h300" stroke="{BRASS}" stroke-width="6" marker-end="url(#a)"/>' + T(670, 280, "Arrow on filter frame", 26, 700, BRASS, "middle")
    + "".join(f'<path d="M{x} 460 h60" stroke="{PRI}" stroke-width="4" marker-end="url(#p)"/>' for x in (200, 360, 520))
    + T(60, 820, "Air flows from the room, through the filter, into the furnace.", 28, 500), "Air filter arrow direction")
D["how-to-fix-drywall-nail-pops-step-2"] = svg(
    HEAD("Lock the panel to the stud")
    + R(500, 140, 200, 640, SAGE2, PRI, 4) + T(600, 130, "Stud (behind drywall)", 26, 700, PRI, "middle")
    + f'<circle cx="600" cy="460" r="22" fill="{PAPER}" stroke="{WARN}" stroke-width="5"/>' + T(740, 470, "Popped nail: set it", 28, 700, WARN)
    + f'<circle cx="600" cy="340" r="14" fill="{PRI}"/><circle cx="600" cy="580" r="14" fill="{PRI}"/>' + T(740, 350, "New screw", 28, 700) + T(740, 590, "New screw", 28, 700)
    + DIM(460, 340, 460, 460, "", 0, 0) + T(440, 410, "1½ in", 28, 700, BRASS, "end") + DIM(460, 460, 460, 580, "", 0, 0) + T(440, 530, "1½ in", 28, 700, BRASS, "end")
    + T(60, 850, "Press the drywall tight, then dimple each screw just below the surface.", 28, 500), "Nail pop screw placement")
D["gfci-outlet-wont-reset-step-3"] = svg(
    HEAD("One GFCI can protect other rooms")
    + R(100, 340, 220, 260, PAPER, PRI, 5, 16) + T(210, 320, "GFCI (garage)", 26, 700, PRI, "middle") + R(150, 400, 120, 40, BRASS, None, 0, 6) + T(210, 428, "RESET", 20, 700, PAPER, "middle") + R(150, 460, 120, 40, SAGE, PRI, 2, 6) + T(210, 488, "TEST", 20, 700, PRI, "middle")
    + "".join(R(x, 380, 160, 200, PAPER, MUTED, 3, 14) + T(x+80, 360, lbl, 24, 600, MUTED, "middle") for x, lbl in ((430, "Outdoor"), (660, "Bathroom 2"), (890, "Garage wall")))
    + L(320, 480, 430, 480, PRI, 5) + L(590, 480, 660, 480, PRI, 5) + L(820, 480, 890, 480, PRI, 5)
    + T(100, 700, "If any of these outlets is dead, reset the GFCI upstream first.", 28, 600)
    + T(100, 745, "Check every GFCI: bathrooms, kitchen, garage, basement, outside.", 26, 500, MUTED), "GFCI upstream protection")
D["how-to-unclog-a-kitchen-sink-step-3"] = svg(
    HEAD("Parts of a sink P-trap")
    + R(300, 150, 600, 120, SAGE, PRI, 4) + T(600, 220, "Sink basin", 28, 700, PRI, "middle")
    + R(570, 270, 60, 180, SAGE2, PRI, 4) + T(540, 360, "Tailpiece", 26, 700, INK, "end")
    + f'<path d="M570 450 v80 a70 70 0 0 0 140 0 v-60" fill="none" stroke="{PRI}" stroke-width="40"/>' + T(640, 650, "Trap", 28, 700, INK, "middle")
    + R(690, 450, 300, 40, SAGE2, PRI, 4) + T(1000, 440, "Trap arm → wall", 26, 700, INK, "end")
    + R(555, 440, 90, 20, BRASS) + R(680, 460, 20, 60, BRASS) + T(480, 470, "Slip nut", 26, 700, BRASS, "end") + T(730, 560, "Slip nut", 26, 700, BRASS)
    + f'<path d="M540 680 h200 l-20 120 h-160z" fill="none" stroke="{MUTED}" stroke-width="4"/>' + T(640, 760, "Bucket", 24, 600, MUTED, "middle"), "Kitchen sink P-trap parts")
D["how-to-replace-a-showerhead-step-3"] = svg(
    HEAD("Wrap thread tape clockwise")
    + R(140, 380, 520, 90, SAGE2, PRI, 5) + T(300, 520, "Shower arm (from wall)", 26, 600, MUTED, "middle")
    + "".join(L(660 + i*28, 372, 660 + i*28 + 14, 478, PRI, 4) for i in range(6)) + R(660, 380, 170, 90, "none", PRI, 4)
    + f'<path d="M700 360 a70 70 0 1 1 -10 140" fill="none" stroke="{BRASS}" stroke-width="5" marker-end="url(#a)"/>'
    + T(880, 300, "3–4 wraps", 26, 700, INK) + f'<circle cx="1000" cy="470" r="70" fill="{SAGE2}" stroke="{PRI}" stroke-width="4"/><circle cx="1000" cy="470" r="26" fill="{MIST}" stroke="{PRI}" stroke-width="3"/>' + f'<path d="M1000 380 a90 90 0 0 1 88 108" fill="none" stroke="{BRASS}" stroke-width="6" marker-end="url(#a)"/>' + T(1000, 590, "End view: clockwise", 24, 700, BRASS, "middle")
    + T(140, 680, "Wrapping this way means screwing the head on tightens the tape", 28, 500) + T(140, 720, "instead of peeling it off.", 28, 500), "Thread tape wrap direction")
D["how-to-fix-squeaky-floors-step-2"] = svg(
    HEAD("Pull the subfloor tight to the joist")
    + R(100, 300, 1000, 40, SAGE, PRI, 3) + T(1090, 290, "Carpet or hardwood", 24, 600, MUTED, "end")
    + R(100, 340, 1000, 50, SAGE2, PRI, 4) + T(1090, 420, "Subfloor", 24, 600, MUTED, "end")
    + "".join(R(x, 390, 60, 260, PAPER, PRI, 4) for x in (200, 520, 840)) + T(550, 700, "Joists", 26, 700, PRI, "middle")
    + L(550, 250, 550, 520, BRASS, 8) + f'<path d="M538 250 h24" stroke="{BRASS}" stroke-width="8"/>' + T(580, 240, "Breakaway screw", 26, 700, BRASS)
    + DIM(230, 760, 550, 760, "16 in on center", 390, 745)
    + T(100, 850, "Tap the floor: it sounds solid over a joist and hollow between.", 26, 500), "Squeaky floor screw into joist")
D["how-to-fix-a-sagging-gate-step-4"] = svg(
    HEAD("Cable pulls, brace pushes")
    + R(100, 180, 60, 600, SAGE2, PRI, 4) + T(130, 170, "Hinge post", 22, 700, PRI, "middle")
    + R(180, 220, 440, 480, PAPER, PRI, 5) + R(190, 230, 420, 30, SAGE) + R(190, 660, 420, 30, SAGE)
    + L(200, 250, 600, 680, BRASS, 6) + f'<rect x="385" y="450" width="40" height="16" fill="{PRI}" transform="rotate(47 405 458)"/>'
    + T(390, 820, "Cable: top hinge corner → bottom latch", 24, 700, BRASS, "middle")
    + R(720, 180, 60, 600, SAGE2, PRI, 4)
    + R(800, 220, 340, 480, PAPER, PRI, 5) + R(810, 230, 320, 30, SAGE) + R(810, 660, 320, 30, SAGE)
    + f'<polygon points="815,660 845,690 1130,262 1100,232" fill="{SAGE2}" stroke="{PRI}" stroke-width="3"/>'
    + T(960, 820, "Brace: bottom hinge → top latch", 24, 700, PRI, "middle")
    + T(600, 870, "Hinges are on the left of each gate.", 24, 500, MUTED, "middle"), "Anti-sag cable and brace directions")
D["how-to-find-a-stud-without-a-stud-finder-step-2"] = svg(
    HEAD("Clues that point to studs")
    + R(100, 150, 1000, 560, None, LINE, 3)
    + "".join(R(150 + i*240, 150, 40, 560, SAGE2, PRI, 3) for i in range(4))
    + R(190, 420, 60, 90, PAPER, PRI, 4, 6) + T(260, 470, "Outlet box", 22, 700, INK)
    + R(100, 680, 1000, 30, SAGE, PRI, 3) + "".join(f'<circle cx="{170 + i*240}" cy="695" r="6" fill="{BRASS}"/>' for i in range(4)) + T(1095, 670, "Trim nails", 22, 700, BRASS, "end")
    + "".join(f'<circle cx="{170 + i*240}" cy="{y}" r="5" fill="{PRI}"/>' for i in range(4) for y in (220, 340, 580))
    + DIM(170, 760, 410, 760, "16 in on center", 290, 745)
    + T(100, 850, "Combine two or three clues, then confirm with a hidden test nail.", 26, 500), "Stud finding clues")

def CELL(x, y, name, val, hint, good):
    return (R(x, y, 470, 230, PAPER, PRI, 4, 10) + T(x+30, y+55, name, 28, 700, PRI) + T(x+30, y+130, val, 56, 700, INK)
            + T(x+30, y+180, hint, 24, 600, MUTED) + T(x+440, y+130, good, 26, 700, BRASS, "end"))
D["are-replacement-windows-worth-it-step-5"] = svg(
    HEAD("Reading a window's energy label")
    + T(60, 135, "Example values. Compare the same four numbers on every quote.", 26, 500, MUTED)
    + CELL(100, 180, "U-factor", "0.27", "Heat loss through the window", "Lower = warmer")
    + CELL(630, 180, "Solar heat gain", "0.25", "Sun heat that comes through", "Lower = cooler")
    + CELL(100, 450, "Visible light", "0.48", "Daylight that comes through", "Higher = brighter")
    + CELL(630, 450, "Air leakage", "0.1", "Drafts through the frame", "Lower = tighter")
    + T(100, 760, "Cold climate: focus on a low U-factor.", 28, 600)
    + T(100, 805, "Hot, sunny climate: focus on a low solar heat gain number.", 28, 600)
    + T(100, 850, "Then check ENERGY STAR certification for your climate zone.", 26, 500, MUTED), "Window energy label explained")

def SH(x, y, w=70, h=34): return R(x, y, w, h, SAGE2, PRI, 2, 2)
_rows = "".join(SH(270 + c*74 - (r % 2)*37, 240 + r*38) for r in range(9) for c in range(9) if 270 + c*74 - (r % 2)*37 >= 240 and 270 + c*74 - (r % 2)*37 <= 860)
_S, _DX, _DY = 0.72, -60, 70          # house drawn at 1:1 below, then scaled into the left of the canvas
def _p(x, y): return round(_DX + x * _S), round(_DY + y * _S)
_house = (
    f'<clipPath id="roof"><polygon points="200,590 280,230 900,230 980,590"/></clipPath>'
    + f'<polygon points="200,590 280,230 900,230 980,590" fill="{SAGE}" stroke="{PRI}" stroke-width="5"/>'
    + f'<g clip-path="url(#roof)">{_rows}</g>'
    + f'<path d="M280 230 Q590 262 900 230" fill="none" stroke="{BRASS}" stroke-width="6"/>'           # sagging ridge
    + R(568, 316, 70, 34, MIST, PRI, 2, 2)                                                              # missing shingle
    + f'<path d="M642 392 h70 v34 h-70 z" fill="{SAGE2}" stroke="{PRI}" stroke-width="2"/><path d="M642 392 q35 -30 70 0" fill="{SAGE2}" stroke="{PRI}" stroke-width="3"/>'  # curling
    + f'<ellipse cx="800" cy="520" rx="80" ry="34" fill="{MUTED}" opacity="0.55"/>'                     # bald patch
    + R(770, 150, 70, 120, SAGE2, PRI, 4) + L(762, 270, 848, 270, BRASS, 6, "10 8")                     # chimney flashing
    + R(230, 590, 720, 220, PAPER, PRI, 5) + R(330, 650, 110, 110, MIST, PRI, 4) + R(740, 650, 110, 110, MIST, PRI, 4) + R(540, 670, 90, 140, SAGE, PRI, 4)
    + R(950, 600, 22, 200, SAGE2, PRI, 3) + "".join(f'<circle cx="{960 + dx}" cy="{818 + dy}" r="5" fill="{MUTED}"/>' for dx, dy in ((-20, 0), (-8, 6), (4, -2), (16, 5), (28, 1), (-30, 6), (40, 4)))
)
_LX = 760
def _lab(pt, y, text):
    x, yy = _p(*pt); return LEAD(x, yy, _LX, y, text)
D["signs-your-roof-needs-replacement-step-2"] = svg(
    HEAD("What to look for from the ground")
    + f'<g transform="translate({_DX} {_DY}) scale({_S})">{_house}</g>'
    + _lab((450, 240), 210, "Sagging ridge")
    + _lab((808, 270), 265, "Loose flashing")
    + _lab((603, 333), 320, "Missing shingle")
    + _lab((677, 395), 375, "Curling edges")
    + _lab((800, 520), 430, "Bald patch (granules gone)")
    + _lab((985, 818), 640, "Grit at the downspout")
    + T(60, 760, "One sign alone is often a repair.", 28, 600)
    + T(60, 805, "Several across the roof usually means it's near the end of its life.", 28, 600)
    + T(60, 850, "Use binoculars and stay on the ground.", 26, 500, MUTED),
    "Roof warning signs seen from the ground")

# ── Batch 3 diagrams (2026-11-02)
def NOTE(lines, y0=770):
    return "".join(T(60, y0 + i*44, t, 28 if i == 0 else 26, 600 if i == 0 else 500, INK if i == 0 else MUTED) for i, t in enumerate(lines))
def hexagon(cx, cy, r, fill, stroke):
    import math
    pts = " ".join(f"{cx + r*math.cos(math.radians(a)):.1f},{cy + r*math.sin(math.radians(a)):.1f}" for a in range(0, 360, 60))
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="4"/>'

D["garbage-disposal-humming-not-working-step-3"] = svg(
    HEAD("Underside of a garbage disposal")
    + f'<circle cx="430" cy="430" r="260" fill="{SAGE}" stroke="{PRI}" stroke-width="6"/>'
    + f'<circle cx="430" cy="430" r="200" fill="none" stroke="{SAGE2}" stroke-width="4" stroke-dasharray="10 10"/>'
    + hexagon(430, 430, 34, PAPER, PRI)
    + f'<path d="M430 430 L430 300 L520 300" fill="none" stroke="{BRASS}" stroke-width="14" stroke-linecap="round" stroke-linejoin="round"/>'
    + R(560, 560, 44, 44, BRASS, PRI, 4, 6)
    + f'<path d="M230 600 q-60 90 -150 110" fill="none" stroke="{MUTED}" stroke-width="10" stroke-linecap="round"/>'
    + LEAD(430, 430, 760, 360, "Hex socket (1/4 in)")
    + LEAD(530, 300, 760, 260, "Wrench: crank both ways")
    + LEAD(582, 582, 760, 560, "Reset button")
    + LEAD(120, 690, 760, 660, "Power cord: unplug first")
    + NOTE(["Turn the wrench until it spins in full circles.", "If the reset button pops back out, wait about 10 minutes."]),
    "Garbage disposal hex socket and reset button")

D["slow-draining-bathroom-sink-step-1"] = svg(
    HEAD("Parts of a pop-up sink drain")
    + f'<path d="M120 170 H760 Q740 330 440 330 Q140 330 120 170 Z" fill="{PAPER}" stroke="{PRI}" stroke-width="5"/>'
    + R(415, 300, 50, 300, SAGE2, PRI, 4)
    + f'<path d="M405 240 h70 v24 h-70 z" fill="{BRASS}" stroke="{PRI}" stroke-width="3"/>' + L(440, 264, 440, 470, BRASS, 6)
    + L(440, 470, 640, 470, PRI, 6) + R(452, 456, 40, 28, BRASS, PRI, 3, 4)
    + R(632, 300, 14, 300, SAGE2, PRI, 3) + L(560, 200, 560, 150, MUTED, 6) + L(560, 200, 610, 310, MUTED, 4)
    + f'<path d="M415 600 v60 a70 70 0 0 0 140 0 v-30 h220" fill="none" stroke="{PRI}" stroke-width="36" stroke-linejoin="round"/>'
    + LEAD(440, 252, 820, 220, "Stopper")
    + LEAD(472, 470, 820, 430, "Pivot nut + rod")
    + LEAD(639, 380, 820, 330, "Lift strap")
    + LEAD(485, 700, 820, 650, "P-trap")
    + NOTE(["Hair usually wraps around the stopper's post.", "Loosen the pivot nut to lift the stopper out."]),
    "Pop-up sink drain parts")

def _floor(x, w, h, label):
    return R(x, 520 - h, w, h, SAGE2, PRI, 3) + T(x + w/2, 560, label, 22, 600, MUTED, "middle")
def _panel(x0, title, profile):
    return (T(x0 + 160, 200, title, 30, 700, PRI, "middle") + R(x0, 520, 320, 30, SAGE, PRI, 3)
            + profile + L(x0, 580, x0 + 320, 580, LINE, 2))
D["how-to-install-floor-transition-strips-step-1"] = svg(
    HEAD("Three transition profiles")
    + _panel(60, "T-molding",
        _floor(60, 130, 50, "") + _floor(250, 130, 50, "") + R(205, 500, 30, 20, BRASS, PRI, 2)
        + f'<path d="M170 470 H270 V480 H232 V515 H208 V480 H170 Z" fill="{PAPER}" stroke="{PRI}" stroke-width="4"/>')
    + _panel(440, "Reducer",
        _floor(440, 130, 50, "") + _floor(630, 130, 18, "") + R(585, 500, 30, 20, BRASS, PRI, 2)
        + f'<path d="M550 470 H600 L680 500 V502 H612 V515 H588 V480 H550 Z" fill="{PAPER}" stroke="{PRI}" stroke-width="4"/>')
    + _panel(820, "End cap",
        _floor(820, 170, 50, "") + R(1010, 380, 40, 140, SAGE, PRI, 3) + R(995, 500, 20, 20, BRASS, PRI, 2)
        + f'<path d="M960 470 H1005 V515 H985 V480 H960 Z" fill="{PAPER}" stroke="{PRI}" stroke-width="4"/>' + T(1030, 370, "Door", 20, 600, MUTED, "middle"))
    + T(220, 620, "Same height on both sides", 24, 600, INK, "middle") + T(600, 620, "Thicker floor to thinner", 24, 600, INK, "middle") + T(980, 620, "Edge against a door", 24, 600, INK, "middle")
    + T(60, 690, "Brass = track, fastened to the subfloor in the gap.", 26, 700, BRASS)
    + NOTE(["Never screw or glue the molding through a floating floor.", "Leave the expansion gap your flooring maker specifies."], 760),
    "T-molding, reducer and end cap cross-sections")

D["how-to-paint-a-room-step-1"] = svg(
    HEAD("How much paint? A worked example")
    + T(60, 140, "12 x 12 ft room, 8 ft ceiling, 1 door, 1 window, 2 coats", 28, 500, MUTED)
    + "".join(R(60, 180 + i*110, 1080, 90, PAPER if i < 4 else SAGE, PRI if i == 4 else LINE, 3, 10)
              + T(90, 237 + i*110, a, 30, 600, INK) + T(1110, 237 + i*110, b, 32, 700, PRI if i == 4 else INK, "end")
              for i, (a, b) in enumerate([("Wall area: 4 walls x 12 ft x 8 ft", "384 sq ft"),
                                         ("Minus 1 door (20) and 1 window (15)", "349 sq ft"),
                                         ("Two coats: 349 x 2", "698 sq ft"),
                                         ("Divide by 350 sq ft per gallon", "2.0 gallons"),
                                         ("Buy", "2 gallons")]))
    + NOTE(["Use 350 sq ft per gallon to be safe; labels often say 350–400.", "Bare drywall, textured walls and dark colors need more."], 770),
    "Paint quantity calculation example")

D["how-to-find-main-water-shut-off-valve-step-3"] = svg(
    HEAD("Which way is off?")
    + T(300, 170, "Ball valve (lever)", 30, 700, PRI, "middle") + T(900, 170, "Gate valve (wheel)", 30, 700, PRI, "middle")
    + R(80, 330, 440, 50, SAGE2, PRI, 4) + R(250, 300, 100, 110, SAGE, PRI, 4) + L(300, 300, 300, 270, PRI, 8)
    + R(290, 255, 170, 26, BRASS, PRI, 3, 6) + T(300, 450, "ON: lever along the pipe", 26, 600, INK, "middle")
    + R(80, 640, 440, 50, SAGE2, PRI, 4) + R(250, 610, 100, 110, SAGE, PRI, 4) + L(300, 610, 300, 590, PRI, 8)
    + R(287, 490, 26, 110, BRASS, PRI, 3, 6) + T(300, 760, "OFF: lever across the pipe", 26, 700, PRI, "middle")
    + R(680, 450, 440, 50, SAGE2, PRI, 4) + R(850, 400, 100, 150, SAGE, PRI, 4) + L(900, 400, 900, 330, PRI, 8)
    + f'<circle cx="900" cy="300" r="90" fill="none" stroke="{BRASS}" stroke-width="14"/>' + L(810, 300, 990, 300, BRASS, 8) + L(900, 210, 900, 390, BRASS, 8)
    + f'<path d="M960 190 A120 120 0 0 1 1020 300" fill="none" stroke="{PRI}" stroke-width="6" marker-end="url(#p)"/>'
    + T(900, 600, "Turn clockwise until it stops", 26, 700, PRI, "middle")
    + NOTE(["Don't force a stuck valve. Old gate valves can break.", "Test it: close it and check that a faucet stops running."], 820),
    "Ball valve and gate valve shut-off directions")

def _breaker(x, pos, label, flag=False):
    hy = {"on": 250, "mid": 330, "off": 410}[pos]
    return (R(x, 200, 160, 300, PAPER, PRI, 4, 10) + R(x + 60, 230, 40, 240, SAGE, LINE, 2, 6)
            + R(x + 40, hy - 26, 80, 52, PRI if not flag else BRASS, PRI, 3, 8)
            + T(x + 80, 540, label, 28, 700, INK if not flag else BRASS, "middle"))
D["how-to-reset-a-tripped-breaker-step-2"] = svg(
    HEAD("Reading a breaker")
    + _breaker(100, "on", "ON") + _breaker(380, "mid", "TRIPPED", True) + _breaker(660, "off", "OFF")
    + T(940, 260, "To reset:", 30, 700, PRI)
    + T(940, 320, "1. Push firmly", 28, 600) + T(940, 360, "    to OFF", 28, 600)
    + T(940, 420, "2. Then back", 28, 600) + T(940, 460, "    to ON", 28, 600)
    + f'<path d="M560 330 C620 330 620 410 650 410" fill="none" stroke="{BRASS}" stroke-width="5" marker-end="url(#a)"/>'
    + NOTE(["A tripped handle rests in the middle; some show an orange flag.", "Trips again with nothing plugged in? Leave it off and call an electrician."], 640),
    "Circuit breaker ON, tripped and OFF positions")

D["how-to-fix-a-door-that-sticks-step-3"] = svg(
    HEAD("A long screw pulls a sagging door back")
    + R(80, 160, 360, 560, None, PRI, 8)
    + f'<polygon points="96,176 424,186 424,704 96,704" fill="{SAGE}" stroke="{PRI}" stroke-width="4"/>'
    + R(88, 230, 16, 70, BRASS) + R(88, 600, 16, 70, BRASS)
    + f'<ellipse cx="410" cy="186" rx="40" ry="14" fill="none" stroke="{WARN}" stroke-width="5"/>' + T(300, 150, "Rubs here", 24, 700, WARN, "middle")
    + T(620, 170, "Top hinge, seen from above", 28, 700, PRI)
    + R(560, 330, 560, 80, SAGE, PRI, 4) + T(840, 380, "Wall stud (framing)", 24, 600, MUTED, "middle")
    + R(560, 250, 560, 60, SAGE2, PRI, 4) + T(840, 290, "Door jamb", 24, 600, MUTED, "middle")
    + R(600, 230, 120, 20, BRASS) + T(660, 220, "Hinge", 22, 700, BRASS, "middle")
    + L(640, 240, 640, 290, MUTED, 6) + T(600, 470, "Short screw:", 24, 600, MUTED) + T(600, 500, "jamb only", 24, 600, MUTED)
    + L(690, 240, 690, 400, PRI, 8) + f'<path d="M682 400 L690 418 L698 400 Z" fill="{PRI}"/>' + T(760, 470, "3-inch screw:", 24, 700, PRI) + T(760, 500, "reaches the stud", 24, 700, PRI)
    + f'<path d="M800 560 C760 520 720 520 700 540" fill="none" stroke="{BRASS}" stroke-width="5" marker-end="url(#a)"/>' + T(820, 575, "Pulls the hinge, and the door,", 24, 600) + T(820, 607, "back toward the frame", 24, 600)
    + NOTE(["Replace the screw closest to the doorstop in the top hinge.", "Tighten every hinge screw before you sand or plane."], 790),
    "Long hinge screw fixing a sagging door")

D["how-to-install-low-voltage-path-lights-step-1"] = svg(
    HEAD("Path light layout")
    + R(60, 150, 1080, 70, SAGE2, PRI, 4) + T(600, 195, "House wall", 26, 600, PRI, "middle")
    + R(140, 230, 60, 60, PAPER, PRI, 4) + T(170, 270, "GFCI", 18, 700, INK, "middle")
    + R(220, 230, 90, 70, BRASS, PRI, 4) + T(325, 275, "Transformer", 22, 700, BRASS)
    + f'<path d="M260 380 C420 420 520 560 640 600 S900 640 1120 560" fill="none" stroke="{SAGE}" stroke-width="110" stroke-linecap="round"/>'
    + f'<path d="M265 300 L265 330 C300 470 470 500 600 520 S900 560 1120 480" fill="none" stroke="{PRI}" stroke-width="4" stroke-dasharray="14 10"/>'
    + "".join(f'<circle cx="{x}" cy="{y}" r="18" fill="{PAPER}" stroke="{BRASS}" stroke-width="6"/>' for x, y in ((380, 470), (560, 650), (720, 545), (900, 680), (1060, 520)))
    + DIM(380, 760, 560, 760, "8–10 ft", 470, 745) + T(640, 610, "Path", 26, 700, PRI, "middle")
    + LEAD(600, 520, 760, 440, "Cable along the path edge")
    + T(60, 850, "Stagger lights on alternate sides. Keep the load under about 80% of the transformer rating.", 24, 600),
    "Low-voltage path light layout")

D["how-to-choose-and-install-drywall-anchors-step-2"] = svg(
    HEAD("Match the anchor to the load")
    + "".join(R(x, 180, 40, 440, PAPER, PRI, 4) + T(x + 20, 660, t, 30, 700, PRI, "middle") + T(x + 20, 700, sub, 24, 600, MUTED, "middle")
              for x, t, sub in ((180, "Light", "plastic expansion"), (580, "Medium", "self-drilling threaded"), (980, "Heavy", "toggle bolt")))
    + f'<path d="M120 390 h60 l40 -12 v44 l-40 -12 h-60 z" fill="{SAGE2}" stroke="{PRI}" stroke-width="3"/>' + L(60, 400, 230, 400, BRASS, 6)
    + f'<path d="M520 380 h70 v40 h-70 z" fill="{SAGE2}" stroke="{PRI}" stroke-width="3"/>' + "".join(L(590 + i*10, 384, 596 + i*10, 416, PRI, 3) for i in range(3)) + L(460, 400, 640, 400, BRASS, 6)
    + L(860, 400, 1060, 400, BRASS, 6) + R(1022, 300, 18, 200, SAGE2, PRI, 3)
    + T(60, 160, "Drywall", 22, 600, MUTED)
    + NOTE(["Use a stud for anything heavy, and always for TV mounts.", "Stay well under the weight rating on the package."], 770),
    "Drywall anchor types by load")

D["how-to-test-and-replace-smoke-alarms-step-1"] = svg(
    HEAD("Where smoke alarms go (one level)")
    + R(60, 140, 1080, 600, PAPER, PRI, 5)
    + R(60, 140, 360, 300, None, PRI, 3) + T(240, 290, "Bedroom", 26, 600, MUTED, "middle")
    + R(420, 140, 300, 300, None, PRI, 3) + T(570, 290, "Bedroom", 26, 600, MUTED, "middle")
    + R(60, 440, 660, 100, None, PRI, 3) + T(540, 500, "Hallway", 26, 600, MUTED, "middle")
    + R(720, 140, 420, 400, None, PRI, 3) + T(930, 220, "Kitchen", 26, 600, MUTED, "middle")
    + R(60, 540, 1080, 200, None, PRI, 3) + T(400, 650, "Living room", 26, 600, MUTED, "middle")
    + R(950, 300, 80, 80, SAGE2, PRI, 3) + T(990, 350, "Stove", 18, 700, INK, "middle")
    + f'<circle cx="990" cy="340" r="135" fill="none" stroke="{WARN}" stroke-width="3" stroke-dasharray="10 8"/>' + T(740, 520, "Keep alarms 10 ft from the stove", 22, 700, WARN)
    + "".join(f'<circle cx="{x}" cy="{y}" r="22" fill="{PAPER}" stroke="{BRASS}" stroke-width="6"/><circle cx="{x}" cy="{y}" r="6" fill="{BRASS}"/>' for x, y in ((240, 220), (570, 220), (230, 490), (760, 650)))
    + T(60, 790, "Alarm in every bedroom, outside each sleeping area, and on every level.", 26, 700)
    + T(60, 835, "Interconnected alarms are best: when one sounds, they all sound.", 24, 500, MUTED),
    "Smoke alarm placement floor plan")

for stem, s in D.items():
    (OUT / f"{stem}.svg").write_text(s)
print(f"wrote {len(D)} diagrams")
