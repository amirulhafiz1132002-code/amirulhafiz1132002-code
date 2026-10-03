# AMRHZ Current Engineering State

**Recorded:** 2026-10-04

## 1. Current phase

AMRHZ/AP1 is currently in **VERIFY** after P0 test-infrastructure remediation.

Locked workflow:

**STABILIZE → VERIFY → CONNECT → EXTEND**

Per-task workflow:

**INSPECT → MINIMAL SAFE CHANGE → TEST → PASS → CHECKPOINT**

## 2. AP1-WEB-Console P0 checkpoint

- P0 verification: **29/29 PASS**
- Deprecation warnings: **3 observed**
- Remediation checkpoint: **97905d5**
- Commit message: `test: remediate P0 test infrastructure`
- Working tree at checkpoint: **CLEAN**
- Application logic was not changed by the P0 remediation.

The remediation boundary covered verification infrastructure including CORS middleware testing, Motor `find()` mocking, database fixture rebinding, slow-test collection behavior, and CI path handling.

## 3. Verification boundary

The P0 result is a verification checkpoint, not a declaration that the whole system is complete.

Before EXTEND:

1. Inspect the broader test suite.
2. Inspect CI workflow-run metadata and actual job creation/results.
3. Preserve failures as evidence before introducing unrelated fixes.
4. Verify the foundation before connecting or extending capabilities.

## 4. AMRHZ evidence model

Core rules:

- **REAL STATE > UI SIMULATION**
- **EVIDENCE > CLAIM**
- **HUMAN INTENTION > AI ASSUMPTION**
- **VERIFICATION > BLIND TRUST**
- **FAILURE IS DATA**
- **ONE TASK → ONE TEST → PASS → NEXT**

Development maturity states:

**CONCEPT → PROPOSED → PLANNED → DEVELOPMENT → PARTIAL → VERIFIED → LIVE**

Additional states: **BLOCKED, DEPRECATED, UNKNOWN**.

Evidence overrides UI labels. A UI status is not proof of runtime capability.

## 5. AP1 architecture boundaries

### GitHub

GitHub is the source of truth for code, architecture, documentation, decisions, and development history.

### PostgreSQL

PostgreSQL is the runtime-state boundary for approvals, jobs, runtime status, telemetry, and execution records.

Memory/RAG is not treated as the authoritative source of project history.

### AP1 Hub

Operating flow:

**Inspect → Propose → Approve / Cancel**

Read-only inspection is preferred by default. Execution requires an explicit human approval boundary.

Evolution path:

**Health → Diagnostics → Missions → Agent Execution → Evaluation → Learning**

## 6. Human–AI Memory Bridge

Current maturity: **PROPOSED / LOCKED FOR DEVELOPMENT**.

```text
HUMAN INTENTION
      ↓
AI INTERPRETATION
      ↓
STRUCTURED SHARED STATE
      ↓
PROPOSED ACTION
      ↓
HUMAN APPROVAL
      ↓
SYSTEM / AI ACTION
      ↓
REAL EVIDENCE
      ↓
HUMAN VERIFICATION
      ↓
UPDATED REAL STATE
```

## 7. Current ecosystem state

| Area | State | Interpretation |
|---|---|---|
| AP1-WEB-Console | VERIFY | P0 29/29 PASS; broader suite/CI still requires inspection |
| Human–AI Memory Bridge | PROPOSED | Architecture documented; implementation separate |
| Neural visual layer | DEVELOPMENT / PARTIAL | UI representation does not prove runtime state |
| Multi-agent orchestration | DEVELOPMENT | Expansion does not imply verified autonomy |
| Enhanced memory/retrieval | PLANNED | Not represented as completed capability |
| Autonomous workflows | PLANNED | Requires explicit approval and verification |

## 8. Source-of-truth rule

When documentation, UI, or memory conflicts with direct repository/runtime evidence, the direct evidence wins.

**Evidence first. Human intent first. Real state first.**