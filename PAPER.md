# Governed Agent Organizations

## Persistent identity, context continuity, human authority, and evidence-bounded improvement

**Edition:** Paper v1 - architecture and research synthesis  
**Evidence cutoff:** 2026-08-16  
**Status:** Paper v1 public edition; public release approved by the principal on 2026-08-18

## Abstract

Language models can generate plans, code, analysis, and text, but those abilities alone do not create an organization. A durable organization needs identity that survives model and session changes, working context that is not confused with institutional memory, authority that cannot be inferred from conversation, independent evaluation, explicit ownership and closure, and outcomes that are not reduced to agent activity.

This paper proposes a governed architecture for persistent AI agent organizations. Its contribution is not a single new memory algorithm, context method, orchestration framework, or optimization technique. It is a system of non-substitutable layers and explicit transitions joining persistent identity, active working context, inspectable institutional memory, human authority, evidence-bounded improvement, organizational coordination, domain engines, and outcome discipline.

The architecture is presented as six falsifiable hypotheses rather than a universal novelty claim. Existing prior art supplies important components. This work asks how those components can be combined without turning context into truth, signatures into authority, candidates into active behavior, or activity into outcomes.

A public reference implementation of managed context refresh is available in `wrg32786/aigent-os` at commit `81dd47d3215df0aedb73a378601be431defc7d2f`. One bounded release population observed 11 of 11 transport transactions on one Windows reference seat, with one capsule request, one acknowledgement, one clear, and one fresh session identity per transaction; zero acknowledgements were stranded and zero duplicate clears occurred. This does not establish 20-cycle bookkeeping, fleet reliability, universal platform behavior, implemented organizational products, or business outcomes.

## 1. Problem and contribution

Capable models do not, by themselves, constitute durable workers or organizations. A production agent system must preserve several different kinds of state and authority across model swaps, context boundaries, process failures, changing evidence, and human decisions.

The central claim of this paper is a governed-integration hypothesis:

```text
AgentIdentity != ModelProfile != RuntimeBinding != AuthorityGrant
WorkingContext != InstitutionalMemory
Message != DecisionRecord
Signature != Permission
Candidate != ActivatedCapability
Activity != Outcome
```

The contribution is the refusal to collapse those layers, plus explicit transitions that can fail honestly and be independently reviewed.

### What is not claimed as original

This paper does not claim invention of externalized context, memory retrieval, agent workflows, tool protocols, multi-agent collaboration, skill optimization, event-sourced sessions, or plugin composition. Prior work supplies each of those mechanisms. The proposed contribution is the governed combination and its non-substitution rules.

### Evidence vocabulary

Material statements are typed as one of:

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

The following substitutions are prohibited:

```text
paper result != local result
code present != capability working
test file != executed test
research accepted != implementation
one run != reliability
agent activity != organizational performance
publish event != business outcome
```

## 2. Six falsifiable hypotheses

### H1 - Layer Non-Substitution

Identity, runtime binding, authority, working context, institutional memory, evidence, and outcome are distinct layers. Collapsing any pair is expected to create a predictable failure class.

Examples:

- model selection silently changes privacy or authority;
- a stale checkpoint is treated as current organizational truth;
- a signed message is treated as permission;
- an accepted research result is treated as installed behavior;
- a publish event is treated as a business outcome.

### H2 - Continuity Transaction

Continuity is not a checkpoint file or a successful-looking screen. It is a complete transaction:

```text
capture requested
-> request submitted
-> durable state acknowledged
-> boundary crossed exactly once
-> fresh identity observed
-> prior state re-grounded
-> wake submitted exactly once
-> material work continues
-> transaction closes with evidence
```

Partial transport is not continuity. A pseudo-terminal write is not necessarily a submitted command. A new session is not necessarily a re-grounded session.

A comparative prediction follows from the architecture: discrete capsules plus a fresh-session boundary may reduce cumulative semantic drift relative to repeated summary-of-summary consolidation over many context boundaries. This is a hypothesis, not an empirical superiority claim. DeepSeek Harness retains its complete append-only event log even when its model-visible surface is compacted; that durable log must not be described as lost.

