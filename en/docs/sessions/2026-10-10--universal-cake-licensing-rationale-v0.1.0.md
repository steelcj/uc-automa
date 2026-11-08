---
title: "Universal Cake Licensing Rationale"
dc:title: "Universal Cake Licensing Rationale"
dc:creator: "Christopher Steel"
dc:subject: "Universal Cake, licensing, AGPL-3.0-or-later, Creative Commons, CC BY-SA 4.0, radar evaluations"
dc:description: "Records why Universal Cake licenses its tools under AGPL-3.0-or-later and its content under Creative Commons, and weighs whether some content should move to CC BY-SA 4.0."
dc:date: "2026-10-10"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:ba50a87f-795b-463d-8bff-702865dd9232"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Universal Cake Licensing Rationale

10 Oct 2026 · @sirhc

## Purpose and scope

Universal Cake licenses its tools under AGPL-3.0-or-later and its content under Creative Commons, so that anything used to vet products and services stays open, inspectable and portable. This document records why, and weighs whether some content should move to Creative Commons Attribution-ShareAlike (CC BY-SA 4.0).

It covers three kinds of work: the tools (code in `uc-radar` and related repositories), the radar evaluations (the Evaluation Metrics document and the placements on the assess, trial, adopt and re-review rings), and the wellbeing documentation. It is a rationale, not legal advice; the license texts themselves govern.

## Current licensing at a glance

Code is AGPL-3.0-or-later and content is Creative Commons, with one exception: the Evaluation Metrics document is currently AGPL-3.0-or-later too.

| Work                        | Examples                                                     | Current license                       | Main reason                                                  |
| --------------------------- | ------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------ |
| Tools                       | `uc-radar`, `uc-cboard`, `universal-cake-themes`, build and scoring scripts | AGPL-3.0-or-later                     | Source stays available even when a tool runs as a hosted service |
| Evaluation Metrics document | the versioned criteria for inclusive design, agency, environment, multilingual support, privacy, security, sovereignty and longevity | AGPL-3.0-or-later                     | Kept with the code that applies it                           |
| Radar evaluations           | per-item write-ups, scores, ring placements                  | Creative Commons (variant to confirm) | Readers can reuse and cite findings freely                   |
| Wellbeing documentation     | guides and procedures aimed at people rather than systems    | Creative Commons (variant to confirm) | Maximum reach, translation and adaptation                    |

Open question: which Creative Commons variant is applied today, CC BY 4.0 or CC BY-SA 4.0? The rest of this document assumes CC BY 4.0 as the baseline.

## Why AGPL-3.0-or-later for tools

The AGPL is chosen because Universal Cake tools are likely to run as web services, and the AGPL is the GPL variant that keeps source available in that case (Free Software Foundation, 2007).

- Network clause. Section 13 requires anyone who modifies the software and offers it to users over a network to give those users the corresponding source. A hosted radar cannot become a closed fork.
- Agency and sovereignty. A client, NGO or municipality that adopts a tool can always obtain, audit, migrate and self-host it, which is the same test the radar applies to other products.
- No lock-in by the practice itself. Vishpala cannot later close the tools on clients either; anyone holding a copy keeps the rights.
- Consistency with the radar. A project that scores vendors on agency and longevity should pass its own criteria.
- Or-later. The "or-later" clause lets the tools move to a future AGPL version without tracking down every contributor.

The main cost is that some organizations have blanket policies against AGPL code. That friction is accepted for the tools, because hosted use is exactly the risk the license addresses.

## Why Creative Commons for content

Content uses Creative Commons rather than the AGPL because CC licenses are written for prose, images and data, while software licenses are written around source code and patents (Creative Commons, n.d.-a).

- Fit. Creative Commons itself recommends against its licenses for software and in favour of FSF or OSI approved licenses, and supports CC for documentation (Creative Commons, n.d.-a). The reverse also holds: AGPL terms such as "corresponding source" map poorly onto a guide or an evaluation.
- Recognition. Government bodies, NGOs and educators already know CC terms, so reuse rarely needs a legal review.
- Version 4.0. The 4.0 licenses are international, cover sui generis database rights alongside copyright, and require reusers to indicate modifications (Creative Commons, n.d.-a). All three matter for evaluations and scored data.
- No endorsement. Reusers may not imply that Universal Cake endorses their use or their version (Creative Commons, n.d.-a).
- Trademarks are separate. CC licenses do not cover the Universal Cake name or marks, so the content can be open while the name stays a signal of origin (Creative Commons, n.d.-a).

## Radar evaluations

The radar's value is that its findings are traceable and reusable, so its license has to protect two things at once: free reuse of the findings, and clarity about which version is Universal Cake's own.

- Facts are not owned. A score, a ring placement or a fact about a product is largely not copyrightable; the license reaches the written analysis, the criteria text and the selection and arrangement of the dataset. Any license choice therefore governs the reasoning more than the numbers.
- Integrity through attribution, not restriction. The 4.0 duty to indicate modifications, plus the no-endorsement rule, means a third party can republish a modified evaluation but cannot present it as the original (Creative Commons, n.d.-a).
- Versioning carries authority. Each evaluation names the metrics version it was scored against, so a fork scored under different criteria is visibly different.
- The metrics document sits between code and content. It is AGPL today so that it travels with the scoring code. If it moves to CC BY-SA 4.0, it can still flow into the GPL family of tools through the one-way BY-SA to GPLv3 compatibility (Creative Commons, 2015), and GPLv3 section 13 allows combination with AGPL code.
- Vendors as readers. Evaluated vendors may quote, rebut or republish an evaluation. A permissive or share-alike CC license allows that openly, which suits a project that wants scrutiny.

