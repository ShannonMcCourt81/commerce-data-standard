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
