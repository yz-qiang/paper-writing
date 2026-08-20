---
name: paper-reasoning
description: Use when a technical paper section is not ready to draft because its scientific role, source authority, technical process, abstraction, evidence boundary, terminology, or paragraph logic remains unresolved.
---

# Paper Reasoning

## Core principle

Reconstruct the research argument before writing manuscript prose. Determine
what the section must establish, which evidence supports it, and which
abstraction exposes the contribution without leaking implementation structure.

**Required dependency:** Use `paper-writing-core`. Read its `SKILL.md`, shared
writing standards, Section Contract reference, and the selected section profile
completely before producing an output.

## Deliverable boundary

Produce one `Status: proposed` Section Contract for author approval. Add concise
evidence notes or unresolved questions outside the Contract when needed.

**Do not draft complete manuscript prose.** Short candidate formulations are
allowed only when they help distinguish two materially different concepts or
titles. Do not use polished paragraphs to bypass the approval gate.

## Workflow

### 1. Lock the local task

Identify the target section, its neighboring manuscript context, and the exact
decision the author wants to make. Distinguish among designing the argument,
checking an existing outline, explaining implementation behavior, and drafting
prose. This skill owns the first three tasks, not the final one.

### 2. Establish source authority

Record every author-designated paper source before inspecting auxiliary
materials. Apply the authority order defined by `paper-writing-core`.

When paper terminology conflicts with implementation names, preserve the paper
terminology. Use code to verify the mechanism, conditions, and output. Report a
material conflict instead of merging the accounts.

### 3. Reconstruct the technical process

Describe the mechanism privately in plain terms before choosing paper labels:

```text
object being analyzed or transformed
driver or execution context
input and configuration
action
reason for the action
scope or correctness condition
output
consumer of the output
```

Inspect code or experimental artifacts only to answer an explicit factual
question. Search by concepts and data flow, not merely by internal stage names.
Do not let file order become the method outline.

### 4. Select the paper abstraction

Classify each verified detail as a core mechanism, a scope-defining condition,
or an engineering parameter. Retain only the first two in the method argument.

Check nearby concepts for accidental collapse. Common distinctions include:

- operation versus harness;
- corpus versus workload;
- analyzed project versus execution driver;
- pattern match versus rewrite applicability;
- per-context measurement versus project-level aggregation;
- dynamic regression evidence versus semantic equivalence.

Choose concise conceptual names. Reject magic identifiers and implementation
labels that do not express a reader-relevant distinction.

### 5. Build the section decision chain

Select one primary section profile from `paper-writing-core`. Use the profile as
a reasoning guide, not as a form to fill mechanically. State the section-level
question. Then assign one rhetorical job to each planned paragraph.

For a method section, verify the progression from local need to action,
condition, output, and downstream use. For an Introduction, derive the required
capability before introducing the technique. For a Results section, separate
the observation from an unsupported mechanism explanation.

### 6. Run the reviewer audit

Review the proposed chain as an FSE/ICSE reviewer:

1. Does the section establish why its action is needed?
2. Does a claimed limitation have a concrete failure mechanism?
3. Do neighboring modules have non-overlapping responsibilities?
4. Does each title accurately name the content?
5. Is paper terminology controlled by the author-designated source?
6. Are technical objects distinct from harnesses, workloads, and inputs?
7. Does every stage output feed a later decision?
8. Are formulas delayed until their operational meaning is clear?
9. Are Approach details separated from Experimental Setup parameters?
10. Does every validation statement remain within observed evidence?

Repair the reasoning chain before presenting it. Do not hide an unresolved gap
with fluent prose.

### 7. Produce the Contract and stop

Fill only applicable fields from the core Section Contract schema. Cite exact
source files under `Evidence and source files`. Put attractive but unsupported
claims under `Unsupported claims` or `Claims that must not be made`.

Present one recommended Contract. Offer alternatives only when they correspond
to materially different paper abstractions. End with a direct request for
author approval or correction. Do not mark the Contract approved yourself.

## When evidence is incomplete

Continue with verified fields when the missing information does not affect the
section's main claim. Mark the gap outside manuscript prose. Stop for author
input when a missing choice changes the claim, technical sequence, baseline,
scope, or section output.

Never invent experiments, mechanisms, citations, examples, terminology, or
qualifiers to complete the Contract.

## Common failures

| Failure | Correction |
|---|---|
| Summarizing source files in their existing order | Reconstruct object, action, condition, and output first. |
| Treating code names as paper concepts | Restore the author-designated taxonomy. |
| Listing implementation details without a local question | Build a decision chain using the selected profile. |
| Treating a detected pattern as an applicable rewrite | Record detection evidence and semantic preconditions separately. |
| Writing polished paragraphs before approval | Return a proposed Contract and stop. |
| Offering many cosmetic outlines | Recommend one abstraction; show only materially different alternatives. |
