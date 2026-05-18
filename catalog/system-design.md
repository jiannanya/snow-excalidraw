# System Design Diagrams

Use this guide when the goal is to show infrastructure, cloud architecture, microservices, or service-to-service interactions.

Default style: `blueprint` (see `../styles/blueprint.md`)

---

## One Diagram = One Architectural Question

A system design diagram should answer exactly one question:
- How does the system handle a specific request type?
- Which services communicate, and how?
- Where does data enter, transform, and exit?
- What happens during a failure or failover?

Do not draw "the whole system." Draw one slice.

---

## Canonical Layouts

### Request Path (left-to-right)
```
[Client] → [Gateway/LB] → [Service A] → [Service B] → [Data Store]
```
Use for: API request flows, microservice call chains, gateway routing.

### Event-Driven (top-to-bottom)
```
[Producer]
    ↓
[Message Broker]
    ↓
[Consumer A]  [Consumer B]
    ↓
[Storage]
```
Use for: event sourcing, queue-based processing, pub/sub systems.

### Multi-Zone (spatial)
```
┌── Zone A ──────────┐   ┌── Zone B ──────────┐
│  [Service]         │   │  [Service replica]  │
│  [Cache]           │   │  [Cache replica]    │
└────────────────────┘   └────────────────────┘
         ↕  [Sync/Replication]
```
Use for: high availability, multi-region, disaster recovery.

### Layered Stack (top-to-bottom)
```
[Presentation Layer]
[API / BFF Layer]
[Business Logic Layer]
[Data Access Layer]
[Database / Storage]
```
Use for: layered architecture explanations, clean architecture.

---

## Required Elements

Every system design diagram must include:

1. **One entry point** — client, browser, mobile app, external trigger
2. **One or more services** — the core components of the architecture
3. **At least one data boundary** — database, cache, object store, message queue
4. **Labeled arrows** with protocol or event names (HTTP, gRPC, Kafka, SQL, etc.)
5. **One failure path or edge case** if the diagram is showing a flow

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Client / Browser | `ellipse` or browser component from `../components/interfaces.md` | Entry point; leftmost or topmost |
| Service / Microservice | `rectangle` | Core processing; label = service name |
| Database / Storage | Use DB component from `../components/data-stores.md` | Cylinder or rectangle with "DB" annotation |
| Cache | `rectangle` + dashed border | Use `strokeStyle: "dashed"` |
| Message Queue / Broker | `ellipse` or queue component | Represents async boundary |
| Load Balancer | `diamond` or labeled rectangle | Routing decision node |
| External System | `ellipse` + `strokeStyle: "dashed"` | Third-party, not owned |
| Zone / Region / Cluster | `frame` | Use for logical grouping of co-located services |
| Arrow | Labeled with protocol or method | `endArrowhead: "arrow"` |
| Failure Path | `arrow` + `strokeStyle: "dashed"` | Mark with label "fallback" or "on error" |

---

## Evidence Artifacts

For technical diagrams, include 1–2 evidence artifacts showing real data:
- A JSON payload example (in a `rectangle` with monospace text)
- A real event name, topic name, or method signature
- An HTTP status code or error type

Place evidence artifacts to the **side of the main flow**, not inline.

---

## Anti-Patterns

- Grid of identical rectangles with no visual hierarchy
- Arrows with no protocol labels
- More than 8 services on one canvas without zone grouping
- Bidirectional arrows without explanation
- Showing the entire system instead of one architectural slice
- No entry point visible

---

## Example Minimum Complete Diagram

```
[Browser] → [API Gateway] → [Auth Service] → [User Service] → [PostgreSQL]
                    ↓
              [Rate Limiter] (on quota exceeded)
```

With labels on arrows:
- Browser → API Gateway: `HTTPS POST /login`
- API Gateway → Auth Service: `gRPC ValidateToken`
- Auth Service → User Service: `HTTP GET /user/{id}`
- User Service → PostgreSQL: `SQL SELECT`
- API Gateway → Rate Limiter: `on 429`
