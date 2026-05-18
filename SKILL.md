---
name: snow-excalidraw
description: >
  Generate precise, professional Excalidraw diagrams for any domain: system architecture,
  data pipelines, product flows, concept maps, wireframes, timelines, UML sequence diagrams,
  ER diagrams, kanban boards, sales funnels, and more.
  Supports multiple visual styles (sketch, blueprint, clean, dark). Delivers a live
  edit URL by default (via local sites/ viewer); PNG, animated SVG, and saved source on request.
  Uses the `audit` delivery mode by default (opens `sites/audit.html`).
---

Follow the execution pipeline in `./workflow.md`.

Core references (always load):
- `./catalog/intent-matrix.md` — maps user intent to diagram type
- `./styles/index.md` — visual style selection
- `./schema/spec.md` — Excalidraw JSON rules

## Quick Start for Agents

1. Read `./workflow.md` for the full 4-phase pipeline
2. Identify diagram type from `./catalog/intent-matrix.md`
3. Select visual style from `./styles/index.md`
4. Load the matching catalog entry for detailed guidance
5. Compose JSON using `./schema/element-recipes.md`
6. Validate with `./scripts/validate.py`
7. Deliver via `./scripts/open.py`

## Rendering Tools

### Preferred: Chrome DevTools MCP (fast, no Playwright)
```
npm install -g chrome-devtools-mcp
```
Add to Claude settings (`~/.claude/settings.json`):
```json
{
  "mcpServers": {
    "chrome-devtools-mcp": {
      "command": "npx",
      "args": ["chrome-devtools-mcp"]
    }
  }
}
```

### Fallback: Playwright
Used only when Chrome DevTools MCP is unavailable. Slower; requires browser installation.

## Style System Summary

| Style | When to Use | Key Visual Properties |
|-------|-------------|----------------------|
| `sketch` | Default; informal, creative, teaching | roughness=1, Virgil font, monochrome |
| `blueprint` | Technical specs, infra diagrams | roughness=0, monospace, blue tones |
| `clean` | Presentations, product docs | roughness=0, sharp lines, minimal color |
| `dark` | Night-mode, dashboard backgrounds | dark canvas, light strokes |

Full details in `./styles/`.

## Diagram Catalog Summary

| Category | Keywords | Guide |
|----------|----------|-------|
| System Design | architecture, infra, services, microservices | `catalog/system-design.md` |
| Data Flow | pipeline, ETL, data movement, stream | `catalog/data-flow.md` |
| Product Journey | user journey, checkout, onboarding, screen flow | `catalog/product-journey.md` |
| Concept Web | mind map, concept map, cluster, ideas | `catalog/concept-web.md` |
| Org Structure | org chart, team map, reporting lines | `catalog/org-structure.md` |
| Timeline View | roadmap, sequence, chronology, milestones | `catalog/timeline-view.md` |
| Comparison Frame | vs, trade-offs, options, before/after | `catalog/comparison-frame.md` |
| Wireframe Kit | webpage, landing page, UI mockup, dashboard | `catalog/wireframe-kit.md` |
| Narrative Flow | explain, teach, story, how it works | `catalog/narrative-flow.md` |
| Sequence Diagram | UML sequence, API call flow, request/response | `catalog/sequence-diagram.md` |
| ER Diagram | entity relationship, database schema, data model | `catalog/er-diagram.md` |
| Kanban Board | kanban, sprint board, task board, WIP | `catalog/kanban.md` |
| Sales Funnel | funnel, conversion, stages, marketing funnel | `catalog/sales-funnel.md` |

## Viewer Pages (sites/)

Self-contained local HTML pages for viewing and animating diagrams without a remote server:

| Page | Purpose |
|------|---------|
| `sites/index.html` | Skill landing page and navigation |
| `sites/audit.html` | Full Excalidraw editor — loads diagram from URL fragment or local file picker |
| `sites/animate.html` | Step-by-step animation player with play/pause/step controls |

URLs use a `file://` scheme with a gzip+base64 bundle in the fragment:  
`file:///path/to/sites/audit.html#<encoded-bundle>`

Use `scripts/open.py --mode audit` or `--mode animate` to auto-open the correct viewer.

## Visual Guides (guides/)

Additional design reference materials for agents:

| Guide | Purpose |
|-------|---------|
| `guides/arrow-routing.md` | Arrow JSON anatomy, routing patterns, common mistakes |
| `guides/patterns.md` | 10 reusable visual layout patterns with coordinate formulas |
| `guides/prompt-templates.md` | Copy-ready prompt templates for each diagram type |

## Default Behavior

- Write diagram files to system temp directory; never write to user workspace unless asked
- Always surface a hosted edit URL as the primary deliverable
- Offer animation as an opt-in follow-up
- Offer PNG only when user explicitly requests an image
- Default style is `sketch` unless context indicates otherwise
