#!/usr/bin/env bash
# Fails if any HIH file outside assets/hih-tokens.css hard-codes a color or a px/ms value.
# Scope: HIH-owned files (assets/hih*.css|js, sections/hih-*.liquid, snippets/hih-*.liquid).
set -euo pipefail
cd "$(dirname "$0")/.."
files=$(ls assets/hih*.css assets/hih*.js sections/hih-*.liquid snippets/hih-*.liquid 2>/dev/null | grep -v 'assets/hih-tokens.css' || true)
status=0
for f in $files; do
  # hex colors, rgb()/hsl(), px and ms literals (0px allowed). Skip SVG path data, viewBox and width/height attrs.
  hits=$(grep -nE '#[0-9a-fA-F]{3,8}\b|rgba?\(|hsla?\(|[^0-9a-zA-Z._-][1-9][0-9]*(\.[0-9]+)?(px|ms)\b' "$f" \
    | grep -vE 'viewBox=|<path|stroke-width=|<svg|&#|scripts/check-tokens' || true)
  if [ -n "$hits" ]; then echo "✗ $f"; echo "$hits"; status=1; fi
done
[ $status -eq 0 ] && echo "✓ tokens: no raw colors or px/ms values outside hih-tokens.css"
exit $status
