---
title: "Markdown: No Heading Numbers"
dc:title: "Markdown: No Heading Numbers"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "markdown, headings, numbering, changelog"
dc:description: "Headings carry no section numbering such as \"## 3. Release\"; a version number inside a heading, as in a changelog's \"## [0.1.0] - 2026-10-09\", is not numbering and is allowed."
dc:date: "2026-10-09"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:5de5b74c-98b9-4533-bd50-8ddb48d3a13b"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "In force"
sat:directive: "markdown/no-heading-numbers"
sat:enforced_by:
  - "conformance.markdown.no_heading_numbers"
---

# Markdown: No Heading Numbers

Version: 0.1.0
Status: In force

## Rule

A Markdown heading is not numbered. The rule forbids section numbering, such as `## 3. Release`, `### 3.1 Scope`, `## 4) Notes` or `## 3 Release`. It does not forbid a number that is part of what the heading names: a version inside a heading, as Keep a Changelog writes `## [0.1.0] - 2026-10-09`, is allowed.

## Rationale

Numbers in headings go stale whenever a section is added, moved or removed, and Markdown renderers and editors already number or outline headings when a reader wants that.

## Examples

| Heading | Verdict |
| --- | --- |
| `## Release ceremony` | Conforms |
| `## [0.1.0] - 2026-10-09` | Conforms: a version, not numbering |
| `## 3. Release ceremony` | Numbered |
| `### 3.1 Scope` | Numbered |

## Check

`conformance.markdown.no_heading_numbers` reads the headings of every Markdown file outside code fences and flags only numbering patterns: a leading number followed by a dot, a parenthesis or a space and a word, and two-level numbers such as `3.1`. Its fixtures are under `tests/fixtures/conformance/markdown/no-heading-numbers/`.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-09 | In force | Initial version |

## License

This document, *Markdown: No Heading Numbers*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
