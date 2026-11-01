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
