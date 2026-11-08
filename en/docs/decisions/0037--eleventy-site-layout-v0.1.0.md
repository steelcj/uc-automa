---
title: "Decision: An eleventy-site Layout"
dc:title: "Decision: An eleventy-site Layout"
dc:creator: "Christopher Steel"
dc:contributor: "Claude Opus 5.5 (Anthropic), AI assistance"
dc:subject: "layouts, eleventy-site, Eleventy, Netlify, websites, naming, tool-required names"
dc:description: "Add an eleventy-site layout extending base, requiring eleventy.config.js, package.json, package-lock.json and src/ with themes/ and netlify.toml optional, so an Eleventy website conforms out of the box; the names Eleventy requires by default join the names a tool requires."
dc:date: "2026-10-23"
dc:type: "Text"
dc:format: "text/markdown"
dc:identifier: "urn:uuid:bb2a6b93-ee71-43fa-9398-8ac9fa060318"
dc:relation:
  - "urn:uuid:ac5f649a-9d64-476a-9ad8-5c37630b4f78"
  - "urn:uuid:66c97c8d-e1cb-4652-91a8-25279a1dacdd"
dc:language: "en-CA"
dc:rights: "CC-BY-4.0"
sat:version: "0.1.0"
sat:status: "Accepted"
---

# Decision: An eleventy-site Layout

Version: 0.1.0
Status: Accepted

## Context

eleventy-website-vishpala-com, the repository for vishpala.com, is the first Vishpala repository that is a website rather than a Python tool. It holds an Eleventy configuration, an npm manifest and lockfile, the site's input under `src/`, and a theme under `themes/`. The root is always closed and a path no layout describes is a finding about the layout, with no per-repository exception (uc-automa 0013), so under `base` alone every one of those paths is a finding.

Eleventy fixes some names by default. It looks for its configuration as `eleventy.config.js`; inside its input directory it reads data from `_data/` and layouts and partials from `_includes/`; and it reads directory and template data from files named for their folder or template with `.11tydata.json` or `.11tydata.js`, such as `guides.11tydata.json`. The directive `naming/lowercase-names` already exempts names a tool requires, such as `REUSE.toml`, but its check listed only `REUSE.toml`, so it reported every one of these.

## Decision

- Add the layout `eleventy-site`, extending `base` directly, since a website is not a Python tool.
- It requires `eleventy.config.js`, `package.json`, `package-lock.json` and `src/`, and allows `themes/`. These are what an Eleventy site holds when set up as Eleventy and npm expect by default, so a site conforms without configuring anything away from those defaults.
- It also allows `netlify.toml`, for a site deployed to Netlify. Netlify reads its configuration from that file at the root of the repository, so the build settings, redirects and response headers can be kept and reviewed with the site rather than only in Netlify's dashboard.
- `src/` and `themes/` stay open: their contents are the site's own and change with it, and the layout does not describe them.
- The built output and installed dependencies, such as `_site/` and `node_modules/`, are not described. They are ignored by `.gitignore`, so the layout check never sees them.
- The check for `naming/lowercase-names` accepts the names Eleventy requires: `eleventy.config.js` everywhere; and, in a repository whose layout chain includes `eleventy-site`, the directories `_data/` and `_includes/` and the `.11tydata.json` and `.11tydata.js` suffixes under `src/`. The part of a data file's name before the suffix still follows the rule, so `Guides.11tydata.json` and `a.b.11tydata.json` are still reported. The directive's text already covers names a tool requires, so this is a check fixed without changing the rule (uc-automa 0029), and the directive keeps its version.

## Alternatives considered

**A general `website` layout.** Rejected for now. What a site holds at the top level depends on its generator, and only one generator is in use. A shared parent can be drawn out of `eleventy-site` when a second generator arrives.

**Generating Netlify's `_headers` and `_redirects` into the built site instead of allowing `netlify.toml`.** Not chosen as the only way. Those files carry redirects and headers but not the build command or the publish directory, which would then live only in Netlify's dashboard. A site can still generate them alongside `netlify.toml`, since they are output and never committed.

**Describing the configuration files of other hosts as well.** Not done yet. Only Netlify is in use; another host's file joins the layout when a site deploys there.

**Requiring the Sveltia CMS files.** Rejected. Where the CMS's `admin/` lives depends on the site's input directory, and a site can be built without a CMS.

**Configuring Eleventy away from its defaults, such as with `.eleventy.js`.** Rejected. A site should work out of the box as Eleventy documents it, and the layout follows the site rather than the reverse.

## Consequences

- `uc-automa init --layout eleventy-site` writes the same subscriptions as `base`, since the layout adds no `from_offering` paths.
- The seeded `REUSE.toml` covers a Python tool's usual paths, so each site adds annotations for `src/`, `themes/`, `package.json`, `package-lock.json` and `eleventy.config.js`, and for any font licences, as its own record.
- The directory guide gains a section for the layout.

## Changelog

| Version | Date | Status | Notes |
| --- | --- | --- | --- |
| 0.1.0 | 2026-10-23 | Accepted | Initial version |

## License

This document, *Decision: An eleventy-site Layout*, by **Christopher Steel**, with AI assistance from **Claude Opus 5.5 (Anthropic)**, is licensed under the [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/).
