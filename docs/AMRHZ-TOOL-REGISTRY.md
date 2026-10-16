# AMRHZ Tool Registry

**Written by:** Muhammad Amirul Hafiz bin Md Khalil Miah  
**AI writing and structuring assistance:** ChatGPT (OpenAI)  
**Owner:** AMRHZ  
**Last reviewed:** 2026-10-17  
**Registry state:** PARTIAL — reconstructed from available project context and repository evidence; not a complete machine audit of every repository.

## Purpose

This registry tracks tools and technologies associated with AMRHZ projects without treating every mention, dependency, or planned integration as proof of active use.

**Operating rule:** REAL STATE > UI SIMULATION · EVIDENCE > CLAIM · VERIFICATION > BLIND TRUST.

## Status definitions

- **USED** — use is evidenced by project work or a concrete interaction.
- **CONFIGURED / OBSERVED** — present in code, workflow, dependency files, or project documentation; active runtime use may still be unverified.
- **TESTED** — a specific test or experiment was reported or recorded; this does not imply production readiness.
- **PLANNED / DISCUSSED** — considered or proposed, without verified implementation evidence.
- **UNKNOWN** — available evidence is insufficient to classify current use.
- **BLOCKED** — an identified issue currently prevents the intended use.

Statuses apply only to the stated scope. They are not endorsements or claims that a tool is currently connected, deployed, or working.

## 1. Source control and collaboration

| Tool | Status | Known role / evidence boundary |
|---|---|---|
| GitHub | USED | Source repositories, commits, branches, issues, pull requests, workflow runs, and documentation. A repository link alone does not prove runtime behavior. |
| Git | USED | Local/remote synchronization, branches, commits, fetches, merges, and history verification in Termux. |
| GitHub Actions | USED | CI workflow runs and logs have been inspected for the profile repository. Each workflow's current state must be checked by run ID and commit SHA. |
| GitHub Code Scanning / SARIF upload | CONFIGURED / OBSERVED | ESLint workflow uses SARIF reporting and an upload step. Past failures included a missing SARIF file; do not assume every run succeeds. |

## 2. AI assistants and app-building platforms

| Tool | Status | Known role / evidence boundary |
|---|---|---|
| ChatGPT | USED | Planning, reasoning, documentation, prompt design, code/workflow analysis, and evidence reconciliation. This registry does not imply OpenAI endorsement of AMRHZ projects. |
| Claude | USED | Reviewer output and implementation/verification prompts have been discussed in the project workflow. No persistent connection is implied. |
| Grok | USED — REVIEW ROLE | Assigned by the project owner as an adversarial external reviewer to challenge conclusions and identify economical tests. No automated integration is implied. |
| Lovable | USED | Used as an AI app-building/workspace platform in the AP1 ecosystem. Current deployment and synchronization state require separate verification. |
| Hugging Face | USED — REPOSITORY REVIEW | The AMRHZ-AI-13 model repository was inspected; prior checkpoint evidence described it as a minimal repository without model weights or tokenizer artifacts. Recheck before claiming its current contents. |
| GitHub Copilot | DISCUSSED / ROLE DOCUMENTED | Mentioned in repository collaboration documentation. Current usage and live integration are not established by this registry. |
| Meta AI | DISCUSSED / ROLE DOCUMENTED | Mentioned as a possible additional perspective; current usage is not independently established here. |
| Gemini | DISCUSSED / ROLE DOCUMENTED | Mentioned for comparative reasoning; current usage is not independently established here. |
| Perplexity | DISCUSSED / ROLE DOCUMENTED | Mentioned for research and source discovery; current usage is not independently established here. |

## 3. Languages, runtime, and development environment

| Tool / technology | Status | Known role / evidence boundary |
|---|---|---|
| Python | USED | Backend services, agent logic, scripts, and model experiments. |
| JavaScript / JSX | USED | React frontend and UI components. |
| HTML / CSS | USED | Web structure and styling. |
| Node.js / npm | USED | Frontend package and script ecosystem. |
| Yarn | CONFIGURED / OBSERVED | A `yarn.lock` file was observed in AP1-WEB-Console project context; verify current dependency state in the target checkout. |
| Android Termux | USED | Primary local development environment in the recent project context. |
| FastAPI | CONFIGURED / OBSERVED | Backend framework referenced in AP1-WEB-Console. Endpoint health and full runtime behavior must be tested independently. |
| Uvicorn | USED — LOCAL RUN | Used to run the local ASGI backend during prior development checks. |
| React | CONFIGURED / OBSERVED | Frontend framework present in AP1-WEB-Console/profile repository context. |
| pytest | USED — TESTING | Used for Python tests; test counts and pass/fail status are checkpoint-specific, not a blanket claim that the whole suite passes. |
| ESLint | USED — CI | Used in the profile repository's GitHub Actions workflow; success is run- and commit-specific. |
| Visual Studio Code | HISTORICAL / CONTEXT | Mentioned in earlier PC development context; current availability is unknown. |

