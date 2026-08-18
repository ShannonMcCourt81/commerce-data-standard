# CDS in Plain English

*The whole system explained without jargon. If you read nothing else, read this. (v0.2, 2026-08-17)*

---

## What this project actually is

This started as one practical question: **how should a Shopify store set up its tags, filters, categories and product data properly, so it doesn't turn into a mess?**

Answering that properly meant writing down the rules — what makes a good category tree, which words are allowed in a colour filter, when a tag is the right tool and when it isn't, and how to *check* the store actually shows what you intended. Written down carefully, those rules became a reusable rulebook that would work for any store, not just this one. That rulebook is the Commerce Data Standard.

**So: CDS is still the answer to the original question.** It just comes in layers now, and you only need the top one day-to-day.

## The three layers (and who they're for)

1. **The Runbook** — *for you.* "Do this, then this" for setting up the store. This is the practical document the project was always meant to produce. Use the companion Adoption Workbook to record decisions and evidence as you go.
2. **The Standard** — *for looking things up.* Every rule the runbook follows, with its reasoning. You never read it cover to cover; you open it when a runbook step cites a rule and you want the why.
3. **The machine files** (schemas + dictionaries) — *for the software.* The allowed vocabulary (the dictionary CSVs) and the technical contracts that let the PIM software check its own work automatically. You'll never open these; the PIM uses them.

## The whole idea in one story

A supplier sends you a shirt in "French Navy".

- The PIM looks up "French Navy" in the **colour dictionary**. It's a known name → it's filed under the official colour `french_navy`, which belongs to the broad family **Blue**. (If it were some unknown name like "Moonlit Harbour", it would wait in a queue for you to decide — the system never invents vocabulary on its own.)
- The product page shows **"French Navy"** (the nice name customers should see).
- The storefront **filter** shows **"Blue"** (because nobody wants a colour filter with 200 near-identical shades).
- Google gets **"French Navy"** (Google's rules require the name shown on the page).
- The category tree — decided once, on paper, with a logbook for the tricky calls — automatically generates the **tags** that drive collections. Nobody hand-types tags, and tags are never used as filters.
- After publishing, the PIM **reads the store back** and compares: does Shopify actually show what we sent? Every field gets a light: **Green** (matches), **Amber** (missing or waiting), **Red** (contradicts). If a staff member edits a product directly in Shopify, that shows up as a Red/Amber difference with a reason — you find out, instead of the store quietly drifting away from your data.

That's the entire system. Everything in the standard is that story, made precise enough that software can enforce it and any future store or developer can follow it without asking you.

**Want this story with the exact names you'd actually type — the dictionary row, the PIM field, the Shopify metafields, the verification result? That's Appendix A of the Setup Runbook ("One Attribute End-to-End") — the same French Navy story, told on a single-colour cushion with every field name spelled out.**

## The ten bits of jargon, translated

| Term | Plain meaning |
|---|---|
| Prose | Normal sentences for humans (the chapters), as opposed to code for machines. |
| Canonical | The one official version of a fact. Canonical colour = the official filed colour, whatever the supplier called it. |
| Dictionary | The list of allowed words for one thing (colours, materials, fits) plus their spellings/aliases. |
| Facet | A filter customers use, with deliberately few, broad options ("Blue", not 40 shades). |
| Alias | A known alternative name that maps to an official one ("rayon" → Viscose). |
| Projection | A copy generated *from* the master data for one purpose (the page label, the filter value, the Google feed) — never edited directly. |
| Drift | The store showing something different from what the PIM says it should — detected, not silently accepted. |
| Provenance | Where a value came from and who/what set it (supplier file, you, a formula, AI). |
| Schema | A machine-readable form template — software uses it to auto-reject malformed data. |
| Namespace / prefix | The label at the front of a field name (`MF_colour_family`) that tells you at a glance what kind of field it is. |
| Conformance | How much of the standard an implementation genuinely follows — with proof, not vibes. |

## What you actually do next

1. Read the **runbook's first page (the TL;DR)** — five minutes.
2. When you're ready to build the store, follow the runbook phase by phase. It stops and asks you for six decisions along the way; everything else is procedure.
3. Ignore everything else in the folder until something sends you there.

*Why keep the heavyweight layers at all? Because they're what make the practical layer trustworthy: every runbook instruction traces to a written rule, every rule traces to evidence, and the software can prove the store matches the plan. You get the simple experience precisely because the complicated part is nailed down underneath.*
