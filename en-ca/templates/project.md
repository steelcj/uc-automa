---
title: "<Project title>"
description: "<One sentence stating what the project delivers and which decision it carries out.>"
date: YYYY-MM-DD
lang: en-CA
tags:
  - project
dc:
  identifier: "urn:uuid:<uuidgen -r>"
  title: "<Project title>"
  creator: "Christopher Steel"
  publisher: "Vishpala"
  date: YYYY-MM-DD
  language: en-CA
  type: Text
  format: text/markdown
  rights: "CC BY 4.0"
  license: "https://creativecommons.org/licenses/by/4.0/"
sat:
  version: "0.1.0"
  status: provisional
  project: uc-automa
project:
  slug: <short-slug>          # same as the folder name under projects/
  status: planned             # planned | active | done | abandoned
  implements: []              # decision IDs this project carries out, such as LIC-0001
  scope:
    - <repository>
  date_started:
  date_finished:
---

# <Project title>

This project carries out [<DECISION-ID>](<link to the decision record>): <what will be true when it is done>.

Status: Planned.

## Before starting

- [ ] Confirm the decision this project carries out is Accepted.
- [ ] Change this project's status to Active and fill `date_started`.

## Steps

- [ ] <Step>
- [ ] <Step>

## Finishing

- [ ] Record completion in the changelog of each decision this project carries out.
- [ ] Change this project's status to Done and fill `date_finished`.

Questions that come up while the project runs and need a lasting answer become new decision records in `vishpala-decisions`, linked from here, rather than notes in this file.

## Changelog

| Version | Date | Status | Changes |
| --- | --- | --- | --- |
| 0.1.0 | YYYY-MM-DD | Planned | First draft |

## Licence

This document is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/).
