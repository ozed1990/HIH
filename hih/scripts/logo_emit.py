import json,re
P=json.load(open('hih/brand/logo-paths.json'))
def rnd(d): return re.sub(r'-?\d+\.\d+', lambda m: str(round(float(m.group()))), d)
def layer(name):
    s=""
    if P[name]["dark_bbox"]: s+=f'<path fill-rule="evenodd" class="hih-logo-ink" d="{rnd(P[name]["dark"])}"/>'
    if P[name]["blue_bbox"]: s+=f'<path fill-rule="evenodd" class="hih-logo-leaf" d="{rnd(P[name]["blue"])}"/>'
    return s
W=1489; h1=93; h2=h1*2.1; s2=h2/225; gap=30; th=h1+gap+h2; mh=738; sm=th*1.25/mh; mw=860*sm; tx=mw+60; mtot=mh*sm; ty=(mtot-th)/2
VB=f"0 0 {round(tx+W)} {round(mtot)}"
sym=(f'<symbol id="hih-logo-art" viewBox="{VB}">'
 f'<g transform="scale({sm:.4f}) translate(-595 -425)">{layer("mark")}</g>'
 f'<g transform="translate({tx:.1f} {ty:.1f}) translate(-279 -1241)">{layer("line1")}</g>'
 f'<g transform="translate({tx:.1f} {ty+h1+gap:.1f}) scale({s2:.4f}) translate(-665 -1385)">{layer("hub")}</g></symbol>')
open('snippets/hih-logo-defs.liquid','w').write(
"{%- comment -%} HIH logo artwork, defined once per page (rendered by hih-header) and drawn by hih-logo via <use>.\n  Traced from the owner's logo; colors come from tokens through --hih-logo-ink / --hih-logo-leaf. {%- endcomment -%}\n"
f'<svg class="hih-svg-defs" aria-hidden="true" focusable="false">{sym}</svg>\n')
open('snippets/hih-logo.liquid','w').write(
"{%- comment -%} Horizontal logo lockup. Needs hih-logo-defs on the page (the header renders it). {%- endcomment -%}\n"
f'<svg class="hih-logo__svg" viewBox="{VB}" role="img" aria-label="Home Improvement Hub"><use href="#hih-logo-art"></use></svg>\n')
# favicon mark svg (standalone, for PNG render only)
mark=f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><rect width="512" height="512" rx="96" fill="#ffffff"/><g transform="translate(46 70) scale(0.488) translate(-595 -425)">{layer("mark").replace("class=\"hih-logo-ink\"","fill=\"#1f2a26\"").replace("class=\"hih-logo-leaf\"","fill=\"#3d7a5e\"")}</g></svg>'
open('hih/brand/favicon.svg','w').write(mark)
print(VB, len(sym))
