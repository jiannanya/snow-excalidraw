# Snow-Excalidraw

A professional Excalidraw diagram skill for AI agents, featuring four visual styles, a structured four-phase pipeline, a component library, and nine diagram types.

Snow-Excalidraw enables AI agents to produce high-quality, validated Excalidraw diagrams from natural language requests — covering everything from system architecture to product wireframes to narrative explanations.

---

## What It Does

Snow-Excalidraw gives an AI agent:

- **Diagram routing** — automatically maps user requests to the correct diagram type
- **Four visual styles** — sketch, blueprint, clean, and dark, each with defined typography, color, and stroke properties
- **Nine diagram types** — covering all common technical and product communication needs
- **A component library** — ready-to-use JSON templates for servers, databases, actors, UI chrome, and flow primitives
- **A 4-phase pipeline** — structured Intent → Compose → Verify → Deliver execution with built-in quality gates
- **Validation** — a Python validator that catches structural errors before delivery
- **Multiple delivery modes** — edit in Excalidraw, export PNG, open animated view, or save files to a project directory

---

## Quick Start

1. Place the `snow-excalidraw` folder in your AI skill directory
2. In your agent prompt or system message, reference `snow-excalidraw/SKILL.md`
3. Ask for a diagram:
   - "Draw a system architecture for a login service with API gateway, auth service, and PostgreSQL"
   - "Sketch a user journey for the checkout flow"
   - "Create a dark-style comparison of REST vs GraphQL vs gRPC"
4. The agent follows the 4-phase pipeline, writes the `.excalidraw` file, and opens it in your browser

---

## Visual Styles

### Sketch

Hand-drawn appearance. Roughness 1, Virgil font, dark strokes on white canvas. Best for brainstorming, concept webs, and narrative diagrams.

### Blueprint

Technical precision. Roughness 0, Cascadia Code font, blue stroke palette on white canvas. Best for system design, architecture, and data flow diagrams.

### Clean

Presentation-ready. Roughness 0, Helvetica font, dark strokes with minimal color. Best for org charts, timelines, comparisons, wireframes, and product journeys.

### Dark

Dark-mode presentation. Roughness 0, Helvetica font, light strokes on `#1a1b1e` canvas with a single cyan accent. Best for presentations and screen-based delivery.

**Style selection is automatic** based on diagram type. Override with keywords: "sketch", "blueprint", "clean", "dark".

---

## Diagram Types

### System Design
Server and service architecture diagrams. Covers request paths, event-driven systems, multi-zone deployments, and layered stacks. Default style: blueprint.

### Data Flow
ETL, pipeline, and data transformation diagrams. Covers linear pipelines, fan-out patterns, validation branches, and lambda architectures. Default style: blueprint.

### Product Journey
User experience and screen flow diagrams. Covers linear screen flows, decision branches, state maps, and sitemaps. Default style: clean.

### Concept Web
Idea relationships and knowledge maps. Covers radial, network, cluster, and hierarchical layouts. Default style: sketch.

### Org Structure
Team reporting structures and responsibility maps. Covers top-down hierarchy, flat teams, and matrix structures. Default style: clean.

### Timeline View
Event and milestone sequences. Covers horizontal timelines, vertical timelines, swimlane timelines, and Gantt-style charts. Default style: clean.

### Comparison Frame
Side-by-side option comparisons. Covers two-column comparisons, before/after frames, multi-column matrices, and spectrum scales. Default style: clean.

### Wireframe Kit
Low-fidelity UI mockups. Covers landing pages, dashboards, mobile screens, and form layouts. Default style: clean.

### Narrative Flow
Story and explanation diagrams. Covers linear stories, hero + context frames, cause-effect chains, and comparative narratives. Default style: sketch.

---

## Component Library

Ready-to-copy JSON templates for common diagram elements.

### Servers and Infrastructure (`components/servers-and-infra.md`)
- Server / service node (rectangle + bound label)
- Cloud zone (frame with dashed border)
- Load balancer (diamond shape)
- Kubernetes pod group (overlapping rectangles)
- External system (dashed ellipse)

### Interfaces (`components/interfaces.md`)
- Browser chrome (outer rect + URL bar + dot)
- Mobile screen (outer rect + status bar + notch)
- Desktop window (outer rect + title bar)

### Data Stores (`components/data-stores.md`)
- Database / cylinder (body rect + top ellipse)
- Cache (dashed rectangle)
- Message queue (elongated ellipse)
- Object store / bucket (body + lid)

### Actors (`components/actors.md`)
- Person (head ellipse + body rect)
- Team group (frame + 3 dot ellipses)
- External organization (dashed rectangle)

### Flow Primitives (`components/flow-primitives.md`)
- Start node (ellipse)
- End / sink node (ellipse with thick border)
- Process step (rectangle)
- Decision diamond
- Labeled connector (arrow)
- Feedback / loop arrow
- Swimlane divider
- Path annotation

### Callout Kit (`components/callout-kit.md`)
- Warning badge (diamond + "!")
- Success tick (ellipse + "✓")
- Annotation bubble (rect + text)
- Error marker (ellipse + "×")

---

## Four-Phase Pipeline

Every diagram request follows this pipeline:

### Phase 1: Intent
Extract diagram type, style, delivery mode, and component inventory from the user request. See `phases/phase-1-intent.md`.

