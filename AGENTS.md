# AGENTS.md — Snow-Excalidraw

Configuration and instructions for AI agents using this skill.

---

## Skill Identity

- **Name:** snow-excalidraw
- **Purpose:** Generate professional Excalidraw diagrams with multiple visual styles, a component library, and a structured 4-phase pipeline
- **Entry point:** `SKILL.md`

---

## Activation

This skill activates when a user asks for:
- A diagram, chart, map, or visual representation
- System architecture, data flow, user journey, or org chart
- Comparison, timeline, wireframe, or concept visualization
- Any output containing shapes, arrows, or canvas elements

---

## Agent Execution Order

When fulfilling a diagram request, follow this pipeline:

```
Phase 1: Intent     → phases/phase-1-intent.md
Phase 2: Compose    → phases/phase-2-compose.md
Phase 3: Verify     → phases/phase-3-verify.md
Phase 4: Deliver    → phases/phase-4-deliver.md
```

Do not skip phases. Do not deliver before Phase 3 (Verify) completes.

---

## Required Reference Files

Before composing any diagram, load these files:

| When | Load |
|------|------|
| Always | `catalog/intent-matrix.md` |
| For the selected diagram type | `catalog/<type>.md` |
| For the selected style | `styles/<style>.md` |
| For element construction | `schema/element-recipes.md`, `schema/binding-guide.md` |
| When using components | `components/<component>.md` |

---

## Validation Rule (Non-Negotiable)

Run `scripts/validate.py` before calling `scripts/open.py`. 

```bash
uv run python scripts/validate.py /path/to/diagram.excalidraw
```

A diagram that fails validation must not be delivered. Fix all errors and re-validate.

---

## File Naming Conventions

| File | Name |
|------|------|
| Main diagram | `diagram.excalidraw` |
| Animation sequence | `diagram.animseq.json` |
| Edit launcher | `launch-edit.html` |
| Animate launcher | `launch-animate.html` |
| Rendered PNG | `diagram.png` |
| Animated SVG | `diagram.animated.svg` |

For multi-diagram projects, use descriptive names: `auth-flow.excalidraw`, `overview.excalidraw`.

---

## Style Defaults by Diagram Type

| Diagram Type | Default Style |
|-------------|--------------|
| System Design | blueprint |
| Data Flow | blueprint |
| Product Journey | clean |
| Concept Web | sketch |
| Org Structure | clean |
| Timeline View | clean |
| Comparison Frame | clean |
| Wireframe Kit | clean |
| Narrative Flow | sketch |

User keywords `"sketch"`, `"blueprint"`, `"clean"`, `"dark"` override defaults.

---

## Delivery Mode Defaults

Default mode when not specified: `edit`

All modes: `edit`, `animate`, `save-excalidraw`, `save-image`, `open-image`, `save-animation`

---

## Quality Gates

A diagram passes quality gates when:
1. `validate.py` exits 0
2. All Phase 1 components are present in the diagram
3. No shapes overlap
4. Every shape has a label
5. Style is consistent across all elements

See `quality/checklist.md` for the full gate definition.

---

## Do Not Do

- Do not deliver a diagram that fails validation
- Do not add elements not mentioned by the user unless they are required connections
- Do not use decorative color (color must be semantic)
- Do not write paragraphs inside shapes
- Do not create elements with `isDeleted: true`
- Do not skip Phase 3 verification

---

## Script Usage

All scripts use `uv run python`:

```bash
uv run python scripts/validate.py diagram.excalidraw
uv run python scripts/open.py diagram.excalidraw --mode edit
uv run python scripts/render.py diagram.excalidraw diagram.png
uv run python scripts/animate.py diagram.excalidraw diagram.animated.svg
```

Scripts do not require a virtualenv — `uv` manages dependencies automatically.
