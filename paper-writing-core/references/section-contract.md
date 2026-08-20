# Section Contract

## Purpose

The Section Contract is the single source of truth shared by reasoning,
drafting, and polishing. It freezes the section's scientific role, evidence,
terminology, exclusions, and paragraph logic before prose generation.

Create the Contract as a short Markdown artifact. Retain only applicable
fields. Delete an inapplicable field instead of filling it with speculative
content.

## Schema

```text
Section:
Profile:
Status: proposed | approved

Section role:
Question answered:
Main claim:
Evidence and source files:
Unsupported claims:
Necessary qualifiers:

Starting context:
Existing solution or prior state:
Limitation:
Root cause or missing capability:
Required insight:
Proposed response:
Section output:

Technical objects:
Driver or execution context:
Input and output:
Required distinctions:
Comparison baseline:

Stable terminology:
Required definitions:
Information deferred to other sections:
Claims that must not be made:
Paragraph plan:
```

## Field rules

- `Section role` states what this section contributes to the paper argument.
- `Question answered` is one reader question, not a topic label.
- `Main claim` is the strongest conclusion the evidence permits.
- `Evidence and source files` names the authority for every factual claim.
- `Unsupported claims` records attractive claims that current evidence cannot
  sustain.
- `Necessary qualifiers` records scope, applicability, and validation limits.
- `Section output` names the artifact or conclusion consumed later.
- `Technical objects` separates the analysis target from drivers and inputs.
- `Required distinctions` prevents nearby concepts from collapsing into one
  term.
- `Information deferred to other sections` controls detail placement.
- `Claims that must not be made` creates explicit semantic guardrails.
- `Paragraph plan` assigns one rhetorical job to each paragraph.

## Approval gate

`paper-reasoning` creates `Status: proposed` and presents the complete Contract
for author review. Only explicit author approval changes the status to
`approved`. Editing prose, accepting one sentence, or continuing the
conversation does not imply approval.

If the author changes a claim, source authority, technical sequence, qualifier,
or baseline, return the Contract to `proposed`. Update and reapprove it before
drafting resumes.

## Handoff rules

- Reasoning may attach concise evidence notes outside the Contract.
- Drafting may add local transitions but cannot alter Contract fields.
- Polishing may revise wording but must compare the revision against the
  Contract for semantic drift.
- Missing evidence returns to the author or evidence collection. It is never
  represented by a placeholder in manuscript prose.

## Minimal approval presentation

Present one recommended Contract. Add alternatives only when they encode
materially different scientific abstractions. End with a direct request for
approval or correction.