### H3 - Governed Improvement

Safe improvement requires separate state and authority for:

```text
candidate generation
exact artifact identity
execution environment
independent evaluation
promotion decision
serving scope
outcome measurement
rollback or retirement
```

A skill, harness, engine, evaluator, or organizational change cannot approve itself merely because it improved its own metric.

### H4 - Durable Human Gate

Consequential control cannot reliably exist only as chat, an interrupt, a notification, or an approval button. It requires canonical decision objects, authority basis, options, evidence, a durable decision record, propagation, and closure evidence.

A decision is incomplete until dependent work has resumed, changed, delegated, deferred, cancelled, or closed.

### H5 - Honest-Terminal Completeness

Systems that cannot terminate honestly as:

```text
UNRUNNABLE
NO_DATA
NO_IMPROVEMENT
HOLD
REJECT
ROLLBACK
```

are structurally biased toward manufacturing progress.

### H6 - Research-to-Learning Closure

Research affects an agent organization only through a complete evidence chain:

```text
source
-> claim
-> independent disposition
-> retrieval at the relevant task moment
-> bounded use
-> learning candidate
-> pre-registered evaluation
-> approved serving
-> measured outcome
-> retain, revise, retire, or rollback
```

A report stored in memory is not learning. Retrieval is not use. Use is not improvement.

## 3. Architecture

### 3.1 Persistent identity

Agent identity belongs outside the current model and session. A model is a runtime binding, not an employee, role, or permission grant. Model changes must preserve identity, mission, memory references, and authority scope, or refuse loudly.

### 3.2 Active working context

Programmatic context methods may hold source bundles, parsed artifacts, indexes, intermediate results, and child-agent handles. This state is useful but transient and non-authoritative.

### 3.3 Institutional memory

Institutional memory should remain inspectable, versioned, provenance-bearing, and separable from retrieval accelerators. Summaries and capsules are bounded state carriers, not universal truth. Current operational facts still require current reads from authoritative systems.

A durable capsule trail has different properties from recursive compaction:

- each capsule remains a separate historical artifact;
- later work can identify when a belief first appeared or was superseded;
- current identity does not come from capsule text;
- live re-grounding can reject stale claims;
- retrieval can search the historical trail with provenance and time.

This does not make capsules automatically accurate. A capsule can omit facts, contain stale assumptions, or carry malicious data. It must be framed as historical evidence, not authority.

### 3.4 Authority

Consequential tools and organizational changes require pre-action authority. Post-action warnings are telemetry, not control. Agent identity, model capability, source authenticity, and action permission remain distinct.

### 3.5 Evidence and evaluation

A green result is evidence only when:

- the population is named;
- exact code, harness, environment, and artifacts are frozen;
- the check can turn red for the intended reason;
- negative tests have same-run positive witnesses;
- the maker is not the sole checker;
- changed identities invalidate prior proof unless the change is outside the proof surface.

### 3.6 Organizational coordination

Messages are not obligations. Findings are not automatically work. Work requires an authority basis, owner, closure condition, evidence requirement, and reopen path. Organizational truth belongs in canonical objects rather than reconstructed chat.

### 3.7 Domain engines

Business-function engines should be inspectable packages with explicit objects, events, integrations, source-of-truth maps, authority matrices, privacy rules, budgets, evaluation profiles, and rollback hooks. Generated candidates cannot grant themselves data, credentials, budget, or activation.

### 3.8 Operator interface

The primary human surface should answer:

```text
What needs me?
Why?
What is blocked?
What is still moving?
What evidence supports the recommendation?
What changes if I decide?
Did dependent work actually resume?
```

The interface is a view over canonical state. Visual green cannot substitute for freshness, completeness, reconciliation, or authority.

## 4. Related work and architectural disposition

