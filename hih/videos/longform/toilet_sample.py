"""HIH long-form animated explainer — 30s sample: why a toilet keeps running (cutaway tank)."""
import math, subprocess, sys
import cairo

W, H, FPS = 1920, 1080, 30
DUR = 34.8

NAVY = (24/255, 46/255, 71/255)
NAVY2 = (33/255, 61/255, 92/255)
CREAM = (250/255, 246/255, 238/255)
PAPER = (246/255, 240/255, 228/255)
AMBER = (242/255, 179/255, 92/255)
BODY = (74/255, 88/255, 104/255)
RED = (214/255, 88/255, 66/255)
GREEN = (63/255, 150/255, 98/255)
WATER = (126/255, 182/255, 224/255)
WATER_D = (88/255, 150/255, 201/255)
INTERIOR = (226/255, 234/255, 241/255)
PORC = (255/255, 253/255, 249/255)
WORN = (150/255, 112/255, 84/255)

TX, TY, TW, TH = 380, 330, 640, 520          # tank interior
FULL, EMPTY = TY + 150, TY + TH - 40          # water levels
HOLE = (TX + 330, TX + 450)                   # flush valve opening
HINGE = (TX + 462, TY + TH - 14)
PIVOT = (TX + 30, TY + 60)
ARM_LEN = 332
ATTACH = 100                                   # chain attach distance from hinge


def clamp(x, a=0.0, b=1.0):
    return max(a, min(b, x))


def ease(x):
    x = clamp(x)
    return x * x * (3 - 2 * x)


def back(x):
    x = clamp(x)
    c = 1.70158
    return 1 + (c + 1) * (x - 1) ** 3 + c * (x - 1) ** 2


def prog(t, a, b):
    return ease((t - a) / (b - a))


def rrect(c, x, y, w, h, r):
    r = min(r, w / 2, h / 2)
    c.new_sub_path()
    c.arc(x + w - r, y + r, r, -math.pi / 2, 0)
    c.arc(x + w - r, y + h - r, r, 0, math.pi / 2)
    c.arc(x + r, y + h - r, r, math.pi / 2, math.pi)
    c.arc(x + r, y + r, r, math.pi, 1.5 * math.pi)
    c.close_path()


def font(c, weight, size):
    c.select_font_face({"black": "Poppins Black", "xbold": "Poppins ExtraBold",
                        "semi": "Poppins SemiBold", "med": "Poppins Medium"}[weight],
                       cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_NORMAL)
    c.set_font_size(size)


def text(c, s, x, y, weight, size, rgb, alpha=1.0, align="left"):
    font(c, weight, size)
    ext = c.text_extents(s)
    if align == "center":
        x -= ext.x_advance / 2
    elif align == "right":
        x -= ext.x_advance
    c.set_source_rgba(*rgb, alpha)
    c.move_to(x, y)
    c.show_text(s)
    return ext.x_advance


def text_w(c, s, weight, size):
    font(c, weight, size)
    return c.text_extents(s).x_advance


# ---------------------------------------------------------------- state over time
def state(t):
    s = {}
    # flush: handle 6.3-6.9, flapper open 6.5-7.2, close 11.8-12.4
    s["flush"] = prog(t, 6.4, 7.1) * (1 - prog(t, 11.8, 12.4))
    # water level
    lvl = FULL
    lvl += (EMPTY - FULL) * prog(t, 7.0, 10.6)           # drain
    lvl -= (EMPTY - FULL) * prog(t, 12.8, 17.4)          # refill
    lvl += 70 * prog(t, 23.6, 26.0)                      # slow leak drop
    lvl -= 70 * prog(t, 26.4, 28.4)                      # refill again
    s["level"] = lvl
    s["spray"] = (12.8 < t < 17.4) or (26.4 < t < 28.4)
    s["drain"] = 7.0 < t < 11.4
    s["warp"] = prog(t, 19.6, 20.6) * (1 - prog(t, 30.0, 30.6))
    s["leak"] = prog(t, 22.9, 23.5) * (1 - prog(t, 30.0, 30.4))
    s["swap"] = prog(t, 29.9, 30.6)                       # old flapper out
    s["new"] = prog(t, 30.4, 31.0)                        # new flapper in
    s["xray"] = prog(t, 3.3, 5.4)
    zin = prog(t, 18.6, 19.6) * (1 - prog(t, 22.6, 23.5))
    s["zoom"] = zin
    return s


