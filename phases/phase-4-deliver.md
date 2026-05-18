# Phase 4: Deliver

**Purpose:** Open the diagram in the correct mode and hand off to the user.

---

## 4.1 Delivery Mode Dispatch

Use the mode determined in Phase 1. Call `open.py` with the appropriate `--mode` flag:

```bash
uv run python open.py "/absolute/path/to/diagram.excalidraw" --mode <mode>
```

| Mode | Script Call | Result |
|------|------------|--------|
| `edit` | `--mode edit` | Writes `launch-edit.html`, opens browser at Excalidraw editor |
| `animate` | `--mode animate` | Writes `launch-animate.html`, opens browser at excalidraw-animate |
| `save-excalidraw` | `--mode save-excalidraw --dest /project/dir` | Copies `.excalidraw` (and `.animseq.json`) to destination |
| `save-image` | `--mode save-image --dest /project/dir` | Renders PNG to destination |
| `open-image` | `--mode open-image --dest /project/dir` | Renders PNG and opens with system viewer |
| `save-animation` | `--mode save-animation --dest /project/dir` | Renders animated SVG to destination |

---

## 4.2 Default Mode Behavior

When no explicit mode was identified in Phase 1, use `edit`:

```bash
uv run python open.py "/absolute/path/to/diagram.excalidraw" --mode edit
```

This opens the diagram in Excalidraw where the user can make live edits.

---

## 4.3 File Paths to Confirm

Before calling `open.py`, verify these files exist:

- `diagram.excalidraw` — the diagram file (mandatory)
- `diagram.animseq.json` — animation sequence (optional; required for animate modes)

If `diagram.excalidraw` does not exist at the expected path, write it first.

---

## 4.4 Handoff Response

After calling `open.py`, provide a brief handoff response to the user:

**For edit mode:**
```
Diagram opened in Excalidraw editor:
  File: /path/to/diagram.excalidraw
  Launcher: /path/to/launch-edit.html
  Elements: N

[Brief description of what the diagram shows]
```

**For animate mode:**
```
Animated diagram opened:
  File: /path/to/diagram.excalidraw
  Sequence: /path/to/diagram.animseq.json
  Launcher: /path/to/launch-animate.html
  Steps: N (estimated duration: Xs)

[Brief description of the animation narrative]
```

**For save modes:**
```
Diagram saved to:
  [list of saved files with paths]
```

---

## 4.5 Offering Follow-ups

End the handoff with at most two follow-up offers. Choose the most relevant:

- "Add animation sequence?" (if mode was `edit` and diagram has multiple stages)
- "Export as PNG?" (if mode was `edit` and diagram is finished)
- "Add a detail view for [sub-system]?" (if diagram shows a complex sub-system)
- "Switch to dark style?" (if diagram is for a dark-mode presentation)

Do not list all follow-ups — pick the two most relevant.

---

## 4.6 Cleanup

After successful delivery:

- Do not delete `diagram.excalidraw` or `.animseq.json`
- Do not delete launcher HTML files (they serve as cached URLs)
- If the script created a temporary file (`*.py` in temp dir), it self-deletes

---

## 4.7 Failure Recovery

If `open.py` fails or the browser does not open:

1. Print the edit URL directly in the response:
   ```
   Open this URL in your browser:
   https://excalidraw.com/#json=<encoded-scene>
   ```
2. Or copy the launcher HTML path and instruct the user to open it manually
3. If even URL encoding fails, offer to paste the raw JSON for manual import

---

## 4.8 Multi-Diagram Projects

When the user requests a project with multiple related diagrams:

1. Create a project directory: `/path/to/project/`
2. Name files descriptively: `overview.excalidraw`, `auth-flow.excalidraw`, `data-pipeline.excalidraw`
3. Deliver each diagram sequentially (Phase 1→4 per diagram)
4. Offer an index in the handoff response:
   ```
   Project diagrams:
     1. overview.excalidraw — system overview
     2. auth-flow.excalidraw — authentication request path
     3. data-pipeline.excalidraw — ETL pipeline detail
   ```
