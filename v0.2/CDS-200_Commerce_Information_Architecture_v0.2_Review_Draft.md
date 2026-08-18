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
