# Approach Profile

## Purpose

Explain how the technique resolves the established problem. Organize the
section around conceptual data flow rather than implementation file order.

## Local argument chain

Use the following chain where applicable:

```text
local problem
→ why direct treatment is insufficient
→ technical action
→ necessary condition, correction, or scope boundary
→ stage output
→ use by the next stage
```

Not every subsection needs every link. Keep only links supported by the method.

## Required distinctions

- Separate the program being analyzed or modified from the harness, workload,
  corpus, profile, or oracle that drives the action.
- Define each stage output before the next stage consumes it.
- Explain why a non-obvious metric or aggregation rule is chosen.
- Separate deterministic detection from semantic applicability.
- State when the method abstains instead of implying universal coverage.

## Detail placement

Include core mechanisms and scope-defining conditions. Defer parameter values,
retry budgets, hardware settings, and other reproduction details to
Experimental Setup unless they define the method itself.

## Audit

- Can the reader state what enters and leaves every stage?
- Does each subsection answer one method question?
- Are formulas introduced after the measured quantity is explained?
- Does validation claim only what the workloads observe?
- Do subsection titles name concise scientific roles?
