"""HIH long-form #1 — Water Softener Maintenance (animated cutaway explainer)."""
import json, math, random, subprocess, sys
import cairo

sys.path.insert(0, "/home/claude/social/lf")
from toilet_sample import (W, H, FPS, NAVY, NAVY2, CREAM, PAPER, AMBER, BODY, RED, GREEN, WATER,
                           WATER_D, INTERIOR, PORC, clamp, ease, back, prog, rrect, font, text,
                           text_w, pop, check)

TIM = json.load(open("/home/claude/social/ws/timing.json"))
DUR = TIM["total"]

TEAL = (98/255, 196/255, 178/255)
BEAD = (250/255, 218/255, 170/255)
RUST = (178/255, 92/255, 52/255)
GREY = (128/255, 136/255, 146/255)
SALT = (255/255, 255/255, 255/255)
SLUDGE = (140/255, 116/255, 88/255)
WOOD = (196/255, 150/255, 98/255)

# ---- world layout
RX, RY, RW, RH = 520, 430, 170, 510          # resin tank interior
HX0, HX1, HY0, HY1 = 485, 725, 325, 425      # control valve head
BX, BY, BW, BH = 820, 600, 380, 340          # brine tank interior
BOT = BY + BH                                # 940
WELL = (842, 872)
FLOOR = 965
IN_Y, OUT_Y = 350, 400
BRINE_PATH = [(857, BOT - 12), (857, 410), (HX1, 410)]
DRAIN_PATH = [(HX1, 352), (1265, 352), (1265, FLOOR + 40)]
IN_PATH = [(120, IN_Y), (HX0, IN_Y)]
OUT_PATH = [(HX0, OUT_Y + 6), (120, OUT_Y + 6)]
RISER_X = RX + RW / 2

random.seed(7)
BEADS = []
for gy in range(RY + 70, RY + RH - 14, 15):
    for gx in range(RX + 12, RX + RW - 8, 15):
        x = gx + random.uniform(-3, 3)
        y = gy + random.uniform(-3, 3)
        if abs(x - RISER_X) < 14:
            continue
        BEADS.append((x, y, random.random()))
PELLETS = [(random.random(), random.random(), random.uniform(0.6, 1.0)) for _ in range(900)]

SEC = TIM["sections"]


def S(k):
    return SEC[k]["start"]


def E(k):
    return SEC[k]["start"] + SEC[k]["dur"]


