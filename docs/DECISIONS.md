# Design and build decisions

One dated line per decision, with the reason. Newest last.

- 2026-11-01: Visual direction is "Calm Home" (eucalyptus green, mist, Instrument Serif + Manrope), picked by the owner from 5 mockups.
- 2026-11-01: Base theme is Shopify Dawn v16.0.0. It is maintained, simpler to extend than Horizon's theme-block architecture, and HIH is content-led, not catalog-led.
- 2026-11-01: All HIH UI lives in hih-* sections, snippets and assets. Dawn core files are untouched except one `render 'hih-head'` line in layout/theme.liquid, so upstream Dawn updates can still be merged.
- 2026-11-01: Tokens live only in assets/hih-tokens.css, which also remaps Dawn's font variables. Enforced by scripts/check-tokens.sh. No merchant-editable token settings yet; add them to settings_schema.json only when the owner asks.
- 2026-11-01: Header and footer are HIH sections (header-group/footer-group), so Dawn colour schemes don't control HIH pages.
- 2026-11-01: Fonts are self-hosted woff2 (SIL OFL 1.1, from Fontsource) because neither family is in Shopify's font library and self-hosting avoids a third-party request.
- 2026-11-01: Motion plan: (1) one orchestrated page-load moment on the home hero; (2) native cross-document View Transitions, with the guide card photo morphing into the guide hero; (3) scroll-driven reading-progress line on guides (CSS only); (4) feedback motion: image fade-in on decode, check-mark draw on "Mark step done", active step in the table of contents. No per-section scroll reveals. Everything collapses to instant under prefers-reduced-motion via tokens.
- 2026-11-01: YouTube loads only after the reader presses play (youtube-nocookie). The poster comes from i.ytimg.com (RemoteAsset warning disabled with a reason here), because downloading thumbnails to our CDN would copy the creator's image.
- 2026-11-01: Remaining theme-check warnings are in unmodified Dawn files (OrphanedSnippet, VariableName, UnusedAssign, LiquidComplexity, UndefinedObject) and are left as upstream ships them.
- 2026-11-01: Featured-guide blocks on the homepage ship with no article selected. Drafts can't be featured; pick guides in the theme editor after publishing them.
- 2026-11-01: Categories sit in their own header row (horizontal scroll if needed) because 10 categories don't fit beside the logo at 1440px.
- 2026-11-01: HIH header/footer use their own menu (hih-categories) so the live Gecko theme's main-menu stays untouched.
- 2026-11-01: Repo layout: theme at the root (what Shopify's GitHub sync expects); HIH content tooling lives in hih/, which Shopify ignores.
- 2026-11-01: HIH/main is now the LIVE theme (published by the owner). Pushing to main deploys to visitors, so all changes go on a hih/* branch and reach main only through a PR the owner merges.
- 2026-11-01: The featured-guides section renders nothing on the storefront until at least one selected guide is published (it stays visible in the theme editor).
- 2026-11-01: Widened the layout at the owner's request ("looks thin"). Page frame is 1440px (was 1240), guide body 58rem (was 44rem), guide sidebar 20rem (was 17rem), paragraph measure 44em (was 38em). All widths are tokens in hih-tokens.css under "Layout widths".
- 2026-11-01: Owner's rule: commit straight to main (no PRs). Shopify syncs main to the live theme.
- 2026-11-01: Header/footer were missing on the live site because their link_list defaults were 'hih-categories' (Shopify only accepts main-menu/footer and silently drops the section). Defaults removed; the menu is set in the group JSON. scripts/check-schema.py now catches this.
- 2026-11-01: 'Home ›' breadcrumb on category and guide pages, in addition to the logo link and the category row in the header.
- 2026-11-01: All HIH sizes are written in Dawn's 10px rem (Dawn sets html to 62.5%). Previously tokens assumed 16px, so the whole site rendered at 62.5% of design ("thin", "small words"). Only hih-tokens.css may hold rem values; check-tokens.sh enforces it. Previews must load Dawn's base.css and root rule.
- 2026-11-01: Logo = the owner's house-and-wrench design, traced to vector (hih/brand, hih/scripts/logo_*.py) and recolored to the theme: ink #1f2a26 + leaf #3d7a5e (5.1:1 on paper); footer uses paper + leaf-light #a9cdb9. One inline SVG symbol (hih-logo-defs, rendered in the header) drawn by hih-logo via <use>, colored by tokens. Header image_picker still overrides it.
- 2026-11-01: Category tiles are a fixed 2-column (phone/tablet) / 5-column (desktop) grid so 10 categories never leave a ragged row.
- 2026-11-01: Theme favicon assets/hih-favicon.png is used unless one is set in Theme settings.
- 2026-11-01: Card/tile motion = "the card you're on comes forward, the rest step back": lift + shadow + title underline, siblings dim (CSS :has), pointer spotlight (hih.js sets --hih-spot-x/y), press scale on touch. Hover effects are (hover: hover) and (pointer: fine) only; :focus-visible gets the same. No 3D tilt, parallax or scroll reveals.
- 2026-11-01: Empty category tiles show a line icon per blog handle (snippets/hih-category-icon.liquid) that redraws on hover; with a photo it becomes a corner badge. Tiles show "N guides →" (slides in on hover, always shown on touch).
- 2026-11-01: View transitions are attribute-driven (hih-head): data-vt-href + data-vt-name on the old page morph into data-vt-to on the new page (card photo → guide hero, tile title → category title). Between tag filters of one category, cards keep names hih-card-<id> so they slide to their new spots.
- 2026-11-01: Guide pages store their step count (hih:total:<id>) next to done steps (hih:done:<id>). Started guides show "Step N of T" + a progress bar on every card and move to the front of their grid (DOM move, so keyboard order matches).