# ---------------------------------------------------------------- tank parts
def draw_interior(c, t, st):
    lvl = st["level"]
    c.set_source_rgb(*INTERIOR)
    c.rectangle(TX, TY, TW, TH)
    c.fill()
    # water with a gentle wave
    c.move_to(TX, TY + TH)
    for i in range(0, TW + 1, 16):
        x = TX + i
        c.line_to(x, lvl + 4 * math.sin(i / 52 + t * 2.4))
    c.line_to(TX + TW, TY + TH)
    c.close_path()
    g = cairo.LinearGradient(0, lvl, 0, TY + TH)
    g.add_color_stop_rgba(0, *WATER, 0.95)
    g.add_color_stop_rgba(1, *WATER_D, 0.95)
    c.set_source(g)
    c.fill()
    # surface highlight
    c.set_source_rgba(1, 1, 1, 0.55)
    c.set_line_width(4)
    for i in range(0, TW + 1, 16):
        x = TX + i
        y = lvl + 4 * math.sin(i / 52 + t * 2.4)
        c.line_to(x, y) if i else c.move_to(x, y)
    c.stroke()


def draw_overflow(c):
    x0 = TX + 470
    c.set_source_rgb(*PORC)
    rrect(c, x0, TY + 110, 34, TH - 130, 6)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(4)
    c.stroke()
    c.set_source_rgb(*NAVY2)
    c.rectangle(x0 + 6, TY + 110, 22, 8)
    c.fill()


def draw_fill_valve(c, t, st):
    x0 = TX + 70
    # shank below tank + supply line
    c.set_source_rgb(*NAVY2)
    c.rectangle(x0 + 4, TY + TH + 24, 22, 40)
    c.fill()
    c.set_line_width(8)
    c.move_to(x0 + 15, TY + TH + 64)
    c.curve_to(x0 + 15, TY + TH + 110, x0 - 40, TY + TH + 110, x0 - 40, 1080)
    c.stroke()
    # tube
    c.set_source_rgb(*PORC)
    rrect(c, x0, TY + 96, 30, TH - 96, 4)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(4)
    c.stroke()
    # float cup rides on the water
    ftop = clamp(st["level"] - 30, TY + 120, TY + TH - 80)
    c.set_source_rgb(*AMBER)
    rrect(c, x0 - 16, ftop, 62, 66, 10)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.stroke()
    # cap
    c.set_source_rgb(*NAVY2)
    rrect(c, x0 - 20, TY + 74, 70, 30, 8)
    c.fill()
    # refill tube to overflow
    c.set_source_rgb(*NAVY2)
    c.set_line_width(6)
    c.move_to(x0 + 50, TY + 88)
    c.curve_to(TX + 250, TY + 10, TX + 420, TY + 30, TX + 487, TY + 104)
    c.stroke()
    # spray
    if st["spray"]:
        for i in range(12):
            ph = (t * 1.7 + i / 12) % 1
            side = -1 if i % 2 else 1
            x = x0 + 15 + side * (14 + 34 * ph) + (i % 3) * 4
            y = TY + 110 + ph * (st["level"] - TY - 110)
            c.set_source_rgba(*WATER_D, 0.9 * (1 - ph * 0.6))
            c.arc(x, y, 5, 0, 2 * math.pi)
            c.fill()
        # hiss arcs
        for k in range(3):
            a = 0.35 + 0.65 * ((t * 2 + k / 3) % 1)
            c.set_source_rgba(*NAVY, 0.35 * (1 - a))
            c.set_line_width(3)
            c.arc(x0 + 15, TY + 88, 40 + 50 * a, -2.4, -0.7)
            c.stroke()
    return ftop


def flapper_shape(c, worn, new_glow=0.0):
    """Flapper in hinge-local coords, extending to -x."""
    c.new_path()
    if worn > 0:
        # warped, uneven slab
        pts = []
        for i in range(0, 141, 10):
            x = -i
            pts.append((x, -11 - worn * 6 * math.sin(i / 18)))
        for i in range(140, -1, -10):
            x = -i
            pts.append((x, 11 + worn * 5 * math.sin(i / 14 + 1)))
        c.move_to(*pts[0])
        for p in pts[1:]:
            c.line_to(*p)
        c.close_path()
    else:
        rrect(c, -140, -11, 140, 22, 10)
    # bulb that seats in the opening
    c.new_sub_path()
    c.save()
    c.translate(-72, 10)
    c.scale(52, 22 - worn * 6)
    c.arc(0, 0, 1, 0, math.pi)
    c.restore()
    col = tuple(AMBER[i] * (1 - worn) + WORN[i] * worn for i in range(3))
    c.set_source_rgb(*col)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.set_line_width(4)
    c.stroke()
    if worn > 0.3:  # cracks
        c.set_source_rgba(*NAVY, worn)
        c.set_line_width(2.5)
        for x in (-38, -96):
            c.move_to(x, -9)
            c.line_to(x + 6, -1)
            c.line_to(x - 2, 6)
            c.stroke()
    # hinge ear
    c.set_source_rgb(*NAVY2)
    c.arc(0, 0, 9, 0, 2 * math.pi)
    c.fill()


