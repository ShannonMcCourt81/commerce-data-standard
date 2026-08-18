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