# ---------------------------------------------------------------- helpers
def path_point(pts, u):
    segs = [(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    lens = [math.dist(a, b) for a, b in segs]
    d = u * sum(lens)
    for (a, b), L in zip(segs, lens):
        if d <= L:
            f = d / L if L else 0
            return a[0] + (b[0] - a[0]) * f, a[1] + (b[1] - a[1]) * f
        d -= L
    return pts[-1]


def particles(c, pts, t, alpha, rgb, n=10, speed=0.45, r=6, hard=False):
    if alpha <= 0.01:
        return
    for i in range(n):
        u = (t * speed + i / n) % 1
        x, y = path_point(pts, u)
        c.set_source_rgba(*rgb, alpha)
        c.arc(x, y, r, 0, 2 * math.pi)
        c.fill()
        if hard:
            c.set_source_rgba(*GREY, alpha)
            c.arc(x + 4, y - 4, 3, 0, 2 * math.pi)
            c.fill()


def pipe(c, pts, w=18):
    c.set_line_join(cairo.LINE_JOIN_ROUND)
    c.move_to(*pts[0])
    for p in pts[1:]:
        c.line_to(*p)
    c.set_source_rgb(*NAVY)
    c.set_line_width(w)
    c.stroke_preserve()
    c.set_source_rgb(*INTERIOR)
    c.set_line_width(w - 8)
    c.stroke()


def pill_label(c, t, t0, t1, s, anchor, pos, side="right", size=30, color=NAVY):
    a = pop(t, t0) * (1 - prog(t, t1, t1 + 0.3))
    if a <= 0.001:
        return
    al = clamp(a)
    w = text_w(c, s, "semi", size) + 44
    hgt = size + 28
    px, py = pos
    bx = px if side == "right" else px - w
    if anchor:
        ex = bx if side == "right" else bx + w
        c.set_source_rgba(*color, al)
        c.set_line_width(3)
        c.move_to(*anchor)
        c.line_to(ex, py + hgt / 2)
        c.stroke()
        c.arc(*anchor, 7, 0, 2 * math.pi)
        c.fill()
    c.save()
    c.translate(bx + w / 2, py + hgt / 2)
    c.scale(a, a)
    rrect(c, -w / 2, -hgt / 2, w, hgt, hgt / 2)
    c.set_source_rgba(1, 1, 1, al)
    c.fill_preserve()
    c.set_source_rgba(*color, al)
    c.set_line_width(3)
    c.stroke()
    text(c, s, -w / 2 + 22, size * 0.36, "semi", size, color, al)
    c.restore()


def card(c, t, t0, t1, x, y, big, small="", bg=NAVY, fg=CREAM, accent=AMBER, icon=None, w=None):
    a = pop(t, t0) * (1 - prog(t, t1, t1 + 0.3))
    if a <= 0.001:
        return
    al = clamp(a)
    wb = text_w(c, big, "black", 50)
    ws = text_w(c, small, "semi", 26) if small else 0
    ix = 84 if icon else 0
    w = w or max(wb, ws) + 60 + ix
    hgt = 126 if small else 96
    c.save()
    c.translate(x, y)
    c.translate(w / 2, hgt / 2)
    c.scale(a, a)
    c.translate(-w / 2, -hgt / 2)
    rrect(c, 0, 0, w, hgt, 24)
    c.set_source_rgba(*bg, al)
    c.fill()
    if icon:
        c.save()
        c.translate(30 + 26, hgt / 2)
        icon(c, al)
        c.restore()
    text(c, big, 30 + ix, 64 if small else 66, "black", 50, accent, al)
    if small:
        text(c, small, 30 + ix, 104, "semi", 26, fg, al)
    c.restore()


def ico_check(c, al, col=GREEN):
    c.set_source_rgba(*col, al)
    c.arc(0, 0, 24, 0, 2 * math.pi)
    c.fill()
    c.set_source_rgba(1, 1, 1, al)
    c.set_line_width(5)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.move_to(-10, 0)
    c.line_to(-3, 8)
    c.line_to(11, -8)
    c.stroke()


def ico_x(c, al):
    c.set_source_rgba(*RED, al)
    c.arc(0, 0, 24, 0, 2 * math.pi)
    c.fill()
    c.set_source_rgba(1, 1, 1, al)
    c.set_line_width(5)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    for s in (1, -1):
        c.move_to(-9, -9 * s)
        c.line_to(9, 9 * s)
        c.stroke()


def ico_warn(c, al):
    c.set_source_rgba(*AMBER, al)
    c.move_to(0, -26)
    c.line_to(26, 20)
    c.line_to(-26, 20)
    c.close_path()
    c.fill()
    c.set_source_rgba(*NAVY, al)
    text(c, "!", -5, 14, "black", 30, NAVY, al)


# ---------------------------------------------------------------- state
def state(t):
    s = {}
    # brine tank content (y coords)
    salt_top = BOT - 0.5 * BH          # 770
    water = BOT - 80                   # 860
    salt_bot = BOT
    sludge = 0.0
    # J1: salt check — dips below water then refilled
    salt_top += (BOT - 30 - salt_top) * prog(t, 89.2, 90.6) * (1 - prog(t, 91.9, 93.3))
    # J2: rock salt sludge, removed during J4 cleaning
    sludge = 26 * prog(t, 103.0, 107.0) * (1 - prog(t, 153.5, 156.5))
    # J3: bridge forms, then broken
    br = prog(t, 116.4, 119.0) * (1 - prog(t, 139.0, 140.2))
    water += 30 * prog(t, 116.4, 119.0) * (1 - prog(t, 139.2, 141.0))
    salt_bot = BOT - (BOT - 830) * br
    salt_top += 34 * prog(t, 139.0, 140.4) * (1 - prog(t, 151.6, 151.7))  # collapse after breaking
    # J4: empty, scrub, refill
    e = prog(t, 151.8, 155.8) * (1 - prog(t, 161.0, 164.2))
    salt_top = salt_top + (BOT - salt_top) * e
    water = water + (BOT - water) * prog(t, 151.8, 155.8)
    water -= (BOT - (BOT - 50)) * prog(t, 161.0, 162.6) * (1 if t < 175 else 1)
    if t > 162.6:
        water = BOT - 50
        if t > 164.2:
            water = BOT - 50 + (30 - 0) * 0  # few inches of water
    # J6: brine tank full of water, then drains after fix
    water = water + (BY + 40 - water) * prog(t, 198.4, 201.5) * (1 - prog(t, 228.6, 232.0))
    s.update(salt_top=salt_top, salt_bot=salt_bot, water=water, sludge=sludge,
             bridge=br, crack=prog(t, 138.9, 139.6))
    s["lid"] = prog(t, 77.2, 78.2) * (1 - prog(t, 165.5, 166.6))
    # broom handle tip y (None = hidden)
    hd = None
    if 131.9 < t < 146.0:
        hd = BY - 300 + (815 - (BY - 300)) * prog(t, 132.0, 134.0)
        if 135.4 < t < 138.9:
            hd = 815 - 18 * abs(math.sin((t - 135.4) * 7))
        if t > 138.9:
            hd = 815 + (BOT - 8 - 815) * prog(t, 143.0, 144.4)
            hd -= (BOT - 8 - (BY - 320)) * prog(t, 145.0, 146.0)
    s["handle"] = hd
    # resin hardness / iron
    hard = prog(t, 36.0, 40.0) + 0.6 * prog(t, 44.0, 46.0)
    hard *= 1 - prog(t, 57.0, 61.0)
    s["hard"] = clamp(hard / 1.6)
    s["iron"] = prog(t, 172.0, 176.5) * (1 - prog(t, 189.0, 193.5))
    # flows
    serv = prog(t, 32.2, 33.0) * (1 - prog(t, 46.8, 47.6))
    serv += prog(t, 63.0, 64.0) * (1 - prog(t, 75.0, 75.5))
    s["service"] = clamp(serv)
    regen = prog(t, 51.0, 52.0) * (1 - prog(t, 62.5, 63.5))
    regen += prog(t, 188.0, 188.8) * (1 - prog(t, 193.6, 194.4))
    regen += prog(t, 228.2, 228.8) * (1 - prog(t, 231.8, 232.6))
    s["regen"] = clamp(regen)
    s["cleaner"] = prog(t, 188.0, 188.8) * (1 - prog(t, 193.6, 194.4))
    s["drain"] = prog(t, 56.3, 57.0) * (1 - prog(t, 62.5, 63.5)) + s["cleaner"] + \
        prog(t, 228.2, 228.8) * (1 - prog(t, 231.8, 232.6))
    # camera: brine-tank close-up for jobs 1-4
    s["zoom"] = prog(t, 76.0, 77.6) * (1 - prog(t, 166.0, 168.0))
    # end panels (test / pro / recap) cover the system
    s["panel"] = prog(t, 232.9, 233.8)
    # hook: system enters
    s["sys"] = prog(t, 6.5, 7.6)
    return s


# ---------------------------------------------------------------- drawing: resin tank + valve head
def draw_resin(c, t, st):
    # shell
    rrect(c, RX - 18, RY - 18, RW + 36, RH + 36, 70)
    c.set_source_rgb(*NAVY2)
    c.fill()
    rrect(c, RX, RY, RW, RH, 56)
    c.set_source_rgb(*INTERIOR)
    c.fill()
    c.save()
    rrect(c, RX, RY, RW, RH, 56)
    c.clip()
    # water
    col = WATER
    c.set_source_rgba(*col, 0.55)
    c.rectangle(RX, RY + 40, RW, RH)
    c.fill()
    if st["regen"] > 0:
        c.set_source_rgba(*TEAL, 0.45 * st["regen"])
        c.rectangle(RX, RY + 40, RW, RH)
        c.fill()
    # beads
    for x, y, r in BEADS:
        iron = st["iron"]
        bc = tuple(BEAD[i] * (1 - iron * 0.75) + RUST[i] * iron * 0.75 for i in range(3))
        c.set_source_rgb(*bc)
        c.arc(x, y, 6.2, 0, 2 * math.pi)
        c.fill()
        if r < st["hard"]:
            c.set_source_rgb(*GREY)
            c.arc(x + 2.5, y - 2.5, 2.6, 0, 2 * math.pi)
            c.fill()
    # riser
    c.set_source_rgb(*PORC)
    c.rectangle(RISER_X - 7, RY + 10, 14, RH - 30)
    c.fill()
    c.set_source_rgb(*NAVY)
    c.set_line_width(2.5)
    c.rectangle(RISER_X - 7, RY + 10, 14, RH - 30)
    c.stroke()
    # moving water in the tank
    if st["service"] > 0 or st["regen"] > 0:
        for mode, a, rgb in (("s", st["service"], WATER_D), ("r", st["regen"], TEAL)):
            if a <= 0.01:
                continue
            for i in range(22):
                ph = (t * 0.35 + i / 22) % 1
                x = RX + 18 + ((i * 37) % (RW - 36))
                if abs(x - RISER_X) < 14:
                    x += 20
                y = RY + 50 + ph * (RH - 90)
                c.set_source_rgba(*rgb, 0.9 * a)
                c.arc(x, y, 4.5, 0, 2 * math.pi)
                c.fill()
                if mode == "s" and ph < 0.35:
                    c.set_source_rgba(*GREY, a)
                    c.arc(x + 4, y - 4, 2.6, 0, 2 * math.pi)
                    c.fill()
                if mode == "r" and ph > 0.5:
                    c.set_source_rgba(*GREY, a)
                    c.arc(x + 4, y - 4, 2.6, 0, 2 * math.pi)
                    c.fill()
            # up the riser
            for i in range(8):
                ph = (t * 0.6 + i / 8) % 1
                y = RY + RH - 25 - ph * (RH - 40)
                c.set_source_rgba(*rgb, 0.95 * a)
                c.arc(RISER_X, y, 4, 0, 2 * math.pi)
                c.fill()
    c.restore()
    # head
    rrect(c, HX0, HY0, HX1 - HX0, HY1 - HY0, 18)
    c.set_source_rgb(*NAVY)
    c.fill()
    rrect(c, HX0 + 70, HY0 + 22, 100, 46, 8)
    c.set_source_rgb(*AMBER)
    c.fill()
    disp = "REGEN" if st["regen"] > 0.5 else ("BYPASS" if st.get("bypass", 0) > 0.5 else "12:00")
    text(c, disp, HX0 + 120, HY0 + 54, "xbold", 22 if len(disp) > 5 else 24, NAVY, align="center")
    # neck
    c.set_source_rgb(*NAVY2)
    c.rectangle(RX + 40, HY1, RW - 80, RY - 18 - HY1)
    c.fill()


def draw_brine(c, t, st):
    lid = st["lid"]
    # shell
    rrect(c, BX - 16, BY - 6, BW + 32, BH + 22, 22)
    c.set_source_rgb(*PORC)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(5)
    c.stroke()
    c.set_source_rgb(*INTERIOR)
    c.rectangle(BX, BY, BW, BH)
    c.fill()
    c.save()
    c.rectangle(BX, BY, BW, BH)
    c.clip()
    sx0 = WELL[1] + 4
    st_top, st_bot, water = st["salt_top"], st["salt_bot"], st["water"]
    # sludge
    if st["sludge"] > 0.5:
        c.set_source_rgb(*SLUDGE)
        c.rectangle(sx0, BOT - st["sludge"], BX + BW - sx0, st["sludge"])
        c.fill()
    # salt pellets
    if st_bot - st_top > 1:
        for px, py, sc in PELLETS:
            x = sx0 + 6 + px * (BX + BW - sx0 - 12)
            y = st_top + 6 + py * (st_bot - st_top - 8)
            if y > BOT - st["sludge"] - 4:
                continue
            c.save()
            c.translate(x, y)
            c.scale(sc, sc * 0.75)
            c.arc(0, 0, 9, 0, 2 * math.pi)
            c.restore()
            c.set_source_rgb(*SALT)
            c.fill_preserve()
            c.set_source_rgba(*NAVY, 0.35)
            c.set_line_width(1.5)
            c.stroke()
        if st["bridge"] > 0.2 and st["crack"] < 1:
            a = clamp((st["bridge"] - 0.2) / 0.5) * (1 - st["crack"])
            c.set_source_rgba(*SLUDGE, 0.55 * a)
            c.rectangle(sx0, st_bot - 18, BX + BW - sx0, 18)
            c.fill()
            c.set_source_rgba(*NAVY, 0.6 * a)
            c.set_line_width(3)
            c.move_to(sx0, st_bot)
            for i in range(0, int(BX + BW - sx0) + 1, 20):
                c.line_to(sx0 + i, st_bot + 4 * math.sin(i / 9))
            c.stroke()
    # falling crust chunks
    if 0 < st["crack"] < 1 or (139.0 < t < 141.0):
        f = clamp((t - 139.0) / 1.6)
        for i in range(9):
            x = sx0 + 30 + i * 36
            y = 815 + f * (BOT - 40 - 815) * (0.6 + 0.4 * ((i * 7) % 5) / 5)
            c.set_source_rgba(*SALT, 1 - f * 0.5)
            rrect(c, x, y, 26, 16, 5)
            c.fill_preserve()
            c.set_source_rgba(*NAVY, 0.5 * (1 - f))
            c.stroke()
    # water
    if water < BOT - 1:
        c.set_source_rgba(*WATER, 0.62)
        c.rectangle(BX, water, BW, BOT - water)
        c.fill()
        c.set_source_rgba(1, 1, 1, 0.7)
        c.set_line_width(3)
        c.move_to(BX, water)
        c.line_to(BX + BW, water)
        c.stroke()
    # brine well
    c.set_source_rgb(*PORC)
    c.rectangle(WELL[0], BY - 4, WELL[1] - WELL[0], BH - 4)
    c.fill()
    c.set_source_rgb(*NAVY)
    c.set_line_width(3)
    c.rectangle(WELL[0], BY - 4, WELL[1] - WELL[0], BH - 4)
    c.stroke()
    c.restore()
    # lid (hinged on the right, lifts up)
    c.save()
    c.translate(BX + BW + 20, BY - 6)
    c.rotate(math.radians(32) * ease(lid))
    rrect(c, -(BW + 40), -26, BW + 40, 26, 10)
    c.set_source_rgb(*PORC)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(5)
    c.stroke()
    c.restore()


def draw_handle(c, t, st):
    hd = st["handle"]
    if hd is None:
        return
    x = BX + 250
    c.set_source_rgb(*WOOD)
    rrect(c, x - 10, hd - 700, 20, 700, 8)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(3)
    c.stroke()


def draw_system(c, t, st):
    pipe(c, IN_PATH)
    pipe(c, OUT_PATH)
    pipe(c, BRINE_PATH, 14)
    pipe(c, DRAIN_PATH, 14)
    # floor + drain grate
    c.set_source_rgba(*NAVY, 0.25)
    c.set_line_width(4)
    c.move_to(80, FLOOR)
    c.line_to(1840, FLOOR)
    c.stroke()
    rrect(c, 1235, FLOOR - 6, 60, 14, 6)
    c.set_source_rgb(*NAVY)
    c.fill()
    bypass = st.get("bypass", 0)
    particles(c, IN_PATH, t, st["service"] * (1 - bypass), WATER_D, n=8, speed=0.5, hard=True)
    particles(c, OUT_PATH, t, st["service"] * (1 - bypass), WATER_D, n=8, speed=0.5)
    particles(c, BRINE_PATH, t, st["regen"], TEAL, n=12, speed=0.35)
    particles(c, DRAIN_PATH, t, clamp(st["drain"]), GREY, n=14, speed=0.3)
    # bypass valve on the inlet
    c.save()
    c.translate(300, IN_Y)
    c.set_source_rgb(*NAVY)
    c.arc(0, 0, 18, 0, 2 * math.pi)
    c.fill()
    c.rotate(math.pi / 2 * bypass)
    rrect(c, -6, -52, 12, 44, 5)
    c.set_source_rgb(*(RED if bypass > 0.5 else NAVY2))
    c.fill()
    c.restore()
    draw_resin(c, t, st)
    draw_brine(c, t, st)
    draw_handle(c, t, st)
    if 157.3 < t < 160.8:
        a = prog(t, 157.3, 157.7) * (1 - prog(t, 160.4, 160.8))
        bx = BX + 200 + 110 * math.sin((t - 157.3) * 6)
        c.save()
        c.translate(bx, BOT - 60)
        c.rotate(0.3 * math.sin((t - 157.3) * 6))
        rrect(c, -60, -10, 120, 34, 10)
        c.set_source_rgba(*AMBER, a)
        c.fill()
        c.set_source_rgba(*NAVY, a)
        c.set_line_width(3)
        for k in range(8):
            c.move_to(-50 + k * 14, 24)
            c.line_to(-50 + k * 14, 44)
        c.stroke()
        rrect(c, -14, -120, 28, 112, 10)
        c.set_source_rgba(*NAVY2, a)
        c.fill()
        c.restore()
        random.seed(2)
        for k in range(18):
            ph = (t * 0.6 + random.random()) % 1
            x = WELL[1] + 20 + random.random() * (BX + BW - WELL[1] - 40)
            y = BOT - 20 - ph * 160
            c.set_source_rgba(1, 1, 1, a * (1 - ph))
            c.set_line_width(2.5)
            c.new_path()
            c.arc(x, y, 6 + 6 * random.random(), 0, 2 * math.pi)
            c.stroke()


# ---------------------------------------------------------------- insets
def inset_beads(c, t, a, hard, iron, regen, cx=1540, cy=640, r=230):
    if a <= 0.01:
        return
    c.save()
    c.translate(cx, cy)
    c.scale(back(a), back(a))
    c.arc(0, 0, r, 0, 2 * math.pi)
    c.set_source_rgb(*INTERIOR)
    c.fill_preserve()
    c.save()
    c.clip()
    c.set_source_rgba(*WATER, 0.5)
    c.paint()
    if regen > 0:
        c.set_source_rgba(*TEAL, 0.45 * regen)
        c.paint()
    random.seed(3)
    for i in range(30):
        x = random.uniform(-r, r)
        y = random.uniform(-r, r)
        bc = tuple(BEAD[k] * (1 - iron * 0.75) + RUST[k] * iron * 0.75 for k in range(3))
        c.set_source_rgb(*bc)
        c.arc(x, y, 34, 0, 2 * math.pi)
        c.fill_preserve()
        c.set_source_rgba(*NAVY, 0.4)
        c.set_line_width(2)
        c.stroke()
        c.set_source_rgba(1, 1, 1, 0.6)
        c.arc(x - 11, y - 11, 8, 0, 2 * math.pi)
        c.fill()
        # hardness ions stuck to bead
        nh = int(round(hard * 4))
        for j in range(nh):
            ang = j * 1.6 + i
            hx, hy = x + 30 * math.cos(ang), y + 30 * math.sin(ang)
            c.set_source_rgb(*GREY)
            c.arc(hx, hy, 9, 0, 2 * math.pi)
            c.fill()
    # free ions drifting during service / leaving during regen
    c.restore()
    c.set_source_rgb(*NAVY)
    c.set_line_width(8)
    c.arc(0, 0, r, 0, 2 * math.pi)
    c.stroke()
    c.restore()


def inset_injector(c, t, a):
    """Big diagram of the injector (venturi) with screen, nozzle, cap and O-rings."""
    if a <= 0.01:
        return
    x0, y0, w, h = 1180, 300, 660, 600
    c.save()
    c.translate(x0 + w / 2, y0 + h / 2)
    c.scale(back(a), back(a))
    c.translate(-w / 2, -h / 2)
    rrect(c, 0, 0, w, h, 30)
    c.set_source_rgb(*PORC)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(5)
    c.stroke()
    text(c, "INJECTOR (VENTURI)", 40, 60, "xbold", 30, NAVY)
    # body: horizontal throat with a narrow middle
    cx, cy = 330, 330
    c.set_source_rgb(*NAVY2)
    c.move_to(80, cy - 50)
    c.line_to(250, cy - 50)
    c.line_to(310, cy - 18)
    c.line_to(350, cy - 18)
    c.line_to(420, cy - 50)
    c.line_to(580, cy - 50)
    c.line_to(580, cy + 50)
    c.line_to(420, cy + 50)
    c.line_to(350, cy + 18)
    c.line_to(310, cy + 18)
    c.line_to(250, cy + 50)
    c.line_to(80, cy + 50)
    c.close_path()
    c.fill()
    # inner channel
    c.set_source_rgb(*INTERIOR)
    c.move_to(80, cy - 34)
    c.line_to(250, cy - 34)
    c.line_to(310, cy - 7)
    c.line_to(350, cy - 7)
    c.line_to(420, cy - 34)
    c.line_to(580, cy - 34)
    c.line_to(580, cy + 34)
    c.line_to(420, cy + 34)
    c.line_to(350, cy + 7)
    c.line_to(310, cy + 7)
    c.line_to(250, cy + 34)
    c.line_to(80, cy + 34)
    c.close_path()
    c.fill()
    # brine port coming up from below the throat
    c.set_source_rgb(*NAVY2)
    c.rectangle(312, cy + 18, 36, 150)
    c.fill()
    c.set_source_rgb(*INTERIOR)
    c.rectangle(322, cy + 10, 16, 160)
    c.fill()
    text(c, "brine from tank", 360, cy + 160, "semi", 24, BODY)
    # screen (removable) at the inlet
    clog = prog(t, 212.9, 213.8) * (1 - prog(t, 220.6, 222.8))
    lift = prog(t, 219.4, 220.4) * (1 - prog(t, 225.6, 226.6))
    sy = -150 * lift
    c.save()
    c.translate(0, sy)
    c.set_source_rgb(*BODY)
    c.set_line_width(2)
    for k in range(9):
        c.move_to(150 + k * 9, cy - 34)
        c.line_to(150 + k * 9, cy + 34)
    c.stroke()
    c.rectangle(146, cy - 36, 80, 72)
    c.set_line_width(4)
    c.stroke()
    random.seed(11)
    for k in range(16):
        c.set_source_rgba(*SLUDGE, clog)
        c.arc(152 + random.uniform(0, 70), cy - 30 + random.uniform(0, 60), random.uniform(3, 6), 0, 2 * math.pi)
        c.fill()
    c.restore()
    # cap
    c.save()
    c.translate(0, -170 * lift)
    rrect(c, 120, cy - 96, 140, 40, 10)
    c.set_source_rgb(*NAVY)
    c.fill()
    c.restore()
    # O-rings
    glow = prog(t, 224.2, 224.8) * (1 - prog(t, 227.6, 228.2))
    for ox in (100, 560):
        c.set_source_rgb(*(AMBER if glow > 0.1 else NAVY))
        rrect(c, ox - 8, cy - 58, 16, 116, 8)
        c.fill()
        if glow > 0.1:
            c.set_source_rgba(*AMBER, 0.35 * glow)
            c.arc(ox, cy, 70, 0, 2 * math.pi)
            c.fill()
    # rinse droplets
    if 220.4 < t < 223.6:
        for k in range(14):
            ph = (t * 1.6 + k / 14) % 1
            c.set_source_rgba(*WATER_D, 0.9)
            c.arc(150 + (k * 13) % 80, cy - 260 + ph * 120, 5, 0, 2 * math.pi)
            c.fill()
    # suction flow arrows (works when clean)
    flow = prog(t, 209.3, 210.0) * (1 - clog) * (1 - lift)
    if t > 228.0:
        flow = 1 - prog(t, 231.6, 232.4)
    if flow > 0.01:
        for k in range(8):
            ph = (t * 0.8 + k / 8) % 1
            c.set_source_rgba(*WATER_D, flow)
            c.arc(90 + ph * 480, cy, 7, 0, 2 * math.pi)
            c.fill()
            c.set_source_rgba(*TEAL, flow)
            c.arc(330, cy + 160 - ph * 160, 6, 0, 2 * math.pi)
            c.fill()
    if clog > 0.3:
        pill_label(c, t, 213.0, 221.0, "Clogged screen", None, (60, 470), size=30, color=RED)
    c.restore()


# ---------------------------------------------------------------- hook icons
def glass_icon(c, al):
    c.set_source_rgba(*NAVY, al)
    c.set_line_width(6)
    c.move_to(-60, -90)
    c.line_to(60, -90)
    c.line_to(44, 90)
    c.line_to(-44, 90)
    c.close_path()
    c.stroke()
    random.seed(5)
    for _ in range(26):
        c.set_source_rgba(*GREY, 0.8 * al)
        c.arc(random.uniform(-45, 45), random.uniform(-75, 80), random.uniform(3, 7), 0, 2 * math.pi)
        c.fill()


def faucet_icon(c, al):
    c.set_source_rgba(*NAVY, al)
    rrect(c, -80, -20, 120, 36, 14)
    c.fill()
    rrect(c, 20, -20, 36, 90, 14)
    c.fill()
    rrect(c, -100, -60, 50, 90, 12)
    c.fill()
    random.seed(9)
    for _ in range(16):
        c.set_source_rgba(1, 1, 1, 0.85 * al)
        c.arc(random.uniform(-70, 50), random.uniform(-14, 70) if random.random() < 0.5 else 10,
              random.uniform(4, 8), 0, 2 * math.pi)
        c.fill()


def soap_icon(c, al):
    rrect(c, -80, -40, 160, 80, 26)
    c.set_source_rgba(*AMBER, al)
    c.fill()
    c.set_source_rgba(*RED, al)
    c.set_line_width(10)
    c.move_to(-100, 80)
    c.line_to(100, -80)
    c.stroke()


def bottle_icon(c, al):
    rrect(c, -20, -32, 40, 60, 8)
    c.set_source_rgba(*AMBER, al)
    c.fill()
    c.set_source_rgba(*NAVY, al)
    c.rectangle(-8, -42, 16, 12)
    c.fill()


# ---------------------------------------------------------------- headlines
HEADS = [
    (0.0, "WATER SOFTENER MAINTENANCE", "Is your water hard again?"),
    (S(1), "HOW IT WORKS", "Two tanks, one job"),
    (S(2), "JOB 1 OF 6", "Check the salt level monthly"),
    (S(3), "JOB 2 OF 6", "Use the right salt"),
    (S(4), "JOB 3 OF 6", "Break up salt bridges"),
    (S(5), "JOB 4 OF 6", "Clean the brine tank yearly"),
    (S(6), "JOB 5 OF 6", "Clean the resin"),
    (S(7), "JOB 6 OF 6", "Clear the injector"),
    (S(8), "FINAL CHECK", "Test your water"),
    (S(9), "KNOW YOUR LIMIT", "When to call a pro"),
    (S(10), "RECAP", "Six jobs, a few minutes each"),
]


def headline(c, t):
    idx = max(i for i, h in enumerate(HEADS) if h[0] - 0.3 <= t)
    t0, kick, head = HEADS[idx]
    a = clamp((t - t0 + 0.3) / 0.4)
    off = 24 * (1 - ease(a))
    w = max(text_w(c, head, "xbold", 64), text_w(c, kick, "semi", 26)) + 80
    rrect(c, 60, 52, w, 164, 28)
    c.set_source_rgba(*CREAM, 0.96)
    c.fill()
    text(c, kick, 100, 106 + off, "semi", 26, AMBER, a)
    text(c, head, 100, 176 + off, "xbold", 64, NAVY, a)


def brand(c):
    text(c, "HOME IMPROVEMENT HUB", W - 70, 70, "xbold", 24, NAVY, 0.55, align="right")


# ---------------------------------------------------------------- section overlays (screen space)
def overlays_world(c, t, st):
    """Callouts placed in world coordinates (move with the camera)."""
    # how it works
    pill_label(c, t, 26.0, 46.6, "Resin tank", (RX, RY + 160), (470, 640), side="left")
    pill_label(c, t, 32.3, 46.6, "Hard water in", None, (110, IN_Y - 92))
    pill_label(c, t, 40.6, 46.6, "Soft water out", None, (110, OUT_Y + 30))
    pill_label(c, t, 51.0, 66.0, "Brine tank", (BX + BW, BY + 60), (1320, 560))
    pill_label(c, t, 56.4, 66.0, "Drain", (1265, 700), (1320, 680))
    # J1
    if 80.2 < t < 93.5:
        a = prog(t, 80.2, 80.8)
        for frac, lab in ((1 / 3, "1/3"), (0.5, "1/2")):
            y = BOT - frac * BH
            c.set_source_rgba(*AMBER, a)
            c.set_line_width(4)
            c.move_to(BX + BW - 4, y)
            c.line_to(BX + BW + 40, y)
            c.stroke()
            text(c, lab, BX + BW + 48, y + 10, "xbold", 28, AMBER, a)
    if 86.4 < t < 93.5:
        a = prog(t, 86.4, 87.0)
        c.set_source_rgba(*NAVY, 0.7 * a)
        c.set_line_width(3)
        c.set_dash([12, 8])
        y = BOT - 0.5 * BH - 8
        c.move_to(WELL[1] + 6, y)
        c.line_to(BX + BW - 6, y)
        c.stroke()
        c.set_dash([])
    # J3 gap
    if 122.6 < t < 131.0:
        a = pop(t, 122.6)
        c.set_source_rgba(*RED, clamp(a))
        c.set_line_width(4)
        c.set_dash([12, 8], t * 20)
        c.rectangle(WELL[1] + 10, 834, BX + BW - WELL[1] - 20, st["water"] - 838)
        c.stroke()
        c.set_dash([])
    # J6: brine line blocked
    if 202.4 < t < 228.0:
        a = pop(t, 202.4)
        c.save()
        c.translate(857, 470)
        c.scale(a, a)
        ico_x(c, 1)
        c.restore()


def overlays_screen(c, t, st):
    # ---- hook
    if t < 8.0:
        items = [(1.0, 420, glass_icon, "Spotty glasses"), (2.7, 960, faucet_icon, "Crusty faucets"),
                 (4.3, 1500, soap_icon, "Soap won't lather")]
        out = prog(t, 6.4, 7.2)
        for t0, x, ic, lab in items:
            a = pop(t, t0) * (1 - out)
            if a <= 0.01:
                continue
            c.save()
            c.translate(x, 600 - 60 * out)
            c.scale(a, a)
            c.arc(0, 0, 170, 0, 2 * math.pi)
            c.set_source_rgb(*PAPER)
            c.fill()
            ic(c, 1)
            c.restore()
            text(c, lab, x, 830, "xbold", 40, NAVY, clamp(a), align="center")
    card(c, t, 13.6, 22.4, 1340, 420, "Minutes", "most jobs take a few", icon=lambda c, al: ico_check(c, al))
    card(c, t, 15.4, 22.4, 1340, 570, "Almost free", "salt, a brush, test strips", icon=lambda c, al: ico_check(c, al))
    card(c, t, 17.4, 22.4, 1340, 720, "6 jobs", "keep it working", bg=AMBER, fg=NAVY, accent=NAVY)
    # ---- how it works
    inset_beads(c, t, prog(t, 28.4, 29.0) * (1 - prog(t, 46.6, 47.2)), st["hard"], 0, 0)
    if 28.4 < t < 47.0:
        a = prog(t, 28.6, 29.2) * (1 - prog(t, 46.4, 46.8))
        text(c, "Resin beads (enlarged)", 1540, 920, "xbold", 30, NAVY, a, align="center")
        if t > 36.1:
            text(c, "grab calcium + magnesium", 1540, 960, "semi", 26, BODY, a * prog(t, 36.1, 36.6), align="center")
    card(c, t, 44.3, 46.6, 1330, 240, "Full!", "beads can only hold so much", bg=RED, accent=CREAM)
    card(c, t, 47.3, 62.8, 1330, 250, "Regenerates", "every few days", icon=lambda c, al: ico_check(c, al, AMBER))
    for i, (t0, lab) in enumerate([(66.5, "Enough salt"), (67.8, "Brine that flows"), (69.9, "Clean resin")]):
        card(c, t, t0, 75.2, 1330, 300 + i * 150, lab, "", bg=NAVY if i % 2 == 0 else NAVY2,
             icon=lambda c, al: ico_check(c, al), w=470)
    # ---- J1
    card(c, t, 80.2, 89.0, 1360, 300, "1/3 to 1/2", "full of salt")
    card(c, t, 83.6, 89.0, 1360, 450, "Salt above", "the water level", icon=lambda c, al: ico_check(c, al))
    card(c, t, 89.1, 92.0, 1360, 360, "Water on top?", "add salt", bg=RED, accent=CREAM, icon=lambda c, al: ico_x(c, al))
    if 91.8 < t < 93.6:  # pellets pouring in
        for k in range(24):
            ph = (t * 1.4 + k / 24) % 1
            x = 960 + (k * 23) % 260
            y = 250 + ph * 420
            c.set_source_rgb(*SALT)
            c.arc(x, y, 9, 0, 2 * math.pi)
            c.fill_preserve()
            c.set_source_rgba(*NAVY, 0.4)
            c.set_line_width(1.5)
            c.stroke()
    # ---- J2
    bags = [("Pellets", True), ("Crystals", True), ("Rock salt", False)]
    for i, (lab, ok) in enumerate(bags):
        t0 = 95.8 + i * 0.25
        tick = 98.6 if ok else 100.9
        a = pop(t, t0) * (1 - prog(t, 107.6, 108.0))
        if a <= 0.01:
            continue
        x, y = 1330 + (i % 3) * 0, 280 + i * 150
        c.save()
        c.translate(x, y)
        rrect(c, 0, 0, 470 * a, 120, 24)
        c.set_source_rgb(*(PAPER if ok else (252/255, 232/255, 226/255)))
        c.fill()
        text(c, lab, 110, 76, "xbold", 44, NAVY, clamp(a))
        b = pop(t, tick)
        if b > 0:
            c.save()
            c.translate(55, 60)
            c.scale(b, b)
            (ico_check if ok else ico_x)(c, 1)
            c.restore()
        c.restore()
    card(c, t, 103.2, 107.6, 1330, 730, "Sludge", "from insoluble material", bg=SLUDGE, accent=CREAM)
    card(c, t, 108.2, 115.2, 1330, 330, "One type", "don't mix salts", icon=lambda c, al: ico_check(c, al))
    card(c, t, 110.4, 115.2, 1330, 480, "Mixing", "can cause bridging", bg=RED, accent=CREAM, icon=lambda c, al: ico_x(c, al))
    # ---- J3
    card(c, t, 116.4, 131.4, 1330, 280, "Salt bridge", "a hard crust above the water", bg=SLUDGE, accent=CREAM)
    card(c, t, 120.3, 122.4, 1330, 440, "Looks full…", "from the top")
    card(c, t, 122.7, 131.4, 1330, 440, "Empty gap", "below the crust", bg=RED, accent=CREAM)
    card(c, t, 125.2, 131.4, 1330, 600, "No brine", "= hard water again", bg=NAVY2)
    card(c, t, 131.9, 146.0, 1330, 300, "Broom handle", "push down in a few spots", bg=NAVY, icon=None)
    card(c, t, 140.3, 146.0, 1330, 460, "Gently", "don't hit the tank walls", bg=RED, accent=CREAM, icon=lambda c, al: ico_warn(c, al))
    if 143.0 < t < 146.0:
        a = pop(t, 144.4)
        if a > 0:
            card(c, t, 144.4, 146.0, 1330, 620, "To the bottom", "no crust left", icon=lambda c, al: ico_check(c, al))
    # ---- J4 checklist
    if S(5) - 0.2 < t < E(5) + 0.8:
        a = prog(t, S(5), S(5) + 0.4) * (1 - prog(t, E(5) + 0.3, E(5) + 0.8))
        steps = [(149.0, "Bypass mode"), (151.6, "Empty salt + water"), (157.3, "Scrub + rinse"),
                 (160.9, "Fresh water + salt"), (164.7, "Out of bypass")]
        rrect(c, 1320, 280, 520, 80 + 92 * len(steps), 28)
        c.set_source_rgba(*PAPER, a)
        c.fill()
        text(c, "ONCE A YEAR", 1360, 336, "xbold", 26, AMBER, a)
        for i, (t0, lab) in enumerate(steps):
            on = t >= t0
            y = 360 + i * 92
            c.save()
            c.translate(1385, y + 40)
            if on:
                b = pop(t, t0)
                c.scale(b, b)
                ico_check(c, a)
            else:
                c.set_source_rgba(*NAVY, 0.3 * a)
                c.set_line_width(3)
                c.new_path()
                c.arc(0, 0, 22, 0, 2 * math.pi)
                c.stroke()
            c.restore()
            text(c, lab, 1430, y + 52, "semi", 34, NAVY, a * (1 if on else 0.45))
    # bypass status chip (J4 and J6)
    # ---- J5
    inset_beads(c, t, prog(t, 168.3, 169.0) * (1 - prog(t, 195.0, 195.6)), 0.0, st["iron"], st["regen"])
    if 168.3 < t < 195.6:
        a = prog(t, 168.5, 169.1) * (1 - prog(t, 194.9, 195.3))
        text(c, "Iron coats the beads" if st["iron"] > 0.3 else "Resin beads (enlarged)", 1540, 920, "xbold", 30, NAVY, a, align="center")
    card(c, t, 176.9, 185.2, 1330, 250, "Resin cleaner", "strips iron off the beads", icon=bottle_icon)
    card(c, t, 179.5, 194.0, 1180, 120, "Every 3–12 months", "more often with iron or rust stains", bg=AMBER, fg=NAVY, accent=NAVY)
    card(c, t, 194.3, 196.4, 1180, 120, "Test next day", "", bg=NAVY2, icon=lambda c, al: ico_check(c, al))
    # bottle pouring into the brine well
    if 185.4 < t < 189.0:
        a = prog(t, 185.4, 185.9) * (1 - prog(t, 188.5, 189.0))
        c.save()
        c.translate(900, 470)
        c.rotate(-1.9 * prog(t, 185.9, 186.6))
        c.scale(2.2, 2.2)
        bottle_icon(c, a)
        c.restore()
        if t > 186.6:
            c.set_source_rgba(*AMBER, a)
            c.set_line_width(7)
            c.move_to(862, 490)
            c.line_to(858, 600)
            c.stroke()
    # ---- J6
    pill_label(c, t, 198.4, 228.4, "Brine tank stays full", (BX + 60, BY + 60), (900, 985), color=RED)
    inset_injector(c, t, prog(t, 205.0, 205.8) * (1 - prog(t, 232.0, 232.8)))
    card(c, t, 214.8, 219.2, 1060, 120, "Bypass + release pressure", "as your manual shows", bg=NAVY2)
    card(c, t, 219.5, 224.0, 1100, 120, "Rinse screen + nozzle", "in warm water", bg=NAVY2)
    card(c, t, 224.2, 228.0, 1180, 120, "Silicone grease", "on the O-rings, then reassemble", bg=AMBER, fg=NAVY, accent=NAVY)
    card(c, t, 228.2, 233.0, 1180, 120, "Level drops", "after the next regeneration", icon=lambda c, al: ico_check(c, al))


def panel_scenes(c, t, st):
    a = st["panel"]
    if a <= 0:
        return
    c.set_source_rgba(*CREAM, a)
    c.paint()
    # ---- test
    if t < E(8) + 0.8:
        b = 1 - prog(t, E(8) + 0.3, E(8) + 0.8)
        # faucet
        c.save()
        c.translate(620, 420)
        c.set_source_rgba(*NAVY, b)
        rrect(c, -160, -30, 260, 60, 24)
        c.fill()
        rrect(c, 60, -30, 60, 140, 20)
        c.fill()
        rrect(c, -200, -110, 80, 150, 16)
        c.fill()
        text(c, "COLD", -160, -130, "xbold", 26, WATER_D, b)
        # stream
        c.set_source_rgba(*WATER, 0.9 * b)
        rrect(c, 72, 110, 36, 360, 14)
        c.fill()
        c.restore()
        # strip
        dip = prog(t, 238.3, 239.3)
        c.save()
        c.translate(900 - 180 * dip, 820 - 120 * dip)
        c.rotate(-0.25)
        rrect(c, -20, -200, 40, 300, 8)
        c.set_source_rgba(1, 1, 1, b)
        c.fill_preserve()
        c.set_source_rgba(*NAVY, b)
        c.set_line_width(3)
        c.stroke()
        col = prog(t, 240.0, 241.5)
        for k in range(3):
            pc = tuple(RED[i] * (1 - col) + GREEN[i] * col for i in range(3))
            c.set_source_rgba(*pc, b)
            rrect(c, -14, -170 + k * 50, 28, 32, 6)
            c.fill()
        c.restore()
        card(c, t, 236.0, E(8) + 0.6, 1300, 330, "1 day after", "the softener regenerates", bg=NAVY)
        card(c, t, 241.6, E(8) + 0.6, 1300, 490, "Soft water", "test strip says so", icon=lambda c, al: ico_check(c, al))
        card(c, t, 242.6, E(8) + 0.6, 1300, 650, "No new spots", "on glasses or fixtures", icon=lambda c, al: ico_check(c, al))
    # ---- pro
    if S(9) - 0.3 < t < E(9) + 0.8:
        b = prog(t, S(9) - 0.3, S(9) + 0.2) * (1 - prog(t, E(9) + 0.3, E(9) + 0.8))
        rows = [(248.6, "Water stays hard", "with plenty of salt and no bridge"),
                (254.8, "Brine tank stays full", "of water"),
                (257.3, "Control valve leaks", ""),
                (259.4, "Softener runs constantly", "")]
        for i, (t0, big, small) in enumerate(rows):
            card(c, t, t0, E(9) + 0.5, 100, 300 + i * 160, big, small, bg=NAVY if i % 2 == 0 else NAVY2,
                 icon=lambda c, al: ico_warn(c, al), w=1100)
        card(c, t, 249.6, E(9) + 0.5, 1300, 300, "Call a pro", "water treatment technician", bg=AMBER, fg=NAVY, accent=NAVY)
    # ---- recap
    if t > S(10) - 0.3:
        rows = [(264.0, "Check the salt"), (265.1, "Use the right salt"), (266.7, "Break bridges"),
                (268.0, "Clean the tank"), (269.1, "Clean the resin"), (270.4, "Keep the injector clear")]
        for i, (t0, lab) in enumerate(rows):
            x = 100 + (i // 3) * 720
            y = 300 + (i % 3) * 140
            card(c, t, t0, 999, x, y, lab, "", bg=NAVY if (i % 2 == 0) else NAVY2,
                 icon=lambda c, al: ico_check(c, al), w=680)
        f = pop(t, 272.4)
        if f > 0:
            s1, s2 = "Full step-by-step guide + checklist", "homeimprovementhub101.com"
            w = max(text_w(c, s1, "semi", 30), text_w(c, s2, "black", 56)) + 90
            c.save()
            c.translate(100 + w / 2, 840)
            c.scale(f, f)
            rrect(c, -w / 2, -80, w, 160, 34)
            c.set_source_rgb(*AMBER)
            c.fill()
            text(c, s1, -w / 2 + 45, -20, "semi", 30, NAVY)
            text(c, s2, -w / 2 + 45, 46, "black", 56, NAVY)
            c.restore()
        g = pop(t, 278.8)
        if g > 0:
            text(c, "Thanks for watching!", 1800, 1010, "xbold", 40, NAVY, clamp(g), align="right")


# ---------------------------------------------------------------- frame
def frame(c, t):
    st = state(t)
    st["bypass"] = prog(t, 149.2, 149.8) * (1 - prog(t, 164.8, 165.4))
    c.set_source_rgb(*CREAM)
    c.paint()
    if st["panel"] < 1:
        z = st["zoom"]
        s = 1 + 0.6 * z
        fx = W / 2 + (BX + BW / 2 - W / 2) * z
        fy = H / 2 + (BY + BH / 2 - 40 - H / 2) * z
        sx = W / 2 + (800 - W / 2) * z
        sy = H / 2 + (660 - H / 2) * z
        c.save()
        c.translate(sx, sy)
        c.scale(s, s)
        c.translate(-fx, -fy)
        sa = st["sys"]
        if sa > 0:
            c.push_group()
            draw_system(c, t, st)
            overlays_world(c, t, st)
            c.pop_group_to_source()
            c.paint_with_alpha(sa)
        c.restore()
        if st["bypass"] > 0.5 and z > 0.5:
            card(c, t, 149.3, 165.0, 1320, 860, "BYPASS ON", "", bg=RED, accent=CREAM, w=330)
        overlays_screen(c, t, st)
    panel_scenes(c, t, st)
    headline(c, t)
    brand(c)


def render(out="ws_silent.mp4", stills=None, start=0.0, end=None):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(surf)
    if stills:
        for ts in stills:
            frame(c, ts)
            surf.write_to_png(f"st_{ts:06.1f}.png")
        return
    end = end or DUR
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset",
                          "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(int(start * FPS), int(end * FPS)):
        frame(c, i / FPS)
        surf.flush()
        p.stdin.write(surf.get_data())
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    if sys.argv[1:2] == ["stills"]:
        render(stills=[float(x) for x in sys.argv[2:]])
    elif sys.argv[1:2] == ["part"]:
        render(out=sys.argv[2], start=float(sys.argv[3]), end=float(sys.argv[4]))
    else:
        render()