def flapper_angle(st):
    ang = math.radians(72) * st["flush"]
    ang += math.radians(4.5) * st["warp"] * (1 - st["swap"])  # warped: never quite closes
    return ang


def attach_point(st):
    a = flapper_angle(st)
    return HINGE[0] - ATTACH * math.cos(a), HINGE[1] - 11 - ATTACH * math.sin(a)


def draw_seat_and_drain(c, t, st):
    # drain pipe below tank
    x0, x1 = HOLE
    c.set_source_rgb(*INTERIOR)
    c.rectangle(x0 + 6, TY + TH, x1 - x0 - 12, 1080 - TY - TH)
    c.fill()
    if st["drain"]:
        a = clamp((t - 7.0) / 0.4) * clamp((11.4 - t) / 0.6)
        c.set_source_rgba(*WATER_D, 0.95 * a)
        c.rectangle(x0 + 6, TY + TH - 6, x1 - x0 - 12, 1080)
        c.fill()
        c.set_source_rgba(1, 1, 1, 0.5 * a)
        c.set_line_width(5)
        for k in range(5):
            y = TY + TH + ((t * 260 + k * 60) % 300)
            c.move_to(x0 + 30 + k * 14, y)
            c.line_to(x0 + 30 + k * 14, y + 36)
            c.stroke()
        # swirl above the opening
        c.set_source_rgba(1, 1, 1, 0.45 * a)
        c.set_line_width(4)
        for k in range(3):
            r = 30 + k * 22
            c.arc((x0 + x1) / 2, TY + TH - 30, r, t * 5 + k, t * 5 + k + 2.2)
            c.stroke()
    if st["leak"] > 0:
        a = st["leak"]
        c.set_source_rgba(*WATER_D, 0.95 * a)
        c.set_line_width(5)
        c.move_to(x0 + 10, TY + TH - 6)
        for k in range(0, 200, 8):
            c.line_to(x0 + 14 + 3 * math.sin(k / 9 + t * 8), TY + TH - 6 + k)
        c.stroke()
        for k in range(4):
            y = TY + TH + 200 + ((t * 150 + k * 40) % 160)
            c.arc(x0 + 15, y, 5, 0, 2 * math.pi)
            c.fill()
    # pipe walls
    c.set_source_rgb(*NAVY)
    c.set_line_width(6)
    for x in (x0 + 6, x1 - 6):
        c.move_to(x, TY + TH + 8)
        c.line_to(x, 1080)
        c.stroke()
    # valve seat ring
    c.set_source_rgb(*NAVY2)
    c.rectangle(x0 - 10, TY + TH - 8, 22, 14)
    c.rectangle(x1 - 12, TY + TH - 8, 22, 14)
    c.fill()


def draw_flapper(c, t, st):
    a = flapper_angle(st)
    old_alpha = 1 - st["new"]
    # old flapper (slides left & fades during swap)
    if old_alpha > 0.01:
        c.save()
        c.push_group()
        c.translate(HINGE[0] - 260 * st["swap"], HINGE[1] - 120 * st["swap"])
        c.rotate(a + 0.4 * st["swap"])
        flapper_shape(c, st["warp"])
        c.pop_group_to_source()
        c.paint_with_alpha(1 - st["swap"])
        c.restore()
    if st["new"] > 0:
        n = st["new"]
        c.save()
        c.translate(HINGE[0], HINGE[1] - 160 * (1 - back(n)))
        c.push_group()
        flapper_shape(c, 0.0)
        c.pop_group_to_source()
        c.paint_with_alpha(clamp(n * 2))
        c.restore()


