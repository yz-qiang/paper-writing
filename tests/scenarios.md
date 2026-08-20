# Paper-Writing Suite Scenario Tests

These fixtures encode observed writing failures. Validation checks behavioral
properties rather than exact wording.

## 1. Operation, harness, corpus, and workload

**Input failure:** The prose uses *workload* for an operation, a harness, an
input collection, and an execution configuration.

**Expected behavior:** Reasoning separates the end-to-end operation from its
driver. It defines a functional or performance workload only after identifying
the relevant operation, inputs, and execution configuration.

## 2. Translation refinement

**Input failure:** The subsection follows cleanup script order and lists every
guard, retry, and compiler check.

**Expected behavior:** Reasoning organizes the section around definition
consolidation and boundary/safety refinement. Drafting includes only the core
mechanism and correctness-relevant conditions.

## 3. Hotspot localization notation

**Input failure:** The draft introduces `s(f,w)` and `h(f)` before explaining
what is sampled or how per-operation hotspot lists are combined.

**Expected behavior:** Drafting first explains profiling under each performance
workload, self-time attribution, and project-level aggregation. Notation appears
only if it shortens that established explanation.

## 4. Many-to-many optimization matches

**Input failure:** The outline assumes one rule per function or one match per
rule.

**Expected behavior:** The Contract preserves the many-to-many relation among
hot functions, optimization rules, and source regions.

## 5. Detection versus applicability

**Input failure:** Matching an observed pattern is described as proof that the
optimization can be applied safely.

**Expected behavior:** Reasoning separates deterministic pattern detection from
the semantic preconditions required by a rewrite. The method may abstain when a
precondition cannot be established.

## 6. Source authority

**Input failure:** Implementation rule identifiers conflict with the nine-rule
taxonomy in `study/RQ3.tex`.

**Expected behavior:** The author-designated paper source controls the paper
taxonomy. Code is inspected only to verify detection and rewrite mechanics.

## 7. Dynamic validation boundary

**Input failure:** Regression testing is claimed to prove semantic equivalence
for all inputs.

**Expected behavior:** The prose claims preservation of observed behavior over
the generated functional workloads and reports performance comparisons over
fixed performance workloads.

## 8. Introduction bridge

**Input failure:** The Introduction moves from a surface limitation directly to
“To this end, we propose ...”.

**Expected behavior:** Reasoning identifies the root cause and derives the
capability required of a solution before introducing the technique.

## 9. Sentence overload

**Input failure:** A sentence carries a mechanism, three forms, an example,
conditions, and consequences through repeated *and* or *or*.

**Expected behavior:** Polishing retains one semantic job per sentence. The
shorter sentences preserve old-to-new continuity instead of becoming a list of
disconnected statements.

## 10. Implementation leakage

**Input failure:** The draft exposes labels such as `W1`, `W2`, or `ChangeSet`
and enumerates retry counts or thresholds in Approach without a method-level
reason.

**Expected behavior:** Reasoning replaces implementation labels with concepts.
Engineering parameters move to Experimental Setup unless they define scope or
correctness.

## 11. Redundant coordination and technical possessives

**Input failure:** The draft writes “into the harness or another caller,” even
though a harness is already a caller, and uses technical possessives such as
“the instruction's debug location.”

**Expected behavior:** Polishing replaces overlapping alternatives with their
shared superordinate term. It also rewrites apostrophe-s possessives for
technical entities as noun compounds or explicit *of* phrases.
