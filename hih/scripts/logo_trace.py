# Rebuild the HIH logo from hih/brand/logo-source.jpg (run from repo root):
#   pip install potracer pillow numpy; python3 hih/scripts/logo_trace.py; python3 hih/scripts/logo_emit.py
# Then render hih/brand/favicon.svg to assets/hih-favicon.png (512px, Playwright screenshot).
import numpy as np, potrace, json
from PIL import Image, ImageFilter
im=np.array(Image.open('hih/brand/logo-source.jpg').convert('RGB')).astype(int)
r,g,b=im[...,0],im[...,1],im[...,2]
blue=(b-r>60)
dark=(~blue)&(im.max(-1)<160)
def clean(m):
    i=Image.fromarray((m*255).astype('uint8')).filter(ImageFilter.MedianFilter(5))
    return np.array(i)>127
blue,dark=clean(blue),clean(dark)
def trace(mask):
    bm=potrace.Bitmap(~mask)
    p=bm.trace(turdsize=40, alphamax=0.8, opticurve=True, opttolerance=0.3)
    d=[]
    for c in p:
        s=c.start_point; d.append(f"M{s.x:.1f} {s.y:.1f}")
        for seg in c.segments:
            if seg.is_corner: d.append(f"L{seg.c.x:.1f} {seg.c.y:.1f}L{seg.end_point.x:.1f} {seg.end_point.y:.1f}")
            else: d.append(f"C{seg.c1.x:.1f} {seg.c1.y:.1f} {seg.c2.x:.1f} {seg.c2.y:.1f} {seg.end_point.x:.1f} {seg.end_point.y:.1f}")
        d.append("Z")
    return "".join(d)
def region(m,y0,y1):
    z=np.zeros_like(m); z[y0:y1]=m[y0:y1]; return z
out={}
for name,(y0,y1) in {"mark":(420,1180),"line1":(1220,1360),"hub":(1365,1640)}.items():
    out[name]={"dark":trace(region(dark,y0,y1)),"blue":trace(region(blue,y0,y1))}
    for k in ("dark","blue"):
        ys,xs=np.where(region(dark if k=="dark" else blue,y0,y1))
        out[name][k+"_bbox"]=[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())] if len(xs) else None
json.dump(out,open('hih/brand/logo-paths.json','w'))
for n,v in out.items(): print(n,{k:(len(v[k]) if not k.endswith('bbox') else v[k]) for k in v})
