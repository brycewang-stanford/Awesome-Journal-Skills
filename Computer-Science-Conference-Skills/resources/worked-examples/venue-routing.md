# Worked Routing Examples

These are fictional routing scenarios for conference selection. They are not
real submissions and do not encode current-year CFP facts.

## Case 1: Foundation Model Method With Systems Bottleneck

Manuscript: a new training method improves sample efficiency but the strongest
evidence is throughput, memory use, and distributed implementation.

Route:
- Start with NeurIPS/ICML/ICLR only if the learning contribution is central and
  baselines/ablations are strong.
- Test MLSys if the system design, training infrastructure, or deployment
  efficiency is the contribution.
- Test systems venues only when the work is a general systems result rather than
  an ML paper with engineering details.

## Case 2: Vision Benchmark Versus Model Paper

Manuscript: a dataset and benchmark for long-tail visual recognition with a
moderate baseline model.

Route:
- CVPR/ICCV/ECCV require a vision contribution with evidence beyond dataset
  release.
- If the dataset is the product, emphasize benchmark design, annotation
  quality, task definition, and evaluation protocol.
- If the method is weak, route to a dataset/benchmark track only when the
  current CFP supports it.

## Case 3: NLP Resource Or Empirical Finding

Manuscript: a multilingual corpus plus analysis of model failures.

Route:
- ACL/EMNLP/NAACL/EACL depend on whether the contribution is core NLP method,
  empirical analysis, resource construction, or regional/community fit.
- LREC-COLING may fit language-resource contributions when corpus design and
  documentation are stronger than model novelty.
- SIGDIAL/INLG/*SEM fit narrower dialogue, generation, or semantics questions.

## Case 4: Security System With Human Study

Manuscript: a phishing-defense tool evaluated through deployment logs and a
small user study.

Route:
- Security venues need a threat model, attack/defense clarity, ethics, and
  reproducible evidence.
- CHI/CSCW may fit if the human behavior and intervention design are the
  contribution.
- Do not hide the security claim inside HCI framing or the human-study claim
  inside security framing; pick the reviewer community that evaluates the main
  novelty.

## Case 5: Software Engineering Tool

Manuscript: a static-analysis tool finds API-migration bugs in real projects.

Route:
- SANER fits analysis/evolution/reengineering value.
- ICSME fits maintenance and evolution decisions over repository histories.
- ISSTA fits testing and program-analysis evidence around defect detection or
  test generation.
- ICSE/FSE/ASE require broader software-engineering contribution or automation
  reach.
