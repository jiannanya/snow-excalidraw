# Snow-Excalidraw

A professional Excalidraw diagram skill for AI agents, featuring four visual styles, a structured four-phase pipeline, a component library, and thirteen diagram types.

Snow-Excalidraw enables AI agents to produce high-quality, validated Excalidraw diagrams from natural language requests — covering everything from system architecture to UML sequence diagrams to kanban boards.

---

## What It Does

Snow-Excalidraw gives an AI agent:

- **Diagram routing** — automatically maps user requests to the correct diagram type
- **Four visual styles** — sketch, blueprint, clean, and dark, each with defined typography, color, and stroke properties
- **Thirteen diagram types** — covering all common technical and product communication needs
- **A component library** — ready-to-use JSON templates for servers, databases, actors, UI chrome, and flow primitives
- **A 4-phase pipeline** — structured Intent → Compose → Verify → Deliver execution with built-in quality gates
- **Validation** — a Python validator that catches structural errors and text overflow before delivery
- **Self-hosted viewer** — local HTML pages (`sites/`) that render diagrams without any remote server
- **Multiple delivery modes** — edit in browser, export PNG, animate step-by-step, or save files to a project directory

---

## Quick Start

### 1. Install dependencies

```cmd
# Windows
scripts\install.cmd

# macOS / Linux
chmod +x scripts/install.sh && scripts/install.sh
```

See `INSTALL.md` for manual installation steps.

### 2. Reference the skill

In your agent prompt or system message, reference `snow-excalidraw/SKILL.md`.

### 3. Ask for a diagram

- "Draw a system architecture for a login service with API gateway, auth service, and PostgreSQL"
- "Sketch a user journey for the checkout flow"
- "Create a dark-style comparison of REST vs GraphQL vs gRPC"
- "Draw a UML sequence diagram for an OAuth login flow"
- "Show the ER diagram for a blog database"
- "Make a kanban board with To Do, In Progress, Review, and Done columns"

### 4. View the result

The agent writes a `.excalidraw` file and opens it via `scripts/open.py`. By default it opens the local editor at:

```
sites/audit.html#<gzip+base64-bundle>
```

No remote server is needed — the viewer loads Excalidraw from the `esm.sh` CDN.

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

### Sequence Diagram
UML sequence diagrams showing actor interactions over time. Covers synchronous calls, return messages, activation boxes, and Alt/Loop frames. Default style: clean.

### ER Diagram
Entity-relationship diagrams for database schema visualization. Covers table headers, primary key rows, foreign key rows, and relationship arrows with cardinality labels. Default style: clean.

### Kanban Board
Task and sprint boards organized in columns. Covers lane backgrounds, task cards with priority color coding, WIP limit badges, and swimlane dividers. Default style: clean.

### Sales Funnel
Conversion funnel diagrams with stacked stages. Covers decreasing-width rectangles, color progressions, conversion rate annotations, and horizontal variants. Default style: clean.

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
| `edit` | Opens diagram in local `sites/audit.html` viewer (default) |
| `animate` | Opens diagram in local `sites/animate.html` step-by-step player |
| `save-excalidraw` | Copies `.excalidraw` and `.animseq.json` to a destination directory |
| `save-image` | Renders PNG to destination directory via Playwright |
| `open-image` | Renders PNG and opens with system image viewer |
| `save-animation` | Renders animated SVG to destination directory |

The `edit` and `animate` modes construct a `file://` URL pointing to the local `sites/` viewer page, with the diagram bundle encoded in the URL fragment. No server needs to be running for these modes.

---

## Animation

Animations use a `.animseq.json` companion file (placed alongside the `.excalidraw` file with the same stem):

```json
{
  "elements": [
    { "id": "element-id-1", "order": 1 },
    { "id": "element-id-2", "order": 2 },
    { "id": "element-id-3", "order": 3 }
  ],
  "duration": 3000,
  "loop": false
}
```

- `elements`: array of `{ id, order }` — elements not listed are always visible as background
- `duration`: total animation duration in milliseconds
- `loop`: whether to loop the animation

The animation player (`sites/animate.html`) groups elements by `order` number and reveals them one step at a time with play/pause/step controls.

See `animation/sequence-spec.md` for full format and narrative patterns.

---

## Scripts

All scripts run via `uv run python` — no manual virtualenv needed.

