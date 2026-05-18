# Data Flow Diagrams

Use this guide when the goal is to show how data moves, transforms, or branches through a system — pipelines, ETL processes, stream processing, or data lifecycle.

Default style: `blueprint` (see `../styles/blueprint.md`)

---

## One Diagram = One Data Question

A data flow diagram should answer exactly one question:
- Where does data come from, and where does it go?
- What transformations happen to data at each stage?
- What happens when data is invalid or fails validation?
- How does data fan out to multiple consumers?

---

## Canonical Layouts

### Linear Pipeline (left-to-right)
```
[Source] → [Ingest] → [Transform] → [Enrich] → [Sink]
```
Use for: ETL, batch processing, data transformation.

### Fan-Out Pipeline
```
[Source]
   ↓
[Router / Topic]
   ↙   ↓   ↘
[A]  [B]  [C]
```
Use for: pub/sub, stream fanout, multi-consumer pipelines.

### Validation Branch
```
[Input] → [Validate]
               ↓          ↘
           [Process]    [Dead Letter]
               ↓
           [Output]
```
Use for: data quality gates, error handling, schema validation.

### Lambda Architecture
```
[Source]
   ↙         ↘
[Batch]    [Stream]
   ↓           ↓
[Batch View] [Realtime View]
         ↘  ↙
      [Serving Layer]
```
Use for: hybrid batch + streaming systems.

---

## Required Elements

1. **Data source(s)** — where data originates (API, file, DB, event)
2. **Transformation stages** — clearly labeled with the operation (parse, validate, enrich, aggregate)
3. **Data sink(s)** — where data lands (DB, S3, dashboard, API)
4. **Data shape** — include at least one example of the data format (JSON snippet, schema field names)
5. **Error / failure path** — what happens to bad data

---

## Visual Vocabulary

| Element | Shape | Notes |
|---------|-------|-------|
| Data Source | `ellipse` | External origin; leftmost/topmost |
| Transformation Step | `rectangle` | Label = operation name (e.g., "Parse JSON") |
| Validation / Gate | `diamond` | Decision on data validity |
| Data Store | DB component from `../components/data-stores.md` | Target storage |
| Message Queue | `ellipse` or queue component | Async buffer |
| Error / Dead Letter | `rectangle` + `strokeStyle: "dashed"` | Off the main path |
| Data Payload | `rectangle` with monospace text | Evidence artifact; use `fontFamily: 3` |
| Arrow | Labeled with data type or event name | Show direction of movement |

---

## Data Shape Rule

Include at least one labeled data shape — a small `rectangle` showing example fields:

```
{ id: "a1b2", event: "purchase", amount: 49.99 }
```

Place it beside the stage where the data is most relevant.

---

## Pipeline Stages Vocabulary

Use these verb labels for transformation shapes:

| Stage | Preferred Label | Alternatives |
|-------|----------------|--------------|
| Receive raw data | `Ingest` | `Collect`, `Receive` |
| Format conversion | `Parse` | `Deserialize`, `Decode` |
| Data quality check | `Validate` | `Schema Check`, `Lint` |
| Add context | `Enrich` | `Join`, `Augment` |
| Summarize | `Aggregate` | `Reduce`, `Group` |
| Write output | `Sink` | `Persist`, `Publish` |
| Handle errors | `Dead Letter` | `Error Queue`, `Reject` |

---

## Anti-Patterns

- Arrows without data type labels
- No error/failure path shown
- Showing only boxes, no data shape examples
- Combining multiple independent pipelines in one diagram
- Using "process" as a label without saying what processing is done
