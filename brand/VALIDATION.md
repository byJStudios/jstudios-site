# Validation

- Approved glyph JSON SHA-256 checked byte-for-byte.
- Both color variants generated from identical path strings.
- Edge Chromium: both main pages at 320, 390, 768, 1440 px; no horizontal overflow.
- JS startup timeline states verified at 100, 600, 1100, 1300, 1500, 2000 and 2500 ms.
- Reduced-motion mode: all glyphs visible and animation stopped.
- No browser runtime exceptions in this test.
- Desktop and mobile screenshots inspected.
- Primary mark SVG is a polygon approximation of the approved PNG, mask IoU 99.30%; the approved raster master is not modified.

The website is deployed through Cloudflare Workers with repository-only Git integration. Contact information is live; formal legal compliance remains unverified.


## 2026-11-25 — site polish

- Geometry: all existing SVG path data and viewBoxes unchanged; one duplicate animated cursor removed per animated logo. Static SVG assets and both master JSON files unchanged.
- Edge Chromium: all three pages at 320, 390, 768, 1440, 1920 and 6400 CSS px (18/18). The last viewport uses a 0.25 device scale to simulate extreme zoom-out, not the browser zoom UI.
- Full-viewport background without tiling and no horizontal overflow verified.
- Real-time startup sequence and idle blink verified for header and hero on both primary pages. Repeated run with denser sampling observed every character state, including the Skolary credit. An earlier sparse sampling run missed a state.
- Static fallback without JavaScript and reduced-motion mode passed; no browser runtime exceptions in final run.
- Legal information is reorganized; complete legal compliance is not certified (no public postal address).

## Portfolio v1.0

- Original and extended glyph masters verified by SHA-256; no changes to approved geometry.
- Revision 6: 1/4 reveal accepted by owner; simulated frame rates 30–144 Hz and native wheel regression tests passed.
- Seven public repositories, each a single clean commit with MIT license; application startup tested in separate local copies, not real data.
- No real school, finance, audio or playback-history files in website or public project repositories.
