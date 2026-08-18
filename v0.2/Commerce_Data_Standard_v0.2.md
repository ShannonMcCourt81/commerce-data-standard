# Commerce Data Standard
## Version 0.2 (Review Draft)

| Field | Value |
|---|---|
| Status | v0.2 Review Draft — for review; not an approved standard |
| Release | CDS v0.2 (single corpus release, ADR-D5) |
| Date | 2026-08-17 |
| Requirements | 1,034 identified (REVIEW-004 index) |
| Companion package | CDS-1200_Reference_Package_v0.2 (v0.2.1; verified 33/33 clean-environment) |
| Licence | Prose CC-BY 4.0 · machine-readable artifacts Apache-2.0 |
| Supersedes | CDS v0.1 Working Corpus (16 chapter PDFs + package v0.1) — changelog: REVIEW-012 |

## Master Table of Contents

1. CDS-000 — Foundations and Core Principles
2. CDS-100 — Terminology
3. CDS-200 — Commerce Information Architecture
4. CDS-300 — Semantic Namespaces and Field Naming
5. CDS-400 — Controlled Dictionaries and Reference Data
6. CDS-500 — Publication, Observation and Verification
7. CDS-600 — Customer Experience, Facets and Navigation
8. CDS-700 — AI Enrichment, Automation and Human Oversight
9. CDS-800 — Governance, Ownership and Change Control
10. CDS-900 — Implementation Profiles and Platform Mappings
11. CDS-1000 — Conformance, Testing and Assurance
12. CDS-1100 — Reference Schemas and Machine-Readable Contracts
13. CDS-1200 — Reference Implementation, Schema Package and Test Fixtures
14. CDS-1300 — Migration, Adoption and Operational Rollout
15. CDS-1400 — Monitoring, Incident Management and Continuous Improvement
16. CDS-1500 — Apparel and Homewares Industry Profiles and Reference Dictionaries

Closing matter: A. ADR Register · B. Requirements Index summary · C. Bibliography

*Reading conventions: RFC 2119/8174 keywords are normative only in upper case within requirement sentences (CDS000-R001). Every section is marked normative or informative. Requirement IDs are stable (CDSnnn-Rmmm).*


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-000 — Foundations and Core Principles

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-000 Working Draft v0.1 (formerly mislabelled v1.0); the one-page "CDS Constitution" (retired to `_superseded/`, its unique principles merged here) |
| Normative status | §3 (Document Conventions), §4 (Versioning and Release Policy) and §6 (Precedence and Extension) are normative. §1, §2, §5 and §7 are informative. |
| Findings addressed | 000-1..6, 300-9, D23, D26; ADR-D1, ADR-D5 |

---

## 1. Foreword and Mission *(informative)*

The Commerce Data Standard (CDS) is an open specification for the modelling, governance, publication and verification of product information. CDS is PIM-first, channel-agnostic, human-readable and governed-AI-ready. It defines how product information is represented independently of any individual commerce platform.

**Mission:** products are described once, understood everywhere, published many times, and verified after publication.

CDS exists to solve recurring commerce-data failures: product information duplicated and independently edited across systems; storefront filters that expose hundreds of near-duplicate raw values; tags used as an ungoverned database; internal taxonomies confused with storefront collections and marketplace categories; successful API writes treated as proof of correct downstream representation; free-text enrichment that defeats deterministic mapping and validation; cryptic field names that force operators to consult external notes; and AI automation that invents values without evidence or approval.

The core proposition:

> Describe once in the PIM → normalise and govern → project to each channel → observe the downstream result → verify expected versus actual → present actionable data-quality health.

## 2. Scope and Non-Goals *(informative)*

**CDS defines:** the canonical product model; classification and taxonomy separation; semantic namespaces and naming; controlled dictionaries and reference data; facet and customer-experience projection; publication, observation and verification; governance, ownership and conformance; AI enrichment under governance; implementation profiles for specific platforms and industries.

**CDS does not define:** ERP, OMS, WMS or accounting systems; pricing strategy; CMS implementation; order, customer or inventory mastering (these may be *observed* by a CDS implementation but are mastered elsewhere — see the per-fact authority model in CDS-200).

CDS is vendor-neutral. Platform-specific behaviour lives only in versioned, dated profiles (CDS-900). No platform — including any reference implementation — shapes the core standard.

## 3. Document Conventions *(normative)*

**CDS000-R001** The key words MUST, MUST NOT, SHOULD, SHOULD NOT and MAY in CDS documents are to be interpreted as described in RFC 2119 and RFC 8174: they are normative **only when they appear in upper case within the body of a requirement sentence**.

**CDS000-R002** The keyword SHALL is not used in CDS. Requirement sentences MUST NOT carry a detached requirement-level prefix label; the in-sentence keyword governs. *(Resolves the prefix-corruption defect catalogued in the v0.2 errata manifest.)*

**CDS000-R003** Every normative requirement carries a stable requirement identifier of the form `CDSnnn-Rmmm` (chapter number, requirement number). Identifiers are never reused after retirement.

**CDS000-R004** Every section is explicitly marked normative or informative. Examples, worked scenarios and platform observations are informative unless individually marked otherwise.

**CDS000-R005** Each defined term has exactly one authoritative definition, in CDS-100. Each normative topic has exactly one authoritative home chapter; other chapters cite it and MUST NOT restate its requirements. The authoritative homes are: terminology — CDS-100; entity and authority model — CDS-200; namespaces and naming — CDS-300; dictionaries and value layers — CDS-400; publication, observation, verification and statuses — CDS-500; facets and customer experience — CDS-600; AI — CDS-700; governance roles and change control — CDS-800; platform profiles — CDS-900; conformance levels, tests and claims — CDS-1000; machine-readable contracts — CDS-1100.

**CDS000-R006** Architecture decisions are recorded as ADRs in a single global register, one ADR per decision. A superseded ADR is marked superseded and cross-referenced; the same decision MUST NOT be recorded in multiple ADRs.

## 4. Versioning and Release Policy *(normative — from ADR-D5)*

**CDS000-R007** The corpus has one release version shared by every chapter and companion package. The current release is **v0.2 Review Draft**. Chapters MUST NOT carry independent versions.

**CDS000-R008** Release gates: v0.9 requires external/domain review, stable profiles and a complete conformance package; v1.0 requires stable governance, independently tested schemas, current verified profiles and documented adopters. No CDS artifact may be labelled v1.0 before those gates pass.

**CDS000-R009** Schema `$id`s are release-independent URNs (`urn:cds:schema:<domain>:<name>`); each schema carries its own semantic version; instances pin their corpus release via the envelope `cds_version`. (Details: CDS-1100.)

**CDS000-R010** Principle identifiers use the form `CDS-P-nn`; they share no identifier space with chapter numbers, requirement IDs or ADR IDs.

## 5. Core Principles *(informative — each principle anchors requirements that live in its home chapter)*

| ID | Principle | Meaning | Normative home |
|---|---|---|---|
| CDS-P-01 | Canonical First | Every product fact has one canonical representation and one declared authoritative owner. Two systems never simultaneously master the same fact. | CDS-200 |
| CDS-P-02 | PIM First, Channels Downstream | The PIM is the master product-information layer. Channels consume projections; they never become the master. Channel read-back is observed state and never silently overwrites canonical values. | CDS-200, CDS-500 |
| CDS-P-03 | Information Before Technology | Model the product, not the platform. Platform constraints shape mappings in profiles, not canonical identity. | CDS-200, CDS-900 |
| CDS-P-04 | Human First | Visible field identifiers and namespaces reveal purpose in ordinary work without a glossary lookup. Semantic prefixes are part of the user interface. | CDS-300 |
| CDS-P-05 | AI Under Governance | Semantic clarity and structured metadata make product data highly usable by AI — but AI operates under schemas, dictionaries, provenance, confidence and human governance. Prefixes aid AI understanding; they do not replace schema metadata, and AI never infers authority it was not granted. | CDS-700, CDS-300 §22 |
| CDS-P-06 | Publish → Observe → Verify | A transport acknowledgement is not proof. Publication is incomplete until the downstream state is independently observed and compared with the expected state. | CDS-500 |
| CDS-P-07 | Controlled Vocabularies | Dictionaries and typed values are preferred over free text wherever consistency, filtering, mapping or AI use matters. | CDS-400 |
| CDS-P-08 | Facet UX Over Raw Data | Customers see governed, comprehensible facet families; the PIM retains the detailed canonical and source values beneath them. | CDS-600, CDS-400 |
| CDS-P-09 | Explicit Domains | Every **visible** field identifier belongs to a registered semantic namespace. Internal machine keys may differ where a declared reversible mapping exists. | CDS-300 |
| CDS-P-10 | Durable Naming | Names survive technology changes. Identifiers are stable; labels may evolve. | CDS-300 |
| CDS-P-11 | Extensible by Design | New channels, attributes and organisational extensions are added through registered extension points without breaking the model or colliding with reserved namespaces. *(From the retired Constitution.)* | CDS-300 §18–19, CDS-1100 |
| CDS-P-12 | Governance Over Convenience | Long-term data quality outranks short-term convenience. Shortcuts that bypass dictionaries, authority or verification are non-conformant even when expedient. *(From the retired Constitution.)* | CDS-800 |

## 6. Precedence and Extension *(normative)*

**CDS000-R011** Profile precedence: more specific profiles (platform → industry → organisation) MAY add constraints; CDS core semantics remain authoritative for shared concepts. A profile MUST NOT weaken a core requirement; deviations go through the exception process (CDS-800).

**CDS000-R012** Conformance levels, their tests and claim rules are defined solely in CDS-1000 (Foundation → Structured → Publisher → Verified → Governed, with overlay profiles such as AI-Assured). Levels are strictly cumulative. *(ADR-D1.)*

## 7. Relationship to Evidence *(informative)*

CDS's requirements trace to: explicit owner decisions and proven production behaviour (highest weight — the legacy Airtable/Shopify pipeline with per-field round-trip verification and traffic-light health); current official platform documentation, verified and dated in profiles; established PIM literature (Abraham 2014 — which supports the canonical model, taxonomy separation and controlled vocabularies, and whose silence on post-publication verification marks Publish → Observe → Verify as a CDS contribution); and reasoned architecture decisions recorded as ADRs. Working-draft prose is never self-evidencing.


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-100 — Terminology

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-100 Working Draft v0.1 (formerly mislabelled v1.0) |
| Normative status | §2–§6 are normative definitions. §7 (lifecycle diagram and example) is informative. §8 (deprecated terms) is normative. |
| Findings addressed | 100-1..5, Matrix 4 conflicts; ADR-D3, ADR-D4; 800-3 (exception), 1100 R023 (variant), CDS-1500-4 (multicolour) |

**CDS100-R001** The definitions in this chapter are normative. A term has exactly one CDS definition; other chapters MUST use these terms consistently and MUST NOT redefine them. Where industry usage conflicts, the CDS definition prevails within CDS documents.

**CDS100-R002** Each definition names the chapter that owns the term's detailed requirements ("Home"). Definitions state *what a term means*; the home chapter states *what implementations must do*.

---

## 2. Core Entities *(normative)*

**Product** — A logical commercial item described by a single canonical information record. *Home: CDS-200.*

**Variant** — A distinct sellable unit of a Product, identified by the values of its variant options. A difference becomes a variant option only when it creates a distinct sellable unit. A Product with no variant options has exactly **one** variant, which MAY be implicit in storage but is a variant for counting, publication and verification purposes. A variant is normally identified by a stable SKU; an implementation MAY use an explicitly documented alternative sellable-unit key. *Home: CDS-200 §5.*

**Variant Option** — A named dimension (e.g. size, colour) whose values distinguish the variants of one Product. *Home: CDS-200 §5.*

**Attribute** — A named characteristic describing a Product or Variant.

**Attribute Definition** — The first-class schema record for an attribute: its identifier, type, scope (product/variant), validation rules, dictionary binding, requiredness, facet/display/search/channel policies and comparison strategy. Products store values; Attribute Definitions store behaviour. *Home: CDS-200 §7.*

**Attribute Value** — The stored value of an attribute on a specific Product or Variant, with provenance. *Home: CDS-200 §7.*

**Classification** — The assignment of a Product to nodes of the internal taxonomy. *Home: CDS-200 §6.*

**Internal Taxonomy** — The organisation's own classification tree, independent of any channel's taxonomy. A Product has exactly one primary category at the most specific applicable level; additional non-projecting secondary placements MAY exist. *Home: CDS-200 §6.*

**Product Family / Product Type** — The upper and middle tiers of the recommended three-tier internal taxonomy (Family → Type → Category). The three-tier stack is a recommended profile shape; core requirements bind to "an internal taxonomy", not to this exact stack. *Home: CDS-200 §6.*

**Category** — A node of a taxonomy (internal or external). *Home: CDS-200 §6.*

**Collection** — A merchandising grouping presented to customers, derived from rules, classification or curation. Collections never redefine product identity or replace classification. *Home: CDS-600 §6 (rule: CDS-200).*

**Tag** — A governed, flat channel signal generated from canonical data (e.g. `collection_*` projections). Tags are integration outputs, never the primary store for structured product facts. *Home: CDS-400 (governance), CDS-500 (publication merge semantics).*

## 3. Value Layers and Dictionaries *(normative — per ADR-D4)*

**Source Value** — The raw value exactly as received from a supplier, import or channel, preserved verbatim with provenance. *(Replaces the former term "Reference Value" — see §8.)* *Home: CDS-400.*

**Alias** — A recognised source spelling or synonym of a canonical value.

**Alias Mapping Record** — The governed record mapping one source value (scoped by dictionary, and optionally supplier or locale) to exactly one canonical value. Every source value that has been mapped is retained as an alias with provenance. *Home: CDS-400.*

**Dictionary** — A governed, versioned collection of canonical values for one semantic domain (e.g. colour), including their aliases, labels, facet memberships and lifecycle states. *Home: CDS-400.*

**Dictionary Value / Canonical Value** — A governed entry in a dictionary: a stable `value_id` and snake_case canonical code with lifecycle status and provenance. Canonical product data stores canonical `value_id`s — a Variant's colour field holds the canonical value, never a raw source spelling. Promotion of a source value to a new canonical value is an explicit governed act; bulk imports never silently create canonical values. *Home: CDS-400.*

**Display Label** — A human-facing label linked to a canonical value. Display labels MAY preserve supplier or brand names (e.g. "Moonlit Harbour" displayed while canonical `navy` governs). *Home: CDS-400 §9.*

**Facet** — A customer-facing refinement dimension used for filtering and navigation. *Home: CDS-600.*

**Facet Definition** — The governed configuration of a facet: identifier, label, eligible categories, value source, selection logic and count method. *Home: CDS-600.*

**Facet Value** — A governed, customer-facing grouping value that canonical values map to (e.g. canonical `french_navy` → facet `blue`). Facet values are projections; they never replace canonical values. Multicolour is a facet/status value, never a canonical shade. *Home: CDS-400 (mapping), CDS-600 (presentation).*

**Search Synonym** — A governed query-side term mapped to a preferred concept for search expansion. *Home: CDS-600 §21.*

**Channel Representation** — The value form projected to a specific channel for a specific attribute, as declared by the Attribute Definition and channel profile (which layer feeds each channel — canonical, display or facet — is declared per attribute, never assumed). *Home: CDS-400 §11, CDS-500 §6.*

**Projection** — Any deterministic derivation from canonical data to a downstream form: display, facet, search, tag or channel representation, and the Expected Channel State as a whole. *Home: CDS-500.*

**Quarantine** — The holding state for unknown or ambiguous source values pending human resolution; quarantined items remain in quality denominators. *Home: CDS-400 §17.*

## 4. Identity, Naming and Authority *(normative)*

**Namespace / Prefix** — A registered semantic domain marker (e.g. `MF_`, `CH_`, `QA_`) forming the first segment of visible field identifiers. The single normative registry lives in CDS-300. *Home: CDS-300.*

**Semantic Identifier** — The visible, namespace-prefixed field identifier (e.g. `MF_colour_family`) used in operator-facing contexts. Distinct from both the Human Label and the Machine Key. *Home: CDS-300 §8.*

**Human Label** — The natural-language label shown in UIs (e.g. "Colour family").

**Machine Key** — The internal storage key, which MAY differ from the semantic identifier where a declared reversible mapping exists (e.g. lossy export targets). *Home: CDS-300 §8.*

**Extension Namespace** — An organisation-registered prefix or extension point that cannot collide with any reserved core prefix. *Home: CDS-300 §18–19.*

**Authority** — The declared right of exactly one system to master a given product fact. Authority is declared **per fact**, not per system: the PIM masters canonical product content; other facts (e.g. inventory, price) MAY be mastered elsewhere and observed. Delegation is an explicit recorded act. *Home: CDS-200 §13.*

**System of Record** — The system holding authority for a fact.

**Owner** — The accountable person or role for a governed artifact (field, dictionary, facet, mapping, workflow). *Home: CDS-800.*

**Provenance** — The recorded origin and history of a value: source, method (manual, formula, import, AI-proposed), actor, time and evidence. *Home: CDS-200 §16, CDS-700.*

**Confidence** — A bounded score (0–1) attached to a machine-proposed value; never the sole acceptance criterion. *Home: CDS-700.*

**Override** — A governed record that redirects the expected channel value for a specific field/channel away from the default projection. A verified match against an active override is a true MATCH with `OVERRIDDEN` provenance. *Home: CDS-500 §22.*

**Exception** — A governance record granting a time-limited, documented, approved deviation from a requirement, with an expiry and a named owner. Expired exceptions never remain silently active. An exception acknowledges non-conformance; it does not convert failure into conformance. *(Single definition — supersedes the conflicting exception/waiver uses in earlier drafts; "waiver" as a noun is retired, see §8. The field-level verification status `WAIVED` — an accepted difference under an active exception that does not redirect the expected value — remains, defined in CDS-500.)* *Home: CDS-800 §16.*

## 5. Publication, Observation and Verification *(normative)*

**Channel** — Any downstream consumer of product information (e.g. Shopify, Google Merchant Center, Meta).

**Channel Profile** — The versioned, dated definition of a channel's capabilities, constraints, field mappings, write semantics and propagation window. *Home: CDS-900 (content), CDS-500 (role).*

**Field Mapping** — The declared transformation from a canonical attribute (at its declared layer) to a channel target field, including transformation version, write mode and comparison strategy. *Home: CDS-500 §6, CDS-1100.*

**Expected Channel State** — The persisted, reproducible projection of what a channel should hold for a product: derived from a specific canonical revision, mapping-set version and dictionary versions. Regenerating it with the same inputs yields the same output. *Home: CDS-500 §6.*

**Publication** — The controlled delivery of an expected channel state to a channel, recorded immutably.

**Publication Record** — The immutable record of one publication attempt: payload identity (hash), canonical revision, mapping-set version, transport status and acknowledgement. *Home: CDS-500 §8.*

**Acknowledgement** — The channel's transport-level response to a publication. An acknowledgement is not proof of correct downstream representation. *Home: CDS-500 §9.*

**Observation** — The independent retrieval of the state a channel currently holds, separate from any outbound payload. *Home: CDS-500 §14.*

**Observation Record / Observed State** — The stored result of an observation, kept strictly separate from canonical values, with method, time and per-field coverage. *Home: CDS-500 §15.*

**Coverage** — The per-field account of what an observation could and could not see (observed, empty, not returned, unsupported, permission denied, stale, pending visibility). Missing and unobservable are never conflated. *Home: CDS-500 §15.*

**Verification** — The comparison of expected channel state against observed state, field by field, under each field's declared comparison strategy. *Home: CDS-500 §16.*

**Verification Status** — The outcome classification of a verification, drawn from the single normative enum owned by CDS-500 §17. The eight **core statuses** (machine contract) are MATCH, MISSING, MISMATCH, PENDING, UNOBSERVABLE, NOT_APPLICABLE, OVERRIDDEN and ERROR; detailed statuses roll up to these deterministically. *(Summary here is informative; CDS-500 governs.)*

**Comparison Strategy** — The declared, type-aware method for comparing one field (exact, case-insensitive, unordered set, numeric tolerance, normalised text), drawn from the normalisation registry with test vectors. *Home: CDS-500 §16.*

**Reason Code** — The machine-readable code (CDS_* registry) carried by every non-MATCH field result, explaining *why* — the layer beneath the traffic light. *Home: CDS-1100 §21 (registry), CDS-500 (use).*

**Traffic Light** — The presentation layer over verification statuses: Green = expected equals observed; Amber = attention (missing, pending, unobservable, overridden, waived); Red = confirmed contradiction or error; Amber escalates to Red per declared rules. Colours are presentation, never stored statuses. *Home: CDS-500 §18 (per ADR-D3).*

**Drift** — Downstream state that no longer conforms to the current expected channel state or ownership contract. Republishing is not always the correct repair. *Home: CDS-500 §20, CDS-1400 §15.*

**Repair** — A governed action resolving drift (republish, accept via override/exception, or correct canonical data). *Home: CDS-500.*

**Channel Health** — The aggregate quality indication for a channel, computed from expected-state coverage, publication outcomes, observation coverage and verification results, with explicit denominators. Unobserved fields never count as matched. *Home: CDS-1400 §5–6 (metrics), CDS-500 §23 (aggregation).* *(This supersedes the narrower v0.1 definition "derived from verification results".)*

**Propagation Window** — The channel-declared time allowance between publication and observable effect; PENDING beyond the window escalates. *Home: CDS-900 (declared), CDS-500 (used).*

## 6. AI and Automation *(normative)*

**AI Proposal** — A machine-generated suggested value or action, stored separately from canonical state, carrying evidence, confidence, model/workflow version and review state. Acceptance is an auditable act linking the proposal to the canonical revision it produced. *Home: CDS-700.*

**Autonomy Level (A0–A4)** — The declared, per-workflow ceiling on what an AI workflow may do without human action, from suggest-only to bounded auto-acceptance. Never interpreted as unrestricted autonomy. *Home: CDS-700 §5.*

**Evidence Class (E1–E4)** — The declared strength ranking of the evidence supporting a proposal. *Home: CDS-700 §7.*

**Abstention** — A first-class AI outcome: declining to propose rather than inventing a value. Absence of evidence never becomes a positive claim. *Home: CDS-700.*

**Deterministic Automation** — Rule-based processing where identical inputs always produce one correct result; preferred over AI for such tasks, and never obscured by AI. *Home: CDS-700 §20.*

## 7. Controlled Value Lifecycle *(informative — corrected to the branch model per ADR-D4)*

```
Source Value ── Alias Mapping Record ──► Canonical Value
  "French Navy"      (governed)             value_id: colour_french_navy
                                                 │
              ┌───────────────┬────────────────┼────────────────┬───────────────┐
              ▼               ▼                ▼                ▼               ▼
        Display Label    Facet Value     Search Synonyms   Channel Repr.    Tag / other
        "French Navy"      "Blue"        "dark blue","navy"  (per attribute   projections
                                                             + profile)
```

Projections branch **in parallel** from the canonical value; channels are fed from the layer declared per attribute — never implicitly from the facet.

**Worked example.** A supplier provides "French Navy". The alias mapping resolves it to canonical `colour_french_navy` (or, in a coarser configuration, aliases it to `colour_navy` — both granularities are conformant). The variant stores the canonical `value_id`. The product page displays the Display Label "French Navy"; the storefront filter presents the Facet Value "Blue"; the channel receives whichever layer the Attribute Definition declares for it. When the mapping changes, republication regenerates every projection deterministically without editing any product.

## 8. Deprecated and Retired Terms *(normative)*

**CDS100-R003** The following terms are retired and MUST NOT be used in v0.2+ documents except when quoting v0.1 drafts or legacy systems:

| Retired term | Replacement | Reason |
|---|---|---|
| **Reference Value** | Source Value (the raw input) or Alias Mapping Record (the mapping) or Canonical Value (the governed entry) — whichever layer is meant | Three conflicting published meanings across v0.1 chapters (ADR-D4) |
| **Waiver** (noun, governance record) | Exception | Two chapters defined exception/waiver with swapped meanings (finding 800-3). The verification status `WAIVED` remains (CDS-500) |
| **SHALL** | MUST | Single keyword set (CDS000-R002) |
| **Mapping** (bare, unqualified) | Field Mapping, Alias Mapping Record, or Taxonomy Mapping — whichever is meant | Ambiguous across three distinct record types |
| **DF_** (prefix, new design) | CH_ | ADR-D24; DF_ remains a registered deprecated legacy prefix for migration aliases |

## 9. Design Principles Supported *(informative)*

One concept, one definition (CDS100-R001). Canonical information precedes publication (CDS-P-01/02). Customer experience and internal data are separate concerns (CDS-P-08). Semantic clarity benefits humans, software and governed AI equally (CDS-P-04/05).


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-200 — Commerce Information Architecture

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-200 Working Draft v0.1 |
| Normative status | §3 (Canonical Model), §4 (Entity Model), §5 (Product/Variant Boundary), §6 (Classification), §7 (Attribute Architecture), §13 (Ownership and Authority), §14 (State and Audit), §15 (Rules and Validation) are normative. §1–§2, §8–§12, §16–§18 are informative. |
| Findings addressed | 200-1, 200-2, 200-3, 200-4, 200-5, 200-6, 200-7, 200-8, 200-9; SYS-4 (chapter scope); decisions D9/D30 (LC-10); Matrix 5 relocations; ADR-D3, ADR-D4, ADR-D24 |

This chapter is the authoritative home for the **core entity model, the product/variant boundary, the per-fact authority model, and classification** (CDS000-R005). Terminology is defined in CDS-100 and used here without redefinition.

---

## 1. Purpose and Scope *(informative)*

CDS-200 defines the vendor-neutral information architecture that sits above commerce platforms and below business operations: what the master product layer contains, how information is classified and governed, who is authoritative for each fact, and how downstream channels consume projections of it.

The architecture is PIM-first (CDS-P-01/02/03). Sales channels and marketplaces are consumers. They may impose schemas and constraints, but they do not define the canonical identity of a product.

Publication, observation and verification mechanics are defined in CDS-500; naming in CDS-300; dictionaries and value layers in CDS-400; facets in CDS-600; AI participation in CDS-700; platform specifics in CDS-900 profiles.

## 2. Architectural Objectives *(informative)*

- **Single authority** — every product fact has one clearly defined authoritative source.
- **Separation of concerns** — identity, classification, attributes, merchandising, publication and verification remain distinct.
- **Human legibility** — names and structures communicate purpose without separate notes (CDS-300).
- **Machine determinism** — software can parse, validate, map and compare values without subjective interpretation.
- **AI clarity** — AI agents receive explicit schemas, dictionaries, constraints and confidence rules (CDS-700).
- **Channel durability** — technology-specific changes are absorbed by mappings, not by redesigning the canonical model.
- **Customer usability** — internal richness is simplified into usable facets and navigation (CDS-600).
- **Observability** — publication success is measured by observed downstream state, not merely by API response (CDS-500).

## 3. The Canonical Commerce Model *(normative)*

The canonical commerce model is the set of product information that is true independently of any channel: identity, classification, attribute values, variant relationships, content, media, compliance and lifecycle state. It excludes channel-specific formatting and channel-owned operational data unless such data is explicitly adopted as canonical.

```
Canonical Product Model
|
+-- Identity
+-- Classification
+-- Attribute Values
+-- Variants / Sellable Units
+-- Content
+-- Media
+-- Compliance
+-- Lifecycle
+-- Reference Data Links
|
+-- Publication Projections (per channel; CDS-500)
```

**CDS200-R001** A CDS implementation MUST maintain a canonical product layer independent of any single sales channel.

**CDS200-R002** A channel-specific limitation MUST NOT reduce the information fidelity of the canonical model. Channel constraints are absorbed by field mappings and profiles (CDS-500, CDS-900).

**CDS200-R003** A downstream read-back MAY inform verification, but MUST NOT silently overwrite canonical values. Observed state is stored separately from canonical state (observation mechanics: CDS-500 §14–§15).

**CDS200-R004** Canonical information MUST be stored once and projected many times.

**CDS200-R005** A field that exists only because one channel requires it SHOULD be represented as a channel field or mapping (`CH_` scope, CDS-300), not as canonical product truth.

*Informative note:* a Google product category is normally a channel taxonomy mapping. Material, colour and dimensions are normally canonical facts.

## 4. Core Entity Model *(normative)*

CDS defines a logical entity model rather than a flat product table.

**CDS200-R006** An implementation MAY store data physically in relational tables, documents, graphs or spreadsheets, but MUST preserve the logical entities below and the rules attached to them.

| Entity | Role | Detail home |
|---|---|---|
| Product | The logical commercial item and parent information record. | CDS-200 §5 |
| Variant | A sellable unit identified by its variant option values. | CDS-200 §5 |
| Attribute Definition | The first-class schema, behaviour and governance record for an attribute. | CDS-200 §7 |
| Attribute Value | A product- or variant-level value conforming to an Attribute Definition, with provenance. | CDS-200 §7 |
| Dictionary | A governed, versioned set of canonical values, aliases and projections. | CDS-400 |
| Alias Mapping Record | The governed mapping from a source value to exactly one canonical value. | CDS-400 |
| Facet Definition | A customer-facing grouping and filter behaviour. | CDS-600 |
| Category | A node in a taxonomy (internal or external). | CDS-200 §6 |
| Taxonomy Mapping | A relationship between an internal category and an external taxonomy node. | CDS-200 §6 |
| Taxonomy Decision Log | The recorded tie-break decisions for primary-category assignment. | CDS-200 §6 |
| Channel | A downstream consumer of published product information. | CDS-500 |
| Publication Record | The immutable record of one publication attempt. | CDS-500 §8 |
| Observation Record | The state read back from a downstream channel, stored separately. | CDS-500 §15 |
| Verification Result | The comparison of expected versus observed values. | CDS-500 §16–§17 |
| Override Record | A governed redirection of the expected channel value. | CDS-500 §22 |
| Authority Declaration | The per-fact declaration of the mastering system (and any delegation). | CDS-200 §13 |
| Rule | A validation, inheritance, transformation or publication condition. | CDS-200 §15 |

**CDS200-R007** Tags MUST be governed projections generated from canonical data (e.g. `collection_*` signals regenerated from classification rules) and MUST NOT serve as the primary store for structured product facts. Tag governance is defined in CDS-400; tag publication and merge semantics in CDS-500.

## 5. Product and Variant Boundaries *(normative)*

A Product is a logical record shared by all sellable forms. A Variant is a sellable unit with its own SKU or documented sellable-unit key (CDS-100 §2).

**CDS200-R008** A difference MUST create a distinct sellable unit before it is modelled as a variant option. Attributes that do not produce a separately sellable unit MUST NOT be modelled as variant options merely to make them filterable (filterability is a facet concern — CDS-600).

**CDS200-R009** A Product with no variant options has exactly one variant, which MAY be implicit in storage but MUST be countable as a variant for publication and verification purposes.

**CDS200-R010** Product-level attribute values MUST describe facts shared by all variants of the product.

**CDS200-R011** Variant-level attribute values MUST describe facts specific to the sellable unit, and MUST be stored as canonical `value_id`s (never raw source spellings) per ADR-D4.

**CDS200-R012** Where a variant-scoped attribute (such as colour on a multi-colour product) is presented at product level for display, faceting or search, the product-level value MUST be a projection derived from the variant values and MUST NOT be an independently authored canonical fact.

```
Product: Linen Shirt
  Product attribute values (facts shared by all variants):
    MF_material      = material_linen
    MF_fit           = fit_relaxed
    MF_sleeve_length = sleeve_long
  Variants (canonical value_ids per ADR-D4):
    SKU-001: VAR_colour = colour_french_navy, VAR_size = size_s
    SKU-002: VAR_colour = colour_french_navy, VAR_size = size_m
    SKU-003: VAR_colour = colour_white,       VAR_size = size_s
  Product-level projections (derived from variants, never authored):
    MF_colour_display = "French Navy / White"     (display projection)
    MF_colour_family  = [blue, white]             (facet projection)
```

*Informative note:* style, occasion and fit usually describe the product. Size and sellable colour commonly define variants. In v0.1 this chapter's worked examples treated colour as both a variant option and an authored product-level value on a multi-colour product; R012 resolves that contradiction — the variant values are canonical, the product-level colour fields are derived projections.

## 6. Classification Architecture *(normative)*

Classification answers *what the product is*. CDS separates internal classification from external taxonomy mappings and from customer-facing merchandising collections.

**CDS200-R013** An implementation MUST maintain an internal taxonomy that is independent of any channel taxonomy. Core requirements in this section bind to *an internal taxonomy*, not to any particular tier structure.

**CDS200-R014** The three-tier shape **Product Family → Product Type → Category** (e.g. Apparel → Shirt → Linen Shirts) SHOULD be adopted as the recommended profile shape; industry profiles (CDS-1500) refine it. Implementations MAY use a different documented internal structure without loss of conformance to this section.

**CDS200-R015** A product MUST have exactly one primary internal category.

**CDS200-R016** The primary category SHOULD be the most specific applicable node — a node none of whose child nodes applies to the product.

**CDS200-R017** Where more than one category could serve as the primary category, the assignment MUST be resolved using an **organisation-declared, documented, ordered set of tie-break rules**, applied in order until one yields a decision and applied consistently across the catalogue. The following ordering is the **recommended default** *(informative)*:

1. **Customer mental model** — the category the customer would navigate to or search within when intending to buy the product.
2. **Dominant use** — the function the product is primarily designed to perform.
3. **Material / form** — what the product physically is, where use is ambiguous.
4. **Commercial priority** — where the product's assortment peers sit and where it best serves the range plan.

> RESOLVED (was D30 (resolved), owner decision 2026-08-04): the standard requires only *an* organisation-declared documented order (matching the legacy production discipline); the four-rule ordering above is demoted to recommended default. The owner noted this may be revisited after practical use.

**CDS200-R018** Every tie-break decision MUST be recorded in a taxonomy decision log entry carrying at least: the product type or product concerned, the category chosen, the rule applied, and the date. Subsequent products matching a logged entry MUST follow it; changing the decision requires a superseding log entry, not an ad-hoc different assignment.

**CDS200-R019** A product MAY additionally hold **secondary category placements**. Secondary placements are non-projecting: they MUST NOT drive external taxonomy mappings, required-attribute inheritance or collection projection unless a rule explicitly and individually opts a placement in.

**CDS200-R020** External taxonomy identifiers (channel or standard taxonomies) MUST be stored as Taxonomy Mappings from internal categories (or products) and MUST NOT replace the internal taxonomy. Category-level mappings MAY be inherited by child categories.

**CDS200-R021** A product MAY carry a per-channel taxonomy mapping override where the category-level mapping is wrong for that specific product on that specific channel. Such an override MUST be recorded as a governed override record (CDS-500 §22), scoped to product + channel.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): R021 reuses the CDS-500 §22 override record for taxonomy overrides rather than defining a separate taxonomy-override record; the alternative is a dedicated field on Taxonomy Mapping.

**CDS200-R022** A product MAY appear in multiple collections without being assigned multiple primary categories. Collections are merchandising groupings and MUST NOT redefine classification (presentation rules: CDS-600).

```
Internal category:  Apparel > Tops > Shirts
     |
     +-- external taxonomy mappings (per channel; inherited or overridden)
     +-- inherited attribute family / required-attribute rules
     +-- collection projection rules (governed tags per R007)
```

*Informative note — taxonomy overlap vs merchandising overlap.* If a product genuinely *belongs* in two categories, the category boundaries overlap and should be fixed. If a product merely *appeals* to two audiences, that is a merchandising concern: keep one primary category and reach the second audience via collections, governed tags and cross-links — never via a second primary category.

## 7. Attribute Architecture *(normative)*

Attributes are governed by Attribute Definitions. The definition is a first-class entity and carries more intelligence than the product record itself.

| Definition property | Purpose |
|---|---|
| identifier | Stable semantic key (registered per CDS-300). |
| label | Human-readable name. |
| description | Plain-language purpose. |
| scope | Product, variant, category, channel or system. |
| data type | Text, number, boolean, date, measurement, reference, list or structured object. |
| cardinality | Single or multiple values. |
| dictionary | Optional controlled value source (CDS-400). |
| requiredness | Required, conditionally required or optional. |
| inheritance | Whether a value may inherit from category, family or parent. |
| validation | Format, range, units, dependencies and exclusions. |
| display behaviour | Whether and how the value appears on product pages. |
| facet behaviour | Whether and how the value participates in filtering (CDS-600). |
| search behaviour | Indexing, synonyms and weighting. |
| publication mapping | Destination fields and transformations per channel (CDS-500). |
| channel source layer | Which value layer (canonical, display, facet) feeds each channel (ADR-D4). |
| comparison strategy | Exact, normalised text, numeric, set, ordered list or identifier (CDS-500 §16). |
| authority / delegation | The fact's declared authority and any recorded delegation (§13). |
| AI behaviour | Extractability, confidence threshold and review requirement (CDS-700). |

**CDS200-R023** Every governed attribute MUST have an Attribute Definition.

**CDS200-R024** Products and variants MUST store values; Attribute Definitions MUST store behaviour.

**CDS200-R025** A channel mapping SHOULD be defined on the Attribute Definition rather than repeated on every product.

**CDS200-R026** The Attribute Definition MUST declare which value layer feeds each consuming channel (canonical value, display label or facet value); channels are never fed implicitly from the facet layer (ADR-D4).

## 8. Dictionaries and Value Layers *(informative)*

Canonical values, alias mappings, display labels, facet values, search synonyms and channel representations follow the branch model **Source Value → Alias Mapping Record → Canonical Value → parallel projections** defined normatively in CDS-400 (model) and CDS-100 §3 (terms), per ADR-D4. This chapter's architecture consumes that model; it does not restate it.

## 9. Facets and Customer Experience *(informative)*

Facets are governed projections of canonical data, designed for customer usability — never a blind exposure of every distinct internal value. Facet architecture, dictionary design and presentation rules are defined in CDS-600, with facet-mapping governance in CDS-400.

## 10. Channel and Publication Architecture *(informative)*

A Channel consumes versioned projections of canonical data: canonical data → field mapping → expected channel state → publish → observe → verify. Expected-state calculation, publication records, acknowledgement semantics ("an acknowledgement is not proof") and repair are defined normatively in CDS-500.

## 11. Verification and Channel Health *(informative)*

Verification compares expected channel state with observed downstream state, field by field, under declared comparison strategies. The single normative verification status enum, reason codes, traffic-light mapping and channel-health aggregation are owned by CDS-500 §16–§18 (per ADR-D3) and CDS-1400. This chapter defines no status vocabulary.

## 12. Semantic Namespace Layer *(informative)*

Every visible field identifier belongs to a registered semantic namespace (e.g. `STD_`, `CAT_`, `VAR_`, `MF_`, `CH_`, `QA_`). The single normative prefix registry, the identifier grammar and casing rules, registry validation (the testable mechanism replacing v0.1's "prefix must communicate purpose" wording), and the visible-identifier / human-label / machine-key separation are all owned by CDS-300. Namespace-prefixed identifiers appearing in this chapter's examples are illustrative uses of that registry.

## 13. Data Ownership and Authority *(normative)*

Authority is declared **per fact**, not per system. The PIM is the system of record for canonical product information; specialised systems may own operational facts such as live inventory or order state, which the PIM observes but does not master.

| Information | Typical authority |
|---|---|
| Product identity, classification and descriptive attributes | PIM |
| Channel mappings and publication configuration | PIM |
| Product content and media sequencing | PIM unless explicitly delegated |
| Inventory quantity | Inventory or warehouse authority |
| Orders and customers | Commerce platform or order-management authority |
| Observed downstream state | Channel connector read-back (CDS-500) |
| Verification status | PIM verification engine (CDS-500) |

**CDS200-R027** Every governed product fact MUST have exactly one declared authority, recorded on the Attribute Definition or in an equivalent authority matrix.

**CDS200-R028** Two systems MUST NOT simultaneously claim authoritative ownership of the same product fact.

**CDS200-R029** Delegation of authority MUST be an explicit recorded declaration on the Attribute Definition or authority matrix, carrying at least: the delegated fact scope, the delegate system, the approving owner, the effective date and a review date. Undeclared delegation is non-conformant; "the other system just edits it" is not delegation.

**CDS200-R030** A channel-specific deviation from the projected canonical value MUST be expressed as a governed override record as defined in CDS-500 §22 (scope, replacement value, reason, owner, approval, time bounds, verification expectation). A downstream edit to a PIM-owned field without an active override record is drift (CDS-500 §11).

**CDS200-R031** Read-back (observed) values MUST be stored separately from canonical values (observation record: CDS-500 §15). See also R003.

## 14. State, Versioning and Audit *(normative)*

Commerce information changes over time; versioning and audit metadata are first-class architecture. Canonical records carry a revision identifier, change timestamps and the actor or process responsible; publication, observation and verification timestamps per channel are defined by the CDS-500 record set.

**CDS200-R032** An implementation MUST be able to determine which canonical revision produced a published channel state (record linkage: CDS-500 §8).

**CDS200-R033** Mappings and dictionaries SHOULD be versioned, because changes to them alter downstream output without changing the product record (dictionary versioning: CDS-400; mapping-set versioning: CDS-500).

## 15. Rules and Validation *(normative)*

Rules define requirements, inheritance, transformations and publication conditions, evaluated against the canonical model and channel profiles.

```
IF CAT_product_family = apparel
THEN REQUIRE MF_material, MF_colour, MF_care_instructions

IF CAT_product_type = candle
THEN REQUIRE MF_wax_type, MF_burn_time

IF MF_material = material_leather
THEN REQUIRE MF_country_of_origin
```

**CDS200-R034** Conditional requirements MUST be represented as explicit rules rather than undocumented staff knowledge.

**CDS200-R035** Validation errors MUST distinguish missing, invalid, conflicting and unmapped values.

**CDS200-R036** Rules SHOULD operate on canonical values and declared channel projections, not on uncontrolled display text.

*Informative note:* channel-imposed identifier requirements (for example Google Merchant Center's GTIN/MPN/brand rules) are platform policy, not core architecture; they are specified, dated and verified in the relevant CDS-900 platform profile and expressed here only as ordinary conditional rules bound to that profile.

## 16. AI Participation *(informative)*

AI may assist with extraction, classification, enrichment, mapping suggestions and anomaly detection — always as a proposer, never as an authority merely because it generated a value. All normative AI requirements (proposal separation, evidence, confidence, review, autonomy levels, publication restrictions) are owned by CDS-700. AI-proposed values conform to the same Attribute Definitions and dictionaries as human-entered values; that requirement is stated normatively in CDS-700.

## 17. End-to-End Examples *(informative)*

### 17.1 Apparel colour (per ADR-D4)

```
Source value (supplier)      = "French Navy"
Alias mapping record         = "French Navy" -> colour_french_navy
Variant stores               : VAR_colour = colour_french_navy   (canonical value_id)
Display projection           : MF_colour_display = "French Navy"
Facet projection (product)   : MF_colour_family = [blue]         (derived from variants)
Channel representation       : CH_google_colour = "Blue"         (layer declared per R026)
Verification (CDS-500)       : QA_shopify_colour = MATCH
```

On a multi-colour product, `VAR_colour` differs per variant and `MF_colour_family` derives the full set (e.g. `[blue, white]`) — the product-level fields are never authored directly (R012).

### 17.2 Homewares material

```
Source value                 = "Tasmanian Oak"
Canonical value              : MF_material = material_oak
Display projection           : MF_material_display = "Tasmanian Oak"
Facet projection             : MF_material_family = wood
Channel representations      : Shopify "Oak"; Google "Wood" (declared per attribute)
Search synonyms              : timber, oak, tasmanian oak
```

### 17.3 Category assignment and projection

```
Candidate categories         : Homewares > Living Room > Cushions
                               vs Homewares > Textiles > Soft Furnishings
Tie-break (R017)             : rule 1, customer mental model -> Cushions
Decision log entry (R018)    : "Cushions | Living Room > Cushions | customer mental model | 2026-08-04"
Primary category             : Homewares > Living Room > Cushions
Derived outputs              : CAT_product_type = cushion
                               CH_shopify_category = Home & Garden > Decor > Throw Pillows
                               CH_google_product_category = Home & Garden > Decor > Decorative Pillows
                               Collection projection = Cushions (governed tag, R007)
                               Required attributes = colour, material, shape, dimensions, fill
```

### 17.4 Round-trip verification

```
Canonical value              : colour_navy
Expected Shopify value       : "Navy"
Observed Shopify value       : "navy"
Comparison strategy          : case-insensitive canonical text
Result                       : MATCH  (statuses and traffic light: CDS-500 §17–§18)
```

## 18. Conformance *(informative)*

The conformance criteria for this chapter are its requirement identifiers CDS200-R001–R036. Conformance levels, test suites and claim rules are defined solely in CDS-1000; machine-readable expression of this chapter's entities in CDS-1100.

*Architecture decisions:* the decisions underlying this chapter (PIM-first mastering, value layers, status vocabulary, DF_→CH_) are recorded in the single global ADR register (CDS000-R006) — see ADR-D3, ADR-D4, ADR-D24.

*Platform notes:* Shopify-specific implementation guidance formerly in Appendix A (taxonomy mapping targets, metafield publication, Search & Discovery facet consumption, read-back population) lives in the CDS-900 Shopify profile. The tags rule formerly there is now normative as R007.

*Legacy alignment:* the legacy Airtable PIM prefix mapping tables and migration alignment formerly in Appendix B live in the migration annex (CDS-1300).


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-300 — Semantic Namespaces and Field Naming

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-300 Working Draft v0.1; the namespace registry tables formerly duplicated in CDS-000, CDS-200 and CDS-900 (this chapter is the single normative registry per CDS000-R005) |
| Normative status | §3–§23 are normative. §1, §2, §24 and §25 are informative. |
| Findings addressed | 300-1 (ADR-D2), 300-2 (D7), 300-3, 300-4 (ADR-D24), 300-5 (D6), 300-6, 300-7 (D8), 300-8, 300-9; Matrix 1 (all rows); REVIEW-002A LEG-1, LEG-3; CDS-700 §22 registration request |

---

## 1. Purpose and Scope *(informative)*

CDS-300 defines how commerce fields are named so that their purpose is immediately apparent to humans, deterministic for software and semantically useful to AI. Names are part of the user interface (CDS-P-04): a visible identifier is a compact explanation of why the field exists, which domain owns it and, where necessary, which destination consumes it.

```
MF_material
CH_google_product_category
QA_shopify_material
WF_copy_review
SYS_updated_at
```

This chapter is the **single normative home of the CDS namespace prefix registry** (CDS000-R005). Other chapters cite the registry; they do not restate it. Platform mapping tables live in CDS-900 profiles; they map registered prefixes, they never define them.

The naming system is a visible presentation layer over the information architecture of CDS-200. Implementations need not use identical physical column names, but visible identifiers and exported field names preserve the same semantics (§8).

## 2. Design Requirements *(informative)*

| Requirement | Meaning |
|---|---|
| Human recognisability | A new operator infers the field purpose within seconds. |
| Machine safety | Identifiers never require escaping in spreadsheets, CSV, JSON, SQL, APIs or common languages. |
| AI legibility | Semantic purpose is inferable from the identifier plus its schema metadata. |
| Stable sorting | Related fields group naturally when sorted alphabetically. |
| Durability | Names describe business purpose, not temporary delivery technology. |
| Brevity | Short enough to scan, never cryptic. |
| Extensibility | Organisations and channels extend the registry without collisions. |
| Migration clarity | Deprecated identifiers map explicitly to replacements. |

Uppercase prefixes create strong visual grouping; the lowercase snake_case remainder is readable and portable. Names optimise for recognition and scanning before typographic elegance. Abbreviations appear only where obvious to the commerce audience or standardised by CDS.

## 3. Identifier Grammar *(normative)*

The visible CDS field identifier grammar:

```
<NAMESPACE>_<field_name>
CH_<channel>_<field_name>      (channel form)
QA_<channel>_<field_name>      (verification form)
```

**CDS300-R001** A visible field identifier MUST communicate its semantic role without requiring ordinary users to consult a separate document during routine work.

**CDS300-R002** The namespace segment MUST be two to eight uppercase ASCII characters, MUST begin with a letter, and MUST be followed by a single underscore separator.

**CDS300-R003** The field-name portion SHOULD use lowercase snake_case. The first field-name segment MUST begin with a lowercase letter; subsequent segments MAY be numeric (e.g. `CH_google_custom_label_0`).

**CDS300-R004** The complete identifier MUST NOT contain spaces, colons, equals signs, dots, slashes, backslashes, commas or Unicode punctuation, and MUST use only ASCII letters, digits and underscores unless a profile explicitly permits another character set.

**CDS300-R005** Identifiers MUST match the regular expression:

```
^[A-Z][A-Z0-9]{1,7}_[a-z][a-z0-9]*(?:_[a-z0-9]+)*$
```

This expression is a **syntactic superset**; the registry refines it: an identifier is valid only when its namespace segment is a registered prefix (§22). *(Resolves finding 300-8: the pattern now encodes the 2–8 character namespace bound and the letter-initial first field segment previously stated only in prose.)*

**CDS300-R006** A field registry MUST enforce identifier uniqueness case-insensitively.

**CDS300-R007** Hyphens MAY appear inside controlled values and tags where CDS-400 permits, but SHOULD NOT be used as a field-name separator.

**CDS300-R008** Names MUST NOT use positional codes such as `field_1`, `misc_2` or `data_a` as permanent identifiers.

| Identifier | Assessment |
|---|---|
| `MF_material` | Conformant |
| `CH_google_product_category` | Conformant |
| `mf_material` | Not the visible profile (see §8 lossy targets) |
| `MF.Material`, `MF:material`, `MF=material`, `MF material` | Non-conformant |
| `CH_Google_Product_Category` | Non-conformant |

## 4. Core Namespace Registry *(normative)*

This table is the normative CDS prefix registry. It resolves every registry divergence catalogued in the v0.2 review (Matrix 1): the STD_/MF_ boundary (ADR-D2), DF_→CH_ (ADR-D24), the QA_ grammar (D7), PRC_/INV_ membership, AI_ adoption, IMPORT_ and OBS_ registration, and reservation of the full core set.

| Prefix | Status | Semantic domain | Example |
|---|---|---|---|
| STD_ | Core | Core product field set, defined by the closed enumeration in §5. Platform-neutral: whether a channel stores an STD_ field natively is a profile mapping concern (CDS-900), never part of the definition. | `STD_title` |
| CAT_ | Core | Internal classification and taxonomy assignments (not external taxonomy mappings — those are CH_). | `CAT_product_type` |
| VAR_ | Core | Variant and sellable-unit fields. | `VAR_size` |
| MF_ | Core | Extended structured product attributes in the canonical model, mechanism-neutral (§10, ADR-D2). | `MF_material` |
| CH_ | Core | Channel-specific mapping, output, override and feed projection (§9, ADR-D24). | `CH_google_product_category` |
| SEO_ | Core | Metadata whose primary purpose is search presentation, indexing or discoverability. **Caution:** legacy fields named `SEO` (`DF_Airtable_SEO_*`) were data-feed fields, not search metadata (REVIEW-002A LEG-3); they migrate to CH_, never to SEO_. | `SEO_title` |
| MED_ | Core | Media assets and media-specific metadata. | `MED_primary_image` |
| PRC_ | Core (conditional) | Pricing and commercial amounts. Registered for use only where the PIM is the declared authority or governed integration surface for pricing (CDS-200 authority model). | `PRC_retail_price` |
| INV_ | Core (conditional) | Inventory and availability. Same authority condition as PRC_. | `INV_available_quantity` |
| WF_ | Core | Workflow and operational state. | `WF_copy_review` |
| QA_ | Core | Field-level channel verification results only, grammar `QA_<channel>_<field_name>` (§13). | `QA_shopify_material` |
| SYS_ | Core | System identifiers, technical metadata and computed quality metrics (§12). | `SYS_updated_at` |
| AI_ | Core | AI proposals, provenance, confidence and workflow metadata (§15; rules in CDS-700). | `AI_material_suggestion` |
| IMPORT_ | Core | Ingested source records and intake provenance (§16). | `IMPORT_supplier_colour` |
| OBS_ | Core | Observed channel state captured by read-back (§16; observation model in CDS-500). | `OBS_shopify_material` |
| CDS_ | Reserved | Standard metadata and conformance artifacts. | `CDS_version` |
| TMP_ | Reserved | Temporary migration data; prohibited in published schemas. | — |
| LEG_ | Reserved | Explicit legacy-compatibility fields. | `LEG_df_google_category` |
| EXT_ | Reserved | Generic extension metadata; not a substitute for a meaningful namespace. | — |
| CMP_ | Recommended extension | Compliance and regulatory data. | `CMP_country_of_origin` |
| SUP_ | Recommended extension | Supplier and sourcing data. | `SUP_supplier_sku` |
| DICT_ | Recommended extension | Dictionary and reference-data entities. Dictionary value identity itself is governed by CDS-400 (`value_id`); DICT_ names dictionary *entities* where an implementation surfaces them as fields. | `DICT_colour_canonical` |
| DF_ | Deprecated (legacy alias) | Legacy data-feed layer prefix; replaced by CH_ for all new design (ADR-D24). Registered so §22 validation accepts sanctioned migration aliases. | `DF_google_product_category` → `CH_google_product_category` |
| Match_ | Deprecated (legacy alias) | Legacy verification traffic lights; replaced by QA_ verification fields backed by CDS-500 verification records. | `Match_SEO_title` → `QA_google_title` |
| Airtable_ (incl. `MF_Airtable_*`, `DF_Airtable_SEO_*`, `Import_*`, `Shopify_*`) | Deprecated (legacy alias) | Legacy Airtable PIM field families; alias targets per §21. | `MF_Airtable_material` → `MF_material` |

> RESOLVED — accepted as drafted (owner 2026-08-04; was D6 (resolved)): OBS_ is registered here as the observed-channel-state namespace on the strength of the legacy `Shopify_*` mirror-column precedent (REVIEW-002A); prior drafts used "OBS" without defining it. Alternative: leave observed state entirely to CDS-500 record structures with no visible prefix.

**CDS300-R009** Every visible field identifier MUST belong to a prefix registered in this registry or in the implementation's extension registry (§20). *(Upholds CDS-P-09.)*

**CDS300-R010** An implementation MUST maintain a namespace registry identifying, for every visible prefix: meaning, owner, allowed scope, publication behaviour, lifecycle status (active, deprecated, reserved) and — for deprecated prefixes — replacement and deprecation date.

**CDS300-R011** A field MUST use the namespace that describes its semantic responsibility, not its current storage location or delivery mechanism.

**CDS300-R012** WF_, QA_, SYS_, AI_, IMPORT_ and OBS_ fields MUST NOT be published to customer-facing channels unless a channel profile explicitly requires them.

## 5. The STD_ Closed Enumeration *(normative)*

Per ADR-D2, STD_ is defined by a **closed enumeration** published in this registry — never by a judgement about "core-ness". Anything structured and not in the enumeration is MF_.

**CDS300-R013** The STD_ namespace MUST contain exactly the fields enumerated in the STD_ registry table. Adding or removing an STD_ field is a registry change under CDS-800 change control.

Initial registry content at v0.2 (the starter enumeration; final list fixed at v0.2 freeze):

| Identifier | Meaning |
|---|---|
| `STD_id` | Product identity: the primary commercial identifier (product-level SKU or equivalent; variant SKUs are `VAR_sku`) |
| `STD_title` | Product title |
| `STD_description` | Product description |
| `STD_brand` | Brand |
| `STD_vendor` | Vendor / supplier of record |
| `STD_primary_category_ref` | Reference to the primary internal category (assignment detail lives in CAT_) |
| `STD_media_set` | Reference to the product's governed media set (media items live under MED_) |
| `STD_status` | Lifecycle status of the product record |

**CDS300-R014** A structured product attribute not present in the STD_ enumeration MUST use MF_ (or a more specific registered namespace whose domain it belongs to).

The v0.1 namespace-selection decision tree is deleted (ADR-D2): it was undecidable (`MF_material` matched both "canonical core fact" and "published as metafield"). Namespace assignment is a registry lookup, never a judgement call — which is also how the boundary was successfully maintained in production.

## 6. Field Name Construction *(normative)*

**CDS300-R015** The field-name portion SHOULD state the product fact or operational purpose in plain, specific language, using terminology defined by CDS-100/CDS-400 or by the applicable channel specification.

**CDS300-R016** Acronyms such as SKU, GTIN, MPN, URL and SEO MAY be retained where widely recognised; other unexplained abbreviations SHOULD NOT be used.

| Preferred | Avoid | Reason |
|---|---|---|
| `MF_material` | `MF_mat` | Unexplained abbreviation. |
| `CH_google_product_category` | `CH_google_cat` | Preserve the actual channel concept. |
| `QA_shopify_material` | `QA_mat_status` | Identify the verification target. |
| `WF_photography_required` | `WF_photo` | State the workflow condition. |
| `SYS_last_verified_at` | `SYS_lva` | Readable outside the originating system. |

## 7. Case and Separators — see §3 *(normative)*

Case, separator and character-set rules are part of the identifier grammar (CDS300-R002–R008). This casing rule is stated normatively only here; CDS-000 carries it as principle CDS-P-09/P-10 without restating it. *(Resolves finding 300-9.)*

## 8. Semantic Identifier, Human Label and Machine Key *(normative)*

CDS distinguishes three things (definitions: CDS-100 §4): the **Semantic Identifier** (visible, namespace-prefixed), the **Human Label** (natural language) and the **Machine Key** (internal storage/transport key). They MAY differ, provided their relationship is explicit.

```
Semantic identifier:  MF_care_instructions
Human label:          Care instructions
Machine key:          product.attributes.care_instructions
Channel mapping:      custom.care_instructions        (profile concern, CDS-900)
```

**CDS300-R017** Every machine key exposed to users MUST have a stable semantic identifier or an equally self-describing equivalent.

**CDS300-R018** A human label MAY contain spaces and title case but MUST NOT replace the semantic identifier in exports or integrations.

**CDS300-R019** The mapping between semantic identifier, machine key and channel destination MUST be discoverable from the Attribute Definition or field registry.

**CDS300-R020** Exports and integrations SHOULD preserve identifier case. Where a target is lossy (e.g. a platform that case-folds keys), an export MAY apply case-folding **only where the registry or Attribute Definition declares a reversible mapping** between the semantic identifier and the folded form; the folded form then round-trips deterministically. *(Resolves finding 300-6; upholds CDS-P-09.)*

## 9. Channel Namespace (CH_) *(normative)*

CH_ identifies information whose semantic responsibility belongs to a specific downstream channel: taxonomy mappings, required outputs, custom labels, channel-only overrides, publication configuration and feed-column projections.

```
CH_shopify_product_category
CH_shopify_title_override
CH_google_product_category
CH_google_custom_label_0
CH_meta_product_category
CH_amazon_browse_node
```

**CDS300-R021** The first field-name segment after `CH_` MUST identify the channel using its registered lowercase channel key.

**CDS300-R022** Channel keys MUST remain stable even when the technical transport changes (file feed, API or otherwise).

**CDS300-R023** CH_ MUST NOT be used for a canonical attribute merely because that attribute is sent to a channel; a canonical fact used by many channels remains canonical and SHOULD NOT be duplicated under multiple CH_ fields unless distinct channel representations are required.

**CDS300-R024** A field is a feed-layer projection if and only if it is a literal serialized feed column; such projections live under CH_, and the feed artifact is verified end-to-end at the formatted-output layer (verification model: CDS-500). *(ADR-D24, replacing the untestable "retain DF_ where useful".)*

CH_ replaces the legacy DF_ ("Data Feed") prefix for all new design (ADR-D24): "channel" names the durable business destination; "data feed" named one delivery implementation. DF_ remains a registered deprecated prefix for migration aliases (§21).

## 10. Extended Attribute Namespace (MF_) *(normative)*

MF_ identifies **extended structured product attributes in the canonical model**. The definition is mechanism-neutral: it says nothing about how any platform stores or publishes the attribute.

```
MF_material
MF_pattern
MF_fit
MF_care_instructions
MF_colour_display
MF_colour_family
```

Per ADR-D2 this is an explicit **redefinition, not an inheritance**: in the legacy system MF_ literally meant a platform metafield. The prefix letters are retained for operator familiarity and legacy-mapping continuity; the meaning is now defined solely by this registry. Typical projections of MF_ attributes to metafield-like channel structures are documented informatively in the relevant CDS-900 profile.

**CDS300-R025** MF_ fields MUST describe product information — never integration status, workflow state or system metadata.

**CDS300-R026** An MF_ field SHOULD be backed by an Attribute Definition (CDS-200 §7) declaring type, cardinality, dictionary binding, display, facet and channel mappings.

**CDS300-R027** Where a channel publishes an MF_ attribute as a native or standard field, that is the channel profile's mapping concern; the canonical prefix MUST NOT change.

## 11. Classification and Variant Namespaces (CAT_, VAR_) *(normative)*

```
CAT_product_family      VAR_sku
CAT_product_type        VAR_size
CAT_season              VAR_colour
                        VAR_barcode
```

**CDS300-R028** CAT_ MUST be used for internal classification and taxonomy assignments, not external taxonomy mappings (those are CH_).

**CDS300-R029** VAR_ MUST be used for values specific to a sellable unit or variant option (variant boundary rule: CDS-200 §5).

## 12. Workflow and System Namespaces (WF_, SYS_) *(normative)*

```
WF_copy_review           SYS_product_id
WF_photography_status    SYS_created_at
WF_publish_approval      SYS_last_published_at
                         SYS_completeness_score
```

**CDS300-R030** WF_ fields MUST describe work state, responsibility or approval.

**CDS300-R031** SYS_ fields MUST represent technical identity, timestamps, versions, process metadata or **computed quality metrics** (e.g. `SYS_completeness_score`), and SHOULD remain hidden from customer-facing channels.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D7 (resolved)): Quality metrics (formerly `QA_completeness_score`) are homed under SYS_ so that QA_ can carry a single channel-verification grammar. Alternative considered: a formal two-shape QA_ grammar, rejected as re-introducing the parse ambiguity of finding 300-2.

## 13. Verification Namespace (QA_) *(normative)*

QA_ is reserved exclusively for field-level channel verification results. It has exactly one grammar:

```
QA_<channel>_<field_name>

QA_shopify_material
QA_google_gtin
QA_meta_availability
```

**CDS300-R032** A QA_ identifier MUST use the form `QA_<channel>_<field_name>`, where `<channel>` is a registered channel key. No other QA_ shape is valid. *(Resolves finding 300-2: the v0.1 registry's own example `QA_completeness_score` would have failed the v0.1 §21 validation; it is now `SYS_completeness_score`.)*

**CDS300-R033** The associated verification record MUST retain expected value, observed value, detailed status, comparison strategy and timestamps even where a UI shows only a traffic-light symbol. Status vocabulary and traffic-light mapping are defined solely in CDS-500.

**CDS300-R034** Legacy `Match_` prefixes MAY be accepted as deprecated aliases (§21) but MUST NOT be used in new design.

## 14. Search, Media, Pricing and Inventory Namespaces *(normative)*

```
SEO_title                MED_primary_image      PRC_retail_price        INV_available_quantity
SEO_description          MED_alt_text           PRC_compare_at_price    INV_backorder_allowed
SEO_search_synonyms      MED_sort_order         PRC_cost_price          INV_expected_restock_at
```

**CDS300-R035** SEO_ MUST be used only for metadata whose primary purpose is search presentation, indexing or discoverability. Legacy fields containing the token "SEO" MUST be classified by actual responsibility before migration — production `DF_Airtable_SEO_*` fields were feed fields and migrate to CH_ (REVIEW-002A LEG-3).

**CDS300-R036** MED_ MUST be used for media assets and media-specific metadata.

**CDS300-R037** PRC_ and INV_ MUST be used only when the PIM is the declared authority or governed integration surface for those domains (CDS-200 authority model). Where it is not, price and inventory facts observed from their mastering systems use OBS_ or remain outside the visible registry.

## 15. AI Namespace (AI_) *(normative)*

AI_ is formally registered as a core namespace for AI proposals, provenance, confidence and workflow metadata. This satisfies the registration requested by CDS-700 §22, resolves finding 300-5, and follows the legacy `Automated_` precedent (machine-generated content state was a production concern, not a novelty).

```
AI_material_suggestion    AI_review_status     AI_generated_at
AI_material_confidence    AI_model_id          AI_reviewed_by
AI_material_evidence      AI_workflow_version
```

**CDS300-R038** AI_ fields MUST represent proposals, provenance, confidence or workflow metadata; they MUST NOT replace the canonical field namespace. On acceptance, the value is stored in its semantic canonical field (e.g. `MF_material`) with AI provenance retained per CDS-700.

All AI governance rules — proposal lifecycle, evidence, confidence, review, autonomy — are defined solely in CDS-700.

## 16. Ingestion and Observation Namespaces (IMPORT_, OBS_) *(normative)*

**IMPORT_** names ingested source records and intake provenance — the raw layer before normalisation (value layers: CDS-400). It formalises the load-bearing legacy `Import_*` production namespace (REVIEW-002A) that earlier drafts used (CDS-900 "Layer 1: IMPORT_") without ever registering.

**OBS_** names observed channel state captured by read-back — the legacy `Shopify_*` mirror-column pattern, generalised across channels. Observation semantics, coverage states and the never-overwrite rule are defined solely in CDS-500.

```
IMPORT_supplier_colour = "French Navy"
OBS_shopify_material   = "linen"
```

**CDS300-R039** IMPORT_ fields MUST retain source provenance and MUST NOT be treated as canonical values; promotion to canonical goes through the value-layer model (CDS-400).

**CDS300-R040** OBS_ fields MUST hold observed downstream state only and MUST NOT silently overwrite canonical values (CDS-500; CDS-P-02).

## 17. Dictionary-Backed Field Naming *(normative)*

Dictionary-backed fields distinguish canonical, display and facet purposes; dictionary value identity (`value_id`) and layer semantics are governed by CDS-400.

```
MF_colour_canonical
MF_colour_display
MF_colour_family
```

**CDS300-R041** Where separate fields are materially required, the suffix MUST identify display, canonical or facet purpose explicitly.

**CDS300-R042** Implementations SHOULD NOT persist redundant per-product representations that the dictionary can derive deterministically.

## 18. Localisation *(normative)*

Localisation is modelled as an **Attribute-Definition dimension** — a locale axis on the attribute's value, declared in the Attribute Definition and represented per the localised-text contract in CDS-1100. It is not encoded in the identifier, and **LOC_ is not a registered prefix**: identifier-encoded locales (`LOC_fr_title`) scale combinatorially (fields × locales) and had no grammar or locale registry.

**CDS300-R043** Locale MUST NOT be encoded in the visible field identifier; localised values are dimensions of one identifier, declared in the Attribute Definition.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D8 (resolved)): Localisation as an Attribute-Definition dimension (LOC_ unregistered) is the call made here, resolving finding 300-7. Alternative: identifier-encoded locales with a formal grammar and locale registry.

## 19. Scope, Inheritance and Cardinality *(normative)*

Field names do not encode every schema property; scope, inheritance and cardinality belong in the Attribute Definition (CDS-200 §7).

```
MF_material               VAR_size
  scope: product            scope: variant
  cardinality: multiple     cardinality: single
  inheritance: family       inheritance: none
```

**CDS300-R044** The identifier MUST NOT be overloaded with type, requiredness or cardinality suffixes when those properties are represented in the schema; suffixes such as `_list`, `_required` or `_text` SHOULD be avoided unless they carry enduring business meaning.

## 20. Extension Namespaces and Reservation *(normative)*

Organisations MAY define additional namespaces for real semantic domains not covered by the core registry.

**CDS300-R045** An extension namespace MUST be registered before use, and its registry entry MUST define purpose, owner, examples, publication behaviour and deprecation policy.

**CDS300-R046** An extension prefix MUST satisfy the grammar of §3 and MUST NOT collide, case-insensitively, with **any** prefix in the §4 registry — core, conditional, reserved, recommended-extension or deprecated. *(Resolves finding 300-3: the entire core set is reserved, not only CDS_/TMP_/LEG_/EXT_.)*

**CDS300-R047** Reserved prefixes MUST NOT be repurposed by an organisation.

**CDS300-R048** Forward compatibility: future CDS releases MAY register new core prefixes. Organisation prefixes SHOULD therefore be organisation-distinctive (never generic domain words likely to be standardised). If a later CDS release registers a prefix that collides with an existing organisation extension, the CDS registration prevails and the organisation prefix MUST be migrated using the §21 pattern within the organisation's adoption of that release.

**CDS300-R049** Organisation prefixes SHOULD NOT encode temporary project names or staff initials.

## 21. Deprecation, Aliases and Migration *(normative)*

Field names are integration contracts; silent renaming is prohibited.

```
Legacy:         DF_Airtable_SEO_Product Category
Interim alias:  DF_google_product_category      (registry status: deprecated)
Replacement:    CH_google_product_category
Migration:      copy -> verify -> switch consumers -> retire
```

**CDS300-R050** A deprecated identifier MUST identify its replacement and deprecation date in the registry.

**CDS300-R051** Aliases MAY be accepted on import but MUST resolve to exactly one canonical identifier; synonymous fields MUST be consolidated or explicitly linked by alias and deprecation metadata.

**CDS300-R052** Every sanctioned alias prefix MUST carry a registry entry with status `deprecated`, so that §22 validation accepts it during migration. *(Resolves finding 300-4, where the v0.1 chapter's own sanctioned alias failed its own validation; per ADR-D24.)*

**CDS300-R053** Renaming MUST include impact analysis covering formulas, imports, exports, channel mappings, automation and verification, and a migration SHOULD preserve old and new fields through a verified transition period (copy → verify → switch → retire) wherever data loss is possible.

Legacy alias directions (full legacy Airtable alignment annex: CDS-1300):

| Legacy pattern | CDS destination |
|---|---|
| `Import_*` | IMPORT_ (source provenance retained; never canonical) |
| `Airtable_*` | STD_ / CAT_ / VAR_ / PRC_ / INV_ by semantic responsibility |
| `MF_Airtable_*` | MF_ canonical attributes (platform-name segment removed) |
| `MF_Shopify_*`, `Shopify_*` | OBS_ observed publication state; visible verification via QA_ |
| `DF_Airtable_SEO_*`, `DF_*` | CH_ channel fields (never SEO_) |
| `Match_*`, `MF_Match_*` | QA_ backed by full CDS-500 verification records |
| `collection_*` tags | Governed generated channel projections (CDS-400/CDS-500 tag rules) |

## 22. Parsing and Validation *(normative)*

A CDS validator parses namespace, channel segment and semantic field name deterministically:

```
Input: CH_google_product_category
  namespace = CH
  channel   = google
  field     = product_category
```

**CDS300-R054** Validation MUST reject an identifier whose namespace has no registry entry (core, extension or deprecated). Deprecated-prefix identifiers MUST be accepted only as aliases per §21 and SHOULD raise a deprecation warning.

**CDS300-R055** Validation MUST reject identifiers failing the §3 grammar, including empty segments, duplicate underscores, leading or trailing underscores and non-ASCII punctuation.

**CDS300-R056** Validation MUST verify that the channel key of a CH_, QA_ or OBS_ identifier exists in the channel registry.

**CDS300-R057** Validation SHOULD warn on unexplained abbreviations and excessively long identifiers.

**CDS300-R058** Identifiers MUST be validated before schema or import changes are accepted, and AI-generated field proposals MUST pass the same registry and naming validation as human proposals.

## 23. AI Interpretation of Identifiers *(normative)*

Semantic prefixes improve AI understanding; they do not replace schema metadata (CDS-P-05). AI governance — proposal lifecycle, evidence, confidence, autonomy, review — is defined solely in CDS-700; the rules below are naming-specific.

**CDS300-R059** AI systems SHOULD receive the semantic identifier together with its human label, description, data type, dictionary binding and examples — never the identifier alone.

**CDS300-R060** An AI system MUST NOT infer schema properties from a prefix (e.g. that every MF_ field is free text, that every CH_ field is canonical, or that any prefix implies a storage mechanism).

```
identifier: MF_material
label: Material
description: Canonical materials present in the product
type: list<dictionary_reference>
dictionary: material_canonical
facet_mapping: material_family
channel_mappings: shopify, google, meta
```

## 24. Worked Examples *(informative)*

Apparel product:

```
STD_title = Linen Relaxed Shirt
STD_brand = Example Brand
CAT_product_family = apparel
CAT_product_type = shirt
STD_primary_category_ref = women/tops/shirts
MF_material = linen
MF_fit = relaxed
MF_colour_display = French Navy
MF_colour_family = blue
VAR_size = m
VAR_colour = french_navy
CH_shopify_product_category = apparel_accessories_clothing_shirts_tops
CH_google_product_category = 212
SEO_title = Linen Relaxed Shirt | Example Brand
QA_shopify_material = MATCH
```

Publication and read-back (statuses per CDS-500):

```
Canonical:            MF_material = linen
Expected projection:  Linen
Observed:             OBS_shopify_material = linen
Comparison strategy:  case_insensitive_dictionary_id
Result:               QA_shopify_material = MATCH
```

Platform-specific naming behaviour (metafield projections, taxonomy mapping, tag generation) is documented in the CDS-900 profiles.

## 25. Architecture Decisions *(informative)*

Decisions live in the global ADR register (CDS000-R006). Affecting this chapter: **ADR-D2** (MF_ retained and redefined mechanism-neutral; STD_/MF_ boundary by closed enumeration; supersedes CDS-ADR-008), **ADR-D24** (DF_→CH_, one consolidated ADR superseding the four parallel v0.1 ADRs; DF_ registered deprecated). Upheld from v0.1: uppercase prefixes with underscore separator (ADR-007); identifier/label/key separation (ADR-010); rejection of colon, equals and dot separators (ADR-011); schema metadata excluded from identifiers (ADR-012).


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-400 — Controlled Dictionaries and Reference Data

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-400 Working Draft v0.1 |
| Normative status | §1, §3–§18, §20–§28 and §30 are normative. §2, §19 (baseline note), §29, §31 and all appendices are informative except where individually marked. |
| Findings addressed | CDS-400-1..10; DICT-1, DICT-2, DICT-3, DICT-5, DICT-9; ADR-D1, ADR-D4; open decisions D28, D29 |

CDS-400 is the authoritative home for dictionaries and the value layers (CDS000-R005). Terminology is defined in CDS-100 §3; verification statuses and reason-code use live in CDS-500; facet presentation and search behaviour live in CDS-600; AI controls live in CDS-700; conformance levels, tests and claims live in CDS-1000.

---

## 1. Purpose *(normative)*

CDS-400 defines how commerce systems govern repeated values such as colours, materials, styles, rooms, finishes, patterns, occasions, conditions, units and channel vocabularies. It separates detailed product truth from the simplified values presented in customer filters, and defines how one canonical value is projected into display labels, facet values, search synonyms and channel-specific outputs without duplicating product data.

**CDS400-R001** A CDS implementation MUST treat governed values as first-class reference-data entities rather than uncontrolled text wherever consistent reuse, filtering, search, validation or channel mapping is required.

**CDS400-R002** The PIM MUST remain the authority for canonical dictionary values and their mappings.

**CDS400-R003** A customer-facing filter MUST NOT be created by exposing every distinct incoming or display value.

## 2. Problem Statement *(informative)*

Commerce data arrives with rich but inconsistent language. A supplier may describe blue products as Navy, French Navy, Ocean, Denim, Royal, Sky, Petrol or Steel Blue. Publishing those terms directly as filter values produces an unusable panel of near-duplicates. Discarding them and storing only "Blue" destroys product detail and merchandising language.

```
Source terms:        French Navy | Navy | Ocean Blue | Royal Blue | Denim | Sky Blue
Bad storefront facet: the same six near-duplicates exposed to customers
Bad canonical model:  all source detail replaced with "Blue"
CDS model:            preserve detail -> normalise meaning -> expose a usable facet -> project to channels
```

The correct response is not less information; it is a layered model that gives each consumer the appropriate representation.

## 3. Dictionary Principles *(normative)*

| Principle | Meaning |
|---|---|
| Preserve source fidelity | Keep the original value and its provenance even when it maps to a canonical value. |
| Stable identity | Values use stable identifiers independent of labels, spelling and localisation. |
| One canonical meaning | Each governed concept has one approved internal semantic representation. |
| Separate customer facets | Filter groupings are designed for usability, never copied from canonical detail. |
| Derive channel output | Channel values are generated from dictionary mappings wherever possible. |
| Govern change | Aliases, deprecations, replacements and mapping changes are versioned and reviewable. |
| Context matters | The same word can mean different things in different dictionaries or attributes. |
| Humans, machines and AI | The model is readable by operators, deterministic for software and explicit for AI. |

**CDS400-R004** A dictionary MUST have a declared semantic scope, a named owner and a declared value identity scheme.

**CDS400-R005** Labels MUST NOT be used as the only permanent identifier for governed values.

## 4. Controlled Value Lifecycle *(normative — per ADR-D4)*

CDS separates intake, internal meaning and projection. Projections branch in parallel from the canonical value (branch model, CDS-100 §7); the layer that feeds each channel is declared per attribute in the Attribute Definition (CDS-200 §7), never assumed.

```
Source Value ── Alias Mapping Record ──> Canonical Value
                    (governed)                |
        +---------------+---------------+----+----------+----------------+
        v               v               v               v                v
  Display Label    Facet Value    Search Synonyms  Channel Repr.   Tag / other
                                                   (per attribute)  projections
```

> **Supersession note.** The v0.1 term "Reference Value" is retired (ADR-D4; CDS-100 §8). The raw input is a **Source Value**; the governed mapping is an **Alias Mapping Record**; the governed dictionary entry is a **Canonical Value**; everything downstream of canonical is a **projection**.

**CDS400-R006** The original source value MUST remain available, verbatim with provenance, for audit and reprocessing.

**CDS400-R007** An Alias Mapping Record MUST resolve to exactly one canonical value within its declared context, unless the mapping is explicitly marked ambiguous and routed for review.

**CDS400-R008** Facet values, display labels, search synonyms and channel representations MUST be derived from or linked to canonical values rather than maintained as unrelated free text.

*Informative:* not every implementation exposes every layer as a visible column; the logical distinctions must still exist.

## 5. Dictionary Entity Model *(normative)*

A Dictionary is the governed container. A Canonical Value is a stable semantic entity. Aliases, facet mappings and channel mappings attach to the value, never repeated on every product. Canonical product data stores the canonical `value_id`; a variant's colour field holds the canonical value, never a raw source spelling (ADR-D4).

| Property | Purpose |
|---|---|
| dictionary_id | Stable identifier for the dictionary. |
| dictionary_key | Human-readable machine key such as `colour` or `material`; also the context-scoping key for shared codes (§20). |
| value_id | Stable identifier for one canonical value. |
| canonical_code | Portable code such as `navy` or `organic_cotton`. |
| canonical_label | Default human-readable label. |
| status | Value Lifecycle Status (§17.1). |
| version | Version of this value record; incremented on any governed change (§24). |
| aliases | Alias Mapping Records: recognised source terms, spellings and abbreviations, each with scope, status, provenance and locale. |
| display_labels | Optional labels by locale, brand or product (§9). |
| facet_mappings | Ordered facet memberships; the single authoritative facet mechanism (§10). |
| search_terms | Synonyms and related query terms (behaviour: CDS-600 §21). |
| channel_mappings | Values or identifiers required by channels, with mapping_version. |
| parent_id | Optional broader-value relationship — informative analytics only (§13). |
| related_values | Optional typed relationships (synonym, similar, substitute, compatible, contrast). |
| metadata | Swatch, unit, sort order, notes or other dictionary-specific data. |
| provenance | Who or what introduced and approved the value or mapping. |
| effective_dates | When a value or mapping becomes valid or invalid. |
| replacement_id | Successor value when deprecated. |

**CDS400-R009** Every canonical value MUST have a stable `value_id` or equivalent immutable identity.

**CDS400-R010** A canonical code SHOULD use lowercase ASCII snake_case and MUST remain stable when a display label changes.

## 6. Value Identity and Labels *(normative)*

Identity and presentation are separate. A value called Navy in English may be displayed differently by locale, brand or campaign while its identity is unchanged.

```
value_id:            colour_00017
canonical_code:      navy
canonical_label:     Navy
locale_label_en_AU:  Navy
locale_label_fr_FR:  Bleu marine
facet_mappings:      [blue]
CH_google_colour:    Blue
```

**CDS400-R011** Changing a label MUST NOT create a new value identity when the underlying meaning is unchanged.

**CDS400-R012** Merging or splitting meanings MUST be performed through an explicit governed migration (§24), never a silent label edit.

**CDS400-R013** Display labels MAY contain spaces, punctuation and brand language; canonical codes SHOULD remain portable and stable.

## 7. Source Values and Alias Mapping Records *(normative)*

A Source Value is the exact content received from a supplier, manufacturer, import, manual entry or extraction process. An Alias Mapping Record recognises that source term and links it to exactly one canonical value within a defined context.

```
Source value:      "French Navy"
Source system:     Supplier A
Source attribute:  Colour
Normalised match:  french navy
Alias mapping:     alias_colour_french_navy  (row_type: alias)
Canonical value:   navy                      (row_type: canonical)
```

**CDS400-R014** Source values MUST be retained exactly as received when traceability is required.

**CDS400-R015** An Alias Mapping Record MUST identify the dictionary (via `dictionary_key`) and context in which it is valid.

**CDS400-R016** Supplier-specific mappings SHOULD be supported where the same term has different meanings between suppliers.

*Informative:* alias mappings make supplier onboarding progressively easier — once a term is governed, future imports resolve automatically. Every distinct source value that has been mapped is retained as an alias with provenance (ADR-D4).

## 8. Canonical Values *(normative)*

A Canonical Value is the approved internal representation used for product truth, rules, analytics and derivation. It expresses meaning at the level of detail the business needs, not merely the broadest customer filter. Both granularities are conformant: an organisation may govern `french_navy` as a canonical shade with facet `blue`, or govern only `navy` and keep "French Navy" as a display label (ADR-D4).

**CDS400-R017** Canonical values MUST be semantically distinct within their dictionary.

**CDS400-R018** Canonical values SHOULD preserve commercially useful detail that would be lost in a broader facet value.

**CDS400-R019** A canonical value MUST NOT be created solely because one supplier uses a unique spelling.

**CDS400-R020** A canonical value SHOULD be reused across products and suppliers whenever the meaning is equivalent.

```
Source values                        Canonical value
French Navy, Marine, Deep Navy   ->  navy
Sky, Pale Blue, Baby Blue,
Light Blue                       ->  sky_blue
Royal, Cobalt                    ->  royal_blue
Ocean Blue                       ->  ocean_blue  (only if the business needs the distinction)
```

*Note:* the canonical code for the pale-blue shade is `sky_blue`, matching the shipped reference dictionaries and CDS-1500; the v0.1 code `light_blue` is recorded as an alias of `sky_blue` (resolves DICT-3).

## 9. Display Labels *(normative)*

A Display Label is the wording shown to a customer or operator. It may preserve a supplier or brand name, use a merchandising phrase or provide a localised label. Display labels never define canonical identity.

**CDS400-R021** A product MAY use a display label that differs from the value's canonical label.

**CDS400-R022** A display label MUST remain linked to a canonical value when the field participates in governed filtering, search or channel publication.

**CDS400-R023** A display label SHOULD NOT be used as the only search or facet value.

**CDS400-R024** Label precedence MUST be resolved in this order: (1) a product-level display label, valid only when recorded as a governed Display Label link to the canonical value; (2) the value's locale display label for the viewer's locale; (3) the value's canonical label. A product-level free-text label with no Display Label link MUST NOT override the value's labels in governed contexts.

```
Canonical colour:  navy
Product display:   French Navy   (governed Display Label link)
Facet display:     Blue
Search terms:      navy, dark blue, french navy
Google output:     Blue
```

## 10. Facet Values and Facet Mappings *(normative)*

A Facet Value is a customer-facing grouping used for filtering and refinement. Facet design is a user-experience activity, not a database distinct-value query. Facet presentation — labels, storefront order, selection logic, counts — is defined in CDS-600; CDS-400 owns the mapping from canonical values to facet values.

**CDS400-R025** The Facet Dictionary, referenced through the `facet_mappings` property of canonical values, is the single authoritative mechanism for facet membership. Facet membership MUST NOT be derived from the parent hierarchy (§13), from labels or from any other source. *(Resolves CDS-400-2.)*

**CDS400-R026** Facet values MUST be explicitly governed in a Facet Dictionary or equivalent configuration.

**CDS400-R027** A facet dictionary SHOULD minimise unnecessary near-duplicate choices while preserving distinctions that materially affect purchase intent. *(Downgraded from MUST: "minimise" is not mechanically testable; the testable mechanism is CDS400-R028.)*

**CDS400-R028** A new or materially changed facet dictionary MUST have a recorded usability review, covering the §10.1 checklist, before activation.

**CDS400-R029** `facet_mappings` is an ordered list. The first facet value is the primary membership; a canonical value MUST have exactly one primary facet value per facet dimension and MAY have additional secondary memberships where justified.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D28 (resolved)): Call made — multi-facet memberships are ordered, first entry is primary. Alternative — unordered set with an explicit `is_primary` flag. The teal exemplar is aligned to the shipped reference data (`[green, blue]`, green-dominant per CDS-1500); the v0.1 Blue-primary example is corrected accordingly.

**CDS400-R030** A multi-colour or multi-material product MAY participate in multiple facet values; the storefront MUST treat the product as one result, never a duplicate. Multicolour is a facet or status value, never a canonical shade (CDS-100 §3).

*Informative:* for colour, Blue is normally a facet; French Navy is a display label or canonical shade. For material, Wood may be a facet while Tasmanian Oak is the canonical material or display label.

### 10.1 Facet Usability Review *(normative checklist for CDS400-R028)*

The recorded review MUST cover:

- number of values and expected product counts;
- overlap and ambiguity between values;
- labels visible above and below the fold on common devices;
- whether customers search for the broad group or the detailed value;
- whether a value is better represented by search, a swatch, a range or a separate facet;
- behaviour when multiple facet values are selected;
- zero-result and low-count values; and
- localisation and sort order.

## 11. Channel Representations *(normative)*

A Channel Representation is the value, identifier or label required by a specific downstream channel. It is stored once on the dictionary value or mapping definition and derived for every applicable product. Which layer feeds each channel (canonical, display or facet) is declared per attribute in the Attribute Definition (ADR-D4; CDS-200 §7).

```
Canonical value:          navy
CH_shopify_filter_colour: Blue
CH_google_colour:         Blue
CH_meta_colour:           Blue
Product display label:    French Navy
```

**CDS400-R031** Channel representations SHOULD be defined at dictionary level rather than repeated on every product.

**CDS400-R032** A product-level channel override MAY be used only when the product genuinely requires a different output and the reason is recorded (override semantics: CDS-500 §22).

**CDS400-R033** A missing required channel mapping MUST produce a validation or publication error, never silent free-text substitution.

## 12. Search Terms *(normative)*

Search synonyms attach to canonical values as a projection and extend discovery without expanding the visible facet list. Search behaviour, directionality and query handling are defined in CDS-600 §21.

**CDS400-R034** Search synonyms MUST NOT change canonical identity, and a synonym that is ambiguous across dictionaries MUST be scoped to the applicable dictionary or attribute.

## 13. Hierarchies and Relationships *(normative; parent hierarchy informative)*

A dictionary MAY record a parent hierarchy (e.g. `navy` under `blue`, `oak` under `wood`). In v0.2 the parent hierarchy is an **optional, informative structure for analytics, reporting and operator navigation only**. It carries no authority over facets, channel output or validation; the Facet Dictionary is the only facet-mapping mechanism (CDS400-R025). *(Resolves CDS-400-2.)*

**CDS400-R035** Hierarchy and related-value relationships MUST be explicit records and MUST NOT be inferred solely from labels.

**CDS400-R036** A value MUST NOT have circular parent relationships.

**CDS400-R037** A parent relationship MUST NOT erase, replace or auto-merge the child value.

**CDS400-R038** Related-value links SHOULD state their relationship type: synonym, similar, substitute, compatible or contrast.

## 14. Multi-value and Composite Attributes *(normative)*

A product may have multiple values, and some facts are composite rather than simple lists.

```
Simple multi-value:       materials = [cotton, linen]
Structured composition:   composition = [{material: cotton, percentage: 80},
                                         {material: polyester, percentage: 20}]
Facet projection:         material facets = [cotton, synthetic]
```

**CDS400-R039** A composition MUST NOT be reduced to an unstructured material label when percentages or component roles are required.

**CDS400-R040** Multi-value order MUST be declared significant or insignificant by the Attribute Definition.

**CDS400-R041** Facet membership MAY be derived from each component while the structured composition remains canonical.

## 15. Normalisation and Matching *(normative)*

Normalisation prepares source terms for matching while preserving the original value. The default text pipeline:

1. Preserve original source text
2. Unicode NFC normalisation
3. Trim leading and trailing whitespace
4. Collapse repeated internal whitespace
5. Apply case-insensitive comparison form
6. Apply dictionary-specific punctuation and spelling rules
7. Match exact governed aliases before fuzzy or AI-assisted suggestions
8. Record the rule and mapping used

**CDS400-R042** Normalisation MUST NOT overwrite the original source value.

**CDS400-R043** Exact governed mappings MUST take precedence over fuzzy or AI-assisted matching.

**CDS400-R044** Numeric and measurement values MUST use type-aware comparison rather than text comparison.

**CDS400-R045** A dictionary MAY define locale-specific or supplier-specific normalisation rules.

## 16. Ambiguity and Context *(normative)*

The same term may mean different things in different contexts. Natural may be a colour, a finish, a fibre claim or marketing copy. Large may be a size, a capacity or a package count.

**CDS400-R046** Every mapping MUST be scoped at least by dictionary (`dictionary_key`) or attribute.

**CDS400-R047** Ambiguous aliases MUST NOT resolve globally without context.

**CDS400-R048** Where context is insufficient to resolve a source term, the term MUST enter review or remain unresolved; it MUST NOT be force-mapped.

```
"Natural" in MF_colour_display  -> colour: natural
"Natural" in MF_finish          -> finish: natural_oil / natural
"Natural" in MF_material_claim  -> no automatic mapping; review required
```

## 17. Unknown Values, Resolution and Quarantine *(normative)*

Unknown source values are expected in a living catalogue. They are data-governance events, never a reason to create uncontrolled canonical values automatically.

### 17.1 Two status enums *(normative — resolves CDS-400-4)*

v0.1 mixed two lifecycles in one vocabulary. v0.2 defines two named enums on two named entities. They share no tokens.

**Value Lifecycle Status** — attribute `value_lifecycle_status` on the **Canonical Value**:

| Status | Meaning |
|---|---|
| proposed | Candidate canonical value awaiting governance review. |
| active | Approved for use in canonical data and projections. |
| deprecated | Still resolvable; identified replacement or declared no-replacement; scheduled for retirement. |
| retired | No longer assignable; retained for history and audit. |
| rejected | Reviewed and refused; never activated. |

**Source-Term Resolution Status** — attribute `resolution_status` on the **Source Value intake record**:

| Status | Meaning |
|---|---|
| resolved | Mapped to an active canonical value via an Alias Mapping Record. |
| promotion_proposed | Term proposed as a new canonical value; a linked `proposed` Canonical Value exists. |
| quarantined | Excluded from canonical data and projections until resolved (§17.2). |
| invalid | Not a legitimate value for any target attribute (junk, corruption, wrong field). |
| ignored | Legitimate content, intentionally not used for the target attribute. |

**CDS400-R049** Implementations MUST record the two statuses as separate enums on their respective entities and MUST NOT conflate them in schemas, UIs or exports.

**CDS400-R050** Unknown source values MUST be surfaced to a review queue or explicit error process; they MUST NOT be silently dropped.

**CDS400-R051** Bulk imports MUST NOT silently create new canonical values. Promotion of a source term to a canonical value is an explicit governed act, performed only by roles authorised under §25 — this applies equally to human, scripted and AI-initiated imports.

**CDS400-R052** A promotion proposal MUST include source evidence, affected products and suggested mappings.

### 17.2 Publication consequence of quarantine *(normative — resolves CDS-400-5)*

**CDS400-R053** While a source term for an attribute is `quarantined`, that attribute value MUST be omitted from every projection (display, facet, search, channel) for the affected products. The raw source value is never published as a stand-in.

**CDS400-R054** Verification of an affected field MUST carry the reason code `CDS_VALUE_QUARANTINED` (reason-code registry: CDS-1100 §21; use in verification: CDS-500). The field is reported as attention-state, not silently skipped.

**CDS400-R055** A quarantined value MUST NOT block publication of the product as a whole unless the affected attribute is declared requiredness-blocking for that channel in its Attribute Definition or channel profile; in that case the product publication fails validation per CDS400-R033.

*Informative:* quarantined items remain in quality denominators (CDS-1400 §5) — quarantine is visible pressure to resolve, never a way to improve a health score. A dictionary dashboard should show recurring unknown values so one governance action resolves many future imports.

## 18. Units and Measurements *(normative)*

Units are governed reference data. Measurements store a numeric value and a unit identifier, never units embedded in free text.

```
Measurement:  value: 40, unit_id: centimetre
Display:      40 cm      Channel conversion: 15.75 in      Comparison base: 0.4 m
```

**CDS400-R056** Measurements MUST separate numeric value from unit identity.

**CDS400-R057** Unit conversions MUST use declared conversion rules and precision.

**CDS400-R058** An implementation MUST distinguish similarly named units with different definitions, such as short ton and metric tonne.

**CDS400-R059** Display units MAY differ by locale or channel while the canonical measurement remains stable.

## 19. Colour Dictionaries *(normative; baseline note informative)*

Colour requires multiple representations: product label, canonical shade, broad filter family, search language and channel vocabulary are not always the same.

| Layer | Example |
|---|---|
| Canonical shade | navy |
| Display label | French Navy |
| Facet mappings (ordered) | [blue] — or [green, blue] for a green-dominant teal |
| Search terms | navy blue, dark blue, marine |
| Swatch metadata | Optional representative colour; not a guarantee of physical appearance |
| Channel mapping | Blue |

**CDS400-R060** A colour dictionary SHOULD distinguish canonical shade from broad colour family.

**CDS400-R061** Hex, RGB or other digital swatch values MAY be stored but MUST NOT be treated as an exact representation of physical material colour unless measured under a defined process.

**CDS400-R062** A product with a branded colour name SHOULD retain that name for display while participating in one or more governed colour facets.

**CDS400-R063** Pattern and colour MUST remain separate attributes even when a supplier combines them in one phrase.

*Informative — baseline ownership:* the reference colour facet family list (including `natural` as a top-level facet and `multicolour` as a facet-only value) is owned by CDS-1500 Appendix C. CDS-400 appendices cite that baseline and use consistent exemplars (resolves CDS-400-3 / DICT-2).

## 20. Material and Composition Dictionaries *(normative)*

Material dictionaries support specific materials, broader families, blends and structured composition. A storefront may filter by Cotton while displaying 80% Cotton / 20% Polyester.

**CDS400-R064** Specific material identity and material family MUST be separate where both are useful.

**CDS400-R065** Composition percentages SHOULD be stored as structured values and SHOULD sum according to the organisation's declared tolerance rules.

**CDS400-R066** Claims such as organic, recycled, vegan or certified MUST NOT be inferred solely from the material name unless governed evidence supports the claim.

**CDS400-R067** There is one materials dictionary per organisation. Where the same canonical code needs different family or facet treatment in different commercial contexts (e.g. cotton in apparel vs homewares), the treatment MUST be expressed as context-scoped family and facet mappings keyed by `dictionary_key` scope (e.g. `material.apparel`, `material.homewares`) on the shared canonical value — never by forking the canonical meaning into duplicate values. *(Resolves DICT-5.)*

> RESOLVED — accepted as drafted (owner 2026-08-04; was D29 (resolved)): Call made — one materials dictionary with context scoping via `dictionary_key` scoped families; shared codes keep one meaning with per-context family/facet mappings. Alternative — two independent apparel/homewares dictionaries permitted to diverge on shared codes.

```
Canonical composition:  cotton 80, polyester 20
Facet projection:       Cotton, Synthetic
Display:                80% Cotton, 20% Polyester
```

## 21. Size and Fit Dictionaries *(normative)*

Size labels are contextual: S, M and L are not universal measurements, and numeric sizes vary by market, gender category, brand and product type.

**CDS400-R068** A size value MUST be scoped to a declared size system or scale when the label is not globally unambiguous.

**CDS400-R069** Display size, canonical size code and measurement chart MUST be separable.

**CDS400-R070** Size conversion tables SHOULD be represented as governed mappings with provenance and effective dates.

**CDS400-R071** Fit descriptors such as slim, regular, relaxed and oversized MUST be maintained separately from size.

```
Size system: apparel_womens_au   Display size: 10   Canonical code: au_10
Approximate mappings: US 6, EU 38   Product measurements: stored separately   Fit: relaxed
```

## 22. Localisation *(normative)*

Localisation changes presentation, never canonical identity.

**CDS400-R072** Canonical codes and value identifiers MUST remain language-neutral or follow a stable declared base-language policy.

**CDS400-R073** Localised labels MUST identify locale, not merely language, where regional wording differs.

**CDS400-R074** A missing translation SHOULD fall back according to a declared locale policy and SHOULD be visible as a completeness issue.

**CDS400-R075** Search synonyms MAY vary by locale and market.

## 23. Provenance and Audit *(normative)*

Every important mapping answers: who created it, why it exists, which source introduced it and which products it affects.

| Field | Purpose |
|---|---|
| created_by | User, import process or AI agent. |
| approved_by | Data steward or authorised reviewer. |
| source_system | Supplier, manufacturer, channel or internal team. |
| source_value | Exact original value. |
| evidence | Description, image, document or rule supporting the mapping. |
| created_at / changed_at | Audit timestamps. |
| version / mapping_version | Value-record and mapping versions used during a publication or verification run. |
| affected_count | Products or variants currently relying on the mapping. |

**CDS400-R076** A mapping change SHOULD record the previous value, the new value, the actor and the affected product count.

**CDS400-R077** AI-created suggestions MUST record model or process identity, confidence and evidence where available (full AI provenance requirements: CDS-700).

## 24. Versioning, Deprecation, Migration and Breaking Changes *(normative)*

Dictionary changes can alter thousands of products without editing those products directly. They therefore require versioning and impact review. Corpus-level version policy is ADR-D5; this section governs value- and mapping-level versioning.

**CDS400-R078** Every canonical value record MUST carry a `version`, and every alias, facet and channel mapping MUST carry a `mapping_version`, incremented on any governed change.

**CDS400-R079** A canonical value MUST NOT be deleted while products, aliases, rules or channel mappings reference it.

**CDS400-R080** Deprecated values MUST identify a replacement or state that no direct replacement exists.

**CDS400-R081** Mapping changes SHOULD support preview of affected products and expected downstream changes before activation.

### 24.1 Breaking changes *(normative — resolves CDS-400-7)*

**CDS400-R082** The following changes are breaking changes to value meaning:

1. **Facet remap** — moving a canonical value's primary facet membership to a different facet value;
2. **Alias retarget** — repointing an existing Alias Mapping Record to a different canonical value;
3. **Meaning narrowing** — restricting what an existing canonical value denotes so that some current usages become incorrect.

A breaking change MUST either (a) create a new value identity (new `value_id`, old value deprecated with `replacement_id`), or (b) be executed through a **governed migration record** that captures the old and new state, the actor and approver, affected product and collection counts, the activation date and the expected verification changes. A breaking change MUST NOT be applied as an in-place edit without one of these two paths.

```
Status transition:  proposed -> active -> deprecated -> retired

Deprecated value:
  canonical_code: petrol_blue
  replacement_id: teal
  migration_note: Consolidated after merchandising review
  active_until:   2026-09-30
```

## 25. Dictionary Governance *(normative)*

Governance defines who may propose, approve, change and retire values, and prevents dictionaries from becoming another uncontrolled tag list. Role definitions and change-control machinery are owned by CDS-800; this section states the dictionary-specific obligations.

| Role | Responsibility |
|---|---|
| Dictionary owner | Accountable for scope, quality and policy. |
| Data steward | Reviews new values, aliases, mappings and deprecations. |
| Merchandising owner | Approves customer facet labels, grouping and order. |
| Channel owner | Maintains external channel vocabularies and requirements. |
| Search owner | Maintains search synonyms and query behaviour. |
| AI process | May propose; never authoritative by default (CDS-700). |

**CDS400-R083** Every dictionary MUST have a named owner.

**CDS400-R084** The organisation MUST define which roles may create canonical values and which may only propose them.

**CDS400-R085** Facet changes SHOULD include merchandising or customer-experience review; channel mapping changes SHOULD include channel validation or test publication.

## 26. Publication and Verification *(normative)*

Dictionary mappings form part of the expected channel state. Verification compares the value generated by the active mapping version with the value read back from the channel. The verification model, status enum, comparison strategies and reason codes are owned by CDS-500; this section states what dictionaries contribute.

```
Canonical value: navy            Mapping version: colour_map_v12
Expected Shopify facet: Blue     Observed: blue     Strategy: case-insensitive     Result: MATCH
Expected Google colour: Blue     Observed: blank                                   Result: MISSING
```

**CDS400-R086** Publication records SHOULD identify the dictionary version and `mapping_version` used to generate channel output, so the expected value is reproducible.

**CDS400-R087** Verification MUST compare the expected representation (generated from the active mapping version) with the observed representation under the declared comparison strategy (CDS-500 §16).

**CDS400-R088** A dictionary change that alters expected output SHOULD trigger re-publication or re-verification for affected records.

## 27. AI Participation *(normative)*

AI may classify source terms, suggest aliases, recommend canonical values, propose facet memberships and detect anomalies — always inside the governed dictionary model. Autonomy levels, evidence classes, proposal storage and review flow are owned by CDS-700; the dictionary-side constraints are:

**CDS400-R089** AI MUST receive the applicable dictionary, attribute context and allowed values before proposing a mapping where practical.

**CDS400-R090** AI suggestions outside the dictionary MUST be marked as promotion proposals or unknown and routed under §17 and §25; AI MUST NOT silently create a new active canonical value (CDS400-R051 applies; autonomy ceilings: CDS-700 §5).

**CDS400-R091** AI SHOULD return confidence, evidence and alternative candidates for ambiguous values; abstention is a first-class outcome (CDS-700).

```
Input: "French Navy"    Context: apparel colour
Allowed candidates: navy, royal_blue, ocean_blue, black
AI suggestion: navy     Confidence: 0.97
Evidence: supplier colour name and product image
Decision: auto-accept only if policy threshold and evidence rules pass (CDS-700)
```

## 28. Performance and Implementation Considerations *(informative except CDS400-R092)*

CDS specifies logical behaviour, not a storage engine. Implementations should avoid recalculating the entire catalogue for every dictionary lookup:

- immutable value identifiers and indexed alias lookups;
- cached active dictionary and channel mappings with version identifiers;
- recomputation of affected products when a `mapping_version` changes;
- product-to-value and value-to-product indexes for impact analysis;
- source values and observed channel values kept separate from canonical values;
- bulk review and approval for recurring unknown values;
- dictionary health metrics: unknown rate, deprecated-use count, unmapped-channel count.

**CDS400-R092** Optimisation MUST NOT remove provenance, `mapping_version` or the ability to reproduce expected output.

## 29. Worked Examples *(informative)*

### 29.1 Apparel Colour

```
Source supplier colour: French Navy
Alias Mapping Record:   french navy -> navy
Canonical value stored on variant: value_id of navy
Display label:          French Navy
Facet mappings:         [blue]
Search terms:           navy, dark blue, french navy
Shopify filter value:   Blue        Google colour: Blue
Verification comparison: normalised text (CDS-500)
```

### 29.2 Teal with Ordered Multi-Facet Membership

```
Canonical value:  teal
Facet mappings:   [green, blue]   (ordered; green primary — green-dominant per CDS-1500 baseline)
Display label:    Deep Teal
Search terms:     teal, blue green, green blue
Policy:           product appears once even when both Green and Blue are selected
```

### 29.3 Cotton Blend

```
Source description:     80% Cotton, 20% Polyester
Canonical composition:  cotton = 80, polyester = 20
Display:                80% Cotton, 20% Polyester
Facets:                 Cotton, Synthetic
Google material:        Cotton/Polyester
Claims:                 no organic or recycled claim without governed evidence
```

### 29.4 Tasmanian Oak Homeware

```
Source material:   Tasmanian Oak
Canonical value:   oak   (family via material.homewares scope: wood)
Display label:     Tasmanian Oak
Facet:             Wood
Search terms:      timber, oak, tasmanian oak
Google material:   Wood
```

### 29.5 Unknown Supplier Colour (Moonlit Harbour)

```
Source value:     Moonlit Harbour
Dictionary match: none
AI suggestion:    navy (confidence 0.61)
Policy threshold: 0.90
Result:           resolution_status = quarantined
Publication:      colour omitted from projections; verification reason code
                  CDS_VALUE_QUARANTINED; product still publishes (colour not
                  requiredness-blocking on this channel)
Action:           human review
Outcome:          alias "Moonlit Harbour" -> navy; display label remains Moonlit Harbour
```

### 29.6 Facet Remap as a Governed Migration (breaking change)

Moving `petrol_blue` from facet Blue to facet Green is a **facet remap** — a breaking change under CDS400-R082. It cannot be applied as an in-place mapping edit; it proceeds as a governed migration record:

```
Migration record: MIG-2026-014
  Change:      petrol_blue facet_mappings [blue] -> [green]
  Actor:       merchandising owner   Approver: dictionary owner
  Impact:      127 products, 3 Shopify collections, 1 Google supplemental feed
  Activation:  2026-09-01
  Expected verification changes calculated before activation;
  re-publication and re-verification scheduled for affected records (CDS400-R088)
```

## 30. Conformance *(normative)*

Conformance levels, test suites and claim rules are owned by CDS-1000 (Foundation -> Structured -> Publisher -> Verified -> Governed; ADR-D1). CDS-400 defines **dictionary capability badges**: cumulative capability declarations inside the Structured evidence set. Each badge requires everything in the badges before it.

| Badge | Requires | Minimum capability |
|---|---|---|
| Dictionary Core | — | Stable canonical values, aliases, the two lifecycle/resolution enums, quarantine, provenance. |
| Dictionary Facet | Dictionary Core | Governed Facet Dictionary, ordered facet mappings, recorded usability review. |
| Dictionary Channel | Dictionary Facet | Channel representations, `mapping_version`s, channel validation. |
| Dictionary Round-Trip | Dictionary Channel | Expected-state publication and downstream verification of dictionary-derived output (CDS-500). |

> **Supersession note.** The v0.1 badge "Dictionary Verified" is renamed **Dictionary Round-Trip** to avoid colliding with the global Verified level, and the badges are now strictly cumulative (ADR-D1; resolves CDS-400-9).

**CDS400-R093** A dictionary capability badge MUST NOT be claimed unless all lower badges are also satisfied; badge claims are made and evidenced under CDS-1000.

The chapter's core obligations for any conformant implementation are CDS400-R001..R009 (governed values, layers, identity), R025/R028/R029 (single facet mechanism), R049..R055 (statuses and quarantine), R078..R082 (versioning and breaking changes) and R086..R088 (reproducible expected output).

## 31. Architecture Decisions *(informative)*

The v0.1 chapter-local ADR table (CDS-ADR-007..013) is superseded by the single global ADR register (CDS000-R006). The decisions binding this chapter are ADR-D1 (conformance ladder and badges), ADR-D4 (value-layer terminology and variant storage) and ADR-D5 (version and identifier policy).

---

## Appendix A — Recommended Dictionary Schema *(informative; field-presence rules normative where marked Required)*

One row set holds both canonical values and alias mappings; `row_type` disambiguates (ADR-D4; resolves DICT-1, CDS-400-6). Machine-readable schema: CDS-1100.

| Field | Type | Requirement | Purpose |
|---|---|---|---|
| dictionary_id | string / UUID | Required | Stable dictionary identity. |
| dictionary_key | string | Required | Portable semantic key and context scope (§20). |
| row_type | enum | Required | `canonical` or `alias`. |
| value_id | string / UUID | Required | Stable canonical value identity (target value for alias rows). |
| canonical_code | string | Required (canonical rows) | Lowercase snake_case portable code. |
| canonical_label | string | Required (canonical rows) | Default label. |
| alias_text | string | Required (alias rows) | The recognised source term. |
| alias_scope | object | Optional | Supplier, locale or attribute scope of the alias. |
| status | enum | Required | Value Lifecycle Status (canonical rows) or Source-Term Resolution Status (alias rows) — §17.1. |
| version | integer | Required | Value-record version (§24). |
| mapping_version | integer | Required (alias/facet/channel mappings) | Mapping version used in publication and verification. |
| locale | string | Required where localised | Locale of labels and synonyms (e.g. `en-AU`). |
| parent_value_id | reference | Optional | Broader value — informative analytics only (§13). |
| display_labels | localised list | Optional | Merchandising or locale labels. |
| facet_mappings | ordered list | Optional | Facet memberships; first entry is primary (§10). |
| search_terms | localised list | Optional | Synonyms and related queries. |
| channel_mappings | map | Optional | Channel identifiers and labels, each with mapping_version. |
| metadata | object | Optional | Swatches, sort order, unit data, notes. |
| provenance | object | Required | Creation, source and approval data (§23). |
| valid_from / valid_to | datetime | Optional | Effective period. |
| replacement_value_id | reference | Conditional | Required when deprecated if a direct replacement exists. |

## Appendix B — Apparel Colour Example *(informative)*

Facet families cite the CDS-1500 Appendix C colour baseline, which owns the reference family list; `natural` is a top-level facet there and is used as such here (resolves CDS-400-3 / DICT-2). Canonical `sky_blue` per DICT-3, with `light blue` as an alias.

| Aliases | Canonical | Display | Facet mappings (ordered) | Search | Channel |
|---|---|---|---|---|---|
| french navy | navy | French Navy | [blue] | navy; dark blue; marine | Google: Blue; Shopify facet: Blue |
| royal; cobalt | royal_blue | Royal Blue | [blue] | royal; bright blue | Google: Blue; Shopify facet: Blue |
| sky; pale blue; baby blue; light blue | sky_blue | Sky Blue | [blue] | sky; pale blue | Google: Blue; Shopify facet: Blue |
| teal | teal | Teal | [green, blue] | teal; blue green | Google: Green; Shopify facets: Green, Blue |
| natural; undyed; ecru | natural | Natural | [natural] | natural; undyed; ecru | Google: Beige; Shopify facet: Natural |

## Appendix C — Homewares Material Example *(informative)*

One materials dictionary; family and facet treatment scoped by `dictionary_key` context (§20, D29 resolved).

| Source | Canonical | Scope: material.homewares family | Display | Facet | Search | Channel |
|---|---|---|---|---|---|---|
| Tasmanian Oak | oak | wood | Tasmanian Oak | Wood | timber; oak | Google: Wood |
| American Walnut | walnut | wood | American Walnut | Wood | timber; walnut | Google: Wood |
| Stoneware | stoneware | ceramic | Stoneware | Ceramic | ceramic; pottery | Google: Ceramic |
| Rattan | rattan | natural_fibre | Rattan | Natural Fibre | cane; wicker; rattan | Google: Rattan |
| 80% Cotton / 20% Polyester | structured composition | textile | 80% Cotton, 20% Polyester | Cotton; Synthetic | cotton blend | Google: Cotton/Polyester |

## Appendix D — Legacy Alignment *(informative)*

The legacy production PIM already separated raw supplier input, resolved authoritative values, channel outputs and read-back verification. CDS-400 makes those layers explicit entities: `Import_*` fields correspond to Source Values with provenance; lookup-map normalisation corresponds to Alias Mapping Records; resolved authoritative fields correspond to Canonical Values; legacy `DF_*` feed fields correspond to Channel Representations (`CH_*` in new design, ADR-D24); read-back match fields correspond to verification results (CDS-500). Legacy lookup maps import directly as Alias Mapping Records with provenance; every distinct source value that was mapped is retained as an alias (ADR-D4).

## Appendix E — Platform Notes *(informative)*

Platform-specific mappings and constraints live in the versioned, dated profiles of CDS-900. In summary for any storefront platform: platform attribute stores and metafield-equivalents are publication targets, never the dictionary master; storefront filters use governed facet values, not distinct raw values; a product page may display a governed Display Label while the filter shows the facet value; tags are not the primary store for controlled attributes when typed fields exist; read-back is normalised and compared with expected values generated from the active `mapping_version`; manual downstream edits to PIM-owned values are reported as drift unless an approved override exists (CDS-500 §22).

END OF CDS-400 v0.2 REVIEW DRAFT


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-500 — Publication, Observation and Verification

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-500 Working Draft v0.1 (3 August 2026) |
| Normative status | §1, §3–§27 are normative except where individually marked. §2, §28 and the appendices are informative. |
| Findings addressed | CDS500-1, CDS500-2, CDS500-3, CDS500-4, CDS500-5, CDS500-6, CDS500-7, CDS500-8, CDS500-9, CDS500-10; CDS900-1 (status/colour conflict, resolved here per ADR-D3); LEG-2, LEG-4, LEG-6, LC-1, LC-2; ADR-D3 (implemented in full), ADR-D24 §3; CLEANUP-PASS items 2 (cross-reference side) and 6 |

**Single-home notice.** CDS-500 is the sole normative home for: the publication assurance lifecycle, the expected-channel-state model, field ownership contracts, the observation and coverage model, the comparison/normalisation registry obligations, the **verification status enum**, the **traffic-light mapping**, and the rule that **read-back never overwrites canonical values**. Other chapters cite these; they do not restate them (CDS000-R005, Reconciliation Matrix 5). Machine encodings live in CDS-1100; platform specifics live in CDS-900 profiles; terminology lives in CDS-100.

---

## 1. Purpose and Scope *(normative)*

CDS-500 defines publication as an assurance lifecycle, not a single API call. It specifies how an implementation converts a canonical product revision into an expected channel representation, validates and dispatches that representation, observes what the channel actually exposes, compares expected and observed values, and reports or repairs discrepancies. It applies to API integrations, file feeds, supplemental feeds, bulk imports, event streams and manual channel exports, independent of channel type.

**CDS500-R001** The PIM MUST remain the master product-information layer throughout the publication lifecycle (authority model: CDS-200).

**CDS500-R002** Publication MUST NOT be considered complete solely because a payload was generated, transmitted or acknowledged.

**CDS500-R003** Where a channel permits observation, the implementation MUST compare observed downstream state with the expected channel state.

**CDS500-R004** Where a channel cannot be observed, the implementation MUST report that limitation explicitly and MUST NOT represent the state as verified.

**CDS500-R005** Channel read-back MAY inform verification and repair, but observed state MUST NOT overwrite canonical values silently. Any adoption of an observed value into the canonical record MUST be an explicit, attributed, auditable change. *(This is the single normative home of the read-back rule; CDS-200 and other chapters cite it.)*

## 2. Publication Principles *(informative)*

| Principle | Meaning |
|---|---|
| Canonical before channel | A channel projection is derived from a versioned canonical revision. |
| Expected before actual | The expected channel state is calculated before anything is written. |
| Acknowledgement is not proof | Transport acceptance confirms receipt, not downstream fidelity. |
| Observe independently | Read-back uses the channel or a trusted downstream surface, never the outbound payload. |
| Compare semantically | Equivalent values may differ in case, order, formatting, units or identifiers. |
| Never hide uncertainty | Unsupported, unreadable and stale fields remain explicit states. |
| Repair by policy | Drift responses are governed, not improvised. |
| Evidence over assumption | Every status traces to payloads, responses, snapshots and rules. |
| Human-readable operations | An operator can see why a field is Green, Amber or Red without reading connector code. |
| Safe automation | Automated repair is bounded by ownership, criticality and confidence. |

## 3. Publication Assurance Lifecycle *(normative)*

The lifecycle runs: canonical revision → expected projection → preflight → dispatch → acknowledgement → independent observation → comparison → drift classification → governed repair → health.

**CDS500-R006** Each lifecycle stage MUST produce a durable status or evidence record sufficient to explain the current publication state.

**CDS500-R007** A later stage MUST NOT erase the evidence of an earlier stage.

### 3.1 Assurance Levels

| Level | Name | Meaning |
|---|---|---|
| PA-0 | MODELLED | Canonical product information exists; no channel projection calculated. |
| PA-1 | PROJECTED | An expected channel state has been calculated and versioned. |
| PA-2 | VALIDATED | The projection passes channel-specific preflight checks. |
| PA-3 | DISPATCHED | A publication attempt has been sent or exported. |
| PA-4 | ACKNOWLEDGED | The transport or channel reports acceptance or successful processing. |
| PA-5 | OBSERVED | A downstream snapshot has been read independently. |
| PA-6 | VERIFIED | Expected and observed values have been compared with declared strategies. |
| PA-7 | HEALTH-MANAGED | Drift, alerts, repair policies and trend reporting operate continuously. |

**CDS500-R008** An implementation MUST NOT claim a higher publication assurance level than the evidence it maintains. *(Conformance levels, tests and claims: CDS-1000.)*

*Informative note:* a channel may support only part of the lifecycle; the implementation declares the highest assurance level it can honestly provide in the channel profile.

## 4. Publication Entity Model *(normative)*

Publication is represented by related, versioned entities rather than mutable flags on a product record.

| Entity | Purpose |
|---|---|
| Channel Profile | Capabilities, constraints, credentials reference, field mappings, propagation window, observation support. |
| Canonical Revision | Immutable snapshot or revision identifier of master product data. |
| Publication Projection | Expected channel-specific representation produced from a canonical revision. |
| Publication Job / Record | One dispatch operation and its immutable attempt records. |
| Acknowledgement | Transport and processing response from the channel. |
| Observed Snapshot | Independent read-back of downstream state at a point in time. |
| Verification Result | Field-level comparison of expected and observed values, with status and reason code. |
| Health Summary | Aggregated product, batch, channel and organisation view. |
| Repair Action | Governed remediation attempt and its outcome. |
| Evidence Artifact | Payload, response, feed row, API result, checksum, screenshot reference or diagnostic report. |

**CDS500-R009** Publication projections and observed snapshots MUST identify the channel, product, revision and time to which they apply.

**CDS500-R010** A verification result MUST reference both the expected projection and the observed snapshot used in the comparison.

*Informative note:* machine-readable schemas for these entities are defined in CDS-1100; this chapter defines their semantics.

## 5. Channel Profiles and Capabilities *(normative)*

A Channel Profile declares what a destination can accept, return, transform and verify. Profiles prevent connector assumptions from leaking into the canonical model. Profile *content* for specific platforms lives in CDS-900; this section defines what any profile must declare.

| Capability | Description |
|---|---|
| write_mode | API, file, feed, bulk import, event, manual export or hybrid. |
| read_mode | API read-back, feed diagnostics, storefront observation, report download or unavailable. |
| field_support | Writable, readable, required, optional, derived or unsupported fields. |
| operation_semantics | Create, update, upsert, patch, full replace, append, delete, archive behaviour. |
| rate_limits | Request, batch, quota and retry constraints. |
| propagation_window | Declared delay allowance between acknowledgement and observable state (see §13, §17, §18). |
| normalisation | Known channel casing, truncation, sorting, sanitisation and unit rules. |
| identity | Product, variant and channel record identifiers. |
| ownership | Which system controls each field or list partition (§7). |
| verification_grade | Highest assurance level supported by the connector and channel. |
| critical_set | Declared fields whose failure blocks publication or escalates presentation (§18, §23). |

**CDS500-R011** Every channel connector MUST publish a governed, machine-readable or equivalent capability profile.

**CDS500-R012** A channel profile MUST declare a propagation window for each write mode it supports. The window bounds PENDING (§17) and drives Amber-to-Red escalation (§18).

**CDS500-R013** An organisation claiming verification for a channel MUST declare the channel's critical field set (which MAY be empty). The critical set drives escalation (§18) and the critical-failure cap (§23).

**CDS500-R014** A field unsupported by the channel MUST be marked unsupported rather than silently dropped.

## 6. Canonical Revisions, Projections and Expected Channel State *(normative)*

### 6.1 Projection identity

A projection is calculated from a specific canonical revision plus a specific channel profile, mapping set, dictionary versions and transformation rules:

```
projection_identity =
  product_id
  + canonical_revision
  + channel_id
  + channel_profile_version
  + mapping_version
  + dictionary_version
  + transformation_version
```

**CDS500-R015** The same projection inputs MUST produce the same expected channel state unless a declared non-deterministic process is involved.

**CDS500-R016** A projection MUST retain lineage to every canonical field, mapping and rule that contributed to each output field.

**CDS500-R017** A new mapping, dictionary or transformation version MUST be able to trigger re-projection even when the canonical product record has not changed.

### 6.2 Field mappings and transformations

Transformations convert canonical values into channel representations: dictionary lookup, taxonomy mapping, formatting, unit conversion, template rendering, omission and list construction.

**CDS500-R018** Every transformation MUST be identified by a versioned rule or function.

**CDS500-R019** Transformations SHOULD be deterministic and side-effect free.

**CDS500-R020** Lossy transformations MUST be declared so that verification compares against the expected lossy output rather than the richer canonical value.

**CDS500-R021** A transformation error MUST be reported separately from a channel rejection or a downstream mismatch (see §17, ERROR family).

### 6.3 Expected channel state

The expected channel state is the exact semantic representation the implementation expects to observe after publication and channel processing. It is first-class and persisted, not recomputed ad hoc at comparison time.

```
Expected field record (informative example):
  field_key: MF_material
  canonical_value: linen
  expected_channel_value: Linen
  destination: custom.material
  ownership: EXCLUSIVE_PIM
  comparison_strategy: NORMALIZED_TEXT
  criticality: important
  source_revision: product-123@rev-48
```

**CDS500-R022** Expected state MUST be calculated before dispatch and MUST be stored, or exactly reproducible from versioned inputs, for later comparison.

**CDS500-R023** Expected state MUST reflect declared channel transformations, not merely raw canonical values.

**CDS500-R024** Fields intentionally omitted by rule MUST be distinguishable from fields lost during transformation or publication.

## 7. Field Ownership Contracts *(normative)*

Multi-system commerce fails when ownership is implied rather than declared. Each channel declares field-level ownership modes.

| Ownership mode | Meaning |
|---|---|
| EXCLUSIVE_PIM | The PIM owns the entire field or list. Downstream edits are drift and may be overwritten. |
| PARTITIONED_PIM | The PIM owns only declared namespaces, prefixes, keys or list members. |
| MERGED | The connector combines PIM-owned and externally owned values under a deterministic merge rule. |
| CHANNEL_OWNED | The channel owns the field. The PIM may observe but does not publish it. |
| OBSERVE_ONLY | The PIM records the field for diagnostics without claiming authority. |
| UNMANAGED | The field is outside the connector contract and must not influence verification. |
| OVERRIDE_ALLOWED | The PIM owns the default; a governed channel-specific exception may replace it (§22). |

**CDS500-R025** Every published field and list MUST have a declared ownership mode.

**CDS500-R026** Full-replace operations MUST NOT delete channel-owned or externally owned values unless the ownership contract explicitly permits it.

**CDS500-R027** A partitioned or merged full-replace list MUST be rebuilt before dispatch by reading the current downstream list, retaining externally owned members, and regenerating all PIM-owned members from current rules.

**CDS500-R028** A manual downstream edit to an EXCLUSIVE_PIM field MUST be classified as drift, not accepted silently into the canonical record.

*Informative note:* tag lists commonly require PARTITIONED_PIM or MERGED ownership — the PIM may own collection and merchandising namespaces (e.g. `collection_*`, `merch_*`, regenerated from rules) while another application owns operational tags. See the worked example in §28.3. Tag governance: CDS-400; the publication merge rule lives here.

## 8. Preflight Validation, Publication Jobs and Records *(normative)*

### 8.1 Preflight

Preflight determines whether a projection is fit to publish before external side effects occur. Areas: schema shape; dictionary and taxonomy mappings active; identity (SKU, GTIN, variant, channel record IDs); channel constraints (length, character, image, URL, price, enumeration); ownership (payload changes only authorised fields); business rules (lifecycle, approval, eligibility); dependencies (parents, variants, media); change safety (preview of additions, changes, removals, list-replacement effects); channel readiness (credentials, quota, connector health).

**CDS500-R029** Blocking preflight errors MUST prevent dispatch.

**CDS500-R030** Preflight warnings MAY permit dispatch but MUST remain visible in the publication record.

**CDS500-R031** Bulk publication SHOULD provide a preview of field additions, modifications and removals — including full-replace list effects — before execution.

### 8.2 Jobs and publication records

A Publication Job is one dispatch operation; a batch groups related jobs. Each attempt produces an immutable Publication Record carrying: job, batch and correlation identifiers; channel, product and projection identity; operation (create, update, upsert, delete, archive, withdraw); requester; timing; attempt count; payload hash; status; evidence references.

**CDS500-R032** Every dispatch attempt MUST have a unique, immutable attempt record, even when retries belong to the same logical job.

**CDS500-R033** A batch MUST report partial success without converting successful items into failures or hiding failed items inside an overall success status.

## 9. Transport Acknowledgement *(normative)*

Acknowledgement records what the transport or channel reported after dispatch. It is evidence of processing, not verification of final state.

| Acknowledgement | Meaning |
|---|---|
| ACCEPTED | Request or file accepted for processing. |
| PARTIAL | Some records or fields accepted, others rejected. |
| REJECTED | Channel rejected the operation. |
| QUEUED | Accepted but not yet processed. |
| PROCESSED | Channel reports processing complete. |
| UNKNOWN | No reliable acknowledgement is available. |
| TIMEOUT | Outcome was not received within the declared interval. |

**CDS500-R034** Acknowledgement status MUST remain separate from verification status.

**CDS500-R035** A successful transport response (2xx, successful upload, processed feed) MUST NOT automatically produce MATCH verification results.

## 10. Idempotency, Delta Publication and Replace Semantics *(normative)*

**CDS500-R036** Where the channel supports idempotency keys, the connector SHOULD use them for retriable write operations.

**CDS500-R037** A delta publication MUST be calculated against a known prior expected or observed state, not against assumptions.

**CDS500-R038** The connector MUST declare whether an empty value means clear, omit, unknown or no change.

**CDS500-R039** Sorting SHOULD be canonicalised for semantically unordered lists to produce stable diffs and checksums.

*(Full-replace list safety: CDS500-R026/R027 in §7.)*

## 11. Retries, Errors and Partial Failure *(normative)*

Error classes: TRANSIENT (timeout, rate limit, outage), VALIDATION, AUTHENTICATION, AUTHORISATION, IDENTITY (target record unresolvable), CONFLICT (concurrent change, ownership violation), MAPPING, TRANSFORMATION, PARTIAL, UNKNOWN.

**CDS500-R040** Retries MUST use a bounded policy with attempt limits, delay and a terminal state.

**CDS500-R041** Deterministic validation, mapping and transformation errors MUST NOT be retried without a relevant data or configuration change.

**CDS500-R042** A partial batch failure MUST preserve successful results and separately queue or report failed items.

**CDS500-R043** Rate limiting and connector back-pressure MUST be visible as operational states, not misclassified as product-data errors.

## 12. Rollback, Withdrawal and Republication *(normative)*

Channels differ in whether they support rollback; CDS defines outcomes rather than assuming a universal undo.

**CDS500-R044** A rollback MUST identify the exact previously verified projection being restored.

**CDS500-R045** Where rollback is unsupported, the connector MAY republish an equivalent prior expected state as a new operation.

**CDS500-R046** Withdrawal, deletion, unpublishing and archiving MUST be distinct operations when the channel distinguishes them.

**CDS500-R047** Destructive operations MUST require stronger authorisation than ordinary field updates.

## 13. Scheduling and Verification Cadence *(normative)*

Verification may occur immediately, after propagation delay, on schedule, on demand, on canonical/mapping/override change, on channel events, or by governed sampling.

**CDS500-R048** The verification schedule MUST account for the channel's declared propagation window (CDS500-R012) so that in-window latency is reported as PENDING, not drift.

**CDS500-R049** Fields in the declared critical set SHOULD be verified more frequently than low-risk descriptive fields.

## 14. Downstream Observation *(normative)*

Observation independently retrieves the state a channel currently holds or exposes. The observation source and time are part of the evidence.

| Observation source | Use |
|---|---|
| Authoritative channel API | Preferred when the API returns the stored field. |
| Channel diagnostics or item report | Feed and marketplace processing results. |
| Storefront or public item endpoint | When the customer-visible result is the verification target. |
| Search index or catalogue export | When the downstream consumer differs from the write endpoint. |
| Connector cache | Acceptable only under CDS500-R052. |
| Manual evidence | Exceptional fields only; not representable as automated verification. |

**CDS500-R050** Observed snapshots MUST include capture time, source, channel record identity and freshness status.

**CDS500-R051** Read-back MUST NOT reuse the outbound payload as the observed state.

**CDS500-R052** A connector cache MAY serve as an observation source only when it was populated from channel read operations, and its entries carry capture time and provenance satisfying CDS500-R050. A cache populated from the connector's own writes MUST NOT be used as observed state.

**CDS500-R053** Where the write endpoint and the customer-visible endpoint differ, implementations SHOULD verify the surface relevant to the business objective.

*(Adoption of observed values into canonical data: CDS500-R005.)*

## 15. Observation Coverage and Unknown State *(normative)*

A missing returned value is not always proof that the channel stored nothing. CDS separates value state from observation capability.

| Coverage state | Meaning |
|---|---|
| OBSERVED_VALUE | The field was returned with a value. |
| OBSERVED_EMPTY | The field was returned and explicitly empty or null. |
| NOT_RETURNED | The field was expected in the response but absent. |
| UNSUPPORTED | The observation interface cannot expose the field. |
| PERMISSION_DENIED | The connector lacks access to observe the field. |
| NOT_APPLICABLE | The field does not apply to this item or channel. |
| STALE | A value was returned but does not meet the freshness requirement. |
| OBSERVATION_ERROR | The read operation failed. |
| PENDING_VISIBILITY | The write is acknowledged but the propagation window has not expired. |

**CDS500-R054** An implementation MUST preserve the distinction between absence of data and absence of observability. UNSUPPORTED, PERMISSION_DENIED and NOT_RETURNED MUST NOT be collapsed into the MISSING verification status without the evidence required by the derivation table in §17.4.

## 16. Normalisation and Comparison *(normative)*

Comparison determines semantic equivalence between expected and observed values. Every field declares a comparison strategy drawn from a documented normalisation registry.

### 16.1 Strategy catalogue

EXACT, CASE_INSENSITIVE, NORMALIZED_TEXT (unicode/whitespace/punctuation/case), IDENTIFIER, BOOLEAN, NUMERIC, NUMERIC_TOLERANCE (declared absolute or percentage), MONEY (currency + declared rounding), MEASUREMENT (unit conversion then numeric), DATE_TIME (time-zone and precision normalisation), UNORDERED_SET, ORDERED_LIST, MULTISET, HTML_SEMANTIC (declared sanitisation policy), URL_CANONICAL, IMAGE_IDENTITY, IMAGE_SEQUENCE, CHANNEL_RULE (specialised comparator declared in the channel profile).

### 16.2 Registry obligations

**CDS500-R055** Every verifiable field MUST declare a comparison strategy that is an entry in the implementation's normalisation registry.

**CDS500-R056** Each registry entry MUST declare: a stable comparator identifier, a behaviour version, supported input types, ordered normalisation steps, the equality rule, any tolerance parameters, and test vectors including at least one negative (non-matching) case. A change to normalisation or tolerance behaviour MUST increment the comparator version.

**CDS500-R057** A comparator's declared behaviour and test vectors are the sole authority for what its normalisation may discard. A comparator MUST NOT be applied outside its declared input types, and an implementation MUST NOT substitute a broader comparator than the one the field declares. *(This replaces the untestable v0.1 "must not hide meaningful data loss" rule: what the comparator may hide is exactly what its registry entry documents and its vectors demonstrate.)*

**CDS500-R058** Substring containment MUST NOT be used as a text-equality rule. Registries MUST record the substring false-green case of Appendix A.4 as a negative test vector for any text comparator.

**CDS500-R059** Comparison inputs and normalised forms SHOULD be retained for diagnostics, alongside the comparator identifier and version used.

*Informative note:* Appendix A seeds the registry with the production-proven legacy tolerance vectors (money rounded to 2 dp, weight to 3 dp, case/whitespace-insensitive text, unordered tag sets) and the documented substring false-green negative case (findings LEG-4/LC-2).

## 17. Verification Status Model *(normative — the single normative status enum for all of CDS)*

Verification status expresses the relationship between expected state, observation coverage and comparison result. This section implements ADR-D3. All other chapters cite this enum; CDS-1100 encodes it verbatim.

### 17.1 Core statuses (the machine contract)

**CDS500-R060** The core verification status enum is exactly: **MATCH, MISSING, MISMATCH, PENDING, UNOBSERVABLE, NOT_APPLICABLE, OVERRIDDEN, ERROR**. Implementations MUST NOT add, remove or rename core statuses.

| Core status | Meaning |
|---|---|
| MATCH | Expected and observed values are equivalent under the declared comparator. |
| MISSING | The channel was observed with sufficient evidence and the expected value is absent. |
| MISMATCH | Observed state contradicts expected state (differing value, or an unauthorised value present). |
| PENDING | Resolution is legitimately awaited (propagation latency, or expected/observed revisions not yet aligned). |
| UNOBSERVABLE | The field cannot currently be read back with sufficient evidence or freshness. |
| NOT_APPLICABLE | The field is intentionally outside the product-channel contract. |
| OVERRIDDEN | The result is governed by an active exception rather than by comparison (see §22). |
| ERROR | The lifecycle failed before a comparison verdict could be produced. |

### 17.2 Detailed statuses and deterministic rollup

**CDS500-R061** Every field-level verification result MUST carry a core status; it SHOULD additionally carry a detailed status. Where a detailed status is recorded, its core status MUST be derived from the following table with no implementation-defined variation:

| Detailed status | Rolls up to | Meaning |
|---|---|---|
| MATCH | MATCH | Equivalent under the declared comparator. |
| MISSING_DOWNSTREAM | MISSING | Observed with evidence; expected value absent. |
| MISMATCH | MISMATCH | Expected and observed values differ. |
| UNEXPECTED_DOWNSTREAM | MISMATCH | A value exists downstream where none was expected or authorised. |
| PENDING | PENDING | Propagation window not yet elapsed. |
| STALE_EXPECTED | PENDING | Observed state corresponds to a different expected revision; re-projection or re-observation is awaited. |
| UNOBSERVABLE | UNOBSERVABLE | The observation interface cannot expose the field, or access is denied, or no sufficiently fresh observation exists. |
| NOT_APPLICABLE | NOT_APPLICABLE | Outside the product-channel contract. |
| WAIVED | OVERRIDDEN | A governed exception accepts the discrepancy without redirecting the expected value (§22). |
| TRANSFORMATION_ERROR | ERROR | Expected state could not be calculated. |
| PUBLICATION_ERROR | ERROR | Dispatch failed or was rejected. |
| OBSERVATION_ERROR | ERROR | Read-back failed. |
| COMPARISON_ERROR | ERROR | Values could not be compared under the declared strategy. |

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): WAIVED rolls up to core OVERRIDDEN (both are "governed exception" outcomes, distinguishable by detailed status and reason code). The alternative — a ninth core status — was rejected to keep the machine contract at ADR-D3's eight values.

**CDS500-R062** SUPERSEDED is a record-retention state, not a live verification status. A verification result belonging to an older projection or publication revision MUST be marked superseded when a newer result for the same field exists, MUST be retained for audit, and MUST NOT appear in current status displays, health denominators or the machine status enum. *(Resolves the STALE_EXPECTED/SUPERSEDED boundary: STALE_EXPECTED is a live condition awaiting realignment; SUPERSEDED is an archival marker on the record.)*

### 17.3 Reason codes

**CDS500-R063** Every field-level verification result whose core status is not MATCH MUST carry a machine-readable `reason_code` drawn from the CDS_* reason-code registry defined in CDS-1100 §21. A free-text `message` MAY accompany the reason code but MUST NOT replace it.

**CDS500-R064** A MATCH produced under a redirected-expected override (§22) MUST carry OVERRIDDEN provenance (override identity) visible alongside the status.

*Informative note:* Appendix B provides a seed reason-code list. The registry itself — identifiers, governance, additions — is owned by CDS-1100 §21. Reason codes are a v0.2 design; they have no legacy precedent.

### 17.4 Derivation from observation coverage

**CDS500-R065** Where an expected value exists for a field, the field's detailed verification status MUST be derived from the observation coverage state (§15) as follows:

| Coverage state | Detailed status | Notes |
|---|---|---|
| OBSERVED_VALUE | MATCH, MISMATCH or COMPARISON_ERROR | Per the declared comparator. |
| OBSERVED_EMPTY | MISSING_DOWNSTREAM | The interface affirmatively returned empty/null. |
| NOT_RETURNED | UNOBSERVABLE, unless the channel profile declares that the read interface enumerates every stored field, in which case MISSING_DOWNSTREAM | Absence in the response is evidence of absence only when the profile declares complete enumeration. |
| UNSUPPORTED | UNOBSERVABLE | |
| PERMISSION_DENIED | UNOBSERVABLE | Reason code distinguishes the cause. |
| NOT_APPLICABLE | NOT_APPLICABLE | |
| STALE | UNOBSERVABLE | No sufficiently fresh observation; reason code `CDS_STALE_OBSERVATION`. |
| OBSERVATION_ERROR | OBSERVATION_ERROR | The coverage state and detailed status share a name by design; this row is their relation rule. |
| PENDING_VISIBILITY | PENDING | Only within the declared propagation window (CDS500-R066). |

*(This table promotes the v0.1 §30.2 sketch to normative and replaces the v0.1 §15 reference to a nonexistent "MISSING" status: coverage states derive to MISSING_DOWNSTREAM, never to a bare "MISSING" detailed status.)*

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): NOT_RETURNED derives to UNOBSERVABLE by default, flipping to MISSING_DOWNSTREAM only under a declared complete-enumeration read interface; the alternative (always MISSING) was rejected as unevidenced. STALE derives to UNOBSERVABLE rather than PENDING because staleness is an observation deficiency, not write latency.

### 17.5 PENDING expiry

**CDS500-R066** A field result MUST NOT remain PENDING beyond the channel's declared propagation window. When the window lapses, the implementation MUST re-verify: re-observe and re-derive the status under CDS500-R065, recording reason code `CDS_PROPAGATION_WINDOW_EXPIRED` on any non-MATCH outcome. If re-observation is not possible, the status MUST become UNOBSERVABLE with that reason code. In all cases the lapsed condition escalates at presentation (CDS500-R070).

### 17.6 Aggregation

**CDS500-R067** Verification status MUST be field-specific before it is aggregated to product, batch or channel level.

**CDS500-R068** A product-level verified claim MUST identify the canonical revision and the verification scope (which fields, which coverage) it covers.

## 18. Traffic-Light Presentation *(normative)*

A traffic light is a presentation layer over verification statuses. Colours are never stored statuses. This mapping is complete: every core status has exactly one row.

**CDS500-R069** Where traffic-light presentation is used, the colour mapping MUST be:

| Colour | Core statuses | Semantics |
|---|---|---|
| GREEN | MATCH | Expected equals observed under the declared comparator — with no exceptions. A MATCH under a redirected-expected override is GREEN with its OVERRIDDEN provenance visible (CDS500-R064). |
| AMBER | MISSING, PENDING, UNOBSERVABLE, OVERRIDDEN (including detailed WAIVED) | Attention: absence, latency, blindness or governed exception. Never a confirmed contradiction. |
| RED | MISMATCH, ERROR | Confirmed contradiction or lifecycle failure. |
| GREY *(optional)* | NOT_APPLICABLE | Outside the contract. Implementations that do not use GREY MUST NOT colour NOT_APPLICABLE as GREEN and MUST exclude it from success denominators either way. |

**CDS500-R070** An AMBER indicator MUST escalate to RED presentation when either declared condition is met: (a) the channel's declared propagation window for the publication has lapsed without resolution, or (b) the field is a member of the channel's declared critical set (CDS500-R013). Escalation changes presentation and alerting; it does not alter the stored status or reason code.

**CDS500-R071** WAIVED results MUST always present as AMBER. A waiver never produces GREEN; only a redirected-expected override that yields a true MATCH does (§22).

**CDS500-R072** The user interface MUST make the detailed status and reason code accessible from every traffic-light indicator. AMBER MUST NOT function as a generic category: the indicator MUST distinguish — via detailed status and reason code — whether the field is missing, pending, unobservable, overridden or waived.

**CDS500-R073** Colours MUST NOT be stored or exchanged as verification statuses. Machine records carry statuses and reason codes; colour is derived at presentation time.

*Informative note:* v0.1's BLUE ("in-progress activity") is dropped from the standard per ADR-D3. Implementations remain free to animate or badge in-flight operations as a local presentation choice; such a treatment is not a CDS colour and carries no conformance meaning. GREY and any further presentation variants are optional presentation extensions, never additional statuses.

*Informative note:* MISSING presents as AMBER, restoring the production-proven legacy semantics (blank on either side = amber; red = confirmed mismatch only — LEG-2) and resolving the v0.1 CDS-500/CDS-900 colour conflict in favour of Amber. The escalation rule (CDS500-R070) captures the real risk of long-standing absence without punishing day-one latency.

## 19. Feed-Output Three-Way Match *(normative — optional layer)*

Channel-formatted projections (the CH_ layer, ADR-D24) are first-class artifacts: a serialized feed column or formatted payload field, distinct from both the canonical value and the channel's stored state. Legacy production practice verified this layer independently (`DF_Match_*` — LEG-6/LC-1).

**CDS500-R074** An implementation MAY maintain expected/observed/match verification records at the formatted-output layer, in addition to canonical-versus-channel field verification. Where it claims this layer, each formatted-output field MUST use the §17 status enum, the §16 registry comparators and the §18 presentation rules, and the feed artifact MUST be verified end-to-end (generated output compared against the ingested or reported feed content).

**CDS500-R075** A formatted-output MATCH MUST NOT substitute for downstream observation: it proves the feed said what was intended, not that the channel stored or displays it.

## 20. Drift Classification *(normative)*

Drift is any downstream state that no longer conforms to the current expected channel state or ownership contract.

| Drift type | Description |
|---|---|
| EXTERNAL_EDIT | A user or application changed a PIM-owned value downstream. |
| CHANNEL_NORMALISATION | The channel transformed the value in a known but unmatched way. |
| CHANNEL_TRUNCATION | The channel shortened or removed content. |
| MAPPING_CHANGE | The expected output changed because a mapping or dictionary changed. |
| STALE_PUBLICATION | The channel still reflects an older canonical revision. |
| PARTIAL_PUBLICATION | Only part of a projection was applied. |
| IDENTITY_MISMATCH | The observed record belongs to the wrong product or variant. |
| DELETION | The expected record or field was removed. |
| DUPLICATION | Multiple downstream records represent one expected item. |
| UNMANAGED_MUTATION | A field outside the ownership contract changed; not PIM drift. |
| CONNECTOR_DEFECT | The connector transformed, omitted or targeted data incorrectly. |
| UNKNOWN_CAUSE | Evidence is insufficient to assign a cause. |

**CDS500-R076** Drift detection SHOULD assign a cause category separate from the verification status and reason code.

**CDS500-R077** A known channel normalisation SHOULD be incorporated into expected-state or comparator rules (with a registry entry per §16.2) rather than generating repeated false alarms.

### 20.1 Drift Attribution *(normative — owner decision A1/D17, 2026-08-04)*

Detection tells you *that* a value changed; attribution helps you find *who or what* changed it — which distinguishes an innocent staff mistake from a connector defect or an unauthorised edit.

**CDS500-R077a** Observation records MUST be retained append-only per field and channel (never overwritten in place), so that for any drifted field the implementation can produce: the **previous observed value**, the **new observed value**, and the **detection interval** (last observation at which the field still matched, first observation at which it differed).

**CDS500-R077b** When drift of type EXTERNAL_EDIT is detected, the implementation SHOULD correlate the detection interval with whatever actor evidence the channel exposes (event logs, audit logs, webhook actor metadata, staff activity records — declared per channel profile, CDS-900) and record the attribution outcome (actor identified, actor class identified, or unattributable) on the drift record.

**CDS500-R077c** Attribution evidence is observed data about the channel, never a verdict about intent. An unattributable drift is still drift; attribution failure MUST NOT delay detection, verification status or escalation.

*(Channel-specific attribution mechanisms and their limits are profile content: CDS-900. This restores and extends the legacy production insight that per-field expected/observed comparison — the Match fields — doubles as the change-detection layer.)*

*(Drift metrics and monitoring: CDS-1400. Republishing is not always the correct repair — see §21.)*

## 21. Reconciliation and Repair Policies *(normative)*

A repair policy determines what happens after drift or failure is detected: REPORT_ONLY, AUTO_REPUBLISH, RETRY_SAME_PROJECTION, QUARANTINE_PRODUCT, SUSPEND_CHANNEL, ACCEPT_EXCEPTION, REMAP_AND_REPROJECT, MANUAL_REPAIR, ROLLBACK, WITHDRAW.

**CDS500-R078** Automatic repair MUST be limited to fields and operations owned by the PIM under the declared ownership contract.

**CDS500-R079** Critical or destructive repair actions SHOULD require approval or a pre-authorised policy.

**CDS500-R080** Every repair action MUST create a new evidence record and MUST trigger re-verification where observation is supported.

## 22. Overrides and Exceptions *(normative)*

Channel-specific differences are sometimes legitimate. CDS permits explicit, governed exceptions without weakening the canonical model. An override record carries: identifier, scope (product/variant/field/locale/market/channel), replacement value (if any), reason, owner, approver, effective window, review date, verification expectation, and lifecycle status. *(Exception governance: CDS-800.)*

Two forms exist, with different verification outcomes (ADR-D3):

- **Redirected-expected override** — the override supplies an approved channel-specific replacement value. The expected channel state is recalculated to that value; verification compares against it and can yield a **true MATCH**, presented GREEN with OVERRIDDEN provenance (CDS500-R064).
- **Waiver (acceptance without redirection)** — a reviewed exception tolerates a known discrepancy without changing the expected value. The result is detailed status **WAIVED** (core OVERRIDDEN), presented AMBER always (CDS500-R071).

**CDS500-R081** An override MUST NOT silently replace canonical product truth; the canonical value is unchanged and the override is a distinct governed record.

**CDS500-R082** Overrides SHOULD be time-bounded and MUST carry a review date.

**CDS500-R083** Verification MUST compare against the active redirected expected value when one exists.

## 23. Channel Health and Aggregation *(normative)*

Health aggregates field-level evidence into product, batch and channel views. A score aids prioritisation; it never replaces reason codes or critical-field rules. Metric definitions, denominators and monitoring cadence are owned by CDS-1400; the aggregation rules below are owned here.

**CDS500-R084** Health calculations MUST publish their weighting, inclusion and critical-field rules.

**CDS500-R085** Any field in the declared critical set (CDS500-R013) whose presentation is RED — directly or via escalation (CDS500-R070) — MUST cap the aggregate product and channel presentation at RED regardless of the numeric score.

**CDS500-R086** NOT_APPLICABLE and superseded results MUST NOT count as successes in any health denominator; UNOBSERVABLE fields MUST NOT count as matched. *(No 100% match rate for unobserved fields — see CDS-1400.)*

```
Illustrative weighted score (informative):
  health = 100 * sum(field_weight * field_pass) / sum(field_weight)
  field_pass = 1 for MATCH; configurable partial value for PENDING or
  OVERRIDDEN; 0 for MISMATCH or ERROR
```

## 24. Audit, Lineage and Evidence *(normative)*

Every decision in the publication lifecycle is reconstructable from: the canonical revision used; projection inputs (profile, mappings, dictionaries, rules, overrides); expected payload; dispatch record; acknowledgement; observed snapshot; normalised comparator inputs; verification result with status, reason code and comparator version; repair history; and actor provenance (human, system, schedule or AI agent).

**CDS500-R087** Audit records MUST be append-only or otherwise protected against silent alteration.

**CDS500-R088** Sensitive payload content and credentials MUST be redacted or securely referenced without destroying operational traceability (hashes, IDs and reason codes retained).

## 25. Security, Permissions and Secrets *(normative)*

**CDS500-R089** Connector credentials MUST be stored in a secret-management mechanism and MUST NOT be embedded in product records, logs or exported evidence.

**CDS500-R090** Connectors SHOULD use the least privilege sufficient for their declared operations.

**CDS500-R091** Create, update, delete, withdraw, override and repair actions SHOULD support distinct permissions.

## 26. Bulk Operations and Scale *(normative)*

**CDS500-R092** Bulk systems MUST preserve product- and field-level outcomes even when transport is batched.

**CDS500-R093** A batch restart SHOULD resume from durable item states rather than replaying the full batch.

**CDS500-R094** Checksums MAY be used to avoid unnecessary projection, dispatch or comparison work, provided the checksum inputs are versioned and auditable.

## 27. AI Participation *(normative)*

AI may assist with anomaly classification, mapping suggestions, repair recommendations, prioritisation and evidence summarisation. It is never the authority for downstream truth. *(AI governance, autonomy levels and proposal lifecycle: CDS-700.)*

**CDS500-R095** AI-generated repair actions MUST remain constrained by field ownership, permissions and approval policy (CDS500-R078/R079).

**CDS500-R096** AI MAY propose that two values are semantically equivalent, but only a governed comparator or approved mapping MUST determine the verification result.

**CDS500-R097** An AI agent MUST NOT convert an UNOBSERVABLE or PENDING field into MATCH based on likelihood or inference.

**CDS500-R098** AI repair and triage proposals SHOULD key off reason codes and detailed statuses, not presentation colours.

## 28. Worked Examples *(informative)*

### 28.1 Metafield round trip (API-integrated storefront, e.g. Shopify)

```
Canonical:        MF_material = linen
Expected:         custom.material = "Linen" (single_line_text_field)
Acknowledgement:  productUpdate accepted            -> PA-4
Observed:         "Linen" (independent read-back)   -> PA-5
Comparison:       NORMALIZED_TEXT                   -> MATCH
Presentation:     GREEN                             -> PA-6
```

### 28.2 Missing versus unobservable

```
Field A: expected "Linen"; read-back returns the field as null
  coverage = OBSERVED_EMPTY -> MISSING_DOWNSTREAM (core MISSING)
  reason_code = CDS_OBSERVED_EMPTY -> AMBER (escalates per CDS500-R070)

Field B: expected "Blue"; read-back interface does not expose the field
  coverage = UNSUPPORTED -> UNOBSERVABLE
  reason_code = CDS_INTERFACE_UNSUPPORTED -> AMBER
```

The two fields never share a reason code (§17.4 is the normative derivation).

### 28.3 Full-replace tag safety

```
Current channel tags:  collection_Shirts, merch_featured, review_five_star
Ownership:             collection_*, merch_* = PARTITIONED_PIM
                       review_* = external application
New PIM projection:    collection_Shirts, merch_sale
Safe merged payload:   collection_Shirts, merch_sale, review_five_star
```

Sending only the PIM tags to a full-replace API would delete `review_five_star` — a CDS500-R026/R027 violation. PIM-owned partitions are regenerated from rules on every publication.

### 28.4 Mapping change without product edit

Canonical revision stays at rev-12; the dictionary mapping changes (`navy -> Blue`, previously `Navy`). A new projection is required because `dictionary_version` changed (CDS500-R017); verification uses the new expected value.

### 28.5 Channel health summary

```
Channel 1 (API round-trip):        PA-7, match 99.6%, coverage 100%,
                                   0 critical failures      -> GREEN
Channel 2 (feed with diagnostics): PA-6, match 96.8%, coverage 91%,
                                   4 missing GTINs in the critical set -> RED (cap)
Channel 3 (write-only feed mode):  PA-4, no field read-back in this
                                   integration mode -> AMBER, "acknowledged,
                                   not verified"
```

Channel 3's limitation is a property of the *integration mode in use* (a write-only feed without item-level read-back), not of any named platform; the same platform integrated through an API with read-back could reach PA-6.

## 29. Conformance and Relationship to Other Chapters *(informative)*

Conformance levels, test suites and claim rules for this chapter's requirements are defined solely in CDS-1000. Machine-readable encodings of the entities, the eight-value core enum, `detailed_status`, `reason_code` and the validation-output contract are defined in CDS-1100 (the enum is encoded verbatim from §17). Platform-specific profile content is defined in CDS-900. Monitoring metrics and drift-age reporting: CDS-1400. The architecture decisions behind this chapter are recorded in the global ADR register (notably ADR-D3, ADR-D24; superseding the v0.1 chapter-local CDS-ADR-020..029, whose substance survives as requirements here).

---

## Appendix A — Normalisation Registry Seed *(informative except A.1)*

### A.1 Registry entry shape *(normative)*

**CDS500-R099** Each comparator registry entry MUST record: `comparator_id`, `version`, `input_types`, `normalisation_steps` (ordered), `equality_rule`, `tolerance` (where applicable), `diagnostics`, and `test_vectors` including negative cases (per CDS500-R056/R058).

### A.2 Seed entries (legacy production tolerance vectors — LEG-4/LC-2)

These are the first entries of the registry, restored from proven production comparison behaviour:

| comparator_id | Behaviour | Positive vector | Negative vector |
|---|---|---|---|
| MONEY.round2 | Round both sides to 2 dp, then numeric equality (with currency match) | 19.999 vs 20.00 -> MATCH | 19.99 vs 20.00 -> MISMATCH |
| MEASUREMENT.weight_round3 | Convert to common unit, round to 3 dp, numeric equality | 1.5 kg vs 1500 g -> MATCH | 1.5005 kg vs 1500 g -> MISMATCH |
| NORMALIZED_TEXT.v1 | Case fold, trim, collapse internal whitespace, then equality | " French  Navy " vs "french navy" -> MATCH | "French Navy" vs "Navy" -> MISMATCH |
| UNORDERED_SET.v1 | Same unique members regardless of order | {a,b,c} vs {c,a,b} -> MATCH | {a,b} vs {a,b,c} -> MISMATCH |

### A.3 Money and measurement tolerances

Rounding precision (2 dp money, 3 dp weight) is part of the comparator version. Changing precision is a comparator version change (CDS500-R056), never a silent edit.

### A.4 Documented negative case: substring false-green

Legacy text comparison used substring containment (spreadsheet `SEARCH()`), which tolerated case and whitespace — and also real prefix differences. Example: expected `"Blue"`, observed `"Blue Grey"` — substring containment reports a match; the values differ. This case MUST appear as a negative test vector for text comparators (CDS500-R058). Substring containment is not an equality rule in CDS.

## Appendix B — Reason-Code Seed List *(informative)*

The reason-code registry (identifiers, governance, additions) is owned by CDS-1100 §21. This seed list illustrates the codes this chapter's rules require:

| Reason code | Typical detailed status |
|---|---|
| CDS_OBSERVED_EMPTY | MISSING_DOWNSTREAM |
| CDS_FIELD_NOT_RETURNED | MISSING_DOWNSTREAM or UNOBSERVABLE (per §17.4) |
| CDS_INTERFACE_UNSUPPORTED | UNOBSERVABLE |
| CDS_PERMISSION_DENIED | UNOBSERVABLE |
| CDS_STALE_OBSERVATION | UNOBSERVABLE |
| CDS_PROPAGATION_WINDOW_EXPIRED | any post-lapse non-MATCH (§17.5) |
| CDS_AWAITING_PROPAGATION | PENDING |
| CDS_EXPECTED_REVISION_AHEAD | STALE_EXPECTED |
| CDS_VALUE_DIFFERS | MISMATCH |
| CDS_UNEXPECTED_VALUE_PRESENT | UNEXPECTED_DOWNSTREAM |
| CDS_IDENTITY_MISMATCH | MISMATCH / drift IDENTITY_MISMATCH |
| CDS_CHANNEL_TRUNCATION | MISMATCH / drift CHANNEL_TRUNCATION |
| CDS_TRANSFORMATION_FAILED | TRANSFORMATION_ERROR |
| CDS_DISPATCH_REJECTED | PUBLICATION_ERROR |
| CDS_READBACK_FAILED | OBSERVATION_ERROR |
| CDS_COMPARATOR_FAILED | COMPARISON_ERROR |
| CDS_WAIVED_EXCEPTION | WAIVED |
| CDS_OVERRIDE_ACTIVE | (provenance on overridden results) |
| CDS_NOT_IN_CONTRACT | NOT_APPLICABLE |

## Appendix C — Platform, Legacy and Schema Pointers *(informative)*

- **Platform specifics.** The v0.1 Appendices C (Shopify implementation profile) and D (Google Merchant and feed-based channels) are replaced by the versioned, dated implementation profiles in **CDS-900**. Platform behaviour never shapes the requirements of this chapter (Reconciliation Matrix 5).
- **Legacy alignment.** The legacy Airtable/Shopify prefix mapping and migration alignment (v0.1 Appendix E) lives in the consolidated legacy annex (see CDS-1300). The migration mapping of legacy match fields is 1:1: green -> MATCH, amber -> MISSING/PENDING, red -> MISMATCH (ADR-D3); `DF_*` feed fields migrate to `CH_*` per ADR-D24, with the feed-layer verification pattern retained in §19.
- **Schemas.** Recommended entity schemas (the v0.1 Appendix A sketch) are superseded by the machine-readable contracts in **CDS-1100**: verification-result schema carries `status` (8-value core enum), `detailed_status`, `reason_code`, `coverage_ratio` and `comparison_engine_version`.

## Appendix D — Operational Checklist *(informative)*

1. Confirm the canonical revision is approved for publication.
2. Generate the projection with current profile, mappings, dictionaries and overrides.
3. Run blocking and warning preflight checks; preview additions, changes, removals and full-replace list effects.
4. Confirm field ownership and destructive-operation permissions.
5. Dispatch with correlation and idempotency identifiers where supported.
6. Record acknowledgement without treating it as verification.
7. Observe downstream state after the declared propagation window.
8. Normalise and compare with declared registry comparators.
9. Derive statuses per §17; present detailed status and reason code beneath any traffic light.
10. Classify drift; execute the governed repair or exception policy; re-verify.
11. Retain payload, response, observation, comparison and actor evidence.


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-600 — Customer Experience, Facets and Navigation

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-600 Working Draft v0.1 |
| Normative status | §1, §3, §5–§29 are normative. §2, §4, §30–§32 and all appendices are informative. Examples and notes inside normative sections are informative unless marked otherwise. |
| Findings addressed | SYS-1 (CLEANUP-PASS §C: all 118 prefix-labelled rules corrected — 76 different-inline-keyword, 42 label-strip-only), SYS-2 (requirement IDs), SYS-4, CDS-600-2, CDS-600-3 (D10), CDS-600-4, CDS-600-5, CDS-600-6 (D11), CDS-600-7, CDS-600-8, CDS-600-9, CDS-600-10, CDS-600-11 |

CDS-600 is the single normative home for facets and customer-experience projection (CDS000-R005), including zero-result and unavailable facet-value behaviour (§17, per open decision D10). CDS-1500 and other chapters cite this chapter and do not restate its rules.

---

## 1. Purpose and Scope *(normative)*

CDS-600 defines how canonical product information is projected into customer-facing discovery experiences: site navigation, category and collection pages, facets, search refinement, sorting, product-card presentation, and the governance that keeps those experiences coherent as a catalogue grows. It does not prescribe a visual design system; it specifies the information, behaviour and quality rules beneath the interface so that different storefronts may implement distinct designs without weakening customer comprehension or data integrity.

**CDS600-R001** A CDS implementation MUST derive customer-facing discovery structures from governed product information rather than from uncontrolled labels entered independently in the storefront.

**CDS600-R002** Customer-facing simplification MUST NOT destroy the richer canonical or source information held by the PIM.

**CDS600-R003** A storefront MAY vary presentation by device, market or audience, provided the underlying meaning remains consistent.

## 2. Customer Experience Principles *(informative)*

- **Customer language first** — labels use terms customers understand, even when internal or channel taxonomies use different wording.
- **Progressive disclosure** — reveal enough structure to support a decision without presenting the whole data model at once.
- **Controlled simplicity** — rich canonical data is grouped into concise facets and navigation choices (CDS-P-08).
- **Predictable behaviour** — the same control and value behaves consistently across categories unless a documented category profile requires otherwise.
- **No dead ends** — filtering and search minimise preventable zero-result states and provide useful recovery (§17).
- **Availability-aware discovery** — customers are not encouraged toward choices that cannot produce a purchasable result (§16–§17).
- **Accessible by default** — discovery controls remain understandable and operable without relying on colour, pointer input or visual position alone (§24, normative).
- **Measurable quality** — facet, search and navigation performance is evaluated with behavioural and data-quality evidence (§28).

## 3. Experience Architecture *(normative)*

```
Canonical Product Information
  |-- Internal Taxonomy
  |-- Controlled Dictionaries
  |-- Attribute and Variant Values
  `-- Merchandising Rules
          |
          v
Customer Experience Projection
  |-- Navigation and Category Pages
  |-- Collections and Facets
  |-- Search, Sort and Ranking
  `-- Product Card Presentation
          |
          v
Experience Analytics and Health
```

**CDS600-R004** Customer experience structures MUST be treated as projections of canonical information, not as independent product facts.

**CDS600-R005** The PIM or governed commerce layer SHOULD be able to explain which canonical values and rules produced each customer-facing label, filter and collection membership.

## 4. Shopping Modes and Customer Intent *(informative)*

| Mode | Typical behaviour | Primary support |
|---|---|---|
| Directed search | Customer knows a product, brand, model or requirement | Search, synonyms, identifiers, relevance ranking |
| Category browsing | Customer knows the general kind of product | Navigation, categories, collections, breadcrumbs |
| Attribute refinement | Customer narrows by colour, size, material, room or specification | Facets and counts |
| Inspirational discovery | Customer begins with a style, occasion, campaign or need | Editorial collections, merchandising, cross-links |
| Comparison | Customer evaluates similar products | Consistent attributes, sorting, comparison-ready presentation |

A taxonomy answers what a product *is*. Merchandising and facets help customers discover why it may be *relevant* to them.

## 5. Taxonomy, Navigation, Collections, Facets and Search *(normative)*

| Construct | Primary question | Typical source |
|---|---|---|
| Taxonomy / category | What is this product? | Internal classification (CDS-200 §6) |
| Navigation | Where should customers begin browsing? | Selected category and collection nodes |
| Collection | Which products should be presented together? | Taxonomy, merchandising rules or curation |
| Facet | Which characteristic should refine the current result set? | Controlled attribute projection (CDS-400) |
| Search | Which products are relevant to this query? | Index, synonyms, attributes, ranking signals |

**CDS600-R006** These constructs MUST remain logically distinct even when a platform implements more than one of them with the same technical feature.

**CDS600-R007** A collection MUST NOT be treated as a substitute for a missing controlled attribute when customers need to refine by that attribute.

**CDS600-R008** A facet MUST NOT be used to redefine a product category.

## 6. Navigation Architecture *(normative)*

Navigation is a curated entry into the catalogue, not a complete rendering of every internal category. It exposes stable, meaningful destinations and defers fine-grained refinement to facets.

**CDS600-R009** Primary navigation SHOULD expose no more than the levels required for customers to orient themselves and reach a useful product set.

**CDS600-R010** Deep internal taxonomy nodes MAY remain available through category pages, search or links without appearing in the main menu.

**CDS600-R011** Navigation labels MUST have clear, non-overlapping meanings within the same level.

**CDS600-R012** A product MAY be discoverable from multiple navigation paths while retaining one primary internal category (CDS-200 §6).

> Informative note: the one-primary-category rule protects classification integrity. Cross-links and collections solve merchandising overlap without duplicating product identity.

## 7. Category and Collection Architecture *(normative)*

Category pages represent product types or taxonomy nodes. Collections represent merchandising groupings such as New Arrivals, Winter Edit or Staff Picks. Both may be customer-facing, but they carry different meanings.

**CDS600-R013** A category page SHOULD inherit its product membership from classification or an equivalent deterministic rule.

**CDS600-R014** A merchandising collection MUST declare whether membership is computed, manually curated or hybrid.

**CDS600-R015** Temporary collections SHOULD have an owner, activation window and retirement rule.

**CDS600-R016** Parent pages SHOULD explain their scope and provide clear paths to child categories or relevant facets.

## 8. Information Scent and Labels *(normative)*

Information scent is the customer's ability to predict what lies behind a label or control. Weak labels force experimentation; strong labels make the catalogue feel smaller and more understandable.

**CDS600-R017** Navigation, collection and facet labels MUST be written in customer language and SHOULD avoid internal abbreviations.

**CDS600-R018** A label MUST distinguish neighbouring choices. Terms such as Other, General or Miscellaneous SHOULD be avoided unless no clearer grouping exists.

**CDS600-R019** Where a term is ambiguous across industries or regions, the label SHOULD include qualifying context.

**CDS600-R020** Synonyms MAY support search, but the interface SHOULD present one preferred label per concept.

## 9. Facet Model and Facet Definitions *(normative)*

A facet is a customer-facing refinement dimension (CDS-100). A Facet Definition governs its label, values, applicability, selection behaviour, ordering, counts, visibility and mapping from canonical attributes.

| Property | Requirement |
|---|---|
| Stable ID | Machine identifier independent of display label |
| Label | Localisable customer-facing name |
| Description | Meaning and inclusion boundaries |
| Source | Canonical attribute or derived rule |
| Eligibility | Applicable categories, collections or search contexts |
| Value model | Dictionary, numeric range, boolean or hierarchy |
| Selection mode | Single-select, multi-select or range |
| Within-facet operator | OR or AND within the facet |
| Count unit and method | Products, purchasable variants or another declared unit; count semantics per §16 |
| Ordering | Semantic, numeric, popularity or alphabetic |
| Disclosure | Expanded, collapsed, hidden or conditional |
| Unavailable-value behaviour | Per §17 |
| Analytics key | Stable event identifier |
| Owner | Responsible data or merchandising role |

**CDS600-R021** Every customer-facing facet MUST have a governed Facet Definition.

**CDS600-R022** Facet values MUST come from controlled canonical or facet dictionaries (CDS-400), not from unrestricted distinct strings.

**CDS600-R023** The same logical facet SHOULD retain one identifier across channels even where the display label is localised.

**CDS600-R024** A Facet Definition MUST declare its count unit (products, purchasable variants or another declared unit) and its count method (§16).

**CDS600-R025** A Facet Definition MUST declare its selection logic; interfaces MUST NOT rely on undocumented platform defaults.

**CDS600-R026** How facets combine across a result set is a property of the facet set, not of an individual facet. The cross-facet operator MUST be declared at the facet-set (category- or context-profile) level, and a Facet Definition MUST NOT carry its own cross-facet operator. *(Resolves CDS-600-4; see §15 and Appendix A.)*

## 10. Facet Eligibility *(normative)*

Not every attribute should become a filter. Eligibility is determined by customer usefulness, coverage, value distribution, category relevance and interface cost:

| Criterion | Question |
|---|---|
| Decision relevance | Does the attribute meaningfully affect product choice? |
| Coverage | Is the value populated for enough products in the eligible result set? |
| Discrimination | Does the facet divide the catalogue into useful groups rather than one dominant value and many singletons? |
| Comprehension | Will customers understand the values without specialist knowledge? |
| Stability | Are values governed and unlikely to change unpredictably? |
| Result utility | Will selecting a value usually leave a useful product set? |
| Maintenance | Can the organisation govern the dictionary and mappings? |

**CDS600-R027** A field MUST NOT become a facet merely because the platform permits filtering on it.

**CDS600-R028** Facet eligibility SHOULD be reviewed per category profile rather than globally.

**CDS600-R029** Low-coverage or highly fragmented facets SHOULD remain hidden until data quality and grouping are adequate (thresholds per §28).

## 11. Value Projection for Facets *(normative)*

The value-layer model (Source Value -> Alias Mapping Record -> Canonical Value -> projections) is owned by CDS-400 and defined per ADR-D4; terms per CDS-100 §3. Facet Values are one projection branch:

```
Canonical Value
  +--> Display Label
  +--> Facet Value
  +--> Search Synonyms
  +--> Channel Representation
```

**CDS600-R030** Facet values MUST be projections of canonical values and MUST NOT replace those canonical values in the PIM.

**CDS600-R031** Many canonical values MAY map to one broader facet value when that grouping improves customer comprehension.

**CDS600-R032** A canonical value MAY map to more than one facet group only where the secondary membership is deliberate, documented and non-deceptive.

## 12. Colour Facets *(normative)*

Colour is a high-risk facet because suppliers and brands use rich marketing names while customers generally need a concise set of recognisable families. CDS separates the sellable colour, its Display Label and its facet family.

**CDS600-R033** *(Definition — resolves CDS-600-7.)* The **sellable colour** of a Variant is the canonical value of its colour Variant Option (CDS-100 §2–§3). What the customer sees is that canonical value's Display Label (e.g. "French Navy"); what filtering uses is the Facet Value the canonical value maps to (e.g. Blue). Implementations MUST maintain this distinction; the Display Label is never itself the canonical value.

```
Display Label (sellable colour as shown):  French Navy
Canonical value:                           colour_french_navy (shade: navy)
Primary facet family:                      Blue
Optional tone:                             Dark
Search synonyms:                           navy, dark blue, french navy
Swatch:                                    governed visual sample
```

**CDS600-R034** A colour facet MUST use a controlled colour-family dictionary rather than exposing every display colour as a separate filter value.

**CDS600-R035** The storefront MAY display the sellable colour's Display Label on the product card or product page while filtering by the broader family.

**CDS600-R036** Colour swatches MUST NOT be the sole means of communicating a value; a text label MUST remain available (§24).

**CDS600-R037** Multi-colour, transparent, metallic and natural finishes SHOULD be modelled explicitly rather than forced into an inaccurate basic hue. Multicolour is a facet/status value, never a canonical shade (CDS-100 §3).

**CDS600-R038** Where a product contains several meaningful colours, the system SHOULD distinguish primary colour, secondary colour and multicolour status.

> Informative note *(resolves CDS-600-6 per D11)*: the exemplar colour-family baseline — including the core family set and the boundary rules for neighbours such as Cream/Beige/Natural/White and Silver/Grey — is owned by CDS-1500 Appendix C. This chapter deliberately publishes no family list of its own; the exact dictionary remains profile-specific and is adopted from that baseline.

## 13. Size, Fit and Dimension Facets *(normative)*

Size information is frequently variant-level and may use category-specific scales. Fit describes intended garment shape and normally remains product-level. Dimensions may require units and ranges rather than labels.

**CDS600-R039** Size facets MUST preserve the distinction between the displayed size label and the normalised size order or scale.

**CDS600-R040** A category profile MUST define which size system applies (e.g. alpha, numeric apparel, footwear, waist, bedding, dimensional).

**CDS600-R041** Size values MUST sort semantically rather than alphabetically.

**CDS600-R042** Fit MUST NOT be inferred from size alone.

**CDS600-R043** Numeric dimension facets SHOULD use normalised units and MAY present customer-local units.

> Informative note: a size label of 10 may represent different measurements in different markets. CDS therefore requires profile and unit context rather than treating the visible label as a universal canonical value.

## 14. Material, Style, Pattern, Occasion and Room Facets *(normative)*

| Facet | Canonical detail | Typical facet projection |
|---|---|---|
| Material | linen; cotton; oak; stoneware | Linen; Cotton; Wood; Ceramic |
| Composition | 80% cotton / 20% polyester | Cotton or Cotton Blend, per declared policy |
| Pattern | fine white pinstripe | Striped |
| Style | relaxed coastal resort shirt | Coastal and/or Relaxed, per profile |
| Occasion | beach holiday | Beach / Holiday |
| Room | living room cushion | Living Room |
| Finish | natural Tasmanian oak | Natural / Wood |

**CDS600-R044** Material composition MUST remain separately available from the simplified material facet where percentages or blends matter.

**CDS600-R045** Style and occasion facets SHOULD use a small governed vocabulary and MUST NOT become an uncontrolled list of marketing phrases.

**CDS600-R046** Homewares facets SHOULD be category-aware; a Room facet may be useful for decor but irrelevant for cookware components. *(Industry baselines: CDS-1500.)*

## 15. Selection Logic *(normative)*

Selection logic determines how multiple chosen values combine. The intended logic must be explicit because platforms and customers may otherwise interpret the same control differently. Cross-facet combination is declared per facet set (CDS600-R026).

**CDS600-R047** Different facets SHOULD combine with AND logic (Blue AND Linen), as the declared facet-set default.

**CDS600-R048** Multiple values within the same categorical facet SHOULD combine with OR logic (Blue OR Green).

**CDS600-R049** An AND-within-facet mode MAY be used where a product must possess all selected values, but the interface MUST make that behaviour clear.

**CDS600-R050** Single-select facets MUST prevent contradictory simultaneous choices.

**CDS600-R051** A range facet MUST define inclusive boundaries, units and rounding behaviour.

```
Selected:
  Colour: Blue OR Green
  Material: Linen
  Size: M OR L
Result logic:
  (Blue OR Green) AND Linen AND (M OR L)
```

## 16. Counts and Variant Availability *(normative)*

Facet counts can represent products or sellable variants. Availability-aware variant counting ensures that selecting Blue and Size M returns products with a purchasable Blue/M combination, not products that merely have Blue somewhere and M somewhere.

**CDS600-R052** Facet counts MUST declare their counting unit and availability scope (CDS600-R024).

**CDS600-R053** Variant-defined facets SHOULD evaluate valid variant combinations rather than independent product-level unions.

**CDS600-R054** Where the storefront platform supports combination-level availability filtering, a product MUST NOT be counted as satisfying a selected combination unless at least one eligible sellable unit satisfies the complete selected combination.

**CDS600-R055** Where the storefront platform does not support combination-level availability filtering, the implementation MUST disclose that limitation in its platform profile (CDS-900) and SHOULD approximate combination behaviour as closely as the platform allows. *(Resolves CDS-600-2.)*

> RESOLVED (was CDS-600-2 (resolved); verified 2026-08-04, REVIEW-006A): the conditional structure of R054/R055 stands (it is the correct platform-neutral form), and the pending question is answered — **native Shopify Search & Discovery evaluates variant-option and availability filters at variant scope** (`filter.v.option.*`, `filter.v.availability`; different filters AND at variant level), so the Shopify profile declares the capability present (CDS-900 §4.7). Per-value count accuracy under combined selections remains a vertical-slice empirical check.

> Informative note *(preserved)*: R054 prevents the classic false-positive result where a shirt has Blue only in Small and Medium only in White, yet appears after Blue + Medium is selected.

**CDS600-R056** *(Disjunctive count semantics — resolves CDS-600-5.)* Within a multi-select OR facet, the count displayed for an unselected value MUST be computed against the result set produced by all *other* facet selections, excluding that facet's own current selection, so that the count predicts the effect of adding the value rather than reporting the already-filtered set. The count method in force MUST be declared in the Facet Definition (CDS600-R024).

**CDS600-R057** The interface SHOULD update counts or availability after each selection so customers can anticipate the effect of another filter.

## 17. Unavailable Values and Zero-Result Recovery *(normative — single normative home per D10)*

This section is the corpus-wide normative home for zero-result and unavailable facet-value behaviour. CDS-1500 §19 and any other chapter cite this section and MUST NOT restate or vary these rules. The stricter CDS-1500 wording is adopted here as the governing MUST. *(Resolves CDS-600-3.)*

**CDS600-R058** A facet value whose selection would produce no truthful available result in the current context MUST be disabled or hidden.

**CDS600-R059** As a governed exception to R058's hiding branch, out-of-stock values MAY remain visible for discovery only where the interface presents a clear unavailable state; unavailable values MUST be distinguished from purchasable options and MUST NOT be presented as normally selectable.

**CDS600-R060** When no results remain, the interface MUST preserve the selected filters and provide a clear recovery action.

**CDS600-R061** Recovery SHOULD identify the narrowest selected constraint or offer removal of one filter at a time.

**CDS600-R062** A zero-result message MUST NOT imply that the store has no relevant products when the result is caused by an over-restrictive combination.

## 18. Ordering, Defaults and Disclosure *(normative)*

Facet order and value order are part of the merchandising experience. Alphabetical sorting is appropriate only when it matches how customers think about the values.

**CDS600-R063** High-value decision facets SHOULD appear before secondary descriptive facets.

**CDS600-R064** Size, numeric ranges and lifecycle stages MUST use semantic order rather than alphabetical order.

**CDS600-R065** Colour families MAY use a stable merchandising order or a visual palette order, provided labels remain accessible.

**CDS600-R066** Long value lists SHOULD use search, grouping or progressive disclosure rather than expanding the page indefinitely.

**CDS600-R067** A facet SHOULD be expanded by default only when it is broadly useful in the current context.

## 19. Mobile and Responsive Filtering *(normative)*

**CDS600-R068** Mobile filtering MUST expose the number of active filters and provide a persistent way to clear or edit them.

**CDS600-R069** An apply action MAY defer result updates inside a mobile filter panel; where it does, the apply control MUST display a preview of the result count that will apply, and selected counts and availability SHOULD remain understandable while the panel is open. *(Resolves CDS-600-9.)*

**CDS600-R070** Filter controls MUST remain operable with touch targets, keyboard navigation and assistive technology (§24).

**CDS600-R071** A long mobile facet list SHOULD support internal search or grouping rather than forcing excessive scrolling.

**CDS600-R072** Closing the filter interface MUST preserve current selections unless the user explicitly cancels them.

## 20. Search, Synonyms and Query Understanding *(normative)*

Search and facets share dictionaries but serve different interactions: search interprets free-form intent; facets expose governed choices.

**CDS600-R073** Search indexes SHOULD include canonical values, display labels, approved aliases and relevant facet families.

**CDS600-R074** A search synonym MUST map to a preferred concept or query expansion and MUST NOT create an uncontrolled duplicate value.

**CDS600-R075** Brand, SKU, MPN and GTIN identifiers SHOULD be indexed according to access and relevance requirements.

**CDS600-R076** Search query interpretation MAY infer a facet selection, but the resulting refinement SHOULD be visible to the customer.

**CDS600-R077** Misspelling tolerance and semantic expansion MUST NOT override exact product identifiers or create materially misleading results.

```
Query: "navy linen shirt"
Interpreted intent:
  Product type = Shirt
  Colour facet = Blue / canonical navy
  Material facet = Linen
Visible refinements:
  Shirts | Blue | Linen
```

## 21. Sorting and Ranking *(normative)*

**CDS600-R078** Every sort option MUST declare the data and tie-breakers used.

**CDS600-R079** Price sorting MUST use the same customer-visible price basis used in the current market and tax context.

**CDS600-R080** Newness SHOULD use a governed publication or arrival date, not an arbitrary last-edit timestamp.

**CDS600-R081** Relevance ranking MAY use behavioural signals, but product-data completeness and availability SHOULD remain quality inputs.

**CDS600-R082** Sponsored or commercially influenced ranking MUST be identifiable where applicable.

> Informative note: Best Selling, Featured and Recommended are not self-defining technical fields. Each requires a documented calculation or merchandising owner.

## 22. Product Cards and Variant Presentation *(normative)*

**CDS600-R083** A product card SHOULD display the attributes necessary to distinguish neighbouring products without reproducing the entire product page.

**CDS600-R084** Variant swatches or size indicators MUST reflect actual eligible variants and availability.

**CDS600-R085** A colour swatch SHOULD use the governed Display Label and visual sample, while its filter behaviour uses the facet family.

**CDS600-R086** Product-card badges such as New, Sale, Clearance or Exclusive MUST originate from governed lifecycle or merchandising rules.

**CDS600-R087** A product card MUST NOT show an unavailable price or variant as though it were the active purchasable choice.

## 23. Breadcrumbs, Cross-Links and Merchandising Overlap *(normative)*

**CDS600-R088** Breadcrumbs SHOULD reflect the chosen customer navigation context while remaining consistent with the primary category model.

**CDS600-R089** Cross-links MAY surface a product to another audience without assigning a second primary category.

**CDS600-R090** Editorial and campaign pages SHOULD link back to stable category or collection destinations where customers can continue browsing.

**CDS600-R091** A product appearing in several collections MUST retain one canonical identity and one primary classification.

## 24. Accessibility *(normative)*

**CDS600-R092** Facet groups and controls MUST have programmatically determinable labels.

**CDS600-R093** Selected state, disabled state and result counts MUST be exposed to assistive technology.

**CDS600-R094** Colour swatches and colour indicators MUST include text alternatives, and colour MUST NOT be the sole signal for any value, state or distinction.

**CDS600-R095** Keyboard focus MUST follow a logical order and remain visible.

**CDS600-R096** Changes to result counts MUST be announced to assistive technology without causing disruptive focus movement.

**CDS600-R097** Clear-all and remove-filter controls MUST have unambiguous accessible names.

**CDS600-R098** Range controls MUST expose current values, minimum, maximum and units.

## 25. Performance and Resilience *(normative)*

**CDS600-R099** An implementation MUST declare a response-time target for facet and filter interactions and MUST monitor performance against that declared target. *(Resolves CDS-600-8; replaces the untestable "quickly enough" wording.)*

> Informative note: the intent of the target is that the interface preserves a direct, perceptible relationship between a selection and its response.

**CDS600-R100** The storefront MUST fail safely when a facet service is unavailable; product browsing SHOULD remain possible.

**CDS600-R101** Cached counts MUST identify their freshness and MUST NOT be presented as live availability when they are materially stale relative to the declared target and propagation windows.

**CDS600-R102** Large dictionaries SHOULD support indexed lookup rather than rendering all values unconditionally.

**CDS600-R103** Performance optimisation MUST NOT change selection semantics or counts without explicit disclosure.

## 26. Faceted Navigation and SEO *(normative)*

Faceted combinations can create an unbounded number of URLs. CDS does not prescribe one search-engine policy, but requires explicit governance so that customer refinement does not accidentally generate a duplicate crawl space.

**CDS600-R104** An implementation MUST define which facet combinations are indexable, canonicalised, blocked or represented without unique URLs.

**CDS600-R105** Indexable landing pages SHOULD have stable intent, sufficient product depth and unique explanatory content.

**CDS600-R106** Transient or extremely narrow combinations SHOULD NOT become indexable pages by default.

**CDS600-R107** The canonical category and collection structure MUST remain discoverable independently of facet-generated URLs.

**CDS600-R108** SEO policy MUST NOT weaken customer filter behaviour merely to simplify crawling.

## 27. Personalisation and AI *(normative)*

AI proposal, evidence, approval and autonomy rules are owned by CDS-700; dictionary authority by CDS-400. This section carries only the customer-experience rules.

**CDS600-R109** Personalisation MAY reorder facets, values or products but MUST NOT change the semantic meaning of a facet.

**CDS600-R110** A personalised interface MUST retain a predictable way to access the full applicable filter set.

**CDS600-R111** Sensitive personal inference MUST NOT be required for ordinary product discovery.

> Informative note: AI may suggest facet mappings, synonyms, labels and collection memberships only as proposals under CDS-700 governance; governed dictionaries and approval rules remain authoritative (CDS-400, CDS-700).

## 28. Measurement and Analytics *(normative)*

| Measure | Examples *(informative)* |
|---|---|
| Facet usage | Selections, removals, clear-all events and sequence |
| Result quality | Zero-result rate, low-result rate and recovery |
| Coverage | Percentage of eligible products populated per facet |
| Fragmentation | Number of values, singleton values and long-tail share |
| Discovery | Search-to-filter transitions and navigation depth |
| Conversion support | Outcome after facet or search interaction |
| Performance | Response latency against the declared target (R099) |
| Accessibility | Keyboard and assistive-technology defects |
| Data drift | Unexpected values or missing mappings |

**CDS600-R112** Analytics identifiers MUST remain stable when display labels change.

**CDS600-R113** Facet analytics SHOULD distinguish exposure, interaction and resulting product-set size.

**CDS600-R114** The organisation MUST declare its thresholds for facet usage and facet coverage. A facet whose usage exceeds the declared usage threshold while its coverage falls below the declared coverage threshold MUST trigger data-quality review rather than automatic removal. *(Resolves CDS-600-11; replaces the untestable "high-use facet with poor coverage".)*

## 29. Governance and Change Management *(normative)*

Roles, decision rights and change control in general are owned by CDS-800; dictionary and mapping workflows by CDS-400. This section carries the facet-specific rules.

**CDS600-R115** Every facet MUST have an owner responsible for definition, dictionary, coverage and retirement.

**CDS600-R116** New facet values MUST enter through the governed dictionary or mapping workflows defined in CDS-400.

**CDS600-R117** Renaming a visible label SHOULD preserve the stable facet and value identifiers.

**CDS600-R118** Merging or splitting values MUST include migration, publication, search and analytics impact analysis.

**CDS600-R119** Facet changes SHOULD be tested against representative categories, devices and product combinations before release.

**CDS600-R120** Deprecated values MUST retain aliases or redirects long enough to protect imports, saved URLs and historical analytics where applicable.

## 30. Worked Examples *(informative)*

### 30.1 Apparel: colour and size

```
Product: Relaxed Linen Shirt
Variants:
  French Navy / S / in stock
  French Navy / M / out of stock
  White / M / in stock
Canonical:
  colour: colour_french_navy -> facet Blue (Display Label "French Navy")
  colour: colour_white       -> facet White
  size scale: Alpha Apparel
Customer selects Blue + M:
  Product excluded — no purchasable Blue/M variant exists (R054).
Customer selects Blue:
  Product included; product card shows "French Navy" (R035).
```

### 30.2 Homewares: material and room

```
Product: Tasmanian Oak Side Table
Canonical material: oak            Display material: Tasmanian Oak
Material family facet: Wood        Room facets: Living Room, Bedroom
Style facet: Contemporary
Filters on Side Tables collection: Material, Colour, Style, Shape, Width, Price
Room may remain available on a broader Furniture collection (R046).
```

### 30.3 Pattern simplification

```
Display pattern: Fine White Pinstripe
Canonical pattern: pinstripe
Facet value: Striped
Search aliases: pinstripe, stripe, striped
```

The customer sees "Striped" in filters and "Fine White Pinstripe" on the product page.

## 31. Conformance *(informative)*

Conformance levels, test suites and claim rules are defined solely in CDS-1000 (CDS000-R012). CDS-600 conformance is assessed against the requirement IDs in this chapter; the UX-oriented test suite (T-UX) covers them per CDS-1000. No conformance content is defined here.

## 32. Design Decision Summary *(informative)*

Chapter-level ADRs from v0.1 are queued for the single global ADR register (CDS000-R006). Their substance, as carried forward:

| v0.1 ADR | Decision as carried into v0.2 |
|---|---|
| CDS-ADR-601 | Facet values are projections, separate from canonical values (§11) |
| CDS-ADR-602 | Taxonomy and collections remain distinct (§5, §7) |
| CDS-ADR-603 | Colour filters use controlled families; the exemplar baseline is owned by CDS-1500 App C (§12, D11) |
| CDS-ADR-604 | Within-facet OR and cross-facet AND are the defaults; cross-facet combination is a facet-set property (§15, CDS-600-4) |
| CDS-ADR-605 | Variant combinations determine availability-aware results, conditional on platform capability with mandatory disclosure (§16, CDS-600-2) |
| CDS-ADR-606 | Facet Definitions are first-class governed entities (§9) |
| CDS-ADR-607 | Faceted SEO policy is implementation-specific but mandatory (§26) |

---

## Appendix A. Recommended Facet Definition and Facet-Set Schemas *(informative)*

Per-facet definition (cross_facet_operator removed per CDS600-R026):

```
facet_id
label
localised_labels
source_attribute_ids
eligible_category_ids
value_dictionary_id
selection_mode
within_facet_operator
count_unit
count_method            # incl. disjunctive-count semantics per R056
availability_policy     # unavailable-value behaviour per section 17
value_sort_strategy
facet_sort_priority
default_disclosure
mobile_presentation
accessible_label
analytics_id
owner
status
version
created_at
updated_at
```

Facet-set / category-context profile (holds what was per-facet in v0.1):

```
facet_set_id
context                 # category, collection or search context
member_facet_ids        # ordered
cross_facet_operator    # normally AND (R047)
response_time_target    # declared per R099
owner
version
```

## Appendix B. Industry Facet Baselines *(informative)*

The apparel and homewares facet profiles and the exemplar colour-family baseline formerly in this chapter's Appendices B and C are owned by CDS-1500 (industry dictionaries and profiles; colour families in CDS-1500 Appendix C). *(Resolves CDS-600-10.)*

## Appendix C. Platform Implementation Profiles *(informative)*

Platform-specific guidance (including the former Shopify implementation notes) lives in versioned, dated CDS-900 profiles. Platform declarations relevant to this chapter: combination-level availability filtering capability (R054/R055) and any facet value/group limits.

## Appendix D. Operational Review Checklist *(informative)*

- Are primary categories and collections clearly distinguished?
- Does every visible facet have a definition, owner and controlled value source?
- Are colour values grouped into a manageable customer-facing dictionary (per the CDS-1500 baseline)?
- Are size values ordered by the correct category and market scale?
- Do variant combinations produce truthful availability-aware results, or is the platform limitation disclosed?
- Are low-coverage and highly fragmented facets hidden or remediated against declared thresholds?
- Can customers recover easily from zero results?
- Are mobile controls accessible, and do deferred-apply controls preview the result count?
- Are search synonyms governed rather than invented per product?
- Are facet URLs and indexing rules documented?
- Are facet analytics stable across display-label changes?
- Are customer-facing values verified after publication (CDS-500)?
- Is the declared response-time target being monitored?


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-700 — AI Enrichment, Automation and Human Oversight

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-700 Working Draft v0.1; CDS-800 v0.1 §29 (AI governance rules consolidated here per the single-home rule) |
| Normative status | §1, §3, §5–§33 are normative. §2, §4, §34 and Appendices A–D are informative. |
| Findings addressed | SYS-1 (errata manifest §C: all 105 prefix-labelled rules corrected), SYS-2/700-2 (requirement IDs), 700-3, 700-4, 700-5, 700-6, 700-7, 700-8, 700-9; Matrix 2 (D14, open), Matrix 5 (AI single-home); provides the autonomy-scaled monitoring hook for 1400-11 |

CDS-700 is the single authoritative home for AI and probabilistic-automation requirements in CDS (CDS000-R005). Other chapters cite this chapter and do not restate its rules. This chapter in turn cites: statuses and verification — CDS-500; namespace registry — CDS-300; dictionaries and value layers — CDS-400; facets and customer experience — CDS-600; governance roles and change control — CDS-800; platform profiles — CDS-900; conformance levels and the T-AI test suite — CDS-1000; the machine-readable AI-proposal contract — CDS-1100.

---

## 1. Purpose and Scope *(normative)*

CDS-700 defines how artificial intelligence and other probabilistic automation may participate in a PIM-first commerce data environment: extraction, classification, normalisation, dictionary mapping, content generation, translation, media analysis, channel assistance, human review, evaluation and operational governance. It does not select a model vendor, prompting framework or orchestration technology; it defines the information contracts and assurance boundaries that hold regardless of which model, agent or platform performs the work.

**CDS700-R001** AI MUST operate as a producer of proposals, evidence or bounded actions; it MUST NOT become the implicit source of truth for product information.

**CDS700-R002** AI-generated information MUST conform to the same schemas, dictionaries, validation rules and publication controls as information entered by a human or imported from a supplier.

**CDS700-R003** The PIM MUST remain the master product-information layer when AI is used (CDS-200; CDS-P-02).

**CDS700-R004** An implementation MUST make AI participation visible and auditable: authorised operators MUST be able to enumerate the active AI workflows (via the registry of §33) and inspect the work objects (§6) behind any AI-originated value.

## 2. AI Principles *(informative)*

- **Canonical authority remains human-governed.** AI may propose or transform; acceptance into canonical state follows declared policy.
- **Evidence before assertion.** Product facts are supported by eligible evidence (§7).
- **Schema before prose.** AI fills governed fields and controlled values before producing unconstrained text.
- **Abstention is valid.** Returning unknown or requesting review is a first-class outcome, safer than a confident invention.
- **Risk determines autonomy.** Low-risk, reversible tasks may be automated more aggressively than pricing, compliance, safety or product claims.
- **Deterministic rules stay deterministic.** Validation, arithmetic, unit conversion and exact mappings are not delegated to probabilistic reasoning when reliable rules exist.
- **Humans remain legible participants.** AI workflows and field names are understandable without specialist prompt-engineering knowledge (CDS-P-04).
- **Evaluation precedes scale.** A workflow is tested on representative products before it touches a whole catalogue.
- **Publication remains assured.** AI does not bypass CDS-500 expected-state, observation and verification controls.
- **Provenance survives acceptance.** Accepted values retain their source, evidence and AI-generation history without polluting the canonical field name.

## 3. AI Participation Architecture *(normative)*

```
Eligible Source Evidence
        |
        v
Schema + Dictionaries + Rules + Task Policy
        |
        v
AI Proposal / Transformation / Classification
        |
        v
Validation + Confidence + Evidence Check
        |
        +--> Reject / Abstain / Quarantine
        |
        v
Human or Policy Approval
        |
        v
Canonical Acceptance or Draft Content
        |
        v
CDS-500 Publication and Verification
```

**CDS700-R005** Every AI workflow MUST identify its inputs, expected output schema, validation rules, approval policy and permitted destination state.

**CDS700-R006** An AI workflow MUST NOT write directly into a canonical field unless its autonomy level and the field's risk class explicitly permit that action.

*Informative note:* the AI system is one participant in the information lifecycle. The schema, dictionaries, rule engine and verification engine remain separate authorities.

## 4. Roles of AI in Commerce Information *(informative, except R007)*

| Role | Typical tasks | Default risk posture |
|---|---|---|
| Extractor | Identify material, colour, dimensions, features or model identifiers from eligible sources | Low to medium |
| Classifier | Suggest product family, type, category or taxonomy mapping | Medium |
| Normalizer | Map source wording to canonical dictionary values | Low to medium |
| Writer | Draft titles, descriptions, bullets, care text or summaries | Medium |
| Translator | Translate and localise governed content | Medium |
| Media analyst | Describe images, detect visible attributes, propose alt text or sequence | Medium |
| Channel assistant | Suggest channel categories, labels, titles or policy fixes | Medium to high |
| Quality analyst | Detect anomalies, missing values, conflicts and likely drift | Low to medium |
| Merchandising assistant | Suggest collections, facets, synonyms, related products or campaign groupings | Medium |
| Workflow coordinator | Route work, request evidence and invoke approved tools | Depends on permissions |

**CDS700-R007** *(normative)* An implementation MUST declare the role an AI workflow performs rather than describing all AI activity as a single generic enrichment step.

## 5. Autonomy Levels *(normative)*

| Level | Name | Permitted behaviour |
|---|---|---|
| A0 | Disabled | No AI processing for the task or field. |
| A1 | Assistive | AI proposes values or content; a human must accept each result. |
| A2 | Governed draft | AI may populate a non-canonical draft or review queue after validation. |
| A3 | Bounded acceptance | AI may accept eligible values into canonical state only under the bounded-A3 controls of R011. |
| A4 | Bounded execution | AI may trigger approved downstream actions for specified low-risk fields or workflows, subject to publication and verification controls (§30) and the enumeration rule R012. |

**CDS700-R008** An organisation MUST declare the autonomy level for each AI workflow.

**CDS700-R009** A4 MUST NOT be interpreted as unrestricted autonomy.

**CDS700-R010** High-risk fields — price, tax, regulated claims, hazardous-use instructions, legal warranties and safety information — MUST NOT use A3 or A4 without an explicit specialist-approved policy.

**CDS700-R011** **Bounded A3** is A3 operated under all four of the following controls. A workflow claiming A3 MUST implement all four; R2-risk tasks (Appendix B) MAY use A3 only in this bounded form:
1. a **per-field policy** declaring which fields and value classes are eligible for automatic acceptance;
2. a **calibrated confidence threshold** derived from representative reviewed examples for that task and field (§17);
3. **mandatory sampled human review** of accepted results at a declared sampling rate;
4. **automatic suspension** of automatic acceptance when the reviewer correction rate breaches a declared threshold.

**CDS700-R012** An A4 workflow MUST enumerate its permitted actions in its workflow definition; any action not enumerated is prohibited for that workflow.

*Informative note:* a single catalogue may use A3 for mapping supplier colour names while requiring A1 for compliance claims and A2 for marketing descriptions.

## 6. AI Work Objects and Review States *(normative)*

AI work is represented as durable objects, not transient chat responses. A work object records the task, source evidence, schema, output, validation, review and final disposition. The machine-readable contract for this record is the CDS-1100 ai-proposal schema; Appendix A lists the recommended semantic fields.

| Property | Purpose |
|---|---|
| work_id | Stable identifier for the AI task |
| product_id / variant_id | Target information record |
| task_type | Extraction, mapping, classification, writing, translation or analysis |
| workflow_version | Approved workflow or agent definition |
| model_id | Model and version used |
| input_evidence | References to eligible source material |
| output_schema | Expected structured result |
| proposal | Generated values or content |
| confidence | Field- or task-level confidence |
| validation_results | Dictionary, schema and business-rule outcomes |
| review_state | See R015 |
| reviewer | Human or policy that authorised acceptance |
| timestamps | Created, completed, reviewed and accepted times |
| cost_and_usage | Optional operational usage data |

**CDS700-R013** AI proposals MUST be stored separately from canonical values until accepted by the declared approval policy.

**CDS700-R014** Rejecting or superseding a proposal MUST NOT erase its audit record.

**CDS700-R015** The review state of an AI proposal MUST use the shared enum: `proposed`, `review_required`, `accepted`, `rejected`, `superseded`, `expired`. This enum is identical in CDS-700 and the CDS-1100 ai-proposal schema — they describe the same record. Execution failure (timeout, malformed output, tool error) is a work-object disposition (§28), not a review state.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D14 (resolved)): Adopted the merged enum proposed/review_required/accepted/rejected/superseded/expired ("accepted" replaces v0.1 "approved"; "expired" adopted from CDS-1100; "review_required" retained from CDS-700; v0.1 "failed" moved to work-object disposition). Alternative: keep two vocabularies with a mapping table — rejected because Matrix 2 shows they describe one record.

## 7. Source Evidence and Input Eligibility *(normative)*

AI quality is constrained by the information it receives. CDS distinguishes eligible evidence from contextual material that may inspire wording but cannot establish a product fact.

| Class | Eligibility criteria | Examples | Permitted use |
|---|---|---|---|
| E1 — Authoritative | Publisher is the manufacturer, the contracted supplier or the organisation itself, with an identifiable authority chain to the product (specification, signed record, approved internal measurement) | Manufacturer specification, signed supplier record, approved internal measurement | May establish canonical facts subject to validation |
| E2 — Strong secondary | Publisher identity is known and the content originates from a brand-controlled or certified source: an **official product page** (a page whose origin is controlled by the brand owner or authorised distributor), packaging produced by the brand, or a **certified feed** (a data feed whose certifier is named in the evidence record) | Official product page, packaging image, certified data feed | May support facts with provenance and review policy |
| E3 — Observational | Direct observation of the product or its current presentation; publisher authority not required, but the observation itself is verifiable | Product photographs, video, existing storefront copy | May support visible or descriptive attributes; ambiguity must remain explicit |
| E4 — Contextual | No qualifying publisher identity or authority chain | Competitor listings, general web content, related-product text | May inform terminology or review; must not establish unverified product facts |

**CDS700-R016** An evidence record MUST identify the publisher and the basis for its class assignment; evidence that cannot meet the E1–E3 criteria MUST be classed E4. For E2 "certified feed" evidence the certifier MUST be named.

**CDS700-R017** Every factual AI proposal MUST identify the evidence used or explicitly declare that no eligible evidence was available.

**CDS700-R018** AI MUST NOT convert absence of evidence into a positive product claim.

**CDS700-R019** Conflicting eligible sources MUST be surfaced as a conflict rather than silently resolved by model preference.

## 8. Schema-Constrained Generation *(normative)*

AI outputs are constrained by Attribute Definitions, controlled dictionaries, units, cardinality and conditional rules (CDS-200 §7, CDS-400). Free-form generation is reserved for content fields that are intentionally unstructured.

```
Task: Extract apparel attributes
Allowed output:
  MF_material: dictionary(materials), multi-value
  MF_pattern: dictionary(patterns), single-value
  MF_fit: dictionary(fits), single-value
  MF_sleeve_length: dictionary(sleeve_lengths), single-value
  AI_evidence: source references
  AI_confidence: 0.00-1.00
Not allowed:
  new dictionary values
  price claims
  sustainability claims without evidence
```

**CDS700-R020** An AI workflow MUST receive an explicit output schema.

**CDS700-R021** Out-of-schema fields MUST be rejected or quarantined.

**CDS700-R022** When an output requires a dictionary value, the AI MUST select from the allowed identifiers or return an unknown-value proposal (CDS-400 §17).

## 9. Extraction and Normalisation *(normative)*

Extraction identifies candidate facts from source material. Normalisation converts those candidates into canonical units, identifiers and dictionary values. The two stages remain distinguishable for audit and correction.

```
Observed source text: "80% cotton / 20% recycled poly"
Extracted components:
  cotton = 80 percent
  recycled polyester = 20 percent
Canonical composition:
  material.cotton = 80
  material.recycled_polyester = 20
Facet projection:
  Cotton
  Recycled material
```

**CDS700-R023** The original extracted text MUST be preserved when the normalised result may be disputed or reprocessed.

**CDS700-R024** Unit conversion and arithmetic SHOULD be performed by deterministic code after AI extraction, not by unchecked model calculation.

**CDS700-R025** A normalisation step MUST identify whether the result was exact, alias-based, transformed or inferred.

## 10. Classification and Taxonomy Assistance *(normative)*

AI may suggest internal categories, product types and external taxonomy mappings. Classification remains governed because it controls inherited attributes, collections, navigation and channel requirements (CDS-200 §6).

**CDS700-R026** AI classification MUST select from the current approved taxonomy identifiers.

**CDS700-R027** The classifier SHOULD return ranked candidates, confidence and the evidence that distinguished the selected category from nearby alternatives.

**CDS700-R028** A category suggestion MUST NOT automatically create a new category.

**CDS700-R029** External taxonomy suggestions MUST remain channel mappings and MUST NOT replace the internal classification.

*Informative note:* low-confidence classification routes to the taxonomy decision log rather than creating silent inconsistency.

## 11. Dictionary Mapping and Unknown Values *(normative)*

AI's role in mapping supplier values (colour names, materials, fits) to controlled dictionaries is to propose a mapping, not to hide ambiguity. Dictionary governance, aliases and unknown-value quarantine are defined in CDS-400.

| Outcome | Required behaviour |
|---|---|
| Exact canonical or alias match | Use deterministic mapping; AI is unnecessary |
| High-confidence contextual match | AI may propose an existing canonical value with evidence |
| Ambiguous match | Return ranked candidates and require review |
| No suitable value | Create an unknown-value record or dictionary-extension request |
| Potential synonym | Propose an alias; do not add it silently |

**CDS700-R030** AI MUST NOT create a canonical dictionary value merely to avoid returning unknown.

**CDS700-R031** A proposed alias MUST retain the source wording, language, supplier and approval status.

## 12. Product Content Generation *(normative)*

AI may draft titles, descriptions, feature bullets, care summaries and other commerce content. Generated content remains grounded in canonical facts and eligible evidence.

**CDS700-R032** Generated content MUST NOT introduce product capabilities, compatibility, certifications, scarcity, sustainability or performance claims that are absent from approved information.

**CDS700-R033** The workflow SHOULD distinguish factual fields, marketing interpretation and stylistic wording.

**CDS700-R034** A generated title MUST preserve the identifiers and distinguishing attributes required by the organisation's declared product-title policy (R035).

**CDS700-R035** An organisation using AI title generation MUST declare a **product-title policy**: a per-catalogue or per-category-profile statement of which identifiers (e.g. brand, model number) and which distinguishing attributes (e.g. colour, size, capacity) a title must preserve, and any ordering or length constraints. The policy is the testable reference for R034.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The product-title policy had no home chapter in v0.1 (referenced only here), so it is defined here as a declared-policy mechanism. Alternative: relocate to CDS-600 (customer experience) or CDS-200 (canonical model) if a later revision gives titles a fuller treatment.

**CDS700-R036** Generated content SHOULD cite or internally link the canonical fields used, so reviewers can trace each factual statement.

*Informative note:* a strong writing workflow generates from governed facts. It does not treat an old product description as unquestionable truth.

## 13. Translation and Localisation *(normative)*

Translation changes language. Localisation adapts terminology, units, spelling, regulatory wording and market conventions. These are modelled separately.

**CDS700-R037** The canonical source language and approved translation MUST remain linked by version.

**CDS700-R038** Dictionary values SHOULD use locale-specific display labels (CDS-400) rather than being translated independently in every product record.

**CDS700-R039** AI translation MUST preserve product identifiers, measurements, brand names and regulated wording according to field policy.

**CDS700-R040** A translation workflow MUST report omitted, ambiguous or culturally adapted content.

## 14. Image, Video and Document Analysis *(normative)*

AI may analyse product photographs, packaging, diagrams, manuals and video to propose attributes, alt text, media roles or quality findings.

**CDS700-R041** Visual analysis MUST distinguish visible observation from inferred product fact.

**CDS700-R042** AI-generated alt text SHOULD describe relevant visible content concisely and MUST NOT repeat unsupported marketing claims.

**CDS700-R043** Image-derived colour SHOULD be treated as observational (E3) evidence: lighting, editing, display profiles and material reflectance can all shift apparent colour.

**CDS700-R044** Sensitive or private information found in media MUST be handled under the organisation's security policy and MUST NOT be copied into product content by default.

## 15. Channel Optimisation and Mapping Assistance *(normative)*

Channel optimisation is a projection task; it must not alter canonical facts to satisfy one platform (CDS-P-03).

**CDS700-R045** AI channel optimisation MUST operate on expected channel state (CDS-500), not rewrite canonical information to match a channel limitation.

**CDS700-R046** Channel-specific generated text MUST be stored as a CH_ override or draft when it differs from canonical content (CDS-300).

**CDS700-R047** Policy-sensitive marketplace attributes MUST be validated against current channel rules before publication.

**CDS700-R048** An AI suggestion MUST NOT be treated as evidence that a channel will accept or display the value.

## 16. Search, Facet and Merchandising Assistance *(normative)*

AI may assist with synonyms, query interpretation, related-product suggestions, collection candidates and facet-gap analysis. These outputs influence customer discovery and therefore require measurement and governance; facet and search governance is defined in CDS-600.

**CDS700-R049** AI MAY propose search synonyms; dictionary and search owners MUST approve terms that materially broaden or redirect meaning.

**CDS700-R050** AI MUST NOT expose every generated concept as a customer facet.

**CDS700-R051** Merchandising suggestions MUST remain distinguishable from taxonomy classification.

**CDS700-R052** Personalised or generated collection membership SHOULD be explainable by declared signals and MUST respect availability and exclusion rules.

## 17. Confidence, Uncertainty and Abstention *(normative)*

Confidence is a decision aid, not proof. Model scores may be uncalibrated, task-specific or incomparable across versions. Confidence is interpreted together with evidence and validation:

| Signal | Meaning |
|---|---|
| Model confidence | The system's estimate for its own proposal |
| Evidence strength | Authority and directness of source material (§7) |
| Dictionary certainty | Exact, alias, contextual, ambiguous or unknown mapping |
| Validation outcome | Whether schema and business rules pass |
| Risk class | Consequence if the result is wrong (Appendix B) |
| Review requirement | Human, policy or no approval required |

**CDS700-R053** A confidence score MUST NOT be used as the sole acceptance criterion.

**CDS700-R054** The workflow MUST support an explicit abstain or insufficient-evidence outcome.

**CDS700-R055** Thresholds SHOULD be calibrated on representative reviewed examples for the specific task and field; for bounded A3 this calibration is mandatory (R011).

## 18. Evidence, Provenance and Explainability *(normative)*

Explainability in CDS is practical lineage, not a demand that a model reveal internal reasoning.

**CDS700-R056** An AI proposal MUST record the source references, model, workflow version, timestamp and validation results.

**CDS700-R057** Where feasible, extracted facts SHOULD include a source snippet, document region, image region or field reference.

**CDS700-R058** The implementation MUST NOT require or expose private model chain-of-thought as an audit mechanism.

**CDS700-R059** A human-readable decision summary SHOULD explain the evidence, mapping and policy outcome without revealing sensitive internal reasoning.

## 19. Human Review and Approval *(normative)*

Human review is a governed task, not a decorative approve button. Reviewers need the proposal, current value, evidence, validation results, impact and available actions in one place.

| Review action | Meaning |
|---|---|
| Accept | Write the proposal to the permitted target state |
| Edit and accept | Correct the proposal while preserving original AI output |
| Reject | Do not apply; record reason |
| Request evidence | Return to the workflow for additional eligible sources |
| Create dictionary request | Escalate an unknown or missing controlled value |
| Defer | Keep pending without acceptance |
| Bulk accept | Apply only when preview, scope and rollback are available |

**CDS700-R060** A reviewer MUST be able to see which fields will change before acceptance.

**CDS700-R061** Bulk approval MUST provide a summary of affected products, values, risks and validation exceptions.

**CDS700-R062** Human corrections SHOULD be captured as evaluation data, subject to privacy and governance policy.

## 20. Deterministic and Probabilistic Boundaries *(normative)*

A robust system combines AI with deterministic software. AI handles ambiguity and interpretation; deterministic components handle exact rules and repeatable transformations.

| Prefer deterministic logic | Prefer AI assistance |
|---|---|
| Arithmetic and tax calculation | Extracting a price from unstructured text |
| Unit conversion after unit identification | Identifying a unit in a diagram |
| Exact dictionary aliases | Suggesting a mapping for a new supplier term |
| Required-field validation | Inferring which attributes are described in prose |
| Identifier format validation | Classifying a product from mixed evidence |
| Known channel transformation | Drafting a channel-specific summary |

**CDS700-R063** An implementation SHOULD use deterministic logic whenever the same inputs should always produce one objectively correct result.

**CDS700-R064** For each task the workflow registry (§33) marks as deterministic-eligible, the registry entry MUST either name the deterministic implementation used or record why no reliable deterministic rule exists. *(This replaces the untestable v0.1 rule "AI MUST NOT be used to obscure a missing deterministic rule" with an auditable mechanism.)*

## 21. Validation and Guardrails *(normative)*

Guardrail layers: schema validation (types, cardinality, required fields, structure); dictionary validation (approved identifiers, aliases, unknown-value handling); business validation (conditional requirements, incompatibilities, range limits); evidence validation (eligible sources, conflicts); content validation (prohibited claims, duplicate wording, field length); channel validation (allowed values, required fields, destination limits); publication validation (authority, workflow state, expected-state generation).

**CDS700-R065** Guardrails MUST be evaluated after AI output and before canonical acceptance or publication.

**CDS700-R066** A failed guardrail MUST produce a specific reason code rather than a generic AI error.

**CDS700-R067** A model instruction alone MUST NOT be treated as a sufficient guardrail for critical rules that can be enforced deterministically.

## 22. AI Semantic Namespace *(normative)*

`AI_` is a registered core semantic namespace in the CDS-300 v0.2 namespace registry, reserved for AI work metadata and proposals. The prefix identifies the role of a field without changing the semantic identity of an accepted canonical value. Naming patterns are listed in Appendix C; the registry itself is owned by CDS-300.

**CDS700-R068** AI_ fields MUST represent proposals, provenance, confidence or workflow metadata; they MUST NOT replace the canonical field namespace.

**CDS700-R069** After acceptance, the value MUST be stored in its semantic canonical field (e.g. MF_material) while AI provenance remains linked in the audit record.

*Informative note:* MF_material means material. AI_material_suggestion means an AI proposal about material. The prefix communicates role immediately to humans, software and AI agents.

## 23. Prompt, Model and Configuration Versioning *(normative)*

AI behaviour can change when the model, system instruction, prompt template, tool set, retrieval source, dictionary or validation policy changes. Reproducibility depends on a versioned workflow, not the model name alone.

**CDS700-R070** Every production AI result MUST identify the model and workflow version used.

**CDS700-R071** Prompt templates, tool permissions, retrieval sources, output schemas and thresholds SHOULD be versioned together as one deployable configuration.

**CDS700-R072** A workflow change that may alter accepted outputs MUST pass evaluation (§24) before production rollout.

**CDS700-R073** Historical proposals MUST remain associated with the configuration that generated them.

## 24. Evaluation and Benchmark Sets *(normative)*

Evaluation uses representative, reviewed commerce examples, including ordinary products and difficult boundary cases.

| Metric | Example application |
|---|---|
| Precision | How often accepted material mappings are correct |
| Recall | How often available attributes are successfully found |
| Exact-match rate | Category or dictionary identifier selection |
| Schema-valid rate | Structured output validity |
| Unsupported-claim rate | Generated content grounding |
| Abstention quality | Whether uncertain cases are correctly deferred |
| Reviewer correction rate | Human effort required after generation |
| Downstream verification rate | Whether accepted AI output publishes faithfully |

**CDS700-R074** An AI workflow MUST be evaluated before bulk production use.

**CDS700-R075** The benchmark set SHOULD include diverse suppliers, categories, languages, missing data, conflicting evidence and unknown dictionary values.

**CDS700-R076** Evaluation results MUST be associated with the exact workflow version.

## 25. Drift, Regression and Change Detection *(normative)*

Model providers, prompts, dictionaries and product distributions change. A workflow that performed well previously may degrade without an obvious software error.

**CDS700-R077** Production workflows SHOULD be re-evaluated after material model, prompt, schema, dictionary or source changes.

**CDS700-R078** The implementation SHOULD monitor changes in acceptance rate, correction rate, unknown-value rate, content violations and downstream mismatch rate.

**CDS700-R079** A significant regression MUST be able to pause or roll back the affected workflow.

**CDS700-R080** Previously accepted canonical values MUST NOT be silently regenerated merely because a model version changed.

**CDS700-R081** Monitoring obligations MUST scale with the declared autonomy level of a workflow: segmented monitoring that distinguishes AI-originated from human-originated values MUST apply to A3 and A4 workflows, SHOULD apply to A2 workflows, and MAY be limited to volume and sampled quality checks for A1. Operational monitoring mechanics are defined in CDS-1400, which cites this rule for its AI segmentation requirement.

## 26. Security, Privacy and Data Handling *(normative)*

AI workflows may process supplier records, internal prices, unpublished products, contracts, customer material or credentials. The organisation controls what data leaves its boundary and which tools an agent may invoke.

**CDS700-R082** Each AI workflow definition MUST declare the data classes it may receive as input; supplying data outside the declared classes is non-conformant. Declared inputs SHOULD be the minimum necessary for the task.

**CDS700-R083** Secrets and credentials MUST NOT be included in model input. This prohibition admits no policy exception.

**CDS700-R084** Private customer data MUST NOT be included in model input unless a declared data-handling policy explicitly permits it and states the safeguards applied (such as minimisation, masking or pseudonymisation, retention limits and access controls).

**CDS700-R085** Tool permissions MUST be scoped to the workflow; read access MUST NOT imply write or publication access.

**CDS700-R086** Logs and evidence records MUST follow retention and access-control policy.

## 27. Rights, Claims and Restricted Content *(normative)*

Commerce content may include copyrighted supplier text, trademarks, certifications, environmental claims and regulated statements. AI does not remove the need to establish rights and factual authority.

**CDS700-R087** An AI workflow MUST NOT infer regulated or rights-bearing claims — such as certifications, origin claims, sustainability claims, medical claims or legal warranties — from style, context or similar products. *Informative note:* which claim categories are regulated, and how, is jurisdiction-dependent; the categories named here are examples, and organisations MUST rely on their declared claim policies for the binding list in each market.

**CDS700-R088** Generated content MUST NOT reproduce supplier or third-party content beyond the rights the organisation holds to use it.

**CDS700-R089** Generated content SHOULD avoid close stylistic imitation of identifiable third-party content even where reproduction rights are not directly at issue.

**CDS700-R090** Brand and trademark wording MUST follow approved source and brand policy.

**CDS700-R091** Restricted or regulated categories SHOULD use specialist review profiles and narrower autonomy levels.

## 28. Failure Modes and Recovery *(normative)*

| Failure | Required response |
|---|---|
| Malformed output | Reject and retry only under bounded policy |
| Unsupported dictionary value | Quarantine or dictionary review (CDS-400 §17) |
| Conflicting evidence | Human review; preserve both sources |
| Tool or retrieval failure | Mark incomplete; do not fabricate missing input |
| Model timeout or refusal | Record status and preserve work object |
| Hallucinated claim | Reject, record reason and include in evaluation set |
| Bulk anomaly | Pause batch and provide rollback or staged recovery |
| Publication mismatch | Use CDS-500 reconciliation; do not assume AI output was accepted |

**CDS700-R092** Retries MUST be bounded and MUST NOT conceal repeated failure.

**CDS700-R093** A fallback model or workflow MUST meet the same schema, evidence and evaluation requirements as the primary.

## 29. Agent and Workflow Orchestration *(normative)*

Agentic systems may coordinate extraction, validation, research, review routing and publication tools. An agent is not exempt from field authority, permissions or evidence rules.

```
Orchestrator
  |-- Evidence Reader (read only)
  |-- Attribute Extractor (proposal only)
  |-- Dictionary Mapper (proposal only)
  |-- Validator (deterministic)
  |-- Human Review Queue
  `-- Publisher (explicitly authorised, CDS-500 controlled)
```

**CDS700-R094** Each agent or tool MUST have a declared role and least-privilege permission set.

**CDS700-R095** The orchestrator MUST preserve task lineage across delegated steps.

**CDS700-R096** An agent MUST NOT grant itself broader authority based on its own confidence or task interpretation.

**CDS700-R097** A human-readable workflow name and state SHOULD be visible to operators.

## 30. Publication Boundaries *(normative)*

AI acceptance and channel publication are separate events. A value may be approved as canonical yet still fail channel mapping, preflight validation or downstream publication.

**CDS700-R098** AI workflows MUST NOT bypass CDS-500 expected channel state and publication preflight.

**CDS700-R099** AI-generated channel overrides MUST be visibly channel-specific and independently reviewable.

**CDS700-R100** Direct AI publication MAY be used only under A4 for an explicitly approved, low-risk workflow with rollback and downstream verification.

**CDS700-R101** Price, inventory, legal status and safety-critical changes SHOULD remain outside direct AI publication unless governed by a specialist standard and deterministic controls.

## 31. Verification and Reconciliation *(normative)*

AI output is verified at two boundaries: against the canonical schema and evidence at acceptance, and against the observed downstream state after publication (CDS-500).

```
AI proposal
  -> Canonical validation and approval
  -> Expected channel representation
  -> Publication
  -> Channel observation
  -> Semantic comparison
  -> Health and reconciliation
```

**CDS700-R102** An accepted AI value MUST be included in ordinary CDS-500 field-level verification when published.

**CDS700-R103** Before a downstream mismatch involving AI-originated content is dispositioned as an AI-content defect, its triage record MUST evidence that mapping, transformation and channel behaviour were checked and excluded.

**CDS700-R104** AI MAY assist with anomaly triage; repair actions remain governed by field ownership and CDS-500 policy.

## 32. Audit, Observability and Cost *(normative)*

Recommended operational telemetry: work volume and completion status; acceptance, rejection and correction rates; unknown and abstention rates; validation and guardrail failures by reason code; model, workflow and dictionary versions; latency, token or compute usage and cost; human review time; downstream publication and verification outcomes.

**CDS700-R105** An implementation MUST retain sufficient audit data to reconstruct how an AI proposal reached canonical or published state.

**CDS700-R106** Operational metrics SHOULD distinguish quality, throughput, cost and human effort.

**CDS700-R107** A cost-optimisation change MUST NOT alter a workflow's declared evidence-class requirements, validation configuration or required review rate except through the workflow change process (§23, §33). *(This replaces the untestable v0.1 rule "cost optimisation MUST NOT silently reduce quality" with a reviewable mechanism.)*

## 33. Governance, Ownership and the Workflow Registry *(normative)*

AI governance belongs inside normal data governance (CDS-800), not in a separate experimental layer. Attribute owners, dictionary owners, channel owners and risk owners remain accountable for their domains. This section is the single home for AI governance rules; CDS-800 cites it.

**CDS700-R108** Every production AI workflow MUST have an accountable owner, a declared autonomy level, a risk class, evaluation evidence and approved destination permissions.

**CDS700-R109** Organisations operating production AI workflows MUST maintain a registry of approved workflows recording, per workflow: owner, role (§4), autonomy level, risk class, permitted fields and destinations, input data classes (R082), deterministic-eligibility disposition (R064) and current version. The registry is the mechanism behind R004's visibility requirement.

**CDS700-R110** Workflow changes MUST follow versioning, evaluation, approval and rollback policy (§23–§25); model or prompt changes that can alter output semantics MUST pass change and regression controls before rollout.

**CDS700-R111** AI-generated canonical changes MUST retain provenance and applicable human-review evidence (§18–§19).

**CDS700-R112** Deprecated workflows MUST be disabled for new work while historical audit records remain readable.

*Informative note:* AI exceptions and waivers follow the CDS-800 exception process (expiry and review included); conformance levels, the AI-Assured overlay profile and the T-AI test suite are defined in CDS-1000, which traces its tests to the CDS700-Rmmm identifiers in this chapter.

## 34. Worked Examples *(informative)*

### 34.1 Apparel colour mapping

```
Source evidence: supplier value "French Navy" (E1 supplier record)
Task: dictionary mapping
AI proposal: canonical colour = navy
Dictionary status: existing canonical value
Facet projection: blue
Autonomy: A3 (bounded, R011 controls active) for approved supplier
Validation: pass
Canonical write: MF_colour = navy
Provenance retained: AI work object + source value
Publication: channel displays "French Navy", filter "Blue"
Verification: observed values match expected
```

### 34.2 Unknown homewares finish

```
Source evidence: "smoked eucalypt finish"
AI proposal candidates: smoked_wood (0.54), dark_wood (0.49)
Dictionary status: no exact or approved alias
Outcome: ABSTAIN
Action: create dictionary review request
Canonical value: unchanged
Customer facet: not published until approved
```

### 34.3 Product description generation

```
Inputs: canonical title, material, dimensions, care, included items;
        approved brand voice; prohibited-claim rules
AI output: draft short description and bullets
Validation: no unsupported claims; measurements match canonical fields
Autonomy: A2 governed draft
Human action: edit and accept
Publication: ordinary channel workflow
```

### 34.4 Channel category assistance

```
Internal category: Homewares > Living Room > Cushions
AI suggestion: candidate mappings for two external channel taxonomies
Result: channel mapping proposals only; no change to internal category
Review: channel specialist approves mappings
Publication: expected channel state generated and verified
```

---

## Appendix A — Recommended AI Work Object Fields *(informative)*

The normative machine-readable contract is the CDS-1100 ai-proposal schema. Recommended semantic fields:

```
AI_work_id, AI_task_type,
SYS_product_id, SYS_variant_id,
AI_workflow_version, AI_model_id,
AI_input_evidence[], AI_output_schema_version,
AI_proposal{}, AI_confidence{},
AI_validation_results[],
AI_review_status, AI_reviewed_by, AI_reviewed_at,
AI_disposition_reason, AI_generated_at,
SYS_created_at, SYS_updated_at
```

The exact storage model may differ; the semantic information and lineage remain available.

## Appendix B — Risk and Review Matrix *(informative)*

Category examples in this matrix are informative; the binding list of regulated categories is jurisdiction-dependent (R087).

| Risk class | Examples | Maximum default autonomy | Review expectation |
|---|---|---|---|
| R1 — Low | Aliases, internal suggestions, alt-text drafts, anomaly flags | A3 | Sampled or exception review |
| R2 — Moderate | Material mapping, classification, search synonyms, ordinary content | A2, or A3 only in bounded form (R011) | Human review or calibrated policy with sampling |
| R3 — High | Compatibility, origin, sustainability claims, channel policy attributes | A1 or A2 | Qualified human approval |
| R4 — Critical | Price, tax, safety, regulated claims, hazardous-use instructions, legal warranty | A1 | Specialist approval; deterministic controls required |

## Appendix C — Recommended AI Field Naming *(informative)*

The AI_ namespace registration lives in the CDS-300 registry; these patterns illustrate its use.

| Pattern | Example | Meaning |
|---|---|---|
| AI_<field>_suggestion | AI_material_suggestion | Proposed value for a governed field |
| AI_<field>_confidence | AI_material_confidence | Task-specific confidence |
| AI_<field>_evidence | AI_material_evidence | Evidence references |
| AI_<task>_status | AI_classification_status | Workflow state |
| AI_model_id | AI_model_id | Model/version identifier |
| AI_workflow_version | AI_workflow_version | Versioned instruction, tools and policy |
| AI_reviewed_by | AI_reviewed_by | Human or policy that authorised disposition |

Human-facing identifiers SHOULD remain descriptive even when the underlying implementation uses structured work-object properties.

## Appendix D — Platform Profiles *(informative)*

Platform-specific guidance for AI-assisted publication (including the Shopify profile that appeared as v0.1 Appendix D) lives in CDS-900. The invariants are platform-independent: AI suggestions are created and reviewed in the PIM; accepted values publish through ordinary channel mappings; channel-only AI text uses CH_ overrides; read-back verifies AI-originated values exactly as human-originated ones; manual downstream edits to PIM-owned fields are drift unless an authorised override exists.

## Appendix E — Operational Review Checklist *(informative)*

- Is the task role and autonomy level declared?
- Are the source materials eligible and referenced, with evidence classes assigned?
- Is the output schema explicit?
- Are dictionary values and unknown handling defined?
- Are deterministic validations applied, and deterministic-eligibility recorded in the registry?
- Can the workflow abstain?
- Is risk-appropriate review configured (including bounded-A3 controls where claimed)?
- Are model and workflow versions recorded?
- Can the change be previewed and rolled back?
- Will accepted values pass through normal publication and read-back verification?
- Are quality, correction rate and downstream mismatch monitored at the level the autonomy class requires?
- Can a new operator understand the AI fields and statuses without separate notes?


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-800 — Governance, Ownership and Change Control

> RESOLVED (was new (resolved), owner decision 2026-08-04): retitle accepted — "Governance, Ownership and Change Control". File renamed to match.

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-800 Working Draft v0.1, including its §9 conformance ladder (superseded by CDS-1000 per ADR-D1) and its exception/waiver dual vocabulary (superseded by the single Exception definition in CDS-100 §4) |
| Normative status | §1, §3–§8, §9–§30 are normative except where marked. §2 (principles), §31 (scenarios), Annexes A–C, E (templates/checklists) and Annex F (organisation example) are informative. Annex D is a normative pointer. |
| Findings addressed | 800-1 (via ADR-D1), 800-2, 800-3, 800-5, 800-6, 800-7, 800-8, 800-9, 800-10; SYS-1 (CLEANUP-PASS §C: all 86 prefix-labelled rules corrected, including the one ambiguous case), SYS-2 (requirement IDs), SYS-4 (non-testable MUSTs); ADR-D1, ADR-D24; REVIEW-003 Matrix 5 dedup |

---

## 1. Purpose and Scope *(normative)*

CDS-800 defines how a CDS implementation is governed over time: authority, ownership, decision rights, change control, quality oversight, audit evidence, security responsibility and the governance of conformance claims. Conformance **levels, tests and claim schemas** are owned by CDS-1000; this chapter governs who may claim, how claims stay honest, and how the organisation operates the standard day to day.

A technically capable PIM still fails if nobody owns the taxonomy, uncontrolled dictionary values are accepted, channel mappings change without review, or editors work around the master data layer. Governance exists to keep those failures from becoming normal operating practice.

**CDS800-R001** Every CDS implementation MUST define accountable ownership for the canonical product model, each governed data domain and each publication channel.

*Informative note:* Governance does not require a large committee. A small organisation may assign several roles to one person (see §18 and ADR-800-008), but responsibilities and decision rights remain explicit. Governance is judged by operating behaviour and its evidence trail (§16), not by the existence of a policy document.

## 2. Governance Principles *(informative)*

- **Accountability precedes automation.** A system may automate work only after authority, ownership and exception handling are defined.
- **One owner, many contributors.** Many people and systems may contribute to a field; one authority resolves conflict (CDS-200 §13).
- **Enter data where it originates.** Information is captured and corrected in its system of authority, not patched downstream. Downstream edits to upstream-owned facts are drift, not maintenance (CDS-500 §11).
- **The standard is stable; implementations evolve.** Local tools and schemas change without weakening CDS principles (CDS-P-12, Governance Over Convenience).
- **Change is deliberate.** New fields, values, namespaces and mappings follow a visible proposal and review path.
- **Exceptions are explicit.** A deviation is recorded, time-bounded and reviewed — never an undocumented permanent rule.
- **Evidence survives decisions.** Approvals, migrations, mappings and verification results remain auditable.
- **Quality is measured.** Completeness, validity, consistency, mapping coverage and channel fidelity are observable (CDS-1400).
- **Access follows responsibility.** Users receive the minimum permission needed for their role.
- **Customer impact matters.** Governance decisions consider storefront discovery, accessibility, truthfulness and usability.
- **Conformance is testable.** Requirements are capable of objective assessment wherever practical (CDS-1000).

## 3. Governance Operating Model *(normative)*

```
CDS Standard and Profiles
        -> Organisation Policies and Ownership
        -> Schemas + Taxonomies + Dictionaries + Rules
        -> Product Data Operations and Publication
        -> Verification + Metrics + Audit Evidence
        -> Review, Change and Continuous Improvement
```

**CDS800-R002** The governance model MUST cover definition, operation, monitoring and change, and MUST NOT stop after initial PIM configuration.

**CDS800-R003** An organisation SHOULD maintain one identifiable forum or accountable role capable of resolving cross-domain conflicts.

*Informative note:* The forum may be called a Data Council, Product Information Council, PIM Steering Group or any locally meaningful name. CDS governs function, not branding.

## 4. Decision Rights and Authority *(normative)*

| Decision | Required authority | Typical consultation |
|---|---|---|
| Create or retire a product family | PIM Product Owner | Schema, taxonomy, channel and operations owners |
| Add or rename a category | Taxonomy Owner | Merchandising, SEO, channel and analytics owners |
| Add a canonical dictionary value | Dictionary Owner | Merchandising and channel owners |
| Change a facet grouping | Facet and Search Owner | Dictionary, search and merchandising owners |
| Add or change a canonical attribute | Schema Owner | Domain steward, integration and channel owners |
| Introduce a semantic namespace | CDS Governance Owner | Architecture, integration and operations owners |
| Change a channel mapping | Channel Owner | Schema, dictionary and verification owners |
| Approve an AI workflow for canonical writes | AI Governance Owner and Product Data Owner | Security, product and operations owners |
| Declare CDS conformance | Conformance Declaration Executive | CDS Governance Owner and assurance functions |

**CDS800-R004** A decision right MUST identify who may approve, who must be consulted and who must be informed.

**CDS800-R005** The person requesting a material change SHOULD NOT be the only person approving it when the change can affect many products or channels.

**CDS800-R006** The organisation MUST declare, in its implementation statement (§9), the thresholds that make a change *material* (for example: product count affected, number of channels affected, breaking-change class per §11).

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): R006 converts the otherwise untestable "material change" qualifier (SYS-4) into a declared-threshold mechanism. Alternative: fix corpus-wide thresholds in CDS-1000 test conditions.

## 5. Roles and Responsibilities *(normative)*

This table is the **role register** for the CDS corpus. Other chapters and local artefacts use these role names; local titles MAY differ where the mapping is documented (§9).

| Role | Accountability |
|---|---|
| CDS Governance Owner | Local interpretation of CDS, policy hierarchy, namespace introduction and unresolved cross-domain decisions. |
| Conformance Declaration Executive | The executive or accountable system owner who approves and signs conformance declarations (§29). |
| PIM Product Owner | System capability, roadmap, operational fitness and the master product layer. |
| Product Data Owner | A business data domain and its fitness for use. |
| Data Steward | Definitions, values, quality, issue resolution and daily governance within a domain (may specialise: Taxonomy Steward, Dictionary Steward). |
| Schema Owner | Product families, attribute definitions, requiredness and validation rules. |
| Taxonomy Owner | Internal category structure, boundaries, mappings and decision log. |
| Dictionary Owner | Canonical values, aliases, facets, channel representations and value lifecycle. |
| Facet and Search Owner | Customer-facing filter behaviour, search synonyms, ranking and usability outcomes. |
| Channel Owner | Destination capability, mappings, policy requirements, publication behaviour and channel health. |
| Integration Owner | Connector behaviour, transformations, retries, technical monitoring and data lineage. |
| AI Governance Owner | AI use-case approval, risk classification, evaluation, evidence and human-review policy (controls: CDS-700). |
| Security and Compliance Owner | Access, data handling, regulated claims, retention and incident obligations. |
| Auditor / Assurance Reviewer | Independent assessment of conformance, evidence and control operation. |

**CDS800-R007** One person MAY hold multiple roles, but each responsibility MUST remain explicitly assigned.

**CDS800-R008** Role assignment MUST be reviewed when personnel, systems or operating models change.

## 6. Domain Ownership Contracts *(normative)*

A domain ownership contract states what a domain owns, consumes, enforces and commits to downstream.

```
Domain: colour
Owner: Dictionary Owner
Canonical facts: canonical shade, colour family, aliases
Consumes: supplier colour text, image evidence
Publishes: display label, search terms, channel colour values
Controls: allowed values, mappings, deprecation, facet membership
Quality measures: unmapped rate, ambiguous rate, channel mismatch rate
```

**CDS800-R009** Each governed domain SHOULD have a concise ownership contract accessible to operators and automated agents.

**CDS800-R010** A domain contract MUST distinguish canonical facts from derived display, facet and channel representations.

## 7. Policy and Document Hierarchy *(normative)*

| Level | Artefact | Function |
|---|---|---|
| 1 | CDS specification | Vendor-neutral normative requirements and terminology |
| 2 | CDS profile | Industry, platform or overlay implementation constraints |
| 3 | Organisation policy | Local authority, risk, approval and operating rules |
| 4 | Data model and registries | Schemas, taxonomies, dictionaries, mappings and namespaces |
| 5 | Procedures and runbooks | How operators execute, verify and recover work |
| 6 | Records and evidence | Approvals, releases, exceptions, audits and verification results |

**CDS800-R011** Lower-level artefacts MUST NOT silently contradict higher-level normative requirements.

**CDS800-R012** Where an implementation cannot satisfy a requirement, the deviation MUST be represented through the exception process (§14) rather than hidden in procedure.

## 8. Conformance Levels and Profiles *(normative)*

The single CDS conformance ladder is defined in CDS-1000: **Foundation → Structured → Publisher → Verified → Governed**, strictly cumulative, with **overlay profiles** (for example AI-Assured, CX, multi-tenant) claimable alongside a level. Level definitions, test suites, evidence packages and claim schemas are owned by CDS-1000 and are not restated here.

*Supersession note (ADR-D1):* the v0.1 CDS-800 §9 ladder (Foundation → Governed → Publisher → Verified → AI-Assured) is withdrawn. "CDS Governed" now names only the capstone level of the CDS-1000 ladder; "AI-Assured" is an overlay profile, not a level.

**CDS800-R013** A profile MUST identify the CDS release it depends on.

**CDS800-R014** A profile MAY add required attributes, dictionaries, rules or mappings, but MUST NOT weaken any base CDS requirement or the cumulativity of the conformance levels. *(The v0.1 exception-based escape clause is deleted — finding 800-2. Implementation-level deviations use the exception process (§14); a profile itself is never a vehicle for weakening.)*

**CDS800-R015** Organisation-specific extensions MUST use governed identifiers registered per CDS-300 and MUST NOT collide with reserved CDS namespaces.

*Informative note:* Profiles make the standard practical without turning platform-specific behaviour into universal product truth.

## 9. Organisation-Specific Implementation Statement *(normative)*

Local choices — role-name mappings, approval and materiality thresholds (R006), product families, custom attributes and dictionaries, channel enablement, risk classes and human-review thresholds, quality targets, retention and access controls, approved extension namespaces — are recorded in one controlled place.

**CDS800-R016** Local implementation choices MUST be documented in an implementation statement or equivalent controlled record.

**CDS800-R017** Local naming MAY differ from CDS examples, provided semantic intent and the mapping to CDS terms remain unambiguous.

## 10. Change Proposal Lifecycle *(normative)*

```
Propose -> Triage -> Impact Analysis -> Consult Owners
  -> Approve / Reject / Return -> Implement in Test
  -> Validate and Migrate -> Release -> Observe and Review
```

| Required proposal field | Purpose |
|---|---|
| Change identifier | Stable reference for discussion and audit |
| Problem statement | Explains the need, not only the desired solution |
| Affected domains | Schemas, products, dictionaries, channels and users |
| Proposed change | The exact model or rule alteration |
| Compatibility impact | Breaking and non-breaking effects (§11) |
| Migration plan | Data, connector and channel transition |
| Validation plan | How correctness will be tested |
| Owner and approver | Accountability |
| Target release | Connection to deployment control (§28) |
| Rollback or recovery | Response to adverse outcomes |

**CDS800-R018** Material changes (per the declared thresholds, R006) MUST be represented by a durable change proposal before production implementation.

**CDS800-R019** Emergency changes MAY use an accelerated path, but MUST be documented and reviewed retrospectively.

## 11. Versioning and Release Policy for Governed Artefacts *(normative)*

Corpus and document versioning is defined in CDS-000 §4 (ADR-D5). This section governs **local** artefacts: schemas, dictionaries, taxonomies, mappings and profiles. Semantic-versioning principles apply, adapted to the impact on consuming systems and stored data.

| Change class | Typical examples | Version effect |
|---|---|---|
| Major / breaking | Remove a field, change meaning, replace identifiers, incompatible cardinality | Major version |
| Minor / compatible | Add optional field, add dictionary value, add supported mapping | Minor version |
| Patch / corrective | Correct documentation, label or non-semantic metadata | Patch version |

**CDS800-R020** Version identifiers MUST change when a governed artefact changes semantically.

**CDS800-R021** A release record MUST identify included changes, migrations, tests, approvals and effective date.

## 12. Compatibility and Migration *(normative)*

Migration execution (baselines, cutover, rollback mechanics) is defined in CDS-1300; this section governs the change-control obligations.

**CDS800-R022** A breaking change MUST include a migration plan and a defined compatibility period, unless immediate removal is required for safety, law or severe data-integrity risk.

**CDS800-R023** Migration tooling SHOULD provide a preview of affected products and values before bulk changes are applied.

**CDS800-R024** Channel mappings and verification logic MUST be reviewed when canonical identifiers or value semantics change.

*Informative note:* Renaming a display label may be a patch. Replacing a stable canonical identifier is a breaking change.

## 13. Deprecation, Aliases and Removal *(normative)*

```
Active
  -> Deprecated (replacement announced)
  -> Migration in progress
  -> Read-only alias / compatibility period
  -> Removed from new use
  -> Retired after evidence confirms no active dependency
```

**CDS800-R025** Deprecated fields and values MUST identify a replacement or explicitly state that no replacement exists.

**CDS800-R026** Aliases MAY support ingestion and migration, but MUST resolve to one canonical identity.

**CDS800-R027** A deprecated identifier MUST NOT be reused for a different meaning.

**CDS800-R028** Removal MUST be blocked while verified active dependencies remain, unless a documented risk decision authorises otherwise.

## 14. Exceptions *(normative)*

An **Exception** is defined once, in CDS-100 §4: a time-limited, documented, approved deviation from a requirement, with an expiry and a named owner. An exception acknowledges non-conformance; it does not convert failure into conformance. The v0.1 "waiver" noun is retired (CDS-100 §8, finding 800-3); the field-level verification status `WAIVED` remains and is defined in CDS-500.

| Required field | Description |
|---|---|
| Identifier | Stable exception reference |
| Requirement | The CDS or local control being deviated from (requirement ID where applicable) |
| Scope | Products, fields, channels, teams or dates affected |
| Reason | Why conformance is not currently practical |
| Risk | Customer, operational, legal, security and data-quality effects |
| Compensating control | What reduces the risk during the exception |
| Owner and approver | Who accepts accountability |
| Expiry or review date | Prevents permanent undocumented drift |
| Resolution plan | How the organisation returns to conformance |
| Retest result | Evidence at closure that conformance was re-established |

**CDS800-R029** Every exception MUST have an owner, scope, rationale, compensating-control assessment and a review or expiry date.

**CDS800-R030** Expired exceptions MUST NOT remain silently active.

**CDS800-R031** Exception closure MUST record a retest result demonstrating that conformance was re-established, or a new approved exception continuing the deviation. *(New in v0.2 — finding 800-6.)*

## 15. Data Quality Governance *(normative)*

Data quality is assessed against fitness for use, not merely field population. The quality dimensions below are the governance vocabulary; canonical metric formulas, denominators and monitoring live in CDS-1400 (which owns Channel Health and the no-100%-for-unobserved-fields rule).

| Dimension | Meaning *(informative)* |
|---|---|
| Completeness | Required information is present |
| Validity | Values conform to definitions, types, units and rules |
| Consistency | Equivalent facts agree across products and representations |
| Uniqueness | Identifiers and records do not create unintended duplicates |
| Timeliness | Information is updated within an appropriate operating window |
| Provenance | Source and decision history are known |
| Mapping coverage | Canonical values have required facet and channel mappings |
| Publication fidelity | Observed channel state matches expected state (CDS-500) |
| Usability | Customer-facing values support clear discovery and decisions |

**CDS800-R032** Quality rules MUST identify the applicable scope, severity, owner and remediation path.

**CDS800-R033** A product SHOULD NOT be published while blocking quality rules fail.

**CDS800-R034** Each governance metric (for example exception age, change failure rate) MUST be defined with an explicit formula and denominator such that repeated calculation produces comparable results.

**CDS800-R035** Quality targets SHOULD be set by risk and business use rather than one universal threshold.

*Informative note:* A 100% score can still mislead if the wrong fields are required. Governance reviews the model as well as the metric.

## 16. Audit Evidence and Traceability *(normative)*

Evidence classes retained: current and historical schema definitions; category, dictionary, mapping and namespace versions; change requests and approvals; publication and observation records; verification outcomes and channel-health calculations; exceptions; AI evidence and workflow versions where applicable; access changes and privileged actions; migration results and rollback evidence; conformance assessments and declared scope.

**CDS800-R036** Audit evidence MUST be sufficient to reconstruct who changed what, when, under which authority and with what downstream effect.

**CDS800-R037** Retention periods MUST be declared per record class in the implementation statement and reflect legal, operational and assurance needs.

## 17. Security and Access Governance *(normative)*

**CDS800-R038** Access MUST follow least privilege and be granted according to role responsibilities.

**CDS800-R039** Privileged actions such as schema change, bulk publication, mapping replacement and canonical-value deletion SHOULD require stronger authentication and enhanced audit logging.

**CDS800-R040** Supplier credentials, channel tokens and other secrets MUST NOT be exposed through human-readable product fields or AI model inputs. *(Absolute — aligned with the CDS-700 §26 credential rule, finding 700-3; the v0.1 "approved need" escape applied only to non-secret confidential source data, which remains policy-gated under CDS-700.)*

**CDS800-R041** Production and test environments SHOULD be separated.

## 18. Segregation of Duties *(normative)*

| Activity | Recommended separation *(informative)* |
|---|---|
| Create schema change | Requester separate from final approver for material changes |
| Create channel credentials | Credential administrator separate from ordinary product editors |
| Bulk publish | Operator separate from policy owner for high-impact releases |
| Approve high-risk AI canonical writes | Reviewer separate from workflow developer (CDS-700) |
| Declare conformance | Conformance Declaration Executive supported by independent assessment |
| Close serious incident | Incident owner supported by verification or assurance review |

**CDS800-R042** Material high-risk changes SHOULD involve at least two distinct accountable participants.

*Informative note (small teams — ADR-800-008):* Where full organisational separation is impractical, small teams MAY substitute system controls, delayed approval, peer review or periodic independent review. The CDS-1300/CDS-1400 small-team profile cross-references this accommodation; roles are hats, responsibilities are not erased.

## 19. Multi-Tenant and Organisation Isolation *(normative)*

**CDS800-R043** Organisation-specific products, dictionaries, mappings, credentials, exceptions and audit records MUST be isolated from other organisations.

**CDS800-R044** A shared CDS baseline MAY provide definitions and templates, but MUST NOT expose or merge tenant-specific values without explicit authorisation.

**CDS800-R045** Imports and bulk actions MUST execute within a declared organisation context.

**CDS800-R046** Cross-tenant administrative access MUST be privileged, logged and reviewed.

*Test-coverage note (finding 800-7):* conformance tests for R043–R046 are bound to the **multi-tenant overlay profile** defined in CDS-1000; single-tenant implementations declare the profile not applicable.

## 20. Supplier and Import Governance *(normative)*

**CDS800-R047** Every supplier source MUST have an identified owner, acquisition method, field mapping, refresh policy and trust classification.

**CDS800-R048** Raw source values SHOULD be preserved separately from resolved canonical values (value model: CDS-400).

**CDS800-R049** Bulk imports MUST provide validation results and a preview of high-impact changes before commit.

Unknown-value quarantine and the prohibition on imports silently creating canonical values are defined in CDS-400 §17 and are not restated here.

## 21. Taxonomy Governance *(normative)*

Governed content per taxonomy: category name, definition and inclusion boundary; parent-child relationships and depth; primary-category assignment rules; tie-breaking decision log; inherited family or attribute rules; external taxonomy mappings; collection and navigation projections.

**CDS800-R050** Every category MUST have a recorded scope definition that distinguishes what belongs from what does not.

**CDS800-R051** A taxonomy change MUST analyse product reassignment, collection, navigation, facet, SEO and channel impacts before approval.

**CDS800-R052** Ambiguous product-type decisions SHOULD be recorded in a taxonomy decision log.

## 22. Dictionary and Reference-Data Governance *(normative)*

The value model — stable canonical identifiers, alias resolution, promotion of source values, quarantine — is owned by CDS-400. This section governs the change-control obligations around it.

**CDS800-R053** New canonical values MUST be checked for existing synonyms, aliases and facet membership before approval.

**CDS800-R054** Facet-grouping changes MUST consider customer usability, product counts, search behaviour and channel effects (facet requirements: CDS-600).

**CDS800-R055** Dictionary owners MUST monitor unknown, ambiguous and unmapped value rates.

**CDS800-R056** Channel representations MUST be reviewed when destination vocabularies change.

## 23. Attribute and Schema Governance *(normative)*

| Change question *(informative)* | Required consideration |
|---|---|
| Does the attribute describe a stable product fact? | If not, it may belong to workflow, channel or merchandising state |
| Is an existing attribute semantically equivalent? | Avoid duplicates and near-duplicates |
| What is the scope and cardinality? | Product, variant, category or channel; single or multi-value |
| Is a dictionary required? | Prefer controlled values for filterable and mapped information |
| Who owns the value? | Assign authority and stewardship |
| How is it validated? | Type, range, unit, dependency and source evidence |
| How is it displayed and filtered? | Separate canonical, display and facet behaviour |
| How is it published and verified? | Define channel mappings and comparison strategy |

**CDS800-R057** A new attribute MUST have an Attribute Definition (CDS-200 §7) before product values are created at scale.

**CDS800-R058** Attribute removal or semantic change MUST follow the compatibility and migration controls of §12.

## 24. Namespace Governance *(normative)*

The single normative prefix registry, the naming tests and the reserved-prefix rules are owned by CDS-300.

**CDS800-R059** Introduction, deprecation or retirement of a semantic namespace MUST follow the change proposal lifecycle (§10) and be recorded in the CDS-300 registry.

**CDS800-R060** Legacy prefix aliases MAY remain during migration, but new fields SHOULD use the current approved namespace.

The DF_ → CH_ transition is recorded once, in ADR-D24 (see CDS-300); it is not restated here.

## 25. Channel Governance *(normative)*

| Channel governance object | Minimum content |
|---|---|
| Capability profile | Supported fields, limits, types, observability, update semantics (content: CDS-900) |
| Mapping registry | Canonical source, transformation, destination and version |
| Ownership contract | Channel owner, integration owner and escalation path |
| Publication policy | Eligibility, scheduling, retry and approval rules (CDS-500) |
| Verification policy | Read-back coverage, comparison and health thresholds (CDS-500) |
| Override policy | Allowed local differences and expiry/review rules (CDS-500 §22) |
| Change watch | How platform schema and policy changes are detected and assessed |

**CDS800-R061** Each active channel MUST have an owner and a maintained capability profile.

**CDS800-R062** Channel changes MUST be assessed against mappings, publication, observation and verification before production rollout.

## 26. AI Governance *(normative)*

All AI controls — autonomy levels, risk classes, evidence, evaluation, provenance, human review, exception handling for AI outcomes — are owned by CDS-700 and are not restated here *(finding 800-8; the v0.1 §29 duplicates are deleted)*. This chapter contributes only the role-assignment rule:

**CDS800-R063** Every production AI workflow MUST have a named owner recorded in the workflow registry (CDS-700).

## 27. Incident, Drift and Recovery Governance *(normative)*

Incident management process, severity model and monitoring are owned by CDS-1400; drift classification and repair by CDS-500. This section governs the accountability obligations.

| Incident class *(informative)* | Expected response |
|---|---|
| Data integrity (wrong canonical values, duplicate identities) | Contain, assess scope, correct and verify |
| Publication (incorrect bulk update, partial channel writes) | Pause, reconcile, retry or roll back |
| Drift (downstream edits, platform transformations) | Classify ownership, restore or approve override (CDS-500) |
| Security (credential exposure, cross-tenant leakage) | Revoke, contain, investigate, notify as required |
| AI quality (systematic hallucination, regression) | Disable workflow, review accepted outputs (CDS-700) |
| Governance (expired exception, bypassed approval) | Record non-conformance, restore control, review cause |

**CDS800-R064** A material incident MUST have an owner, severity, affected scope, containment action and closure evidence.

**CDS800-R065** Incident closure MUST include verification that canonical and downstream states are correct.

**CDS800-R066** Repeated incidents SHOULD trigger root-cause review of schema, process, tooling or authority design.

## 28. Release and Deployment Governance *(normative)*

```
Approved Change Set -> Build / Configuration -> Test Data Validation
  -> Migration Preview -> Approval Gate -> Production Release
  -> Publication Observation -> Verification and Health Review
  -> Close or Roll Back
```

**CDS800-R067** A production release MUST identify the included change records and the versions of affected governed artefacts.

**CDS800-R068** High-impact releases SHOULD use staged rollout, limited product cohorts or channel canaries.

**CDS800-R069** A release MUST NOT be considered complete until required verification and health checks pass.

## 29. Conformance Claims Governance *(normative)*

Level definitions, test suites, evidence packages and the claim/manifest schema are owned by CDS-1000 (claim schema: CDS-1000 §23). This section governs claim integrity and authority.

**CDS800-R070** A conformance claim MUST describe the implemented scope and level honestly; an organisation MUST NOT claim conformance to capabilities it has not implemented.

**CDS800-R071** An implementation MUST pass all MUST and MUST NOT requirements applicable to its declared scope.

**CDS800-R072** SHOULD requirements MAY be unmet only where a documented rationale exists. *(Keyword corrected per the CLEANUP-PASS §C ambiguous-case ruling: the governing modal is MAY; "SHOULD requirements" is a noun reference to the requirement class.)*

**CDS800-R073** A conformance claim MUST be accompanied by a dated conformance statement conforming to CDS-1000 §23, approved by the Conformance Declaration Executive.

**CDS800-R074** An organisation MAY declare different conformance levels or overlay profiles for different channels or business units, provided each claim's scope is explicit.

**CDS800-R075** Assessment method MUST be stated using the CDS-1000 §20 vocabulary: **self-attestation**, **customer assessment** or **independent assessment** *(finding 800-5; replaces v0.1 "self-assessed / partner-reviewed / independent")*.

**CDS800-R076** A certification mark or badge MUST NOT imply independent assessment when only self-attestation occurred.

**CDS800-R077** Material scope or control changes SHOULD trigger reassessment before a previous claim is reused.

*Informative example claim (CDS-1000 naming):* CDS v0.2 · scope: apparel catalogue, AU organisation, Shopify and Google channels · level: **CDS Verified** · overlay profiles: none (AI-Assured overlay not claimed) · assessment: self-attestation, 2026-08-04 · known exceptions: EXC-014, expires 2026-10-01. Full field set: CDS-1000 §23.

## 30. Review Cadences and Forums *(normative)*

| Cadence *(informative)* | Typical review |
|---|---|
| Daily / event-driven | Import failures, publication errors, blocking quality issues, security alerts |
| Weekly | Unknown values, workflow queues, channel drift, ageing incidents |
| Monthly | Quality scorecards, mapping coverage, AI evaluation, change backlog |
| Quarterly | Taxonomy, dictionary, namespace, exception and access review |
| Per release | Schema, mapping, migration and conformance impact |
| Annually | Governance model, ownership, profiles, conformance claim, roadmap |

Minimum recurring-review requirements are owned by CDS-1400 §24; the table above is a recommended shape, not a mandate.

**CDS800-R078** Review cadence SHOULD reflect the rate and risk of change in the governed domain.

**CDS800-R079** Review outcomes SHOULD create assigned actions rather than remain informational only.

## 31. Worked Governance Scenarios *(informative)*

**31.1 Supplier introduces a new colour name.** Supplier value "Midnight Ocean" enters the source layer; dictionary matching finds no approved alias; the value is quarantined (CDS-400 §17). The Dictionary Steward reviews imagery and supplier evidence and aliases it to canonical `navy`, retaining "Midnight Ocean" as the display label; facet membership is `blue`; channel values inherit existing navy mappings. The decision and evidence are recorded; affected products are revalidated, published, and read-back verifies the expected result (CDS-500).

**31.2 Proposed category rename.** "Throw Pillows" → "Cushions": the internal category identifier remains stable; display label, navigation text and storefront collection title change; URLs require redirect review; external taxonomy mappings are unchanged; analytics dimensions need an alias/continuity plan; legacy `collection_*` tag compatibility is assessed. Approved as a minor compatible release.

**31.3 Manual downstream edit creates drift.** Expected channel title "Linen Relaxed Shirt"; observed "Summer Linen Shirt"; verification result MISMATCH. The title is PIM-owned with no active override, so this is unauthorised drift: restore the expected title on the next controlled publication, notify the editor of the ownership rule ("enter data where it originates"), retain the observed value and reconciliation evidence.

**31.4 High-risk AI workflow change.** A request to let AI write compliance claims directly into canonical fields is rejected (claims may require evidence and legal approval — CDS-700). Approved alternative: AI drafts a proposal with mandatory evidence attachment; the compliance owner reviews; the accepted value enters the canonical record with provenance; publication remains subject to channel verification.

## 32. Architecture Decision Records *(normative record; rationale informative)*

| ADR | Decision | Status | Rationale |
|---|---|---|---|
| CDS-ADR-800-001 | Governance is a conformance requirement | Accepted (scope updated) | A sound data model degrades without ownership, controlled change and measurable operation. Under ADR-D1, full governance is the **Governed capstone level**; ownership basics (R001) bind from Foundation. |
| CDS-ADR-800-002 | Conformance is scoped and levelled | **Superseded by ADR-D1** | The single ladder and overlay-profile model now live in CDS-1000. |
| CDS-ADR-800-003 | One authority per product fact | Accepted | Multiple simultaneous masters create unresolved drift and accountability gaps (CDS-200 §13). |
| CDS-ADR-800-004 | Exceptions expire or are reviewed | Accepted | Unbounded exceptions become hidden permanent architecture. |
| CDS-ADR-800-005 | Stable identifiers are governed separately from labels | Accepted | Display language evolves without breaking identity and mappings. |
| CDS-ADR-800-006 | Release completion includes verification | Accepted | Deployment success does not prove correct downstream state. |
| CDS-ADR-800-007 | Certification claims distinguish assessment type | Accepted | Self-attestation, customer assessment and independent assessment are not equivalent (vocabulary: CDS-1000 §20). |
| CDS-ADR-800-008 | Small teams may combine roles but not erase responsibilities | Accepted | Governance must remain practical while preserving accountability. Cross-referenced by the CDS-1300/CDS-1400 small-team profile. |

---

## Annex A — Recommended RACI Matrix *(informative)*

Role names are those of the §5 register.

| Governance activity | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|
| Canonical product model | PIM Product Owner | Schema Owner | Product Data and Channel Owners | Product teams |
| Taxonomy change | Taxonomy Owner | Data Steward (taxonomy) | Merchandising, SEO, Channel Owners | Editors and analysts |
| Dictionary value approval | Dictionary Owner | Data Steward (dictionary) | Merchandising and Channel Owners | Import and content teams |
| Channel mapping release | Channel Owner | Integration Owner | Schema Owner, verification owners | Commerce operations |
| AI workflow approval | AI Governance Owner | AI workflow owner (per CDS-700 registry) | Product Data, Security and Compliance Owners | Reviewers and operators |
| Conformance statement | Conformance Declaration Executive | CDS Governance Owner | Assurance Reviewer and domain owners | Stakeholders |

## Annex B — Change Proposal Record *(informative template)*

Change ID · Title · Requester · Problem statement · Proposed change · Affected artefacts · Affected product count · Affected channels · Compatibility class · Risk and customer impact · Migration plan · Validation plan · Rollback plan · Required approvals · Target release · Outcome and evidence.

## Annex C — Exception Record *(informative template)*

Exception ID · Requirement (ID) · Scope · Reason · Risk · Compensating control · Owner · Approver · Start date · Expiry/review date · Resolution plan · **Retest result** (evidence at closure, R031) · Status.

*(The v0.1 "Exception and Waiver Record" title is retired with the waiver noun — CDS-100 §8.)*

## Annex D — Conformance Statement *(normative pointer)*

The conformance statement and claim/manifest schema are defined in CDS-1000 §23 and encoded in CDS-1100. The v0.1 Appendix D template is withdrawn *(finding 800-6)*; CDS-800 adds only the governance obligations of §29 (executive approval, honest scope, dated statement, assessment vocabulary).

## Annex E — Governance Readiness Checklist *(informative)*

- [ ] PIM and canonical authority are explicitly declared (CDS-200 §13).
- [ ] Every governed domain has an accountable owner.
- [ ] Taxonomy, dictionary, schema and namespace registries exist.
- [ ] Channel owners and capability profiles exist.
- [ ] Change, release, migration and rollback processes are documented.
- [ ] Exceptions have owners, review dates and retest evidence at closure.
- [ ] Quality metrics and review cadences are defined.
- [ ] Publication observation and verification are operational for claimed channels.
- [ ] Access and tenant isolation are reviewed.
- [ ] AI workflows have named owners and CDS-700 controls.
- [ ] Conformance statement scope is accurate and supportable with evidence (CDS-1000).

## Annex F — Organisation Example: Legacy Documentation Alignment *(informative — organisation-specific example; not part of the vendor-neutral standard)*

This annex records how one adopting organisation's pre-CDS artefacts map to this chapter *(finding 800-10: all organisation-specific material consolidated here)*. It illustrates that CDS governance can be reached bottom-up from working practice; no artefact named here is a CDS requirement.

| Existing artefact or pattern | CDS-800 interpretation |
|---|---|
| Legacy product-data workflow | Operational evidence of source separation, canonical resolution, channel output and verification responsibility |
| Legacy tag-governance workflow | A governed registry, namespace discipline, deprecation model and PIM authority over channel tags |
| Legacy implementation sequencing guide | A controlled implementation sequence in which taxonomy and governance precede product-scale publication |
| Airtable `Import_*` / `Airtable_*` / `Shopify_*` / `Match_*` layers | Clear separation of supplier intake, authority, observed state and verification evidence — a working example of §20's source/canonical separation |
| Traffic-light formulas | Human-facing control status backed by detailed reconciliation logic (now: CDS-500 §18) |
| Taxonomy decision log | A practical record for ambiguous classification decisions (R052) |
| Profile H / Profile S choice | An organisation-level implementation policy that must remain consistent or be migrated deliberately (§9) |

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): Annex placement. REVIEW-003 Matrix 5 proposes one corpus-wide legacy-alignment annex (candidate homes: CDS-1300 or standalone). This chapter's organisation-specific material is consolidated here for now; if a corpus-wide annex is created at v0.2 freeze, this annex merges into it and becomes a pointer.

*END OF CDS-800 v0.2 REVIEW DRAFT*


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-900 — Implementation Profiles and Platform Mappings

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-17 |
| Supersedes | CDS-900 Working Draft v0.1; the platform-specific material of CDS-500 v0.1 Appendices C and D (merged here per REVIEW-006 systemic finding 2) |
| Normative status | §1–§3 (profile model, precedence, mapping contract), the profile rules in §4–§11 and §13 (conformance) are normative. All platform-behaviour statements, mapping tables marked informative, §12 (migration), the appendices and every IMPLEMENTATION NOTE are informative. |
| Findings addressed | SYS-1 (errata manifest §C: all 64 prefix-labelled rules), CDS900-1, CDS900-3, CDS900-4, CDS900-5, CDS900-6, CDS900-7, CDS900-8, CDS900-9, CDS900-10, 200-7, CDS500-6 (corollary), Matrix 1 (STD_ row), Matrix 5; ADR-D2, ADR-D3, ADR-D24; REVIEW-006 |

**Profile releases defined by this chapter:** CDS-SHOPIFY-0.2 (§4), CDS-GMC-0.2 (§5), CDS-META-0.2 (§6). Platform references were retrieved and spot-verified on **2026-08-03**, with Shopify Search & Discovery limits refreshed on **2026-08-17** (REVIEW-006); Appendix D carries per-reference dates.

> IMPLEMENTATION NOTE *(informative)*: Platform behaviour changes over time. Platform-specific requirements in this chapter are **versioned profile rules, not permanent changes** to the canonical CDS model. Each platform profile carries a release identifier and dated references so that a claim of conformance is always a claim against a stated platform snapshot.

---

## 1. Purpose and Profile Model *(normative)*

CDS defines a canonical commerce information model. A profile explains how that model is implemented within a platform, channel, industry or organisation without allowing the implementation target to become the master product layer.

**CDS900-R001** Every implementation profile MUST identify its scope, mapping rules, platform constraints, publication behaviour, observation coverage and conformance tests.

**CDS900-R002** Every platform profile MUST carry a profile release identifier and MUST date every external platform reference it relies on (retrieved-on date).

**CDS900-R003** A platform profile MUST NOT redefine canonical product truth merely because the target platform lacks a corresponding field.

**CDS900-R004** An industry profile MAY require additional attributes and dictionaries, but MUST preserve the CDS core semantics.

**CDS900-R005** An organisation profile MAY extend a platform or industry profile, but MUST document every divergence.

```
CDS Core Standard
      |
      +-- Industry Profile: Apparel
      |       |
      |       +-- Platform Profile: Shopify (CDS-SHOPIFY-0.2)
      |               |
      |               +-- Organisation Profile: Example Store
      |
      +-- Industry Profile: Homewares
              |
              +-- Platform Profile: Google Merchant Center (CDS-GMC-0.2)
```

## 2. Profile Hierarchy and Precedence *(normative)*

Profiles are applied in layers.

| Layer | Purpose | Example |
|---|---|---|
| CDS Core | Vendor-neutral semantics and architecture | Canonical colour, facet colour, channel mapping |
| Industry Profile | Domain-specific fields and rules | Apparel fit, garment size; homewares room and finish |
| Platform Profile | Platform storage and delivery mapping | Shopify product category, Google product_type |
| Organisation Profile | Store-specific vocabularies and policies | Brand colour names, collection hierarchy |
| Product Record | Actual values and permitted overrides | French Navy shirt in size M |

**CDS900-R006** **Precedence rule:** more specific profiles (industry → platform → organisation) MAY add constraints; **CDS core semantics remain authoritative for every shared concept**. Where two profiles conflict, the implementation MUST preserve the core CDS meaning and MUST record the narrower profile decision explicitly. (This restates CDS-000 §6 CDS000-R011 in profile terms; a profile never weakens a core requirement.)

**CDS900-R007** A platform limitation MAY create an exception in the publication projection, but MUST NOT silently alter the canonical record.

## 3. Common Platform Mapping Contract *(normative)*

Every channel mapping is described by a common contract. This enables consistent publication and verification even when platforms use different APIs, files or terminology.

| Contract Property | Meaning |
|---|---|
| Canonical source | The PIM field or derived canonical value. |
| Target path | The channel field, metafield, attribute or feed column. |
| Transformation | The deterministic conversion from canonical to expected channel value. |
| Requiredness | Always, conditional, optional or unsupported. |
| Cardinality | Single, list, set or variant-specific. |
| Write semantics | Replace, merge, append, upsert or derived. |
| Read-back path | How the downstream value is observed. |
| Comparison rule | Exact, normalized, numeric, set, ordered list or identifier. |
| Ownership | PIM, channel, shared by explicit contract, or observed only. |
| Failure policy | Block, warn, omit, quarantine or retry. |

**CDS900-R008** Where a transformation is defined, verification MUST compare the expected channel representation with the observed channel representation, not raw PIM text. (Lifecycle, statuses and comparison semantics: CDS-500.)

**CDS900-R009** A mapping MUST declare whether the channel value is observable. Missing and unobservable MUST remain different verification states (CDS-500 §17).

**CDS900-R010** Where an MF_ attribute is published to a channel's native or standard field rather than a metafield-like structure, that is a mapping concern of the platform profile; the canonical prefix does not change (ADR-D2). A profile MUST document MF_→metafield, MF_→native-field and MF_→feed-column projections per mapping.

## 4. Shopify Implementation Profile — CDS-SHOPIFY-0.2 *(normative rules; platform statements informative, references retrieved 2026-08-03)*

The Shopify profile maps CDS product information into Shopify standard fields, product categories, category metafields, custom metafields, variants, collections, tags, media and Search & Discovery filters. Shopify is a publication and transaction platform; the PIM remains authoritative for PIM-owned product information (CDS-200).

### 4.1 Shopify Object Boundaries *(normative)*

| CDS Concept | Shopify Target | Authority |
|---|---|---|
| Canonical product | Product resource and related custom data | PIM |
| Sellable variant | Product variant | PIM for descriptive identity; inventory authority may differ |
| Internal category | No direct equivalent; mapped to product category and store collections | PIM |
| Shopify standard category | Product category | PIM mapping |
| Product type | Product type field | PIM |
| Canonical attribute | Category metafield or custom metafield | PIM |
| Facet value | Search & Discovery filter source or controlled projection | PIM |
| Merchandising collection | Automated or manual collection | PIM or governed merchandiser |
| Workflow state | Normally retained in PIM; optional internal tag/metafield | PIM |
| Observed state | Read-back through connector/API | Channel observation only |

**CDS900-R011** PIM-owned product fields edited directly in Shopify SHOULD be considered downstream drift unless an approved override workflow exists (CDS-500 ownership modes).

#### Edit protection and drift attribution on Shopify *(informative platform facts, verified 2026-08-04 — REVIEW-006A; implements CDS-500 §20.1 for this profile)*

**What permissions can and cannot do.** Shopify staff permissions for products are: View, View cost, Create and edit, Edit cost, Edit price, Export, Delete — **there is no field-level or per-product edit restriction** on any plan (Plus adds user groups/custom org roles but the product permission set is the same). The one real permission lever: staff who do not need to edit products can have "Create and edit" withheld entirely. Note the metafield implication: anyone with product edit rights can also add, edit and **delete metafield definitions and values** — merchant-owned metafield definitions cannot be protected from staff; the only edit-proof mechanism is app-owned reserved namespaces (with the D17 visibility trade-off, declared per this profile).

**Attribution mechanisms and their limits** (for CDS500-R077b correlation):
| Mechanism | What it gives | Limits |
|---|---|---|
| GraphQL `events` query / Events resource | Timestamped events with `author` string, app/admin attribution booleans | Product verbs are create/destroy/published/unpublished — **routine field edits may generate no event**; author is a string, not a typed staff ID; 1-year retention |
| Admin Store activity log | Recent admin actions with actor name (person/app/channel) | View-only, max 250 results, no export; bulk edits/background jobs/app syncs can show "Shopify" instead of the actor |
| `products/update` webhook | Near-real-time change signal with timestamps | **Payload contains no actor field** — tells you *when*, never *who* |
| User-management activity log (CSV export, 6 months) | User/role changes | Does not cover product edits |
| PIM's own publication records | Complete provenance for API writes made by the PIM | Covers only the PIM's own writes |

**Consequence:** on Shopify, drift attribution is **best-effort correlation**: the CDS-500 §20.1 detection interval (previous vs new observed value, bounded by observation timestamps) narrowed against the Store activity log's recent window and webhook `X-Shopify-Triggered-At` timestamps. The implementation SHOULD record the attribution outcome class honestly (actor identified / actor class identified / unattributable) and MUST NOT promise field-level audit trails this platform does not provide.

**CDS900-R012** The Shopify connector MUST know, per target field, whether an update replaces or merges the downstream value, and MUST declare this in the mapping's write semantics.

**CDS900-R013** The connector MUST use the correct current mutation for each object class and MUST NOT assume one product mutation covers variants.

> Platform note *(informative, verified 2026-08-03)*: in the current Shopify GraphQL Admin API, `productUpdate` **no longer updates variant data**; variant changes require `productVariantsBulkUpdate` or `productSet`. Connectors written against older API behaviour will silently stop updating variants. Source: [S6].

### 4.2 Shopify Namespace Mapping *(normative table; CDS-300 is the registry of record)*

The namespace registry lives solely in CDS-300; this table states only how registered namespaces **project onto Shopify targets**. It does not define any namespace.

| CDS Namespace (per CDS-300) | Shopify Projection | Example |
|---|---|---|
| STD_ (canonical core field, closed enumeration per ADR-D2) | Mapped **to** the corresponding native Shopify field | STD_title -> Product title |
| CAT_ | Internal classification; mapped product category and product type projections | CAT_shopify_category_id |
| VAR_ | Option and variant data | VAR_size, VAR_colour |
| MF_ (extended structured attribute, mechanism-neutral per ADR-D2) | Typically a category or custom metafield; MAY project to a native field where one exists | MF_material -> category metafield |
| CH_shopify_ | Shopify-specific output or override | CH_shopify_title_override |
| SEO_ | Search engine listing fields | SEO_title -> search engine listing title |
| MED_ | Product media and alt text | MED_primary_image |
| OBS_shopify_ | Observed Shopify state (read-back), never canonical | OBS_shopify_material |
| QA_shopify_ | Comparison result and verification status | QA_shopify_material |
| WF_ | PIM workflow; not customer-facing, published only by exception | WF_ready_to_publish |

> IMPLEMENTATION NOTE *(informative)*: MF_ identifies the human-recognisable attribute domain. The internal technical key may still use a durable namespace and key such as `cds.material` or `custom.material` (CDS-300 visible-identifier vs internal-key separation).

### 4.3 Classification and Taxonomy *(normative)*

> Platform note *(informative, verified 2026-08-03)*: each Shopify product has **one** product category (from Shopify's Standard Product Taxonomy) and **one** merchant-defined product type; assigning a standard category unlocks the category metafields associated with that category. Source: [S1].

**CDS900-R014** The PIM internal category MUST remain separate from the Shopify product category and the Shopify product type.

**CDS900-R015** The PIM SHOULD map each final internal category to one Shopify Standard Product Taxonomy category identifier or breadcrumb.

**CDS900-R016** The mapping SHOULD be stored on the category entity and inherited by products unless a documented product-level exception is required.

**CDS900-R017** The Shopify product type SHOULD contain a controlled merchant vocabulary and MUST NOT be a concatenation of descriptive attributes.

```
Internal category:
  Apparel > Women > Tops > Shirts
Shopify projections:
  Product category  = Apparel & Accessories > Clothing > Clothing Tops > Shirts
  Product type      = Shirt
  Collections       = Women, Tops, Shirts
  Category metafields = fabric, colour, neckline, sleeve length, target gender...
```

> IMPLEMENTATION NOTE *(informative, not spot-verified this pass)*: Shopify may update or replace taxonomy nodes. The PIM should version category mappings and treat taxonomy migration as a controlled profile change, not a manual per-product repair.

### 4.4 Attributes, Metafields and Metaobjects *(normative)*

> Platform note *(informative; unlock mechanism verified 2026-08-03, metaobject-entry detail partially verified)*: Shopify category metafields are standardized product attributes associated with a product category; their entries use Shopify metaobjects and standardized base values. Custom metafields remain available for information not represented by the category model. Sources: [S1] [S3].

**CDS900-R018** When an appropriate Shopify category metafield exists, the Shopify profile SHOULD map the corresponding canonical attribute to it.

**CDS900-R019** A custom metafield SHOULD be used when the canonical attribute is not available as a category metafield, is store-specific, or requires a different type or lifecycle.

**CDS900-R020** The choice of category metafield versus custom metafield MUST be recorded in the Attribute Definition mapping (CDS-200 §7), not decided independently for each product.

**CDS900-R021** A metafield used as a storefront filter MUST have an appropriate metafield definition and a supported data type.

| Canonical Attribute | Preferred Shopify Target | Fallback |
|---|---|---|
| Material / fabric | Category metafield when available | Custom product metafield |
| Colour family | Category metafield or dedicated filter metafield | Custom product metafield |
| Display colour | Variant option / linked category entry | Custom product or variant metafield |
| Fit | Category metafield when available | Custom product metafield |
| Care instructions | Custom product metafield | Rich text content block |
| Supplier identifier | Internal custom metafield only if required downstream | Keep in PIM |
| Workflow review status | Keep in PIM | Internal-only metafield or tag by exception |

> IMPLEMENTATION NOTE *(informative)*: Shopify allows category entries to be customised for brand presentation, but CDS still distinguishes display label, canonical value and facet value (CDS-400). Renaming a Shopify entry does not by itself redefine the PIM canonical dictionary.

### 4.5 Variants and Options *(normative)*

> Platform note *(informative, verified 2026-08-03)*: current Shopify documentation permits up to **three options and 2,048 variants** per product, while noting that some themes, apps and sales channels may have lower effective support (historically ≤100). Source: [S4].

**CDS900-R022** Only SKU-producing differences MAY become Shopify variant options under the CDS profile (variant boundary rule: CDS-200 §5).

**CDS900-R023** The connector MUST preflight the projected variant count and option count against the profile's declared platform limits before publication.

**CDS900-R024** A canonical product model requiring more options than Shopify supports MUST use a documented decomposition strategy rather than dropping information.

**CDS900-R025** Variant option values SHOULD be connected to reusable category metafield entries where that improves consistency and the target theme or channel supports them.

#### 4.5.1 Variant Decomposition Strategies *(informative)*

| Condition | Preferred Strategy |
|---|---|
| More than three independent options | Split into logical products or use a configured product mechanism. |
| Very high variant count | Use combined listings or split by a major customer choice where supported. **Caveat:** combined listings have historically been restricted by Shopify plan (Plus); availability on the store's plan must be confirmed before this strategy is adopted (not verified this pass — REVIEW-006). |
| Personalisation that does not create inventory | Use line-item/customer input rather than variants. |
| Colour-specific product imagery and titles | Retain canonical parent relation; publish separate products only when merchandising requires it. |
| Size is not inventory-bearing | Do not create variants merely for filtering. |

### 4.6 Collections, Tags and Navigation *(normative)*

CDS separates classification from merchandising. Shopify collections are customer-facing groupings. Tags are governed integration signals and may drive automated collections, but they are not the canonical source for structured attributes (CDS-400 tag governance).

**CDS900-R026** Taxonomy collections SHOULD be generated from the PIM category tree or explicit category-to-collection projection rules.

**CDS900-R027** Campaign and editorial collections MAY use merchandising rules or manual curation, but MUST have a declared owner and lifecycle.

**CDS900-R028** Structured values such as material, colour family, dimensions and fit SHOULD be stored in metafields or standard attributes rather than duplicated as tags solely for filtering.

**CDS900-R029** Every published tag MUST be generated, registered or explicitly approved. Uncontrolled tag creation MUST be rejected or quarantined.

**CDS900-R030** Tag publication MUST be set-based: the connector MUST regenerate and write the complete governed tag set, or use an explicitly additive operation, and MUST declare which in the mapping's write semantics.

> Platform note *(informative, verified 2026-08-03)*: in the Shopify GraphQL Admin API, updating the `tags` field via `productUpdate` is a **full replacement** — "Updating tags overwrites any existing tags"; `tagsAdd` exists for additive updates. A connector that writes a partial tag list silently deletes every other tag on the product. Source: [S7]. *(Absorbed from CDS-500 v0.1 Appendix C; the general set-comparison and merge-semantics rules remain in CDS-500.)*

#### 4.6.1 Tag Namespace Profile *(normative table)*

| Tag Prefix | Purpose | Generation |
|---|---|---|
| collection_ | Automated collection or navigation projection | Computed from category/collection rules |
| merch_ | Merchandising signal | Governed manual or rule-based |
| season_ | Seasonal relevance where a binary signal is sufficient | Controlled value / rule-based |
| workflow_ | Internal process signal | PIM only by default; publish by exception |
| supplier_ | Traceability | PIM only by default; publish by exception |

> IMPLEMENTATION NOTE *(informative)*: the legacy `collection_*` model remains valid as a Shopify projection regenerated from governed rules. It is not the canonical category itself. A future connector may use explicit collection membership instead without changing the PIM taxonomy.

### 4.7 Search, Discovery and Facets *(normative)*

> Platform note *(informative, verified 2026-08-17)*: Shopify Search & Discovery supports filters based on category, product and variant metafield definitions, including text, numeric, boolean and metaobject reference types, and permits grouping filter values into a single displayed value. Documented limits: **25 filters per store**; **100 values displayed per storefront filter**; **1,000 values visible per filter in the app**; **200 unique values per filter group**; **1,000 filter groups store-wide**; filters do not display on collections over **5,000 products** or searches over **100,000 results**; and the **Category filter cannot use value grouping**. Source: [S2].

**CDS900-R031** Customer filters MUST use the CDS facet layer (CDS-600) rather than exposing every distinct source or display value.

**CDS900-R032** The Shopify profile MUST define one filter source per approved facet and MUST document its data source.

**CDS900-R033** A colour filter SHOULD expose broad colour families such as Blue rather than dozens of commercial shade names.

**CDS900-R034** Filter value grouping MAY be used as a channel-level convenience, but the authoritative grouping MUST remain in the PIM facet dictionary.

**CDS900-R035** Facet projections MUST be preflighted against the declared platform limits (filter count, storefront and app value limits, values per group, store-wide group count, collection/search result limits and non-groupable filters) recorded in the profile's channel capability declaration.

```
Product display shade:    French Navy
Canonical shade:          Navy
Facet family:             Blue
Shopify product/variant:  French Navy
Shopify filter value:     Blue
Search synonyms:          french navy, navy, dark blue
```

> RESOLVED (was new (resolved); verified 2026-08-04, REVIEW-006A): native Search & Discovery **does evaluate variant-scope filters at variant level**. Variant-option filters use variant-scope parameters (`filter.v.option.color`, `filter.v.option.size`), availability is a variant-specific filter (`filter.v.availability=1`), different filters combine with AND ("selecting Red from Color and 8 from Size returns products that are both red and size 8"), and the product object's `featured_media`/`url` update to the first variant matching the current filters — variant-level evaluation, not product-level unions. Sources: help.shopify.com Search & Discovery filters; shopify.dev storefront-filtering (both accessed 2026-08-04). The Shopify profile therefore declares the combination-availability capability **present**; empirical confirmation of per-value *count* accuracy under combined selections remains a vertical-slice test item.

### 4.8 Publication and Verification *(normative)*

The Shopify profile implements the CDS-500 lifecycle: calculate expected state, publish, observe, normalize, compare and report. Shopify success responses are transport acknowledgements, not field-level proof (CDS-P-06).

**CDS900-R036** The connector MUST retain Shopify product and variant identifiers after creation.

**CDS900-R037** The connector MUST read back the PIM-owned fields required by the verification profile.

**CDS900-R038** Tags and list fields MUST be compared as sets unless order has declared meaning.

**CDS900-R039** Rich text and HTML MUST be compared using a declared canonicalisation method (normalisation registry: CDS-500 §16).

**CDS900-R040** Category and metafield references SHOULD be compared by stable identifiers or base values rather than display text alone.

**CDS900-R041** Verification statuses and their traffic-light presentation are defined solely in **CDS-500 §17–§18**; this profile MUST use that enum and mapping and MUST NOT define its own.

> Migration note *(informative, per ADR-D3)*: the v0.1 CDS-900 status table is deleted. Legacy `WRITE_ERROR` maps to the detailed status `PUBLICATION_ERROR` (core status `ERROR`); `WARNING` is retired — use the appropriate core status plus a `reason_code`; `ACCEPTED_WITH_LIMITED_OBSERVATION` is not a status and is expressed as per-field `MATCH` / `UNOBSERVABLE` results with a coverage ratio (see Appendix A.1).

## 5. Google Merchant Center Profile — CDS-GMC-0.2 *(normative rules; mapping table informative, references retrieved 2026-08-03)*

The Google profile maps canonical product information to the Merchant Center product data specification. Google uses submitted product data to match products with relevant queries and requires accurate formatting to avoid disapprovals or display problems *(verified 2026-08-03, [G1])*.

### 5.1 Classification *(normative)*

> Platform note *(informative, verified 2026-08-03)*: `google_product_category` uses Google's predefined taxonomy and accepts **either** a category ID **or** a full breadcrumb path, not both; Google describes it as an override of automatic categorisation, honoured only in applicable cases (category-specific requirements, Ads targeting, alcohol compliance). `product_type` carries the merchant's own classification path. Sources: [G2] [G3].

**CDS900-R042** CH_google_product_category MUST contain a valid Google taxonomy identifier or an accepted breadcrumb (one form, not both) when supplied.

**CDS900-R043** CH_google_product_type SHOULD be derived from the PIM internal category path from broad to specific.

**CDS900-R044** Google taxonomy and PIM taxonomy MUST remain separate mappings even where their text appears similar.

```
CAT_path                   = Apparel > Women > Tops > Shirts
CH_google_product_type     = Apparel > Women > Tops > Shirts
CH_google_product_category = Apparel & Accessories > Clothing > Shirts & Tops
```

### 5.2 Core Field Mapping *(informative — snapshot of the Google product data specification as retrieved 2026-08-03; the current dated specification governs at publication time)*

| CDS Source | Google Attribute | Requiredness (as at 2026-08-03) | Profile Rule |
|---|---|---|---|
| STD_id / SKU | id | Required | Stable unique offer identifier. |
| STD_title or approved override | title | Required | Channel title may be transformed but canonical title is preserved. |
| Content description | description | Required | Remove unsupported markup and channel-inappropriate content. |
| Canonical product URL | link | Required | Must resolve to the correct product or variant landing page. |
| MED_primary_image | image_link | Required | Use the primary compliant image. **Minimum 500x500 px enforced from 31 January 2027** (verified 2026-08-03). |
| Availability authority | availability | Required | Map controlled stock state to Google vocabulary. |
| Price authority | price | Required | Include currency and current sell price. |
| Brand dictionary | brand | **Required for new products other than media/books** (verified 2026-08-03) | Use canonical brand name. |
| GTIN / MPN | gtin / mpn | Conditional; **omitting an existing GTIN limits visibility/performance** (verified 2026-08-03) | Publish valid identifiers when available; identifier policy is a dated profile rule, not a core CDS rule (finding 200-7). |
| Canonical colour / channel value | color | Conditional (apparel) | **Landing-page colour value (Display Label / sellable colour)** — see the resolved note below. |
| Canonical material | material | Conditional | Use controlled channel representation. |
| Variant relationship | item_group_id | Conditional (variants) | Group related variants consistently. |
| CAT mapping | google_product_category | Optional (override) | Mapped Google taxonomy (ID or breadcrumb). |
| CAT path | product_type | Optional | Merchant-defined category breadcrumb. |

> RESOLVED (was new (resolved); verified 2026-08-04 against support.google.com/merchants/answer/6324487, REVIEW-006A): **the facet-family projection is NOT compliant and is removed as an option.** Google's minimum requirements state the submitted `color` must match the landing page ("if the landing page uses 'Toasted Walnut', submit 'Toasted Walnut' — don't submit 'Brown'"); non-compliance risks disapproval. Normative guidance for this profile:
> - **`color` = the landing-page colour value** (the Display Label / sellable colour, e.g. "French Navy"), never the facet family.
> - The **broad searchable colour name belongs in `title`** where discoverability is wanted (Google's own best practice for unique colour names).
> - **Multi-colour**: up to 3 slash-separated values, one primary + up to two secondary ("Navy/White"); never commas or merged strings.
> - As of May 2026 Google recommends also sending `variant_option` when colour is variant-identifying.
> The GMC field mapping's `source_layer` for `color` is therefore **display**, and the CDS-400 facet family remains a storefront-filter concern only.

**CDS900-R045** The Google profile MUST preserve variant identity and item grouping consistently across updates.

**CDS900-R046** The connector MUST validate required and conditional attributes against the current, dated Google product data specification before publication.

**CDS900-R047** Disapprovals and diagnostics SHOULD be imported as observed channel quality events, not treated as canonical product values.

### 5.3 Observation and Verification *(normative)*

**CDS900-R048** The Google connector SHOULD observe item status, diagnostics and accepted attribute values where the integration provides access.

**CDS900-R049** A product accepted into Merchant Center MUST NOT automatically be treated as fully verified if field-level observation is incomplete; unobserved fields carry UNOBSERVABLE, and coverage is reported per CDS-500.

**CDS900-R050** Google-normalised or automatically inferred values MUST be stored as observed or inferred channel state and MUST NOT be silently copied into canonical fields.

## 6. Meta Catalogue Profile — CDS-META-0.2 *(normative rules; platform statements informative, references retrieved 2026-08-03)*

> Platform note *(informative, verified 2026-08-03)*: Meta catalogues can receive product information through partner integrations, manual entry, APIs, scheduled data feeds **and pixel-based ingestion**. Meta publishes product data specifications for catalogue ingestion and supports data-source management in Commerce Manager. Sources: [M1] [M2] [M3].

**CDS900-R051** The Meta profile MUST identify the exact ingestion mechanism in use, because write, update, read-back and diagnostic behaviour differ by source.

**CDS900-R052** Meta category, gender, age group and other channel values MUST be mapped from canonical dictionaries or channel mappings.

**CDS900-R053** The PIM MUST remain authoritative even when Shopify or another partner platform forwards products to Meta.

### 6.1 Direct versus Indirect Meta Publication *(normative)*

| Mode | Benefits | CDS Requirement |
|---|---|---|
| Direct PIM to Meta feed/API | Maximum mapping control and independent verification | PIM owns expected state and source identifiers. |
| PIM to Shopify to Meta channel | Simpler operations; platform-managed transfer | Treat Meta as a second-hop channel and document reduced observation coverage. |
| Supplier/partner source to Meta | Fast onboarding | Must not bypass canonical governance for fields the organisation claims to control. |

**CDS900-R054** Multi-hop publication MUST record the immediate publication target and SHOULD record the final destination channel.

**CDS900-R055** Where final Meta values cannot be read back, the verification status MUST be UNOBSERVABLE rather than MATCH.

> IMPLEMENTATION NOTE *(informative, corollary of finding CDS500-6)*: "Meta read-back is unavailable" is **not a platform fact** — the Graph/Catalog API supports item reads. Read-back availability depends on the **integration mode**: a direct API integration can observe items; a Shopify-forwarded catalogue typically cannot be observed from the PIM. Declare observation coverage per ingestion mechanism, honestly. A second-hop value that cannot be observed is reported as an observation gap, never assumed correct.

## 7. Supplier Import Profile *(normative)*

The supplier import profile standardises raw acquisition while preserving supplier-specific source data and provenance. It formalises the proven three-layer pattern from the legacy Airtable PIM:

```
Layer 1: IMPORT_ raw supplier source record (Source Values per CDS-400; legacy Import_* fields alias to IMPORT_)
Layer 2: canonical PIM value
Layer 3: channel expected and observed values

Supplier value -> normalize -> map dictionary -> validate -> propose/accept canonical value
```

> RESOLVED (was new (resolved)): CDS-300 v0.2 registers `IMPORT_` as a core namespace for ingested source records and intake provenance (CDS-300 §4/§16), formalising the load-bearing legacy `Import_*` production namespace. Layer 1 uses `IMPORT_`; legacy `Import_*` fields are migration aliases to it.

**CDS900-R056** Raw supplier values MUST be preserved separately from canonical values.

**CDS900-R057** Every supplier mapping MUST record source, field, transformation version and last acquisition time.

**CDS900-R058** Unknown dictionary values MUST enter quarantine or review and MUST NOT silently create new canonical values (CDS-400 §17).

**CDS900-R059** Supplier categories MUST be treated as source classifications and mapped to the internal taxonomy, not copied directly as canonical categories.

| Supplier Input | Canonical Target | Example Transformation |
|---|---|---|
| Brand spelling | Brand dictionary | Blackmagic -> Blackmagic Design |
| Stock text | Availability/quantity authority | IN STOCK -> governed availability state |
| Colour name | Colour reference dictionary | French Navy -> Navy -> Blue facet |
| Category text | Internal taxonomy mapping | Cameras - Cinema -> Cameras > Cinema Cameras |
| Price text | Money value | $1,476.00 -> 1476.00 AUD |
| Barcode text | GTIN string | Remove spaces; retain leading zeros |
| Composition text | Material composition structure | 80% Cotton / 20% Polyester -> component list |

## 8. Apparel Industry Profile *(normative)*

The apparel profile adds domain-specific requirements for garment classification, variants, colour, size, fit, material composition, care and customer facets. (Detailed reference dictionaries: CDS-1500.)

### 8.1 Required Attribute Families *(normative table)*

| Group | Common Attributes | Scope |
|---|---|---|
| Identity | Brand, style number, season, range | Product |
| Classification | Department, garment type, target gender, age group | Product |
| Colour | Display shade, canonical shade, colour family, swatch | Product/variant |
| Size | Size system, label, normalized size, measurements | Variant |
| Fit | Fit type, silhouette, rise, leg style | Product |
| Construction | Material composition, weave/knit, lining, closure | Product |
| Design | Pattern, neckline, sleeve length, garment length | Product |
| Care | Wash, dry, iron, bleach, dry-clean instructions | Product |
| Merchandising | Style, occasion, seasonality | Product |
| Compliance | Country of origin and required claims | Product/variant |

**CDS900-R060** Apparel colour MUST support at least display shade, canonical shade and customer facet family (value layers: CDS-400).

**CDS900-R061** Apparel size MUST record its size system and MUST NOT rely on an unqualified label such as M or 10 alone when multiple systems are possible.

**CDS900-R062** Material composition MUST preserve percentages and component order where supplied.

**CDS900-R063** Fit and style MUST remain separate attributes; style is not a substitute for garment fit.

### 8.2 Apparel Facet Profile *(informative)*

| Facet | Recommended Customer Values |
|---|---|
| Colour | Black, White, Grey, Blue, Green, Red, Pink, Purple, Brown, Beige/Cream, Yellow, Orange, Metallic, Multi |
| Size | Store-specific normalized size groups with visible system labels |
| Material | Cotton, Linen, Wool, Silk, Denim, Leather, Synthetic, Blended |
| Fit | Slim, Regular, Relaxed, Oversized, Tailored, Loose |
| Pattern | Plain, Striped, Checked, Floral, Animal, Abstract, Geometric, Textured |
| Occasion | Everyday, Work, Formal, Party, Wedding, Travel, Beach, Active |
| Style | Classic, Minimal, Coastal, Boho, Streetwear, Resort, Athleisure and governed store values |

> IMPLEMENTATION NOTE *(informative)*: the recommended values are informative seeds. Each organisation must validate its customer vocabulary and avoid facet lists that are too long to scan (CDS-600).

## 9. Homewares Industry Profile *(normative)*

The homewares profile adds room, product form, material, finish, dimensions, shape, indoor/outdoor suitability, care and safety considerations.

| Group | Common Attributes | Scope |
|---|---|---|
| Classification | Homeware type, room, use | Product |
| Material | Primary material, secondary materials, composition | Product |
| Finish | Painted, glazed, polished, brushed, matte, natural | Product/variant |
| Colour | Display colour, canonical colour, colour family | Product/variant |
| Dimensions | Height, width, depth, diameter, capacity, weight | Product/variant |
| Shape | Round, square, rectangular, oval, irregular | Product |
| Use | Indoor/outdoor, food safe, dishwasher safe, microwave safe | Product |
| Care | Cleaning and maintenance instructions | Product |
| Room | Living, bedroom, dining, kitchen, bathroom, office, outdoor | Product |
| Style | Modern, coastal, Scandinavian, rustic, industrial, classic | Product |

**CDS900-R064** Measurements MUST use structured numeric values and units; display strings alone are insufficient.

**CDS900-R065** A material family facet MAY group detailed values, for example Tasmanian Oak -> Oak -> Wood.

**CDS900-R066** Room is a merchandising/facet attribute and MUST NOT replace the product's primary category.

**CDS900-R067** Safety and suitability claims MUST be backed by an admissible evidence class (CDS-700) and MUST NOT be generated solely from aesthetic inference.

## 10. Cross-Channel Mapping Matrix *(informative)*

| Canonical Concept | Shopify | Google | Meta | PIM Authority |
|---|---|---|---|---|
| Internal category | Mapped to product category + collections | product_type + taxonomy mapping | category mapping | Yes |
| Product title | Native title | title | title | Yes |
| Display colour | Variant option / display metafield | color representation | color representation | Yes |
| Colour family facet | Filter metafield/category value | **Never published to `color`** (non-compliant — §5.2 resolved note); storefront filter concern only | Storefront filters | Yes |
| Material | Category/custom metafield | material | material where supported | Yes |
| Variant grouping | Product + variants | item_group_id | item_group_id / retailer group | Yes |
| Google taxonomy | Optional Shopify feed field/mapping | google_product_category | May inherit/map | Yes — as mapping |
| Merchandising collection | Collection | custom label by choice | product set / label by choice | Yes |
| Verification result | PIM QA only | PIM QA only | PIM QA only | Yes |

## 11. Conformance and Testing *(normative)*

A CDS-900 conformant platform implementation passes both structural and behavioural tests. (Levels, claims and test-suite governance: CDS-1000.)

### 11.1 Common Profile Tests

- Every mapped field declares canonical source, target, transformation, authority and comparison strategy (R008, §3).
- Unsupported canonical values remain preserved in the PIM (R003, R007).
- Channel overrides are distinguishable from canonical values.
- Expected state can be regenerated from the same canonical revision and mapping version (CDS-500).
- Observed values are stored separately from expected values.
- Missing and unobservable are distinct verification states (R009).
- Dictionary and taxonomy mappings are versioned.
- Unknown supplier values enter review rather than silently extending dictionaries (R058).
- The profile release identifier and dated references are present (R002).

### 11.2 Shopify Profile Tests

- A product category mapping publishes a valid Shopify taxonomy value (R015).
- Product type remains a controlled merchant value distinct from category (R014, R017).
- Category/custom metafield selection is defined at schema level (R020).
- Variant counts and option counts are preflighted (R023).
- Facet projections respect declared Search & Discovery limits (R035).
- Structured facets use metafields or standard attributes rather than uncontrolled tags (R028).
- Collection tags, if used, are regenerated from governed rules; tag writes are set-complete or explicitly additive (R029, R030).
- Variant updates use a variant-capable mutation (R013).
- Read-back verification detects direct Shopify edits to PIM-owned fields (R011, R037).

### 11.3 Google and Meta Profile Tests

- Internal category and external taxonomy values remain separate (R044).
- Variant grouping identifiers are stable (R045).
- Channel-required values are validated against the current dated specification (R046).
- Diagnostics are imported as observed quality events (R047).
- The ingestion mechanism and its observation coverage are declared (R051; §6.1).
- Multi-hop publication records reduced observation coverage honestly (R054, R055).

## 12. Migration from the Legacy Airtable PIM *(informative — organisation example)*

This section documents one organisation's legacy conventions and their CDS mapping. It is retained as a worked migration example, not as normative content. The legacy conventions align strongly with CDS; migration preserves their human readability and round-trip verification pattern while replacing formula sprawl with governed schema entities and mappings.

| Legacy Field Pattern | CDS-900 Interpretation | Migration Action |
|---|---|---|
| Import_* | Supplier import profile raw source field | Retain source data and provenance (§7). |
| Airtable_* | Canonical or computed standard field | Map to STD_, CAT_, VAR_ or other canonical domain. |
| MF_Airtable_* | Canonical value intended for metafield publication | Map to MF_ definition and target mappings (ADR-D2). |
| DF_Airtable_SEO_* | Google feed projection | Map to CH_google_*; feed-layer fields live under CH_ with end-to-end feed verification (ADR-D24). |
| Shopify_* / MF_Shopify_* | Observed Shopify state | Map to OBS_shopify_* observation fields. |
| Match_* | Verification result | Map to QA_shopify_* status and reason code (ADR-D3). |
| collection_* | Computed Shopify collection signal | Retain as governed Shopify projection if used (§4.6). |
| Traffic light formulas | Human-facing verification status | Retain UI; detailed machine status underneath per CDS-500 §17–§18. |

**CDS900-R068** Migration MUST preserve historical source and observed values where they are required for audit or reconciliation.

**CDS900-R069** Legacy DF_ names MAY remain as registered deprecated aliases during migration, but new channel mappings SHOULD use CH_. The DF_→CH_ transition is governed by the single consolidated **ADR-D24** (which supersedes CDS-ADR-900-002/003); DF_ is a deprecated legacy prefix in the CDS-300 registry.

**CDS900-R070** The migration MUST NOT collapse canonical, expected and observed values into one field.

## 13. Architecture Decision Records *(informative — global ADR register is authoritative)*

| ADR | Decision | Status |
|---|---|---|
| CDS-ADR-900-001 | Profiles extend CDS core without redefining it | Accepted |
| CDS-ADR-900-002 | CH_ is the default namespace for channel-specific data | **Superseded by ADR-D24** |
| CDS-ADR-900-003 | DF_ may remain for actual feed artefacts and legacy aliases | **Superseded by ADR-D24** |
| CDS-ADR-900-004 | Shopify category, product type and collections remain distinct | Accepted |
| CDS-ADR-900-005 | Metafield mappings are schema decisions | Accepted |
| CDS-ADR-900-006 | Facet simplification is canonical PIM logic | Accepted |
| CDS-ADR-900-007 | Multi-hop channels declare observation gaps | Accepted |
| CDS-ADR-900-008 | Industry profiles add requirements without creating new product truth | Accepted |

---

## Appendix A — Example Product Records *(informative)*

### A.1 Apparel: Linen Relaxed Shirt

```
STD_product_id             = P-1001
STD_title                  = Linen Relaxed Shirt
CAT_internal_path          = Apparel > Women > Tops > Shirts
CAT_product_type           = Shirt
CAT_shopify_category       = Apparel & Accessories > Clothing > Clothing Tops > Shirts
VAR_colour_display         = French Navy
VAR_size                   = M
MF_colour_canonical        = Navy
MF_colour_facet            = Blue
MF_material                = Linen
MF_fit                     = Relaxed
CH_google_product_type     = Apparel > Women > Tops > Shirts
CH_google_product_category = Apparel & Accessories > Clothing > Shirts & Tops
CH_google_color            = French Navy   (landing-page display shade — §5.2; the facet
                                            family is never published to color)
CH_google_material         = Linen
QA_shopify_material        = MATCH
QA_google_title            = MATCH
QA_google_color            = UNOBSERVABLE
QA_google_coverage_ratio   = 0.62          (per-field results + coverage replace the retired
                                            aggregate ACCEPTED_WITH_LIMITED_OBSERVATION)
```

### A.2 Homewares: Tasmanian Oak Side Table

```
STD_product_id             = P-2001
STD_title                  = Tasmanian Oak Side Table
CAT_internal_path          = Homewares > Living Room > Tables > Side Tables
CAT_product_type           = Side Table
MF_material_display        = Tasmanian Oak
MF_material_canonical      = Oak
MF_material_facet          = Wood
MF_room                    = Living Room
MF_height_mm               = 520
MF_width_mm                = 450
MF_depth_mm                = 450
CH_shopify_filter_material = Wood
CH_google_material         = Wood
QA_shopify_dimensions      = MATCH
```

## Appendix B — Namespace Registry Excerpt *(informative)*

**The registry of record is CDS-300.** This excerpt lists only the namespaces this chapter's profiles project, with their publication behaviour; it registers nothing and is not authoritative. Consult CDS-300 for definitions, the STD_ enumeration (ADR-D2), lifecycle states and reserved prefixes.

| Namespace (CDS-300) | Role in this chapter | Publication behaviour |
|---|---|---|
| STD_ | Canonical core field (closed enumeration) | Mapped to native platform fields where they exist |
| CAT_ | Internal classification and taxonomy mappings | May project to category/product-type fields |
| VAR_ | Sellable variant and option value | Projects to platform variant model |
| MF_ | Extended structured attribute (mechanism-neutral) | Projects per schema mapping: metafield, native field or feed column |
| CH_ | Channel-specific mapping, expected output or override | Publishes only to the named channel |
| SEO_ | Search engine listing fields | Projects to listing/SEO fields |
| MED_ | Media and alt text | Projects to platform media model |
| DF_ | Deprecated legacy feed prefix (ADR-D24) | Sanctioned migration aliases only; not for new design |
| OBS_ | Observed downstream state | Never customer-facing; never canonical |
| QA_ | Verification result and quality state | Never customer-facing |
| WF_ | Workflow state | PIM-only by default |
| AI_ | AI proposal, confidence, provenance | PIM-only unless explicitly approved (CDS-700) |

## Appendix C — Profile Change Checklist *(informative)*

1. Identify the official platform change, its effective date, and the retrieved-on date of the source.
2. Classify whether the change affects vocabulary, requiredness, capability, API transport or observation.
3. Update the channel capability profile (including declared limits and propagation windows).
4. Update mappings and transformation versions.
5. Run reference products through preflight, publication and read-back tests.
6. Assess migration and rollback requirements.
7. Update affected organisation and industry profiles.
8. Publish a versioned profile release (e.g. CDS-SHOPIFY-0.3) and retain the previous mapping for audit.

## Appendix D — References *(informative; verification per REVIEW-006, dated)*

| Ref | Source | Location | Retrieved / verified |
|---|---|---|---|
| [S1] | Shopify Help Center, Shopify's Standard Product Taxonomy (product category) | help.shopify.com/en/manual/products/details/product-category | Verified 2026-08-03 |
| [S2] | Shopify Help Center, Adding filters with Shopify Search & Discovery | help.shopify.com/manual/online-store/search-and-discovery/filters | Verified 2026-08-17 (25 filters; 100 storefront values; 1,000 app values; 200/group; 1,000 groups; 5,000 collection and 100,000 search-result limits) |
| [S3] | Shopify Help Center, Metafields | help.shopify.com/en/manual/custom-data/metafields | Retrieved 2026-08-03 (partially verified) |
| [S4] | Shopify Help Center, Adding variants | help.shopify.com/en/manual/products/variants/add-variants | Verified 2026-08-03 |
| [S5] | Shopify Help Center, Adding color swatches using category metafields | help.shopify.com/en/manual/custom-data/metafields/category-metafields/using-category-metafields | Retrieved 2026-08-03 (not spot-verified) |
| [S6] | Shopify GraphQL Admin API, productUpdate mutation | shopify.dev/docs/api/admin-graphql/latest/mutations/productUpdate | Verified 2026-08-03 (variants no longer updated) |
| [S7] | Shopify GraphQL Admin API, ProductUpdateInput (tags) | shopify.dev/docs/api/admin-graphql/latest/input-objects/ProductUpdateInput | Verified 2026-08-03 (tags full replacement) |
| [G1] | Google Merchant Center Help, Product data specification | support.google.com/merchants/answer/7052112 | Verified 2026-08-03 |
| [G2] | Google Merchant Center Help, Google product category | support.google.com/merchants/answer/6324436 | Verified 2026-08-03 |
| [G3] | Google Merchant Center Help, Product type | support.google.com/merchants/answer/6324406 | Retrieved 2026-08-03 |
| [G4] | Google Merchant Center Help, color attribute | support.google.com/merchants/answer/6324487 | Verified 2026-08-04 (REVIEW-006A) — governs §5.2 |
| [M1] | Meta Business Help Center, Product data specifications for catalogues in Commerce Manager | facebook.com/business/help/120325381656392 | Retrieved 2026-08-03 |
| [M2] | Meta Business Help Center, Ways to add products in your catalog | facebook.com/business/help/384041892421495 | Verified 2026-08-03 (corroborated via /365831587397584 and /125074381480892) |
| [M3] | Meta Business Help Center, About catalog data sources (incl. pixel) | facebook.com/business/help/125074381480892 | Retrieved 2026-08-03 |

END OF CDS-900 v0.2 REVIEW DRAFT


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1000 — Conformance, Testing and Assurance

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-1000 Working Draft v0.1; CDS-800 §9 conformance ladder and CDS-800 Appendix D claim template (both replaced by references to this chapter per ADR-D1) |
| Normative status | §§2–5, 7–19, 21–27 and Appendix B are normative. §1, §6, §20, §28 and Appendices A and C are informative. |
| Findings addressed | 1000-1, 1000-2, 1000-3, 1000-4, 1000-5, 1000-6; 800-1, 800-2, 800-5, 800-6, 800-7 (this chapter's side); CDS1100-6 (corollary); SYS-2; ADR-D1, ADR-D3, ADR-D5 |
| Dependencies | CDS-000 through CDS-900 (all published in the CDS v0.2 corpus release); machine-readable claim and manifest schemas in CDS-1100 |
| Audience | Implementers, PIM vendors, auditors, platform integrators, data owners, standards maintainers |

---

## 1. Purpose and Scope *(informative)*

CDS-1000 makes the Commerce Data Standard testable. The other chapters state what a conformant implementation does; this chapter defines how an implementation proves it: objective conformance levels, overlay profiles, test suites, evidence requirements, assurance methods and the rules for honest public claims.

This chapter is the **single normative home** for conformance levels, test suites, conformance claims and assurance (CDS-000 R005, ADR-D1). Other chapters cite it and do not restate it. In particular, the divergent five-level ladder formerly in CDS-800 §9 and the claim template formerly in CDS-800 Appendix D are superseded by this chapter.

CDS-1000 does not create a certification authority. It defines the framework that a self-assessor, customer, auditor or future certification body may use.

## 2. Conformance Philosophy *(normative)*

- **Objective.** A test yields the same conclusion when repeated against the same implementation state.
- **Version-specific.** A claim applies to a named CDS release and does not automatically transfer to a later release.
- **Profile-aware.** Platform, industry and overlay profiles add requirements; they never weaken the CDS core.
- **Evidence-based.** Every pass is supported by a retained artefact, query result, export, log or reproducible observation.
- **No compensation.** Strong performance in one area does not cancel failure of a mandatory requirement in another.
- **Honest scope.** A component, connector or workflow may claim limited conformance without implying that the entire organisation is conformant.
- **Repeatable.** The test suite is designed for automation where possible and controlled human review where necessary.

**CDS1000-R001** A conformance claim MUST identify the CDS version, test-suite version, conformance level, applicable profiles, implementation scope, assessment method and assessment date.

**CDS1000-R002** An implementation MUST NOT claim general CDS conformance when only a subset of requirements has been tested.

**CDS1000-R003** Tests MUST evaluate observable system behaviour and evidence, not marketing descriptions or intended future capability.

**CDS1000-R004** Mandatory tests MUST be pass/fail. A score or maturity percentage MUST NOT convert a failed mandatory test into a conformant result.

**CDS1000-R005** Informative quality metrics MAY accompany a conformance result but MUST be clearly separated from normative pass/fail status.

## 3. Conformance Claim Model *(normative)*

A complete claim is a structured statement with these parts: specification version, test-suite version, conformance level, implementation scope, profiles and assessment method.

```yaml
cds_claim:
  specification_version: "0.2"
  test_suite_version: "0.2"
  level: verified
  scope: Product information service and storefront connector
  profiles:
    - apparel-0.2
    - <platform-profile>-0.2
  assessment_method: independent_assessment
  assessed_at: 2026-08-04
  valid_until: 2027-08-04
```

**CDS1000-R006** A claim MUST name the product, service, component or organisational process being assessed.

**CDS1000-R007** A claim MUST list every profile — platform, industry and overlay — included in the assessment.

**CDS1000-R008** A claim MUST state its assessment method as exactly one of the three canonical methods defined in §20: self-attestation, customer assessment or independent assessment.

**CDS1000-R045** A claim and its machine-readable manifest (§26) MUST record the `test_suite_version` and `assessment_method` used, so that the result can be reproduced against the same test definitions.

## 4. Conformance Levels *(normative)*

CDS defines exactly five conformance levels, strictly cumulative:

**Foundation → Structured → Publisher → Verified → Governed**

| Level | Primary capability | Minimum proof |
|---|---|---|
| CDS Foundation | Canonical authority and semantic clarity | Canonical source, ownership, terminology and namespace evidence |
| CDS Structured | Governed classification, attributes and dictionaries | Schema, data types, dictionary controls, validation and facet separation |
| CDS Publisher | Deterministic channel projection and publication | Expected channel state, mappings, preflight and publication records |
| CDS Verified | Downstream observation and field-level reconciliation | Read-back, comparison strategies, verification results and channel health |
| CDS Governed | Sustained ownership, change control and assurance | Owners, policies, audit, incident handling, versioning and recurring review |

**CDS1000-R009** A higher-level claim MUST satisfy all mandatory tests of every preceding level. No profile — platform, industry, overlay or organisational — may exempt an implementation from this rule or weaken any core requirement. There is no exception process for level cumulativity.

**CDS1000-R010** An implementation MAY claim different levels for different components if the scope of each claim is explicit.

*Informative notes:*
- A PIM implementation might be CDS Structured while its channel connector is CDS Verified. This is preferable to an inflated claim covering both.
- Governance is deliberately the capstone: a team may prove Publisher and Verified round-trip value before formalising full change-control and audit governance (ADR-D1).
- Superseded drafts of CDS-800 defined a different ladder in which "Governed" was level 2 and permitted profiles to relax cumulativity. That ladder and its escape clause are deleted; any prior claim using it must be restated against this section.

## 5. Overlay Profiles *(normative)*

An overlay profile binds an additional test suite to a claim without being a level. Overlays are claimed alongside a level and appear in the claim's `profiles` list.

| Overlay profile | Binds test suite | Additional bound controls | Minimum level |
|---|---|---|---|
| AI-Assured | T-AI (§17) | CDS-700 normative controls for proposal status, provenance, approval and publication boundary | CDS Structured |
| CX | T-UX (§16) | CDS-600 facet and navigation requirements within the declared storefront scope | CDS Foundation |
| Multi-Tenant | T-TEN (§18) | CDS-800 §22 tenant-isolation requirements | CDS Foundation |

**CDS1000-R039** An overlay profile claim MUST name the overlay, its version and the level alongside which it is claimed, and MUST pass every mandatory test in the bound suite in addition to all mandatory tests of the claimed level.

**CDS1000-R040** The AI-Assured overlay MUST NOT be claimed below CDS Structured, because T-AI tests presuppose governed attribute definitions and dictionaries for AI output to conform to.

**CDS1000-R041** A claim that includes customer-facing facet or navigation scope MUST bind the CX overlay for that scope; T-UX tests are mandatory only under this overlay.

**CDS1000-R042** An implementation serving more than one organisation from shared infrastructure MUST bind the Multi-Tenant overlay before claiming any level for that shared deployment.

*Informative note:* AI-Assured is not a sixth level (ADR-D1). Implementations without AI enrichment simply do not claim the overlay; their level claims are unaffected.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The T-TEN suite (§18) is newly designed here as a minimal one-test-per-requirement mapping of CDS-800 §22; ADR-D1 assigned the overlay pattern but not the test list. Alternative: a broader penetration-style suite, deferred to a future test-suite version.

## 6. Adoption Maturity Mapping *(informative)*

CDS-1300's adoption maturity model describes organisational progress; it is not a conformance construct. It maps onto the conformance ladder as follows (ADR-D1):

| CDS-1300 maturity level | Conformance ladder equivalent |
|---|---|
| Level 0 — Fragmented | Pre-Foundation (no claim available) |
| Level 1 — Foundation (formerly "Canonical") | CDS Foundation |
| Level 2 — Structured | CDS Structured |
| Level 3 — Publisher | CDS Publisher |
| Level 4 — Verified | CDS Verified |
| Level 5 — Governed | CDS Governed |

CDS-400's cumulative dictionary capability badges — Dictionary Core, Dictionary Facet, Dictionary Channel, Dictionary Round-Trip (renamed from "Dictionary Verified") — are not levels or overlays. They are evidence descriptors carried inside the CDS Structured evidence set, defined in CDS-400.

## 7. Requirement and Test Identification *(normative)*

Every normative requirement and test case has a stable identifier. Requirement identifiers (`CDSnnn-Rmmm`) describe obligations; test identifiers describe a reproducible method for evaluating them.

```text
Requirement:   CDS500-R014
Test:          CDS1000-T-VRF-014
Profile test:  CDS1000-T-<profile>-023
Evidence:      EVID-2026-000184
```

| Prefix | Suite | Bound to |
|---|---|---|
| T-FND | Foundation tests | CDS Foundation |
| T-STR | Structured data tests | CDS Structured |
| T-PUB | Publisher tests | CDS Publisher |
| T-VRF | Verified tests | CDS Verified |
| T-GOV | Governed tests | CDS Governed |
| T-DICT | Controlled dictionary tests | CDS Structured |
| T-UX | Customer experience tests | CX overlay |
| T-AI | AI governance tests | AI-Assured overlay |
| T-TEN | Tenant isolation tests | Multi-Tenant overlay |

Each platform or industry profile in CDS-900 registers its own test prefix in its versioned profile test matrix (Appendix A).

**CDS1000-R011** Test identifiers MUST remain stable after publication. Substantive changes to test meaning require a new identifier or a new test-suite version.

**CDS1000-R012** Every mandatory requirement in the CDS corpus MUST map to at least one test case or a documented inspection procedure.

*Informative note:* the corpus-wide retrofit of `CDSnnn-Rmmm` requirement identifiers is complete in v0.2 (finding SYS-2 resolved); every chapter now carries stable IDs, so this traceability mandate is implementable across the whole standard.

## 8. Test Categories *(normative)*

| Category | Method | Typical evidence |
|---|---|---|
| Static schema | Inspect definitions and configuration | Schema export, namespace registry, dictionary definitions |
| Data sample | Evaluate representative records | Product export, variant records, mapping outputs |
| Behavioural | Trigger a workflow and observe the result | API logs, before/after states, job records |
| Round-trip | Publish, read back and compare | Expected state, observed state, comparison result |
| Negative | Provide invalid or unknown data | Validation error, quarantine record, rejected publication |
| Security and governance | Inspect permissions and approvals | Role matrix, audit history, change record |
| Human factors | Review visible labels and operational clarity | UI capture, field list, task observation |
| Performance | Measure defined operational limits | Timing log, batch result, retry behaviour |

**CDS1000-R013** A test suite SHOULD include positive, negative and boundary cases where the requirement can fail in materially different ways.

## 9. Test Artefacts and Evidence Package *(normative)*

The evidence package is the durable record supporting a claim. It must allow another qualified reviewer to reproduce or reasonably verify the assessment conclusion. Contents:

- assessment manifest and scope statement
- implementation, test-suite and profile versions
- test-run identifier and timestamps
- test environment description
- input fixtures and expected outcomes
- actual outputs and comparison results
- screenshots or exports for human-inspection tests
- logs for publication, observation and verification
- list of failed, not-tested and not-applicable tests
- exceptions and corrective-action records
- assessor identity or responsible organisation
- cryptographic hashes or checksums for retained files

**CDS1000-R014** Evidence MUST be retained for every mandatory test result included in a claim.

**CDS1000-R015** Evidence MUST identify the implementation version and configuration that was tested.

**CDS1000-R016** Sensitive evidence MAY be redacted, but the redaction MUST NOT remove information necessary to validate the result.

## 10. Foundation Test Suite (T-FND) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-FND-001 | Canonical source exists | Product facts have a declared master and channel read-back is stored separately |
| T-FND-002 | Authority is explicit | Each tested field has exactly one declared authority |
| T-FND-003 | Channel independence | Canonical values remain valid and retrievable with any single channel disabled |
| T-FND-004 | Self-describing fields | Every sampled visible field identifier resolves to a registered namespace and Attribute Definition (CDS-300/CDS-200) with no out-of-band notes required; sample size and selection rule are declared in the assessment scope |
| T-FND-005 | Semantic namespaces | Field prefixes match the approved namespace registry |
| T-FND-006 | Product/variant boundary | SKU-producing differences are variants; descriptive facts are not misused as options |
| T-FND-007 | Classification separation | Internal category, collection and external taxonomy are distinct concepts |
| T-FND-008 | Audit identity | A change can be attributed to an actor or process |

**CDS1000-R017** CDS Foundation conformance requires every mandatory Foundation test to pass.

## 11. Structured Data Test Suite (T-STR) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-STR-001 | Attribute definitions | Every governed attribute has type, scope, cardinality and validation |
| T-STR-002 | Controlled values | Governed enumerations use a dictionary or equivalent reference-data control |
| T-STR-003 | Canonical identity | Dictionary values use stable identifiers independent of display labels |
| T-STR-004 | Source fidelity | Original supplier values are retained when required for provenance |
| T-STR-005 | Facet separation | Facet values are stored distinctly from canonical values for every attribute with a declared facet layer |
| T-STR-006 | Conditional rules | Category- or value-dependent requirements are machine-expressible |
| T-STR-007 | Unknown-value handling | Unmapped values are rejected or quarantined rather than silently accepted |
| T-STR-008 | Units and measurements | Numeric quantities retain declared units and normalisation rules |
| T-STR-009 | Inheritance | Inherited values preserve provenance and can be distinguished from direct values |
| T-STR-010 | Dictionary lifecycle | Aliases, deprecation and replacement are governed |

**CDS1000-R018** CDS Structured conformance requires Foundation conformance plus all mandatory Structured tests, including the Controlled Dictionary Test Suite (§15).

## 12. Publisher Test Suite (T-PUB) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-PUB-001 | Expected state generation | The system calculates an expected channel representation before publishing |
| T-PUB-002 | Mapping determinism | The same canonical input and mapping version produce the same expected output |
| T-PUB-003 | Preflight validation | Invalid or incomplete output is blocked before transport |
| T-PUB-004 | Publication record | Each attempt records product, channel, revision, status and timestamps |
| T-PUB-005 | Replace semantics safety | Full-replace operations preserve governed values and remove stale generated values |
| T-PUB-006 | Partial failure handling | Field or object failures are visible and not reported as complete success |
| T-PUB-007 | Retry safety | Retries do not create duplicate or contradictory downstream records |
| T-PUB-008 | Override governance | Channel overrides are explicit, scoped and auditable |
| T-PUB-009 | Mapping version trace | Published output identifies the transformation or mapping version |
| T-PUB-010 | Disabled publication | A disabled channel or product does not publish unintentionally |

**CDS1000-R019** CDS Publisher conformance requires Structured conformance plus all mandatory Publisher tests.

## 13. Verified Test Suite (T-VRF) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-VRF-001 | Downstream observation | Published values are read back or otherwise observed |
| T-VRF-002 | Expected vs observed separation | Expected and observed values are stored separately |
| T-VRF-003 | Comparison strategy | Each verified field uses a declared type-aware comparison |
| T-VRF-004 | Status distinction | Missing, unobservable, pending and not-applicable verification states are distinguishable per the CDS-500 status enum |
| T-VRF-005 | Mismatch evidence | A mismatch records expected value, observed value and a machine-readable reason code (CDS-500, CDS-1100) |
| T-VRF-006 | Normalised equivalence | Equivalent case, numeric and unordered-list representations can pass correctly |
| T-VRF-007 | Drift detection | Manual or external downstream changes are detected |
| T-VRF-008 | Channel health | Health reporting is derived from detailed verification results |
| T-VRF-009 | Timestamp integrity | Last publish, last observe and last verify times are separately recorded |
| T-VRF-010 | Repair policy | Automatic repair, alert or accepted override is governed and auditable |

**CDS1000-R020** CDS Verified conformance requires Publisher conformance plus all mandatory Verified tests.

## 14. Governed Test Suite (T-GOV) *(normative)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-GOV-001 | Domain ownership | Every governed domain has an accountable owner |
| T-GOV-002 | Change control | Schema, dictionary, namespace and mapping changes follow an approved process |
| T-GOV-003 | Versioning | Breaking, additive and corrective changes are distinguishable |
| T-GOV-004 | Deprecation | Retired values and fields have aliases, replacement guidance and dates |
| T-GOV-005 | Access control | Roles follow least privilege and separate approval where required |
| T-GOV-006 | Incident response | Data-quality and publication incidents have detection, ownership and recovery procedures |
| T-GOV-007 | Review cadence | Governance reviews occur at a declared interval |
| T-GOV-008 | Exception expiry | Exceptions are scoped, justified, approved and time-limited (CDS-800 §16) |
| T-GOV-009 | Supplier governance | Supplier mappings and imports are controlled and reviewable |
| T-GOV-010 | Claim governance | Public CDS claims match current assessment scope and status |

**CDS1000-R021** CDS Governed conformance requires Verified conformance plus all mandatory Governed tests.

## 15. Controlled Dictionary Test Suite (T-DICT) *(normative)*

Dictionary tests verify both data integrity and customer-useful projection. This suite is bound to CDS Structured: it is mandatory for every claim at Structured or above.

| Test ID | Fixture | Expected result |
|---|---|---|
| T-DICT-001 | French Navy | Reference preserved; canonical Navy; facet Blue |
| T-DICT-002 | navy / NAVY / Navy | Aliases resolve to one canonical identifier |
| T-DICT-003 | Blue-Green | Ambiguous value is mapped by rule or sent to review |
| T-DICT-004 | 80% cotton, 20% polyester | Composition retained; Cotton and Synthetic facet rules applied explicitly |
| T-DICT-005 | Tasmanian Oak | Canonical Oak; facet Wood; display label may remain Tasmanian Oak |
| T-DICT-006 | Unknown supplier colour | Quarantine or review; no uncontrolled canonical creation |
| T-DICT-007 | Deprecated canonical value | Alias resolves to replacement while history remains auditable |
| T-DICT-008 | Channel vocabulary mismatch | Channel-specific representation is generated without changing canonical identity |

**CDS1000-R022** A dictionary test MUST verify identifiers and relationships, not only visible labels.

**CDS1000-R043** The Controlled Dictionary Test Suite is mandatory at CDS Structured and every higher level; a Structured claim MUST NOT omit it.

## 16. Customer Experience Test Suite (T-UX) *(normative — mandatory under the CX overlay)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-UX-001 | Facet size control | Each assessed facet exposes no more values than the maximum declared for its facet family in the assessment scope, and every exposed value is a governed facet value rather than a raw source or canonical shade |
| T-UX-002 | Colour family projection | Detailed shades group into usable colour families |
| T-UX-003 | Truthful availability | Facet counts and product cards reflect available product or variant combinations |
| T-UX-004 | No false zero results | For the filter-combination set and zero-result threshold declared in the assessment scope, misleading empty states do not exceed the threshold. If no combination set and threshold are declared, this test is a WARNING-class advisory: it MUST NOT report PASS and its result MUST NOT support the CX overlay claim |
| T-UX-005 | Progressive disclosure | Long lists collapse or search without hiding essential context |
| T-UX-006 | Accessible labels | Facet names and values remain understandable without colour alone |
| T-UX-007 | Search synonym alignment | Search terms map to the same governed concepts as facets |
| T-UX-008 | Navigation distinction | Navigation categories and filter facets do not duplicate each other unnecessarily |

**CDS1000-R023** A customer-facing facet test MUST evaluate the published experience, not only the PIM configuration.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): T-UX-001 and T-UX-004 use declared-threshold criteria (thresholds set in the assessment scope) rather than fixed universal numbers; the alternative — standard-wide numeric limits — was rejected as arbitrary across industries. Finding 1000-2.

## 17. AI Governance Test Suite (T-AI) *(normative — mandatory under the AI-Assured overlay)*

| Test ID | Objective | Pass condition |
|---|---|---|
| T-AI-001 | Proposal status | AI output is identifiable as a proposal until accepted |
| T-AI-002 | Schema constraint | AI values conform to attribute definitions and dictionaries |
| T-AI-003 | Evidence and provenance | The source evidence, model/workflow version and confidence are retained |
| T-AI-004 | Abstention | Low-confidence or unsupported extraction returns review-required rather than invented data |
| T-AI-005 | Human approval | Required review gates cannot be bypassed accidentally |
| T-AI-006 | Publication boundary | AI does not publish to production outside declared authority |
| T-AI-007 | Regression testing | Model or prompt changes are tested against a benchmark set |
| T-AI-008 | Rights and privacy | Restricted source material and personal data controls are enforced |

**CDS1000-R024** AI tests MUST assess the complete workflow, including validation and approval, rather than only model output quality. The controls under test are defined in CDS-700.

## 18. Tenant Isolation Test Suite (T-TEN) *(normative — mandatory under the Multi-Tenant overlay)*

Each test maps to one of the four tenant-isolation requirements of CDS-800 §22 (finding 800-7 resolved).

| Test ID | Objective | Pass condition |
|---|---|---|
| T-TEN-001 | Tenant data isolation | A cross-tenant read attempt against organisation-specific products, dictionaries, mappings, credentials, exceptions or audit records is denied and the denial is evidenced |
| T-TEN-002 | Shared baseline boundary | Shared baseline definitions and templates are readable, but no tenant-specific value is exposed to or merged into another tenant without recorded explicit authorisation |
| T-TEN-003 | Organisation-scoped operations | An import or bulk action submitted without a declared organisation context is rejected; the same operation with a declared context affects only that organisation's records |
| T-TEN-004 | Cross-tenant administration | Cross-tenant administrative access requires a privileged role and produces a reviewable log entry for each access |

*CDS1000-R042 (defined in §5) applies here: shared deployments must pass all mandatory T-TEN tests before claiming any level.*

## 19. Platform and Industry Profile Test Suites *(normative)*

A platform or industry profile adds profile-specific tests to the applicable core level. It may constrain mappings, capability declarations and observation methods; it cannot weaken core requirements (CDS1000-R009, CDS000-R011).

Profile test content — including test matrices, expected platform outputs and observation methods — lives with the versioned, dated profile definitions in CDS-900 (platform) and CDS-1500 (industry), not in this chapter (see Appendix A).

**CDS1000-R025** A profile conformance claim MUST pass all mandatory core tests for the claimed level and all mandatory tests in that profile's version-pinned test matrix.

*Informative note — typical profile test areas:* commerce-platform profiles cover taxonomy mapping, variant constraints, structured metadata definitions, tag/collection safety under full-replace semantics, storefront facet exposure, API read-back and drift handling; feed-destination profiles cover taxonomy and identifier mapping, field validation, disapproval handling and observed item-state reconciliation; supplier-import profiles cover source identification, delta/full behaviour, normalisation, duplicate detection, unknown-value quarantine and provenance; apparel and homewares profiles cover colour, size, fit, composition, materials, dimensions, units and facet truthfulness.

## 20. Reference Test Vectors *(informative)*

Reference vectors are small, portable records with known expected outcomes, usable in automated tests and demonstrations. Core vectors state **canonical and facet expectations only**; platform-specific expected outputs (e.g. a channel's filter value or feed colour) live in the version-pinned profile test matrices (finding 1000-4), because they change with platform API versions while canonical expectations do not.

### 20.1 Apparel product

```yaml
input:
  product_type: shirt
  supplier_colour: French Navy
  material_text: 100% Linen
  variants:
    - { size: S, colour: French Navy }
    - { size: M, colour: French Navy }
expected:
  canonical_colour: navy
  facet_colour: blue
  canonical_material: linen
  verification_case_rule: case_insensitive
# Channel-specific expectations for this vector are defined in each
# profile's version-pinned test matrix (CDS-900 / CDS-1500).
```

### 20.2 Homewares product

```yaml
input:
  product_type: cushion
  supplier_material: Tasmanian Oak buttons and linen cover
  dimensions: 50 x 50 cm
expected:
  canonical_materials: [linen, oak]
  material_facets: [textile, wood]
  dimension_width: 50 cm
  dimension_height: 50 cm
  room_facets: determined_by_governed_rule_or_review
```

### 20.3 Verification equality

```yaml
expected: [Cotton, Linen]
observed: [linen, cotton]
comparison: unordered_list + case_insensitive + dictionary_identity
result: MATCH
```

## 21. Test Outcomes *(normative)*

A test result takes exactly one of six outcomes. Spellings are the canonical underscore forms (ADR-D3 alignment). Test outcomes are distinct from field-level verification statuses, whose single normative home is CDS-500.

| Outcome | Meaning | Effect on claim |
|---|---|---|
| PASS | Mandatory condition is satisfied with evidence | Supports conformance |
| FAIL | Mandatory condition is not satisfied | Blocks the applicable level/profile claim |
| WARNING | Non-mandatory guidance or quality concern | Does not block the claim but MUST be reported |
| NOT_APPLICABLE | Requirement genuinely does not apply to the declared scope | Allowed only with documented rationale |
| NOT_TESTED | No valid test result exists | Blocks the claim when the test is mandatory |
| INCONCLUSIVE | Evidence is insufficient or contradictory | Treated as not passed until resolved |

**CDS1000-R026** A conformance claim MUST NOT be made for a level or profile while any of its mandatory tests has a result of FAIL, NOT_TESTED or INCONCLUSIVE.

**CDS1000-R027** NOT_APPLICABLE requires a written scope-based justification and reviewer approval.

## 22. Nonconformity, Exceptions and Corrective Action *(normative)*

A nonconformity is a failed mandatory requirement. An exception (defined in CDS-100; governed by CDS-800 §16) is a time-limited, documented, approved acknowledgement that the implementation does not currently satisfy a requirement. An exception acknowledges non-conformance; it never converts failure into conformance.

An exception record contains:

- identifier and affected requirement
- description and evidence
- risk and affected records/channels
- responsible owner
- corrective action and target completion date
- temporary control
- approval and expiry date
- retest result

**CDS1000-R028** An exception MUST NOT be used to claim conformance to a level or profile whose mandatory capability is absent. This rule is absolute; no CDS release, profile or exception class relaxes it.

**CDS1000-R029** Corrected nonconformities MUST be retested using the same or a stronger test method.

## 23. Assurance Methods: Self-Attestation and Independent Assurance *(normative)*

The three assurance methods below are the canonical vocabulary for the entire standard; CDS-800's claims-governance requirements cite this section (finding 800-5 resolved).

| Method | Description | Claim wording |
|---|---|---|
| Self-attestation | The implementing organisation performs and records its own assessment | "Self-attested CDS Verified conformance" |
| Customer assessment | A customer or contracting party evaluates the implementation | "Customer-assessed against CDS Publisher" |
| Independent assessment | A qualified party independent of implementation delivery performs the assessment | "Independently assessed CDS Governed conformance" |

**CDS1000-R030** The assurance method MUST be disclosed wherever a conformance claim is presented.

**CDS1000-R031** Independent assessment MUST include evidence sampling, assessor independence and conflict-of-interest disclosure.

## 24. Certification Framework *(normative)*

CDS-1000 provides a future-ready certification structure but does not designate a certification body.

**CDS1000-R044** Any organisation offering CDS certification MUST publish its assessor-competence, impartiality, surveillance, complaint and certificate-withdrawal processes.

**CDS1000-R032** A certificate MUST identify its issuer, scope, CDS version, level, profiles, issue date, expiry date and public verification reference.

**CDS1000-R033** A certification mark MUST NOT imply endorsement of product quality beyond the assessed CDS conformance scope.

## 25. Versioning and Reassessment *(normative)*

Conformance can be invalidated by changes to the system, schema, mappings, dictionaries, channel API behaviour, governance or the CDS specification itself.

| Change | Minimum response |
|---|---|
| Patch implementation release | Risk review and targeted regression tests |
| New attribute or dictionary values | Structured-data tests for affected domains |
| Mapping change | Publisher and Verified tests for affected fields/channels |
| New platform API version | Platform profile regression and observation review |
| Major architecture change | Full reassessment of affected level and profiles |
| New CDS minor version | Gap analysis and tests for new/changed requirements |
| New CDS major version | Formal reassessment before using the new-version claim |

**CDS1000-R034** A claim MUST be reviewed after any change that could alter a mandatory test outcome.

**CDS1000-R035** A claim SHOULD include an expiry or reassessment date.

## 26. Machine-Readable Conformance Manifest *(normative)*

A machine-readable manifest enables automated reporting, procurement checks and public verification. This chapter owns the manifest's semantics; its JSON Schema is published in CDS-1100 (finding 800-6: the former CDS-800 Appendix D template is a pointer to this section). JSON or YAML may be used, provided the required semantics are preserved.

```yaml
cds_conformance:
  specification_version: "0.2"
  test_suite_version: "0.2"
  level: verified
  scope_id: product-information-service-connector
  profiles:
    - <platform-profile>-0.2
    - apparel-0.2
    - ai-assured-0.2
  assessment_method: independent_assessment
  assessed_at: 2026-08-04T09:00:00+10:00
  valid_until: 2027-08-04
  results:
    passed: 86
    failed: 0
    warnings: 4
    not_applicable: 7
    not_tested: 0
    inconclusive: 0
  evidence_package_hash: sha256:...
  public_report: https://example.invalid/cds/assessment-184
```

**CDS1000-R036** The manifest MUST NOT report a conformant level or profile when any mandatory test for that level or profile has a result of FAIL, NOT_TESTED or INCONCLUSIVE.

*(Required fields `test_suite_version` and `assessment_method`: CDS1000-R045.)*

## 27. Reporting and Public Claims *(normative)*

Reports should be understandable to both technical and non-technical readers. Detailed evidence may remain private, while the public summary states scope, result, limitations and assurance method.

```text
Conformant claim:
"Product Information Service 4.2 is independently assessed as conformant with
Commerce Data Standard v0.2 at the CDS Verified level for the Apparel v0.2
profile and the AI-Assured v0.2 overlay. Scope excludes inventory and order
management. Assessment date: 4 August 2026."

Nonconformant claim:
"CDS certified"   # invalid: no version, scope, level, profile, issuer or method
```

**CDS1000-R037** Public claims MUST be precise enough that a reader can determine what was assessed and what was excluded.

**CDS1000-R038** Expired, withdrawn or superseded claims MUST be removed or visibly marked.

## 28. Decision Records *(informative)*

Architecture decisions are held in the single global ADR register (CDS000-R006). Decisions governing this chapter: **ADR-D1** (one cumulative ladder owned by CDS-1000; governance as capstone; AI-Assured, CX and Multi-Tenant as overlay profiles; T-DICT bound to Structured; assurance vocabulary and claim/manifest ownership here), **ADR-D3** (status-enum spellings; verification statuses homed in CDS-500), **ADR-D5** (single corpus release version; casing of enum values). The chapter-local records CDS-ADR-1000-001..007 from v0.1 (cumulative levels; pass/fail mandatory tests; version- and scope-specific claims; self-attestation with disclosure; warnings separated from conformance; machine-readable manifest; no in-spec certification body) are subsumed into the global register unchanged in substance.

---

## Appendix A — Profile Test Matrices *(informative)*

Version-pinned profile test matrices — including all platform-specific expected outputs formerly embedded in this chapter's reference vectors and Shopify appendix — are published alongside each profile definition (CDS-900 for platforms, CDS-1500 for industries). Each matrix pins: the profile version, the platform API version and date verified, the registered test prefix, the mandatory test list, and the profile-specific expected outputs for the shared core reference vectors (§20). A representative matrix covers: product identity mapping, taxonomy mapping, structured metadata definitions, variant boundaries, tag/collection safety, storefront filter exposure, observation method, verification comparison and drift handling.

## Appendix B — Apparel and Homewares Reference Dataset *(normative)*

Implementations must demonstrate more than a single happy path.

**CDS1000-R046** A test dataset used to support a conformance assessment MUST include negative and non-happy-path cases, covering at minimum: an unknown supplier value requiring quarantine, a deprecated alias resolving to a current canonical value, and a deliberate downstream manual edit that must produce detected drift.

The reference dataset SHOULD additionally contain:

- an apparel product with multiple size and colour variants
- colour values French Navy, Sky Blue, Royal Blue and Teal with controlled facet grouping
- an unordered multi-material composition
- a homewares product with dimensions and explicit units
- a homewares product with multiple materials and one dominant display material
- a product whose internal category maps differently to two external taxonomies
- a product with a deliberate channel title override

## Appendix C — Example Evidence Package *(informative)*

```text
assessment-184/
  manifest.yaml
  scope.md
  environment.yaml
  results/
    T-FND-001.json
    T-STR-001.json
    T-PUB-001.json
    T-VRF-001.json
    ...
  fixtures/
    apparel-shirt.json
    homewares-cushion.json
  exports/
    attribute-definitions.json
    dictionaries.json
    namespace-registry.json
  logs/
    publication.ndjson
    observation.ndjson
    verification.ndjson
  screenshots/
    storefront-filters.png
    channel-health.png
  exceptions/
    none.md
  report.pdf
  checksums.sha256
```

---

*End of CDS-1000 v0.2 Review Draft.*


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1100 — Reference Schemas and Machine-Readable Contracts

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-1100 Working Draft v0.1 |
| Normative status | §§1, 3–23 and Appendix A are normative. §2, §§24–26 and Appendices B–D are informative. |
| Findings addressed | CDS1100-1 through CDS1100-24; ADR-D3, ADR-D4, ADR-D5; open decisions D14 (via CDS-700 §6) and D21 |
| Dependencies | CDS-000 through CDS-1000; reference schema package CDS-1200 v0.2.1 |
| Audience | PIM developers, commerce platform engineers, connector authors, data architects, test-tool developers, AI workflow designers |

**Single-home notice.** CDS-1100 is the sole normative home for: the machine-readable document contracts, the common document envelope, the schema identifier and schema-versioning scheme, the extension-key grammar for document envelopes, the validation-output contract and the **CDS_\* reason-code registry** (§21). This chapter *encodes* — and never redefines — semantics owned elsewhere: verification statuses, detailed statuses and the traffic-light mapping are owned by CDS-500 §17–18; conformance levels, test suites and claims by CDS-1000; AI review rules by CDS-700; dictionaries and value layers by CDS-400; visible field-identifier namespaces by CDS-300; terminology by CDS-100 (CDS000-R005).

**Relationship to the shipped package.** Every schema this chapter describes exists in the CDS-1200 Reference Package v0.2.1 (`schemas/`, 21 schemas at schema version 0.2.0). Where this chapter states what a schema requires, the statement has been checked against the shipped schema text. The published specification governs where package and prose conflict (CDS-1200 README), but as of v0.2 no such conflict is known.

---

## 1. Purpose and Scope *(normative)*

CDS-1100 defines the machine-readable contracts that represent the entities and lifecycle records specified by the Commerce Data Standard. It translates the architectural language of products, attributes, dictionaries, channel projections, observations and verification into interoperable documents that software can validate and exchange.

This chapter defines logical contracts and their reference JSON Schema expression. It does not prescribe a database engine, API style, message broker, programming language or storage topology. A relational, document, graph, event-stream or spreadsheet-backed implementation MAY conform if its exported and consumed documents satisfy these contracts.

**CDS1100-R001** A CDS machine-readable document MUST declare its document type, schema identifier, corpus release version, document identifier and revision (the envelope, §5).

**CDS1100-R002** An implementation MUST validate externally exchanged CDS documents against the applicable schema and profile constraints before accepting them as authoritative input.

**CDS1100-R003** A serialization or API transport MUST NOT alter the semantic meaning, type or precision of a CDS value.

## 2. Contract Design Principles *(informative)*

- **Explicit over inferred.** Types, identifiers, scopes and authorities are declared, never guessed from labels or field order.
- **Stable identity.** Business identity is separate from labels, array positions and channel identifiers.
- **Composable contracts.** Shared definitions (envelope, localised text, measurement, money, entity reference) are referenced, not copied.
- **Human-readable payloads.** Keys and enumerations remain understandable to operators and reviewers.
- **Strict core, governed extension.** Core property sets are complete and closed; extension points are namespaced and governed (§20).
- **Canonical and observed separation.** Authoritative values never share storage locations with downstream read-back values (CDS-200, CDS-500).
- **Validation before mutation.** Invalid input is rejected or quarantined before it changes canonical state (CDS-400 §17).
- **Evidence by design.** Publication and verification contracts retain revisions, versions, hashes and comparison evidence.
- **Round-trip safety.** Serializing and parsing preserves identifiers, values, units, significant order and null semantics.
- **AI containment.** AI outputs are proposals, distinct from accepted canonical values (CDS-700).

**CDS1100-R004** A contract MUST distinguish absent, explicitly null, empty string, empty list and zero wherever those states have different business meaning.

**CDS1100-R005** A list whose order is semantically significant MUST declare that significance in its Attribute Definition or contract documentation.

## 3. Serialization and Schema Dialect *(normative)*

JSON is the normative interchange syntax for CDS reference contracts. The reference validation language is JSON Schema Draft 2020-12. Implementations MAY provide YAML 1.2-compatible views for human editing (Appendix C) and MAY expose equivalent Protocol Buffers, Avro, XML or database schemas, provided a lossless mapping to the normative JSON contract is documented and tested.

| Concern | CDS baseline |
|---|---|
| Character encoding | UTF-8 |
| JSON Schema dialect | Draft 2020-12, declared via `$schema` |
| Media type | `application/json` or a profile-specific type; APIs SHOULD identify the CDS document type through media type or envelope |
| Date-time | RFC 3339-compatible timestamp |
| Duration | ISO 8601 duration string where needed |
| Language tag | BCP 47-compatible string |
| Country | ISO 3166-1 alpha-2 where a country code is required; display names are separate from codes |
| Currency | ISO 4217 alphabetic code |
| Units | Stable CDS or recognised unit code; value and unit are distinct fields |

**CDS1100-R006** Exchanged JSON MUST be encoded as UTF-8, and reference schemas MUST declare the Draft 2020-12 dialect via `$schema`.

**CDS1100-R007** Timestamps MUST include a timezone (UTC `Z` or an explicit offset). *The shipped schemas enforce this doubly: every date-time property asserts both `format: date-time` and a pattern requiring the offset, so environments that skip format assertion still reject offset-less timestamps.*

**CDS1100-R008** JSON numbers MUST NOT be used for identifiers such as GTIN, SKU, MPN or postal codes; leading zeros and exact textual form are significant, so identifiers are strings.

**CDS1100-R009** Monetary values MUST be represented in a decimal-safe form that guarantees declared precision; binary floating-point rounding MUST NOT silently alter a published amount. The reference money contract is defined in §7.

**CDS1100-R010** Implicit YAML typing MUST NOT change CDS scalar values; YAML representations MUST be converted to the canonical JSON data model before schema validation (Appendix C).

## 4. Schema Package Architecture and Identifiers *(normative — implements ADR-D5)*

The reference package is a registry of independently versioned schemas. Shared primitives live in `common/` and are referenced from entity schemas. The shipped v0.2 layout (21 schemas):

```
schemas/
  common/     envelope, entity-reference, localised-text, measurement, money
  core/       product, variant, attribute-definition
  reference/  dictionary, dictionary-value, category, taxonomy-mapping, facet-definition
  channel/    channel-profile, field-mapping, publication-record,
              observation-record, verification-result
  automation/ ai-proposal
  assurance/  conformance-manifest, validation-output
```

Platform and industry profiles are not schema directories in v0.2: platform-specific constraints live in CDS-900 profiles and industry constraints in CDS-1500, applied by composition (§20). The v0.1 `profiles/` directory sketch is withdrawn.

Three identity layers, per ADR-D5:

1. **Schema identity.** Every schema `$id` is a release-independent URN: `urn:cds:schema:<domain>:<name>` (for example `urn:cds:schema:core:product`). The specification release is *not* part of the URN, so identifiers are stable across releases. The v0.1 `https://schemas.cds.example/v1/...` example URIs are retired.
2. **Schema version.** Every schema carries its own semantic version in a `version` keyword (all shipped schemas: `0.2.0`), bumped by the compatibility rules of §22, independently of chapter prose revisions.
3. **Instance release pinning.** The envelope's `cds_version` is a per-release constant (`{"const": "0.2"}` in the v0.2 package). An instance therefore pins the corpus release it was written against, and a validator can refuse mismatched generations.

**CDS1100-R011** Every published schema MUST have a stable, release-independent `$id` of the form `urn:cds:schema:<domain>:<name>`, independent of any file-system location.

**CDS1100-R012** Every published schema MUST declare its own semantic version in a `version` keyword, distinct from both the corpus release and any document revision.

**CDS1100-R013** A schema package release MUST publish a manifest listing schema identifiers, versions, per-file hashes, and a package-level hash. *(The shipped `package-manifest.json` carries a `schema_registry` inventory and a `package_hash`; its self-hash convention is documented in the CDS-1200 README.)*

**CDS1100-R014** A profile schema MAY add constraints through composition but MUST NOT redefine the meaning of a core property (§20).

*Informative note:* schemas are resolved offline from the registry — the reference validator loads all schemas from the package and resolves `$ref` URNs against that in-memory registry. URNs carry no resolution promise; nothing dereferences them over a network. Registered `https` URIs were deferred until a domain and governance body exist (ADR-D5, revisit at v0.9).

## 5. Common Document Envelope *(normative)*

Every top-level CDS document uses a common envelope (`urn:cds:schema:common:envelope`). The envelope supports routing, validation, audit, multi-tenant labelling and version-specific interpretation without requiring consumers to inspect business fields first.

| Property | Type | Required | Purpose |
|---|---|---|---|
| `cds_schema` | string (URN) | Yes | `$id` of the schema this document conforms to |
| `cds_version` | const `"0.2"` | Yes | Corpus release the document targets |
| `document_type` | string | Yes | Logical entity or lifecycle record type |
| `document_id` | string | Yes | Stable globally unique document identifier |
| `revision` | integer >= 1 or string | Yes | Monotonic entity revision or immutable revision identifier |
| `status` | enum `draft`, `active`, `deprecated`, `archived` | Yes | Document lifecycle state |
| `tenant_id` | string | Optional | Organisation boundary label for multi-tenant implementations (§6) |
| `created_at` | date-time | Yes | Creation timestamp of the logical record |
| `updated_at` | date-time | Yes | Timestamp of the current revision |
| `source_system` | string | Yes | System that produced the document |
| `correlation_id` | string | Optional | Links related import, publish, observe and verify operations |
| `extensions` | object | Optional | Governed extensions; key grammar per §20 |

```json
{
  "cds_schema": "urn:cds:schema:core:product",
  "cds_version": "0.2",
  "document_type": "product",
  "document_id": "prd_shirt_100",
  "revision": 42,
  "status": "active",
  "tenant_id": "org_reference",
  "created_at": "2026-07-18T03:12:10Z",
  "updated_at": "2026-08-03T00:08:17Z",
  "source_system": "cds-reference-package",
  "correlation_id": "job_01K1PUB9"
}
```

*Composition idiom (preserved from v0.1, now safe).* Entity schemas compose the envelope with `allOf: [{$ref: envelope}, {entity properties}]` and close the document with `unevaluatedProperties: false`. In v0.1 this closure was a trap: it forbade properties the prose promised (lifecycle, provenance, reviewer fields). In v0.2 the property sets are complete — every property a contract names is present in its schema — so closure now does what it should: any unnamed property is a defect, not a casualty. (CDS1100-5, CDS1100-23 resolved.)

The envelope `status` enum is the *document* lifecycle. It is deliberately distinct from the dictionary-value lifecycle owned by CDS-400 and from verification statuses owned by CDS-500; the three vocabularies never mix.

**CDS1100-R015** Every top-level CDS document MUST carry the envelope, with all envelope-required properties present.

**CDS1100-R016** `document_id` MUST remain stable across revisions of the same logical record.

**CDS1100-R017** `revision` MUST change whenever any property affecting canonical meaning or downstream projection changes.

**CDS1100-R018** A consumer MUST reject or quarantine a document whose `cds_schema` is unknown or unsupported, unless an explicitly configured forward-compatibility policy applies.

**CDS1100-R019** `cds_schema` MUST equal the `$id` of the schema against which the document is validated. *(The reference validator cross-checks this on every fixture; a mismatch is a validation failure.)*

## 6. Identity, References and Tenancy *(normative)*

CDS distinguishes canonical identifiers, human business keys and downstream identifiers. A product may hold an internal CDS identifier, one or more SKUs, supplier identifiers and channel platform identifiers. These are related but never interchangeable.

| Identifier class | Example | Authority |
|---|---|---|
| CDS entity ID | `prd_shirt_100` | PIM or CDS entity service |
| Business key | `SHIRT-100` | Organisation |
| Variant SKU | `SHIRT-100-NVY-M` | Organisation or inventory authority |
| Supplier SKU | `SUP-829103` | Supplier |
| GTIN | `09338716007824` | Assigned standards authority / brand |
| Channel ID | `gid://shopify/Product/123` | Downstream channel |
| Taxonomy node ID | `aa-1-2-3` | Taxonomy publisher |

Cross-document references use the shared entity-reference contract (`urn:cds:schema:common:entity-reference`): `document_type` + `document_id` required, optional `role` and `tenant_id`.

```json
{ "document_type": "dictionary_value", "document_id": "dictval_colour_navy", "role": "canonical_colour" }
```

**CDS1100-R020** A channel identifier MUST be stored inside a channel identity or mapping structure and MUST NOT replace the canonical CDS entity ID.

**CDS1100-R021** Cross-document references MUST use stable IDs and MUST include the referenced document type. *(v0.1's SHOULD is upgraded: the entity-reference schema requires `document_type`, so the requirement is mechanically enforced.)*

### 6.1 Tenancy — what the schema does and does not guarantee

`tenant_id` is an optional envelope property: it *labels* an organisation boundary, and single-tenant deployments legitimately omit it. Schema validation of one document **cannot** enforce a boundary between documents; tenant isolation is a property of the consuming implementation, not of any JSON Schema.

**CDS1100-R022** A multi-tenant implementation MUST prevent cross-document references from resolving across tenant boundaries unless a governed shared-reference mechanism is explicitly defined. This is an **implementation obligation**: it is not, and cannot be, a schema-level guarantee. Its test coverage is the mandatory T-TEN suite in CDS-1000 §18; the reference runner's SEM-004 check (all related fixture documents share one `tenant_id`) is an illustration of the join, not the enforcement. *(CDS1100-13 resolved by honesty rather than by pretending the envelope enforces it.)*

## 7. Type System and Standard Formats *(normative)*

Attribute Definitions declare the applicable type and constraints; values MUST conform before becoming canonical. The reference value types (the attribute-definition `value_type` enum, shipped):

| CDS type | JSON representation | Key constraints |
|---|---|---|
| `text` | string | Length, pattern, whitespace policy |
| `boolean` | boolean | No string substitutes such as yes/no |
| `integer` | integer | Minimum, maximum, unit where applicable |
| `decimal` | string | Declared scale and rounding mode (decimal-safe) |
| `date` | string | Calendar date, no time component |
| `date_time` | string | Timezone required (R007) |
| `identifier` | string | Pattern and authority required |
| `enum_reference` / `enum_reference_list` | object reference(s) | Must resolve to an active dictionary value; `dictionary_id` required (§10) |
| `measurement` | object | `urn:cds:schema:common:measurement` — string decimal `value` + `unit` |
| `money` | object | `urn:cds:schema:common:money` — string decimal `amount` + ISO 4217 `currency` |
| `localised_text` | array | Items per `urn:cds:schema:common:localised-text` |
| `composition_list` | array | Dictionary references with percentages |
| `object` | object | Nested schema required |

*Rich text is not a v0.2 reference type.* Markup-bearing content is exchanged as `text` under the sanitisation obligations of §23; a structured rich-text contract is deferred.

**Single localised-text model.** All localised values corpus-wide use one shape: an array of `{"language": "<BCP 47 tag>", "text": "..."}` objects. The v0.1 mixture of language-keyed maps (`{"en-AU": "Navy"}`), arrays and bare strings is retired; dictionary-value `canonical_label` and facet `label` are now arrays of localised-text like product content. (CDS1100-15 resolved.) The attribute-definition `label` is an operator-facing plain string in the reference schema; customer-facing labels are the localised ones.

**Measurement.** `{"value": "1.250", "unit": "kg"}` — value is a string decimal, unit a code. The measurement schema is wired into the package: product typed values reference it (`measurement` branch, §7.1), and `measurement` is an attribute-definition value type. It is no longer dead weight (CDS1100-10 resolved).

**Money.** `{"amount": "129.95", "currency": "AUD"}` — amount is a string decimal in **major units**; currency is an ISO 4217 alphabetic code. The shipped schema documents the design call in its `$comment`.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): Money is a string decimal in major units, matching the measurement convention already in the package. Alternative: integer minor units (cents), which avoids scale ambiguity but diverges from every other numeric-as-string-decimal in the corpus. Revisit if a payments-adjacent profile needs exact minor-unit semantics.

**CDS1100-R023** A measurement MUST store the numeric value separately from its unit.

**CDS1100-R024** A localised value MUST identify the language of each translation using the localised-text contract.

### 7.1 Typed attribute values

Canonical product attribute values are constrained to a minimal **typed-value** shape (product schema `$defs/typed_value`): a value is exactly one of

`{dictionary_value_id, percentage?}` | `{text: [localised-text]}` | `{number, unit?}` | `{measurement}` | `{money}` | `{boolean}` | `{identifier}` | `{date_time}`

or a non-empty array of such values. Bare scalars are rejected: `"MF_material": 42` no longer validates (CDS1100-14).

*Deliberate limits.* The typed-value shape is intentionally minimal. It guarantees that every canonical value has a declared representation; it does **not** encode the binding between a specific attribute and its declared `value_type`, cardinality or dictionary — JSON Schema cannot look up an Attribute Definition while validating a product. Enforcing that a value keyed `MF_material` actually is a `composition_list` against `dict_material` remains an implementation obligation (§21.4). The same limit applies to variant `variant_attributes`, which the shipped schema constrains only to an object.

**CDS1100-R025** A canonical attribute value MUST use the typed-value shape (or an array of it), and an implementation MUST additionally validate each value against its Attribute Definition's declared type, cardinality and dictionary before accepting it as canonical.

## 8. Canonical Product Contract *(normative)*

`urn:cds:schema:core:product`. The Product contract represents the logical commercial item: product-level truth, classification, content and references to variants. Channel projections and observations are separate documents (§15–§17).

Required beyond the envelope: `product_id`, `business_key`, `classification` (`product_family_id`, `product_type_id`, `category_id` — all IDs), `content` (localised `title` required; `short_description`, `long_description` optional), `attributes`, `variant_ids`. Optional: `brand_id`, `manufacturer_part_number`, `media` and `relationships` (entity-reference arrays), and the `lifecycle` (`introduction_date`, `end_of_sale_date`, `approval_state`) and `provenance` (`source_type`, `source_reference`, `acquired_at`) groups restored in v0.2 (CDS1100-23).

Attribute keys are validated by the strict semantic-name pattern `^[A-Z][A-Z0-9]*_[a-z0-9]+(?:_[a-z0-9]+)*$` (prefix grammar owned by CDS-300); attribute values use §7.1 typed values.

```json
{
  "product_id": "prd_shirt_100",
  "business_key": "SHIRT-100",
  "classification": {
    "product_family_id": "family_apparel",
    "product_type_id": "type_shirt",
    "category_id": "cat_womens_shirts"
  },
  "content": { "title": [{ "language": "en-AU", "text": "Relaxed Linen Shirt" }] },
  "attributes": {
    "MF_material": [{ "dictionary_value_id": "material_linen", "percentage": "100.00" }],
    "MF_fit": { "dictionary_value_id": "fit_relaxed" }
  },
  "variant_ids": ["var_shirt_100_navy_s", "var_shirt_100_navy_m"]
}
```

**CDS1100-R026** Product attributes MUST be keyed by stable Attribute Definition identifiers conforming to the CDS-300 namespace grammar, never by mutable display labels.

**CDS1100-R027** A product contract MUST NOT embed observed channel values in its canonical attributes object.

**CDS1100-R028** Variant references MUST resolve to sellable-unit records whose parent `product_id` matches the product. *(Executed as reference semantic test SEM-001; see §21.4.)*

## 9. Variant and Sellable Unit Contract *(normative)*

`urn:cds:schema:core:variant`. The Variant represents a separately sellable, inventory-addressable unit. Required beyond the envelope: `variant_id`, `product_id`, `sku`, `option_values` (each `{option, value_id, display?}`), `sellability` (`sellable`, `preorder`, `unavailable`, `retired`). Optional: `barcode_identifiers`, `variant_attributes`.

Barcode identifiers are typed and length-checked per scheme:

| Scheme | Length | Note |
|---|---|---|
| `gtin_8` | exactly 8 digits | |
| `gtin_12`, `upc` | exactly 12 digits | |
| `gtin_13`, `ean` | exactly 13 digits | |
| `gtin_14` | exactly 14 digits | |

Values are strings, so leading zeros are preserved — the positive reference fixture deliberately uses the zero-leading GTIN-14 `09338716007824` (CDS1100-21).

```json
{
  "variant_id": "var_shirt_100_navy_m",
  "product_id": "prd_shirt_100",
  "sku": "SHIRT-100-NVY-M",
  "option_values": [
    { "option": "colour", "value_id": "colour_navy", "display": "French Navy" },
    { "option": "size", "value_id": "size_m", "display": "M" }
  ],
  "barcode_identifiers": [{ "scheme": "gtin_13", "value": "9338716007824" }],
  "sellability": "sellable"
}
```

**CDS1100-R029** A variant MUST carry a stable SKU or an explicitly documented alternative sellable-unit key.

**CDS1100-R030** Option values MUST reference controlled values (`value_id`) when a dictionary exists for that option; display strings are presentation only.

**CDS1100-R031** A barcode identifier MUST declare its scheme, MUST be represented as a string preserving leading zeros, and MUST satisfy the exact digit length of its scheme.

**CDS1100-R032** Inventory quantity SHOULD remain owned by the declared inventory authority and MAY be referenced rather than duplicated into the canonical record (per-fact authority: CDS-200).

## 10. Attribute Definition Contract *(normative)*

`urn:cds:schema:core:attribute-definition`. Attribute Definitions carry the schema intelligence of CDS: what a value means, where it applies, how it is validated, displayed, faceted, compared and proposed by AI. Required beyond the envelope: `attribute_id` (semantic-name pattern), `label`, `scope` (`product`, `variant`, `category`, `channel`, `system`), `value_type` (§7 table), `cardinality` (`{minimum, maximum|null}`), `behaviour` (`filterable`, `searchable`, `displayable`, `comparison_strategy` — all required). Optional: `description`, `dictionary_id`, `channel_mappings` (entity references).

```json
{
  "attribute_id": "MF_material",
  "label": "Material",
  "scope": "product",
  "value_type": "composition_list",
  "dictionary_id": "dict_material",
  "cardinality": { "minimum": 1, "maximum": 10 },
  "behaviour": {
    "filterable": true, "searchable": true, "displayable": true,
    "comparison_strategy": "unordered_composition"
  }
}
```

**CDS1100-R033** An Attribute Definition MUST declare scope, value type, cardinality and behaviour (including a comparison strategy for every attribute that participates in downstream verification).

**CDS1100-R034** An Attribute Definition whose `value_type` is `enum_reference` or `enum_reference_list` MUST declare `dictionary_id`. *(Mechanically enforced by if/then in the shipped schema; CDS1100-16.)*

**CDS1100-R035** Attribute labels MAY change and be localised at the display layer without changing `attribute_id`.

## 11. Dictionary Definition and Value Contracts *(normative)*

`urn:cds:schema:reference:dictionary` and `urn:cds:schema:reference:dictionary-value`. CDS separates the Dictionary Definition (name, purpose, `value_type` flat/hierarchical, `default_locale`, `governance_owner`, `dictionary_version` — all required) from its Values. Value semantics, lifecycle and governance are owned by CDS-400; this section defines only the machine shape.

Dictionary Value — required beyond the envelope: `dictionary_value_id`, `dictionary_id`, `canonical_code` (lower snake case pattern), `canonical_label` (localised-text array), `aliases` (unique strings), `facet_memberships` (`{facet_id, value_id, primary}`), `channel_representations` (map of channel key to scalar). Optional: `parent_value_id` for hierarchical dictionaries.

```json
{
  "dictionary_value_id": "colour_navy",
  "dictionary_id": "dict_colour",
  "canonical_code": "navy",
  "canonical_label": [{ "language": "en-AU", "text": "Navy" }],
  "aliases": ["navy blue", "french navy", "dark navy"],
  "facet_memberships": [{ "facet_id": "facet_colour_family", "value_id": "facet_blue", "primary": true }],
  "channel_representations": { "google_merchant": "Blue", "shopify_filter": "Blue" }
}
```

**CDS1100-R036** Dictionary Value identity MUST NOT depend on the displayed label or array position.

**CDS1100-R037** Aliases MUST NOT be treated as additional canonical values (intake and quarantine rules: CDS-400 §17).

**CDS1100-R038** Facet memberships MUST reference governed facet values, never arbitrary strings. *(Executed as reference semantic test SEM-002; see §21.4.)*

**CDS1100-R039** Channel representations SHOULD be stored at dictionary or mapping level when they apply consistently across products.

## 12. Classification and Taxonomy Mapping Contracts *(normative)*

`urn:cds:schema:reference:category` and `urn:cds:schema:reference:taxonomy-mapping`. Internal category identity remains stable when external taxonomies change.

Category — required beyond the envelope: `category_id`, `parent_id` (nullable at the root), `name`, `path`, `product_family_id`, `required_attribute_ids`. **`path` is an ordered array of stable ancestor `category_id`s ending with the category's own id** — identifiers, not display labels, so renaming a category never rewrites descendants' paths (CDS1100-15, stable-identity principle).

Taxonomy Mapping — required beyond the envelope: `mapping_id`, `internal_category_id`, `channel`, `taxonomy_version`, `external_node_id`, `mapping_status` (`proposed`, `approved`, `deprecated`, `rejected`), `inherited`.

```json
{
  "mapping_id": "map_cat_womens_shirts_shopify",
  "internal_category_id": "cat_womens_shirts",
  "channel": "shopify",
  "taxonomy_version": "2026-Q3",
  "external_node_id": "aa-1-2-3",
  "mapping_status": "approved",
  "inherited": false
}
```

**CDS1100-R040** An external taxonomy mapping MUST identify the external taxonomy version where the publisher provides one.

**CDS1100-R041** A category `path` MUST consist of stable category identifiers, and a category parent reference MUST NOT create a cycle. *(Acyclicity is graph-level and remains an implementation obligation — §21.4.)*

**CDS1100-R042** A taxonomy remap MUST create a new mapping revision and MUST NOT rewrite historical publication evidence.

## 13. Facet Definition Contract *(normative)*

`urn:cds:schema:reference:facet-definition`. A facet is a customer-experience projection, not merely an attribute flag; facet semantics, UX behaviour, SEO and accessibility rules are owned by CDS-600. Required beyond the envelope: `facet_id`, `label` (localised-text array), `source_attribute_id`, `selection_mode` (`single`, `multi_or`, `multi_and`, `range`), `sort_mode` (`configured`, `alphabetical`, `count`, `numeric`), `value_ids` (unique).

```json
{
  "facet_id": "facet_colour_family",
  "label": [{ "language": "en-AU", "text": "Colour" }],
  "source_attribute_id": "VAR_colour",
  "selection_mode": "multi_or",
  "sort_mode": "configured",
  "value_ids": ["facet_black", "facet_white", "facet_blue", "facet_green", "facet_red"]
}
```

**CDS1100-R043** A customer facet MUST reference a controlled value set (or, for `range` mode, a declared numeric/date range model per CDS-600).

**CDS1100-R044** Facet value order and selection logic MUST be explicit; raw supplier values MUST NOT be exposed as facet values without dictionary governance (CDS-400) and UX review (CDS-600).

## 14. Channel Profile and Field Mapping Contracts *(normative)*

`urn:cds:schema:channel:channel-profile` and `urn:cds:schema:channel:field-mapping`. Channel Profile semantics — capabilities, ownership modes, limits, write semantics — are owned by CDS-500 §5 and §7; platform-specific profile content by CDS-900.

**Field Mapping is a standalone contract in v0.2** (resolving open decision D21 in favour of standalone): `urn:cds:schema:channel:field-mapping`, with all properties required — `source_field`, `target_field`, `source_layer` (`canonical`, `display`, `facet`, `search` — the ADR-D4 value layers), `transformation`, `transformation_version`, `write_mode` (`replace`, `merge`, `append`), `read_back_path` (nullable when the target is not readable), `comparison_strategy`.

A Channel Profile (required: `channel_profile_id`, `channel`, `profile_version`, `capabilities`, `field_mappings`) MAY inline field mappings; each inlined item conforms to the standalone field-mapping contract by `$ref`. **Authority:** the mapping set pinned by a Publication Record's `mapping_set_version` (§15) is authoritative for interpreting that publication; a channel profile's inlined `field_mappings` express the profile's *current* mapping set and are superseded, for historical interpretation, by whatever version the publication record pinned.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D21 (resolved)): Field mapping ships as a standalone envelope-free component schema referenced by channel-profile — standalone won, and the composition keeps one authoritative shape. A top-level *enveloped* "mapping set" document type (independently publishable, revision-controlled) is deferred; today `mapping_set_version` is a version string, not a document reference. Alternative: promote mapping sets to full documents in v0.3.

The shipped capability block is a deliberately minimal core set of four booleans (`supports_readback`, `supports_partial_update`, `supports_variant_attributes`, `supports_structured_metafields`); richer capability declarations (limits, normalisation behaviour, ownership defaults) are profile content per CDS-500 §5 and MAY be carried under `extensions` until standardised.

**CDS1100-R045** A Field Mapping MUST identify source field, source value layer, target field, transformation and transformation version, write mode, read-back path (or its explicit absence) and comparison strategy.

**CDS1100-R046** A mapping target path MUST be interpreted within the named Channel Profile, not as a global CDS path.

**CDS1100-R047** A channel capability declaration MUST distinguish unsupported fields from supported-but-currently-absent values (observation coverage model: CDS-500 §15; encoded in §16).

## 15. Publication Record Contract *(normative)*

`urn:cds:schema:channel:publication-record`. The Publication Record is immutable evidence of what the PIM intended to publish: the expected channel state generated from a specific canonical revision under a specific mapping set. Semantics: CDS-500 §6 and §8–9.

Required beyond the envelope: `publication_id`, `product_id`, `channel_profile_id`, `canonical_revision`, `expected_state`, `publication_status` (`queued`, `preflight_failed`, `published`, `partially_published`, `failed`), `published_at` (nullable until transport), `transport_reference` (nullable), `mapping_set_version`, `payload_hash` (`sha256:` + 64 hex), `preflight_result` (`passed`, `failed`, `not_run`), `transport_status` (`queued`, `sent`, `acknowledged`, `rejected`, `failed`).

The v0.1 conflation of preflight and transport into one status is resolved: **preflight outcome, transport status and overall publication status are three separate properties**, so "valid but rejected by the channel" and "never dispatched because preflight failed" are distinguishable machine states (CDS1100-3).

```json
{
  "publication_id": "pub_shopify_shirt_100_r42",
  "product_id": "prd_shirt_100",
  "channel_profile_id": "chp_shopify_main",
  "canonical_revision": 42,
  "expected_state": { "title": "Relaxed Linen Shirt", "material": ["Linen"] },
  "publication_status": "published",
  "published_at": "2026-08-03T00:10:00Z",
  "transport_reference": "gid://shopify/Product/123456",
  "mapping_set_version": "shopify-1.4.0",
  "payload_hash": "sha256:2af3...",
  "preflight_result": "passed",
  "transport_status": "acknowledged"
}
```

**CDS1100-R048** A Publication Record MUST identify the exact canonical revision and mapping-set version used to produce the expected state. *(Revision pinning is executed as reference semantic test SEM-003; see §21.4.)*

**CDS1100-R049** Transport acknowledgement MUST remain distinct from preflight outcome and from field-level verification status ("acknowledgement is not proof": CDS-500 §9).

**CDS1100-R050** The expected payload's immutable hash MUST be recorded; the full payload MAY be stored externally by reference provided the evidence location is retrievable under CDS-500 §24.

## 16. Observation Record Contract *(normative)*

`urn:cds:schema:channel:observation-record`. The Observation Record stores downstream state read back from a channel. It is evidence, not canonical truth. Observation semantics and the coverage model are owned by CDS-500 §14–15.

Required beyond the envelope: `observation_id`, `publication_id`, `product_id`, `channel_profile_id`, `observed_at`, `coverage`, `observed_state`, `channel_revision` (nullable), `observation_method` (`api_read`, `feed_diagnostic`, `scrape`, `manual`). Optional: `channel_entity_id` (nullable channel-native identity).

`coverage` is **per-field**: two required lists of JSON Pointer paths, `supported` and `unobservable`. This replaces the v0.1 bare description and makes the missing-versus-unobservable distinction machine-checkable — a field absent from `observed_state` but listed in `supported` is *missing*; a field listed in `unobservable` can never be missing (CDS1100-2).

```json
{
  "observation_id": "obs_shopify_shirt_100_001",
  "publication_id": "pub_shopify_shirt_100_r42",
  "product_id": "prd_shirt_100",
  "channel_profile_id": "chp_shopify_main",
  "observed_at": "2026-08-03T00:11:42Z",
  "observation_method": "api_read",
  "coverage": { "supported": ["/title", "/material", "/tags"], "unobservable": ["/search_index_tokenisation"] },
  "observed_state": { "title": "Relaxed Linen Shirt", "material": ["Linen"] },
  "channel_revision": null,
  "channel_entity_id": "gid://shopify/Product/123456"
}
```

**CDS1100-R051** Observation data MUST be stored separately from canonical state and from expected channel state.

**CDS1100-R052** An Observation Record MUST declare its observation method and timestamp.

**CDS1100-R053** The coverage declaration MUST distinguish, per field, a missing value from a field that is unobservable through the selected method.

## 17. Verification Result Contract *(normative — encodes CDS-500 §17, never redefines it)*

`urn:cds:schema:channel:verification-result`. Verification Results compare expected with observed field representations under declared comparison strategies. **All status semantics are owned by CDS-500**: the core enum and detailed statuses by §17, the traffic-light mapping by §18, aggregation by §17.6. This schema encodes them verbatim per ADR-D3.

Required beyond the envelope: `verification_id`, `publication_id`, `observation_id`, `verified_at`, `overall_status`, `field_results`. Optional: `coverage_ratio` (0..1 — observable fraction of contracted fields, CDS-500 §17.6), `comparison_engine_version` (reproducibility), `presentation_status` (`green`, `amber`, `red`, `grey` — informative presentation derived per CDS-500 §18, never a stored status).

Each field result carries:

| Property | Requirement |
|---|---|
| `field_path` | Required. JSON Pointer (RFC 6901) into expected/observed state — replaces the v0.1 bare field name |
| `expected`, `observed` | Required (any type, may be null) |
| `comparison_strategy` | Required; from the CDS-500 §16 registry |
| `status` | Required; the 8-value core enum: `MATCH`, `MISSING`, `MISMATCH`, `PENDING`, `UNOBSERVABLE`, `NOT_APPLICABLE`, `OVERRIDDEN`, `ERROR` |
| `detailed_status` | Optional; the CDS-500 §17.2 detailed set with deterministic rollup to the core status |
| `reason_code` | **Required whenever `status` is not `MATCH`** (schema-enforced if/then); `^CDS_[A-Z_]+$`, from the §21 registry |
| `repair_action` | Optional |
| `message` | Optional free text; never a substitute for `reason_code` (CDS500-R063) |

```json
{
  "field_path": "/material",
  "expected": ["Linen"],
  "observed": [],
  "comparison_strategy": "unordered_text_set",
  "status": "MISSING",
  "detailed_status": "MISSING_DOWNSTREAM",
  "reason_code": "CDS_OBSERVED_EMPTY"
}
```

**CDS1100-R054** The verification-result contract MUST encode the CDS-500 §17 status enum verbatim and MUST NOT introduce, remove or re-map statuses.

**CDS1100-R055** Every field-level result MUST identify its field by JSON Pointer, its comparison strategy and its core status.

**CDS1100-R056** Every field-level result whose core status is not `MATCH` MUST carry a `reason_code` from the §21 registry (encodes CDS500-R063; mechanically enforced by the shipped schema and covered by a negative fixture).

**CDS1100-R057** Traffic-light colour MUST NOT be stored as a verification status; it is presentation derived per CDS-500 §18. *(The package's "uppercase GREEN rejected as a status" negative fixture expresses this.)*

## 18. AI Proposal and Provenance Contract *(normative — encodes CDS-700, never redefines it)*

`urn:cds:schema:automation:ai-proposal`. AI outputs are proposals with evidence and confidence, not canonical values. All AI policy — autonomy levels, review rules, evidence classes, abstention — is owned by CDS-700; this schema encodes the record.

Required beyond the envelope: `proposal_id`, `target_document_id`, `target_field`, `proposed_value` (any type), `confidence` (number 0..1), `evidence` (non-empty array of `{source_type, source_reference, excerpt|null}`), `model_id`, `workflow_version`, `review_state`, `task_type` (`extraction`, `mapping`, `classification`, `writing`, `translation`, `analysis`), `validation_results` (array of §21 validation-output items). Optional: `reviewer` (nullable until reviewed), `accepted_revision` (nullable until accepted).

`review_state` uses the **shared enum** `proposed`, `review_required`, `accepted`, `rejected`, `superseded`, `expired` — identical to CDS-700 §6 (CDS700-R015); CDS-700 and this schema describe the same record, resolving the v0.1 vocabulary split (D14).

```json
{
  "proposal_id": "aip_01K1MAT9",
  "target_document_id": "prd_shirt_100",
  "target_field": "/attributes/MF_material",
  "proposed_value": { "dictionary_value_id": "material_linen", "percentage": "100.00" },
  "confidence": 0.97,
  "evidence": [{ "source_type": "supplier_description", "source_reference": "doc_sup_829103", "excerpt": "100% pure linen" }],
  "model_id": "example-extractor-2",
  "workflow_version": "extract-material-1.3.0",
  "review_state": "proposed",
  "task_type": "extraction",
  "validation_results": []
}
```

**CDS1100-R058** An AI Proposal MUST remain distinguishable from accepted canonical data until an authorised workflow accepts it.

**CDS1100-R059** A proposal MUST identify its evidence, calibrated confidence, model identifier and workflow version, and MUST carry its validation results in the §21 validation-output contract.

**CDS1100-R060** Acceptance MUST create an auditable link from the proposal to the canonical revision it affected (`accepted_revision`, plus the reviewing identity in `reviewer`).

## 19. Conformance Manifest Contract *(normative — encodes CDS-1000 §23, never redefines it)*

`urn:cds:schema:assurance:conformance-manifest`. Conformance levels, test suites, claim rules and manifest semantics are owned by CDS-1000; this schema is their machine expression.

Required beyond the envelope: `manifest_id`, `implementation_name`, `implementation_version`, `claimed_level` (`Foundation`, `Structured`, `Publisher`, `Verified`, `Governed` — the ADR-D1 ladder), `profiles` (unique strings), `test_summary` (`passed`, `failed`, `not_tested`, `inconclusive` — all four counts required), `evidence_uri`, `test_suite_version`, `assessment_method` (`self-attestation`, `customer-assessment`, `independent-assessment`).

**CDS1100-R061** A Conformance Manifest MUST identify the implementation scope and MUST NOT imply conformance beyond that scope (claim rules: CDS-1000 §24).

**CDS1100-R062** The manifest MUST identify the exact test-suite version, the applicable profiles and the assessment method.

**CDS1100-R063** Every executed test case MUST be counted in exactly one `test_summary` disposition; failed or not-executed mandatory tests MUST NOT be omitted. *(The v0.1 fixture that claimed "Verified" with a count contradicting its own evidence report is retired; the shipped fixture counts match the shipped evidence — CDS1100-6.)*

## 20. Extension and Profile Rules *(normative)*

CDS supports platform, industry and organisation extensions without uncontrolled schema fragmentation. Envelope `extensions` keys are constrained by the shipped schema's `propertyNames` pattern to **dotted reverse-namespace form** — `^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$`, e.g. `com.example.photography_status`, `profile.apparel.garment_measurement_set_id` — so namespace governance is mechanically enforced at validation time, not merely urged (CDS1100-12). Visible *field-identifier* prefixes (`MF_`, `VAR_`, ...) are a separate registry owned by CDS-300; the two grammars do not overlap.

```json
"extensions": {
  "com.example.warehouse_zone": "A3",
  "profile.apparel.garment_measurement_set_id": "gms_womens_tops_au"
}
```

**CDS1100-R064** An extension key MUST use the dotted-namespace grammar, and its namespace MUST be organisationally controlled with an identified owner.

**CDS1100-R065** An extension MUST NOT reuse a core property name with a different meaning, and a profile MAY require additional properties, restrict enumerations or tighten validation but MUST NOT make a core mandatory property optional.

**CDS1100-R066** Unknown governed extensions SHOULD be preserved during read-modify-write operations unless an explicit policy authorises removal.

## 21. Validation Output and the Reason-Code Registry *(normative — registry home)*

### 21.1 Validation output contract

`urn:cds:schema:assurance:validation-output` — shipped in v0.2 (it was promised and absent in v0.1; CDS1100-1). A validation finding is machine-actionable and human-readable:

| Property | Requirement |
|---|---|
| `document_id` | Required — the affected document |
| `field_path` | Required — JSON Pointer (RFC 6901) to the instance location |
| `reason_code` | Required — `^CDS_[A-Z_]+$` from the §21.3 registry |
| `severity` | Required — `error`, `warning`, `info` |
| `message` | Optional free text (nullable) |

Validation-output items are embedded by the ai-proposal contract (`validation_results`) and are the recommended shape for import, preflight and API validation responses.

**CDS1100-R067** A validation finding MUST identify the affected document, the instance location as a JSON Pointer, a registered reason code and a severity; severity MUST distinguish errors, warnings and informational findings.

**CDS1100-R068** A rejected import SHOULD retain the original value and source provenance in quarantine rather than discarding it (quarantine model: CDS-400 §17).

### 21.2 Registry governance

**CDS1100-R069** Machine-readable reason codes MUST match `^CDS_[A-Z_]+$` and MUST be drawn from the CDS_* reason-code registry defined here. Additions, deprecations and semantics changes follow CDS-800 change control; a code, once registered, is never reused with a different meaning. Organisation-specific codes are not permitted in the `CDS_` namespace; organisations extend via their own prefix under the CDS-300 extension registry.

### 21.3 Seed registry (v0.2)

Reason codes are a v0.2 design with no legacy precedent (ADR-D3). The seed list below is the initial registry content; CDS-500 Appendix B mirrors the verification subset informatively.

| Reason code | Class | Typical use (detailed status where applicable) |
|---|---|---|
| CDS_OBSERVED_EMPTY | verification | MISSING_DOWNSTREAM |
| CDS_FIELD_NOT_RETURNED | verification | MISSING_DOWNSTREAM or UNOBSERVABLE (CDS-500 §17.4) |
| CDS_INTERFACE_UNSUPPORTED | verification | UNOBSERVABLE |
| CDS_PERMISSION_DENIED | verification | UNOBSERVABLE |
| CDS_STALE_OBSERVATION | verification | UNOBSERVABLE |
| CDS_AWAITING_PROPAGATION | verification | PENDING |
| CDS_PROPAGATION_WINDOW_EXPIRED | verification | post-lapse non-MATCH (CDS-500 §17.5) |
| CDS_EXPECTED_REVISION_AHEAD | verification | STALE_EXPECTED |
| CDS_VALUE_DIFFERS | verification | MISMATCH |
| CDS_UNEXPECTED_VALUE_PRESENT | verification | UNEXPECTED_DOWNSTREAM |
| CDS_IDENTITY_MISMATCH | verification | MISMATCH / drift IDENTITY_MISMATCH |
| CDS_CHANNEL_TRUNCATION | verification | MISMATCH / drift CHANNEL_TRUNCATION |
| CDS_TRANSFORMATION_FAILED | verification | TRANSFORMATION_ERROR |
| CDS_DISPATCH_REJECTED | verification | PUBLICATION_ERROR |
| CDS_READBACK_FAILED | verification | OBSERVATION_ERROR |
| CDS_COMPARATOR_FAILED | verification | COMPARISON_ERROR |
| CDS_WAIVED_EXCEPTION | verification | WAIVED |
| CDS_OVERRIDE_ACTIVE | verification | provenance on OVERRIDDEN results |
| CDS_NOT_IN_CONTRACT | verification | NOT_APPLICABLE |
| CDS_SCHEMA_VALIDATION_FAILED | validation | document fails its declared schema |
| CDS_SCHEMA_UNKNOWN | validation | `cds_schema` unknown or unsupported (R018) |
| CDS_VALUE_NOT_IN_DICTIONARY | validation | value does not resolve to an active dictionary value |
| CDS_VALUE_QUARANTINED | validation | value held in quarantine (CDS400-R054) |
| CDS_REFERENCE_UNRESOLVED | validation | cross-document reference does not resolve |
| CDS_TENANT_BOUNDARY_VIOLATION | validation | reference crosses a tenant boundary (R022) |

### 21.4 Semantic and referential integrity

JSON Schema validates one document at a time. Integrity that spans documents is specified as semantic tests. In v0.2 the reference runner **executes** the semantic catalogue (v0.1 shipped it dead; CDS1100-8):

| Test | Integrity class | Encoding requirement |
|---|---|---|
| SEM-001 | Variant references resolve; parent `product_id` matches | R028 |
| SEM-002 | Facet memberships resolve to configured facet values | R038 |
| SEM-003 | Publication `canonical_revision` equals the product revision projected | R048 |
| SEM-004 | Related documents share one tenant boundary | R022 (illustration) |

The following integrity classes remain **implementation obligations** with no reference-runner check in v0.2: dictionary-reference resolution to *active* values (lifecycle is in the dictionary-value document, not the referencing one); attribute-value conformance to the owning Attribute Definition's type, cardinality and dictionary (§7.1); category-graph acyclicity (R041); taxonomy-mapping resolution against the published external taxonomy; and tenant isolation at the storage and API layer (R022, tested via CDS-1000 §18 T-TEN).

**CDS1100-R070** An implementation MUST enforce the cross-document integrity classes above before accepting a document as authoritative, whether or not a reference-runner check exists for them.

## 22. Versioning and Compatibility *(normative — implements ADR-D5)*

Schema versioning follows the CDS governance model (change control: CDS-800). Per schema: breaking changes require a new major version; additive compatible changes a minor version; corrections that do not change accepted or produced instance meaning a patch version. The `$id` never changes with the version (§4).

| Change | Compatibility expectation |
|---|---|
| Add optional property | Usually backward compatible (minor) |
| Add required property without default/migration | Breaking |
| Remove or rename property | Breaking (rename: unless an alias/migration profile is provided) |
| Tighten enumeration | Potentially breaking |
| Add enumeration value | May break closed consumers; profile policy required |
| Change numeric precision or unit semantics | Breaking |
| Clarify description only | Patch if validation meaning is unchanged |
| Change mapping transformation | Mapping-set version change; no core schema change implied |

**CDS1100-R071** A schema MUST declare its semantic version independently of the CDS corpus release and of any document revision.

**CDS1100-R072** A breaking contract change MUST publish migration guidance and a new major schema version; the schema `$id` MUST NOT change.

**CDS1100-R073** Historical publication and verification records MUST retain the schema versions, `cds_version` and mapping-set versions under which they were created; a corpus release MUST NOT rewrite stored evidence.

*Migration note (informative):* v0.1 URNs of the form `urn:cds:schema:v0.1:*` map one-to-one to the release-independent URNs of §4 for anything already persisted (ADR-D5).

## 23. Security, Privacy and Data Minimisation *(normative)*

Product information is usually less sensitive than customer data, but contracts may carry supplier costs, unpublished products, workflow notes, provenance and user identities.

**CDS1100-R074** Secrets, API credentials and access tokens MUST NOT be embedded in CDS documents.

**CDS1100-R075** A producer MUST publish only the fields required by the destination profile and approved organisation policy; cost and margin fields SHOULD be excluded from channel payloads unless the destination is explicitly authorised.

**CDS1100-R076** Inbound documents MUST be treated as untrusted input and validated for size, recursion depth, markup, URLs and extension content; markup-bearing text MUST be sanitised before render. Schema validation MUST NOT be treated as sufficient security validation.

**CDS1100-R077** Personal reviewer identities SHOULD be represented by governed user IDs and exposed only as policy permits; logs and evidence packages MUST follow retention and access policies (CDS-500 §24, CDS-800).

Cross-tenant reference rejection: R022. External references SHOULD use allow-listed schemes and hosts where automatic retrieval is supported.

## 24. Worked Apparel Contract *(informative)*

Separation of supplier value, canonical value, customer facet, channel representation and verification evidence (four-layer value model: CDS-400; worked end-to-end in the reference fixtures):

```
Supplier input:      colour = "French Navy"; composition = "100% Linen"
Canonical:           VAR_colour -> dictionary_value_id colour_navy
                     (reference form "French Navy" retained per CDS-400 intake)
                     MF_material = [{dictionary_value_id: material_linen, percentage: "100.00"}]
Facet projection:    facet_colour_family = facet_blue; facet_material_family = linen
Shopify expected:    option colour = "French Navy"; metafield colour_family = "Blue";
                     metafield material = "100% Linen"
Google expected:     color = "Blue"; material = "Linen"
Observed Shopify:    option colour = "French Navy"; colour_family = "blue"; material = "100% linen"
Verification:        /options/colour     -> MATCH (exact_text)
                     /colour_family      -> MATCH (case_insensitive_enum)
                     /material           -> MATCH (normalised_composition)
```

Display, canonical, facet and channel values may all differ while remaining correctly mapped and verifiable — that is the point of declared comparison strategies.

## 25. Worked Homewares Contract *(informative)*

A detailed display material coexisting with a broader customer-facing family:

```
Supplier input:      material = "Tasmanian Oak"; finish = "Natural Oil"; dimensions = "45 x 45 x 50 cm"
Canonical:           MF_material = material_oak; MF_material_origin_label (display text)
                     MF_finish = finish_natural_oil
                     MF_width  = {measurement: {value:"45", unit:"cm"}}
                     MF_depth  = {measurement: {value:"45", unit:"cm"}}
                     MF_height = {measurement: {value:"50", unit:"cm"}}
Facets:              material_family = wood; finish_family = natural; room = living_room
Channels:            Shopify material = "Oak"; Google material = "Wood"; PDP display = "Tasmanian Oak"
Verification:        dimensions -> numeric-with-unit comparison
                     material   -> canonical identifier comparison
                     display    -> normalised text comparison
```

Structured measurements are exchanged as separate value-and-unit fields, not as the unparsed display string, whenever the destination supports structured fields (R023).

## 26. Conformance, Package and Decision Pointers *(informative)*

- **Conformance.** Levels, test suites, evidence and claim rules for this chapter's requirements are defined solely in CDS-1000; the machine-readable claim is §19's manifest.
- **Reference package.** The CDS-1200 Reference Package v0.2.1 ships the 21 schemas of Appendix A, positive and negative fixtures, the executed structural and semantic test catalogues, the validation runner and the regenerable manifest. Package composition, runner behaviour and evidence conventions are CDS-1200's subject matter.
- **Decisions.** The v0.1 chapter-local ADR table (CDS-ADR-1101..1110) is superseded by the global ADR register (ADR-D3 statuses and reason codes; ADR-D4 value layers; ADR-D5 identifiers and versioning). Its substance survives as requirements here: JSON + Draft 2020-12 (§3), YAML as a view not a model (§3, Appendix C), the common envelope (§5), canonical/expected/observed/verification separation (§8, §15–17), stable IDs independent of labels (§6, §11), AI-as-proposal (§18), namespaced extensions (§20), payload-by-immutable-reference (§15), stable JSON Pointer error paths (§21).

## Appendix A — Reference Schema Registry *(normative)*

The registry of shipped v0.2 schemas. `$id`s are release-independent (§4); all shipped schema versions are 0.2.0 in this release. This table is regenerated from the package manifest at each release.

| Schema `$id` | Version | Purpose |
|---|---|---|
| urn:cds:schema:common:envelope | 0.2.0 | Common envelope and audit metadata |
| urn:cds:schema:common:entity-reference | 0.2.0 | Typed cross-document reference |
| urn:cds:schema:common:localised-text | 0.2.0 | Language tag plus text |
| urn:cds:schema:common:measurement | 0.2.0 | String-decimal value and unit |
| urn:cds:schema:common:money | 0.2.0 | String-decimal amount and ISO 4217 currency |
| urn:cds:schema:core:product | 0.2.0 | Canonical logical product |
| urn:cds:schema:core:variant | 0.2.0 | Sellable unit |
| urn:cds:schema:core:attribute-definition | 0.2.0 | Attribute schema and behaviour |
| urn:cds:schema:reference:dictionary | 0.2.0 | Dictionary definition |
| urn:cds:schema:reference:dictionary-value | 0.2.0 | Controlled canonical value |
| urn:cds:schema:reference:category | 0.2.0 | Internal taxonomy node |
| urn:cds:schema:reference:taxonomy-mapping | 0.2.0 | External taxonomy projection |
| urn:cds:schema:reference:facet-definition | 0.2.0 | Customer filter definition |
| urn:cds:schema:channel:channel-profile | 0.2.0 | Channel capabilities and mapping carrier |
| urn:cds:schema:channel:field-mapping | 0.2.0 | Canonical-to-channel field transformation |
| urn:cds:schema:channel:publication-record | 0.2.0 | Expected state and transport evidence |
| urn:cds:schema:channel:observation-record | 0.2.0 | Read-back evidence with per-field coverage |
| urn:cds:schema:channel:verification-result | 0.2.0 | Field comparison, statuses and reason codes |
| urn:cds:schema:automation:ai-proposal | 0.2.0 | AI candidate, evidence and review |
| urn:cds:schema:assurance:conformance-manifest | 0.2.0 | Machine-readable conformance claim |
| urn:cds:schema:assurance:validation-output | 0.2.0 | Validation findings with CDS_* reason codes |

The v0.1 registry keys (`cds/common/envelope` style), the `https://schemas.cds.example/...` example URIs, and the unshipped v0.1 sketch entries (`identifiers`, `language`, `provenance` as separate schemas; a `profiles/` schema directory) are retired. Identifier and provenance shapes live inside the entity schemas; language lives in localised-text.

## Appendix B — Illustrative JSON Schema Fragments *(informative)*

Shipped fragments, quoted from the v0.2 package:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:cds:schema:common:measurement",
  "version": "0.2.0",
  "title": "CDS Measurement",
  "type": "object",
  "properties": {
    "value": { "type": "string", "pattern": "^-?\\d+(\\.\\d+)?$" },
    "unit": { "type": "string", "pattern": "^[a-zA-Z][a-zA-Z0-9_./-]*$" }
  },
  "required": ["value", "unit"],
  "additionalProperties": false
}
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:cds:schema:common:entity-reference",
  "version": "0.2.0",
  "title": "CDS Entity Reference",
  "type": "object",
  "properties": {
    "document_type": { "type": "string", "minLength": 1 },
    "document_id": { "type": "string", "minLength": 3 },
    "role": { "type": "string", "minLength": 1 },
    "tenant_id": { "type": "string", "minLength": 1 }
  },
  "required": ["document_type", "document_id"],
  "additionalProperties": false
}
```

Composition idiom (entity schemas):

```json
{
  "$id": "urn:cds:schema:core:variant",
  "allOf": [
    { "$ref": "urn:cds:schema:common:envelope" },
    { "type": "object", "properties": { "...entity properties..." : {} }, "required": ["..."] }
  ],
  "unevaluatedProperties": false
}
```

## Appendix C — YAML Representation Rules *(informative)*

- Quote identifier values that may look numeric: GTINs, SKUs with leading zeros, postal codes.
- Quote date-like values when the intended CDS type is plain text rather than date.
- Do not use YAML tags or implementation-specific object constructors in interoperable CDS files.
- Do not rely on anchors and aliases to create business identity; stable document IDs remain authoritative.
- Convert YAML to the canonical JSON data model before schema validation (R010).
- Preserve mapping keys and list order exactly where order is declared significant.

```yaml
document_type: variant
variant_id: var_shirt_100_navy_m
sku: SHIRT-100-NVY-M
barcode_identifiers:
  - scheme: gtin_14
    value: "09338716007824"
```

## Appendix D — Standards References *(informative)*

| Reference | Location |
|---|---|
| JSON Schema Draft 2020-12 | https://json-schema.org/draft/2020-12 |
| YAML 1.2.2 specification | https://yaml.org/spec/1.2.2/ |
| RFC 3339 — Date and Time on the Internet | https://www.rfc-editor.org/rfc/rfc3339 |
| RFC 6901 — JSON Pointer | https://www.rfc-editor.org/rfc/rfc6901 |
| RFC 8259 — JSON | https://www.rfc-editor.org/rfc/rfc8259 |
| BCP 47 language tags | https://www.rfc-editor.org/info/bcp47 |
| RFC 8141 — URN syntax | https://www.rfc-editor.org/rfc/rfc8141 |

END OF CDS-1100 v0.2 REVIEW DRAFT


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1200 — Reference Implementation, Schema Package and Test Fixtures

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1200 Working Draft v0.1 (and Reference Package v0.1.0) |
| Companion package | CDS-1200 Reference Package v0.2.1 (semver, independent of chapter prose — ADR-D5; schemas remain 0.2.0) |
| Normative status | §1–§2, §4–§16 and §18 are normative except where marked otherwise. §3, §17, §19–§21, Annex A and Appendices A–B are informative. |
| Findings addressed | CDS1200-1..13, PKG-1, PKG-2 (REVIEW-010); ADR-D5 |

A reproducible reference package that turns the CDS machine-readable contracts into executable schemas, fixtures, an executable structural and semantic test suite, and environment-annotated validation evidence.

---

## 1. Purpose and Scope *(normative)*

CDS-1200 defines the executable reference implementation that accompanies the machine-readable contracts in CDS-1100. Its purpose is to make the standard reproducible: implementers obtain the same schemas, run the same fixture suite, observe the same expected failures and produce comparable validation evidence.

The reference implementation is deliberately small enough to read in full, but complete enough to demonstrate the core CDS lifecycle from canonical product records through channel publication, observation and verification (CDS-500). It is not a production PIM, commerce connector or certification service, and it confers no conformance claim by itself (claims: CDS-1000).

**CDS1200-R001** A CDS reference package MUST contain executable schemas, positive fixtures, negative fixtures, a machine-readable expected-results catalogue, a machine-readable semantic test catalogue and a repeatable validation procedure.

**CDS1200-R002** A reference fixture MUST NOT depend on undocumented database state, a network service, the mutable current time or an external API response.

**CDS1200-R003** Where the reference package and the published specification conflict on **normative content** — contract meaning, requirement wording, enumerations, identifier and versioning rules — the specification governs and the package carries the defect. This precedence rule does NOT extend to execution evidence: test reports, result counts and environment records are informative snapshots of a recorded run (§16), never specification prose, and the specification cannot make a non-reproducing number authoritative over an actual run. *(Re-scoped per finding CDS1200-8.)*

## 2. Relationship to CDS-1100 *(normative)*

CDS-1100 specifies the logical contracts and their serialization rules; CDS-1200 packages those contracts into concrete schema files, reusable examples and automated tests. The chapters are complementary, not duplicative. Contract semantics, type rules and extension rules are homed in CDS-1100 and are not restated here.

| CDS-1100 responsibility | CDS-1200 responsibility |
|---|---|
| Define the logical document contracts | Publish executable schema files |
| Define identifier, type and extension rules | Provide conforming and non-conforming examples |
| Define validation and compatibility expectations | Run validation and produce evidence |
| Define the reference schema registry | Distribute the registry as a versioned package |
| Define document semantics | Demonstrate cross-document and lifecycle behaviour |

**CDS1200-R004** The reference package MUST identify the CDS release its contracts implement: the envelope pins `cds_version` as a per-release constant (`"0.2"` for this release), and every schema carries its own semantic version (ADR-D5; details CDS-1100).

**CDS1200-R005** A package release MUST NOT silently change the meaning of a schema without a corresponding specification change or schema version change.

## 3. Reference Implementation Principles *(informative)*

- **Executable:** every claimed schema rule is represented in a validation artefact where the schema language can express it.
- **Reproducible:** a clean environment, with the declared pinned dependencies installed, runs the suite and obtains the same expected outcomes. An environment that cannot enforce a declared assertion fails loudly instead of passing weakly (§5).
- **Deterministic:** fixture IDs, timestamps, values and expected reports are fixed.
- **Inspectable:** schemas and fixtures are readable without proprietary tooling.
- **Layered:** structural schema validation is separated from semantic cross-document tests — and both layers are executed (§12).
- **Positive and negative:** a rule is demonstrated by valid examples and by intentionally invalid counterexamples that fail for the intended reason (§11).
- **Channel-aware:** the package includes an expected publish, observed state and verification chain (§13).
- **Safe:** fixtures contain synthetic data — no real credentials, customer records or confidential supplier data.
- **Portable:** the logical test catalogues are independent of the reference Python runner.
- **Evidence-producing:** a run emits a structured, environment-annotated report rather than only console text.

## 4. Distribution Package Layout *(normative)*

```
CDS-1200_Reference_Package_v0.2/
  README.md
  CHANGELOG.md
  LICENSE.txt
  requirements.txt
  package-manifest.json
  schemas/
    common/  core/  reference/  channel/  automation/  assurance/
  fixtures/
    positive/
    negative/
  tests/
    expected-validation-results.json
    semantic-tests.json
  tools/
    validate.py
    make_manifest.py
  evidence/
    test-report.json        (generated)
```

**CDS1200-R006** A reference distribution MUST keep schemas, fixtures, test catalogues, tools and generated evidence logically separate.

**CDS1200-R007** A consumer MUST be able to identify which files are source artefacts and which are generated evidence. In the reference layout, everything under `evidence/` is generated; everything else is source.

## 5. Dependency Declaration and Environment Integrity *(normative)*

The v0.1 package shipped without a dependency declaration, and its headline evidence claim did not reproduce in a clean environment: JSON Schema Draft 2020-12 treats `format` as annotation-only by default, and the Python format checker silently skips the `date-time` assertion unless the optional `rfc3339-validator` package is installed. A clean run therefore accepted an invalid timestamp fixture (22/23 against a claimed 23/23; REVIEW-010). The v0.2 package closes both the declaration gap and the silent-weakening gap.

**CDS1200-R008** A reference package MUST declare its complete runtime dependencies with pinned versions in a machine-readable file distributed with the package.

**CDS1200-R009** The reference runner MUST verify at startup that every validation capability the suite depends on (including the `date-time` format assertion) is actually enforced in the current environment, and MUST exit non-zero with an actionable message when one is not — it MUST NOT continue with silently weakened validation.

*Informative note.* `requirements.txt` pins `jsonschema==4.26.0`, `referencing==0.37.0` and `rfc3339-validator==0.1.4`. `tools/validate.py` probes a deliberately invalid date-time against a `format: date-time` schema before loading anything; if the probe validates, the runner exits with `FATAL: the 'date-time' format assertion is not enforced in this environment` and the install command. This was proven the same way the original defect was found: in a third clean virtualenv with no dependencies installed, the v0.2 runner refuses to run at all — where the v0.1 runner reported a quietly wrong pass — and with the pinned dependencies installed the full suite reproduces (§17).

## 6. Package Manifest and Integrity *(normative)*

`package-manifest.json` inventories the distributed files with a SHA-256 digest and byte length per file, plus the schema registry inventory (§7). This supports reproducible downloads, release comparison and evidence that a run used the intended artefacts.

The manifest convention *(resolves finding CDS1200-6)*: the manifest lists every package file **except itself and `evidence/`**. The manifest cannot contain its own hash without circularity, and evidence is regenerated per run and instead embeds the manifest's hash (`manifest_sha256` in the report). The manifest's top-level `package_hash` is the SHA-256 over the sorted `"path  sha256"` lines, giving a single package-level integrity value that covers all listed files. The manifest is regenerated with `tools/make_manifest.py`, run *before* the validator so the report embeds the current manifest hash.

**CDS1200-R010** A released package MUST include a machine-readable file manifest with a cryptographic hash for each distributed file, and MUST state its self-exclusion convention.

**CDS1200-R011** The manifest MUST include a single package-level hash derived deterministically from the per-file hashes.

**CDS1200-R012** Generated evidence intended for assurance MUST embed the hash of the package manifest (or an equivalent package release identifier) so the evidence identifies the exact artefacts evaluated. *(Closes finding CDS1200-10: the v0.2 report records `manifest_sha256`.)*

**CDS1200-R013** A validator or assurance process SHOULD verify package hashes before treating results as release evidence.

## 7. Executable Schema Registry *(normative)*

The v0.2 package ships **21 schemas** implementing the registry needed to demonstrate the canonical and publication lifecycle. Each schema declares JSON Schema Draft 2020-12, a release-independent URN `$id` and its own semantic version.

| Domain | Schemas (21) |
|---|---|
| common (5) | envelope, entity-reference, localised-text, measurement, money |
| core (3) | product, variant, attribute-definition |
| reference (5) | dictionary, dictionary-value, category, taxonomy-mapping, facet-definition |
| channel (5) | channel-profile, field-mapping, publication-record, observation-record, verification-result |
| automation (1) | ai-proposal |
| assurance (2) | conformance-manifest, validation-output |

Identifier policy (ADR-D5, homed in CDS-000/CDS-1100; restated here only as it binds the package): `$id`s take the form `urn:cds:schema:<domain>:<name>` with **no release version in the URN**, so identifiers are stable across releases; each schema carries a `version` keyword with its own semver (all `0.2.0` at this release); instances pin the corpus release via the envelope `cds_version` constant. *(Resolves finding CDS1200-13: v0.1's "stable $id" wording contradicted its version-embedded `urn:cds:schema:v0.1:*` URNs.)*

**CDS1200-R014** Every reference schema MUST declare the supported schema dialect, a release-independent `$id` and a per-schema semantic version, per the identifier policy in CDS-1100.

**CDS1200-R015** The package MUST include all referenced schemas required to validate the distributed fixtures without network access, and the manifest MUST inventory the registry (id, version, path).

## 8. Shared Definitions and Composition *(normative)*

Common types are defined once and reused by `$ref`. Entity schemas compose the common document envelope with entity-specific properties, so identifiers, revisions, timestamps and source-system fields behave consistently.

```json
{
  "$id": "urn:cds:schema:core:product",
  "version": "0.2.0",
  "allOf": [
    {"$ref": "urn:cds:schema:common:envelope"},
    {"type": "object", "properties": {"document_type": {"const": "product"}}}
  ],
  "unevaluatedProperties": false
}
```

The envelope requires `cds_schema`, `cds_version`, `document_type`, `document_id`, `revision`, `status`, `created_at`, `updated_at` and `source_system`; `cds_version` is `{"const": "0.2"}` *(resolves finding CDS1200-7 — v0.1 fixtures declared `"1.0"` against an unpinning pattern)*; extension keys are constrained to dotted reverse-namespace form (extension rules: CDS-1100, CDS-300).

**CDS1200-R016** A shared definition MUST have exactly one authoritative schema file within a package release.

**CDS1200-R017** Entity schemas SHOULD close unevaluated top-level properties unless a governed extension point is explicitly provided.

**CDS1200-R018** The reference runner MUST cross-check each instance's declared `cds_schema` against the `$id` of the schema actually applied, and treat a mismatch as a validation error.

## 9. Fixture Design Model *(normative)*

A fixture is a stable document designed to demonstrate one or more contract rules, identified by path, declared schema and expected outcome. Positive fixtures model realistic commerce records; negative fixtures isolate a specific invalid condition.

| Fixture property | Rule |
|---|---|
| Synthetic | No personal, confidential or credential data |
| Minimal but meaningful | Enough business context to explain the rule |
| Stable | No current timestamps, random IDs or live taxonomy lookups |
| Single purpose | A negative case fails for one declared principal reason |
| Self-identifying | The envelope declares document type and schema |
| Traceable | The expected-results catalogue names the schema, expected outcome and, for negatives, the intended error |

**CDS1200-R019** Every fixture MUST have a declared expected validation outcome in the machine-readable catalogue.

**CDS1200-R020** A negative fixture SHOULD isolate one principal violation so that a failed test remains diagnosable.

**CDS1200-R021** Reference fixtures MUST be synthetic and MUST NOT contain live credentials, personal customer information or confidential supplier data.

## 10. Positive Fixture Suite *(normative)*

The v0.2 suite contains **16 positive structural fixtures**. Together they demonstrate the canonical product, controlled dictionary, classification, channel profile and publication assurance chain.

| Fixture group | Demonstrated behaviour |
|---|---|
| Attribute Definitions (2) | Semantic prefix syntax, scope, value type, cardinality, comparison behaviour, dictionary binding |
| Dictionaries (2) | Stable dictionary identity, canonical labels (localised-text form), aliases, facet memberships, channel representations |
| Classification (2) | Internal category path (stable-ID array) and Shopify taxonomy mapping |
| Product and variants (3) | Canonical product truth, typed attribute values, variant options, SKU and zero-preserving GTIN handling |
| Channel profile (1) | Capabilities, field mappings (source layer, write mode, comparison strategy), transformations |
| Publication chain (3) | Expected channel state, observed state, field-level verification (§13) |
| Facets (1) | Facet family definition and configured values |
| AI proposal (1) | Proposed value, evidence, confidence, review state, model and workflow version (rules: CDS-700) |
| Conformance manifest (1) | Declared level, profiles, assessment method, test summary (semantics: CDS-1000 §26) |

**CDS1200-R022** All positive fixtures MUST validate under their declared schemas, and the package MUST include at least one complete canonical product-to-verification lifecycle fixture chain.

## 11. Negative Fixture Suite *(normative)*

The package includes **13 negative fixtures**. Each fails under its declared schema, and — new in v0.2 — each catalogue entry declares the *intended* error via `expected_error_substrings`. Negative tests prove that a validator rejects invalid input for the right reason, not merely that it produced some error.

The mechanism *(resolves findings CDS1200-3 / PKG-2)*: because entity schemas compose the envelope via `allOf` and close with `unevaluatedProperties: false`, any subschema failure in Draft 2020-12 drops property annotations and triggers a blanket "Unevaluated properties are not allowed" cascade error alongside the real one. In v0.1 the runner asserted only "any error", so the suite could not detect loss of the constraint actually under test. The v0.2 runner requires at least one declared intended substring among the reported errors and **excludes the `unevaluatedProperties` cascade line from counting as evidence** — a negative case whose only surviving error is the cascade is a suite failure.

| Negative fixture | Intended principal failure |
|---|---|
| product-missing-product-id.json | Missing required `product_id` |
| envelope-missing-revision.json | Missing required envelope `revision` |
| envelope-bad-status.json | Envelope status not in the controlled enumeration |
| variant-invalid-gtin.json | Barcode contains a non-digit |
| attribute-invalid-semantic-name.json | Field identifier violates CDS semantic prefix syntax (CDS-300) |
| dictionary-value-invalid-code.json | Canonical code is not lowercase snake_case (CDS-400) |
| publication-invalid-status.json | Publication status not in the controlled enumeration (CDS-500) |
| observation-invalid-timestamp.json | Timestamp is not RFC 3339 date-time |
| timestamp-missing-offset.json | Date-time lacks a timezone offset |
| product-attribute-wrong-type.json | Attribute value violates the typed-value shape |
| verification-invalid-status.json | Presentational colour label used where a normative verification status is required (CDS-500) |
| verification-missing-reason-code.json | Non-MATCH field result lacks the required `reason_code` (CDS-500) |
| ai-confidence-out-of-range.json | Confidence exceeds 1.0 (CDS-700) |

**CDS1200-R023** A package MUST contain negative fixtures for required fields, controlled enumerations, semantic identifier syntax, numerical ranges and standard formats where those constraints are normative.

**CDS1200-R024** A validator run MUST be considered failed if a negative fixture unexpectedly validates.

**CDS1200-R025** Each negative catalogue entry MUST declare the intended error (as one or more expected error substrings or an equivalent machine-checkable assertion), and the runner MUST require the intended error to be present, excluding composition-cascade errors from counting as evidence.

## 12. Semantic and Cross-Document Tests *(normative)*

JSON Schema validates a document in isolation. CDS also requires relationships that span documents, revisions and tenant boundaries. These live in a separate machine-readable semantic catalogue (`tests/semantic-tests.json`) and — new in v0.2 — are **executed by the reference runner**, not merely documented. *(Resolves finding CDS1200-4: in v0.1 the semantic catalogue was aspirational, SEM-001 would have failed if run, and the CI narrative listed steps the runner never performed.)*

| Test | Cross-document rule |
|---|---|
| SEM-001 | Product variant references resolve to variants whose `product_id` matches the product |
| SEM-002 | Dictionary value facet membership resolves to a configured facet value |
| SEM-003 | Publication `canonical_revision` equals the product revision used to calculate expected state |
| SEM-004 | All related documents remain within the same tenant boundary |

Scope honesty: SEM-001..004 demonstrate the *mechanism* — a distinct, executed semantic layer over already-validated documents. They are four checks over a small fixture set, not a complete semantic integrity suite. Production-scale referential integrity, authority enforcement and tenancy isolation remain the implementation's obligation, tested under CDS-1000 (for example T-TEN-001 for tenant isolation).

**CDS1200-R026** An implementation MUST NOT represent cross-document or semantic integrity as established merely because each individual document passes structural schema validation. *(Applies equally to this chapter's own evidence: §17 reports structural and semantic counts separately.)*

**CDS1200-R027** A semantic test MUST identify all documents or services required to evaluate the rule.

**CDS1200-R028** The reference runner MUST execute the packaged semantic catalogue, and a run MUST be considered failed when any semantic outcome differs from its declared expectation.

## 13. Publication Assurance Test Chain *(normative)*

The reference apparel fixtures demonstrate the CDS-500 assurance lifecycle using four linked documents, separating canonical revision, expected state, downstream observation and verification evidence. Verification statuses, detailed statuses and traffic-light presentation are homed in CDS-500 and not restated here.

```
prd_shirt_100 revision 42
  -> pub_shopify_shirt_100_r42   expected title, category, material, tags
  -> obs_shopify_shirt_100_001   observed downstream representation
  -> ver_shopify_shirt_100_001   field comparison + overall MATCH
```

The observation returns the same tags in a different order; the declared comparison strategy treats tags as an unordered set, so the verified result remains MATCH.

**CDS1200-R029** A publication assurance fixture MUST preserve the identifiers linking canonical revision, publication, observation and verification result, and MUST keep canonical, observed and verification values in distinct documents.

**CDS1200-R030** A verification fixture MUST declare the comparison strategy used for each compared field.

## 14. Determinism and Reproducibility *(normative)*

A reference suite is useful only when independent implementers can reproduce its results. The package therefore fixes timestamps, revisions, IDs, source systems, channel states and expected reports:

- No fixture calls a live channel or taxonomy service.
- No fixture obtains the current time during validation.
- No test depends on random values or array iteration order.
- All schema references resolve from the local package registry.
- Generated reports use stable case ordering.
- Package and manifest hashes let evidence identify the exact artefacts used.

**CDS1200-R031** A reference fixture MUST be deterministic under the documented comparison and validation rules.

**CDS1200-R032** Where a test requires randomness or time simulation, the seed and clock MUST be explicitly controlled and recorded.

**CDS1200-R033** The packaged validation suite MUST run without network access.

## 15. Reference Validation Runner and CLI Contract *(normative)*

The package contains a small Python runner as an **informative** executable implementation (the standard is language-neutral; §18). A clean run:

1. Verifies that declared validation capabilities are enforced (§5) — else exits FATAL.
2. Loads every schema file and registers it by `$id` in a local registry.
3. Validates each positive fixture and requires no errors; validates each negative fixture, requires errors and requires the intended error substring (§11).
4. Cross-checks `cds_schema` against the applied schema (§8).
5. Executes the semantic catalogue SEM-001..004 (§12).
6. Writes the evidence report, embedding the manifest hash and environment (§16).
7. Exits 0 only when every structural and semantic case matches its expectation.

| CLI behaviour | Contract |
|---|---|
| Default run | Validate the packaged structural and semantic catalogues |
| Report output | Print a structured JSON summary; optionally write the full report to a path |
| Exit 0 | All actual outcomes equal expected outcomes |
| Non-zero exit | Any outcome differs, package loading fails, or a required validation capability is unavailable |
| Offline | All schema references resolve locally |
| Diagnostics | Include fixture, schema, expected, actual, outcome and validator errors |

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python tools/validate.py --write-report evidence/test-report.json
```

**CDS1200-R034** A reference runner MUST return a non-zero process status when any actual outcome differs from the expected outcome or the package cannot be loaded and verified.

**CDS1200-R035** An alternative implementation MAY replace the reference runner if it evaluates the same catalogues and produces equivalent outcomes.

## 16. Validation Evidence and Reporting *(normative)*

Validation evidence is a machine-readable record of the package version, environment, test cases, expected and actual outcomes, and error messages. Evidence is **informative**: it is a snapshot of a recorded run in a recorded environment, never governed prose (§1, CDS1200-R003). Evidence feeding a conformance claim is governed by CDS-1000's evidence-package rules.

| Evidence field | Purpose |
|---|---|
| package_version | Identifies the schema and fixture release |
| generated_at | When the evidence was generated |
| environment | Python version, platform, and pinned dependency versions actually resolved |
| manifest_sha256 | Hash of the package manifest — ties evidence to exact artefacts (CDS1200-R012) |
| summary | Structural and semantic case counts, passed/failed, reported separately and combined |
| fixture / schema_id | Identifies the tested document and governing contract |
| expected / actual / outcome | PASS only when actual equals expected — an intentionally invalid negative fixture passes its test by failing validation |
| detail / errors | Intended-error assertion result and preserved validator diagnostics |

**CDS1200-R036** A validation report MUST distinguish instance validity from test-case outcome.

**CDS1200-R037** Generated evidence MUST identify fixture, schema, expected result, actual result, test outcome and the execution environment (language runtime and dependency versions).

**CDS1200-R038** Structural and semantic results MUST be separately identifiable in the report and its summary.

## 17. Execution Snapshot *(informative)*

The following is the recorded outcome of executing Reference Package v0.2.1 in a clean environment with the pinned dependencies installed. It is an evidence snapshot, not a normative claim (§1); reproducing it requires the recorded environment or a compatible one.

| Metric | Result |
|---|---|
| Schemas | 21 |
| Positive fixtures | 16 |
| Negative fixtures | 13 |
| Structural cases | 29 / 29 as expected |
| Semantic cases (SEM-001..004) | 4 / 4 as expected |
| Total cases | 33 / 33, 0 unexpected outcomes |
| Manifest-listed files | 60 (manifest itself and `evidence/` excluded by convention, §6) |
| Evidence ties | `manifest_sha256` embedded in report; manifest `package_hash` present |

Recorded environment: Python 3.14.7; `jsonschema` 4.26.0, `referencing` 0.37.0, `rfc3339-validator` 0.1.4 (per `evidence/test-report.json`, generated 2026-08-17). In a clean environment *without* the pinned dependencies, the runner exits FATAL at startup rather than reporting a weakened pass (§5) — the failure mode that produced v0.1's non-reproducing 23/23 (REVIEW-010) can no longer occur silently.

## 18. Release Packaging, Versioning and Language Neutrality *(normative)*

The reference package uses semantic versioning independently of chapter prose (ADR-D5). A patch release corrects a fixture or tool without changing schema meaning; a minor release adds backward-compatible schemas or fixtures; a major release introduces incompatible contract changes.

| Change | Package version impact |
|---|---|
| Documentation typo only | Patch |
| Additional positive or negative fixture | Minor, unless it changes a prior expected outcome |
| Backward-compatible optional schema property | Minor |
| New required property | Major |
| Enumeration removal or meaning change | Major |
| Validator bug fix restoring specified behaviour | Patch, with documented evidence change |

**CDS1200-R039** Every package release MUST publish a changelog, a manifest and a test report. *(The v0.2.1 release ships all three; v0.2.0 first closed finding CDS1200-5, under which the v0.1 release failed its own rule.)*

**CDS1200-R040** A fixture outcome change between releases MUST be explained as a standard correction, a test correction or an intentional compatibility change.

**CDS1200-R041** Conformance MUST be determined by documented outcomes against the packaged catalogues, not by use of a particular programming language or library. Python is used only for the initial informative runner; any language may host an equivalent implementation (CDS1200-R035).

> RESOLVED (was D27 (resolved), owner decision 2026-08-04, research REVIEW-006A): dual licence adopted — **Apache-2.0** for machine-readable artifacts (schemas, fixtures, tests, tools, manifests; express patent grant) and **CC-BY 4.0** for specification prose, matching prevailing open-standard practice (OpenAPI, AsyncAPI, CloudEvents use Apache-2.0; W3C separates document and software licences). `LICENSE.txt` declares the split; `LICENSE-CODE.md` and `LICENSE-SPEC.md` contain the full terms; tools carry SPDX headers. The distribution blocker recorded in the original v0.2 draft was closed on 2026-08-17.

## 19. Implementation Guidance: CI, Release Discipline and Code Generation *(informative)*

The v0.1 draft stated several MUSTs regulating adopters' internal CI pipelines, release processes and generated model classes — untestable against this package and out of its scope *(finding CDS1200-9)*. They are retained here as guidance with their normative homes cross-referenced:

- **Run the suite on change.** A maintained implementation should run the reference fixture suite whenever schemas, mappings, serializers or validators change, and should not release a schema change that causes an unexplained change to a golden fixture outcome. (Release evidence obligations for the *package itself* remain normative in §18; conformance testing obligations: CDS-1000.)
- **Reference CI shape.** checkout package → verify manifest → validate schema metaschemas → run structural suite (positive + negative) → run semantic tests → compare evidence summary → publish report and artefact hashes. Unlike v0.1, every step listed here is one the reference runner actually performs, except metaschema validation and hash verification, which `make_manifest.py` and standard tooling cover.
- **Multi-tenant testing.** Production assurance suites should verify that cross-tenant references cannot resolve without an explicit governed sharing mechanism; the normative tenant-isolation test is CDS-1000 T-TEN-001, and SEM-004 demonstrates only the single-boundary fixture case.
- **Code generation.** Generated model classes should preserve unknown governed extensions and CDS scalar semantics when round-tripping documents; the governing serialization and extension rules are CDS-1100's, and round-trip assertions belong to the future suite in §20.
- **Organisation-specific fixtures.** Organisations should add fixtures for known incidents, migrations and channel failure modes; these live alongside, not inside, the reference package.

## 20. Future Work: Round-Trip, Security and Scale Suites *(informative)*

These suites are deliberately out of scope for v0.2 and are stated as future work rather than implied capability.

**Round-trip serialization.** Structural validity does not prove an implementation preserves values when reading and writing. A complete harness should parse, serialize, reparse and compare representative documents with type-aware semantics: GTIN leading zeros and exact textual form; decimal/money scale and value; measurement value/unit separation; ordered arrays vs unordered sets; null vs absent; UTF-8 stability under the declared normalization policy; language-tag association. An implementation claiming safe interchange should pass round-trip tests for every supported CDS type (interchange rules: CDS-1100).

**Security and multi-tenant fixtures.** The public package is synthetic and secret-free (CDS1200-R021). Production assurance additionally needs: cross-tenant reference rejection; quarantine of disallowed script markup; unknown extension namespaces rejected or isolated per policy; fixtures containing credentials blocked from evidence publication; oversized payloads rejected under profile limits; AI proposals unable to mutate canonical state without the required approval transition (CDS-700).

**Performance and scale.** The v0.2 package prioritises correctness. Future releases should add *generated* scale fixtures while preserving a small hand-reviewable core: bounded validation time and memory across small (100 products) to large (1M products, 8M variants) catalogues, wide products, deep taxonomies and large publication batches. Illustrative sizes are not normative performance targets; service-level expectations belong to implementation profiles (CDS-900).

## 21. Adoption by a PIM Project *(informative)*

A PIM project can adopt CDS-1200 incrementally. The package does not force internal database schemas to mirror the JSON documents; it defines stable interchange and assurance boundaries.

1. Map existing product and variant records to the CDS product and variant contracts.
2. Export a small canonical fixture set and validate it.
3. Model existing controlled lists as CDS dictionaries and values.
4. Generate expected channel state for one channel product.
5. Pull the product back into an observation record.
6. Produce a field-level verification result.
7. Add organisation-specific negative fixtures for historical failure modes.
8. Run the suite in CI before connector or schema releases.

*(Steps renumbered from the v0.1 draft's 8–15 — finding CDS1200-11.)*

## 22. Architecture Decision Records *(informative)*

Decisions are held in the single global ADR register (CDS000-R006). Governing this chapter: **ADR-D5** (single corpus release; release-independent `$id` URNs; per-schema semver; envelope `cds_version` const; changelog, pinned dependencies and informative environment-annotated evidence required of the v0.2 package). The chapter-local records CDS-ADR-1200-001..007 from v0.1 are subsumed into the global register unchanged in substance: ship executable artefacts with the prose standard; use JSON Schema Draft 2020-12; separate structural from semantic tests; require positive and negative fixtures; use deterministic synthetic fixtures; treat the Python runner as informative; record package hashes.

---

## Annex A — Organisation Example: Legacy Hosted-Table PIM *(informative)*

An organisation migrating from a hosted-table PIM (for example Airtable) can express its legacy estate directly in package terms: legacy canonical tables and merchandising-fact fields become canonical fixtures; per-channel export tables become observation fixtures; existing match/compare reports become verification fixtures. This turns a migration inventory into an executable regression suite before cutover. The governed migration pathway — including the pre-cutover downstream baseline — is defined in CDS-1300. *(Moved from the v0.1 adoption section per finding CDS1200-12.)*

## Appendix A — Schema and Fixture IDs *(informative)*

| Schema `$id` | Representative fixture |
|---|---|
| urn:cds:schema:core:product | relaxed-linen-shirt.product.json |
| urn:cds:schema:core:variant | relaxed-linen-shirt-navy-s.variant.json, relaxed-linen-shirt-navy-m.variant.json |
| urn:cds:schema:core:attribute-definition | MF_colour.json, MF_material.json |
| urn:cds:schema:reference:dictionary | colour.dictionary.json |
| urn:cds:schema:reference:dictionary-value | colour_navy.value.json |
| urn:cds:schema:reference:category | womens-shirts.category.json |
| urn:cds:schema:reference:taxonomy-mapping | womens-shirts.shopify-mapping.json |
| urn:cds:schema:reference:facet-definition | colour-family.json |
| urn:cds:schema:channel:channel-profile | shopify.channel-profile.json |
| urn:cds:schema:channel:publication-record | shopify-shirt.publication.json |
| urn:cds:schema:channel:observation-record | shopify-shirt.observation.json |
| urn:cds:schema:channel:verification-result | shopify-shirt.verification.json |
| urn:cds:schema:automation:ai-proposal | colour-mapping.ai-proposal.json |
| urn:cds:schema:assurance:conformance-manifest | reference.conformance-manifest.json |

`common/*` (envelope, entity-reference, localised-text, measurement, money), `channel/field-mapping` and `assurance/validation-output` are composed by reference and exercised through every fixture rather than by a dedicated fixture file.

## Appendix B — Reference Commands *(informative)*

```bash
# Unpack the companion package
unzip CDS-1200_Reference_Package_v0.2.zip
cd CDS-1200_Reference_Package_v0.2

# Install pinned dependencies (required; the runner exits FATAL without them)
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run the structural + semantic suite and write evidence
.venv/bin/python tools/validate.py --write-report evidence/test-report.json

# Regenerate the manifest (run BEFORE the validator so evidence embeds the current hash)
.venv/bin/python tools/make_manifest.py
```

---

*End of CDS-1200 v0.2 Review Draft.*


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1300 — Migration, Adoption and Operational Rollout

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1300 Working Draft v0.1 |
| Normative status | §1–§2, §4–§23 are normative except where marked otherwise. §3, §24, Appendices A–C and all worked scenarios are informative. |
| Findings addressed | SYS-3 (D18), 1300-1..14; ADR-D1 (maturity mapping), ADR-D2, ADR-D4, ADR-D24; Matrix 5 (legacy annex, DF_→CH_ consolidation) |

A governed pathway for moving existing commerce data, teams and channels into a CDS-conformant operating model without losing authority, traceability or business continuity.

---

## 1. Purpose and Scope *(normative)*

CDS-1300 defines how an organisation adopts CDS while continuing to operate existing products, channels and business processes. It covers migration from spreadsheets, hosted-table PIMs, legacy enterprise PIMs, channel-first catalogues and mixed estates into a PIM-first CDS architecture.

The chapter governs both technical migration and operating-model transition. A structurally correct database is not a successful migration if staff continue editing authoritative fields in downstream channels, dictionaries remain uncontrolled, verification is absent, or operational ownership is unclear.

**CDS1300-R001** A migration MUST include an operational transition plan, not only a data-load procedure.

**CDS1300-R002** Business continuity, rollback and verification MUST be designed and approved before production cutover.

Completeness of the migration itself is governed by the inventory-disposition rule (CDS1300-R009): nothing leaves the migration without a recorded disposition. *(This replaces the v0.1 "preserve or explicitly retire every authoritative fact" rule, which was untestable as stated.)*

> Informative note: CDS does not require a big-bang replacement. Incremental adoption is preferred where it reduces risk and maintains traceability.

## 2. Operating Scale and the Small-Team Profile *(normative)*

CDS-1300 names many functions. They are **hats, not headcount**. A sole trader and a hundred-person programme can both conform; what scales is evidence and separation of duties, not the org chart.

**CDS1300-R003** Every function named in this chapter MUST have a named owner. One person MAY hold any number of functions simultaneously. A conformance assessment MUST NOT require distinct individuals per function.

**CDS1300-R004** Where staffing permits, the person who builds a migration artifact (mapping, transformation, load package) SHOULD NOT be the sole acceptor of that artifact. Where one person must do both, the acceptance record MUST note the dual role and the compensating control applied (for example: checklist-driven self-review against frozen criteria, evidence archived for later independent review). Segregation-of-duties expectations and compensating controls are defined in CDS-800 (decision-rights and segregation table); this chapter applies them, it does not redefine them.

**CDS1300-R005** An organisation MAY adopt the **small-team profile** by declaring it in its conformance claim (claim rules: CDS-1000). Under that profile the requirements listed in Table 2-1 apply at the downgraded level shown; **all other requirements apply unchanged**.

**Table 2-1 — Small-team profile downgrades**

| Requirement | Base level | Small-team profile level |
|---|---|---|
| CDS1300-R053 (separate read, write and approval migration credentials) | MUST | SHOULD; a single operator MAY hold combined credentials provided every bulk write is attributable, audit-logged, and the log is reviewed at wave exit |
| CDS1300-R057 (operational readiness demonstrated without project-team intervention) | MUST | The intervention-free clause is waived where the operators and the project team are the same people; the readiness demonstration MUST still be performed and recorded |

Requirements that reference "named owners" or "operational owners" are satisfied under either profile by the hats rule (R003); acceptance and evidence records are never waived, only the requirement for the people involved to be different individuals.

> RESOLVED (was D18 (resolved), owner decision 2026-08-04): accepted — self-declared eligibility, no headcount threshold.

## 3. Adoption Principles *(informative)*

- **Authority before movement** — determine who owns each field before copying values.
- **Profile before transformation** — understand the source data before designing target mappings.
- **Preserve provenance** — retain where a value came from and how it was transformed.
- **Canonical before channel** — resolve canonical values before publishing channel projections.
- **Dictionaries before bulk normalisation** — do not mass-convert values until controlled vocabularies and ambiguity rules exist.
- **Verification before trust** — do not declare migration complete until downstream state is observed and compared.
- **Small reversible releases** — prefer bounded migrations that can be measured and rolled back.
- **Human comprehension** — field names, status displays and review queues must remain understandable to operators.
- **No silent loss** — unsupported fields are quarantined, mapped or explicitly retired, never silently dropped.
- **Evidence over confidence** — completion claims require reproducible evidence.

## 4. Migration Pathways and Starting States *(normative)*

Organisations begin from different levels of structure. CDS defines migration pathways rather than assuming one starting point.

| Starting state | Primary migration emphasis |
|---|---|
| Channel-first store | A commerce platform currently holds the most complete product data. Extract and profile the channel state first, then establish PIM authority. |
| Spreadsheet or hosted-table PIM | A structured but implementation-specific master exists. Preserve formulas, mappings and validation behaviour while replacing brittle field coupling. |
| Legacy enterprise PIM | A mature PIM lacks CDS dictionaries, channel verification or human-readable namespaces. Adoption may be layered rather than replacing the platform. |
| ERP-led catalogue | The ERP owns identity and commercial data; descriptive enrichment is scattered. CDS introduces a canonical enrichment layer without displacing legitimate ERP authority. |
| Multi-channel fragmented estate | Channels contain competing product versions. Migration requires explicit reconciliation and an authority decision per field. |
| Greenfield | No production catalogue exists. Sequence taxonomy, schemas, dictionaries, channel profiles and test fixtures before product entry. |

**CDS1300-R006** The migration plan MUST identify the declared starting state and MUST NOT assume that a system is authoritative merely because it currently contains the most data.

## 5. Readiness Assessment *(normative)*

Before migration begins, the organisation assesses readiness. **Minimum evidence for every area below: documented findings, a named owner and a risk rating.**

| Area | Assessment scope |
|---|---|
| Data | Record counts, duplicate rate, missing identifiers, uncontrolled values, rich-text quality, media completeness, historical anomalies. |
| Architecture | Current product/variant model, taxonomies, field definitions, formulas, scripts, APIs, manual workarounds, hidden dependencies. |
| Channels | Published fields, channel overrides, collection logic, feed requirements, read-back capability, rate limits. |
| People | Data owners, editors, approvers, knowledge concentration, training needs, resistance risks. |
| Governance | Existing naming standards, change control, incident handling, deprecation rules, audit evidence. |
| Operations | Release windows, peak trading periods, support coverage, rollback capacity, acceptable freeze periods. |
| Security | Credentials, least privilege, tenant separation, personal data, supplier confidentiality. |

**CDS1300-R007** Production migration MUST NOT begin until every critical readiness risk has an owner, a treatment and an acceptance decision.

## 6. Source-System and Data Inventory *(normative)*

The source inventory records every system, file, integration and manual process that creates, alters, enriches, publishes or verifies product information.

```
Source Inventory Record
- source_id            - identifiers
- system_name          - record_count
- owner                - known_quality_issues
- data_domains         - retention_requirement
- extraction_method    - migration_disposition
- update_frequency     - evidence_location
```

**CDS1300-R008** Every source that can change product information MUST appear in the source inventory, including manual spreadsheets and channel-admin edit practices.

**CDS1300-R009** Every inventoried source, field, mapping and rule MUST carry a `migration_disposition` — one of `migrate`, `transform`, `merge`, `quarantine`, `retire`, `out_of_scope` — with an evidence location. Nothing exits the migration without a recorded disposition.

**CDS1300-R010** The inventory MUST distinguish authoritative source data, reference data, derived data, channel projections and observed downstream data.

**CDS1300-R011** Unknown fields MUST be classified (and receive a disposition) before they are transformed or discarded.

## 7. Authority and Ownership Baseline *(normative)*

Migration is the opportunity to remove competing masters. An authority matrix records the current owner, target owner, transition date and permitted read-back behaviour for each domain or field. (Authority is declared per fact — CDS-200 §13.)

| Domain | Common current owner | Target authority | Migration rule |
|---|---|---|---|
| Product identity | ERP or legacy PIM | PIM or ERP by declared contract | Identifiers remain stable. |
| Descriptive attributes | Files, supplier feeds, channel admin | PIM | Channel edits become drift unless approved overrides exist (CDS-500 §22). |
| Taxonomy | Channel collections, tags, legacy categories | PIM | External taxonomies remain mappings. |
| Price | ERP, PIM or channel | Declared commercial authority | Do not move authority without finance approval. |
| Inventory | Warehouse, ERP or channel | Inventory authority | PIM may consume but not master live stock. |
| Channel observed state | Channel APIs | Observation store | Never merged into canonical values (CDS-500 §15). |
| Verification result | Legacy formulas or none | Verification engine | Reason codes beneath traffic lights (CDS-500 §17–18). |

**CDS1300-R012** Every migrated field MUST have exactly one declared target authority.

**CDS1300-R013** Read-back and verification fields MUST remain separate from authoritative values throughout migration.

**CDS1300-R014** Each authority cutover MUST be evidenced by at least one of: **(a)** a permission or access change that prevents non-authoritative writes to the field; **(b)** drift detection armed on the field (observation plus comparison per CDS-500); or **(c)** a documented acceptance that enforcement is detection-only, naming the residual risk owner.

> Informative note: some platform standard fields cannot be write-protected at all — any admin user can edit them regardless of PIM authority. For such fields option (a) is unavailable by construction; enforcement is necessarily detection-only (b or c), and the training rule CDS1300-R051 is the compensating human control.

## 8. Target-State Design *(normative)*

The target state is designed before bulk transformation: entity boundaries (CDS-200), semantic namespaces (CDS-300), Attribute Definitions, dictionaries (CDS-400), internal taxonomy, channel profiles (CDS-900), publication and observation records (CDS-500), and operating procedures.

```
Canonical PIM                          External Authorities
+-- Products and Variants              +-- ERP / Pricing
+-- Attribute Definitions              +-- Inventory / Warehouse
+-- Dictionaries and Facets            +-- Orders / Customers
+-- Internal Taxonomy
+-- Media and Content
+-- Channel Profiles
+-- Publication Records
+-- Observations
+-- Verification Results
+-- Governance and Audit
```

**CDS1300-R015** The target model MUST be validated with representative products before full mapping begins.

**CDS1300-R016** Target fields MUST NOT be created solely to preserve accidental source-system implementation details; legitimate source provenance and business meaning MUST be preserved even when field names and storage mechanisms change.

## 9. Taxonomy and Classification Migration *(normative)*

Taxonomy migration separates what a product **is** from where it is **merchandised**. Steps (informative): extract all category-like values (tags, product types, collection rules, supplier categories); identify synonyms and overlaps; design a non-overlapping internal tree; assign one primary category per product; map external taxonomies at category level where inheritance is valid; define collection and navigation projections separately; keep a taxonomy decision log for ambiguous types; validate counts, orphans and duplication.

**CDS1300-R017** A channel's collections, tags or product types MUST NOT be assumed to be canonical categories.

**CDS1300-R018** After migration each product MUST have one primary internal category; collections MAY remain many-to-many merchandising projections (rules: CDS-200 §6).

**CDS1300-R019** External taxonomy mappings MUST retain the source taxonomy version and the mapping rationale.

## 10. Attribute and Dictionary Migration *(normative)*

Legacy fields mix source values, canonical values, display labels, facet values and channel output. Migration separates these into the value layers defined by ADR-D4 (definitions: CDS-100 §3; model: CDS-400).

```
Legacy field:  Colour = "French Navy"

Migrated representation (value layers per ADR-D4):
Source value          = "French Navy"      (preserved verbatim, with provenance)
Alias mapping record  = "French Navy" -> colour_french_navy
Canonical value       = colour_french_navy (stored on the variant)
Display label         = "French Navy"
Facet value           = blue
CH_google_colour      = "Blue"             (channel representation)
```

**CDS1300-R020** Distinct source values MUST be profiled before dictionary normalisation begins.

**CDS1300-R021** Ambiguous mappings MUST enter review; they MUST NOT be resolved by first-match or other arbitrary logic.

**CDS1300-R022** Every source value mapped during migration MUST be retained as an alias (an Alias Mapping Record, CDS-400) with provenance. *(v0.1's "where useful" qualifier is deleted: aliases are what future imports and read-back comparison match against — discarding them breaks verification later.)*

**CDS1300-R023** Facet values MUST be designed for customer usability (CDS-600), not inferred solely from current distinct-value counts.

## 11. Product and Variant Migration *(normative)*

Product and variant migration resolves parent–child relationships, SKU identity, shared attributes and sellable differences (variant boundary rule: CDS-200 §5).

| Control | Migration requirement |
|---|---|
| Identity continuity | Preserve SKU, GTIN, MPN, source IDs and channel IDs where continuity is required. |
| Parent grouping | Confirm variants genuinely represent sellable forms of one logical product. |
| Option definition | Only values that create distinct sellable units become options. |
| Shared data lifting | Move identical values from variants to the parent product. |
| Variant truth | Do not create unavailable combinations by Cartesian expansion. |
| Duplicate detection | Detect same SKU, same GTIN, same MPN/brand and near-identical records. |
| Lifecycle state | Preserve active, draft, archived, discontinued and pre-order meaning. |

**CDS1300-R024** A migration MUST NOT create new SKU identities merely to fit a target platform unless a governed re-identification plan exists.

**CDS1300-R025** Every variant consolidation or split MUST be evidenced by an approved old-to-new cross-reference table. The cross-reference table is the **primary** control; mechanical reversibility of a restructure is rarely available on production channels and MUST NOT be assumed or claimed without test evidence.

**CDS1300-R026** The wave design MUST check migrated products against the declared structural limits of each target channel profile (variants per product, option count, value lengths — CDS-900) **at design time**, before mapping is finalised, not at load time.

## 12. Content, Media and Digital Assets *(normative)*

Checklist (informative): preserve original source content separately from enriched content where provenance matters; normalise rich text without silently removing meaningful structure; retain asset identifiers, source URLs, checksums, rights and usage restrictions; define primary image, sequence, variant association and alt-text rules; quarantine broken, duplicate, low-resolution or unsupported assets; verify downstream media ordering and variant-image association after publication.

**CDS1300-R027** Asset migration MUST preserve available rights and provenance metadata.

**CDS1300-R028** Asset transfer success MUST NOT be treated as proof that the channel displays the correct asset in the correct order; media ordering and variant association are in verification scope (CDS-500).

## 13. Channel Mapping and Publication Migration *(normative)*

Channel migration converts legacy output fields and direct-admin practices into governed channel profiles and publication records. The canonical model is not redesigned to mirror channels.

```
Canonical attribute -> channel mapping -> expected representation
                    -> publication -> observation -> verification
```

**CDS1300-R029** Each migrated channel field MUST identify its canonical source, transformation, destination and comparison strategy.

**CDS1300-R030** Channel overrides MUST be explicit, attributable and bounded (override records: CDS-500 §22).

**CDS1300-R031** New channel fields MUST use the `CH_` namespace (ADR-D24; registry: CDS-300). Legacy `DF_` names MAY persist during transition only as registered deprecated aliases with provenance. Per ADR-D24 §3, a field is a feed-layer projection **iff it is a literal serialized feed column**; such projections live under `CH_` and the feed artifact is verified end to end at the formatted-output layer.

**CDS1300-R032** Generated tags, collections and feed outputs MUST be reproducible from governed source data or rules; they MUST NOT be imported as independent canonical truth.

*(v0.1's "retain DF_ only where useful" and "metafield-equivalent" qualifiers are resolved by ADR-D24 and ADR-D2 respectively; the MF_/STD_ boundary is the CDS-300 enumeration, never a judgement call.)*

## 14. SEO and URL Continuity *(normative — new in v0.2)*

After data loss, the largest business risk in a commerce migration is losing accumulated search equity. URL and search continuity is migration scope, not an afterthought.

**CDS1300-R033** A migration that changes customer-facing URLs, handles, slugs or channel identifiers MUST, for every existing customer-facing URL, either preserve the URL or serve a permanent redirect to its successor.

**CDS1300-R034** SEO-critical fields — page titles, meta descriptions, canonical URLs, and any structured-data fields declared in the channel profile — MUST be included in the pre-cutover baseline (§15) and in post-cutover verification scope.

**CDS1300-R035** Redirect coverage SHOULD be verified after cutover by sampling pre-cutover URLs, and index-status and organic-traffic signals SHOULD be monitored through the wave's proving period.

> Informative note: redirect behaviour is a channel-profile capability check. Some platforms create redirects automatically when a handle changes; others require explicit redirect records; some feed-based channels key on identifiers where "redirect" means identifier continuity. Record the mechanism per channel in the CDS-900 profile before cutover.

## 15. Verification Baseline and Downstream Read-Back *(normative)*

Before changing production data, capture what downstream channels currently contain. This separates pre-existing drift from migration-induced drift — the strongest available defence against blaming the migration for old defects, or missing new ones.

```
Baseline: extract current channel state -> store observed values
          -> compare against current expected state -> record pre-existing mismatches
          -> freeze baseline evidence -> begin migration
```

**CDS1300-R036** A downstream baseline MUST be captured and frozen before production cutover wherever read-back is technically available, and the frozen baseline MUST be retained at least until the wave passes its exit gates (it is also the rollback republication source — R042).

**CDS1300-R037** Pre-existing mismatches MUST be recorded and distinguished from mismatches introduced by migration.

**CDS1300-R038** Fields that cannot be observed MUST be recorded with the `UNOBSERVABLE` status from the CDS-500 enum; they MUST NOT be reported as verified. Verification statuses, reason codes and traffic-light presentation are owned by CDS-500 §17–§18 and are not restated here.

## 16. Cutover Strategies *(normative)*

| Strategy | Use and risk |
|---|---|
| Big bang | Everything switches together. Highest coordination risk; only for small, well-tested, easily reversible estates. |
| Wave by category | Bounded category groups; useful for dictionary and taxonomy validation. |
| Wave by brand or supplier | Supports source-specific mappings and operational ownership. |
| Wave by channel | Establish PIM authority, then migrate one downstream channel at a time. |
| Shadow publication | Generate expected output without writing production; compare against current channel state. |
| Dual run | Old and new pipelines run simultaneously with controlled reconciliation — see R040. |
| Pilot cohort | A small representative product set migrated end to end before scale-out. |

**CDS1300-R039** The chosen strategy MUST define scope, entry criteria, exit criteria, rollback point and evidence package.

**CDS1300-R040** At any moment, exactly **one** pipeline MUST be the declared writer for a given channel field-set. On a channel with a single write target, a "dual run" therefore MUST operate as shadow publication on the non-authoritative side: the non-authoritative pipeline generates expected output and compares, and MUST NOT write. Reconciliation happens on evidence, never by both pipelines writing.

**CDS1300-R041** Each wave plan MUST declare its proving period (the post-cutover observation window that must elapse defect-free before exit) before cutover.

> Informative note: typical proving periods run one to four weeks and should cover at least one full business cycle for the affected products (including any weekly ordering, feed or campaign rhythm).

## 17. Rollback, Recovery and Business Continuity *(normative)*

Rollback is a designed capability, not an emergency improvisation.

**CDS1300-R042** Every production migration wave MUST have a tested rollback or compensating recovery procedure. **Channel-side rollback is defined as republication of the frozen pre-cutover baseline (R036)** through the governed publication path, followed by observation and verification — not as restoration of channel-internal state, which most channels cannot provide.

**CDS1300-R043** Rollback MUST NOT overwrite the evidence required to determine what changed and why (publication records, observations, verification results, decision log).

Rollback design checklist (informative): freeze pre-cutover source and channel state; version transformation rules, mappings, dictionaries and payloads; maintain old-to-new identifier cross-references; define stop conditions and escalation authority; test restoration of data, credentials and scheduled jobs; reconcile publication attempts made before failure; preserve evidence from failed runs.

> Informative — irreversibility classes. Republication restores content state but cannot reverse everything. Classes to enumerate per wave: (1) customer interactions bound to channel identifiers (orders, reviews, wishlists) — never reversible; (2) search-engine indexing and ranking signals accumulated against changed URLs (mitigated by §14, not reversed); (3) feeds, emails and ads already consumed downstream; (4) channel-side identifiers destroyed by deletion (recreated objects get new identities); (5) analytics history continuity; (6) third-party caches and syndication copies. A rollback plan states, per class, whether the exposure exists and what compensating action applies.
>
> Informative — commerce activity during rollback: orders, payments and fulfilment are mastered outside CDS scope (CDS-000 §2) and proceed on their own systems. The migration team's obligation is product-data remediation: identify products sold while incorrect data was live, correct the data forward, and hand any customer-impact assessment to the responsible business owner.

## 18. Operational Rollout and Run-State Transition *(normative)*

Migration ends only when the new operating model is stable and owned.

| Run-state area | Required operational definition |
|---|---|
| Publishing | Schedules, queue monitoring, retries, rate limits, incident ownership. |
| Verification | Read-back cadence, mismatch triage, health thresholds, escalation. |
| Dictionaries | New-value review, alias creation, facet governance, deprecation. |
| Taxonomy | Category-change procedure, mapping review, decision log. |
| Imports | Supplier onboarding, schema-change detection, quarantine, delta-sync monitoring. |
| AI | Proposal review, thresholds, benchmarks, model-change handling (CDS-700). |
| Support | Operator runbooks, dashboards, alert routing, service expectations (CDS-1400). |
| Release management | Versioning, change windows, approvals, rollback ownership. |

**CDS1300-R044** Project completion MUST include recorded acceptance by the named run-state owners (who MAY be the same people as the project team — §2).

**CDS1300-R045** Temporary migration scripts and credentials MUST be retired, governed, or incorporated into supported operations.

## 19. Data Quality Remediation *(normative)*

Migration surfaces defects that may have existed for years. CDS separates blocking defects, remediable defects and accepted historical imperfections.

| Class | Treatment |
|---|---|
| Blocking | Missing product identity, duplicate SKU, invalid variant relationship, unsafe price, critical compliance data. |
| High priority | Unmapped category, dictionary ambiguity, missing required channel field, broken media. |
| Improvement | Weak descriptions, missing optional attributes, poor search synonyms, non-critical legacy formatting. |
| Accepted debt | Known issue with documented reason, owner, review date and impact assessment. |

**CDS1300-R046** Quality thresholds MUST be defined before acceptance testing begins.

**CDS1300-R047** Quality and completeness denominators MUST include failed and quarantined records. A record MAY leave a denominator only through a disclosed `migration_disposition` (R009). Reporting completeness over a silently reduced population is non-conformant. *(This is the corpus's strongest anti-gaming control; see also CDS-1400 §6.)*

## 20. AI-Assisted Migration *(normative)*

AI may accelerate classification, attribute extraction, dictionary suggestions, duplicate review, content cleanup and anomaly detection. It remains a **proposal mechanism** governed entirely by CDS-700 (proposals separate from canonical state, evidence classes, confidence, abstention, autonomy levels, review). This section adds only the migration-specific rules.

**CDS1300-R048** AI-generated migration values MUST carry the provenance CDS-700 requires (model/workflow version, evidence, confidence where available) and MUST pass the same schema and dictionary validation as any other input.

**CDS1300-R049** AI MUST NOT silently resolve identifier conflicts, legal claims, safety attributes or other high-risk discrepancies; these MUST enter human review.

**CDS1300-R050** Human review samples SHOULD include both accepted and rejected proposals, to detect systematic error in either direction.

## 21. People, Functions, Training and Change Management *(normative)*

A CDS rollout changes responsibilities and habits. Teams must understand not only new screens but why canonical authority, dictionaries and verification exist.

The migration **functions** (hats — one person MAY hold several, per R003):

| Function | Primary accountability |
|---|---|
| Executive sponsor | Scope, risk and organisational priority. |
| Programme lead | Migration plan, dependencies, acceptance. |
| Data architect | Target model, mappings, technical integrity. |
| Data steward | Dictionaries, taxonomy quality, exceptions. |
| Channel owner | Platform mappings and operational behaviour. |
| Migration engineer | Extraction, transformation, load and evidence automation. |
| Verifier / QA | Expected-versus-observed validation and test evidence. |
| Business editor | Usability, product meaning, workflow fit. |
| Operations owner | Runbooks, monitoring, incidents, support obligations. |

**CDS1300-R051** Training MUST cover authority, namespaces, dictionaries, publication states, verification and exception handling — and specifically **which channel-admin edits will be overwritten or treated as drift**.

## 22. Security, Privacy and Tenant Isolation *(normative)*

Migration often requires broad temporary access and bulk extraction; controls stay proportionate and time-bounded.

**CDS1300-R052** Migration tooling MUST preserve tenant and organisation boundaries (no cross-organisation mixing of dictionary, publication or observation records).

**CDS1300-R053** Migration credentials MUST follow least privilege, and read, write and approval credentials MUST be separated. *(Small-team profile: downgraded per Table 2-1 — combined credentials permitted with full attributable audit logging reviewed at wave exit.)*

**CDS1300-R054** Temporary extracts MUST have a retention and destruction decision; temporary credentials MUST be rotated or revoked after each phase.

Checklist (informative): encrypt exports; restrict supplier-pricing and confidential data; exclude unnecessary customer or order data from product migration datasets; record who executed bulk writes and which package revision was used; validate archive retention against policy.

## 23. Metrics, Acceptance Criteria and Exit Gates *(normative)*

Acceptance criteria are defined at product, wave, channel and programme levels.

| Metric | Acceptance evidence |
|---|---|
| Record reconciliation | Source, transformed, loaded, quarantined and retired counts reconcile (dispositions per R009). |
| Identifier integrity | No unapproved duplicate or changed SKU/GTIN/MPN identities. |
| Schema validity | Required records pass structural and semantic validation. |
| Dictionary coverage | Distinct values mapped, quarantined or explicitly excluded — with aliases retained (R022). |
| Taxonomy coverage | Valid primary categories and expected external mappings. |
| Publication success | Expected payloads accepted without unhandled failure. |
| Observation coverage | Expected fields read back or explicitly `UNOBSERVABLE` (CDS-500). |
| Verification health | Mismatch and missing rates below approved thresholds. |
| SEO continuity | URL/redirect coverage verified per §14. |
| Operational stability | Queues, schedules, retries and alerts operate through the declared proving period (R041). |
| User acceptance | Readiness demonstration per R057. |

**CDS1300-R055** Acceptance thresholds MUST be approved before the migration wave executes.

**CDS1300-R056** A wave MUST NOT exit merely because all jobs completed; quality, verification, SEO-continuity and operational gates also apply.

**CDS1300-R057** Operational readiness MUST be demonstrated by named operators completing representative workflows without project-team intervention, and the demonstration recorded. *(Small-team profile: intervention-free clause waived per Table 2-1.)*

## 24. Conformance *(normative)*

Conformance levels, test suites and claim rules are owned by CDS-1000. A CDS-1300 conformance claim is a claim against the requirement set CDS1300-R001–R057 (with Table 2-1 substitutions where the small-team profile is declared), evidenced per CDS-1000. Recommended practices — pilot cohorts, automated evidence generation, versioned mapping packages, a migration issue/decision register, use of the CDS-1200 fixtures for deterministic validation, and a post-cutover retrospective with debt handover — are SHOULD-level and MAY be cited as supporting evidence in a claim.

## 25. Worked Migration Scenarios *(informative)*

### 25.1 Legacy hosted-table PIM (Airtable) to CDS

```
Legacy layers                             CDS role
Import_*                 -> source ingestion records
Airtable_*               -> canonical core values
MF_Airtable_*            -> canonical structured attributes
DF_Airtable_SEO_*        -> channel/feed projections (Data Feed layer — ADR-D24)
Shopify_* / MF_Shopify_* -> downstream observations
Match_* / MF_Match_*     -> verification results
```

Migration outcome: preserve formula intent as explicit transformations; replace implicit behaviour with Attribute Definitions and rules; retain read-back and traffic-light concepts (CDS-500); map general downstream fields into `CH_*`; register `DF_*` as deprecated aliases (feed-column projections continue under `CH_` per R031).

**CDS1300-R058** Legacy formulas MUST be catalogued and tested before they are replaced by code or rules — hidden business rules must not be lost even where implementation details change.

> Informative note: Airtable formula *logic* is not extractable through the data API — the API returns computed results, not formula text. Catalogue formulas from the schema/UI, exported documentation, or maintained records, and budget for this as a manual step.

### 25.2 Channel-First Clothing Store

Current state: platform products are master; `collection_*` tags drive navigation; colours contain 80+ distinct values; some attributes live in description text.

Migration:
1. extract products, variants, tags, collections and structured fields
2. profile current colour values
3. build canonical colour and facet dictionaries
4. establish internal taxonomy
5. create PIM records and expected channel state
6. shadow compare before write (R040)
7. pilot one category
8. publish, read back and verify
9. expand by category wave

### 25.3 Multi-Supplier Homewares Catalogue

```
Current state                      Target
Supplier A: "Tasmanian Oak"        Source values preserved; aliases retained (R022)
Supplier B: "Oak Timber"           Canonical material = oak or wood, per evidence
Supplier C: "Natural Wood"         Facet material = wood
                                   Display label remains source-appropriate
                                   Channel values follow each channel profile
```

Ambiguous "Natural Wood" **enters review** rather than being auto-mapped to oak (R021): the term may mean oak, pine, or an unspecified species; first-match mapping would fabricate a material claim.

## 26. Architecture Decisions *(informative)*

Per CDS000-R006, ADRs live in the single global register. Decisions originating in this chapter, now recorded there: staged reversible adoption preferred; operational handover is part of migration; pre-cutover downstream baseline required; legacy formula intent preserved before replacement; quality denominators include quarantined records; AI assists but does not silently arbitrate conflicts. The v0.1 record CDS-ADR-1300-005 (DF_→CH_) is **superseded by ADR-D24**.

## Appendix A — Migration Phase Checklist *(informative)*

Each phase exits on evidence accepted by a named accountable owner (one person MAY own several or all phases — §2; builder/acceptor separation per R004).

| Phase | Exit evidence |
|---|---|
| A. Mobilise | Scope, sponsor, programme lead, risk register, release constraints, communication plan approved. |
| B. Discover | Sources, fields, formulas, integrations, channels, users and hidden processes inventoried. |
| C. Profile | Counts, duplicates, nulls, distinct values, taxonomies, variants and media quality measured. |
| D. Design | Target model, ownership, namespaces, dictionaries, taxonomy, mappings and rules approved. |
| E. Build | Extraction, transformation, load, publication, observation and verification workflows implemented. |
| F. Test | Schema, semantic, negative, round-trip, performance, security and rollback tests passed. |
| G. Pilot | Representative cohort migrated and operated through a proving period. |
| H. Cut over | Approved wave executed with monitoring, reconciliation and rollback readiness. |
| I. Stabilise | Mismatches triaged, operational metrics stable, documentation and training completed. |
| J. Close | Operational acceptance, debt register, retrospective, evidence archive, temporary-access retirement completed. |

## Appendix B — Legacy Airtable PIM Mapping *(informative — organisation example)*

This table records one organisation's legacy naming as a worked example. It is not normative reference data; the normative prefix registry is CDS-300.

| Legacy pattern | CDS role | Migration treatment |
|---|---|---|
| `Import_*` | Source ingestion | Retain as source records; never canonical. |
| `Airtable_*` | Resolved core data | Map to canonical product/variant fields. |
| `MF_Airtable_*` | Resolved structured data | Map to governed attributes and values; MF_ per the ADR-D2 enumeration boundary. |
| `DF_Airtable_SEO_*` | Data Feed output (ADR-D24) | Map to `CH_google_*` or feed-column projections under `CH_`. |
| `Shopify_*` | Observed standard fields | Map to observation records (CDS-500 §15). |
| `MF_Shopify_*` | Observed metafields | Map to observation fields. |
| `Match_*` / `MF_Match_*` | Comparison formulas | Map to verification results with reason codes and comparison strategies (CDS-500). |
| `collection_*` tags | Computed collection signals | Regenerate from taxonomy/collection rules; never import as independent canonical truth. |
| Traffic lights | Operator QA display | Retain as presentation over detailed statuses (CDS-500 §18). |

## Appendix C — Adoption Maturity Mapping *(informative)*

The single conformance ladder is owned by CDS-1000 (ADR-D1): Foundation → Structured → Publisher → Verified → Governed. The v0.1 maturity levels of this chapter map as follows and are retained only as adoption-narrative labels:

| v0.1 maturity level | CDS-1000 ladder |
|---|---|
| Level 0 — Fragmented | pre-Foundation |
| Level 1 — Canonical | Foundation |
| Level 2 — Structured | Structured |
| Level 3 — Publisher | Publisher |
| Level 4 — Verified | Verified |
| Level 5 — Governed | Governed |

END OF CDS-1300 v0.2 REVIEW DRAFT


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1400 — Monitoring, Incident Management and Continuous Improvement

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1400 Working Draft v0.1 |
| Normative status | §1–§2, §4–§27 are normative except where marked otherwise. §3, §28, §29 and Appendices A–D are informative. Tables explicitly marked *(informative)* inside normative sections carry no requirements. |
| Findings addressed | SYS-3 (D18), SYS-4, 1400-1..14; ADR-D3 (Appendix E deleted — statuses and traffic lights single-homed in CDS-500 §17–§18); Matrix 5 (drift taxonomy → CDS-500 §20; AI rules → CDS-700; conformance claims → CDS-1000; test-outcome spellings → CDS-1000 §21) |

An operational assurance framework for detecting product-information defects, controlling incidents, measuring downstream health and converting evidence into sustained improvement.

---

## 1. Purpose and Scope *(normative)*

CDS-1400 defines how a CDS-conformant commerce information environment is monitored after adoption and how operational defects are detected, assessed, contained, repaired and prevented from recurring. It covers the full information path from source ingestion and canonical enrichment through channel publication, downstream observation, verification and customer-facing use.

The chapter treats product information as an operational service. Availability alone is insufficient: a PIM can be online while products are missing attributes, filters expose unusable values, channel mappings drift, or downstream listings differ from the expected state.

**CDS1400-R001** A CDS operating model MUST monitor correctness, completeness, timeliness and downstream fidelity in addition to technical availability.

**CDS1400-R002** An organisation MUST define how product-data incidents are declared, owned, escalated, resolved and reviewed.

**CDS1400-R003** Operational monitoring MUST use declared denominators and MUST NOT hide quarantined, failed or unobserved records (denominator rules: §6).

> Informative note: CDS-1400 does not prescribe a particular monitoring product. The controls may be implemented with dashboards, logs, metrics, queues, scheduled reports or a combination of systems.

## 2. Operating Scale and the Small-Team Profile *(normative)*

CDS-1400 names many roles, views and reviews. They are **hats, not headcount** — the same rule that governs migration functions in CDS-1300 §2. A sole trader and a hundred-person operations organisation can both conform; what scales is evidence and separation of duties, not the org chart.

**CDS1400-R004** Every role, review and monitoring domain named in this chapter MUST have a named owner. One person MAY hold any number of roles simultaneously, including all incident-command roles. A conformance assessment MUST NOT require distinct individuals per role.

**CDS1400-R005** Where staffing permits, the person coordinating an incident SHOULD NOT be the person performing the most complex repair, and the person who built a monitoring control or automation SHOULD NOT be its sole acceptor. Where one person must hold both hats, the incident or acceptance record MUST note the dual role and the compensating control applied (for example: checklist-driven self-review against the runbook, evidence archived for later independent review). Segregation-of-duties expectations and compensating controls are defined in CDS-800 §18; this chapter applies them, it does not redefine them. The small-team accommodation mirrors CDS-1300 §2.

**CDS1400-R006** An organisation MAY adopt the **small-team profile** by declaring it in its conformance claim (claim rules: CDS-1000). Under that profile the requirements listed in Table 2-1 apply at the downgraded level shown; **all other requirements apply unchanged**. Acceptance and evidence records are never waived — only the requirement for the people involved to be different individuals.

**Table 2-1 — Small-team profile downgrades**

| Requirement | Base level | Small-team profile level |
|---|---|---|
| CDS1400-R053 (SEV-1 post-incident review includes a participant who was not the primary responder) | MUST | Waived where no second qualified person exists; the review record MUST note the sole-operator condition, and the evidence package MUST be archived so a later independent review remains possible |

After the base-level corrections in this revision — the hats rule (R004), the informative cadence table (§26), SHOULD-level service objectives (R016), the next-business-day coverage allowance (R033) and combined dashboard views (§10) — R053 is the only remaining requirement that presupposes a second person. Migration-phase downgrades continue to be governed by CDS-1300 Table 2-1.

**CDS1400-R007** An organisation MAY declare the **enterprise operations profile** (an overlay profile under CDS-1000 §16). Under that profile: CDS1400-R016 (per-context service objectives) upgrades from SHOULD to MUST, and the minimum-roles column of Appendix B becomes applicable staffing guidance. Outside that profile the minimum-roles column is informative illustration only.

> RESOLVED (was D18 (resolved), owner decision 2026-08-04): accepted — self-declared eligibility, no headcount threshold, mirroring CDS-1300.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The enterprise operations profile is modelled as a CDS-1000 overlay profile so that its upgraded MUSTs are testable within the existing claim machinery; the alternative — leaving SLO enforcement to per-organisation declared thresholds only — was rejected because it gives large multi-team operations no claimable assurance tier.

## 3. Operational Assurance Principles *(informative)*

- **Observe the whole information path** — source, canonical, publication, downstream and customer-experience states.
- **Measure facts, not confidence** — health claims derive from reproducible metrics and evidence.
- **Separate expected from observed** — retain what should exist downstream and what was actually read back.
- **Alert on actionability** — an alert has an owner, a condition and a defined response.
- **Preserve detail beneath summaries** — colour views remain backed by precise statuses, reason codes and affected records.
- **Prefer early containment** — stop incorrect propagation before optimising full repair.
- **Make recovery reversible** — repair, replay and rollback preserve lineage and can be audited.
- **Learn without blame** — post-incident review improves systems and controls, not scapegoats.
- **Track recurrence** — repeated symptoms are a problem-management issue, not isolated tickets.
- **Continuously reduce uncertainty** — monitoring gaps and unobservable fields are explicit, owned risks.

## 4. Observability Model *(normative)*

CDS observability is the ability to determine the health and history of product information from recorded signals. The minimum model contains the linked states:

```
Source State
    -> Canonical State
    -> Expected Channel State
    -> Publication Attempt
    -> Observed Channel State
    -> Verification Result
    -> Customer Experience Signal
```

**CDS1400-R008** Monitoring MUST distinguish data state from processing state. A completed job does not prove that the resulting data is correct.

**CDS1400-R009** Each material signal SHOULD be traceable to product, variant, field, channel, canonical revision and the relevant mapping or dictionary version.

**CDS1400-R010** Where a downstream field cannot be observed, its verification state MUST be recorded as `UNOBSERVABLE` from the CDS-500 §17 enum. It MUST NOT be recorded or reported as `MATCH`. (Test executions that were never run use the CDS-1000 §21 outcome `NOT_TESTED`; verification statuses and test outcomes are distinct vocabularies.)

## 5. Monitoring Domains *(normative)*

*Representative signals (informative):*

| Domain | Representative signals |
|---|---|
| Source ingestion | Fetch success, freshness, record counts, duplicate identifiers, schema changes, parsing errors, supplier anomalies. |
| Canonical product layer | Completeness, validity, conflicts, unresolved overrides, stale values, product/variant integrity. |
| Taxonomies and dictionaries | Unmapped values, ambiguous aliases, deprecated entries, version changes, unexpected cardinality growth. |
| Workflow and enrichment | Queue age, blocked approvals, review backlog, failed rules, missing ownership, time-to-ready. |
| Publication | Preflight failures, attempted writes, acknowledgements, rejections, rate limiting, retries, publish lag. |
| Observation | Read-back coverage, retrieval failures, stale observations, unsupported fields, API visibility gaps. |
| Verification | Match rate, missing rate, mismatch rate, comparison errors, unresolved age, drift recurrence. |
| Customer experience *(conditionally observable — §24)* | Facet cardinality, zero-result combinations, navigation dead ends, search failures, incorrect counts. |
| AI and automation | Proposal volume, confidence calibration, rejection and override rates, out-of-dictionary output, model or prompt drift. |
| Security and tenancy | Credential failures, unauthorised changes, cross-tenant leakage, unusual export volume, evidence tampering. |

**CDS1400-R011** Every CDS operating profile MUST declare which monitoring domains are in scope and who owns each domain (one person MAY own all — §2).

## 6. Metrics, Measures and Denominators *(normative)*

A metric is useful only when its population, time window and exclusions are explicit. *(Measure kinds — count, rate, latency, age, distribution, trend, cardinality, coverage — are informative vocabulary; Appendix A gives the reference catalogue.)*

Worked example — why observation coverage and match rate are separate measures:

```
eligible_expected_fields    = 10,000
observable_expected_fields  =  9,200   (800 are UNOBSERVABLE on this channel)
observed_fields             =  9,050
matched_fields              =  8,960
mismatched_fields           =     60
missing_fields              =     30

observation_coverage        = 9,050 / 9,200   (how much we can see)
verification_match_rate     = 8,960 / 9,050   (how much of what we see is right)
```

Reporting `8,960 / 10,000` as a "match rate" would silently blend blindness into fidelity; reporting `100%` for the 800 unobservable fields would fabricate assurance. Both numbers must travel together.

**CDS1400-R012** A rate MUST name its numerator, denominator, eligibility rules, exclusions and measurement window.

**CDS1400-R013** Quarantined or failed records MUST remain visible in relevant operational denominators unless the metric explicitly measures a different population. A record MAY leave a denominator only through a disclosed disposition. This applies the corpus's strongest anti-gaming control (CDS1300-R047; quarantine model: CDS-400 §17).

**CDS1400-R014** An organisation MUST NOT report a 100 percent match rate — or any match rate — over fields that were not observed. Observation coverage MUST be reported separately from verification match rate and MUST NOT be folded into it.

## 7. Service Indicators, Objectives and Verification-Health Thresholds *(normative)*

*Reference indicators (informative):* publication success (accepted / attempted eligible records); verified fidelity (`MATCH` results / observed expected fields); observation coverage (observed / observable expected fields); freshness (records within permitted age / eligible records); workflow timeliness; facet usability (collection views within approved cardinality and zero-result thresholds); recovery (incidents restored within target / incidents in severity class).

**CDS1400-R015** For every verified channel, the organisation MUST declare and monitor verification-health thresholds — at minimum: acceptable mismatch rate, acceptable missing rate, minimum observation coverage and maximum unresolved-mismatch age. These declared thresholds are the **base assurance mechanism** of this chapter. (Channel health aggregation: CDS-500 §23; migration exit thresholds: CDS-1300 §23.)

**CDS1400-R016** Per-context service objectives (SLOs) with defined measurement windows SHOULD be defined over the reference indicators. Under the enterprise operations profile (R007) this requirement upgrades to MUST. Verification-health thresholds (R015) already deliver the core assurance; full SLO and error-budget apparatus is proportionate to multi-team operations, not a universal floor.

**CDS1400-R017** A breach of a declared threshold or a missed declared objective MUST trigger a review proportional to customer, commercial or compliance impact.

> Informative note: an error budget is the permitted amount of objective failure within a period; organisations may use it to balance change velocity against reliability work. CDS does not prescribe universal numeric targets because catalogue size, channel behaviour and business criticality differ (v0.1 ADR CDS-ADR-1400-008, retained).

## 8. Product, Catalogue and Channel Health *(normative)*

CDS distinguishes health at different aggregation levels — field, product, category, catalogue, channel, customer experience and operations. A single score may be useful for scanning, but it must not replace the underlying dimensions. Health computation and aggregation rules are owned by CDS-500 §23; this section applies them operationally.

**CDS1400-R018** A composite health score MUST expose its component measures, weights and unavailable inputs.

**CDS1400-R019** A green catalogue or channel score MUST NOT conceal a red condition on any field in the channel's **declared critical set**. The mechanism is CDS-500's: the organisation declares the critical field set per channel (CDS500-R013), and any critical-set field presenting RED caps the aggregate presentation at RED regardless of the numeric score (CDS500-R085). This chapter adds the operational obligation: the declared critical set MUST be reviewed when incidents reveal high-impact fields outside it.

## 9. Telemetry and Event Model *(normative)*

Operational signals SHOULD be emitted as structured events or equivalent records supporting correlation, replay and audit. *Reference event fields (informative):* `event_id`, `event_type`, `occurred_at`, `recorded_at`, `organisation_id`, `product_id`/`variant_id`, `field_id`, `channel_id`, `canonical_revision`, `mapping_version`, `dictionary_version`, `correlation_id`, `severity_hint`, `reason_code`, `evidence_reference`.

**CDS1400-R020** Telemetry MUST preserve tenant boundaries and MUST NOT expose sensitive supplier or customer data to unauthorised monitoring users (isolation rules: CDS-800 §19).

**CDS1400-R021** Event types and reason codes SHOULD be versioned and governed as controlled reference data. Verification reason codes are drawn from the CDS_* registry (CDS-1100 §21; seed list CDS-500 Appendix B), not invented per dashboard.

## 10. Dashboards and Operational Views *(normative)*

Dashboards are role-specific views over evidence. *The audience catalogue below is informative: it describes focus areas, not mandatory separate dashboards. Views MAY be combined; a small team MAY operate a single view covering all audiences.*

| Audience *(informative)* | Typical focus |
|---|---|
| Executive | Catalogue and channel health, objective attainment, major incidents, unresolved critical debt. |
| PIM operations | Ingestion freshness, canonical quality, workflow backlog, quarantines, change effects. |
| Channel operations | Publication, observation, verification, rate limits, retries, channel-specific failures. |
| Merchandising / UX | Facet cardinality, zero-result combinations, navigation defects, collection coverage. |
| Data stewardship | Unknown values, ambiguous mappings, dictionary changes, deprecations, ownership queues. |
| Engineering | Job health, APIs, transformations, event correlation, deployment regressions. |
| AI governance | Proposal quality, acceptance, corrections, calibration, prohibited-output incidents. |

**CDS1400-R022** Every summary dashboard MUST support drill-down to affected populations or evidence references.

**CDS1400-R023** Dashboard freshness and last-successful-update time MUST be visible on the dashboard itself.

**CDS1400-R024** Colour MUST NOT be the only signal conveying state in any operational view; a text label, status or reason code MUST accompany colour, for accessibility and for diagnosis. Traffic-light colour semantics and the detailed-status accessibility rule for verification indicators are owned by CDS-500 §18 (CDS500-R069, CDS500-R072–R073); this requirement extends the same principle to every operational view, not only verification indicators.

## 11. Alerting and Noise Control *(normative)*

Alerts exist to cause timely human or automated action. Reports and informational trends should not be disguised as urgent alerts. *Full alert anatomy (informative): condition, scope, owner, urgency, evidence, runbook link, suppression logic, clear condition — a useful design checklist, not eight mandatory artifacts.*

**CDS1400-R025** Every production alert MUST have an accountable response owner and a documented first action. This is the normative floor for alert design.

**CDS1400-R026** Alerts SHOULD be deduplicated by condition, scope and time window to prevent notification storms.

**CDS1400-R027** An alert that repeatedly produces no action MUST be reviewed and SHOULD be redesigned, downgraded or retired. Alerting is self-limiting by design: an ignored alert is operational debt, not coverage.

> Informative note: useful patterns include threshold alerts, absence-of-expected-event alerts, rate-of-change alerts and anomaly alerts. Anomaly alerts require extra caution because they are hard to explain and tune.

## 12. Incident Classification and Severity *(normative)*

An incident is an unplanned condition that materially threatens or degrades canonical integrity, publication fidelity, customer experience, compliance, security or operational continuity.

| Incident class | Description |
|---|---|
| Canonical integrity | Incorrect or lost authoritative product facts, identifiers or relationships. |
| Publication failure | Expected records cannot be published or are rejected. |
| Downstream drift | Observed channel state differs from expected state (causes: CDS-500 §20). |
| Taxonomy or dictionary defect | Incorrect classification, mapping, alias or facet grouping affects products. |
| Customer-experience defect | Filters, search, navigation or product details mislead or block customers. |
| Security or tenant isolation | Unauthorised access, leakage, tampering or cross-organisation exposure. |
| AI or automation defect | Automated enrichment or execution produces material incorrect output. |
| Observability failure | Monitoring or read-back cannot detect or measure a critical state. |
| Operational capacity | Backlog, rate limit, resource exhaustion or staffing prevents timely processing. |

| Severity | Impact interpretation |
|---|---|
| SEV-1 Critical | Widespread or high-risk incorrect data, security/tenant breach, material legal exposure, or loss of control over authoritative data. Immediate coordinated response. |
| SEV-2 High | Material customer or channel impact, significant publication failure, or major drift affecting a defined business area. Urgent response. |
| SEV-3 Moderate | Limited impact with available workaround; bounded degradation. Scheduled but prompt response. |
| SEV-4 Low | Minor defect, cosmetic issue, isolated warning or improvement opportunity. Normal work queue. |

**CDS1400-R028** Severity MUST be based on actual or credible impact, not only the number of affected records.

**CDS1400-R029** Security, safety, legal or tenant-isolation concerns MUST be allowed to raise severity even when the affected population is small.

**CDS1400-R030** Severity MAY change as evidence improves; changes MUST be recorded with rationale.

## 13. Incident Roles and Command *(normative)*

*Incident roles (informative — these are hats per §2, holdable by one person):* incident commander; technical or data lead; operations lead; communications lead; scribe / evidence owner; security or compliance lead; business owner; reviewer.

**CDS1400-R031** Every SEV-1 and SEV-2 incident MUST have a named incident commander. The commander MAY simultaneously hold any or all other incident roles (R004).

**CDS1400-R032** Where staffing permits, the person coordinating the incident SHOULD be distinct from the person performing the most complex repair; the sole-operator case is governed by R005 (dual role noted, compensating control recorded).

**CDS1400-R033** Decision authority, escalation contacts and coverage hours MUST be declared per severity and incident class before an incident occurs. Declared after-hours coverage MAY be next-business-day for any incident class **except security and tenant-isolation classes, which MUST have a declared immediate escalation path at all times**.

## 14. Detection, Triage and Declaration *(normative)*

Triage determines whether a signal is valid, its scope, likely impact and the next safe action. Early uncertainty is expected; hidden uncertainty is not. *Triage checklist (informative):* confirm the signal is current, not a stale dashboard or duplicate event; identify affected organisation, products, variants, fields, categories and channels; determine whether canonical state, publication state, observed state or customer presentation is wrong; check recent code, mapping, dictionary, taxonomy, supplier or bulk-edit changes; estimate impact and declare provisional severity; assign roles and open a durable incident record; decide whether to pause ingestion, enrichment, publication, automated repair or AI workflows; set the next update time and stakeholder audience.

**CDS1400-R034** An incident record MUST contain a declared start time, current severity, affected scope, owner and known evidence.

**CDS1400-R035** Triage MUST distinguish symptom, impact and suspected cause.

**CDS1400-R036** If continued automation can increase impact, the relevant automation MUST be paused or constrained (using the R040 mechanisms) until safe operation is demonstrated.

## 15. Containment, Remediation and Automation Safeguards *(normative)*

Containment limits further impact; remediation restores correct operation. *Containment options (informative):* pause publication; disable one mapping or rule; freeze automation and PIM-side edits on a bounded product set; revert a dictionary or taxonomy version; remove or hide affected listings; switch AI or automation to manual approval; preserve an evidence snapshot before repair changes state.

**CDS1400-R037** Containment MUST prioritise prevention of additional incorrect propagation over speed of full repair.

**CDS1400-R038** Repair actions MUST identify whether they change canonical values, expected channel state, downstream channel state or verification records.

**CDS1400-R039** A bulk repair MUST support preview, bounded scope, evidence capture and post-repair verification.

**CDS1400-R040** For each automated pipeline stage operated in production — ingestion, enrichment, publication, automated repair and AI workflows — a mechanism to pause or constrain that stage MUST exist and be operable **before** the automation runs in production. Containment capability is a system requirement, not an improvisation during the first incident. *(Promotes the capability that v0.1 assumed implicitly in triage and containment steps.)*

## 16. Drift Diagnosis and Repair Selection *(normative)*

Drift is a difference between the governed expected state and the observed state. The drift cause taxonomy (EXTERNAL_EDIT, CHANNEL_NORMALISATION, MAPPING_CHANGE, STALE_PUBLICATION, CONNECTOR_DEFECT, UNKNOWN_CAUSE and the rest) is owned by CDS-500 §20; repair policies by CDS-500 §21. This section governs their operational use.

**CDS1400-R041** Repair policy MUST be selected from the diagnosed drift cause. **Republishing MUST NOT be assumed to be the correct repair**: republishing over an unauthorised external edit destroys the evidence of who changed what; republishing "fixes" a channel normalisation only until the next publish; republishing cannot repair a canonical defect, an observation defect or a transformation defect at all.

*Diagnosis-to-repair guide (informative, causes per CDS-500 §20):*

| Diagnosed cause | Typical correct repair family |
|---|---|
| EXTERNAL_EDIT | Preserve evidence, then republish or escalate per ownership contract; address the editing practice (§28.2). |
| CHANNEL_NORMALISATION | Register the normalisation (CDS-500 §16.2) and adjust comparator or expected state — not repeated republish. |
| MAPPING_CHANGE / transformation defect | Fix the mapping or transformation, re-project, then republish. |
| STALE_PUBLICATION / PARTIAL_PUBLICATION | Republish through the governed path; verify. |
| Observation defect | Fix read-back; the channel may be correct already. |
| Canonical defect | Correct the canonical value under governance; then re-project and publish. |
| Monitoring gap | Record `UNOBSERVABLE`; treat as owned risk, not as health. |

**CDS1400-R042** Automatic repair MAY be used only for explicitly authorised, deterministic and bounded drift conditions, within PIM-owned fields (CDS500-R078).

**CDS1400-R043** A repair MUST be followed by observation and verification before the incident or defect is closed (CDS500-R080).

## 17. Rollback, Replay and Recovery *(normative)*

Recovery restores a known-good operating state and confirms the data path is reliable. *Recovery sequence (informative):* contain; capture evidence and scope; select rollback, forward-fix or replay; validate on a bounded cohort; execute with traceable batch identity; observe; verify; restore paused automation gradually; monitor for recurrence.

**CDS1400-R044** Critical mappings, dictionaries, taxonomies and transformations SHOULD have a known rollback mechanism. Channel-side rollback is republication of known-good state through the governed publication path, not restoration of channel-internal state (definition and irreversibility classes: CDS-1300 §17).

**CDS1400-R045** Replay MUST be idempotent or otherwise protected against duplicate or destructive effects.

**CDS1400-R046** An incident MUST NOT be declared recovered solely because processing resumed; affected data MUST meet the defined verification exit criteria (declared thresholds per R015).

## 18. Communication and Stakeholder Management *(normative)*

Incident communication states what is known, what is not known, what is being done and when the next update will occur. *Minimum content by stage (informative):* initial declaration — severity, start time, known impact, scope, containment, next update time; progress — new evidence, changed scope or severity, actions completed, remaining risks; recovery — restored state, verification coverage, residual risk, monitoring period; closure — confirmed outcome, remediation, review and action ownership.

**CDS1400-R047** Communication MUST distinguish confirmed facts from hypotheses.

**CDS1400-R048** External notification decisions MUST follow legal, contractual, security and channel obligations.

**CDS1400-R049** Sensitive evidence MUST NOT be copied into broad communication channels when a controlled reference is sufficient.

## 19. Post-Incident Review *(normative)*

A post-incident review (PIR) converts an operational failure into durable learning. It reconstructs conditions and decisions without rewriting history after the outcome is known.

**CDS1400-R050** Every SEV-1 incident MUST receive a documented post-incident review (template: Appendix D.1). Every SEV-2 incident SHOULD receive at least a lightweight review (template: Appendix D.2). *(v0.1 mandated full PIRs for all SEV-2 incidents; under this chapter's SEV-2 definition that produces review-writing as a standing tax at small scale and reviews nobody reads at large scale. The SHOULD, with a template that takes minutes rather than hours, keeps the learning loop without the tax.)*

**CDS1400-R051** The review MUST identify contributing conditions and control gaps, not merely the final triggering action.

**CDS1400-R052** Corrective actions arising from a review MUST have named owners and tracked completion evidence.

**CDS1400-R053** A SEV-1 review MUST include at least one participant who was not the primary incident responder. *(Small-team profile: waived per Table 2-1 with sole-operator note and archived evidence.)*

> Informative note: a blameless review does not remove accountability. It separates learning about system conditions from disciplinary or conduct processes, which are handled separately when required.

## 20. Problem Management and Recurrence Prevention *(normative)*

Problem management addresses underlying causes or repeated patterns not fully resolved by individual incident repair. *Recurrence patterns worth a problem record (informative):* repeated mismatch in the same field or channel; recurring supplier schema change; growing dictionary quarantine or alias debt; repeated manual channel edits to PIM-owned fields; frequent alert suppression or false positives; repeated facet-cardinality regressions; recurring AI rejection patterns; multiple incidents sharing an undocumented dependency; thresholds missed across consecutive periods.

**CDS1400-R054** Recurring incidents SHOULD be linked to a problem record with an accountable owner and a long-term remediation plan.

**CDS1400-R055** A temporary workaround MUST have an expiry date, review date or retirement condition recorded at the time the workaround is adopted.

**CDS1400-R056** Known operational debt MUST remain visible in operational reporting until it is accepted, remediated or explicitly retired.

## 21. Change and Regression Monitoring *(normative)*

Most product-data incidents follow a change: supplier import, dictionary edit, taxonomy move, mapping release, bulk update, API version change, theme change, AI model change or staff-process change. *Change controls (informative):* pre-change baseline; change identifier linking the change to telemetry; canary or bounded cohort; regression tests (CDS-1000 suites, CDS-1200 fixtures); post-change comparison against baseline; observation window covering asynchronous publication and indexing; defined rollback trigger.

**CDS1400-R057** Material changes MUST be identifiable in operational telemetry (a change identifier linkable to affected events and records).

**CDS1400-R058** Dictionary, taxonomy, mapping and AI changes SHOULD receive the same regression discipline as code changes.

**CDS1400-R059** A change MUST NOT be considered successful until its downstream effects have been observed and compared against the pre-change baseline within the declared observation window, with results inside the declared thresholds (R015).

## 22. Continuous Improvement System *(normative)*

Continuous improvement turns operational evidence into prioritised change: prevent defects, detect earlier, reduce impact, recover faster, remove toil, improve usability, improve assurance. *(The improvement loop and class examples of v0.1 §21 are retained as informative practice.)*

```
Operational evidence -> trend and incident review -> identify control gap
    -> prioritise by impact and recurrence -> implement bounded change
    -> test and observe -> confirm improved outcome
    -> update standard, profile, runbook or training
```

**CDS1400-R060** Improvement work SHOULD be prioritised using impact, recurrence, risk and effort rather than anecdote alone.

**CDS1400-R061** Completed improvements SHOULD be measured against the outcome they were intended to change.

## 23. AI and Automation Monitoring *(normative)*

AI and automation require both output-quality monitoring and operational monitoring; high throughput does not imply high quality. AI governance — proposals, evidence classes, confidence, abstention, autonomy levels A0–A4 — is owned by CDS-700; this section defines only the operational measurement obligations. *Reference measures (informative):* proposal acceptance rate; human correction rate; out-of-dictionary rate; abstention rate; confidence calibration; evidence coverage; override and rollback rate; model or prompt drift; automation blast radius.

**CDS1400-R062** AI monitoring segmentation MUST scale with the declared autonomy level of each workflow, exactly as defined by CDS700-R081: segmented monitoring distinguishing AI-originated from human-originated values is MUST for A3/A4 workflows, SHOULD for A2, and MAY be limited to volume and sampled quality checks for A1. This chapter supplies the mechanics; CDS-700 owns the scaling rule.

**CDS1400-R063** AI quality MUST be measured against reviewed outcomes, not the model confidence value alone.

**CDS1400-R064** A material decline in quality or an increase in prohibited output MUST trigger containment proportional to the workflow's autonomy level (CDS-700), using the pause/constrain mechanisms required by R040.

## 24. Customer-Experience Signals *(normative)*

Customer-experience health is the hardest domain to observe: most storefronts and marketplaces do not expose interaction telemetry to the PIM side. CDS therefore distinguishes signals computable from governed data from signals requiring channel telemetry.

**CDS1400-R065** Facet cardinality and zero-result **construction** (facet values whose product set is empty by construction) MUST be monitored. These are the minimum customer-experience signals: they are computable PIM-side from governed dictionaries, facet projections and product data, on every channel, with no storefront telemetry required (facet rules: CDS-600).

**CDS1400-R066** Interaction-derived signals — search failure rates, zero-result filter *interactions*, navigation abandonment — are **conditionally observable**. Each channel profile MUST declare whether interaction telemetry is available; where it is not, customer-experience health MUST be reported as a declared monitoring gap for those signals, never assumed healthy.

**CDS1400-R067** Where interaction telemetry is available, it SHOULD be monitored. Interaction-metric monitoring is otherwise profile-optional and MAY be bound to the customer-experience overlay profile (CDS-1000).

## 25. Security, Privacy and Evidence Retention *(normative)*

Monitoring and incident records may contain supplier pricing, unpublished product information, credentials, customer-impact evidence or internal system details. *Practice checklist (informative):* least-privilege access to dashboards, logs and incident records; tenant-scoped telemetry and evidence; redaction or tokenisation of secrets and unnecessary personal data; controlled export and sharing; audit-integrity and timestamp preservation; retention matched to contractual, legal and operational needs; legal hold where required; secure deletion after expiry; monitoring tools reviewed as part of the security boundary.

**CDS1400-R068** Monitoring data MUST follow the same tenant-isolation and access-control principles as product data (CDS-800 §19).

**CDS1400-R069** Secrets, authentication tokens and sensitive personal data MUST NOT be intentionally recorded in general operational telemetry.

**CDS1400-R070** Incident evidence retention MUST be governed and documented.

## 26. Operating Cadence and Review *(normative)*

*Cadence catalogue (informative — a menu, not a mandate):*

| Cadence | Typical review |
|---|---|
| Continuous / event-driven | Critical alerts, publication failures, security events, threshold breaches. |
| Daily | Failed jobs, stale sources, oldest quarantines, unresolved high-impact mismatches. |
| Weekly | Quality trends, workflow backlog, mapping debt, recurring alerts, action progress. |
| Monthly | Objectives/thresholds, incident trends, customer-experience metrics, AI quality, monitoring gaps. |
| Quarterly | Dictionary and taxonomy health, conformance posture, access review, recovery readiness. |
| After material change | Regression review and post-change comparison (§21). |
| After qualifying incident | Post-incident review and action tracking (§19). |

**CDS1400-R071** The operating model MUST include, at minimum: **(a)** one recurring operational review, at a declared cadence, with recorded outcomes and tracked actions; and **(b)** a defined post-incident review path (§19). *(v0.1 mandated five governed review forums; that is enterprise practice, not a conformance floor. One honest recurring review that produces decisions beats five that produce minutes.)*

**CDS1400-R072** A recurring review that repeatedly produces no decisions, ownership or follow-up SHOULD be redesigned or retired — the same self-limiting rule that governs alerts (R027). Reviews are for decisions, not attendance.

## 27. Conformance *(normative)*

Conformance levels, test suites, outcomes and claim rules are owned by CDS-1000. A CDS-1400 conformance claim is a claim against the requirement set CDS1400-R001–R072 (with the Table 2-1 substitution where the small-team profile is declared, and the R007 upgrades where the enterprise operations profile is declared), evidenced per CDS-1000.

The recommended practices of this chapter — service objectives and error budgets (§7), separated dashboard audiences (§10), telemetry correlation and versioned reason codes (§9), canary releases (§21), the continuous-improvement loop (§22), AI calibration monitoring (§23), interaction-metric monitoring (§24) and tested runbooks (Appendix C) — are SHOULD-level and MAY be cited as supporting evidence in a claim. *(v0.1's conformance list restated several of these SHOULDs as MUSTs; this section now matches the strengths of the requirements it summarises — finding 1400-8.)* The testable operational-debt controls remain MUST: workaround expiry (R055) and visible known debt (R056).

## 28. Worked Incident Scenarios *(informative)*

### 28.1 Colour Facet Explosion

**Signal.** Colour facet cardinality rises from 12 to 87 after a supplier import (R065).
**Triage.** Canonical colour dictionary remains valid; the import bypassed alias mapping; raw supplier shades were published as facet values.
**Containment.** Pause affected collection facet publication; revert the facet projection to the last known-good dictionary version.
**Repair.** Quarantine unknown shades (they stay in the denominator — R013); map approved aliases; republish facet values; verify counts and collection filtering.
**Prevention.** Facet-cardinality regression test; alert on raw-to-facet ratio change.

### 28.2 Channel Metafield Drift (SEV-2)

**Signal.** Verification of the material field on a Shopify channel reports 430 `MISMATCH` results. Expected `Linen`, observed `Cotton`; recent change: a manual bulk edit in the channel admin. Diagnosed drift cause: `EXTERNAL_EDIT` (CDS-500 §20).

**Response.**
- Declare SEV-2: customer-visible incorrect material claims.
- Preserve the observation snapshot **before** repairing — republishing first would destroy the evidence of what was edited and when (R041).
- Confirm PIM canonical values are correct (rule out a canonical defect masquerading as drift).
- Republish a bounded cohort through the governed path; observe and verify; then repair the remainder in batches (R039, R043).

**Follow-up — with real mechanisms.** "Freeze affected channel edits" is not an operation most platforms provide; the platform cannot lock a merchant-editable metafield against admin users. The real controls are:

- **Staff instruction and training** — operators are told, specifically, which channel-admin edits will be overwritten or treated as drift (this is the CDS1300-R051 training obligation applied in run-state).
- **Permission narrowing** — restrict which staff accounts hold channel-admin roles that can edit products/metafields at all; this is coarse (role-level, not field-level) but is an enforceable platform mechanism.
- **App-owned namespaces** — move PIM-owned metafields into an app-owned namespace, which admin users cannot edit. **Trade-off:** app-owned metafields are also not visible to merchants in the admin UI, so staff lose the ability to *see* the governed values in their daily tool, which can itself cause errors and shadow spreadsheets.
- **Drift detection stays armed regardless** — enforcement may be detection-only, and that is a legitimate declared posture (CDS1300-R014(c)).

> RESOLVED — accepted as drafted (owner 2026-08-04; was D17 (resolved)): For PIM-owned channel metafields there is an unresolved tension between **app-owned namespaces** (edit-proof but invisible to merchant staff) and **merchant-visible metafields** (visible and editable, so protected only by permissions, training and drift detection). This chapter permits either posture provided it is declared per channel profile with its residual risk; the alternative — mandating app-owned namespaces for all PIM-owned fields — was rejected because operator visibility loss is itself an error source.

### 28.3 Supplier Feed Staleness

**Signal.** No successful stock-source event for 28 hours; expected cadence is daily (absence-of-expected-event alert).
**Triage.** Supplier portal changed HTML format; canonical descriptions and prices unaffected; stock values now stale.
**Containment.** Flag source freshness as stale; prevent stale stock from being represented as freshly verified; notify purchasing and channel operations.
**Repair.** Update the parser; run a bounded extraction test; replay the source load (idempotent — R045); verify quantity and publication effects.
**Prevention.** Keep the absence alert; add a parser fixture from a supplier sample.

### 28.4 AI Material Misclassification

**Signal.** Human correction rate for AI material extraction rises from 4% to 21% after a model change (segmented monitoring per R062 localises it).
**Triage.** Decline limited to homewares image-only extraction; the model confuses rattan-look resin with natural rattan.
**Containment.** Reduce autonomy to proposal-only for the affected task (containment proportional to autonomy — R064, CDS-700); require text evidence or human review.
**Repair.** Revert the model version or update evidence rules; re-evaluate unreviewed proposals.
**Prevention.** Benchmark fixtures for imitation materials; quality gate by product family and evidence class.

## 29. Architecture Decisions *(informative)*

Per CDS000-R006, ADRs live in the single global register. Decisions originating in this chapter, recorded there: monitor data correctness as an operational service; keep observation coverage separate from match rate; base severity on impact, not record count; require verification after repair; treat reference-data and AI changes like code changes; make continuous improvement evidence-driven; prescribe no universal numeric objectives (profiles may). The v0.1 record CDS-ADR-1400-003 (detailed statuses beneath traffic lights) is **subsumed by ADR-D3**, whose normative expression is CDS-500 §17–§18; v0.1 Appendix E (five-colour palette including BLUE) is superseded — see the note after Appendix D.

## Appendix A — Reference Metric Catalogue *(informative)*

| Metric | Definition | Dimensions | Type |
|---|---|---|---|
| source_freshness_age | Age since last successful authoritative source update | source, organisation | duration |
| ingestion_failure_rate | Failed eligible source records / attempted eligible source records | source, batch | rate |
| canonical_required_completeness | Populated required fields / required eligible fields | family, category | rate |
| dictionary_unmapped_rate | Unmapped reference values / distinct eligible reference values | dictionary, source | rate |
| quarantine_backlog | Records currently awaiting governed resolution | queue, owner | count and age |
| publication_lag | Canonical approval to channel acknowledgement | channel, category | duration distribution |
| publication_failure_rate | Failed publication records / attempted eligible records | channel, reason | rate |
| observation_coverage | Observed expected fields / observable expected fields | channel, field | rate |
| verification_match_rate | `MATCH` results / observed expected fields | channel, field | rate |
| unresolved_mismatch_age | Age of unresolved `MISMATCH` | channel, severity | duration distribution |
| facet_cardinality | Distinct facet values exposed | facet, collection | count |
| zero_result_combination_rate | Zero-result filter interactions / filter interactions *(conditionally observable — §24)* | facet, collection | rate |
| ai_correction_rate | Materially corrected accepted proposals / accepted proposals | task, model | rate |
| incident_mtta | Declaration time minus detection time | severity, class | duration |
| incident_mttr | Verified recovery time minus declaration time | severity, class | duration |
| incident_recurrence_rate | Recurring incidents / closed incidents | class, period | rate |

## Appendix B — Severity and Response Matrix *(informative)*

The **minimum-roles column describes the enterprise operations profile (R007)**; it is informative illustration for all other adopters — every role is a hat holdable by one person (§2).

| Severity | Response expectation | Minimum roles *(enterprise profile — informative)* | Communication | Exit condition |
|---|---|---|---|---|
| SEV-1 | Immediate (coverage per R033) | Incident commander; technical/data lead; communications; business owner; security/compliance as relevant | Continuous coordination until contained; frequent updates | Verified containment and business approval to downgrade |
| SEV-2 | Urgent | Incident commander; owning technical/data team; channel/business owner | Regular updates during active response | Material impact stopped; verified recovery plan operating |
| SEV-3 | Prompt business-hours response unless risk increases | Owning team and data/channel owner | Updates at agreed milestones | Scope corrected or controlled workaround accepted (with expiry — R055) |
| SEV-4 | Normal queue | Named owner | Status through work management | Fix, acceptance or explicit retirement |

> Informative note: profiles or organisations may define numeric acknowledgement and restoration targets. Targets should be realistic, measured and reviewed, not copied without operational capacity.

## Appendix C — Runbook Template *(informative)*

| Section | Content |
|---|---|
| Runbook identity | Name, owner, version, last tested date, applicable services. |
| Trigger | Alert conditions, reason codes, scope. |
| Safety checks | Actions not to be taken without approval; data or channel risks. |
| Triage | Queries, dashboards, record samples, recent-change checks. |
| Containment | Safe ways to stop propagation, including the R040 pause mechanisms for each stage. |
| Repair | Deterministic repair, rollback or replay procedure. |
| Verification | Expected observations, comparison strategy, exit criteria. |
| Escalation | Contacts, severity triggers, external obligations. |
| Evidence | Required snapshots, batch IDs, logs, decision records. |
| Recovery | How paused automation is restored and monitored. |
| Known limitations | Unobservable fields, manual dependencies, unsupported scenarios. |

## Appendix D — Post-Incident Review Templates *(informative)*

### D.1 Full review (SEV-1 — R050)

Incident identifier, title, severity and dates; executive summary; impact and affected populations; detection and declaration; timeline; expected controls and actual behaviour; contributing factors; containment and recovery; verification evidence; what went well; what made response difficult; corrective and preventive actions; owners, due dates and completion evidence; recurrence indicators and review date; changes to CDS profiles, runbooks, tests or training.

### D.2 Lightweight review (SEV-2 — R050)

One page or less:

```
Incident:        <id, title, SEV-2, dates>
What happened:   <two or three sentences>
Impact:          <affected products/fields/channels/customers>
Why:             <contributing conditions and the control gap, not just the trigger>
Fixed by:        <repair + verification evidence reference>
Prevent next:    <0..3 actions, each with an owner and a date>
Recurrence of:   <link to problem record, or "first occurrence">
```

---

**Appendix E of v0.1 is deleted.** Traffic-light presentation is single-homed in **CDS-500 §18** (implementing ADR-D3): GREEN/AMBER/RED plus optional GREY, whose denominator semantics are preserved there — `NOT_APPLICABLE` is never a success state and is excluded from success denominators either way (CDS500-R069). v0.1's **BLUE / INFORMATIONAL tier is dropped** from the standard; in-flight badging remains a local presentation choice with no conformance meaning (CDS-500 §18 note). The accessibility rule survives strengthened as CDS1400-R024 (colour never the only signal, in any operational view) alongside CDS500-R072.

END OF CDS-1400 v0.2 REVIEW DRAFT


<div class="chapter"></div>

# Commerce Data Standard (CDS)
## CDS-1500 — Apparel and Homewares Industry Profiles and Reference Dictionaries

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-1500 Working Draft v0.1 and the CDS-1500 Starter Reference Dictionaries v0.1 package structure (data content carried forward, restructured per Appendix E) |
| Normative status | §1, §2, §4, §5, §7–§13, §15–§18, §23, §24 and Appendices A–B are normative. §3, §6, §14, §19–§22, §25, §26 and Appendices C–F are informative. Every table is individually marked. |
| Primary audience | Merchandisers, data stewards, ecommerce operators, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1400, especially CDS-200, CDS-300, CDS-400, CDS-500, CDS-600, CDS-900 and CDS-1100 |
| Companion package | CDS Reference Dictionary (unified informative starter data; column contract in Appendix E) |
| Profile identifiers | `cds.profile.apparel.v0_2` and `cds.profile.homewares.v0_2` |
| Findings addressed | CDS-1500-1..8; CDS-400-3 and DICT-2 (colour-baseline ownership, D11); CDS-600-3 (zero-result rule re-homed); DICT-1..17; Matrix 2 and Matrix 5 deduplication; ADR-D3, ADR-D4, ADR-D24; D12 (partial — see OPEN flag), D28 (as resolved in CDS-400) |

Terminology in this chapter follows CDS-100. In particular, the v0.1 term "reference value" is retired (CDS100-R003); this chapter uses **Source Value → Alias Mapping Record → Canonical Value → Projections** per ADR-D4.

---

## 1. Purpose and Scope *(normative)*

CDS-1500 defines two interoperable industry profiles for a commerce catalogue whose primary range is apparel and accessories and whose secondary range includes lifestyle homewares. It translates the vendor-neutral CDS architecture into concrete product-family schemas, dictionary bindings, facet baselines and publishing expectations. **CDS-1500 is the owning chapter for the colour facet baseline** (Appendix C); CDS-400 and CDS-600 cite it and MUST NOT restate divergent copies *(resolves CDS-400-3/DICT-2 in this chapter's favour, decision D11)*.

**CDS1500-R001** An implementation claiming the Apparel Profile MUST distinguish product identity, sellable variants, canonical attributes, display labels, customer facets and channel representations, per the value-layer model of CDS-400 and CDS-100 §3.

**CDS1500-R002** An implementation claiming the Homewares Profile MUST store dimensions, capacity and other measurable specifications as typed values with declared units rather than uncontrolled text.

**CDS1500-R003** An industry profile MUST NOT force every possible attribute onto every product. Requiredness MUST be defined per product family and category profile.

**CDS1500-R004** A retailer MAY extend the baseline dictionaries, but MUST preserve stable identifiers, aliases, mappings and deprecation history (change control per CDS-400 and CDS-800).

## 2. Industry Profile Model *(normative)*

```
CDS Core
  -> Industry Profile
       -> Product Family
            -> Category Profile
                 -> Attribute Definitions
                 -> Requiredness Rules
                 -> Dictionary Assignments
                 -> Facet Projection Rules
                 -> Channel Mappings
```

**CDS1500-R005** Every profile MUST identify which attributes are inherited common attributes and which are category-specific.

**CDS1500-R006** A category profile MUST declare a requirement level (§4) for each attribute it governs.

**CDS1500-R007** Attributes that create distinct sellable units MUST be modelled at variant scope; descriptive attributes MUST remain at product scope unless values genuinely differ by variant (variant boundary rule: CDS-200 §5).

## 3. Shared Product Information Layers *(informative)*

| Layer | Purpose | Examples | Normative home |
|---|---|---|---|
| Identity | Stable commercial identity | Product ID, SKU, brand, MPN, GTIN | CDS-200 |
| Classification | What the product is | Family, type, internal category, external taxonomy mappings | CDS-200 §6 |
| Canonical attributes | What the product is like | Material, colour, pattern, fit, room, finish | CDS-200 §7, CDS-400 |
| Variant attributes | What creates a sellable unit | Size, sellable colour, pack count | CDS-200 §5 |
| Content | How it is explained | Title, description, features, care, dimensions | CDS-200 |
| Facet projection | How customers filter | Blue, Linen, Relaxed, Living Room, Wood | CDS-600 |
| Channel projection | How a destination receives it | Metafield-like structures, CH_google_color, marketplace category | CDS-500, CDS-900 |
| Verification | Whether the destination matches expectation | Statuses and traffic lights per the single normative enum in CDS-500 §17 | CDS-500 |

**CDS1500-R008** A single product fact SHOULD be entered canonically once and reused across display, search, facets, collections and channel mappings.

## 4. Attribute Requirement Levels *(normative)*

| Code | Meaning | Publication consequence |
|---|---|---|
| R — Required | Every active product in the profile must contain a valid value. | Publication is blocked when absent or invalid (preflight per CDS-500). |
| C — Conditional | Required when a declared condition is true. | Publication is blocked only when the condition applies. |
| REC — Recommended | Expected for strong customer experience and channel quality. | Warning or quality deduction when absent; never blocking. |
| O — Optional | Useful but not expected for every product. | No consequence when absent. |
| N/A | Not applicable to the product family. | Field is hidden or ignored. |

*The v0.1 code "P – Recommended" is replaced by REC; codes now read unambiguously alongside RFC-2119 keywords (resolves CDS-1500-8's companion code finding).*

**CDS1500-R009** Requiredness MUST be evaluated against the product family and category profile, not against a universal flat field list.

**CDS1500-R010** A value of unknown or not-supplied MUST NOT be fabricated to satisfy requiredness (quarantine per CDS-400 §17; abstention per CDS-700).

**CDS1500-R011** Where a requirement level applies to a dictionary-bound field, the requirement binds to **a governed dictionary conforming to CDS-400** (stable value_ids, lifecycle, provenance). The seed baselines in Appendices C–D and the companion CSV package are **informative starter data**: an organisation MAY adopt them verbatim as the initial content of its governed dictionaries, at which point they become governed data under that organisation's control. *(Resolves CDS-1500-3: normative requirement levels no longer bind to informative value sets.)*

## 5. Apparel Product Model *(normative)*

The Apparel Profile treats the Product as the shared style or design and the Variant as the sellable combination of option values. A shirt offered in four sizes and three colours is normally one Product with twelve Variants, provided the descriptive design and construction remain substantially shared.

*Sellable colour* means the colour-bearing variant option value that identifies a distinct sellable unit — a Variant Option in CDS-100 terms, stored as a canonical value_id.

**CDS1500-R012** Size and sellable colour SHOULD be variant attributes when they identify distinct sellable units.

**CDS1500-R013** Where colour is variant-defining, the variant field MUST store the canonical value_id (e.g. `VAR_colour = colour_french_navy`); the product-scope display label and facet value are projections derived from the variants' canonical values, never independently authored parallel facts. *(Per ADR-D4; resolves CDS-1500-6.)*

**CDS1500-R014** Display colour, canonical colour and facet colour MUST remain related but distinct values where the richer display name differs from the broad customer filter (layer model: CDS-400; retained from v0.1).

**CDS1500-R015** A product SHOULD NOT be split into separate products solely to obtain separate product pages. An organisational profile MAY declare a variants-as-products merchandising model, in which case it MUST preserve family relationships between the split products. *(Informative note: variants-as-products was deliberate legacy production architecture — a supported declared pattern, not an anti-pattern; see REVIEW-002A LEG-8.)*

```
Product: Relaxed Linen Shirt            (informative example)
  Product scope:
    CAT_product_type = shirt
    MF_material_primary = linen
    MF_fit = relaxed
    MF_sleeve_length = long
    MF_neckline = collar
  Variant scope:
    VAR_colour = colour_french_navy     # canonical value_id
    VAR_size = au_10
    STD_sku = SHIRT-FN-10
```

## 6. Apparel Product Families and Category Profiles *(informative baseline; the inheritance rule is normative)*

| Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|
| Tops and shirts | material composition; sellable colour; size | fit; sleeve length; neckline/collar; pattern; care | size, colour |
| Dresses and jumpsuits | material composition; sellable colour; size | dress length; sleeve length; neckline; fit; occasion; lining | size, colour |
| Knitwear | material composition; sellable colour; size | knit type; weight; fit; neckline; care | size, colour |
| Jackets and coats | material composition; sellable colour; size | outer material; lining; insulation; closure; weather properties | size, colour |
| Pants and jeans | material composition; sellable colour; size | rise; leg shape; fit; inseam; stretch; closure | waist/size, length, colour |
| Skirts and shorts | material composition; sellable colour; size | length; rise; fit; closure; lining | size, colour |
| Activewear | material composition; sellable colour; size | activity; support; compression; moisture properties | size, colour |
| Swimwear | material composition; sellable colour; size | coverage; support; lining; chlorine resistance | size, colour |
| Sleep and lounge | material composition; sellable colour; size | fit; set contents; warmth; care | size, colour |
| Scarves, hats and soft accessories | material composition; sellable colour | dimensions; construction; season; pattern | colour, size where sellable |

**CDS1500-R016** Profile attributes MAY be inherited from a parent family, but category-specific requirements MUST remain explicit in the category profile.

## 7. Apparel Colour Architecture *(normative; the worked chain is informative)*

Colour uses the four-layer value model (ADR-D4): the source value is preserved with provenance, an alias mapping resolves it to a canonical shade, and display, facet, search and channel forms are parallel projections of the canonical value.

```
Source Value:            "French Navy"      (supplier text, preserved verbatim with provenance)
Alias Mapping Record:    "French Navy" -> colour_french_navy   (dictionary_key: colour)
Canonical Value:         colour_french_navy (code french_navy, status active)
Projections:
  Display Label:         French Navy
  Facet Value:           blue               (single facet; ordered list where multiple)
  Search Synonyms:       french navy, dark navy
  Channel:               CH_google_color = "Blue"   (feeding layer declared per attribute)
```

*An organisation preferring coarser canonicals MAY instead alias "French Navy" to canonical `colour_navy` and keep "French Navy" as display label only. Both granularities are conformant (ADR-D4).*

**CDS1500-R017** The customer colour facet MUST use a deliberately limited colour-family dictionary governed under CDS-400, not the full set of source or display values. (Seed baseline: Appendix C.)

**CDS1500-R018** The canonical shade SHOULD remain more specific than the facet, because content, search, swatches and channel mappings need the specificity the facet deliberately discards.

**CDS1500-R019** A canonical shade MAY belong to more than one colour facet only where its governed dictionary entry declares an **ordered facet list, primary first** (e.g. teal → `green|blue`), per the facet-order rule as resolved in CDS-400 (D28). Facet membership is declared in the dictionary, never decided per product.

**CDS1500-R020** Facet membership MUST be deterministic at dictionary level. Shade names whose real-world appearance spans facet families MUST be split into distinct canonical shades, one per facet, with intake resolved through alias mappings (which MAY be supplier- or locale-scoped per ADR-D4). The seed baseline applies this split: **charcoal_grey** (facet grey) vs **charcoal_black** (facet black); **rust_orange** (facet orange) vs **rust_brown** (facet brown); **tan_beige** (facet beige) vs **tan_brown** (facet brown). Bare source values ("Charcoal", "Rust", "Tan") map by default alias to charcoal_grey, rust_orange and tan_beige respectively; a supplier whose shade reads otherwise gets a supplier-scoped alias to the sibling canonical. *(Resolves CDS-1500-1: the v0.1 "may map to Grey unless visually near-black" judgement notes are deleted.)*

**CDS1500-R021** A product-level facet override (assigning a product a facet other than its canonical shade's dictionary mapping) MAY exist only as a governed override record with provenance, owner and reason, per the override model of CDS-500 §22. It never silently edits the dictionary mapping.

> RESOLVED (was D12 (resolved), owner decision 2026-08-04): product-level facet overrides are **kept**, exceptional, provenance-carrying. Schema home: the **CDS-500 §22 override record** (one override mechanism corpus-wide — same record family as field and taxonomy overrides); no separate CDS-400 mapping-exception record is introduced.

**CDS1500-R022** A multi-colour product MUST NOT be assigned to every colour present in a complex print. The canonical layer records the dominant and/or component shades; **multicolour is a facet/status value only, never a canonical shade** (ADR-D4; resolves CDS-1500-4). An organisational profile MAY define a dominant-colour extraction rule for prints.

## 8. Apparel Fibre, Fabric and Composition *(normative; seed table informative)*

Apparel material data is separated into fibre composition, fabric or construction, and product components. This prevents common category errors such as treating Denim, Jersey or Satin as fibre types. *(Preserved from v0.1 — ADR-1500-003.)*

| Field | Meaning | Example |
|---|---|---|
| MF_fibre_composition | Percentage composition of fibres | 55% Linen; 45% Cotton |
| MF_material_primary | Primary canonical fibre/material | Linen |
| MF_fabric_type | Fabric construction or named textile | Denim, Jersey, Twill, Satin |
| MF_surface_treatment | Finish or treatment | Garment-dyed, Brushed, Washed |
| MF_lining_material | Lining composition when present | 100% Viscose |
| MF_fill_material | Insulation or fill | Recycled Polyester Fill |
| MF_stretch | Stretch behaviour | None, Slight, Moderate, High |

**CDS1500-R023** Composition percentages MUST be numeric values associated with canonical material identifiers and SHOULD total 100 percent per component.

**CDS1500-R024** Fabric type MUST NOT replace fibre composition.

**CDS1500-R025** Marketing claims such as organic, recycled or certified MUST be stored separately from the underlying material identity (fields: §11) and MUST require supporting evidence. Consequences for facets *(resolves CDS-1500-2)*:
- A **"Recycled" customer facet is claim-driven**: it derives from `MF_recycled_content_percent` (and its evidence), never from a material family. `recycled_polyester` remains a canonical material where supply-chain identity warrants it, but its material family is `synthetic` and its material facet is Polyester.
- **Elastane is family `synthetic` with no material facet**; stretch is a garment property expressed through `MF_stretch`, not a material family. A "Stretch" filter, where offered, is a property facet fed by `MF_stretch`.
- The v0.1 facet label "Other Natural" is deleted (CDS-600 forbids Other/General/Misc facet labels); hemp gets its own facet, `hemp`.

Seed material table *(informative — governed adoption per CDS1500-R011; material facet ids reference the material_facets seed, Appendix D)*:

| Canonical material | Alias | Family | Material facet |
|---|---|---|---|
| cotton | — | plant_fibre | cotton |
| organic_cotton | — | plant_fibre | cotton *(organic claim still requires MF_organic_claim evidence)* |
| linen | — | plant_fibre | linen |
| hemp | — | plant_fibre | hemp |
| wool | — | animal_fibre | wool |
| merino_wool | — | animal_fibre | wool |
| cashmere | — | animal_fibre | cashmere |
| silk | — | animal_fibre | silk |
| viscose | rayon | regenerated_cellulose | viscose |
| lyocell | — | regenerated_cellulose | lyocell |
| modal | — | regenerated_cellulose | modal |
| polyester | — | synthetic | polyester |
| recycled_polyester | — | synthetic | polyester *(Recycled facet claim-driven, see R025)* |
| nylon | polyamide | synthetic | nylon |
| acrylic | — | synthetic | synthetic |
| elastane | spandex | synthetic | — *(property: MF_stretch)* |
| leather | — | animal_material | leather |
| suede | — | animal_material | leather |
| faux_leather | vegan leather | synthetic | faux_leather |

## 9. Apparel Size, Fit and Garment Measurements *(normative; seed table informative)*

Size labels are not globally interchangeable. CDS stores the supplied sellable label, the applicable size system, a stable sort key and optional body or garment measurements.

| Field | Scope | Example |
|---|---|---|
| VAR_size_label | Variant | 10, M, 32, EU 40 |
| VAR_size_system | Variant or product | AU_WOMENS_NUMERIC, ALPHA, EU_FOOTWEAR |
| VAR_size_sort_key | Variant | 030, 040, 050 |
| MF_size_chart_id | Product | sizechart_brand_womens_tops_2026 |
| MF_fit | Product | Relaxed |
| MF_garment_length_mm | Product or variant | 720 |
| MF_inseam_mm | Product or variant | 780 |
| MF_model_wears_size | Content metadata | AU 8 / Small |

**CDS1500-R026** A size conversion MUST NOT be presented as exact unless a brand- or product-specific size chart supports it. *(Preserved — ADR-1500-007: no universal exact size conversion.)*

**CDS1500-R027** Size labels MUST be sortable independently of alphabetical order (sort keys or an equivalent declared mechanism).

**CDS1500-R028** Fit describes intended silhouette relative to the size specification; it MUST NOT be used as a substitute for size.

Seed fit dictionary *(informative)*: skinny, slim, regular, relaxed, oversized, tailored, straight, tapered, wide_leg, bootcut, cropped, longline, fitted, loose.

## 10. Apparel Pattern, Style, Occasion and Season *(normative; seed tables informative)*

Pattern, style and occasion are separate controlled concepts. A floral garment may be romantic, resort or casual; the pattern does not define the style by itself.

| Dictionary | Purpose | Examples |
|---|---|---|
| Pattern | Visible repeat or motif | Plain, Striped, Checked, Floral |
| Style | Aesthetic or merchandising language | Classic, Minimal, Bohemian, Resort |
| Occasion | Customer use context | Work, Casual, Formal, Travel, Beach |
| Season relevance | Merchandising relevance, not lifecycle | Summer, Winter, Transitional, All-year |
| Weather suitability | Functional environmental use | Warm weather, Cold weather, Rain |

**CDS1500-R029** Style and occasion MAY be multi-value attributes but SHOULD enforce a declared maximum value count per product to prevent indiscriminate tagging.

**CDS1500-R030** Season relevance MUST NOT be conflated with a collection campaign or product lifecycle status.

Seed pattern dictionary *(informative)*: plain, striped, checked, plaid (alias: tartan), floral, animal, geometric, abstract, paisley, polka_dot, graphic (alias: placement print), colour_block, motif. *Note (DICT-17): the v0.1 entries `textured` and `marbled` are surface textures, not print patterns; they are re-homed as finish/surface values (§17 finishes for homewares, MF_surface_treatment for apparel). `plain` doubles as "no pattern"; organisations wanting the distinction may add an explicit `none` value.*

Seed style dictionary *(informative)*: classic, minimal, modern, contemporary, casual, formal, romantic, bohemian, coastal, resort, streetwear, athleisure, workwear, vintage_inspired, scandinavian, industrial, rustic, country, luxury.

Seed occasion dictionary *(informative)*: everyday, work, casual, formal, party, wedding_guest, travel, holiday, beach, active, outdoor, lounge.

## 11. Apparel Care, Origin and Claims *(normative)*

| Attribute | Requirement guidance | Control |
|---|---|---|
| MF_care_instructions | REC for all apparel; R where special care applies | Structured symbols plus human-readable text where possible |
| MF_country_of_origin | C on legal, channel or organisational requirements | Governed country reference |
| MF_certifications | O unless a claim is made | Reference evidence and expiry or scope |
| MF_recycled_content_percent | R when a quantified recycled claim is published | Numeric, component-aware |
| MF_organic_claim | R when organic is claimed | Evidence source and applicable component |
| MF_animal_material | C for leather, wool, silk, down and similar | Canonical material plus care/compliance controls |

**CDS1500-R031** Claims MUST remain distinct from descriptive attributes and MUST NOT be inferred from supplier marketing language without evidence (evidence classes: CDS-700 §7).

**CDS1500-R032** The profile MUST support withdrawal or expiry of a claim without changing the canonical material identity.

## 12. Footwear and Accessories Extension *(informative baseline; R033 normative)*

| Category | Required | Recommended | Variant options |
|---|---|---|---|
| Footwear | size; size system; sellable colour; upper material | sole material; lining; closure; heel height; width; toe shape | size, colour, width |
| Bags | sellable colour; primary material | dimensions; strap; closure; compartments; capacity | colour, size where applicable |
| Belts | size; sellable colour; primary material | width; buckle material; closure | size, colour |
| Jewellery | primary material; colour/finish | dimensions; stone; plating; closure; care | finish, size where applicable |
| Hats | size or adjustable status; sellable colour; material | brim, crown, fit, care | size, colour |

**CDS1500-R033** Footwear size systems MUST be identified explicitly and MUST NOT be merged into a single unqualified number.

## 13. Homewares Product Model *(normative)*

The Homewares Profile covers lifestyle products used in rooms and domestic settings. It emphasises typed measurements, material and finish separation, product composition, pack contents and use context.

```
Product: Stoneware Table Lamp           (informative example)
  CAT_product_type = table_lamp
  MF_material_primary = stoneware
  MF_finish = glazed
  MF_colour_canonical = colour_oatmeal
  MF_colour_display = Oatmeal
  MF_colour_facet = beige
  MF_room = [living_room, bedroom]
  MF_height_mm = 520
  MF_width_mm = 280
  VAR_plug_type = AU
  VAR_voltage = 230 V
```

**CDS1500-R034** Dimensions, weight, capacity, power and other measures MUST be typed values with declared units.

**CDS1500-R035** Material and finish MUST be separate attributes wherever the same material may appear in multiple finishes.

**CDS1500-R036** Room and style are merchandising attributes and MUST NOT replace functional product classification (CDS-200 §6).

*Electrical compatibility fields use `VAR_plug_type` (the v0.1 variant spelling `VAR_plug_profile` is retired — resolves CDS-1500-8 / CLEANUP-PASS B.7).*

## 14. Homewares Product Families and Category Profiles *(informative)*

| Product family / category | Required | Recommended | Typical variants |
|---|---|---|---|
| Cushions and decorative pillows | dimensions; cover material; colour | fill material; closure; removable cover; pattern; room | colour, size, insert option |
| Throws and blankets | dimensions; material composition; colour | weight/warmth; weave; pattern; care | colour, size |
| Bedding | bed size; material composition; colour; set contents | thread count; weave; closure; care | size, colour |
| Towels and bath textiles | dimensions; material composition; colour | weight/GSM; absorbency; set contents; care | size, colour, pack |
| Rugs and mats | dimensions; primary material; colour | pile height; construction; backing; indoor/outdoor; care | size, colour |
| Candles and home fragrance | product type; net weight/volume; fragrance; burn/diffusion metric | wax type; vessel material; notes; safety; refillability | fragrance, size |
| Vases and decor | dimensions; primary material; colour | finish; shape; room; style; handmade status | colour, size |
| Tableware and serveware | product type; material; dimensions/capacity; set count | finish; microwave/dishwasher suitability; food contact | colour, size, set count |
| Drinkware | capacity; material; set count | thermal properties; dishwasher suitability; lid/straw | colour, capacity, pack |
| Storage and baskets | dimensions/capacity; material | lid; handle; stackability; room; load guidance | colour, size |
| Lighting | type; dimensions; electrical compatibility | material; finish; bulb base; max wattage; dimmable; cable length | colour/finish, plug type |
| Outdoor lifestyle | dimensions; material; outdoor suitability | UV/water resistance; storage; care; assembly | colour, size |

## 15. Homewares Material and Construction *(normative; seed table informative)*

Homewares material data often describes multiple components. The profile supports primary material, component materials and surface finish without flattening them into one tag.

| Field | Purpose | Example |
|---|---|---|
| MF_material_primary | Dominant structural or customer-relevant material | Oak |
| MF_material_components | Named component-material relationships | Frame: Oak; Handle: Brass |
| MF_material_facet | Broad customer filter (governed material facet dictionary, Appendix D seed) | Wood |
| MF_finish | Surface appearance or treatment | Natural Oil |
| MF_construction | Manufacturing or textile construction | Hand-woven, Mouth-blown, Tufted |
| MF_food_contact | Food-contact suitability | Yes / No / Conditional |
| MF_outdoor_suitability | Declared outdoor use | Indoor only, Covered outdoor, Outdoor |

**CDS1500-R037** A material-family facet MUST NOT erase the specific canonical material used for product display and channel mapping.

**CDS1500-R038** Component materials SHOULD identify the component wherever customer understanding, care, compliance or value depends on it.

Seed material table *(informative — the apparel and homewares material dictionaries are **separate dictionaries** with distinct `dictionary_key`s (`material_apparel`, `material_homewares`); the same code may therefore carry a different family classification in each without conflict — resolves DICT-5 via DICT-6 scoping)*:

| Canonical material | Family | Material facet |
|---|---|---|
| cotton | textile | cotton |
| linen | textile | linen |
| wool | textile | wool |
| polyester | textile_synthetic | synthetic_textile |
| ceramic | ceramic | ceramic |
| stoneware | ceramic | ceramic |
| porcelain | ceramic | porcelain |
| glass | glass | glass |
| crystal | glass | glass |
| stainless_steel | metal | metal |
| aluminium | metal | metal |
| brass | metal | metal |
| iron | metal | metal |
| oak | wood | wood |
| pine | wood | wood |
| teak | wood | wood |
| rattan | natural_fibre | natural_fibre |
| bamboo | natural_fibre | natural_fibre |
| marble | stone | stone |
| travertine | stone | stone |
| concrete | mineral | concrete |
| resin | synthetic | resin |
| soy_wax | wax | wax |
| paraffin_wax | wax | wax |

## 16. Homewares Dimensions, Capacity and Units *(normative)*

| Measure | Canonical storage | Display guidance |
|---|---|---|
| Length / width / height / depth / diameter | Millimetres or another declared canonical SI unit | Localise to cm, mm or inches as appropriate |
| Weight | Grams or kilograms with typed unit | Distinguish net product weight from shipping weight |
| Capacity | Millilitres or litres | Never text such as "approximately two cups" |
| Area | Square metres or declared unit | Rugs, wallpaper, flooring-like goods |
| Volume | Cubic measure or capacity depending on use | Distinguish container capacity from external volume |
| Pack count | Integer | Separate pieces from place settings |
| Burn time | Duration range with declared method | Avoid unsupported precision |
| Cable length | Length measure | Electrical accessories and lighting |

**CDS1500-R039** Canonical unit storage MUST be deterministic and conversion-safe.

**CDS1500-R040** Display conversions MUST NOT overwrite canonical values.

**CDS1500-R041** A range used in filtering or comparison MUST store lower and upper bounds rather than a single text string.

## 17. Homewares Room, Style, Finish and Shape *(normative; seed tables informative)*

Room, style, finish and shape describe different concepts and require separate dictionaries.

| Dictionary | Question answered | Examples |
|---|---|---|
| Room | Where is it commonly used? | Living Room, Bedroom, Bathroom |
| Style | What aesthetic does it support? | Coastal, Minimal, Industrial |
| Finish | What surface appearance/treatment does it have? | Matte, Brushed, Glazed |
| Shape | What is its overall geometry? | Round, Square, Organic |
| Use environment | Where can it safely function? | Indoor, Covered Outdoor, Outdoor |

**CDS1500-R042** Room MAY be multi-value, but every-room assignment SHOULD be prevented by a declared maximum room count per product.

**CDS1500-R043** Style SHOULD be curated from a limited organisational vocabulary and MUST NOT be inferred solely from colour.

Seed room dictionary *(informative)*: living_room, bedroom, dining_room, kitchen, bathroom, home_office, entryway, nursery, kids_room, laundry, outdoor, multi_room.

Seed finish dictionary *(informative)*: matte, gloss, satin, polished, brushed, hammered, distressed, weathered, painted, powder_coated, natural_oil, lacquered, glazed, unglazed, antique (alias: aged), textured, marbled *(re-homed from patterns per DICT-17)*.

Seed shape dictionary *(informative)*: round, square, rectangular, oval, cylindrical, tapered, organic (alias: irregular), arched, cone, spherical.

*Cross-dictionary id reuse (DICT-6): codes such as `tapered` (fit and shape), `casual`/`formal` (style and occasion) and `outdoor` (room, occasion and use environment) are distinct values in distinct dictionaries. Every dictionary declares a `dictionary_key`; mappings and alias records are always scoped by it (Appendix E).*

## 18. Shared Colour and Visual Appearance Profile *(normative)*

Apparel and homewares share the same top-level colour facet dictionary so customers encounter consistent filter language across the store. Industry profiles MAY use different canonical shade vocabularies beneath those shared facets. *(Preserved — ADR-1500-001.)*

**CDS1500-R044** A store SHOULD expose one consistent colour-family filter vocabulary across apparel and homewares unless a documented usability finding supports divergence.

**CDS1500-R045** Transparent, metallic, natural and multi-colour appearances MUST be handled explicitly (as facet values or declared extensions, Appendix C) rather than forced into arbitrary hue families.

**CDS1500-R046** Wood species, stone type and metal finish MUST remain material or finish values; a canonical material MAY additionally map to a visual colour family where the product appearance warrants it (declared in the dictionary, per-product only via the R021 override).

## 19. Customer Facet Design and Cardinality *(informative — normative facet rules live in CDS-600)*

Facet dictionaries are UX artefacts. Their success is measured by findability, comprehensibility and result quality rather than by maximum data exposure.

| Facet | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Colour | Broad colour families with swatches and text labels | Every supplier shade as a separate checkbox |
| Material | Customer-recognisable materials or families for the collection | Fibre, fabric, finish and claims mixed in one list |
| Size | Collection-relevant size systems and sort order | Alphabetical sort of mixed AU/US/EU/alpha sizes |
| Fit | Controlled product-family fit terms | Ad-hoc phrases from marketing copy |
| Room | Short curated room list | Every decor product in every room |
| Style | Governed organisational vocabulary | Hundreds of near-synonymous style tags |
| Dimensions | Ranges or typed values | Dozens of text-formatted dimensions |
| Price | Channel-native numeric ranges | Price bands as permanent product attributes |

Progressive disclosure for unscannable lists, facet monitoring (cardinality, zero-result rates, selection behaviour under CDS-1400) and **zero-result value handling follow CDS-600's normative rules** (CDS-600 §17–18: zero-result values SHOULD normally be disabled or hidden). The v0.1 MUST NOT here is withdrawn in favour of that single home *(resolves CDS-600-3)*.

## 20. Product Page Attribute Presentation *(informative)*

Product pages present customer-relevant attributes in logical groups rather than internal field order:

| Apparel group | Examples |
|---|---|
| Design and fit | Fit, length, neckline, sleeve, rise, leg shape |
| Material and construction | Composition, fabric, lining, stretch |
| Care and origin | Care instructions, country of origin, certifications |
| Size help | Size chart, garment measurements, model reference |

| Homewares group | Examples |
|---|---|
| Dimensions and capacity | Height, width, depth, diameter, capacity, weight |
| Materials and finish | Primary material, components, finish, construction |
| Use and care | Room, indoor/outdoor, cleaning, dishwasher or microwave suitability |
| Contents and compatibility | Pack count, included items, electrical compatibility |

Internal workflow, supplier and verification fields are never customer-facing unless intentionally transformed into customer content (rule: CDS-600 §5, CDS-300 QA_ semantics).

## 21. Channel Projection Guidance *(informative — normative rules: CDS-500 publication/verification, CDS-900 platform mappings)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Product category | Mapped standard category plus internal category | CH_google_product_category plus product_type |
| Canonical colour shade | Category/custom metafield and display data | `color` using an accepted customer-readable value |
| Colour facet | Search/discovery filter metafield | May inform `color` but never replaces the richer canonical shade |
| Composition | Structured metafield or content block | `material`, where supported |
| Size system and value | Variant option plus supporting metafields | `size` and `size_system` where required |
| Room/style/finish | Custom metafields and storefront filters | Channel descriptive fields, or omitted when unsupported |
| Dimensions | Typed metafields and display content | Channel fields where supported; otherwise descriptive content |

Channel projections use the expected representation defined by the mapping layer and are verified under CDS-500; unsupported channel attributes remain canonical in the PIM rather than being deleted or coerced into unrelated fields (CDS-500). Which layer (canonical, display or facet) feeds each channel is declared per attribute in the Attribute Definition (ADR-D4).

## 22. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

Profile-specific application of CDS-700's proposal/evidence/review model:

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Colour mapping | Canonical shade and facet family from image and source text | Dictionary validation; review of ambiguous or multi-colour cases; split-shade intake (R020) resolved by governed alias, not model preference |
| Material extraction | Composition and component candidates | Percent totals, canonical dictionary and evidence checks |
| Category classification | Family and category candidates | Taxonomy rules and human review at low confidence |
| Style and occasion | Limited curated suggestions | Declared maxima and merchandising-owner approval |
| Dimensions | Parsed typed measures from supplier documents | Unit validation and plausibility checks |
| Claims | Potential claim language | No acceptance without evidence and policy review |

AI selects from governed dictionaries or returns an unmapped proposal for review; it never manufactures composition percentages, measurements, certifications or care instructions; accepted values retain provenance to evidence and review decision — all per CDS-700 (no restatement here).

## 23. Governance and Organisational Extensions *(normative)*

**CDS1500-R047** An organisation MAY add categories, attributes, values and aliases but MUST assign stable identifiers and owners (CDS-800).

**CDS1500-R048** A new colour shade SHOULD map to an existing colour facet; a new top-level family requires the evidence in R049.

**CDS1500-R049** A proposed new facet value MUST include evidence that it is distinct, understandable and sufficiently populated against declared thresholds in the organisation's facet governance record.

**CDS1500-R050** Deprecated values MUST retain aliases and replacement mappings for migration and historical interpretation.

**CDS1500-R051** Industry-profile changes SHOULD be impact-assessed against storefront UX, supplier imports, channel mappings, saved filters, analytics and verification rules before adoption.

## 24. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS1500-R052** An implementation claiming the CDS Apparel Profile MUST: maintain product and variant scope correctly for size and sellable colour (R007, R012–R013); separate display shade, canonical shade and colour facet (R014); represent fibre composition separately from fabric type and claims (R023–R025); identify size system and deterministic size ordering (R026–R027); apply category-specific attribute requirements (R009); use governed dictionaries conforming to CDS-400 for material, fit, pattern and other filterable attributes (R011); and publish and verify channel representations under CDS-500.

**CDS1500-R053** An implementation claiming the CDS Homewares Profile MUST: store measurable specifications as typed values with units (R034, R039–R041); separate material, component material and finish (R035, R037–R038); apply category-specific requirements for dimensions, capacity, set contents and compatibility (R009); use governed room, style, shape and finish dictionaries where those facets are exposed (R011); project broad customer facets without losing canonical specificity (R037, R046); and publish and verify channel representations under CDS-500.

## 25. Worked Product Examples *(informative)*

### 25.1 Apparel — Relaxed Linen Shirt

```
CAT_family = apparel
CAT_product_type = shirt
CAT_internal_category = women > tops > shirts
MF_material_primary = linen
MF_fibre_composition = [{linen: 55}, {cotton: 45}]
MF_fabric_type = woven
MF_fit = relaxed
MF_pattern = plain

Variant (STD_sku = SHIRT-FN-10):
  VAR_colour = colour_french_navy        # canonical value_id at variant scope (ADR-D4)
  VAR_size_system = AU_WOMENS_NUMERIC
  VAR_size_label = 10

Product-scope colour projections (derived from variant canonical values, R013):
  MF_colour_display = French Navy        # display label projection
  MF_colour_facet = blue                 # facet projection via governed facet dictionary

CH_google_color = Blue                   # channel projection (feeding layer per Attribute Definition)
QA_shopify_colour = MATCH                # verification status per CDS-500 §17
```

### 25.2 Homewares — Stoneware Table Lamp

```
CAT_family = homewares
CAT_product_type = table_lamp
CAT_internal_category = home > lighting > table_lamps
MF_material_primary = stoneware
MF_finish = glazed
MF_colour_canonical = colour_oatmeal     # product-scope canonical (colour not variant-defining)
MF_colour_display = Oatmeal
MF_colour_facet = beige
MF_room = [living_room, bedroom]
MF_height_mm = 520
MF_width_mm = 280
MF_bulb_base = E27
MF_max_wattage_w = 40
VAR_plug_type = AU                       # VAR_plug_profile retired (CDS-1500-8)
CH_shopify_filter_material = Ceramic
QA_shopify_height = MATCH
```

### 25.3 Homewares — Printed Cushion

```
CAT_product_type = decorative_cushion
MF_cover_composition = [{cotton: 100}]
MF_fill_material = recycled_polyester
MF_pattern = floral
MF_colour_display = Garden Multi
MF_colour_components = [colour_sage_green, colour_blush_pink, colour_ecru]
                                         # canonical layer records component shades (ADR-D4)
MF_colour_dominant = colour_sage_green   # optional dominant-shade declaration
MF_colour_facet = multicolour            # multicolour is a facet/status value, never canonical
MF_shape = square
MF_width_mm = 500
MF_height_mm = 500
MF_removable_cover = true
VAR_insert_option = cover_only | feather_insert
```

*(v0.1 stored `MF_colour_canonical = multicolour`, destroying shade detail — corrected per CDS-1500-4 and ADR-D4.)*

## 26. Architecture Decision Records *(informative summary — decisions live in the global ADR register per CDS000-R006)*

| ADR | Decision | Status |
|---|---|---|
| CDS-ADR-1500-001 | Shared top-level colour facets across apparel and homewares | Accepted |
| CDS-ADR-1500-002 | Canonical shade separate from facet colour | Accepted (now an application of ADR-D4) |
| CDS-ADR-1500-003 | Fibre composition separate from fabric type | Accepted |
| CDS-ADR-1500-004 | Measurements stored in canonical typed units | Accepted |
| CDS-ADR-1500-005 | Style and occasion as governed multi-value attributes with declared maxima | Accepted |
| CDS-ADR-1500-006 | Starter dictionaries published as extensible informative baselines; requirements bind to governed dictionaries (R011) | Accepted (amended v0.2) |
| CDS-ADR-1500-007 | No universal exact size conversion claim | Accepted |
| CDS-ADR-1500-008 | Facet-ambiguous shade names split into distinct canonical shades (charcoal, rust, tan), intake via scoped alias mappings; product-level facet override only as governed record with provenance | Accepted (v0.2; applies ADR-D4/D12; see resolved D12 note at §7) |

---

## Appendix A. Apparel Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| VAR_colour | Variant | Canonical value_id (colour dictionary) | C — R when colour distinguishes sellable units |
| MF_colour_canonical | Product | Canonical value_id (colour dictionary) | C — R when colour is not variant-defining |
| MF_colour_display | Product/Variant | Free text linked to a canonical value (CDS-400 §9) | REC |
| MF_colour_facet | Product/Variant | Facet value, derived via the governed facet dictionary | R (derived, not independently authored) |
| VAR_size_label | Variant | Text | C |
| VAR_size_system | Variant/Product | Governed dictionary reference | C |
| MF_fibre_composition | Product | Structured percentage list of canonical material ids | R for garments |
| MF_material_primary | Product | Governed dictionary reference | R |
| MF_fabric_type | Product | Governed dictionary reference | REC |
| MF_fit | Product | Governed dictionary reference | REC |
| MF_pattern | Product | Governed dictionary reference | REC |
| MF_care_instructions | Product | Structured/text | REC |
| MF_country_of_origin | Product | Governed country reference | C |
| MF_size_chart_id | Product | Reference | REC |

*The v0.1 type "Text from dictionary" for MF_colour_display is corrected: display labels are free text linked to a canonical value, per CDS-400 §9 (resolves CDS-1500-7).*

## Appendix B. Homewares Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_material_primary | Product | Governed dictionary reference | R |
| MF_material_components | Product | Structured component list | C |
| MF_finish | Product | Governed dictionary reference | REC |
| MF_colour_canonical | Product/Variant | Canonical value_id (colour dictionary) | R |
| MF_colour_display | Product/Variant | Free text linked to a canonical value (CDS-400 §9) | REC |
| MF_colour_facet | Product/Variant | Facet value, derived via the governed facet dictionary | R (derived) |
| MF_height_mm / MF_width_mm / MF_depth_mm | Product/Variant | Number (typed unit) | C |
| MF_capacity_ml | Product/Variant | Number (typed unit) | C |
| MF_pack_count | Product/Variant | Integer | C |
| MF_room | Product | Governed dictionary list | REC |
| MF_shape | Product | Governed dictionary reference | REC |
| MF_care_instructions | Product | Structured/text | REC |

## Appendix C. Colour Facet Baseline *(informative seed — owned by CDS-1500; CDS-400 and CDS-600 cite this table (D11); becomes governed data on adoption per CDS1500-R011)*

### C.1 Baseline families (18)

| ID | Label | Definition | Typical canonical shades (deterministic — no per-product judgement) |
|---|---|---|---|
| black | Black | Near-black and black visual colours | black, jet_black, charcoal_black |
| white | White | White visual colours | pure_white, optic_white |
| grey | Grey | Neutral grey family | charcoal_grey, slate_grey, dove_grey |
| silver | Silver | Silver metallic appearance | silver, chrome |
| brown | Brown | Brown family | chocolate, espresso, tan_brown, rust_brown |
| beige | Beige | Warm pale brown and neutral family | sand, camel, oatmeal, tan_beige |
| cream | Cream | Warm off-white family | ivory, ecru, vanilla |
| yellow | Yellow | Yellow family | lemon, mustard, ochre |
| orange | Orange | Orange family | rust_orange, terracotta, apricot |
| red | Red | Red family | scarlet, burgundy, wine |
| pink | Pink | Pink family | blush_pink, rose, fuchsia |
| purple | Purple | Purple family | lilac, plum, lavender |
| blue | Blue | Blue family | navy, french_navy, cobalt, sky_blue, denim_blue |
| green | Green | Green family | sage_green, olive_green, emerald, teal (primary facet) |
| gold | Gold | Gold metallic appearance | gold, brass_visual |
| clear | Clear | Transparent or substantially colourless | clear_glass, transparent_acrylic |
| multicolour | Multi-colour | No single dominant colour or intentionally mixed palette | *(facet/status value only — never a canonical shade; ADR-D4)* |
| natural | Natural | Uncoloured natural appearance where no clearer family applies | raw_rattan, undyed_fibre |

The v0.1 appearance-conditional notes ("charcoal may map to Grey unless visually near-black"; "tan may instead map Beige"; "rust may use Orange or Brown based on appearance") are **deleted**; those shades are split into distinct canonicals per CDS1500-R020. Multi-facet shades (teal green|blue, tan_beige-style splits, rose_gold gold|pink) declare an **ordered facet list, primary first** (D28 as resolved in CDS-400).

### C.2 Boundary guidance *(informative)*

- **Cream / Beige / Natural / White** — White is visually white; Cream is warm off-white (ivory, ecru); Beige is warm pale brown (sand, oatmeal); Natural is reserved for *uncoloured* material appearance (raw rattan, undyed fibre) and never used where a hue family clearly applies. Organisations running the 12-family core (C.3) fold Cream into White or Beige and Natural into Beige, per shade.
- **Silver / Grey** — Silver requires metallic appearance; a non-metallic pale neutral is Grey. A brushed-metal product may carry material facet Metal with visual family Silver (R046).
- **Gold / Brown** — Gold requires metallic appearance; warm non-metallic browns (caramel, bronze-toned textiles) are Brown or Beige. Brass-*material* products map to Gold only when the visible appearance is gold-metallic.

### C.3 Recommended core (~12 families) with category-conditional extensions *(informative)*

For most storefronts a 12-family core filter outperforms the full 18: **black, white, grey, beige, brown, red, orange, yellow, green, blue, purple, pink**, plus **multicolour** as a status value. The remaining families are **category-conditional extensions**, enabled where the assortment warrants them: **silver, gold** (jewellery, hardware, decor with metallic finishes), **clear** (glassware, acrylic), **cream, natural** (textiles and natural-fibre homewares where the distinction demonstrably aids filtering). Extensions follow the same governance as any facet value (R049).

## Appendix D. Material Facet Seed *(informative seed — new in v0.2, resolves DICT-4; becomes governed data on adoption per CDS1500-R011)*

`dictionary_key: material_facet` — the governed value set for MF_material_facet and apparel material facets (previously ungoverned free-text labels in the CSVs).

| Facet ID | Label | Scope |
|---|---|---|
| cotton | Cotton | shared |
| linen | Linen | shared |
| wool | Wool | shared |
| hemp | Hemp | apparel |
| cashmere | Cashmere | apparel |
| silk | Silk | apparel |
| viscose | Viscose | apparel |
| lyocell | Lyocell | apparel |
| modal | Modal | apparel |
| polyester | Polyester | apparel |
| nylon | Nylon | apparel |
| synthetic | Synthetic | apparel |
| leather | Leather | apparel |
| faux_leather | Faux Leather | apparel |
| synthetic_textile | Synthetic Textile | homewares |
| ceramic | Ceramic | homewares |
| porcelain | Porcelain | homewares |
| glass | Glass | homewares |
| metal | Metal | homewares |
| wood | Wood | homewares |
| natural_fibre | Natural Fibre | homewares |
| stone | Stone | homewares |
| concrete | Concrete | homewares |
| resin | Resin | homewares |
| wax | Wax | homewares |

Excluded by design: **Recycled** (claim-driven from MF_recycled_content_percent, R025), **Stretch** (property-driven from MF_stretch, R025), **Other Natural** (forbidden catch-all label; hemp promoted to its own facet).

## Appendix E. Reference Dictionary Package *(informative — column contract and audit dispositions)*

The companion CDS-1500 Starter Reference Dictionaries package ships CSVs for colour facets, colour reference values, apparel materials, homewares materials, material facets (new), patterns, fits, styles, occasions, rooms, finishes and shapes, with a manifest and SHA-256 checksums (the SHA256SUMS + manifest pattern is retained — it verified end-to-end in the shipped-CSV audit). The package is versioned per ADR-D5 with folder and manifest versions agreeing (DICT-16). *(Distribution note, 2026-08-05: the companion data now ships as part of the unified **CDS Reference Dictionary** package (version per its manifest) which merges these profile-bound dictionaries with the E.3 gap-fill vocabularies and the ahead-of-profile industry chapters; content and contract unchanged.)*

The package is **informative starter data** in v0.2. Requirement levels bind to governed dictionaries per CDS1500-R011; an organisation adopting these files governs all subsequent changes under CDS-400/CDS-800 before treating them as production master data. The manifest's no-silent-redefinition note is retained and strengthened: a canonical code, once published, is never silently redefined — changes go through deprecation with replacement mappings (R050).

### E.1 Required columns (per DICT-1, DICT-6, DICT-11, DICT-15 and ADR-D4 §5)

Every dictionary file carries, for every row:

| Column | Content |
|---|---|
| dictionary_key | The owning dictionary (e.g. `colour`, `material_apparel`, `material_homewares`, `material_facet`, `fit`, `pattern`, `style`, `occasion`, `room`, `finish`, `shape`). Scopes all ids, mappings and aliases; permits cross-dictionary id reuse (DICT-5/6) |
| row_type | `canonical` or `alias` — source and canonical rows are never conflated in one row shape (DICT-11) |
| value_id / code | Stable identifier (snake_case per CDS-400) |
| label | Single-name display label — never slash-pair composites (DICT-7): "Viscose / Rayon" becomes label **Viscose** with alias `rayon`; likewise Nylon (alias polyamide), Elastane (alias spandex), Plaid (alias tartan), Graphic (alias placement print), Organic (alias irregular), Antique (alias aged) |
| aliases | Alias column present in **all** dictionaries, not only colour (9 of 11 v0.1 files had none — DICT-7); alias scope (supplier/locale) optional per ADR-D4 |
| facet_ids | Where applicable: ordered list, primary first; order significance declared in the package documentation (DICT-9/D28) |
| status | Lifecycle per CDS-400 (proposed/active/deprecated/retired/rejected) |
| provenance | Origin of the row (seed, import, organisational addition) |
| version | Row-level version per CDS-400 change rules |
| locale | Label locale; the seed data declares **en-GB** (DICT-15) |

Package documentation states column semantics, list delimiters (`;` for aliases, `|` for ordered facet lists) and case-matching rules (DICT-10). Channel mappings are declared **out of scope** for the starter package in the manifest (DICT-8); organisations add per-value channel mappings under CDS-400 §11 when needed.

### E.2 Seed content dispositions from the shipped-CSV audit

- **sky_blue** is confirmed as the canonical code, with `light_blue` recorded as an alias; the CDS-400 draft's `sky → light_blue` example is corrected to cite this baseline (DICT-3 — resolved in the CSV's favour under the no-silent-redefinition rule).
- **teal** declares facet order `green|blue`, ordered primary-first (DICT-9; D28 as resolved in CDS-400 — cited, not restated).
- **charcoal, rust, tan** are split per CDS1500-R020; the old single rows become default aliases to the grey/orange/beige-side canonicals.
- **natural** remains a top-level colour facet here; CDS-400's Appendix B "natural → Beige" exemplar is corrected to cite this appendix (DICT-2, D11).
- **colour_reference_values.csv is retained as the four-layer demonstration** — source ≠ display ≠ canonical ≠ facet, including the hard multi-facet cases (teal, rose_gold, and the now-split tan/rust) — restructured with row_type so canonical rows (navy) and alias rows (french_navy → navy in the coarse configuration) are distinguishable (DICT-11). *(Preserve item.)*
- **patterns.csv**: `textured` and `marbled` moved to finishes (texture, not pattern); `plain` documented as also meaning "no pattern" (DICT-17).
- **material facets** now reference material_facets.csv (Appendix D) instead of free-text labels (DICT-4).

### E.3 Known-missing referenced dictionaries (DICT-12)

Referenced by this chapter but not shipped as seed files; organisations supply governed content or adopt future package releases: **fabric types** (MF_fabric_type), **size systems** (VAR_size_system), **care instructions** (MF_care_instructions symbols), **country of origin** (MF_country_of_origin), **component roles** (MF_material_components), **weather/season relevance**, **use environment**. Listing here is disclosure, not endorsement of free text: until governed, these fields cannot satisfy R-level requirements (R011).

## Appendix F. Source Acknowledgements *(informative)*

The profile applies the product classification, attribute, value, unit and distribution concepts described in Jorij Abraham, *Product Information Management: Theory and Practice* (Springer, 2014), together with the project-documented PIM-first pipeline, tag governance and store-sequencing practices. CDS extends those foundations with explicit facet dictionaries, channel read-back verification, AI governance and human-readable semantic namespaces. Verification statuses, traffic lights and reason codes are defined solely in CDS-500 (ADR-D3); this chapter states none of its own.


<div class="chapter"></div>

# Appendix A. Architecture Decision Register

| ADR | Status |
|---|---|
| ADR-D1 — Single Conformance Ladder; Governance as Capstone; AI as Overlay Profile | Accepted (owner, 2026-08-03) |
| ADR-D2 — MF_ Semantics and the STD_/MF_ Boundary by Enumeration | Accepted (owner, 2026-08-03) |
| ADR-D24 — DF_ → CH_ Transition (Consolidated ADR) | Accepted (consolidates and supersedes: CDS-200 ADR-003 "Provisional", CDS-300 ADR-009 "Accepted for new design", CDS-ADR-900-002/003, CDS-ADR-1300-005) |
| ADR-D3 — One Verification Status Enum, Reason Codes, and the Traffic-Light Mapping | Accepted (owner, 2026-08-03) |
| ADR-D4 — Value-Layer Terminology: Source → Alias Mapping → Canonical → Projections | Accepted (owner, 2026-08-03) |
| ADR-D5 — Corpus Version Policy and Schema Identifier Scheme | Accepted (owner, 2026-08-03) |

All v0.1 chapter-local ADRs are superseded by or consolidated into this register and their chapters' v0.2 sections.

# Appendix B. Requirements Index (summary)

1,034 requirements: 584 MUST · 231 MUST NOT · 161 SHOULD · 31 MAY · 11 SHOULD NOT · 16 constitutive/indicative. Full machine-readable index: `requirements-index.csv`.

# Appendix C. Bibliography and Evidence Base

- An anonymised legacy implementation study covering product-data flow, tag governance and implementation sequencing.
- Platform documentation (priority 3, verified 2026-08-03/04, full register REVIEW-006/006A): help.shopify.com (product category; variants; Search & Discovery filters; store permissions; activity logs); shopify.dev (productUpdate; ProductUpdateInput; storefront filtering; webhooks; metafields); support.google.com/merchants (7052112; 6324436; 6324487); facebook.com/business/help (365831587397584; 125074381480892).
- Literature (priority 4): Jorij Abraham, *Product Information Management — Theory and Practice*, Springer 2014 (cross-check REVIEW-002B).
- Licence practice research: REVIEW-006A (OpenAPI, JSON Schema, AsyncAPI, schema.org, W3C, CloudEvents; accessed 2026-08-04).
