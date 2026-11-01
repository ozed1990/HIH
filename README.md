# Home Improvement Hub: Shopify theme and guides

The repository root **is the Shopify theme** (Dawn 16 + the HIH "Calm Home" layer). Shopify's GitHub integration syncs this branch to an unpublished theme.

| Path | Owner skill | What it is |
|---|---|---|
| `assets/hih-*`, `sections/hih-*`, `snippets/hih-*`, `templates/*.json` | hih-theme | The HIH theme layer. Tokens live only in `assets/hih-tokens.css`. |
| `docs/DECISIONS.md` | hih-theme | Dated design and build decisions |
| `scripts/check-tokens.sh` | hih-theme | Fails on raw colors or px/ms values outside the tokens file |
| `hih/content/guides.py` | hih-guide-writer | Source of the guides (Guide contract) |
| `hih/scripts/build_guides.py` | hih-guide-writer | Renders and validates guides → `hih/content/out/*.json` |
| `hih/scripts/diagrams.py`, `render_diagrams.js` | hih-media | Original step diagrams → `hih/content/media/*.webp` |

Checks before every commit:

```
scripts/check-tokens.sh
npx @shopify/cli theme check --fail-level error
python3 hih/scripts/build_guides.py
```

Affiliate placeholders in guides use `href="#add-affiliate-link"`. Search for it in Shopify admin and paste your affiliate URL.
