---
name: paper-polish
description: Use when academic method prose remains unclear or overloaded because its scientific claim, abstraction level, analyzed object, execution context, comparison baseline, aggregation logic, notation, terminology, or paragraph role is not explicit; especially when sentences accumulate conjunctions, consequences, premature enumeration, abstract labels, or implementation details.
---

# Meaning-First Method Polishing

## Core principle

Prioritize scientific clarity over elegance. Freeze the intended claim, local method question, and abstraction level before rewriting. Explain the minimum needed for a reader to understand what the method does, why the design choice is necessary, and what the stage outputs. Completeness belongs to the paragraph or subsection, not to every sentence.

Accuracy outranks surface completeness. Do not make one sentence carry every
condition, manifestation, consequence, and exception. State the load-bearing
claim first. Add another sentence only when it improves correctness or supplies
logic needed by the next sentence. Omission is preferable to a vague attempt at
being exhaustive.

Treat implementation as evidence, not as the paper outline. Inspect code to verify the action and its scope, but do not transfer every guard, threshold, retry, fallback, or validation branch into the manuscript. Aim for prose that is **concrete but not exhaustive**.

## Workflow

### 1. Freeze the semantic kernel

Read the surrounding section and fill only the applicable fields:

```text
Rhetorical job and local question:
Analyzed or transformed object:
Driver or execution context:
Action or definition:
Per-context result:
Aggregation or selection rule:
Final output:
Comparison baseline:
Necessary qualifier:
Claim strength and citation role:
```

Treat “only express these meanings” as a fixed detail budget. Add an implementation detail only when omitting it would make the claim false, hide the core mechanism, or remove a distinction needed later.

### 2. Verify without following code order

Use implementation inspection to answer explicit questions: Does the claimed action occur? What condition delimits its scope? What concrete program change or runtime measurement produces the result? Which details are merely safeguards or engineering parameters?

Return to the frozen paragraph role after inspection. Do not organize the manuscript around files, functions, branches, or pipeline logs.

### 3. Build a method decision chain

Organize a method subsection around one local question. When applicable, progress through:

1. **Motivation:** why the local problem matters and why indiscriminate processing is inadequate.
2. **Measurement or transformation:** the concrete action applied to the program.
3. **Necessary correction:** a confounder or representation mismatch that would otherwise make the result inaccurate.
4. **Aggregation or selection:** how local results become a stage-level decision and why that rule is used.
5. **Output:** the artifact passed to the next stage.

This is a reasoning pattern, not a mandatory five-paragraph template. Omit inapplicable steps; never invent a limitation to complete the sequence. Each paragraph should introduce one new need and resolve it before moving on.

### 4. Rewrite and stop

Prefer a concrete technical subject and a direct verb. Keep technical terms stable; do not cycle among synonyms for *function*, *API*, *operation*, *workload*, *harness*, or a project-defined artifact. Repeat the exact noun when a pronoun could have multiple antecedents. Use *However*, *Therefore*, and *In particular* only for a real contrast, consequence, or elaboration.

Avoid apostrophe-s possessives for technical entities. Prefer a noun compound
when the relation is conventional, as in *the LLVM cost model*. Use an explicit
*of* phrase when the relation needs to remain visible, as in *the debug location
of the instruction* or *the core computation of the project*.

Give each sentence one semantic job. Prefer a simple subject--verb--object
structure. Use a subordinate clause only when separating it would obscure the
logical relation. Short sentences must still form a continuous argument. Begin
from an object the reader already knows, add one fact, then use that fact as the
starting point of the next sentence. This old-to-new progression should make the
reasoning unfold one step at a time.

Apply a coordination budget to every sentence. More than one occurrence of
*and* or *or* is a strong presumption that the sentence is overloaded. Split the
sentence unless the coordinated items form one short, genuinely parallel list.
Before retaining a coordination, check whether its items occupy the same
semantic level. If one item subsumes another, use the superordinate term alone
unless the narrower item introduces a necessary contrast. For example, replace
*into the harness or another caller* with *into a caller* because the harness is
itself a caller.
Do not retain repeated conjunctions merely to sound complete. Treat semicolon
chains and trailing result clauses such as “..., enabling ...” in the same way.
Check whether the sentence combines a mechanism, its manifestations, its
consequences, and an example. If the latter clause is a separate consequence,
split it and state the causal transition directly:

> These simplifications reduce the estimated inlining cost. LLVM can then inline the callee.

Do not enumerate every form or benefit merely to make a definition appear complete. State the load-bearing proposition first; disclose distinctions only where the reader needs them. For rule-oriented prose, use the following progression:

1. The opening sentence names the common performance mechanism.
2. *Observed Pattern* explains the recurring forms and the evidence used to recognize them.
3. A concrete example describes what the program does, without meta-language such as “a representative instance appears” or “the function implements this pattern.”
4. *Optimization Direction* states the corresponding transformation and any necessary precondition.

Do not pull the forms, examples, or all downstream effects into the rule-opening sentence. For example, prefer “Invariant Dispatch Specialization moves an invariant dispatch decision outside the loop.” Explain callback-target dispatch and configuration-value dispatch in *Observed Pattern*, rather than enumerating both in the opening sentence.

