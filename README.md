# TestMedic

> Portable agent for diagnosing missing, weak, or poorly signposted test coverage in software projects.

## What it does

TestMedic inspects a project and looks for evidence that automated testing is absent or difficult to recognize. Instead of pretending to understand the entire codebase, it reports observable evidence and turns that evidence into a focused improvement plan.

### Diagnostic fingerprint

**Test structure → evidence → finding → repair plan**

Its core signal is the presence or absence of recognizable test/specification files, while the shared scanner records the surrounding project evidence used to explain the result.

## Why this agent is distinct

TestMedic is intentionally narrow. It is not a general code reviewer. Its job is to answer one practical question:

> **Can a project clearly demonstrate that it has automated tests?**

That makes it useful as a first-pass quality gate in a larger agent pipeline.

## Passport architecture

```text
Project
  ↓
Scanner
  ↓
Test-focused diagnostic rule
  ↓
Evidence-backed finding
  ↓
Improvement plan
```

The portable contract is separated from the diagnostic implementation, so the agent can be exported without rewriting its identity and behavior for every framework.

## Verification

This repository includes:
- OpenGAP-compatible passport metadata
- local adapters for OpenAI, CrewAI, Claude Code, and Lyzr
- a broken-project fixture designed to trigger the test diagnostic
- adapter verification tests

The repository has been validated against OpenGAP and its four framework exports have been exercised successfully.

## Repository layout

```text
agent.yaml          Identity and passport metadata
SOUL.md             Agent behavior and principles
EXPLAINABILITY.md   Decision and evidence contract
AGENTS.md           Agent roles
DUTIES.md           Maker / Checker duties
agent.py            Runtime entry point
tools/              Scanner and diagnostic rules
adapters/           Portable framework adapters
tests/              Fixtures and verification
```

## Design principle

**Evidence before confidence.** A missing recognizable test file is a signal, not proof that a project has no tests. TestMedic reports what it can observe and keeps recommendations bounded to that evidence.

## Part of the Medic family

TestMedic is one member of a set of focused engineering agents. Each agent owns a different diagnostic domain while sharing the same portable passport structure. The result is a composable toolkit rather than one oversized general-purpose agent.