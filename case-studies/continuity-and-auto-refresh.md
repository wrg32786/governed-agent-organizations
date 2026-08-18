# Case Study: Continuity Is a Transaction

**Status:** bounded Auto-Refresh transport result demonstrated; no 20-cycle or fleet claim.

## Public product identity

```text
transport public commit  4b207ed725d54c01c9fdad066c1762f285326af0
transport public tree    f51e935770ddef47eb2eb1577de7c91e25f4ab89
one-command implementation pin  81dd47d3215df0aedb73a378601be431defc7d2f
one-command pin tree            11a04056e6ffbf79447257e06ad2ec2bcd12f962
current public commit    41051d9e544063309d3b69462aecb7aa4edbe149
current public tree      daf2a7e4a7b068b17e9da28377fefaaef1b78a44
```

The one-command implementation pin contains the same managed Auto-Refresh transport plus the later one-command installer and launcher wiring. The current public commit differs from that pin by documentation-only changes (public PR #40), so the evidence claim is unchanged.

## Failure-derived lesson

A long-running terminal agent can appear to resume while the complete continuity property is still false.

Development exposed these classes:

- a control string was written to a pseudo-terminal but never became a submitted prompt;
- a capsule existed but its acknowledgement was not observed;
- a clear occurred but current-session identity came from stale historical state;
- a new session existed but no material prior work continued;
- a successful transport leg was mistaken for complete continuity;
- operator input could interleave with automated command text;
- changed implementation invalidated earlier proof;
- an observation harness could fail its own bookkeeping while the transport continued working.

```text
physical write != submitted command
capsule != current identity
new session != re-grounded session
wake != material continuation
green screen != evidence
harness failure != product failure
```

## Transaction model

```text
1. boundary condition
2. capsule request
3. actual prompt-submission witness
4. capsule completion acknowledgement
5. exactly one clear
6. fresh session identity
7. current-state re-grounding
8. exactly one wake/resume submission
9. material continuation of the prior objective
10. terminal evidence record
```

A missing leg produces a named partial result, not `PASS`.

## Safety rule

```text
no capsule acknowledgement -> no clear
one valid acknowledgement -> exactly one clear
```

Busy output is not a readiness veto. Command text and a protected, separate Enter use the terminal application's native queued-prompt path.

## Observed population

One Windows reference seat ran an unchanged reviewed release snapshot with an intentionally low context-pressure threshold so refreshes occurred quickly.

Across **11 of 11 observed Auto-Refresh transport transactions**:

- three transactions occurred during setup;
- eight occurred after the test objective began;
- each produced one capsule request;
- each produced one completion acknowledgement;
- each produced one clear;
- each produced one fresh session-start identity;
- zero acknowledgements were stranded;
- zero duplicate clears occurred;
- the prior busy-output abort did not recur;
- the prior partial-line/skipped-byte acknowledgement defect did not recur.

The accelerated test then stopped for a different reason. Inside one unchanged session, the model appended multiple remaining synthetic witness rows and declared the test complete without corresponding refreshes. That was a seat-side instruction and observation-harness failure, not a failed refresh transaction.

## Disposition

```text
Auto-Refresh transport at the reviewed release snapshot  PASS
observed transport transactions                           11 / 11
planned synthetic 20-cycle bookkeeping                    NOT ESTABLISHED
fleet reliability                                         NOT CLAIMED
```

Maximum supported statement:

> One Windows reference seat completed 11 of 11 observed Auto-Refresh transport transactions at the reviewed release snapshot, each with one capsule request, one acknowledgement, one clear, and one fresh session identity, with zero stranded acknowledgements and zero duplicate clears.

This result does not establish fleet reliability, universal platform behavior, implemented Studio or Domain Engines, a runnable reference corporation, or business outcomes.

## Public evidence boundary

The public product repository contains the transport and resume implementation, direct and discovery-based tests, a supported one-command managed install, and documentation of the bounded result.

Detailed raw event logs, private test identities, and internal review records are not published in this edition. Their absence limits public reproducibility and blocks any broader interpretation.
