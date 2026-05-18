# Diagram Type Catalog — Intent Matrix

Use this table to select the correct diagram type from the user's request. Pick exactly one primary type. Load the matching guide from `./catalog/<type>.md`.

---

## Intent → Type Mapping

| User Says | Diagram Type | Catalog Guide |
|-----------|--------------|---------------|
| architecture, services, infra, microservices, cloud, kubernetes, AWS, GCP | **System Design** | `catalog/system-design.md` |
| data pipeline, ETL, data flow, stream, kafka, batch processing, transformation | **Data Flow** | `catalog/data-flow.md` |
| user journey, checkout, onboarding, sign-up, screen flow, UX flow, navigation | **Product Journey** | `catalog/product-journey.md` |
| mind map, concept map, brainstorm, cluster, topic map, idea network | **Concept Web** | `catalog/concept-web.md` |
| org chart, team structure, reporting, hierarchy, who reports to whom | **Org Structure** | `catalog/org-structure.md` |
| roadmap, timeline, milestones, sequence, schedule, chronology, sprint | **Timeline View** | `catalog/timeline-view.md` |
| comparison, vs, trade-offs, options, pros/cons, before/after, alternatives | **Comparison Frame** | `catalog/comparison-frame.md` |
| webpage, landing page, wireframe, dashboard, UI mockup, layout sketch | **Wireframe Kit** | `catalog/wireframe-kit.md` |
| explain, teach, how it works, story, walkthrough, ELI5, overview | **Narrative Flow** | `catalog/narrative-flow.md` |
| sequence diagram, UML sequence, message flow, API call chain, actor, lifeline | **Sequence Diagram** | `catalog/sequence-diagram.md` |
| ER diagram, entity relationship, database schema, tables, foreign key, ORM model | **ER Diagram** | `catalog/er-diagram.md` |
| kanban, task board, sprint board, work-in-progress, WIP, To Do / In Progress / Done | **Kanban Board** | `catalog/kanban.md` |
| sales funnel, conversion rate, pipeline, MQL SQL, lead stages, AIDA, drop-off | **Sales Funnel** | `catalog/sales-funnel.md` |

---

## Disambiguation Rules

| Conflict | Resolution |
|----------|------------|
| Technical AND educational | System Design first; borrow Narrative Flow teaching simplicity |
| Product flow AND screen design | Product Journey if flow is the deliverable; Wireframe Kit if layout is the deliverable |
| Brainstorming AND structured output | Concept Web for exploration; switch to matching type once structure is clear |
| Comparison AND sequence | Comparison Frame if the purpose is trade-off evaluation; Timeline View if the purpose is ordering |
| Org chart AND data flow | Org Structure if people/teams; System Design if services/systems |

---

## Multi-Topic Requests

If the request covers multiple distinct diagram types:

1. Pick the **single most valuable** type for the user's main question.
2. Produce that one diagram.
3. After delivery, mention: "I also noticed this touches [other topic] — want a separate diagram for that?"

Do not combine two diagram types in one canvas unless they naturally overlap (e.g., system design with embedded comparison).

---

## Style Pre-selection by Type

Each diagram type has a natural default style. Override only when the user signals otherwise.

| Diagram Type | Default Style | Override Trigger |
|---|---|---|
| System Design | `blueprint` | "sketch", "rough", "informal" |
| Data Flow | `blueprint` | "sketch", "presentation" |
| Product Journey | `sketch` | "clean", "presentation" |
| Concept Web | `sketch` | "clean", "structured" |
| Org Structure | `clean` | "sketch", "blueprint" |
| Timeline View | `clean` | "sketch", "rough" |
| Comparison Frame | `clean` | "sketch", "informal" |
| Wireframe Kit | `sketch` | "clean", "high-fidelity" |
| Narrative Flow | `sketch` | "clean", "presentation" |
| Sequence Diagram | `clean` | "sketch", "rough" |
| ER Diagram | `clean` | "blueprint", "sketch" |
| Kanban Board | `clean` | "sketch", "informal" |
| Sales Funnel | `clean` | "sketch", "bold" |

Full style definitions in `./styles/index.md`.
