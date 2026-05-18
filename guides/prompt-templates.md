# Prompt Templates

Copy-paste prompts for generating specific diagram types. Substitute `{...}` placeholders.

---

## System Design

```
Draw a system design diagram for {system name}.
Components: {list key services, e.g. API Gateway, Auth Service, PostgreSQL, Redis, S3}.
Show data flow: {describe the main request path}.
Style: blueprint.
Canvas: 1800 × 1000 px.
```

**Example:**
```
Draw a system design diagram for a real-time chat application.
Components: WebSocket Gateway, Message Service, User Service, PostgreSQL, Redis pub/sub, S3.
Data flow: client → WebSocket Gateway → Message Service → Redis pub/sub → all connected clients;
messages persisted to PostgreSQL.
Style: blueprint.
```

---

## Sequence Diagram

```
Draw a UML sequence diagram for {interaction name}.
Actors: {list actors, e.g. Browser, API Server, Auth Service, Database}.
Interactions:
  1. {Actor A} sends {message} to {Actor B}
  2. {Actor B} returns {response} to {Actor A}
  ...
Show activation boxes on {Actor B}.
```

**Example:**
```
Draw a UML sequence diagram for user login with JWT.
Actors: Browser, API Server, Auth Service, Redis.
Interactions:
  1. Browser sends POST /login to API Server
  2. API Server sends validate credentials to Auth Service
  3. Auth Service queries Redis for rate limit
  4. Auth Service returns JWT token to API Server
  5. API Server returns 200 + token to Browser
Show activation boxes on API Server and Auth Service.
```

---

## ER Diagram

```
Draw an ER diagram for {system name}.
Tables: {list tables and their key columns, mark PK and FK}.
Relationships:
  {Table A} has many {Table B} via {foreign key column}
  {Table B} belongs to {Table C} via {foreign key column}
```

**Example:**
```
Draw an ER diagram for a blog platform.
Tables:
  users (PK id, email, created_at)
  posts (PK id, FK user_id, title, body, published_at)
  comments (PK id, FK post_id, FK user_id, body)
  tags (PK id, name)
  post_tags (FK post_id, FK tag_id) — junction table
Relationships:
  users has many posts via user_id
  posts has many comments via post_id
  posts has many tags via post_tags junction
```

---

## Kanban Board

```
Draw a Kanban board for {team/project name}.
Columns: {list column names, e.g. Backlog, To Do, In Progress, Review, Done}.
Tasks:
  {Column}: {task 1}, {task 2}, ...
  {Column}: {task 3}, ...
Highlight {task name} in red (blocked / high priority).
```

**Example:**
```
Draw a Kanban board for the frontend team sprint.
Columns: Backlog, To Do, In Progress, Review, Done.
Tasks:
  Backlog: Redesign settings page, Add dark mode toggle
  To Do: Fix login bug, Update API client
  In Progress: Build dashboard charts
  Review: User onboarding flow
  Done: Setup CI/CD, Authentication screens
Highlight "Fix login bug" in red — it is blocked.
```

---

## Sales Funnel

```
Draw a sales funnel for {product/service}.
Stages (top to bottom):
  {Stage 1}: {count or percentage}
  {Stage 2}: {count or percentage}
  ...
Show conversion rates between each stage.
```

**Example:**
```
Draw a sales funnel for a SaaS trial-to-paid conversion.
Stages (top to bottom):
  Website visitors: 50 000 / month
  Sign-up page: 8 000 (16%)
  Trial activated: 3 200 (40%)
  Feature used 3×: 1 100 (34%)
  Paid conversion: 320 (29%)
Show conversion rate between each stage.
```

---

## Data Flow Diagram

```
Draw a data flow diagram for {pipeline name}.
Input sources: {list sources}.
Transformations: {list processing steps in order}.
Output sinks: {list destinations}.
Show the data format at each stage ({e.g. JSON, CSV, Parquet}).
```

---

## Concept Web / Mind Map

```
Draw a concept web for {central topic}.
Core concepts connected to the centre: {list 4–6 nodes}.
Sub-concepts for {node}: {list 2–3 children}.
Style: sketch.
```

---

## Timeline

```
Draw a product roadmap timeline for {product name}.
Period: {start date} to {end date}.
Milestones:
  {Date}: {milestone name} — {brief description}
  ...
Group milestones by quarter.
```

---

## Tips for Better Results

1. **Specify the style** — "sketch", "blueprint", "clean", or "dark" — if you have a preference.
2. **Name your elements** — listing exact service/table/actor names produces better IDs and labels.
3. **State the purpose** — "for a presentation to investors" vs "for internal engineering review" helps choose the right level of detail.
4. **One diagram, one topic** — don't ask for "system design + ER diagram" in one prompt; request them separately.
5. **Animate it** — add "include animation sequence" to get a `.animseq.json` alongside the diagram.
