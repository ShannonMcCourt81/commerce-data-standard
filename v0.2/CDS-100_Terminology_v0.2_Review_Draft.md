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
