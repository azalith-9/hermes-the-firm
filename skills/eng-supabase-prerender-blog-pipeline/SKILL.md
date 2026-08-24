---
name: eng-supabase-prerender-blog-pipeline
description: Use when building or maintaining the static pre-rendering pipeline that generates SEO-optimized HTML from blog posts and legal insights stored in Supabase. Covers the build trigger, Supabase storage integration, edge-caching strategy, and OG-metadata generation for a legal AI content marketing site.
license: MIT
metadata: " id: eng.supabase-prerender-blog-pipeline category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, supabase, blog, prerender, seo, static-site] related: [eng-supabase-edge-functions-patterns, eng-remotion-explainer-video-generator, eng-supabase-index-knowledge-pipeline] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Supabase Prerender Blog Pipeline

## What it does

The prerender blog pipeline converts blog posts and legal insight articles (stored as rows in Supabase) into pre-rendered static HTML files that are served from Cloudflare (or Supabase Storage with CDN). This matters for SEO: legal AI content ("UAE employment contract template", "DIFC vs ADGM for fintech") has significant organic search value, but client-side-only React apps are not indexed reliably by all crawlers. Pre-rendering solves this without requiring a full SSR infrastructure.

## Setup / auth

Supabase schema:
```sql
CREATE TABLE blog_posts (
  id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
  slug TEXT UNIQUE NOT NULL,
  title TEXT NOT NULL,
  body_md TEXT NOT NULL,           -- Markdown source
  body_html TEXT,                  -- Pre-rendered HTML (populated by pipeline)
  excerpt TEXT,
  cover_image_url TEXT,
  author_id UUID REFERENCES auth.users(id),
  jurisdiction TEXT[],             -- e.g., ["UAE", "DIFC"]
  practice_area TEXT[],
  published BOOLEAN NOT NULL DEFAULT FALSE,
  published_at TIMESTAMPTZ,
  og_title TEXT,
  og_description TEXT,
  og_image_url TEXT,
  created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
  updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);
```

No auth required for public blog reads. The pipeline runs with the service role key (it writes `body_html`).

## Capabilities

### Pipeline trigger

The pipeline runs on:
1. `blog_posts` row insert/update (Postgres webhook → Edge Function `prerender-post`).
2. Nightly cron (rebuild all published posts, catches dependency updates like layout changes).
3. On-demand via `POST /api/admin/prerender` (admin only).

### Rendering steps

1. **Fetch post** — load `slug`, `title`, `body_md`, metadata from Supabase.
2. **Parse Markdown** — use `marked` or `unified` with legal-specific plugins:
   - Auto-link jurisdiction names to relevant resource pages.
   - Highlight `[DISCLAIMER]` blocks with a styled callout component.
   - Convert `[[skill-id]]` wikilinks to actual `/skills/{id}` URLs.
3. **Generate OG metadata** — if `og_title` is null, derive from `title`; if `og_description` is null, use first 160 chars of `excerpt`. OG image: use a template (Vercel OG, Satori, or a Remotion still frame — see [[eng-remotion-explainer-video-generator]]).
4. **Inject into HTML template** — hydrate a minimal HTML shell with `body_html`, head meta tags, and JSON-LD structured data (`LegalArticle` schema type).
5. **Write to storage** — upload rendered HTML to Supabase Storage bucket `blog-html/{slug}/index.html`.
6. **Purge CDN cache** — call Cloudflare Cache Purge API for the slug URL.
7. **Update row** — set `body_html` and `updated_at` in the database.

### JSON-LD structured data (SEO)

```json
{
  "@context": "https://schema.org",
  "@type": "LegalArticle",
  "headline": "{{title}}",
  "author": { "@type": "Organization", "name": "Louis Legal AI" },
  "datePublished": "{{published_at}}",
  "about": [
    { "@type": "Thing", "name": "{{jurisdiction[0]}}" }
  ],
  "description": "{{og_description}}"
}
```

Using `LegalArticle` type (instead of generic `Article`) improves Google's classification of legal content.

### Arabic / RTL blog posts

- Arabic posts set `lang="ar" dir="rtl"` on the `<html>` element.
- The HTML template must include an Arabic web font (IBM Plex Arabic) in the `<head>`. Prerender time is not critical, so full font loading is acceptable.
- Slug for Arabic posts: use the Latin transliteration in the URL (`/ar/aqd-amal-lubnan`), not Arabic Unicode, for URL portability.

### Multilingual routing

| Path | Language |
|---|---|
| `/blog/{slug}` | English (default) |
| `/ar/blog/{slug}` | Arabic |
| `/fr/blog/{slug}` | French |

Each language variant is a separate row in `blog_posts` with a `lang` column and a `translation_of` FK pointing to the canonical English post.

## Usage patterns

### Triggering a single post prerender

```typescript
const res = await supabase.functions.invoke("prerender-post", {
  body: { slug: "uae-employment-law-2024" },
});
```

### Listing posts by jurisdiction for sitemap

```typescript
const { data } = await supabase
  .from("blog_posts")
  .select("slug, updated_at, jurisdiction")
  .eq("published", true)
  .order("published_at", { ascending: false });
```

## Permissions & safety

- The `prerender-post` function runs with service role to write `body_html`. It must not be callable by unauthenticated requests.
- Never render a post with `published = false` to the public-facing storage bucket.
- Markdown-to-HTML pipeline must sanitize HTML (`DOMPurify` or `sanitize-html`) to prevent stored XSS from user-authored content.
- Do not include user-submitted content (comments, intake form data) in pre-rendered HTML — that would be a persistent XSS vector.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| Markdown parse error | `body_html` not updated; old content served | Catch parse errors; set post status to `render_error`; alert |
| Storage upload fails | CDN serves stale content | Retry 3× with backoff; after 3 failures, alert on-call |
| Cloudflare purge fails | Stale HTML cached | CDN max-age should be 1 hour max; purge failure is recoverable |
| OG image missing | Social previews are blank | Always generate a default OG image if `og_image_url` is null |
| Arabic post served without `dir="rtl"` | Broken layout | Validate HTML output includes `dir="rtl"` for Arabic posts before uploading |

## Related skills

- [[eng-supabase-edge-functions-patterns]] — the Edge Function pattern used by `prerender-post`
- [[eng-remotion-explainer-video-generator]] — generates OG/social video cards for high-value posts
- [[eng-supabase-index-knowledge-pipeline]] — similar pipeline for indexing documents (compare patterns)
