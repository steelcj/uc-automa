# uc-automa

uc-automa is the station: the rules, the offerings and the tool that checks repositories against them. It is its own first consumer, with `automa_version: self`.

## Working here

- The brief and decision records under `en-ca/docs/decisions/` are the authority for how uc-automa works. Never infer a convention from another repository; if it is not written in a directive or decision, ask.
- Python 3.8 or later, standard library plus PyYAML and uc-portage, `pathlib` throughout. The only external program is git, for listing a repository's files.
- Run `python3 -m unittest discover -s tests` and `uc-automa check` before every commit.
- Each check names the directive it enforces, and each directive names its check in `sat:enforced_by`.
- Ask before pushing, tagging, or changing any other repository.

<!-- uc-portage:begin uc-automa-signpost -->
## uc-automa

This repository follows uc-automa at the version pinned in `.uc-automa.yaml`.

- The rules are uc-automa's directives, under `en-ca/docs/directives/` at that version. Each names the check that enforces it, if it has one.
- Run `uc-automa check` before committing, and `uc-automa offerings plan` to see whether shared files have drifted.
- Files the layout marks `from_offering` arrive from uc-automa; change them there, not here.
- If a rule is not written in a directive, ask. Never copy a convention from another repository.
<!-- uc-portage:end uc-automa-signpost -->