Stop when the reader can answer: What is the problem? What does the method do? Why is the non-obvious choice necessary? What directly results?

### 5. Run a sentence-to-paragraph pass

Before delivery, inspect the prose at three levels:

1. **Proposition:** underline the main predicate of each sentence. If two
   independent claims remain, split the sentence.
2. **Coordination:** flag every sentence containing more than one *and* or *or*.
   Keep it only for one compact parallel list; otherwise split it.
3. **Continuity:** verify that each sentence follows from the previous one.
   Make contrast, cause, condition, or elaboration explicit only where that
   relation actually exists.

Then read the paragraph as a decision chain. The paragraph should open with one
local question or claim. Each following sentence should resolve the next
necessary step. End once the paragraph has delivered its result. Do not append a
summary sentence that merely repeats the paragraph.

## Method-specific checks

### Separate the object from its driver

Name what the system analyzes or modifies separately from what drives the analysis. A project is profiled *under a workload*; the workload is not the analyzed program. A modified project is validated *with a harness and inputs*; those artifacts are execution context, not the validation target. Check the grammatical object of the main verb whenever several artifacts occur in one sentence.

### Explain non-obvious choices comparatively

For a non-obvious metric, representation, aggregation rule, or validation policy, state the choice and the concrete failure avoided by the nearest plausible alternative: self time rather than inclusive time; maximum rather than mean; source-level frames rather than binary symbols. Keep the comparison local and parallel. Do not invent an alternative merely to create contrast.

### Introduce notation after operational meaning

Notation compresses an explanation; it must not replace one. First describe what is measured, including its scope or denominator when material. Then name the local quantity, define any cross-context aggregation, explain why that aggregation matches the goal, and name the final set or artifact. Keep a short unnumbered definition inline; display or number an equation only when it needs emphasis, spans multiple lines, or is referenced later.

### Match each citation to one claim

Identify whether a citation supports empirical motivation, a theoretical bound, an established measurement technique, or a prior method. Prefer a direct source for a narrow empirical claim over a broad textbook. A citation does not replace a mechanism explanation. During language-only polishing, flag a mismatch rather than adding or replacing sources unless the user explicitly requests source work.

## Reviewer audit

Before returning the revision, verify:

1. **Fidelity:** the scientific claim and qualifiers are unchanged.
2. **Question:** the subsection answers one explicit method question.
3. **Object:** the analysis target is distinct from its workload, harness, inputs, or other driver.
4. **Abstraction:** the detail level matches the paragraph role.
5. **Concreteness:** the action is visible without an implementation dump.
6. **Choice:** each non-obvious decision has an accurate, local rationale.
7. **Notation:** every symbol has an operational meaning before use.
8. **Citation:** each source directly supports its attached claim.
9. **Cohesion:** each paragraph prepares the next, and the subsection ends with a clear output.
10. **Sentence load:** each sentence performs one semantic job and normally uses a simple clause structure.
11. **Coordination:** a sentence with repeated *and* or *or* has been split unless it contains one compact parallel list.
12. **Continuity:** each sentence starts from established context and advances the argument by one step.
13. **Disclosure:** definitions state the common mechanism before forms, examples, and consequences.
14. **Stopping:** another detail would materially improve correctness or understanding; otherwise stop.
15. **Coordination level:** no coordinated item is already covered by another item or by a shared superordinate term.
16. **Possessives:** technical relations avoid apostrophe-s possessives when a noun compound or an *of* phrase is clearer.

## Output discipline

Return one best revision, not cosmetic variants. Diagnose semantic or structural problems before proposing prose. Modify manuscript files only when explicitly requested. Flag any edit that could change scientific meaning.

## Common failure modes

| Failure | Correction |
|---|---|
| Treating code as a paper checklist | Use code to verify the frozen claim; admit only necessary details. |
| Listing steps without a local question | Rebuild the subsection as a decision chain ending in an output. |
| Profiling or validating a workload when the project is the target | Name the project as the object and the workload as context. |
| Hiding the action behind *view*, *representation*, or *relationship* | State the smallest concrete program action. |
| Giving a metric without its alternative | State the nearby alternative and the error the chosen metric avoids. |
| Introducing a formula before its meaning | Explain the quantity, then local notation, aggregation, and output. |
| Attaching a broad citation to a narrow claim | Use a direct source when authorized; otherwise flag the mismatch. |
| Mixing technical abstractions or ambiguous pronouns | Repeat the exact term or split the sentence. |
| Making one sentence “complete” with *and*, *or*, or an *-ing* result tail | Keep the load-bearing proposition; move separate consequences or forms to the next sentence. |
| Coordinating a subtype with its broader category | Keep the shared superordinate term unless the subtype creates a necessary contrast. |
| Using apostrophe-s for a technical object | Use a conventional noun compound or an explicit *of* phrase. |
| Splitting a long sentence into disconnected short statements | Order the statements from known context to new information; make the logical relation explicit. |
| Enumerating every manifestation in a rule definition | Define the shared mechanism first; explain individual forms under *Observed Pattern*. |
| Describing examples through meta-labels such as “representative instance” | State the concrete program behavior directly. |
