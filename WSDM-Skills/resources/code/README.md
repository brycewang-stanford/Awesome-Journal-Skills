# WSDM Code Adapter (shared ML reproducibility kit)

The WSDM pack does not carry its own experiment tooling; it borrows the
repository-level kit shared by the ML/data-mining conference packs. What lives
here is only the pointer plus the WSDM-shaped caveats. (Authors coming from the
economics journal packs: the Stata/DiD/IV/RDD library is deliberately *not*
referenced here - wrong toolchain for log-driven mining work.)

## Where the kit lives

| Piece | Path |
| --- | --- |
| Kit overview | [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md) |
| Experiment matrix template | [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md) |
| Artifact checklist | [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md) |
| Package smoke checker | [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py) |

```bash
# run the structural smoke check on the anonymous repo before the PDF cites it
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anon-artifact
```

## Reading the kit through WSDM eyes

1. Ignore any kit guidance that assumes an uncounted appendix or a separate
   supplement upload; at WSDM the appendices sit inside the page cap and the
   cited repository is the overflow container
   (`../../skills/wsdm-supplementary/SKILL.md`).
2. Extend the generic artifact checklist with the behavioral-data items it
   lacks: temporal split manifest, logging-policy/bias-model statement, and
   per-stage filter counts (`../../skills/wsdm-reproducibility/SKILL.md`).
3. The smoke checker confirms structure only. Anything policy-flavored -
   deadlines, page budgets, anonymity wording - comes from the current CFP via
   [`../official-source-map.md`](../official-source-map.md), never from tooling.