The source registry records exact pins, licenses or citation-only terms, inspection level, supported claim, and limitations.

| Mechanism | Representative source | Disposition | Boundary retained here |
|---|---|---|---|
| Working-context externalization | Recursive Language Models | ADAPT | Working context is not institutional memory or authority |
| Virtual/tiered context | MemGPT | WATCH/ADAPT | Context management does not create organizational truth |
| Memory, reflection, planning | Generative Agents; Reflexion; ExpeL; Agent Workflow Memory | ADAPT | Retrieved experience remains evidence, not active authority |
| Skill optimization | SkillOpt | ADAPT proposal-only | A candidate cannot activate itself |
| Continual harness refinement | Continual Harness | ADAPT research claims | Optimizer and evaluator remain separate |
| Signed-event collaboration | Buzz | INTEROPERATE | Signature is not authority |
| Tool/context protocol | MCP | ADAPT | The application retains policy and scope authority |
| Agent-user event transport | AG-UI | INTEROPERATE | Transport does not grant action authority |
| Agent-agent protocol | A2A | WATCH | Discovery/task exchange is not decision truth |
| Minimal agent runtime | Pi agent core; Prime Agent | ADAPT selected seams | Runtime binding does not own identity or authority |
| Same-session event-sourced runtime and compaction | DeepSeek Harness | INTEROPERATE/ADAPT | Complete log is durable; model-visible recursive summary remains a distinct tradeoff |
| Dynamic component composition | Cordis and its preprint | ADAPT/CITE/WATCH | Reversible runtime effects are not organizational rollback or authority |
| Multi-agent software organizations | MetaGPT; ChatDev | WATCH | Role-play and software benchmarks do not establish governed organizations |
| Kernel-style agent services | AIOS | WATCH/ADAPT | Service composition remains below the governance boundary |

### DeepSeek Harness and Cordis

DeepSeek Harness is a substantial plugin-composed, event-sourced agent runtime. It includes session persistence, goals, plans, tools, permissions, sandboxes, workflows, subagents, skills, and automatic same-session compaction. Cordis provides the underlying service/event/effect composition model.

The architectural lesson is not to rebuild a generic harness blindly. A governed organization can treat DeepSeek Harness, Claude Code, Codex, or another runtime as a `RuntimeBinding`. Identity, authority, institutional memory, accepted evidence, obligations, and outcomes remain outside the replaceable runtime.

Cordis runtime effects can be reversible. Organizational actions often are not. A plugin can unregister a tool; it cannot retroactively undo a payment, revoke a settled decision, or reconcile an external system of record.

## 5. Context continuity reference implementation

The public `aigent-os` repository ships a managed context-refresh path at commit `81dd47d3215df0aedb73a378601be431defc7d2f`.

The intended sequence is:

```text
context pressure rises
-> request one capsule
-> observe one exact acknowledgement
-> submit one clear
-> observe a fresh session identity
-> submit one resume wake
-> load prior work
-> re-ground against live state
-> continue the objective
```

The safety invariant is:

```text
no acknowledgement -> no clear
one valid acknowledgement -> exactly one clear
```

The implementation writes slash-command text and Enter separately so the terminal application can use its native prompt queue. Busy or idle output is not a readiness veto after the acknowledgement.

### Bounded live result

A reviewed release population on one Windows reference seat produced 11 of 11 observed transport transactions. Each transaction had one capsule request, one acknowledgement, one clear, and one fresh session identity. No acknowledgement was stranded and no duplicate clear occurred.

The accelerated observation protocol later failed its own bookkeeping inside one unchanged session. That failure is not counted as a failed refresh transaction, but it prevents a 20-of-20 claim.

The maximum supported statement is:

> One Windows reference seat completed 11 of 11 observed Auto-Refresh transport transactions at the reviewed release snapshot, each with one capsule request, one acknowledgement, one clear, and one fresh session identity, with zero stranded acknowledgements and zero duplicate clears.