### validate.py
Validates a `.excalidraw` file for structural correctness, including text overflow detection.

```bash
uv run python scripts/validate.py /path/to/diagram.excalidraw
```

Checks: non-empty elements, unique IDs, no `isDeleted: true`, broken `containerId` references, broken `boundElements` references, broken arrow bindings, off-canvas elements, stacked elements, text overflow in containers.

Exits 0 on success, non-zero with error list on failure.

### open.py
Opens or exports a diagram in the specified delivery mode.

```bash
uv run python scripts/open.py /path/to/diagram.excalidraw --mode edit
uv run python scripts/open.py /path/to/diagram.excalidraw --mode animate
uv run python scripts/open.py /path/to/diagram.excalidraw --mode save-image --dest /project/dir
```

### render.py
Renders a `.excalidraw` file to PNG using a local HTTP server and Playwright.

```bash
uv run python scripts/render.py /path/to/diagram.excalidraw /path/to/output.png
uv run python scripts/render.py /path/to/diagram.excalidraw /path/to/output.png --timeout 60
```

### animate.py
Generates an animated SVG from a diagram and optional animation sequence.

```bash
uv run python scripts/animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg
uv run python scripts/animate.py /path/to/diagram.excalidraw /path/to/output.animated.svg --animseq /path/to/diagram.animseq.json
```

### scene_bundle.py
Low-level encoding/decoding library used by the scripts above. Not called directly.

```python
from scene_bundle import encode_bundle, decode_bundle, build_local_audit_url
```

### Running tests

```bash
cd scripts
uv run pytest tests/ -v
```

---

## File Structure

```
snow-excalidraw/
├── SKILL.md                    # Entry point for AI agents
├── AGENTS.md                   # Agent configuration
├── workflow.md                 # 4-phase pipeline overview
├── README.md                   # This file
├── INSTALL.md                  # Installation guide
│
├── sites/                      # Self-hosted viewer pages (no server needed)
│   ├── index.html              # Landing page and navigation
│   ├── audit.html              # Full Excalidraw editor
│   └── animate.html            # Step-by-step animation player
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
│   ├── narrative-flow.md
│   ├── sequence-diagram.md     # NEW: UML sequence diagrams
│   ├── er-diagram.md           # NEW: entity-relationship diagrams
│   ├── kanban.md               # NEW: kanban boards
│   └── sales-funnel.md         # NEW: sales/conversion funnels
│
├── guides/                     # Design reference for agents
│   ├── arrow-routing.md        # Arrow JSON anatomy and routing patterns
│   ├── patterns.md             # 10 reusable visual layout patterns
│   └── prompt-templates.md     # Copy-ready prompt templates per diagram type
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
│   ├── layout-grid.md          # 1800×1000 px canvas, 6×8 grid
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
├── scripts/                    # Python utilities
│   ├── pyproject.toml
│   ├── install.cmd             # Windows dependency installer
│   ├── install.sh              # macOS/Linux dependency installer
│   ├── validate.py
│   ├── open.py
│   ├── render.py
│   ├── animate.py
│   ├── scene_bundle.py         # Bundle encode/decode (used by all scripts)
│   ├── local_render_server.py  # Local HTTP server for Playwright rendering
│   └── tests/
│       ├── conftest.py
│       ├── test_scene_bundle.py
│       └── test_validate.py
```

---

## Differences from Other Diagram Skills

| Capability | Snow-Excalidraw | Typical single-style skill |
|------------|----------------|---------------------------|
| Visual styles | 4 (sketch, blueprint, clean, dark) | 1 |
| Diagram types | 13 | 8 or fewer |
| Component library | Yes (6 component files) | None |
| Structural validation | Yes (validate.py + text overflow) | None |
| Delivery modes | 6 | 2–3 |
| Dark mode | Yes | No |
| Animation sequences | `.animseq.json` with per-element order | Basic or none |
| Self-hosted viewer | Yes (`sites/` pages, no server needed) | No |
| Evidence artifacts | Required for technical diagrams | Optional |
| Phase pipeline | 4 phases | 3 steps or fewer |
| Composition rules | Explicit (composition-rules.md) | Implicit |
| Unit tests | Yes (tests/) | No |

---

## License

This skill is part of the snow-skill collection. See `LICENSE` for usage terms.
