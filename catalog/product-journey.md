# Product Journey Diagrams

Use this guide when the goal is to show user navigation, screen flows, UX states, or product interaction sequences.

Default style: `sketch` (see `../styles/sketch.md`)

---

## One Diagram = One Journey

A product journey diagram answers exactly one question:
- What screens does a user visit to complete this task?
- Where do users drop off in this flow?
- What happens when a user takes a wrong turn?
- How does the experience differ between user types?

---

## Canonical Layouts

### Linear Screen Flow (left-to-right)
```
[Entry] → [Screen 1] → [Screen 2] → [Screen 3] → [Success]
```
Use for: checkout, onboarding, sign-up, form completion.

### Decision Branch Flow
```
[Start] → [Gate]
               ↙     ↘
        [Path A]  [Path B]
             ↓         ↓
        [Success] [Dead End / Error]
```
Use for: conditional flows, eligibility gates, role-based navigation.

### State Map
```
[State: Logged Out] ← → [State: Logging In] → [State: Authenticated]
                                                      ↓
                                         [State: Session Expired]
```
Use for: authentication flows, session management, user states.

### Sitemap Sketch
```
[Home]
  ├── [Products]
  │     ├── [Category]
  │     └── [Product Detail]
  ├── [Account]
  └── [Support]
```
Use for: navigation structure, information architecture, sitemap.

---

## Required Elements

1. **Entry point** — where the user begins (home page, notification, deep link)
2. **3–6 primary screens or states** — no more unless the flow demands it
3. **Success outcome** — the end state when the user achieves their goal
4. **At least one branch or error state** — what happens when something goes wrong
5. **Clear labels** — screen names as users would see them (not internal IDs)

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Screen / Page | `rectangle` | Label = page title; use browser frame from `../components/interfaces.md` for key screens |
| User Decision | `diamond` | Yes/No or branching choice |
| Entry Point | `ellipse` | "User opens app", "Click email link" |
| Success State | `ellipse` | Clearly marked endpoint |
| Error / Dead End | `rectangle` + `strokeStyle: "dashed"` | Off the main path |
| Arrow | Directional, labeled with trigger | What causes the transition (e.g., "Submit", "Cancel") |
| Annotation | Free-floating `text` | UX notes, friction points, drop-off metrics |

---

## Screen Content Rule

Do not draw real UI inside screens. Instead:
- Use a labeled `rectangle` for the screen
- Annotate key elements as floating text beside the screen (not inside it)
- Show hierarchy with size (primary screen = larger rectangle)

Exception: Wireframe Kit is the right catalog entry if the user wants actual UI layout detail.

---

## Flow Labeling

Label every arrow with the **trigger** — the action that causes the transition:

| Trigger Type | Example Labels |
|---|---|
| User action | "Click Sign Up", "Submit Form", "Tap Back" |
| System event | "Token expires", "Payment processed", "Error 404" |
| Condition | "If verified", "If cart empty", "On success" |

---

## Anti-Patterns

- Showing more than 8 screens without grouping
- Unlabeled arrows (the reader cannot infer the trigger)
- Missing error or failure branch
- Drawing real UI content inside screen rectangles
- Combining two separate journeys on one canvas without clear separation
