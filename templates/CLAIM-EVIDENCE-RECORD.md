# Claim / Evidence Record

```yaml
claim_id:
claim:
claim_class:
scope:
population:
product_sha:
harness_sha:
fixture_or_corpus:
environment:
model_or_runtime:
evaluator:
method:
positive_witness:
negative_or_adversarial_witness:
result:
limitations:
independent_disposition:
supersedes:
public_evidence:
```

Rules:

- `UNKNOWN` is valid.
- Test presence is not test execution.
- A changed load-bearing identity invalidates prior proof.
- Negative tests require same-run positive witnesses.
- The author does not supply the sole consequential disposition.
