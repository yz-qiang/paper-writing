# Shared Writing Standards

## 1. Source authority

Resolve conceptual conflicts in this order:

1. **Author clarification** in the current task.
2. Author-designated manuscript source.
3. Implementation and experimental artifacts.
4. Auxiliary notes.

The author-designated source controls paper-level terminology and taxonomy.
Code can establish what the system does, under which conditions, and with what
output. **Implementation is evidence, not the paper outline.** Do not transfer
file order, internal IDs, retry branches, logging labels, or every concrete
case into the manuscript.

When sources conflict, record the conflict in the Section Contract. Do not
silently blend incompatible accounts.

## 2. Abstraction control

Classify each implementation detail before admitting it to the paper:

- **Core mechanism:** required to understand what the method does.
- **Scope or correctness condition:** required to state when the mechanism
  applies or why it is valid.
- **Engineering parameter or safeguard:** belongs in Experimental Setup or can
  be omitted when it does not change the method.

Replace magic identifiers such as `W1`, `W2`, and `ChangeSet` with the concept
they denote. Introduce an implementation label only after defining the concept
and only when later prose needs the label.

Do not force every concrete instance into a paper-level rule. A rule may have
several recurring forms. Each form may have multiple concrete instances.

Preserve the actual cardinality of technical relations. Do not collapse a
many-to-many relation into one item per function, rule, site, workload, or
stage merely to simplify the outline. Define the relation explicitly when the
cardinality affects later detection, generation, aggregation, or validation.

## 3. Progressive disclosure

**Progressive disclosure** is mandatory. Define an object before another stage
uses it. Introduce a harness only after defining the operation it drives. State
how a quantity is measured before naming it with notation. Establish a rule
match before discussing interactions among matches.

Use old-to-new continuity:

1. Start from an object established in the preceding context.
2. Add one fact needed by the next sentence.
3. Use that fact as the next sentence's starting point.

Use *However*, *Therefore*, *In particular*, and similar signposts only when a
real contrast, consequence, or elaboration exists. A signpost cannot repair a
missing logical relation.

## 4. Object, driver, input, and artifact

Keep four roles distinct:

- **Object:** the program element being analyzed or transformed.
- **Driver:** the mechanism that executes or exposes the object, such as a
  harness.
- **Input or configuration:** the data and execution settings supplied through
  the driver.
- **Artifact:** the result passed to the next stage.

A Rust project is profiled under a performance workload. The workload is not
the program being optimized. A modified project is validated through a harness
and inputs. The harness is not the validation target.

Check the grammatical object of every action when several technical artifacts
appear in one sentence.

## 5. Section, paragraph, and sentence logic

Each section answers one explicit paper-level question. Each paragraph answers
one local question. Each sentence performs **one semantic job**.

A method paragraph often follows this local chain:

```text
local need
→ concrete action
→ necessary condition or correction
→ result
→ use by the next stage
```

Use only the steps that the material supports. Do not invent a limitation or
comparison to complete a template.

Prefer a concrete subject and a direct verb. Avoid abstract nouns such as
*view*, *relationship*, *representation*, or *framework* when they hide the
actual program action. Repeat a technical noun when a pronoun has more than one
possible antecedent.

More than one occurrence of *and* or *or* creates a strong presumption that a
sentence is overloaded. Keep repeated coordination only for one short,
genuinely parallel list. Treat semicolon chains and trailing *-ing* consequence
clauses the same way. Split separate consequences into separate sentences.

Short sentences must still form an argument. Do not replace one overloaded
sentence with disconnected statements.

## 6. Terminology, titles, examples, and notation

Define project terms once. Reuse the exact noun instead of cycling among loose
synonyms. Ensure definitions match other paper sections.

Use concise section titles that name the scientific role or delivered result.
Avoid titles that expose an evidence source, implementation label, or tool
choice unless that distinction is itself the contribution.

Describe examples through concrete program behavior. Avoid meta-language such
as “a representative instance appears” or “the function implements this
pattern.”

Operational meaning precedes notation. Explain what is measured, under which
context, and for what decision. Introduce a symbol only if it compresses that
explanation. Omit a formula when a short sentence is clearer.

## 7. Choices and comparisons

Explain a non-obvious metric, aggregation rule, scope, or validation policy by
contrasting it with the nearest plausible alternative. State the concrete
failure avoided by the chosen design. Examples include self time versus
inclusive time and maximum versus mean across operations.

Do not invent an alternative merely to create rhetorical contrast.

## 8. Evidence and claim boundaries

The strength of a claim cannot exceed its evidence.

- **Dynamic regression testing** supports preservation of observed behavior on
  the executed functional workloads. It does not prove equivalence for every
  possible input.
- Performance validation compares fixed work under stated conditions. It does
  not establish a context-independent speedup.
- Pattern detection identifies a candidate optimization opportunity. A rewrite
  still requires its semantic and scope preconditions.
- A citation supports one attached claim. It does not replace a mechanism
  explanation.

When evidence is missing, report the gap outside manuscript prose. Never invent
data, citations, mechanisms, examples, or qualifiers.

## 9. Reviewer audit

Before handing a section to the next stage, check:

1. What exact question does the section answer?
2. Does every paragraph have one role?
3. Is the technical object distinct from its driver and inputs?
4. Does code verify the account without dictating the outline?
5. Are scope conditions visible without an implementation dump?
6. Does each stage produce an artifact consumed later?
7. Is notation introduced after operational meaning?
8. Does each claim stay within its evidence boundary?
9. Does each title accurately name its content?
10. Would another detail materially improve correctness or understanding? If
    not, stop.
