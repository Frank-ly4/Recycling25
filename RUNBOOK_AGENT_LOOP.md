# RUNBOOK: Agent Loop for Closing DD Gaps (ORCH → BUILD → VERIFY)

**Purpose:** Convert `DD_GAP_REGISTER_151225.md` into a closed evidence-backed data room by running a repeatable agent loop:
1) ORCH (Planner) selects the next best tickets
2) BUILD (Implementer) produces artifacts + updates docs
3) VERIFY (QA) confirms closure and flips statuses to CLOSED

**Primary queue:** `DD_GAP_REGISTER_151225.md`  
**Visibility:** `DATA_ROOM_INDEX.md` is the single-page status board  
**Gates:** `GO_NO_GO_LAUNCH_GATE.md` defines what must be true to pitch/launch

---

## 0) Definitions

### Status meanings (must be consistent everywhere)
- **MISSING**: No artifact exists. No evidence folder content.
- **IN_PROGRESS**: Placeholder exists OR partially filled, not yet verifiable.
- **ASSUMPTION_VALIDATE**: Claim exists but needs real-world measurement/pilot or official confirmation.
- **BENCHMARK_EXTERNAL**: Needs external data source citations/screenshots/exports.
- **CLOSED**: Artifact exists, evidence stored, cross-references updated, status flipped.

### Evidence rule (hard requirement)
No item can be **CLOSED** without at least one of:
- Official document / signed PDF / stamped letter / receipt / quote / email thread export
- Screenshot/photo with timestamp/context
- Dataset export (CSV) + source note
- A memo documenting a field visit/call + names/contacts + next steps

Evidence goes into the `evidence/` tree specified by the Data Room Index row.

---

## 1) Operating Principles (non-negotiable)

1. **Single Source of Truth for the queue:** `DD_GAP_REGISTER_151225.md`  
2. **Single-page visibility:** `DATA_ROOM_INDEX.md` must reflect every change (status, link/path, owner, last updated).  
3. **Close in small batches:** ORCH outputs 3–5 tickets max per batch. BUILD executes one ticket at a time.  
4. **No architecture churn:** Do not invent new folder structures unless required by an existing playbook.  
5. **Binary closure:** A ticket is either CLOSED or it remains IN_PROGRESS with a punch-list.  
6. **Always update timestamps:** Every changed row must update `last updated` (date).  
7. **Audit trail:** Keep changes attributable: note who/what created evidence and when (short note in the doc or evidence README).

---

## 2) Roles & Responsibilities

### ORCH (Planner / Orchestrator)
**Goal:** Select the next highest-leverage work that unblocks Gates and reduces risk.

**Inputs (must read):**
- `DD_GAP_REGISTER_151225.md`
- `DATA_ROOM_INDEX.md`
- `GO_NO_GO_LAUNCH_GATE.md`
- `TOP_10_REAL_INPUTS_BLOCKERS.md`

**Outputs (must produce):**
- A batch of **3–5 tickets** using the Ticket Format below
- Clear dependency order (Ticket 1..N)
- Each ticket must include exact file paths and evidence paths

**Constraints:**
- Prioritize Gates in this order unless instructed otherwise:
  1) Gate A (Corporate/ownership hygiene)
  2) Gate B (Team/governance)
  3) Gate C (Regulatory posture)
  4) Gate D/E (Insurance + fleet/facility)
  5) Gate F (Commercial readiness)
  6) Gate G/H (Pilot measurement + market proof)
- Prefer tickets that can be closed with desk work before field work, where possible.

---

### BUILD (Implementer)
**Goal:** Execute one ticket completely: create/update artifacts, add evidence placeholders or real evidence references, and update statuses.

**Required actions per ticket:**
1) Create/Update the artifact(s) exactly as specified (no extra scope)
2) Save/organize evidence in the specified `evidence/...` path
3) Update:
   - `DD_GAP_REGISTER_151225.md` row(s)
   - `DATA_ROOM_INDEX.md` row(s)
   - Any cross-referenced doc(s) listed in the ticket
4) Add/Update a short note in evidence folder if needed: `evidence/<path>/README.md`

**Outputs (must produce):**
- List of changed files (diff summary)
- What evidence was added (filenames/paths)
- Which statuses were changed (before → after)

**Constraints:**
- Do not mark CLOSED unless evidence exists and links resolve
- Do not create new policies/claims without a citation or mark as ASSUMPTION_VALIDATE

---

### VERIFY (QA / Closer)
**Goal:** Confirm the ticket meets “Done when” and enforce closure discipline.

**Required checks per ticket:**
- Artifact exists at the exact path(s)
- Evidence exists in the evidence folder
- Links from `DATA_ROOM_INDEX.md` resolve to artifacts/evidence paths
- `DD_GAP_REGISTER_151225.md` status matches index
- “Last updated” dates were updated
- Any required sign-off fields are populated (if applicable)

**Outputs (must produce):**
- PASS → mark CLOSED everywhere required
- FAIL → produce a punch-list:
  - Missing evidence items
  - Broken links
  - Missing fields
  - Which file/line to fix

**Constraints:**
- No vibes. Only verify against “Done when”.
- If not fully done, do NOT close. Keep IN_PROGRESS and return the punch-list.

---

## 3) Ticket Format (standard)

Use this format verbatim for every ticket.

### TICKET
- **ID:** `T-YYYYMMDD-###`
- **Gate:** A/B/C/D/E/F/G/H
- **Source Gap IDs:** (from DD_GAP_REGISTER)
- **Title:** short, specific

#### Objective
One sentence describing the closed state.

