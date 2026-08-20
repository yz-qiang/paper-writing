---
name: paper-drafting
description: Use when an approved Section Contract and its cited evidence are available and the task is to turn the settled argument into manuscript-ready prose for a technical paper section.
---

# Paper Drafting

## Core principle

Draft the approved argument. Do not redesign it. Use progressive disclosure to
turn each Contract unit into clear manuscript prose while preserving source
authority, terminology, qualifiers, and claim strength.

**Required dependency:** Use `paper-writing-core`. Read its `SKILL.md`, shared
writing standards, Section Contract reference, and the Contract's selected
section profile completely before drafting.

## Entry gate

Confirm all of the following before writing prose:

1. The Section Contract states `Status: approved`.
2. The Contract names one primary section profile.
3. The evidence files required by the paragraph plan are available.
4. The main claim, terminology, comparison baseline, and necessary qualifiers
   are explicit.

If the status is `proposed`, stop and return the Contract for author approval.
If evidence is missing, report the gap outside the manuscript. Never insert a
placeholder claim.

## Drafting modes

### Guided mode

In **guided mode**, draft one rhetorical unit or paragraph, obtain author
feedback, and then continue. Use this mode by default for Introductions and core
Approach sections, where local wording often reveals a remaining conceptual
ambiguity.

### Full-section mode

In **full-section mode**, draft the complete section in one pass. Use this mode
for shorter sections or when the Contract and paragraph plan are stable. Do not
choose it merely to avoid the approval gate.

Follow the mode requested by the author. If no mode is specified, apply the
defaults above.

## Workflow

### 1. Freeze the semantic boundary

Copy the following Contract fields into a private drafting checklist:

```text
Question answered
Main claim
Evidence and source files
Necessary qualifiers
Section output
Stable terminology
Required definitions
Claims that must not be made
Paragraph plan
```

**Do not change** the main claim, technical sequence, evidence boundary,
comparison baseline, required distinction, or qualifier. Return to
`paper-reasoning` when author feedback requires such a change.

### 2. Expand the paragraph plan

Give each paragraph one primary rhetorical role:

- motivate a local need;
- define a technical object;
- describe an action;
- justify a non-obvious choice;
- state a scope condition;
- report a result or stage output;
- connect that output to the next stage.

Do not force all roles into every paragraph. Preserve the profile's argument
order and remove any unit unsupported by the Contract.

### 3. Draft through progressive disclosure

Begin each paragraph from established context. Introduce one new concept at a
time. Define an operation before its harness, a measurement before its symbol,
and a detected pattern before the rewrite conditions associated with it.

Use a concrete technical subject with a direct verb. Keep the analyzed object
distinct from its workload, harness, corpus, oracle, or other execution
context. Repeat a stable technical term when a pronoun would be ambiguous.

### 4. Explain choices locally

When the Contract contains a non-obvious metric, aggregation rule, scope, or
validation policy, state the choice beside the concrete failure avoided by the
nearest plausible alternative. Do not add an alternative absent from the
approved reasoning merely for rhetorical effect.

### 5. Control claim strength

Trace each factual sentence to the Contract's evidence. Preserve boundaries
such as observed-behavior regression testing, workload-specific performance,
or conditional rewrite applicability. Do not generalize from evaluated cases
to universal behavior.

Place a citation directly beside the claim it supports. Do not add or replace a
citation unless source work is part of the task.

### 6. Run a prose pass

Check each sentence for one semantic job. Split repeated *and* or *or* unless
the items form one compact parallel list. Preserve old-to-new continuity after
splitting. Use signposts only for genuine logical relations.

Check each paragraph against its assigned role. End when the paragraph delivers
that result. Remove a final sentence that merely repeats the paragraph.

### 7. Deliver manuscript-ready text

Return one best draft. Remove drafting labels, evidence notes, alternatives,
and internal scaffolding from manuscript prose. Preserve LaTeX commands and
project macros when editing a `.tex` file.

Modify a manuscript file only when the author explicitly requests a file edit.
Otherwise return the proposed prose in the response.

## Permitted local decisions

Drafting may:

- choose exact sentence boundaries;
- add necessary local transitions;
- select an approved example when several support the same claim;
- omit an approved detail that is unnecessary for the paragraph's role;
- format notation after its operational meaning has been established.

Drafting may not add a new mechanism, claim, baseline, parameter, example,
scope condition, or citation.

## Feedback routing

| Author feedback | Action |
|---|---|
| Wording is awkward or verbose | revise locally or use `paper-polish` |
| Paragraph order violates the approved plan | repair within drafting |
| Technical meaning is wrong | return to `paper-reasoning` |
| A new claim or source is required | update and reapprove the Contract |
| Evidence cannot support a planned sentence | report the gap; do not draft it |

## Final check

Before delivery, verify that the draft answers the Contract's question, reaches
its stated section output, uses stable terminology, preserves every necessary
qualifier, and makes none of the prohibited claims.
