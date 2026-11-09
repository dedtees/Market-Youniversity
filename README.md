# Market Youniversity

Homepage concepts for the new Market Youniversity site: the training arm alongside
Pinpoint Promotions & Marketing and Eric Duchin Consulting.

This is a plain static site, so Vercel serves it with no build step and no framework.

| Path | Concept | Look |
| --- | --- | --- |
| `/` | Index comparing the four concepts | |
| `/concept-1/` | Split: individuals and organizations side by side | Poster-style blue and pink halves |
| `/concept-2/` | Spotlight: presentation skills first | Dark stage, gold serif, recording light |
| `/concept-3/` | Editorial: organizations first | Big type, numbered sections, yellow highlights |
| `/concept-4/` | Unlock: community, then workshops, as levels | Neon, game-like unlocks |

Each concept is a self-contained `index.html` with its own styles. `assets/common.js`
handles the mobile menu, scroll reveals and the review-only concept switcher;
`assets/img/` holds photos taken from the earlier mockups.

Placeholders: prices and dates are not set, testimonials are samples, forms don't
submit yet, and the Eric Duchin Consulting link needs its URL. The production site is
planned for WordPress with an LMS; these pages are for choosing positioning and look.
