#!/usr/bin/env python3
"""Catch section schemas Shopify silently rejects on GitHub sync (theme check does not).
Rules: valid JSON schema; link_list defaults only 'main-menu' or 'footer'; every section used in a
template/section-group JSON exists in sections/."""
import json, re, sys, pathlib
root = pathlib.Path(__file__).resolve().parents[1]
errs = []
for f in sorted((root / "sections").glob("*.liquid")):
    m = re.search(r"\{%\s*schema\s*%\}(.*?)\{%\s*endschema\s*%\}", f.read_text(), re.S)
    if not m: continue
    try: schema = json.loads(m.group(1))
    except json.JSONDecodeError as e: errs.append(f"{f.name}: invalid schema JSON ({e})"); continue
    settings = list(schema.get("settings", [])) + [s for b in schema.get("blocks", []) for s in b.get("settings", [])]
    for s in settings:
        if s.get("type") == "link_list" and "default" in s and s["default"] not in ("main-menu", "footer"):
            errs.append(f"{f.name}: link_list '{s['id']}' default must be main-menu or footer, got {s['default']!r}")
existing = {p.stem for p in (root / "sections").glob("*.liquid")}
for f in list((root / "templates").glob("*.json")) + list((root / "sections").glob("*.json")):
    txt = re.sub(r"^/\*.*?\*/", "", f.read_text(), flags=re.S)
    for sec in json.loads(txt).get("sections", {}).values():
        if sec["type"] not in existing: errs.append(f"{f.relative_to(root)}: section type '{sec['type']}' not found")
print("\n".join("✗ " + e for e in errs) if errs else "✓ schema: all section schemas and references valid")
sys.exit(1 if errs else 0)
