import cairo, math
from ws_video import *
surf=cairo.ImageSurface(cairo.FORMAT_ARGB32,1280,720); c=cairo.Context(surf)
c.set_source_rgb(*AMBER); c.paint()
st=state(125.0); st["bypass"]=0; st["lid"]=0
c.save(); c.translate(720,70); c.scale(0.76,0.76); c.translate(-470,-300)
c.set_source_rgb(*CREAM); rrect(c,420,250,840,760,40); c.fill()
draw_resin(c,125,st); draw_brine(c,125,st)
c.set_source_rgba(*RED,1); c.set_line_width(6); c.set_dash([16,10]); c.rectangle(WELL[1]+10,834,BX+BW-WELL[1]-20,st["water"]-838); c.stroke(); c.set_dash([])
c.restore()
text(c,"WATER",50,170,"black",120,NAVY)
text(c,"SOFTENER",50,290,"black",120,NAVY)
rrect(c,50,330,470,110,24); c.set_source_rgb(*NAVY); c.fill()
text(c,"6 EASY JOBS",78,410,"black",68,AMBER)
text(c,"Hard water again?",56,520,"xbold",46,NAVY)
text(c,"HOME IMPROVEMENT HUB",56,680,"xbold",28,NAVY,0.7)
surf.write_to_png("thumb.png")
