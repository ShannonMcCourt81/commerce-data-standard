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
