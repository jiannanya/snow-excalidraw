# CLAUDE.md — Snow-Excalidraw

Claude-specific setup and path configuration for using this skill.

---

## Skill Root Path

Set the skill root path at the start of each session:

```
SKILL_ROOT = d:\CC\AI\skills\snow-skill\se\snow-excalidraw
```

Or on macOS/Linux:
```
SKILL_ROOT = /path/to/snow-excalidraw
```

All relative paths in this skill resolve from `SKILL_ROOT`.

---

## Reading the Skill

At the start of a diagram request, Claude should read:

1. `SKILL.md` — overview and quick start
2. `phases/phase-1-intent.md` — to begin intent extraction
3. `catalog/intent-matrix.md` — to select the diagram type

Then read the specific catalog and style files as determined by Phase 1.

**Do not pre-load all files** — read only what Phase 1 determines is needed.

---

## Tool Usage

### File Writing
Use the file writing tool to create `.excalidraw` and `.animseq.json` files. Write complete, valid JSON.

### Script Execution
Run Python scripts via the terminal tool:

```bash
uv run python {SKILL_ROOT}/scripts/validate.py /path/to/diagram.excalidraw
uv run python {SKILL_ROOT}/scripts/open.py /path/to/diagram.excalidraw --mode audit
```

Replace `{SKILL_ROOT}` with the actual path.

### Browser Tool
When `open.py` creates a `launch-audit.html` or `launch-animate.html`, open it in the browser using the browser tool if available:

```
open_browser_page("file:///path/to/launch-audit.html")
```

---

## Working Directory Convention

Always work in a project-specific directory, not the skill root:

**Good:**
```
d:\projects\my-project\diagrams\auth-flow.excalidraw
```

**Bad:**
```
d:\CC\AI\skills\snow-skill\se\snow-excalidraw\auth-flow.excalidraw
```

The skill root contains documentation only, not diagram files.

---

## JSON Output Format

When writing `.excalidraw` files, use compact JSON (no unnecessary whitespace):

```python
json.dumps(data, separators=(',', ':'))
```

Or pretty-printed JSON is also acceptable — Excalidraw loads both.

---

## Error Handling

If `validate.py` reports errors, fix them in the `.excalidraw` file before continuing.

Common patterns:
- **Missing ID reference:** Add the missing element or correct the ID
- **Empty elements array:** The diagram was not composed correctly — regenerate
- **Off-canvas element:** Recalculate coordinates using `schema/layout-grid.md`

---

## Environment Check

To verify the scripts environment is available:

```bash
uv run python --version
```

If `uv` is not installed, scripts can be run with `python` directly if dependencies are available.

---

## Frequently Needed References

| Need | File |
|------|------|
| Diagram type routing | `catalog/intent-matrix.md` |
| JSON element templates | `schema/element-recipes.md` |
| Shape binding patterns | `schema/binding-guide.md` |
| Canvas grid coordinates | `schema/layout-grid.md` |
| Style properties | `styles/<style>.md` |
| Server/infra shapes | `components/servers-and-infra.md` |
| Database shapes | `components/data-stores.md` |
| Flow nodes | `components/flow-primitives.md` |
| Quality gates | `quality/checklist.md` |
| Common mistakes | `quality/anti-patterns.md` |