def draw_chain_arm(c, t, st):
    f = st["flush"]
    arm_a = -math.radians(10) * f
    ex = PIVOT[0] + ARM_LEN * math.cos(arm_a)
    ey = PIVOT[1] + ARM_LEN * math.sin(arm_a)
    ax, ay = attach_point(st)
    if st["swap"] > 0 and st["new"] < 1:
        ax, ay = HINGE[0] - ATTACH, HINGE[1] - 11
    # chain: sagging bezier made of links
    sag = 40 * (1 - f)
    pts = []
    for i in range(0, 41):
        u = i / 40
        x = ex + (ax - ex) * u + sag * math.sin(math.pi * u)
        y = ey + (ay - ey) * u
        pts.append((x, y))
    c.set_line_width(3)
    for i, (x, y) in enumerate(pts):
        c.set_source_rgb(*BODY)
        c.save()
        c.translate(x, y)
        c.scale(1, 1.6)
        c.arc(0, 0, 4.2, 0, 2 * math.pi)
        c.restore()
        c.stroke()
    # arm
    c.set_source_rgb(*NAVY2)
    c.set_line_width(12)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.move_to(*PIVOT)
    c.line_to(ex, ey)
    c.stroke()
    c.set_line_cap(cairo.LINE_CAP_BUTT)
    return (ex, ey), (ax, ay)


def draw_walls(c, t, st):
    # porcelain wall ring (even-odd)
    c.set_fill_rule(cairo.FILL_RULE_EVEN_ODD)
    rrect(c, TX - 26, TY - 26, TW + 52, TH + 52, 28)
    c.rectangle(TX, TY, TW, TH)
    c.set_source_rgb(*PORC)
    c.fill_preserve()
    c.set_fill_rule(cairo.FILL_RULE_WINDING)
    c.set_source_rgb(*NAVY)
    c.set_line_width(5)
    c.stroke()
    # lid
    rrect(c, TX - 44, TY - 74, TW + 88, 50, 16)
    c.set_source_rgb(*PORC)
    c.fill_preserve()
    c.set_source_rgb(*NAVY)
    c.stroke()
    # outside handle (pushes down while flushing)
    f = st["flush"]
    c.save()
    c.translate(TX - 26, TY + 58)
    c.rotate(math.radians(28) * f)
    rrect(c, -86, -10, 86, 20, 10)
    c.set_source_rgb(*NAVY2)
    c.fill()
    c.restore()
    # front cover before the x-ray reveal (wipe left -> right)
    xr = st["xray"]
    if xr < 1:
        wx = TX + TW * xr
        c.save()
        c.rectangle(wx, TY, TX + TW - wx, TH)
        c.clip()
        c.set_source_rgb(*PORC)
        c.rectangle(TX, TY, TW, TH)
        c.fill()
        g = cairo.LinearGradient(TX, 0, TX + TW, 0)
        g.add_color_stop_rgba(0, 0, 0, 0, 0.0)
        g.add_color_stop_rgba(1, *NAVY, 0.07)
        c.set_source(g)
        c.rectangle(TX, TY, TW, TH)
        c.fill()
        c.restore()
        if xr > 0:
            c.set_source_rgba(*AMBER, 0.35)
            c.rectangle(wx - 14, TY - 4, 28, TH + 8)
            c.fill()
            c.set_source_rgb(*AMBER)
            c.rectangle(wx - 3, TY - 4, 6, TH + 8)
            c.fill()


# ---------------------------------------------------------------- overlays
def pop(t, t0, dur=0.32):
    return back((t - t0) / dur) if t >= t0 else 0.0


def label(c, t, t0, t1, s, anchor, pos, side="right"):
    a = pop(t, t0) * (1 - prog(t, t1, t1 + 0.3))
    if a <= 0.001:
        return
    al = clamp(a)
    w = text_w(c, s, "semi", 32) + 44
    hgt = 58
    px, py = pos
    bx = px if side == "right" else px - w
    # leader line
    ex = bx if side == "right" else bx + w
    c.set_source_rgba(*NAVY, al)
    c.set_line_width(3)
    c.move_to(*anchor)
    c.line_to(ex, py + hgt / 2)
    c.stroke()
    c.arc(*anchor, 8, 0, 2 * math.pi)
    c.fill()
    c.save()
    c.translate(bx + w / 2, py + hgt / 2)
    c.scale(a, a)
    rrect(c, -w / 2, -hgt / 2, w, hgt, hgt / 2)
    c.set_source_rgba(1, 1, 1, al)
    c.fill_preserve()
    c.set_source_rgba(*NAVY, al)
    c.set_line_width(3)
    c.stroke()
    text(c, s, -w / 2 + 22, 11, "semi", 32, NAVY, al)
    c.restore()


