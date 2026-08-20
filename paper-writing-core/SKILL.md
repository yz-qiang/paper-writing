---
name: paper-writing-core
description: Use when planning, drafting, or revising a technical paper section that needs stable source authority, terminology, claim boundaries, section-specific argument structure, or a shared contract across writing stages.
---

# Paper-Writing Core

## Core principle

Use one approved Section Contract as the semantic source of truth. Separate
scientific reasoning, prose drafting, and language polishing. Never repair an
upstream reasoning defect by silently changing meaning downstream.

## Required loading protocol

Before working on a paper section:

1. Read `references/writing-standards.md` completely.
2. Read `references/section-contract.md` completely.
3. Select exactly one primary section profile and read it completely.
4. Load another profile only when the section genuinely combines two roles.

Available profiles:

| Section role | Profile |
|---|---|
| Introduction | `references/profiles/introduction.md` |
| Approach or Methodology | `references/profiles/approach.md` |
| Empirical Study | `references/profiles/empirical-study.md` |
| Results | `references/profiles/results.md` |
| Experimental Setup | `references/profiles/experimental-setup.md` |
| Discussion | `references/profiles/discussion.md` |
| Threats to Validity | `references/profiles/threats.md` |

Stop and report the missing dependency if a required reference or profile is
unavailable. Do not reconstruct it from memory.

## Stage contract

- `paper-reasoning` produces a `Status: proposed` Section Contract and stops
  for author approval.
- Author approval changes the status to `approved`. Approval cannot be inferred
  from silence or from the existence of a draft.
- `paper-drafting` accepts only `Status: approved` contracts.
- `paper-polish` receives the approved Contract, selected profile, and current
  draft. It may improve expression but must preserve scientific meaning.

## Non-negotiable boundaries

- Follow the author-designated source when paper concepts conflict with code or
  auxiliary notes.
- Use implementation artifacts to verify facts, not to determine section order.
- Distinguish the analyzed or transformed object from its harness, workload,
  corpus, or other execution context.
- Treat pattern detection as candidate discovery, not proof of rewrite safety.
- Describe dynamic regression testing as evidence over observed executions, not
  as universal semantic equivalence.
- Define operational meaning before notation.
- Move engineering parameters to Experimental Setup unless they define method
  scope or correctness.
- Prefer one accurate proposition to a sentence that appears complete by
  accumulating conditions, forms, examples, and consequences.

## Failure routing

| Failure | Return to |
|---|---|
| Research process or abstraction is unresolved | `paper-reasoning` |
| Section Contract is not approved | author review |
| Paragraph order violates the Contract | `paper-drafting` |
| Planned claim lacks evidence | author or evidence collection |
| Sentence is awkward or overloaded | `paper-polish` |
| Polishing would alter scientific meaning | `paper-reasoning` |

Never hide a failure by completing the next stage's work.