#### Inputs (must read)
- `path/to/doc.md`
- `path/to/template.md` (if any)

#### Outputs (must produce)
- `path/to/new_or_updated_doc.md`
- Evidence folder: `evidence/<path>/`
- Optional: `evidence/<path>/README.md` (if evidence needs narrative)

#### Steps
- [ ] Step 1…
- [ ] Step 2…

#### Done when (binary)
- [ ] Artifact exists and is complete
- [ ] Evidence added in evidence folder (at least 1 item)
- [ ] `DD_GAP_REGISTER_151225.md` row updated (status + last updated + link)
- [ ] `DATA_ROOM_INDEX.md` row updated (status + last updated + link)
- [ ] Any cross-refs updated (list them)

#### Notes / Risks
Only if necessary; max 5 bullets.

---

## 4) Cadence & Batch Rules

### Default batch size
- ORCH: 3–5 tickets per batch
- BUILD: execute **1 ticket** per run
- VERIFY: verify **1 ticket** per run

### Update frequency
- After every ticket: update both `DD_GAP_REGISTER...` and `DATA_ROOM_INDEX...`
- Weekly: run a sweep to ensure no mismatches across status boards

---

## 5) Gate Prioritization Heuristic

When selecting tickets, ORCH uses this scoring:
1. **Gate criticality** (A highest)
2. **Dependency unlock** (unblocks multiple later tickets)
3. **Closeability** (can it be CLOSED within 1–2 sessions?)
4. **Investor sensitivity** (ownership, governance, regulatory, insurance)
5. **Evidence availability** (do we know where to get proof?)

---

## 6) Evidence Standards (quick checklist)

A ticket may be CLOSED only if evidence meets at least one:
- Signed/stamped official doc (PDF/photo)
- Email thread export showing quote/terms/confirmation
- Screenshot + source URL + date captured
- Field memo with contact name/office/steps + photos of visit
- Dataset export + source citation file

**Every evidence folder should contain either:**
- The evidence itself, OR
- `README.md` explaining what’s pending and what was done (if still IN_PROGRESS)

---

## 7) Minimal Prompts (copy/paste)

### ORCH prompt
"Read the 4 canonical docs. Output exactly 5 tickets using the Ticket Format. Prioritize Gates A→C. Include exact paths for outputs and evidence. No extra commentary."

### BUILD prompt
"Execute Ticket 1 only. Implement artifacts, place evidence in the specified folder, update both indexes, and output a diff summary of changed files + evidence added."

### VERIFY prompt
"Verify Ticket 1 against Done when. If PASS, mark CLOSED in both indexes. If FAIL, return a punch-list with exact file(s) to fix."

---

## 8) Stop Conditions

Stop the loop when:
- Gate A + Gate B + Gate C are all CLOSED, OR
- The remaining tickets require real-world inputs (calls/visits/signatures) and are queued as field actions with owners.

---

## 9) Ownership & Accountability

Every row in `DATA_ROOM_INDEX.md` must have:
- Owner (real person/role)
- Status
- Link/path
- Last updated

If Owner is missing, ORCH must create a ticket to assign owners before further work.

---

## 10) Change Control

Do not rewrite core architecture documents unless a ticket explicitly requires it.
When changing a template, note:
- What changed
- Why
- Which downstream docs should be rechecked

Keep it boring. Close the gaps.


Below, example of TICKET_TEMPLATE.md

# TICKET: <ID> — <Short, specific title>

**Gate:** <A/B/C/D/E/F/G/H>  
**Source Gap IDs:** <e.g., CC-01, TF-07>  
**Primary Doc Row:** <link/path to the row or section if available>  
**Owner:** <role/person>  
**Status (start):** <MISSING/IN_PROGRESS/ASSUMPTION_VALIDATE/BENCHMARK_EXTERNAL>  
**Target Status:** <CLOSED or IN_PROGRESS w/ punch-list>  
**Last Updated:** <YYYY-MM-DD>

---

## Objective (1 sentence)
<What “closed” looks like in plain English.>

## Inputs (must read)
- `<path/to/DD_GAP_REGISTER_151225.md>`
- `<path/to/DATA_ROOM_INDEX.md>`
- `<path/to/relevant_doc.md>`
- `<path/to/template.md>` (if any)

## Outputs (must produce)
### Artifacts
- `<path/to/new_or_updated_doc.md>`
- `<path/to/created_file.ext>` (if any)

### Evidence
- Evidence folder: `evidence/<path>/`
- Required evidence type: <signed doc / email export / screenshot+source / dataset export / field memo>

## Scope (in / out)
**In scope:**
- <bullets>
**Out of scope:**
- <bullets>

## Steps (checklist)
- [ ] Step 1: …
- [ ] Step 2: …
- [ ] Step 3: …

## Done when (binary)
- [ ] Artifact(s) exist at specified paths and are complete (no placeholders)
- [ ] Evidence exists in `evidence/<path>/` (at least 1 item) and is readable
- [ ] `DD_GAP_REGISTER_151225.md` updated: status + link/path + owner + last updated
- [ ] `DATA_ROOM_INDEX.md` updated: status + link/path + owner + last updated
- [ ] Cross-references updated (list files): <file1>, <file2>
- [ ] VERIFY passed (or punch-list captured)

## Risks / Notes (max 5 bullets)
- <only if necessary>

---

## VERIFY CHECK (to be completed by QA agent)
**PASS/FAIL:** <PASS or FAIL>

If FAIL, punch-list:
- [ ] Missing…
- [ ] Fix in file: `<path>` (line/section if known)