def chip(c, t, t0, x, y, big, small, bg=NAVY, fg=CREAM, accent=AMBER, t1=99):
    a = pop(t, t0) * (1 - prog(t, t1, t1 + 0.3))
    if a <= 0.001:
        return
    al = clamp(a)
    wb = text_w(c, big, "black", 64)
    ws = text_w(c, small, "semi", 28)
    w = max(wb, ws) + 64
    hgt = 150
    c.save()
    c.translate(x, y + hgt / 2)
    c.scale(a, a)
    rrect(c, 0, -hgt / 2, w, hgt, 26)
    c.set_source_rgba(*bg, al)
    c.fill()
    text(c, big, 32, -4, "black", 64, accent, al)
    text(c, small, 32, 44, "semi", 28, fg, al)
    c.restore()


SCENES = [  # (start, kicker, headline)
    (0.0, "TOILET KEEPS RUNNING?", "Here's what's happening"),
    (3.2, "INSIDE THE TANK", "How a toilet tank works"),
    (6.0, "STEP 1 · FLUSH", "The chain lifts the flapper"),
    (11.6, "STEP 2 · REFILL", "The fill valve refills the tank"),
    (18.6, "THE PROBLEM", "A worn flapper stops sealing"),
    (22.7, "THE RESULT", "Leak, refill, repeat"),
    (29.3, "THE FIX", "Replace the flapper"),
]


def headline(c, t):
    idx = max(i for i, s in enumerate(SCENES) if s[0] <= t)
    t0, kick, head = SCENES[idx]
    a = clamp((t - t0) / 0.35)
    off = 24 * (1 - ease(a))
    size = 66
    w = max(text_w(c, head, "xbold", size), text_w(c, kick, "semi", 26)) + 80
    rrect(c, 60, 52, w, 168, 28)
    c.set_source_rgba(*CREAM, 0.96)
    c.fill()
    text(c, kick, 100, 108 + off, "semi", 26, AMBER, a)
    text(c, head, 100, 180 + off, "xbold", size, NAVY, a)
    # progress dots
    for i in range(len(SCENES)):
        c.set_source_rgba(*(AMBER if i == idx else NAVY), 1 if i == idx else 0.18)
        c.arc(100 + i * 26, 252, 7, 0, 2 * math.pi)
        c.fill()


def brand(c, t):
    text(c, "HOME IMPROVEMENT HUB", W - 70, 70, "xbold", 24, NAVY, 0.55, align="right")


def footer(c, t, t0):
    a = pop(t, t0)
    if a <= 0:
        return
    s1 = "Full step-by-step guide"
    s2 = "homeimprovementhub101.com"
    w = max(text_w(c, s1, "semi", 28), text_w(c, s2, "xbold", 40)) + 70
    c.save()
    c.translate(1130 + w / 2, 930)
    c.scale(a, a)
    rrect(c, -w / 2, -62, w, 124, 30)
    c.set_source_rgb(*AMBER)
    c.fill()
    text(c, s1, -w / 2 + 35, -12, "semi", 28, NAVY)
    text(c, s2, -w / 2 + 35, 36, "xbold", 40, NAVY)
    c.restore()


def check(c, t, t0, x, y, r=46):
    a = pop(t, t0)
    if a <= 0:
        return
    c.save()
    c.translate(x, y)
    c.scale(a, a)
    c.set_source_rgb(*GREEN)
    c.arc(0, 0, r, 0, 2 * math.pi)
    c.fill()
    c.set_source_rgb(1, 1, 1)
    c.set_line_width(r * 0.2)
    c.set_line_cap(cairo.LINE_CAP_ROUND)
    c.move_to(-r * 0.42, 0)
    c.line_to(-r * 0.1, r * 0.32)
    c.line_to(r * 0.45, -r * 0.34)
    c.stroke()
    c.restore()


