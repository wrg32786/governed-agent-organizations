# AI Program Control Plane

A reusable framework for evidence-driven projects built by human overseers and AI workers.

## Roles

```text
Human Overseer
  owns purpose, consequential authority, risk acceptance, and release

Project Lead
  decomposes work, freezes evidence populations, reviews, dispositions,
  promotes accepted conclusions, and protects scope

Program Orchestrator
  maintains canonical program truth, execution order, dependencies,
  integration state, and evidence closure

Builder
  implements the bounded change and produces author evidence

Independent Reviewer
  does not author the candidate and attempts to falsify the claimed property
```

One person or model may hold multiple low-risk roles, but consequential author, sole evaluator, and promoter should not collapse into one actor.

## Systems of record

| Plane | Owns |
|---|---|
| Research repository | sources, reports, corrections, dispositions, hypotheses |
| Program repository | ratified plans, status, dependencies, promotion packets, evidence gates |
| Execution system | work ownership, sequencing, live task state |
| Product repository | code, tests, release artifacts |
| Real-time communication | coordination only; not durable truth |
| External business systems | authoritative customer, finance, delivery, or operational records |

## Four-document program core

### `MASTER-PLAN.md`

Purpose, architecture boundaries, permanent refusals, release definition, and long-range sequencing.

### `CAPABILITY-COMPLETION-PLAN.md`

For each capability:

```text
claim
current mechanism
gap
dependencies
acceptance criteria
red vector
positive witness
evidence population
rollback
```

### `DEFINITION-OF-DONE.md`

The complete release gate. A capability is not complete because a pull request merged.

### `STATUS.md`

Current exact identities, active lanes, blockers, next gate, and evidence counts. Historical prose must not silently override current exact state.

## Claim maturity

```text
prior published result
repository-statically-observed mechanism
repository-test-covered mechanism
implemented mechanism
independently demonstrated behavior
repeated operating result
business outcome
inference
hypothesis
UNKNOWN
```

A claim may move upward only through new evidence. It cannot skip levels by wording.

## Work lifecycle

```text
question
→ source population
→ report
→ independent disposition
→ promotion candidate
→ program acceptance, defer, or reject
→ bounded implementation
→ red-first proof
→ independent review
→ runtime or operational evidence
→ outcome
→ retain, revise, reject, supersede, or retire
```

A report never approves itself.

## Exact population rule

Every consequential result binds to:

```text
product SHA
harness SHA
fixture or corpus identity
environment
configuration
model/runtime identity where material
evaluator identity
```

Changing a load-bearing identity invalidates prior proof until re-established.

## Red-first and positive witnesses

A useful check must:

1. fail against the defect or parent population;
2. pass against the candidate;
3. fail again when the claimed property is deliberately mutated;
4. include a same-run positive witness so a dead path cannot satisfy a negative test.

## Root-cause rule

Before editing a shared function:

```text
read the full flow
grep every caller
identify the first failed predicate
fix the shared chokepoint
leave one runnable check
```

Patch the root once, not every reported caller.

## Review and correction

A review returns:

```text
PASS
FIX
BLOCK
UNRUNNABLE
```

Every finding names the exact location, failed property, evidence, severity, minimum correction, and required falsifier. A review finding does not authorize adjacent redesign.

## Human decision packet

Consequential choices should be presented as:

```text
decision required
why now
options
recommended option
evidence
uncertainty
cost and reversibility
what happens after each choice
exact authority requested
```

The decision becomes a durable record, awakens dependent work, and closes only after propagation evidence exists.

## Research promotion

Promote only the implementation-relevant subset:

```text
accepted conclusion
exact research identity
program relevance
dependency
maximum authorized stage
implementation candidate
required evidence
non-claims
```

Do not copy an entire research archive into the program repository.

## Branch strategy

```text
main                 durable accepted truth
message-board        optional permanent coordination pull request
one temporary branch per active assignment
```

Delete temporary branches after merge. Branches are not an archive.

## Release discipline

A release requires an exact frozen tree, all capability gates closed, independent technical and safety review, public claims reconciled to evidence, installation/update/rollback proof, privacy and license review, visible limitations, and a correction policy.

## Quick start

1. Create the program repository.
2. Write the four-document core.
3. Define roles and systems of record.
4. Inventory current capabilities and claims.
5. Turn every claim into an acceptance criterion and falsifier.
6. Freeze one bounded candidate.
7. Implement red-first.
8. Obtain independent review.
9. Run the required operational evidence.
10. Update status and outcomes; do not let chat become the only record.
