# Commerce Data Standard (CDS)

**Current version: v0.2** (Review Draft status — content-complete and internally verified; v1.0 is reserved until the standard has external review and real adopters behind it).

CDS is a vendor-neutral standard for product information: describe a product once in the PIM, project it to every channel (Shopify, Google, Meta), read back what the channel actually shows, and verify expected vs actual — surfaced as Green/Amber/Red with machine-readable reasons.

---

## What's in this folder, and in what order to read it

| # | Item | What it is | When you use it |
|---|---|---|---|
| 0 | **`CDS_Start_Here.pdf`** | A one-page checklist showing exactly where a human starts and what must be completed first. | **Start here.** |
| 1 | **`README.md`** | This guide. | Use for the complete folder map. |
| 1a | **`CDS_Plain_English_Guide.pdf`** | The whole system explained without jargon — what CDS is, the French Navy story, and a translation table for every technical term. | **Read this first if anything ever feels like nerd-speak.** |
| 2 | **`CDS_Shopify_Setup_Runbook_v0.2.pdf`** | The step-by-step guide to setting up the new Shopify store under CDS. Opens with a one-page TL;DR; 10 phases; six marked OWNER DECISION stops; ends with the done-checklist and **Appendix A — the French Navy worked example: one attribute end-to-end (dictionary → PIM record → Shopify metafields → verified round-trip), with the exact names you type**. | **Read the TL;DR today.** Follow the phases when store setup begins. |
| 2a | **`v0.2/CDS_Adoption_Workbook_v0.2.md`** | One fill-in document for the organisation profile, owner decisions, taxonomy log, channel capabilities, phase evidence, vertical-slice results and human review. | Open at runbook Phase 0.5 and maintain through sign-off. |
| 3 | **`Commerce_Data_Standard_v0.2.pdf`** | **The standard itself** — all 16 chapters in one document. Not a cover-to-cover read: it's the reference the runbook cites (every runbook step lists the rule IDs it implements — look them up here when you want the why). | Reference, on demand. |
| 4 | **`CDS_Dictionary.pdf`** | **The dictionary as a book** — every allowed word in sixteen chapters — from Colours and Materials through Footwear, Beauty and Electronics to Sports, Toys, Pets, Furniture and Garden — each chapter opening with a plain-English note on what belongs there, like an Oxford dictionary. Generated directly from the data below so the two can never disagree. | Browse when deciding vocabulary; the readable face of item 5. |
| 5 | **`CDS_Reference_Dictionary/`** | The same dictionary as data: 50 CSVs / 674 entries, one unified checksummed package (replaces the two earlier separate packs). Chapters 1–7 are bound to your published profiles; 8–16 (footwear, jewellery, beauty, electronics, sports, toys, pets, furniture, garden) are ready vocabulary awaiting profiles. Beauty deliberately excludes marketing claims — those need evidence, not filter buttons. | Imported into the PIM at runbook Phase 2. Not edited by hand after that. |
| 6 | **`CDS-1200_Reference_Package_v0.2/`** | The machine-readable contracts: JSON Schemas + example documents + a test runner. This is how a conforming implementation proves it produces valid CDS documents. | Developers, during implementation. Run: `pip install -r requirements.txt && python tools/validate.py`. |

**Reading flow in one line:** README → runbook TL;DR → (when building) follow the runbook, looking rules up in the standard as cited, seeding data from the dictionary package (browsing the dictionary book to choose vocabulary), validating software output against the reference package.

## Supporting folders (not part of the reading flow)

| Folder | What it is |
|---|---|
| **`v0.2/`** | The *editable sources* behind the two PDFs — one markdown file per chapter, plus the runbook source. Edit here, regenerate the PDFs. Never edit a PDF directly. |

`release-manifest.json` records the SHA-256 digest and byte size of every live v0.2 release artifact so a distributed copy can be checked exactly.

## Rules of the road

1. All editing happens in `v0.2/` markdown; PDFs are regenerated from those sources.
2. CDS is universal and project-agnostic: implementations conform to CDS — never the reverse.
3. v1.0 is gated (CDS000-R008): external review, stable profiles, conformance evidence, documented adopters.

## Where things stand / what's next

- **Done:** the v0.2 standard (1,034 requirements, internally reviewed), the executable reference package (33/33 clean), the restructured dictionary data, and the setup runbook — all adversarially verified.
- **Next:** follow the runbook against a dev Shopify store — that *is* the CDS vertical slice. Its Phase 10 contains two queued real-world checks (filter-count accuracy under combined selections; the drift-attribution workflow) whose results feed v0.3.
- **Later (v0.3 standard track):** remaining platform-claim sweep; per-requirement test IDs.
