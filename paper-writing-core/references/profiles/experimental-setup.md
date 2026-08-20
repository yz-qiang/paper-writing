# Experimental Setup Profile

## Purpose

Provide the information needed to interpret and reproduce the evaluation.

## Required content

Describe the environment, study subjects, baselines, metrics, repeated-run
policy, and parameter values that affect reproduction. Define exclusions and
failure handling when they change the evaluated population.

## Organization

Group information by experimental decision, not by configuration-file order:

```text
subjects and selection
→ comparison baselines
→ workloads and measurement protocol
→ environment
→ metrics and statistical treatment
→ implementation parameters
```

## Audit

- Can a reader identify the exact evaluated versions and baselines?
- Are hardware and software environment details sufficient for reproduction?
- Are warm-up, repetition, timeout, and aggregation policies explicit?
- Are method concepts referenced rather than redefined?