# ---------------------------------------------------------------- frame
def frame(c, t):
    st = state(t)
    c.set_source_rgb(*CREAM)
    c.paint()
    # soft paper panel behind the tank
    c.set_source_rgb(*PAPER)
    c.arc(TX + TW / 2, TY + TH / 2 + 30, 560, 0, 2 * math.pi)
    c.fill()

    # camera
    z = st["zoom"]
    s = 1 + 1.5 * z
    fx = W / 2 + (HINGE[0] - 70 - W / 2) * z
    fy = H / 2 + (HINGE[1] - 40 - H / 2) * z
    sx = W / 2 + (980 - W / 2) * z
    sy = H / 2 + (620 - H / 2) * z
    push = 1 + 0.025 * prog(t, 0, 3.2) * (1 - prog(t, 3.2, 4.0))
    c.save()
    c.translate(sx, sy)
    c.scale(s * push, s * push)
    c.translate(-fx, -fy)

    draw_interior(c, t, st)
    draw_overflow(c)
    ftop = draw_fill_valve(c, t, st)
    draw_seat_and_drain(c, t, st)
    draw_flapper(c, t, st)
    arm_end, att = draw_chain_arm(c, t, st)
    draw_walls(c, t, st)

    # hook: running sound waves over the lid
    if t < 3.4:
        a = prog(t, 0.3, 0.8) * (1 - prog(t, 3.0, 3.4))
        for k in range(3):
            ph = (t * 1.2 + k / 3) % 1
            c.set_source_rgba(*WATER_D, a * (1 - ph))
            c.set_line_width(6)
            c.arc(TX + TW + 20, TY + 120, 40 + 90 * ph, -1.0, 1.0)
            c.stroke()
        text(c, "sssss…", TX + TW + 150, TY + 135, "xbold", 48, WATER_D, a)

    # world-space callouts (camera at rest)
    label(c, t, 7.2, 11.4, "Chain", ((arm_end[0] + att[0]) / 2 + 20, (arm_end[1] + att[1]) / 2), (1130, 430))
    label(c, t, 7.9, 11.4, "Flapper", (att[0] - 20, att[1] + 6), (1130, 760))
    label(c, t, 12.9, 18.4, "Fill valve", (TX + 66, TY + 300), (330, 470), side="left")
    label(c, t, 15.6, 18.4, "Float", (TX + 54, ftop + 33), (330, 640), side="left")
    if 17.2 < t < 18.6:
        check(c, t, 17.2, TX + 85, TY + 40, 34)

    # zoomed: worn flapper ring
    if z > 0.01:
        a = pop(t, 20.7) * (1 - prog(t, 22.4, 22.8))
        if a > 0:
            c.set_source_rgba(*RED, clamp(a))
            c.set_line_width(5)
            c.set_dash([14, 9], t * 30)
            c.arc(HINGE[0] - 72, HINGE[1] + 2, 95 * a, 0, 2 * math.pi)
            c.stroke()
            c.set_dash([])
    if 22.9 < t < 30.0:
        label(c, t, 23.4, 29.6, "Slow leak", (HOLE[0] + 14, TY + TH + 120), (1130, 760))
    if t > 30.9:
        check(c, t, 31.0, HINGE[0] - 72, HINGE[1] - 90, 40)
    c.restore()

    # screen-space overlays
    if z > 0.6:
        a = pop(t, 20.0) * (1 - prog(t, 22.3, 22.7))
        if a > 0:
            c.save()
            c.translate(1330, 470)
            c.scale(a, a)
            for i, s_ in enumerate(["Warped rubber", "Gap = no seal"]):
                w = text_w(c, s_, "xbold", 44) + 60
                rrect(c, 0, i * 100, w, 80, 40)
                c.set_source_rgb(*(RED if i else NAVY))
                c.fill()
                text(c, s_, 30, i * 100 + 55, "xbold", 44, CREAM)
            c.restore()

    chip(c, t, 27.0, 1130, 300, "200 gal/day", "Up to this much water wasted", t1=29.2)
    chip(c, t, 27.8, 1130, 480, "Refills again…", "and again, all day long", bg=PAPER, fg=NAVY, accent=RED, t1=29.2)
    chip(c, t, 31.5, 1130, 330, "About $5", "for a new flapper")
    chip(c, t, 32.3, 1130, 510, "10 minutes", "no tools needed")
    footer(c, t, 32.7)

    headline(c, t)
    brand(c, t)


def render(out="toilet_sample_silent.mp4", stills=None):
    surf = cairo.ImageSurface(cairo.FORMAT_ARGB32, W, H)
    c = cairo.Context(surf)
    c.set_antialias(cairo.ANTIALIAS_GOOD)
    if stills:
        for ts in stills:
            frame(c, ts)
            surf.write_to_png(f"still_{ts:05.1f}.png")
        return
    p = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "bgra",
                          "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset",
                          "veryfast", "-crf", "18", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(int(DUR * FPS)):
        frame(c, i / FPS)
        surf.flush()
        p.stdin.write(surf.get_data())
    p.stdin.close()
    p.wait()


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "stills":
        render(stills=[float(x) for x in sys.argv[2:]])
    else:
        render()
