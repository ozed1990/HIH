# Home Improvement Hub theme

Dawn v16 + the HIH layer. Owner skill: hih-theme. Guide content format: hih-guide-writer (Guide contract).

| Path | What it is |
|---|---|
| assets/hih-tokens.css | Every color, font, size and motion value. The only place to change the look. |
| assets/hih.css, assets/hih.js | Components and interactions, which use tokens only |
| snippets/hih-head.liquid | Fonts, styles and the view-transition hook (rendered in layout/theme.liquid) |
| sections/hih-*.liquid | Header, footer, hero, categories, featured guides, newsletter, category page, guide page |
| templates/index.json, blog.json, article.json | Wire HIH sections into pages |
| scripts/check-tokens.sh | Fails on raw colors or px/ms values outside the tokens file |

Before every commit: `scripts/check-tokens.sh && npx @shopify/cli theme check --fail-level error`