The result does not establish fleet reliability, universal platform behavior, or a completed empirical evaluation of material continuation across every cycle. The sanitized case study records the exact public product identity and the evidence boundary.

## 6. Governance and safety

### 6.1 Non-self-activation

Candidate generation, evaluation, promotion, installation, serving authority, and outcome measurement are separate transitions. Research acceptance or a green test cannot grant production authority.

### 6.2 Business-space isolation

Memory, credentials, integrations, budgets, and customer or financial state must not silently cross organizational scopes. Cross-scope access requires explicit authority and a target contract.

### 6.3 Prompt and memory trust

Persisted text is data, not instruction. A safe renderer should quote, bound, and place untrusted content after policy fences. Semantic influence remains possible even after structural escaping, so provenance and live re-grounding are still required.

### 6.4 External systems of record

Local memory is not automatically authoritative for customers, accounting, publishing, advertising, contracts, payments, analytics, source code, or live program state.

### 6.5 Human authority

Humans remain authoritative for consequential activation, publication, finance and capital, credentials, budgets, privacy destinations, cross-scope access, organizational policy, and acceptance of material risk.

## 7. Evidence maturity

### Demonstrated

- a bounded managed Auto-Refresh transport population on one Windows reference seat;
- public product code and direct test coverage for managed refresh;
- a one-command supported install path for the managed runner.

### Repository-observed or test-covered

- deterministic capsule selection and resume rendering;
- current-session identity supplied by the fresh session-start event rather than historical capsule text;
- protected two-part terminal command submission;
- explicit non-claims and failure terminals;
- reusable program-control artifacts in this repository.

### Proposed or held

- a new general kernel substrate;
- a full operator Studio;
- generated Domain Engines;
- a runnable reference corporation;
- automated evidence-backed self-improvement;
- broad fleet conformance.

### Unknown or unestablished

- 20 consecutive independently verified cycles;
- fleet reliability;
- universal platform reliability;
- lower operator burden;
- improved revenue, retention, customer, or financial outcomes;
- empirical superiority of fresh-session capsules over recursive compaction.

## 8. Evaluation program

A credible evaluation separates:

1. continuity and refresh;
2. memory retrieval and temporal truth;
3. prompt and authority boundaries;
4. skill and harness improvement;
5. evaluator integrity;
6. model/runtime swaps;
7. agent coordination and obligations;
8. operator comprehension and burden;
9. privacy and business-space isolation;
10. customer, financial, and business outcomes.

No opaque composite score may average away authority, privacy, stale-state, rollback, or business-outcome failure.

A future comparison of recursive compaction and fresh-session capsules should hold the task and model population constant, inject exact facts, later corrections, uncertainty, and stale decisions, then score retention, provenance, stale-fact rejection, next-action accuracy, and token cost over many boundaries.

## 9. Limitations and non-claims

This paper does not establish:

- novelty priority for every hypothesis;
- 20-cycle or fleet reliability;
- universal prompt-injection resistance;
- safe autonomous self-improvement;
- implemented multi-business isolation;
- an implemented operator cockpit;
- implemented Domain Engines;
- a runnable reference corporation;
- lower operator burden;
- improved business outcomes.

The detailed raw operating evidence for the bounded live result is not published in this edition. The public claim is limited to the sanitized extract and publicly inspectable product identity. The absence of raw private evidence is a limitation, not permission to infer a broader result.

The Cordis preprint has no reuse license identified at the pinned repository state. It is cited and paraphrased only; no prose, figures, diagrams, pages, or code are reproduced.

## 10. Conclusion

Capable agents do not become organizations by adding more context, memory, tools, agents, or autonomy. They become organizations only when persistent identity, inspectable institutional memory, authority, independent evaluation, obligations, rollback, and outcomes are joined by explicit, falsifiable transitions.

The contribution claimed here is a governed integration and a set of failure-derived hypotheses. Novelty priority remains unproven. A bounded context-refresh transport result exists, while repeated reliability, broad implementation, organizational performance, and business outcomes remain open empirical questions.