## 4. Local AI and model tooling

| Tool / technology | Status | Known role / evidence boundary |
|---|---|---|
| llama.cpp | TESTED | Local GGUF inference was tested on Android/Termux with a Llama 3.2 1B Instruct Q4_K_M model. Recorded speed is a historical experiment, not a current benchmark guarantee. |
| GGUF | TESTED | Model format used in the local llama.cpp experiment. |
| PyTorch | CONFIGURED / OBSERVED | Present in the local model experimentation context. Installed version does not establish that every dependent package imports correctly. |
| Hugging Face Transformers | BLOCKED — HISTORICAL ISSUE | A prior Android/Termux checkpoint reported a Transformers/Tokenizers import compatibility error. Re-test the current environment before changing this status. |
| Tokenizers | BLOCKED — HISTORICAL ISSUE | A prior native import error was reported in the Android environment. Current compatibility is UNKNOWN until retested. |

## 5. Backend, storage, and integration technologies

| Tool / technology | Status | Known role / evidence boundary |
|---|---|---|
| MongoDB / Motor | CONFIGURED / OBSERVED | Conditional connection code using `MONGO_URL` was observed in AP1-WEB-Console. This does not prove a live database connection. |
| Supabase | DISCUSSED / PLANNED | Appeared in broader project/tool context; a working connection in the target repository is not established by this registry. |
| PostgreSQL | DISCUSSED / ARCHITECTURE CONTEXT | Appeared as a runtime-state/database direction in project documentation. Verify actual schema, connection, and runtime before calling it active. |
| Cloudflare Workers | CONFIGURED / DEPLOYMENT CONTEXT | A public website URL is recorded in the profile README. Current availability and deployed revision require a live check. |
| Flask | DISCUSSED / STACK DOCUMENTATION | Listed in project technology documentation; active implementation in the target repository has not been established here. |
| Localhost APIs | USED — DEVELOPMENT CONTEXT | Local API endpoints were used during development checks. Each endpoint needs its own current request/response evidence. |

## 6. AMRHZ project components (not third-party tools)

| Component | Status | Evidence boundary |
|---|---|---|
| AP1-WEB-Console | DEVELOPMENT / VERIFICATION | Repository exists and has been used for frontend/backend and CI work. Runtime and full test-suite state must be checked at the relevant commit. |
| AMRHZ-AI-13 | DEVELOPMENT / PROTOTYPE | Local agent, memory, and autopilot experiments were discussed and tested. Public model-hosting readiness is a separate question. |
| NeuralNetworkLayer | CONFIGURED / OBSERVED | Frontend component was recorded in prior AP1-WEB-Console work. A visual graph alone does not prove live agent orchestration. |
| Agent / memory / orchestrator modules | PARTIAL / CHECKPOINT-SPECIFIC | Names and behavior vary by repository checkpoint. Inspect the exact files and tests before claiming current implementation. |

## 7. Registry limitations and update protocol

This document is a **partial inventory**, not an exhaustive audit of all repositories, installed packages, accounts, deployments, or external integrations. Some statuses derive from prior project context and must be refreshed when the target commit or environment changes.

When updating this registry:

1. Inspect the relevant repository, branch, files, dependency manifests, and workflow logs.
2. Record evidence links, commit SHA, workflow run ID, test command, and observation date where applicable.
3. Separate installed/configured tools from tools that were actually executed successfully.
4. Never infer a live integration from a URL, README statement, UI element, package name, or environment variable alone.
5. Keep unresolved entries as **UNKNOWN**, **BLOCKED**, or **PLANNED / DISCUSSED** rather than promoting them without evidence.
6. Change one scoped item at a time and verify the resulting documentation change.

## AMRHZ operating principle

**INTENT → ACTION → EVIDENCE → VERIFIED STATE**

**STABILIZE → VERIFY → CONNECT → EXTEND**

First make it work. Then make it AMRHZ. Then make it evolve.