### Phase 2: Compose
Select a layout template from the catalog, assign components to grid positions, construct all elements in order (frames → shapes → text → arrows → annotations), and write the `.excalidraw` file. See `phases/phase-2-compose.md`.

### Phase 3: Verify
Run `scripts/validate.py`, check layout spacing, verify typography, confirm all intent components are present, and check style consistency. No delivery until all checks pass. See `phases/phase-3-verify.md`.

### Phase 4: Deliver
Call `scripts/open.py` with the correct delivery mode, provide a handoff summary, and offer two relevant follow-up options. See `phases/phase-4-deliver.md`.

---

## Delivery Modes

| Mode | What Happens |
|------|-------------|
| `edit` | Opens diagram in Excalidraw editor (default) |
| `animate` | Opens diagram in excalidraw-animate for step-by-step reveal |
| `save-excalidraw` | Copies `.excalidraw` and `.animseq.json` to a destination directory |
| `save-image` | Renders PNG to destination directory |
| `open-image` | Renders PNG and opens with system image viewer |
| `save-animation` | Renders animated SVG to destination directory |

---

## Animation

Animations use a `.animseq.json` companion file (placed alongside the `.excalidraw` file with the same stem):

```json
{
  "order": ["element-id-1", "element-id-2", "element-id-3"],
  "duration": 3000,
  "loop": false
}
```

- `order`: array of element IDs in reveal sequence
- `duration`: total animation duration in milliseconds
- `loop`: whether to loop the animation

See `animation/sequence-spec.md` for full format and narrative patterns.

---

## Scripts

All scripts run via `uv run python` — no manual virtualenv needed.

### validate.py
Validates a `.excalidraw` file for structural correctness.

```bash
uv run python scripts/validate.py /path/to/diagram.excalidraw
```

Checks: non-empty elements, unique IDs, no `isDeleted: true`, broken `containerId` references, broken `boundElements` references, broken arrow bindings, off-canvas elements, stacked elements.

Exits 0 on success, non-zero with error list on failure.

### open.py
Opens or exports a diagram in the specified delivery mode.

```bash
uv run python scripts/open.py /path/to/diagram.excalidraw --mode edit
uv run python scripts/open.py /path/to/diagram.excalidraw --mode save-image --dest /project/dir
```

### render.py
Renders a `.excalidraw` file to PNG using Playwright.

```bash
uv run python scripts/render.py /path/to/diagram.excalidraw /path/to/output.png
```

### animate.py
Generates an animated SVG from a diagram and optional animation sequence.

```bash
uv run python scripts/animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg
uv run python scripts/animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg --animseq /path/to/diagram.animseq.json
```

---

## File Structure

```
snow-excalidraw/
├── SKILL.md                    # Entry point for AI agents
├── workflow.md                 # 4-phase pipeline overview
├── AGENTS.md                   # Agent configuration
├── CLAUDE.md                   # Claude-specific setup
├── README.md                   # This file
│
├── phases/                     # Phase-specific execution guides
│   ├── phase-1-intent.md
│   ├── phase-2-compose.md
│   ├── phase-3-verify.md
│   └── phase-4-deliver.md
│
├── catalog/                    # Diagram type definitions
│   ├── index.md
│   ├── intent-matrix.md        # Routing table: intent → type
│   ├── system-design.md
│   ├── data-flow.md
│   ├── product-journey.md
│   ├── concept-web.md
│   ├── org-structure.md
│   ├── timeline-view.md
│   ├── comparison-frame.md
│   ├── wireframe-kit.md
│   └── narrative-flow.md
│
├── styles/                     # Visual style definitions
│   ├── index.md
│   ├── sketch.md
│   ├── blueprint.md
│   ├── clean.md
│   ├── dark.md
│   └── semantic-colors.md
│
├── schema/                     # Excalidraw JSON schema reference
│   ├── spec.md
│   ├── element-recipes.md
│   ├── layout-grid.md
│   └── binding-guide.md
│
├── components/                 # Reusable element templates
│   ├── index.md
│   ├── servers-and-infra.md
│   ├── interfaces.md
│   ├── data-stores.md
│   ├── actors.md
│   ├── flow-primitives.md
│   └── callout-kit.md
│
├── animation/                  # Animation system
│   └── sequence-spec.md
│
├── quality/                    # Quality assurance
│   ├── checklist.md
│   ├── anti-patterns.md
│   └── composition-rules.md
│
└── scripts/                    # Python utilities
    ├── pyproject.toml
    ├── validate.py
    ├── open.py
    ├── render.py
    └── animate.py
```

---

## Differences from Other Diagram Skills

| Capability | Snow-Excalidraw | Typical single-style skill |
|------------|----------------|---------------------------|
| Visual styles | 4 (sketch, blueprint, clean, dark) | 1 |
| Diagram types | 9 | 8 or fewer |
| Component library | Yes (6 component files) | None |
| Structural validation | Yes (validate.py) | None |
| Delivery modes | 6 | 2–3 |
| Dark mode | Yes | No |
| Animation sequences | .animseq.json with order + duration | Basic or none |
| Evidence artifacts | Required for technical diagrams | Optional |
| Phase pipeline | 4 phases | 3 steps or fewer |
| Composition rules | Explicit (composition-rules.md) | Implicit |

---

## License

This skill is part of the snow-skill collection. See `LICENSE` for usage terms.