## Wellbeing documentation

Wellbeing documentation is the content most likely to be translated, printed, simplified and folded into someone else's materials, so its license should remove barriers for the organizations that serve aging and underserved people.

- Adaptation is the point. Plain-language rewrites, large-print editions, offline copies and translations are all adaptations, and every CC license except the ND variants allows them.
- Receiving organizations vary. Health networks, municipalities and NGOs often publish under their own terms, including CC BY, government open licences or all-rights-reserved. Their ability to absorb a page into a larger handbook decides whether the material reaches people.
- Warranty disclaimer. CC licenses provide material as is (Creative Commons, n.d.-a). Wellbeing pages should still carry their own plain statement that they are not medical or professional advice.
- Withdrawal is not possible. CC licenses cannot be revoked (Creative Commons, n.d.-a), so an outdated procedure stays in circulation. Version dates and a canonical URL are the practical fix.
- Credit removal. An author who does not want to be associated with an adaptation can ask for the credit to be removed (Creative Commons, n.d.-a), which protects the practice from a harmful rewrite carrying its name.

## CC BY-SA for some content: arguments for and against

CC BY-SA 4.0 is the content counterpart of the AGPL's copyleft: anyone may adapt the work, but adaptations they share must stay under BY-SA or a designated compatible license (Creative Commons, n.d.-a). The question is where that guarantee is worth the friction it adds.

### Arguments for

- Improvements stay in the commons. A corrected evaluation or an improved translation cannot be taken private, which mirrors the reason for AGPL on the tools.
- Philosophical consistency. Copyleft on both code and content tells clients the same story about agency and anti lock-in.
- Bridge to the tools. CC BY-SA 4.0 is one-way compatible with GPLv3, so adaptations can be released under GPLv3 when content and code are hard to separate (Creative Commons, 2015). That suits the metrics document and any criteria text embedded in `uc-radar`.
- Commons alignment. Wikipedia and other Wikimedia projects use CC BY-SA, so radar findings or wellbeing material can flow into those articles without a license conflict.
- Defence against enclosure. A consultancy or vendor cannot repackage the radar as a proprietary rating product with private improvements.

### Arguments against

- Friction for small governments and NGOs. Organizations that publish under their own licences, or all rights reserved, often cannot adapt BY-SA material into their own handbooks without relicensing the whole adaptation.
- One-way flow. CC BY material can go into BY-SA works, but BY-SA material cannot go into CC BY works (Creative Commons, n.d.-a). Choosing BY-SA narrows who can build on the content.
- Incompatible with NC. BY-SA adaptations cannot be combined with CC BY-NC material, which is common in education and health.
- Limited reach over facts. Scores and placements are mostly uncopyrightable, so share-alike protects the prose more than the data people most want.
- Collections escape it. Share-alike attaches to adaptations, not to placing an unmodified work beside other material, so a vendor can still quote or bundle an evaluation unchanged.
- Compliance burden on reusers. Reusers must track license chains, which is a real cost for volunteers and translators.

### By content type

| Content                     | Case for BY-SA                                               | Case for BY                                                |
| --------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------- |
| Evaluation Metrics document | Strong: keeps criteria forks open, bridges to GPL-family tools | Weak                                                       |
| Radar evaluations           | Moderate: protects written analysis from private repackaging | Moderate: easier citation and quoting by vendors and press |
| Wellbeing documentation     | Weak: share-alike blocks absorption into partner materials   | Strong: maximum reach to the people the work is for        |

## Options and open questions

The draft lean is a split: share-alike where forks are the risk, permissive where reach is the goal. This is provisional until the licensing owner confirms it.

| Option                    | Metrics document           | Radar evaluations | Wellbeing documentation | Trade-off                                                   |
| ------------------------- | -------------------------- | ----------------- | ----------------------- | ----------------------------------------------------------- |
| A. Split (draft lean)     | CC BY-SA 4.0, or keep AGPL | CC BY-SA 4.0      | CC BY 4.0               | Two content licenses to explain                             |
| B. Share-alike everywhere | CC BY-SA 4.0               | CC BY-SA 4.0      | CC BY-SA 4.0            | Simplest copyleft story, least reach for wellbeing material |
| C. Permissive everywhere  | CC BY 4.0                  | CC BY 4.0         | CC BY 4.0               | Widest reuse, no guard against private repackaging          |

Open questions:

- Which CC variant is on the content today?
- Should the metrics document stay AGPL, move to CC BY-SA 4.0, or be dual licensed?
- Is the scored dataset published separately from the prose, and does it need its own licence, for example CC0?
- Does a trademark notice for the Universal Cake name need to sit beside each license statement?
- Do any current or likely partners have policies that rule out BY-SA or AGPL?

This document is a rationale, not legal advice; a lawyer familiar with Canadian copyright should review the final choice.

## References

Creative Commons. (2015, October 8). *CC BY-SA 4.0 now one-way compatible with GPLv3*. https://creativecommons.org/2015/10/08/cc-by-sa-4-0-now-one-way-compatible-with-gplv3/

Creative Commons. (n.d.-a). *Frequently asked questions*. Retrieved October 10, 2026, from https://creativecommons.org/faq/

Creative Commons. (n.d.-b). *Attribution-ShareAlike 4.0 International legal code*. https://creativecommons.org/licenses/by-sa/4.0/legalcode.en

Free Software Foundation. (2007). *GNU Affero General Public License, version 3*. https://www.gnu.org/licenses/agpl-3.0.html