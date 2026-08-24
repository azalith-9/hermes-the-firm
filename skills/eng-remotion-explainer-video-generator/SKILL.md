---
name: eng-remotion-explainer-video-generator
description: Use when building or configuring the Remotion-based pipeline that converts legal explanations, clause summaries, or onboarding content into short animated explainer videos. Covers component structure, data-driven animation patterns, rendering pipeline, and output format considerations for a legal AI product.
license: MIT
metadata: " id: eng.remotion-explainer-video-generator category: eng jurisdictions: [__multi__] priority: P2 intent: [__eng__, remotion, video, explainer, animation] related: [eng-supabase-edge-functions-patterns, eng-streaming-response-rules-mobile, eng-supabase-prerender-blog-pipeline] source: Louis — HAQQ Legal AI (github.com/sboghossian/mini-hermes-the-firm) version: '1.0'"
---

<!--
HERMES PORT NOTE
Mechanically ported into hermes-the-firm from HAQQ Legal AI's mini-claude-for-legal (MIT, the Louis skill library), category 'eng'.
Namespaced as louis-<category>-<skill> on registration.
-->


# Remotion Explainer Video Generator

## What it does

The Remotion explainer video generator turns AI-produced legal summaries and clause explanations into short (30–90 second) animated videos. The primary use case is converting complex legal concepts — "what does this indemnity clause actually mean?" — into accessible visual content for non-lawyer clients. Secondary use cases include onboarding walkthroughs and legal education modules.

Remotion renders React components to MP4/WebM server-side, allowing the output to be driven by structured JSON data produced by the LLM (text, bullet points, jurisdiction flags, highlight phrases).

## Setup / auth

```bash
npm install remotion @remotion/renderer @remotion/bundler
```

For server-side rendering in a Supabase Edge Function environment, use `@remotion/lambda` or run the renderer in a Fly.io/Railway container (Deno/Edge does not support FFmpeg natively).

Environment variables:
- `REMOTION_LAMBDA_FUNCTION_NAME` — if using Lambda renderer
- `REMOTION_AWS_REGION`
- `VIDEO_OUTPUT_BUCKET` — R2 or S3 bucket for rendered MP4 files

## Capabilities

### Data schema — what the LLM should produce

The LLM generates a `VideoScript` JSON object; the Remotion composition consumes it:

```typescript
interface VideoScript {
  title: string;                  // max 60 chars
  jurisdiction?: string;          // "UAE", "KSA", "Lebanon", "DIFC", etc.
  durationSeconds: number;        // 30 | 60 | 90
  scenes: Scene[];
}

interface Scene {
  id: string;
  type: "title" | "bullet_list" | "callout" | "comparison" | "quote";
  durationFrames: number;         // at 30fps: 30s = 900 frames
  content: {
    heading?: string;
    body?: string;
    bullets?: string[];
    leftLabel?: string;           // for comparison scenes
    rightLabel?: string;
    highlightPhrase?: string;     // phrase to animate with emphasis
    quoteText?: string;
    quoteSource?: string;         // "Article 7, DIFC Contract Law"
  };
  language: "ar" | "en" | "fr";
  rtl: boolean;                   // true for Arabic
}
```

### Remotion composition structure

```
src/remotion/
  Root.tsx               — composition registry
  LegalExplainer.tsx     — main composition, maps scenes to components
  scenes/
    TitleScene.tsx
    BulletListScene.tsx
    CalloutScene.tsx
    ComparisonScene.tsx
    QuoteScene.tsx
  shared/
    AnimatedText.tsx     — spring-animated word-by-word reveal
    JurisdictionBadge.tsx
    RTLWrapper.tsx       — wraps scenes in dir="rtl" for Arabic
```

### Arabic / RTL considerations

- Wrap every Arabic scene in a `dir="rtl"` container; Remotion respects CSS direction.
- Use a licensed Arabic font (e.g., IBM Plex Arabic, Noto Sans Arabic) embedded in the composition. System fonts are not available in the Lambda renderer.
- Arabic text should use line-height: 1.8 minimum; Arabic legal text with diacritics needs more vertical space than English.
- For mixed AR/EN scenes, use `unicode-bidi: embed` per text block, not per scene.

### Rendering pipeline

1. LLM generates `VideoScript` JSON (streamed as structured output).
2. Validate JSON against the `VideoScript` schema.
3. Call `renderMedia()` (local) or `renderMediaOnLambda()` with the script as `inputProps`.
4. Upload rendered MP4 to R2 bucket.
5. Return signed URL (24-hour TTL) to client.
6. Store `{ userId, docId, videoUrl, script, createdAt }` in `explainer_videos` table.

## Usage patterns

### Triggering from the chat interface

User asks: "Can you explain this indemnity clause as a short video?"

```typescript
// In the LLM response handler
const script = await generateVideoScript(clauseText, { jurisdiction: "DIFC", lang: "en" });
const videoUrl = await renderAndStore(script, userId);
return { type: "video", url: videoUrl, duration: script.durationSeconds };
```

### Batch generation for onboarding

```typescript
const onboardingTopics = ["what-is-an-nda", "termination-rights-uae", "difc-vs-adgm"];
for (const topic of onboardingTopics) {
  const script = await generateOnboardingScript(topic);
  await renderAndStore(script, "system");
}
```

## Permissions & safety

- Never include PII (party names, amounts, account numbers) in a video script. The video may be shared; the summary should be generic.
- Do not render real client contract text as a quote scene — paraphrase instead.
- Videos are stored per user; R2 object key must include `tenantId/userId/` prefix to prevent enumeration.
- Legal disclaimers: the last scene of every explainer should include a static disclaimer: "This video is for informational purposes only and does not constitute legal advice."
- WCAG: all text must meet 4.5:1 contrast ratio on the background color. Subtitles/captions are required for accessibility.

## Failure modes

| Failure | Impact | Mitigation |
|---|---|---|
| LLM produces invalid VideoScript JSON | Render fails | Validate with Zod schema; fallback to text-only response |
| Arabic font not bundled | Garbled text in rendered video | Bundle fonts at build time; test Arabic scene in CI |
| Render timeout (Lambda 15 min limit) | 90s video not rendered | Cap `durationSeconds` at 90; use async render + polling |
| R2 upload failure | URL never returned | Retry with exponential backoff; return graceful error to user |
| Over-long scene text | Text overflows frame | Truncate at 120 chars per line; wrap at word boundaries |

## Related skills

- [[eng-supabase-edge-functions-patterns]] — deployment pattern for the render-trigger function
- [[eng-streaming-response-rules-mobile]] — mobile display considerations for the returned video URL
- [[eng-supabase-prerender-blog-pipeline]] — similar static asset generation pattern for blog content
