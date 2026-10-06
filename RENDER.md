# Deploy on Render

The root `render.yaml` is a Render Blueprint for a **Static Site**. The generated HTML is already committed: no Node server, Python server, package installation, environment variables or application build is needed to serve it.

## Blueprint setup

1. Open the Render dashboard and choose **New → Blueprint**.
2. Connect `baltazaradamealvarez-creator/despacho-de-abogado-webpage`.
3. Select branch **`claude/rediseno-gonzalez-armendariz`**, the repository's current default branch.
4. Render reads `render.yaml`. Review the `gonzalez-armendariz` static site and apply the Blueprint.
5. Open the `onrender.com` URL returned by Render. Subsequent commits on this branch trigger deployment.

The Render deployment itself is not created by pushing the repository; these steps connect it to your Render account.

## Manual alternative

Choose **New → Static Site** and use:

| Setting | Value |
|---|---|
| Repository | `baltazaradamealvarez-creator/despacho-de-abogado-webpage` |
| Branch | `claude/rediseno-gonzalez-armendariz` |
| Root directory | Leave blank |
| Build command | `true` |
| Publish directory | `site` |

Leave the start command unset. This is a multipage static site: do **not** add a catch-all rewrite to `/index.html`; it would turn missing pages into copies of the home. Render serves directory `index.html` files at their corresponding routes.

## Routes to check after deployment

- `/` — Spanish home
- `/en/` — English home
- `/lp/contabilidad/`, `/lp/asesoria-fiscal/`, `/lp/auditoria/`
- `/en/lp/accounting/`, `/en/lp/tax-advisory/`, `/en/lp/audit/`

The historical repo landing `/lp/contabilidad-empresas/` redirects to `/lp/contabilidad/` when using the Blueprint.

## Current scope

This delivery implements the home and three advertising landing pages in both languages. The complete copy for interior pages is in `entregables/04-paginas.md`; their HTML templates are not implemented. Some navigation, privacy and service links intentionally target the proposed production URLs at `gonzalezarmendariz.com`. Publish those pages and approved legal documents before a production launch. Canonical, hreflang and social image URLs retain the intended production domain; adding a custom domain to Render and changing DNS are separate steps.

The four-field form prepares a WhatsApp request. The visitor must send the message, and the firm confirms the appointment. There is no form backend or CRM integration. Analytics and advertising tags are inactive. The optional consent UI and remaining legal/operational items are documented in the report and launch checklist.

Only `site/` is published by Render. Reports, raw audit sources, schemas and the archived initial draft remain repository files. The earlier Apache `.htaccess` lives in the archive; Render does not use Apache configuration. The previous speculative sitemap is archived rather than published, and the proposed sitemap in `deployment-templates/` must be filtered to pages that are actually implemented and indexable before production use.

Official references: [Render Static Sites](https://render.com/docs/static-sites) and [Blueprint YAML Reference](https://render.com/docs/blueprint-spec).
