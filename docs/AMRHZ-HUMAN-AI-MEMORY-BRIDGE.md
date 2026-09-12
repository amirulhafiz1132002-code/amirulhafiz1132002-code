# AMRHZ Human–AI Memory Bridge

**Status:** PROPOSED / ARCHITECTURAL CHECKPOINT  
**Scope:** AMRHZ / AP1 Human–AI collaboration architecture  
**Implementation status:** Not implemented by this document

## 1. Purpose

The Human–AI Memory Bridge is a proposed human-readable, inspectable state layer for preserving important project context across humans, AI systems, sessions, applications, and devices.

The goal is not to make an AI smarter. The goal is to reduce loss or silent transformation of human intention when work moves between people, AI systems, or interfaces.

## 2. Core Problem

Conversation history is useful but is not a reliable canonical project state by itself. Important decisions, assumptions, unknowns, failures, evidence, and verified results can become difficult to recover or transfer between systems.

AMRHZ proposes treating explicit project state as a first-class artifact that a human can inspect, edit, version, share, and verify.

## 3. Core Concept

```text
HUMAN INTENTION
      ↓
AI INTERPRETATION
      ↓
STRUCTURED SHARED STATE
      ↓
SYSTEM / AI ACTION
      ↓
REAL EVIDENCE
      ↓
HUMAN VERIFICATION
      ↓
UPDATED REAL STATE
      ↓
NEXT ACTION
```

The shared state should remain understandable to a human without requiring a specific AI provider or hidden runtime memory.

## 4. State Categories

A future implementation may represent at least these categories:

- **INTENTION** — what the human is trying to achieve.
- **INTERPRETATION** — how an AI understands the intention.
- **DECISION** — an accepted human or verified project decision.
- **ASSUMPTION** — something believed but not yet verified.
- **UNKNOWN** — information that is not currently known.
- **EVIDENCE** — observable information supporting a claim or state.
- **FAILURE** — an observed unsuccessful result or rejected interpretation.
- **VERIFIED STATE** — a state supported by actual evidence or explicit human verification.

## 5. Human Authority

AI systems may interpret, question, propose, compare, and challenge project state.

AI systems must not silently replace human intention with an AI assumption.

Important state changes should remain inspectable and, where appropriate, require human verification or approval.

## 6. Portability Goal

The long-term goal is to allow the same project state to move between:

- different AI providers
- different applications
- different sessions
- different devices
- human collaborators
- future AMRHZ/AP1 components

Markdown is currently considered as one possible human-readable transport and inspection format. This experiment does **not** assume that Markdown itself is superior to other formats.

## 7. Architecture Principles

The bridge follows the existing AMRHZ principle:

> **REAL STATE > UI SIMULATION**

Additional principles:

> **HUMAN INTENTION > AI ASSUMPTION**

> **EVIDENCE > CLAIM**

> **VERIFICATION > BLIND TRUST**

> **FAILURE IS DATA**

## 8. Experimental Question

A key research/engineering question is:

> Does a structured, explicit, human-readable project state improve the accuracy, consistency, and completeness with which different AI systems recover human intention, goals, constraints, unknowns, and correct next actions compared with unstructured conversation alone?

## 9. Current Hypothesis

A portable structured project state may reduce misunderstanding and context loss between humans and different AI systems.

The mechanism is currently **UNKNOWN**. Any benefit could come from structure, clarity, explicitness, concision, persistence, or another factor.

No claim is made here that Markdown is inherently better.

## 10. Planned Experiment Direction

A controlled comparison can test equivalent information through different communication layers:

- **A — Conversation only**
- **B — Plain-text structured summary**
- **C — Structured Markdown state**
- **D — Markdown state + conversation**

The same human intention and source information should be held constant where practical. AI outputs can then be evaluated for intent preservation, assumption rate, uncertainty preservation, consistency, and correctness of proposed next actions.

A later cross-AI test can compare whether the same state is interpreted consistently by independent AI systems.

## 11. What Is Not Yet Proven

This checkpoint does **not** establish that:

- Markdown is the best format.
- structured state always improves AI performance.
- different AI systems will converge on the same interpretation.
- the approach solves AI drift.
- the approach constitutes a new scientific discovery.
- the approach is ready for production implementation.

These remain testable questions.

## 12. Current Status

**ARCHITECTURE:** Proposed  
**DOCUMENTATION:** Locked as a checkpoint  
**IMPLEMENTATION:** Pending  
**EXPERIMENT:** Pending  
**EVIDENCE:** Initial intent-recovery test only  
**RESEARCH CLAIM:** Not established

## 13. Development Rule

Follow the AMRHZ development loop:

```text
Understand
   ↓
Build
   ↓
Test
   ↓
Verify
   ↓
PASS
   ↓
Next Task
```

This document records an architectural direction. It does not imply that future capabilities already exist.
