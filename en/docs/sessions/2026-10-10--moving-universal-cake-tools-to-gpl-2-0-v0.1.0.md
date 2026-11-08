---
title: "Moving Universal Cake Tools to GPL-2.0"
dc:title: "Moving Universal Cake Tools to GPL-2.0"
dc:creator: "Christopher Steel"
dc:subject: "Universal Cake, licensing, AGPL-3.0-or-later, GPL-2.0, GPL-3.0-or-later, CC BY-SA 4.0"
dc:description: "Weighs moving the Universal Cake tools from AGPL-3.0-or-later to GPL-2.0, and reaches a provisional conclusion: keep AGPL-3.0-or-later for anything run as a service, and consider GPL-3.0-or-later, not GPL-2.0, for tools only distributed and run locally."
dc:date: "2026-10-10"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:23530f44-00ea-4341-90bf-7f4dbdf6c8d5"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Moving Universal Cake Tools to GPL-2.0

10 Oct 2026 · @sirhc

## Summary

Moving the Universal Cake tools from AGPL-3.0-or-later to GPL-2.0 would make them easier for cautious organizations to adopt, but it would remove the protection that matters most for a hosted radar: the right of network users to get the source. GPL-2.0 also lacks an explicit patent grant, is not compatible with Apache-2.0 code, and breaks the CC BY-SA 4.0 bridge that runs only to GPLv3.

The draft conclusion is to keep AGPL-3.0-or-later for anything run as a service, and to consider GPL-3.0-or-later, not GPL-2.0, for tools that are only ever distributed and run locally. This stays provisional until the licensing owner confirms it.

## What would change

The biggest difference is the network clause; most of the others follow from GPLv3 being written 16 years after GPLv2.

| Term                                                         | AGPL-3.0-or-later (current)   | GPL-2.0-only           | GPL-2.0-or-later        |
| ------------------------------------------------------------ | ----------------------------- | ---------------------- | ----------------------- |
| Published                                                    | 2007                          | 1991                   | 1991                    |
| Source owed to network users of a modified version           | Yes, section 13               | No                     | No                      |
| Source owed when copies are distributed                      | Yes                           | Yes                    | Yes                     |
| Explicit patent licence from contributors                    | Yes                           | No, implied at best    | No, implied at best     |
| Anti-tivoization (installation information for consumer devices) | Yes                           | No                     | No                      |
| Cure period after a violation                                | Yes, 30 and 60 day provisions | No, rights end at once | No, rights end at once  |
| Can move to a future licence version                         | Yes                           | No                     | Yes, to GPLv3 and later |
| Combinable with GPLv3 or AGPLv3 code                         | Yes                           | No                     | Yes, by choosing v3     |
| Combinable with Apache-2.0 code                              | Yes                           | No, in the FSF's view  | Yes, by choosing v3     |

## Advantages of GPL-2.0

The case for GPL-2.0 is mostly about adoption and simplicity, not stronger protection.

- Fewer policy blocks. Many companies and some public bodies ban AGPL code outright but allow GPL-2.0, so procurement and IT reviews get shorter.
- Lighter duties for clients who host. A municipality or NGO that modifies a tool and runs it internally or on a public site would owe source only if it distributed copies, not to every visitor.
- Familiarity. GPL-2.0 is the licence of the Linux kernel and has decades of case history and community practice behind it.
- Shorter text. GPL-2.0 is about half the length of AGPLv3 and easier to explain to a non-specialist client.
- Fixed terms (GPL-2.0-only). No future licence version can change what contributors agreed to, which is the reason Linus Torvalds keeps the kernel on version 2 only.
- Kernel and embedded alignment. Code that might one day be shared with GPL-2.0-only projects, such as kernel modules or some embedded firmware, can be combined directly.

## Disadvantages of GPL-2.0

The main cost is that a hosted fork could stay closed, which is the exact risk the AGPL was chosen to prevent.

- The network gap. A vendor or consultancy could modify `uc-radar`, run it as a paid rating service and never publish its changes. GPL-2.0 is triggered by distributing copies, not by serving users.
- No explicit patent grant. Contributors do not expressly licence their patents, and there is no patent retaliation clause, so downstream users of a tool have weaker protection.
- Harsh termination. Any violation ends a licensee's rights immediately, with no cure period, which is a poor fit for small organizations that make honest mistakes.
- No anti-tivoization. A device maker could ship a modified tool on locked hardware that users cannot update, which works against agency and longevity.
- Compatibility losses. GPL-2.0-only cannot be combined with GPLv3, AGPLv3 or Apache-2.0 code, which rules out a large share of modern libraries (Apache Software Foundation, n.d.).
- Dated wording. GPLv2 was written around US concepts like "distribution"; GPLv3 uses "convey" and "propagate" to work more evenly across jurisdictions, including Canada.
- Mixed signals. A practice that scores vendors on sovereignty would be choosing a weaker copyleft for its own hosted tools.

## Compatibility

GPL-2.0-only is the most isolated option here: it combines with GPL-2.0 and permissive code, but not with any version 3 licence, Apache-2.0 or CC BY-SA content.

