# Phase 1: Intent

**Purpose:** Understand exactly what the user wants before writing any JSON.

---

## 1.1 Trigger Recognition

Phase 1 activates on any message that implies a visual output. Common triggers:

- "draw", "create", "design", "sketch", "diagram", "chart", "map", "visualize", "show me"
- "architecture", "flow", "journey", "system", "pipeline"
- "compare", "timeline", "org chart", "wireframe"

When a trigger is detected, proceed with Phase 1 intent extraction. Do not write diagram JSON yet.

---

## 1.2 Topic Extraction

Extract the following from the user message:

| Slot | What to Find | Example |
|------|-------------|---------|
| **Subject** | What is being diagrammed | "user authentication flow" |
| **Components** | Key entities named by the user | "frontend, API gateway, JWT service, DB" |
| **Relationships** | How components relate | "frontend calls API, API validates with JWT service" |
| **Scale** | How large the diagram is | 3 components = small; 10+ = large; default = medium |
| **Audience** | Who will read it | default = technical; "for stakeholders" = non-technical |

---

## 1.3 Diagram Type Selection

Consult `../catalog/intent-matrix.md` and map the subject to a diagram type:

| If the subject is about... | Select |
|---------------------------|--------|
| Services, APIs, infrastructure | System Design |
| Data transformation, ETL | Data Flow |
| User screens, UX flow | Product Journey |
| Ideas, concepts, terminology | Concept Web |
| Teams, reporting lines | Org Structure |
| Events, milestones, schedule | Timeline View |
| Comparing options | Comparison Frame |
| UI mockup, page layout | Wireframe Kit |
| Story, explanation, teaching | Narrative Flow |

If ambiguous, ask one clarifying question before proceeding.

---

## 1.4 Style Selection

Select default style based on diagram type and any explicit user preference:

| Type | Default Style | Override Triggers |
|------|-------------|------------------|
| System Design | blueprint | "sketch", "whiteboard" |
| Data Flow | blueprint | "simple", "clean" |
| Product Journey | clean | "sketch", "hand-drawn" |
| Concept Web | sketch | "technical", "precise" |
| Org Structure | clean | "sketch" |
| Timeline View | clean | "sketch", "dark" |
| Comparison Frame | clean | "sketch", "dark" |
| Wireframe Kit | clean (monochrome) | "dark" |
| Narrative Flow | sketch | "clean", "dark" |

Explicit style keywords from the user override defaults: "sketch", "blueprint", "clean", "dark".

---

## 1.5 Delivery Mode Selection

Infer the intended delivery mode from the user's message:

| User Signal | Mode |
|-------------|------|
| "edit", "I'll adjust it", "let me tweak" | `audit` |
| "animate", "show step by step", "presentation" | `animate` |
| "save", "keep a copy", "export file" | `save-excalidraw` |
| "image", "PNG", "screenshot", "share" | `save-image` |
| "open", "show me" | `open-image` |
| "animated SVG", "animated export" | `save-animation` |
| No signal | `audit` (default) |

---

## 1.6 Component Inventory

Before composing, list the elements that will appear in the diagram:

```
INTENT SUMMARY
  Type:      System Design
  Style:     blueprint
  Mode:      audit
  Subject:   user login request flow
  Components:
    - Browser (actor)
    - API Gateway (service)
    - Auth Service (service)
    - JWT Validator (service)
    - User DB (database)
  Relationships:
    - Browser → POST /login → API Gateway
    - API Gateway → forward → Auth Service
    - Auth Service → validate → JWT Validator
    - Auth Service → query → User DB
    - Auth Service → 200 OK + token → API Gateway → Browser
```

This summary drives Phase 2 without re-reading the user message.

---

## 1.7 Clarification Protocol

Ask at most **one** clarifying question before proceeding. Acceptable reasons to ask:

1. **Type ambiguity** — two diagram types equally match the request
2. **Missing critical component** — required elements are too vague to name
3. **Conflicting signals** — user says "architecture" but also "user journey"

Do not ask about style, scale, or delivery mode — apply defaults.

If the request is clear enough to compose, **do not ask** — proceed to Phase 2.
