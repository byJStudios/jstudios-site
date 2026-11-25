# JStudios website

Official studio website for independent, non-commercial software development and Skolary. Public-facing content only; no application source, credentials or school data.

**Live:** https://jstudios-site.julianschmitz19.workers.dev/

## Local preview

Run `python -m http.server 8787 --bind 127.0.0.1 --directory site` and open http://127.0.0.1:8787/.

## Deployment

Cloudflare Workers with Static Assets, connected to this repository's `main` branch. The deployment command is `npx wrangler deploy`. Static assets are in `site/`. HTTPS is provided by Cloudflare. No paid domain or additional service is required. Keep the private Skolary source repository separate.

## Branding

The approved wordmark glyphs v0.2 are integrated. See [brand kit](brand/README.md) for the source hash, geometry, animation and validation. Preserve the approved outlines.

## Contact and privacy

Contact: jstudios.development@gmail.com. The public contact and technical privacy information is not a legal compliance certification. The owner's private address is not published. Do not publish personal school information, credentials or unpublished release binaries.
