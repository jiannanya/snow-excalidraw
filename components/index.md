# Component Library Index

Pre-built JSON component recipes for common diagram elements. Load only the component files relevant to the current diagram.

---

## Available Components

| File | What It Contains | Use With |
|------|-----------------|----------|
| `servers-and-infra.md` | Server rack, cloud boundary, Kubernetes pod, load balancer | System Design, Data Flow |
| `interfaces.md` | Browser chrome, mobile screen, desktop window | Product Journey, Wireframe Kit |
| `data-stores.md` | Database cylinder, cache layer, object store, message queue | System Design, Data Flow |
| `actors.md` | Person icon, team group, external org | Product Journey, Org Structure, Narrative Flow |
| `flow-primitives.md` | Labeled arrows, decision diamonds, start/end nodes | All types |
| `callout-kit.md` | Warning badge, success tick, annotation bubble, info label | All types |

---

## Usage Rule

Load only the component files that contain elements needed for the current diagram. Do not load all component files for every diagram.

Components are starting-point templates. Customize `x`, `y`, `id`, and text before using.

---

## Component Coordinate Convention

All component recipes use **local coordinates** relative to an origin of `(0, 0)`. Translate to your target canvas position by adding your desired `(x_offset, y_offset)` to all `x` and `y` values in the component.

Example: to place a browser component at `(520, 200)` on your canvas, add `x_offset=520, y_offset=200` to each element in the component recipe.
