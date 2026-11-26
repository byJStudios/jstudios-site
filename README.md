# JStudios website

Independent software development, Skolary, LensLink and seven open-source projects. Static public-facing site only; no private app source, credentials or user data.

**Preferred address:** https://jstudios.pages.dev/

## Local preview

From the repository root run:

    python -m http.server 8787 --bind 127.0.0.1 --directory site

Open http://127.0.0.1:8787/.

## Deployment

Cloudflare Pages is connected to main with no build command and output directory site/. The existing Cloudflare Workers Static Assets configuration remains available during migration. No paid domain or paid hosting service is required.

## Branding

See [brand kit](brand/README.md) and [validation](brand/VALIDATION.md). The original glyph master and approved extension are immutable design sources. All wordmark variants share their vector outlines. JStudios branding assets are separate from the MIT-licensed application source.

## Projects

- [Audio Analyzer](https://github.com/julianschmitz19-wq/audio-analyzer) — MIT
- [CashTracker](https://github.com/julianschmitz19-wq/cashtracker) — MIT
- [KalkulationWebBased](https://github.com/julianschmitz19-wq/kalkulation-webbased) — MIT
- [Lyrics Merge](https://github.com/julianschmitz19-wq/lyrics-merge) — MIT
- [Skolary Classic](https://github.com/julianschmitz19-wq/skolary-classic) — MIT
- [Tarifvergleich Physik](https://github.com/julianschmitz19-wq/tarifvergleich-physik) — MIT
- [VidMatch History Importer](https://github.com/julianschmitz19-wq/vidmatch-history-importer) — MIT

Skolary is the active flagship project; its source remains private. [LensLink](https://jstudios.pages.dev/projects/lenslink/) is an active Android-to-Windows webcam alpha prototype, built on Plugcam, scrcpy and Microsoft Windows-Camera Samples. No public LensLink download is offered yet. Historical projects have startup checks, not comprehensive production acceptance.

## Contact

jstudios.development@gmail.com. See the website for contact and privacy information; formal legal compliance is not certified.
