---
title: "Decision: A Check Exits 2 When Not Ready"
dc:title: "Decision: A Check Exits 2 When Not Ready"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "OSAT managers, exit status, check, baseline, inter-manager interface"
dc:description: "Every OSAT manager that offers a check exits 0 when ready, 2 when not ready, and 1 when the check could not run, so another manager or a script can tell a gap from a failure."
dc:date: "2026-10-21"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:670760b6-2e8e-4dfd-9aa2-00b2369fcbb4"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: A Check Exits 2 When Not Ready

Version: 0.1.0
Status: Accepted, on merge of the pull request that introduces it

## Context

manage-git's `--check` tells other managers whether git meets its baseline. A caller has to tell two outcomes apart: the tool is there but not ready, which the caller can fix, for example by installing a version, and the check itself failed, which it cannot. Exit status 1 already means a refused or failed command in every OSAT manager. Christopher Steel agreed on 2026-10-21 that 2 should mean "not ready", and osat-manager-git decision 0002 proposed it for every manager.

## Decision

- An OSAT manager that offers a check, such as `--check`, exits **0** when what it checks is ready, **2** when it is not ready, and **1** when the check could not run.
- Every other command keeps 0 for success and 1 for anything refused or failed.
- A check that also prints JSON reports the same outcome in it, as `"ready": true` or `false`, so a caller can use either.

## Consequences

- *Creating an OSAT Manager Repository* lists the exit statuses from its version 0.6.0.
- manage-git already follows this. Managers that add a check follow it from their first check.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-21 | Accepted | Initial version, from osat-manager-git decision 0002 |

## License

This document, *Decision: A Check Exits 2 When Not Ready*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
