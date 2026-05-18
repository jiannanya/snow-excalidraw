---
name: snow-excalidraw-workflow
---

# Snow-Excalidraw Execution Pipeline

`{skill-root}` = installed root folder of this skill.
`{project-root}` = active user project folder.

---

## Four-Phase Pipeline

Every diagram request follows four phases in order. Never skip or reorder them.

```
Phase 1: INTENT    → understand what to draw and select diagram type + style
Phase 2: COMPOSE   → design the layout and write the .excalidraw JSON file
Phase 3: VERIFY    → validate the file and apply the quality checklist
Phase 4: DELIVER   → open, export, or save based on the delivery mode
```

---

## Phase 1 — Intent

> Goal: identify the diagram type, visual style, and delivery mode.

1. Read `./catalog/intent-matrix.md` and select one primary diagram type.
2. Read `./styles/index.md` and select the visual style (default: `sketch`).
3. Infer the delivery mode from the user's request (see Delivery Modes table below).
4. If the topic is factual or technical: research real names, event names, payloads, or steps **before** drawing.
5. Load the matching catalog guide (`./catalog/<type>.md`).

**One diagram = one main question.** If the request spans multiple distinct topics, pick the single most important one. Mention the others as possible follow-up diagrams.

---

## Phase 2 — Compose

> Goal: design the layout and write the `.excalidraw` JSON file.

1. Read `./schema/spec.md` and `./schema/element-recipes.md`.
2. Plan the canvas layout using `./schema/layout-grid.md`.
3. Check `./components/index.md` for pre-built component templates that fit the diagram.
4. Check `./styles/<selected-style>.md` for style-specific color and stroke rules.
5. Design the element arrangement on paper (mentally) before writing JSON.
6. Write the `.excalidraw` file with a **non-empty elements array**.
7. File location: `{temp-dir}/snow-excalidraw/<diagram-name>/diagram.excalidraw`
   - Only write to `{project-root}` if the user specifies a path or explicitly requests it.

**Completeness rule:** The diagram must fully answer the user's question. Use as many elements as required — every element must represent a distinct, necessary concept.

**Text economy:** Each shape label = 1–5 words. No sentences or paragraphs inside boxes. Short bullets only (max 3 per container, each ≤ 5 words).

---

## Phase 3 — Verify

> Goal: validate the file and check visual quality.

```bash
cd {skill-root}/scripts
uv run python validate.py "/absolute/path/to/diagram.excalidraw"
```

If the validator exits with errors: fix every listed error and re-run until clean. Do **not** proceed to Phase 4 until validation passes.

Then apply `./quality/checklist.md` mentally:
- Complete answer to the user's question
- No text overflow or clipped labels
- Arrows route around boxes, not through them
- Layout intentional, not crowded
- No empty placeholder boxes
- No duplicated text

---

## Phase 4 — Deliver

> Goal: open, export, or save the diagram per the delivery mode.

```bash
cd {skill-root}/scripts
uv run python open.py "/absolute/path/to/diagram.excalidraw" --mode <MODE> [--dest {project-root}]
```

### Delivery Modes

| User Request | `--mode` | What Happens |
|---|---|---|
| Default / "show me" / "open" / no explicit format | `audit` | Writes `launch-audit.html` → opens standalone Excalidraw editor |
| "watch it animate" / "open animation" / "show animated" | `animate` | Writes `launch-animate.html` → redirects to hosted animation view |
| "save the diagram" / "keep the source" / "save as excalidraw" | `save-excalidraw` | Copies `.excalidraw` (+ `.animseq.json` if present) to `--dest` |
| "animated SVG" / "save animation" / "video" | `save-animation` | Renders + saves `.animated.svg` to `--dest` (always workspace) |
| "save image" / "export PNG" / "PNG" | `save-image` | Renders + saves `.png` to `--dest` |
| "show image" / "open PNG" / "view PNG" | `open-image` | Renders `.png`, saves to `--dest`, opens with system viewer |

**Render order rule (critical):** For any render mode (`save-animation`, `save-image`, `open-image`):
1. Phase 2 must complete (file written)
2. Phase 3 must pass (validator exits 0)
3. Only then call `open.py` — never before the file exists and validates

### Handoff

Every response must include **one** of:
- A `file://` path to the launcher HTML (audit / animate modes)
- The absolute path to the saved output file (save-* / open-image modes)

A response with no path or link is incomplete.

### Follow-up Offers (deliver after handoff, contextually)

- If mode was `audit` and user hasn't asked for animation:
  > "Want to see it draw itself? I can generate an animated version."
- If source file is still in temp and user hasn't asked to save it:
  > "Want me to save the source file to your project folder?"

---

## Animation Integration

If the user requests animation, write a `.animseq.json` file alongside the `.excalidraw` file **after** Phase 3 passes. Reference format: `./animation/sequence-spec.md`.

Animation pipeline rule: the `.excalidraw` file must exist and validate **before** any animation is authored. Never animate before the diagram is complete.

---

## File Naming Convention

```
diagram.excalidraw          — main diagram source
diagram.animseq.json        — animation sequence (optional)
diagram.animated.svg        — rendered animation output
diagram.png                 — rendered static image
launch-audit.html            — browser launcher for audit mode
launch-animate.html         — browser launcher for animate mode
```

All files for one diagram live in the same folder.
