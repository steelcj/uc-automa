# discussion

Practice repo - vishpala-decisions

UC repo - uc-automa

**Cross-cutting decisions belong in one central repository.** These are decisions that govern several repositories or the whole practice: licensing, documentation conventions, metadata and front matter, citation style, versioning, and SAT architecture. Spread across repositories, there's no obvious home for them, no single numbering scheme, and no way to see what is currently in force. Centralizing them gives you one index, one history and one place to send a client who asks why you do things a certain way.

**Component-local decisions are better kept next to the code they govern.** These are choices that only make sense inside one tool, such as why `uc-radar` stores scores a certain way. Kept beside the code, they get updated in the same commit when the code changes. Moved away, they drift out of sync.

This split also fits your sovereignty principle and SAT's goal of liberating a collection from one instance and moving it to another. If a component is handed to a client or forked, its local decisions should travel with it. A component that depends on a central repository to explain itself is a small form of lock-in.

**What I'd suggest**

- **Make the central repository practice-level, not Universal Cake-level.** Your cross-cutting decisions span SAT, sat-doc-automa and Universal Cake, so uc-automa is too narrow a home. A name like `vishpala-decisions`, or simply `decisions`, under steelcj would work. uc-automa can then hold Universal Cake-specific decisions or link to the central ones.
- **Have the central repository index everything, including local records.** An automation step can scan each repository for decision-record front matter and build one index, published as an Eleventy site. You get a single view without moving the local records.
- **Give every record a stable identifier.** Use your `urn:uuid:` values plus a readable ID with a domain prefix, such as `LIC-0001` or `SAT-0003`, so records from different repositories never collide. References then survive moves.
- **Use explicit statuses: proposed, accepted, superseded and deprecated.** Your two SAT ADRs that rest on assumptions that no longer hold are the clearest case. Mark them superseded with a link to whatever replaces them, rather than deleting them, so the reasoning trail stays intact.
- **Move records without breaking links.** When you move a record, leave a short stub at the old path pointing to its new home, and keep the git history. Record the consolidation itself as the first decision in the new repository.

**What to put where now**

- **Central repository:** the licensing decision, the trademark policy, house markdown style, front matter and metadata conventions, the SAT config cascade and its role structure, and the ADRs on naming parity and identifiers.
- **Stays local, indexed centrally:** implementation decisions inside a single tool or site.
- **Not a decision record:** the migration checklist. It's a work plan, so it belongs in uc-automa next to the work, with a link from the licensing decision.

I can draft the README and folder layout for the central repository, a decision-record template with the front matter and status fields, or the first record covering this consolidation.  