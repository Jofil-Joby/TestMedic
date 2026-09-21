# TestMedic

> A portable engineering agent for **test structure and quality**.

TestMedic inspects observable project evidence, detects **missing or weak test assets**, and produces an explainable improvement plan. Its purpose is not to replace specialist tooling. It provides a focused, auditable diagnostic layer that can travel across agent runtimes.

## What makes it different

This project follows an **evidence → decision → explanation** model:

```text
Project
  ↓
Scanner
  ↓
Domain Evidence
  ↓
Deterministic Diagnostic Rule
  ↓
Finding + Evidence + Confidence
  ↓
Improvement Plan
```

The agent does not invent evidence. A finding is tied to what the scanner can actually observe.

## Diagnostic contract

| Layer | TestMedic behavior |
| --- | --- |
| Domain | test structure and quality |
| Primary signal | test/spec files |
| Remediation | Add or strengthen automated tests |
| Output | Structured, explainable findings |
| Uncertainty | Explicitly constrained by available evidence |

## Portable architecture

```text
                    ┌─────────────────────┐
                    │   Portable Agent    │
                    │ identity + behavior  │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ↓                ↓                ↓
          Diagnostic        Duties &         Explainability
            Logic           Workflow           Contract
              │
              ↓
        Runtime Adapters
       ┌──────┬──────┬──────┬──────┐
       ↓      ↓      ↓      ↓
    OpenAI  CrewAI  Claude  Lyzr
```

The core diagnostic logic is kept separate from framework-specific adapters. This is the central design idea of the project, not four copies of the same agent wearing different hats.

## Repository structure

```text
agent.yaml          # Portable identity and passport metadata
SOUL.md             # Identity, principles, and behavior
AGENTS.md           # Agent responsibilities
DUTIES.md           # Maker / Checker workflow
EXPLAINABILITY.md   # Decision, inputs, limits, and evidence contract
core/               # Shared result model
tools/              # Scanner and domain diagnostics
skills/             # Declared capabilities
workflows/          # Agent workflows
adapters/           # Runtime-facing adapters
tests/              # Deliberately diagnostic project fixtures
```

## Passport portability

The agent is structured for the OpenGAP passport model and can be exported to:

- OpenAI Agents SDK
- CrewAI
- Claude Code
- Lyzr

The important part is the **portable contract**: identity, behavior, duties, explainability, tools, and skills remain defined independently of a single runtime.

## Verification

The repository includes:

- Local adapter verification
- A domain-specific broken-project fixture
- OpenGAP-compatible passport metadata
- Explainability requirements
- Export verification across the supported targets

The engineering workflow is:

```text
Validate passport
    → Verify adapters
    → Run diagnostic fixture
    → Export with OpenGAP
    → Inspect generated artifacts
```

## Scope and limitations

TestMedic is a focused diagnostic prototype. Its conclusions are limited to the evidence and rules implemented in this repository. It should complement, not replace, production-grade static analysis, security scanners, observability platforms, CI systems, or human review where appropriate.

## Why this project exists

This repository is one member of a deliberately modular **Medic agent family**. Each agent applies the same portable passport architecture to a different engineering failure surface.

That makes the collection useful as an interoperability experiment:

```text
One passport architecture
        +
Different diagnostic domains
        +
Multiple agent runtimes
        =
Portable engineering-agent family
```

## Challenge context

Built for the **HiDevs × Lyzr Agent Passport Challenge**, exploring portable agent identity, behavior contracts, explainability, verification, and framework interoperability.

## Author

**Jofil Joby**  
[GitHub](https://github.com/Jofil-Joby)
