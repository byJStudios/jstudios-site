# JStudios website

[![Platform: Web](https://img.shields.io/badge/Platform-Web-7656b5.svg)](https://jstudios.pages.dev/)
[![Stack: HTML / CSS / JavaScript](https://img.shields.io/badge/Stack-HTML%20%2F%20CSS%20%2F%20JavaScript-3776ab.svg)](https://jstudios.pages.dev/)
[![Hosting: Cloudflare Pages](https://img.shields.io/badge/Hosting-Cloudflare%20Pages-16889c.svg)](https://pages.cloudflare.com/)
[![Status: Live](https://img.shields.io/badge/Status-Live-34841d.svg)](https://jstudios.pages.dev/)
[![License: Rights reserved](https://img.shields.io/badge/License-Rights%20reserved-356bb4.svg)](LICENSE)

Independent software development, Skolary, LensLink and seven publicly available software projects. Static public-facing site only; no private app source, credentials or user data.

**Preferred address:** https://jstudios.pages.dev/

## Local preview

From the repository root run:

    python -m http.server 8787 --bind 127.0.0.1 --directory site

Open http://127.0.0.1:8787/.

## Deployment

Cloudflare Pages is connected to main with no build command and output directory site/. The existing Cloudflare Workers Static Assets configuration remains available during migration. No paid domain or paid hosting service is required.

## Branding

See [brand kit](brand/README.md) and [validation](brand/VALIDATION.md). The original glyph master and approved extension are immutable design sources. All wordmark variants share their vector outlines. JStudios branding assets are separate from the software licenses of individual projects.

## Projects

- [Audio Analyzer](https://github.com/byJStudios/audio-analyzer) — PolyForm Noncommercial 1.0.0
- [CashTracker](https://github.com/byJStudios/cashtracker) — PolyForm Noncommercial 1.0.0
- [KalkulationWebBased](https://github.com/byJStudios/kalkulation-webbased) — PolyForm Noncommercial 1.0.0
- [Lyrics Merge](https://github.com/byJStudios/lyrics-merge) — AGPL-3.0-only
- [Skolary Classic](https://github.com/byJStudios/skolary-classic) — PolyForm Noncommercial 1.0.0
- [Tarifvergleich Physik](https://github.com/byJStudios/tarifvergleich-physik) — PolyForm Noncommercial 1.0.0
- [VidMatch History Importer](https://github.com/byJStudios/vidmatch-history-importer) — PolyForm Noncommercial 1.0.0

Skolary and [LensLink](https://jstudios.pages.dev/projects/lenslink/) are major projects. Skolary is proprietary software in active development, with a restricted browser pilot. See the [product privacy notice](https://jstudios.pages.dev/skolary/datenschutz/) and [terms of use](https://jstudios.pages.dev/skolary/nutzungsbedingungen/). LensLink v0.1.0 is a published Android-to-Windows webcam, licensed Apache-2.0, built on Plugcam, scrcpy, Softcam and Microsoft Windows-Camera Samples. Official downloads: https://github.com/byJStudios/LensLink/releases/tag/v0.1.0. Historical projects have startup checks, not comprehensive production acceptance.

## Contact

jstudios.development@gmail.com. See the website for contact and privacy information; formal legal compliance is not certified.

## Licensing

[Project licensing overview](https://jstudios.pages.dev/lizenzen/). Previously granted license rights remain unaffected. Website content and JStudios branding are not automatically licensed under the software project licenses. See [LICENSE](LICENSE).

## Product principles

JStudios builds practical tools for everyday use and learning. The applicable project licenses define the permitted uses; all other rights remain reserved. Skolary remains proprietary, while data portability is a core product principle: personal school records should remain usable independently of the app and its infrastructure. Open school-record exports (ZIP with HTML, CSV and JSON) and an independent offline reader for compatible encrypted backups have been implemented and automatically tested in v0.8.2 b36, but are not yet approved for production. See the [Skolary product page](https://jstudios.pages.dev/skolary/) for the current status.
