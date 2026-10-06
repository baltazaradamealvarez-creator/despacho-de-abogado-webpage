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

## Complete multipage website

All 76 routes are committed as static HTML, including the service overview and five detail pages, about, team, contact, insights, guides, publication archive, legal information, careers and advertising landings, in Spanish and English. `site/route-manifest.json` lists each route and its reciprocal language link. Navigation uses local URLs so visitors stay on the Render deployment. A custom `404.html` handles missing pages.

The Blueprint redirects `/blog/`, `/en/blog-2/`, `/en/about-us/` and the original 18 article URLs to their redesigned equivalents. Do not add a catch-all rewrite. `sitemap.xml` includes the implemented indexable pages; advertising landings, historic articles and provisional legal information are excluded. Canonical, hreflang and social images target the intended production domain, `https://gonzalezarmendariz.com`. DNS and a custom domain remain separate from Git deployment.

The four-field form prepares a WhatsApp request. Visitors must send the message, and the firm confirms the appointment. No form backend or CRM is configured. Analytics and advertising tags remain inactive. Privacy information explains the current data flow; the approved full notice and controller details still require the firm’s confirmation.

Only `site/` is published. To regenerate locally, install `requirements-build.txt` and run `python3 build_site.py`. Generated HTML is committed, so the Render build command stays `true`. CSS and JavaScript updates also deploy from commits.

Official references: [Render Static Sites](https://render.com/docs/static-sites) and [Blueprint YAML Reference](https://render.com/docs/blueprint-spec).
