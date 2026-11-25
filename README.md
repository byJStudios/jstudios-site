# JStudios website

Static, independent studio website. Public-facing content only; no app source, credentials, school data, tracking scripts or runtime dependencies.

## Preview

Run `python -m http.server 8787 --bind 127.0.0.1 --directory site` and open http://127.0.0.1:8787/.

## Cloudflare Pages

Use a separate GitHub repository (recommended name: `jstudios-site`), production branch `main`, framework preset None, build command empty, output directory `site`. Cloudflare receives access to this website repository only. The Pages subdomain is subject to availability. No paid domain is needed.

## Before public deployment

- Replace the temporary typographic JStudios/Skolary treatments with approved supplied logo artwork if desired.
- Confirm public content, operator/contact details and applicable German legal/privacy information, including the actual hosting provider. The current hints page is technical draft content, not a reviewed legal notice.
- Do not include real school data, user accounts, private app source or unpublished release binaries.

No deployment is active until the owner's Cloudflare project is connected.
