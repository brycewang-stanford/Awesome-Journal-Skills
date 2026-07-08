# IEEE S&P Reproducibility Code Adapter

This directory points S&P authors to the repo-level ML/CS-conference
reproducibility kit. It is **not** the economics Stata/DiD/IV/RDD code
library; it is a lightweight artifact/reproducibility scaffold, wrapped here
with the checks that are specific to security papers.

## Shared kit

- [`../../../shared-resources/ml-conference-methods/README.md`](../../../shared-resources/ml-conference-methods/README.md)
- [`../../../shared-resources/ml-conference-methods/experiment-matrix.md`](../../../shared-resources/ml-conference-methods/experiment-matrix.md)
- [`../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md`](../../../shared-resources/ml-conference-methods/reproducibility-artifact-checklist.md)
- [`../../../shared-resources/ml-conference-methods/code/check_repro_package.py`](../../../shared-resources/ml-conference-methods/code/check_repro_package.py)

## Typical use

```bash
python3 ../../../shared-resources/ml-conference-methods/code/check_repro_package.py /path/to/anonymous-artifact
```

Use the script as a smoke check only — it confirms the package has an entry
point, pinned dependencies, and no obvious identity leaks. It does **not**
make the S&P-specific judgments below.

## What the generic tool cannot check (do these by hand)

Security artifacts fail on axes a generic ML checker never looks at. Before
relying on the smoke check, walk the S&P-specific list:

1. **Target snapshot.** Is the attacked software/hardware pinned to an exact
   version, build, distro, patch level, and — for microarchitectural work —
   CPU model, stepping, and microcode? (`ieeesp-reproducibility`)
2. **World-dependence.** Does any result depend on a live third-party system
   that may have changed? If so, is a dated snapshot or archived trace
   included, and is the dependence stated in the paper?
3. **Disclosure timing.** Does releasing this artifact conflict with an open
   responsible-disclosure clock? An artifact must not out-run the fix.
   (`ieeesp-artifact-evaluation`)
4. **Dangerous-material handling.** Exploits gated/stubbed where appropriate;
   malware shipped as hashes + retrieval path or password-protected with a
   warning; vulnerable targets containerized so an evaluator cannot expose
   them; no requirement to scan/attack outside infrastructure.
5. **Ethics coverage.** Any dataset in the deposit is within what the paper's
   ethics record and IRB determination cover — the deposit is public forever.
6. **Badge honesty.** The claimed badge (Available / Functional / Results
   Reproduced) matches what an outsider can actually regenerate, with a
   claim → command → expected-output → runtime table in the README.

Venue-specific policy still comes from
[`../official-source-map.md`](../official-source-map.md), the current official
CFP and artifact-evaluation pages, and the S&P skills for experiments,
reproducibility, artifact evaluation, and submission.
