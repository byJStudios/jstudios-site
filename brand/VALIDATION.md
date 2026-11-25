# Validation

- Approved glyph JSON SHA-256 checked byte-for-byte.
- Both color variants generated from identical path strings.
- Edge Chromium: both main pages at 320, 390, 768, 1440 px; no horizontal overflow.
- JS startup timeline states verified at 100, 600, 1100, 1300, 1500, 2000 and 2500 ms.
- Reduced-motion mode: all glyphs visible and animation stopped.
- No browser runtime exceptions in this test.
- Desktop and mobile screenshots inspected.
- Primary mark SVG is a polygon approximation of the approved PNG, mask IoU 99.30%; the approved raster master is not modified.

Public deployment pending confirmed operator details and Cloudflare Git authorization.