| Other licence        | With AGPL-3.0-or-later | With GPL-2.0-only | With GPL-2.0-or-later  |
| -------------------- | ---------------------- | ----------------- | ---------------------- |
| MIT, BSD             | Yes                    | Yes               | Yes                    |
| Apache-2.0           | Yes                    | No, per the FSF   | Yes, if released as v3 |
| GPL-2.0-only         | No                     | Yes               | Yes, as v2             |
| GPL-3.0              | Yes, via section 13    | No                | Yes, as v3             |
| CC BY-SA 4.0 content | Yes, via GPLv3         | No                | Yes, as v3             |

The FSF has never accepted Apache-2.0 as compatible with GPLv2, because of Apache's patent termination and indemnification terms, while Apache-2.0 code can go into GPLv3 works (Apache Software Foundation, n.d.). CC BY-SA 4.0 is one-way compatible with GPLv3 only (Creative Commons, 2015), so the content-to-code bridge in the licensing rationale would not survive a GPL-2.0-only move.

## Against the Universal Cake metrics

Scored against its own criteria, GPL-2.0 does slightly better on ease of adoption and worse on agency, sovereignty, privacy and longevity. The ratings below are a qualitative draft, not a formal radar evaluation.

| Criterion                          | AGPL-3.0-or-later | GPL-2.0  | Why                                                          |
| ---------------------------------- | ----------------- | -------- | ------------------------------------------------------------ |
| Agency                             | Stronger          | Weaker   | Users of a hosted fork keep the right to its source only under AGPL |
| Sovereignty                        | Stronger          | Weaker   | Clients can always take a hosted tool in house only if its source is owed |
| Privacy                            | Stronger          | Weaker   | Users can audit what a hosted fork does with their data only if they get the source |
| Security                           | Stronger          | Weaker   | Explicit patent terms and source for hosted forks support independent review |
| Longevity                          | Stronger          | Mixed    | Or-later allows upgrades; GPL-2.0-only freezes terms but also blocks v3 libraries |
| Inclusive design                   | Neutral           | Neutral  | Licence choice does not change accessibility directly        |
| Multilingual support               | Neutral           | Neutral  | Both allow translation of interfaces and docs                |
| Environment                        | Neutral           | Neutral  | No direct effect                                             |
| Adoption by cautious organizations | Weaker            | Stronger | AGPL bans are common in corporate policy                     |

## Relicensing in practice

A change is only possible for code whose copyright holders all agree, and it never takes back copies already released under AGPL.

- Sole authorship. Code written only by the practice can be relicensed by the practice at any time.
- Outside contributions. Every external contributor must agree, unless they signed a contributor agreement allowing it. Without that, their code stays AGPL and must be rewritten or removed.
- AGPL dependencies. Any AGPL or GPLv3 library a tool depends on must be replaced, because GPL-2.0-only cannot include it.
- Existing releases stay AGPL. Anyone holding an AGPL copy can keep using and forking it under AGPL; only new versions change.
- Repository hygiene. Each repository needs updated `LICENSE` files, SPDX identifiers in file headers, licence statements in the documentation front matter, and a changelog entry.

## Options and open questions

If the goal is easier adoption, GPL-3.0-or-later for locally run tools gets most of that benefit without giving up patent terms or compatibility; GPL-2.0 is hard to justify unless a tool must combine with GPL-2.0-only code.

| Option                 | Network protection | Adoption | Compatibility | Fits when                                                    |
| ---------------------- | ------------------ | -------- | ------------- | ------------------------------------------------------------ |
| Keep AGPL-3.0-or-later | Yes                | Lowest   | Broad         | Tools run as hosted services, such as the radar site         |
| GPL-3.0-or-later       | No                 | Higher   | Broad         | Command-line and build tools only run locally                |
| GPL-2.0-or-later       | No                 | Higher   | Broad, via v3 | Code that may be shared with both v2-only and v3 projects    |
| GPL-2.0-only           | No                 | Higher   | Narrow        | Code that must link with the Linux kernel or other v2-only projects |
| Dual AGPL plus GPL-2.0 | Reuser's choice    | Highest  | Broad         | Rarely worth it; reusers pick the weaker licence             |

Open questions:

- Which tools run as hosted services, and which are only distributed?
- Has any outside contributor's code been merged that would need consent?
- Does any tool need to combine with GPL-2.0-only code today?
- Have specific clients or partners raised AGPL as a blocker?

This is a rationale, not legal advice; a lawyer familiar with Canadian copyright should review any change.

## References

Apache Software Foundation. (n.d.). *Apache License v2.0 and GPL compatibility*. Retrieved October 10, 2026, from https://www.apache.org/licenses/GPL-compatibility.html

Creative Commons. (2015, October 8). *CC BY-SA 4.0 now one-way compatible with GPLv3*. https://creativecommons.org/2015/10/08/cc-by-sa-4-0-now-one-way-compatible-with-gplv3/

Free Software Foundation. (1991). *GNU General Public License, version 2*. https://www.gnu.org/licenses/old-licenses/gpl-2.0.html

Free Software Foundation. (2007). *GNU Affero General Public License, version 3*. https://www.gnu.org/licenses/agpl-3.0.html