# Commerce Data Standard (CDS)
## CDS-1500 — Apparel and Homewares Industry Profiles and Reference Dictionaries

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-09-20 (revision of the 2026-08-04 draft: industry profile register, jurisdiction requirement register and extension profiles added in the industry-profile expansion) |
| Supersedes | CDS-1500 Working Draft v0.1 and the CDS-1500 Starter Reference Dictionaries v0.1 package structure (data content carried forward, restructured per Appendix E) |
| Normative status | §1, §2 (including §2.1 and §2.2), §4, §5, §7–§13, §14A, §14B, §15–§18, §23, §24 and Appendices A–B (including A.1, A.2, B.1, B.2) are normative. §3, §6, §14, §19–§22, §25, §26 and Appendices C–G are informative; Appendix G seeds the jurisdiction requirement register whose record structure and obligations are normative in §2.2. Every table is individually marked. |
| Primary audience | Merchandisers, data stewards, ecommerce operators, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1400, especially CDS-200, CDS-300, CDS-400, CDS-500, CDS-600, CDS-900 and CDS-1100. Cited by CDS-1600 through CDS-2000, which apply the profile model (§2), requirement levels (§4), industry profile register (§2.1) and jurisdiction requirement register (§2.2) homed here |
| Companion package | CDS Reference Dictionary (unified informative starter data; column contract in Appendix E): Chapters 1–9 and 15–16 for the profiles in this chapter; Chapter 19 (Jurisdictions & Regulatory Schemes) for §2.2 |
| Profile identifiers | Base profiles `cds.profile.apparel.v0_2` and `cds.profile.homewares.v0_2`; extension profiles `cds.profile.footwear.v0_2`, `cds.profile.jewellery.v0_2` (§12), `cds.profile.furniture.v0_2`, `cds.profile.garden.v0_2` (§14A–§14B). All profile identifiers in the corpus are registered in §2.1 |
| Findings addressed | CDS-1500-1..8; CDS-400-3 and DICT-2 (colour-baseline ownership, D11); CDS-600-3 (zero-result rule re-homed); DICT-1..17; Matrix 2 and Matrix 5 deduplication; ADR-D3, ADR-D4, ADR-D24; D12 (partial — see OPEN flag), D28 (as resolved in CDS-400) |

Terminology in this chapter follows CDS-100. In particular, the v0.1 term "reference value" is retired (CDS100-R003); this chapter uses **Source Value → Alias Mapping Record → Canonical Value → Projections** per ADR-D4.

---

## 1. Purpose and Scope *(normative)*

CDS-1500 defines two interoperable industry profiles for a commerce catalogue whose primary range is apparel and accessories and whose secondary range includes lifestyle homewares. It translates the vendor-neutral CDS architecture into concrete product-family schemas, dictionary bindings, facet baselines and publishing expectations. **CDS-1500 is the owning chapter for the colour facet baseline** (Appendix C); CDS-400 and CDS-600 cite it and MUST NOT restate divergent copies *(resolves CDS-400-3/DICT-2 in this chapter's favour, decision D11)*.

**CDS1500-R001** An implementation claiming the Apparel Profile MUST distinguish product identity, sellable variants, canonical attributes, display labels, customer facets and channel representations, per the value-layer model of CDS-400 and CDS-100 §3.

**CDS1500-R002** An implementation claiming the Homewares Profile MUST store dimensions, capacity and other measurable specifications as typed values with declared units rather than uncontrolled text.

**CDS1500-R003** An industry profile MUST NOT force every possible attribute onto every product. Requiredness MUST be defined per product family and category profile.

**CDS1500-R004** A retailer MAY extend the baseline dictionaries, but MUST preserve stable identifiers, aliases, mappings and deprecation history (change control per CDS-400 and CDS-800).

CDS-1500 is also the owning chapter (CDS000-R005) for two mechanisms shared by every industry profile in the corpus: the **Industry Profile Register** (§2.1), which lists every profile identifier, its home chapter and its parent profile, and the **Jurisdiction Requirement Register** (§2.2), which defines how an organisation records the per-country regulatory obligations that bear on product data. The industry profile chapters CDS-1600 (beauty, health and personal care), CDS-1700 (food, beverage and grocery), CDS-1800 (consumer electronics, appliances and technical goods), CDS-1900 (parts, automotive, industrial and fitment) and CDS-2000 (sports and outdoor, toys and games, pet supplies) apply both without restatement; each carries its own seed of the register in its Appendix D, and this chapter's seed for apparel, footwear, jewellery, furniture and garden goods is Appendix G. The selection of profiles follows the global commerce vertical research recorded in REVIEW-020.

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

### 2.1 Industry Profile Register *(normative)*

The register is the single list of industry profiles defined by the corpus. A **base profile** stands alone. An **extension profile** refines a base profile for a product family (footwear refines apparel) and is claimed only together with its parent. A conformance claim (CDS-1000) names profile identifiers from this register.

| Profile identifier | Profile | Home chapter | Kind | Requires | Dictionary chapters bound |
|---|---|---|---|---|---|
| `cds.profile.apparel.v0_2` | Apparel | CDS-1500 §5–§11 | Base | — | 1, 2, 3, 4, 5, 6 |
| `cds.profile.footwear.v0_2` | Footwear | CDS-1500 §12.1 | Extension | `cds.profile.apparel.v0_2` | 2, 5, 8 |
| `cds.profile.jewellery.v0_2` | Jewellery and accessories | CDS-1500 §12.2 | Extension | `cds.profile.apparel.v0_2` | 1, 9 |
| `cds.profile.homewares.v0_2` | Homewares | CDS-1500 §13–§17 | Base | — | 1, 2, 3, 4, 6 (styles), 7 |
| `cds.profile.furniture.v0_2` | Furniture | CDS-1500 §14A | Extension | `cds.profile.homewares.v0_2` | 2, 3, 5 (bedding sizes), 7, 15 |
| `cds.profile.garden.v0_2` | Garden and outdoor living | CDS-1500 §14B | Extension | `cds.profile.homewares.v0_2` | 2, 7, 16 |
| `cds.profile.beauty_health.v0_2` | Beauty, health and personal care | CDS-1600 | Base | — | 10, 17 (ingestibles), 18, 19 |
| `cds.profile.food_beverage.v0_2` | Food, beverage and grocery | CDS-1700 | Base | — | 17, 18, 19 |
| `cds.profile.electronics.v0_2` | Consumer electronics, appliances and technical goods | CDS-1800 | Base | — | 11, 18, 19 |
| `cds.profile.parts_fitment.v0_2` | Parts, automotive, industrial and fitment | CDS-1900 | Base | — | 18, 19 (11 where relevant) |
| `cds.profile.sports_outdoor.v0_2` | Sports and outdoor | CDS-2000 §5 | Base | — | 12, 5, 19 |
| `cds.profile.toys_games.v0_2` | Toys and games | CDS-2000 §6 | Base | — | 13, 19 |
| `cds.profile.pets.v0_2` | Pet supplies | CDS-2000 §7 | Base | — | 14, 17, 19 |

Cross-industry mechanisms homed in one chapter and cited by the others: the product relationship record, kits and bundles, and the dangerous-goods declaration (CDS-1900 §5, §11, §12); market registration and responsible-person records (CDS-1600 §12); ingredient, allergen, nutrition and net-quantity patterns (CDS-1700 §5–§9); typed technical specifications and per-market compliance records (CDS-1800 §6, §12); the jurisdiction requirement register (§2.2 below).

**CDS1500-R054** Every industry profile defined by the corpus MUST appear in the register above with a stable identifier following the CDS-1100 §20 grammar, a home chapter, a kind (base or extension) and, for an extension, the profile it requires; a conformance claim MUST name profile identifiers from this register.

**CDS1500-R055** A claim of an extension profile MUST include a claim of the profile it requires; the extension's requirements add to, and MUST NOT weaken, the parent's.

### 2.2 Jurisdiction Requirement Register *(normative; the seed tables in each chapter's Appendix D and this chapter's Appendix G are informative)*

Much of what a product record must contain is decided by law, market by market: what must appear on the label, what must be shown online before purchase, what must be registered before sale, what must be declared for transport and what may not be sold at all. The corpus does not embed those rules in the requirement levels of §4, because they change by jurisdiction and over time. Instead every organisation maintains a **jurisdiction requirement register**: a governed record of the obligations that bear on its product data for each market it publishes to, mapped to the CDS fields that carry the data. The industry profile chapters seed the register with the obligations known at the release date; the organisation verifies, extends and reviews it.

| Register entry property | Meaning | Requirement |
|---|---|---|
| entry_id | Stable identifier | Required |
| jurisdiction | Governed value from the `jurisdiction` dictionary (package Chapter 19; ISO 3166 country codes with sub-national codes where a state or province regulates separately, for example US-CA) | Required |
| regulatory_scheme | Governed value from the `regulatory_scheme` dictionary (package Chapter 19) or a governed organisation extension, naming the instrument | Required |
| regulator | The authority administering the scheme | Required |
| instrument | Citation of the instrument and provision (act, regulation, standard, article or section) | Required |
| product_scope | Product families, categories or attribute conditions the entry applies to (a governed expression over CAT_ and MF_ attributes) | Required |
| obligation_type | One or more of: `pre_market` (registration, notification, listing, approval or certification before sale), `labelling_element` (a data element that must appear on the product or packaging), `listing_element` (a data element or artefact that must appear in the online offer before purchase), `warning_statement` (a mandated warning), `rating_label` (an energy, water, efficiency or similar rating label or class), `restricted_content` (a restriction on what may be claimed, shown or sold, including age and channel restrictions), `transport` (a dangerous-goods or carriage obligation), `documentation` (a document that must exist or be available on request), `post_market` (a producer-responsibility, recall, take-back or repair obligation) | Required |
| data_elements | The data elements the obligation requires, each mapped to the CDS field (namespace and attribute, or record) that carries it, or to a declared organisation extension where no CDS field exists | Required |
| trigger | The condition under which the obligation applies (category, attribute value, quantity, sale channel, customer type) | Required |
| effective_from / effective_to | Dates the obligation applies, including transition periods | Required where dated |
| publication_consequence | What preflight does for the target market when the obligation is unmet: `block`, `warn` or `record` | Required |
| verification_status / verified_on / verified_against | Whether the entry was verified against the primary instrument or a regulator publication, when, and against what | Required |
| owner / review_due | Accountable owner (CDS-800) and next review date | Required |
| notes | Interpretation notes, exemptions relied on | Optional |

**CDS1500-R056** An implementation claiming any industry profile MUST maintain a jurisdiction requirement register conforming to the record structure above for every market it publishes products to, with each entry carrying jurisdiction, scheme, instrument, product scope, obligation types, data elements mapped to CDS fields, trigger, dates, publication consequence, verification status and owner.

**CDS1500-R057** Publication preflight for a target market (CDS-500 §8) MUST evaluate every register entry whose jurisdiction and product scope match the product and channel, and MUST apply the entry's publication consequence: a `block` entry with unmet data elements blocks publication to that market, a `warn` entry records a warning, and a `record` entry records the evaluation; the evaluation result MUST be retained as an observation (CDS-500) with the entry identifier and version.

**CDS1500-R058** Every register entry MUST carry a verification status and date; an entry that is unverified, past its review date or seeded but not yet adopted MUST be visible as such in the register and in preflight results, and an implementation MUST NOT present an unverified entry as a verified legal obligation.

**CDS1500-R059** Where an obligation requires a data element for which the corpus defines no field, the organisation MUST declare an extension attribute or record (CDS-300 §21 grammar; CDS-1100 §20) and map the entry to it; the obligation MUST NOT be recorded as satisfied by free text in a description.

**CDS1500-R060** The seed tables in the industry profile chapters are informative starter content, dated and marked with their verification status: an organisation MAY adopt them as the initial content of its register, at which point they become governed records under that organisation's control and change through CDS-800 governance; an organisation MUST NOT rely on a seed entry marked "retrieved", "unverified" or "not seeded" without verifying it against the primary instrument.

**CDS1500-R061** Register entries whose obligation type is `listing_element`, `warning_statement` or `rating_label` MUST have their required elements projected in the channel representation for the target market and verified under CDS-500 where read-back exists; where the channel exposes no read-back for the element, the verification status MUST be UNOBSERVABLE, not MATCH.

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

## 12. Footwear and Accessories Extension Profiles *(informative baseline; R033 and §12.1–§12.2 normative)*

| Category | Required | Recommended | Variant options |
|---|---|---|---|
| Footwear | size; size system; sellable colour; upper material | sole material; lining; closure; heel height; width; toe shape | size, colour, width |
| Bags | sellable colour; primary material | dimensions; strap; closure; compartments; capacity | colour, size where applicable |
| Belts | size; sellable colour; primary material | width; buckle material; closure | size, colour |
| Jewellery | primary material; colour/finish | dimensions; stone; plating; closure; care | finish, size where applicable |
| Hats | size or adjustable status; sellable colour; material | brim, crown, fit, care | size, colour |

**CDS1500-R033** Footwear size systems MUST be identified explicitly and MUST NOT be merged into a single unqualified number.

### 12.1 Footwear Extension Profile *(normative; `cds.profile.footwear.v0_2`, requires `cds.profile.apparel.v0_2`)*

The footwear profile binds the Chapter 8 vocabularies (styles, heel heights, closures, toe shapes, width fittings) and the footwear size systems of Chapter 5, and adds the attributes that distinguish footwear from garments: upper, lining, sole and insole materials as component materials; width fitting as a variant option where offered; and measured fit (internal length) as the basis for size guidance.

**CDS1500-R062** Footwear MUST model size and, where offered, width fitting as variant options with an explicit size system (R033) and MUST store the size system's sort order (R027); internal length in millimetres SHOULD be stored per size where the brand publishes it, and a size conversion MUST follow R026.

**CDS1500-R063** Upper, lining, sole and insole materials MUST be component materials (the R035 pattern: canonical material per component role) rather than a single material field; the primary material facet derives from the upper unless the category profile declares otherwise.

**CDS1500-R064** Footwear style, heel height, closure, toe shape and width fitting MUST bind to governed dictionaries conforming to CDS-400 where those facets are exposed (R011); heel height MUST be stored as a typed measurement in millimetres with the governed band derived, never authored.

### 12.2 Jewellery and Accessories Extension Profile *(normative; `cds.profile.jewellery.v0_2`, requires `cds.profile.apparel.v0_2`)*

The jewellery and accessories profile binds the Chapter 9 vocabularies (metals, stones, closures, piece styles) and covers jewellery, watches, bags, belts, hats, eyewear and small leather goods. Its distinctive facts are material composition with purity and plating, stone identity with treatment and origin claims, and sizes measured in ring, chain-length and circumference systems.

**CDS1500-R065** Metal, purity or fineness, plating and stone MUST be separate governed attributes: the metal (a `jewellery_metal` value) with its fineness as a typed value (karat or parts per thousand) and the plating or coating as a distinct value; a plated item MUST NOT be described by the plating metal alone.

**CDS1500-R066** Stone identity MUST be a governed `jewellery_stone` value; natural, laboratory-grown, treated and simulated status MUST be an explicit governed attribute per stone, and origin, carat weight and grading are claims or typed values with evidence (R031), never inferred.

**CDS1500-R067** Ring, chain, bracelet and hat sizes MUST identify their size system (`size_system` values such as `au_ring`, `us_ring`, `eu_ring`, `head_circumference_cm`) and store the measured basis (inside circumference or diameter, length, head circumference) as typed measurements where the brand publishes it.

**CDS1500-R068** Precious-metal marking, nickel-release and lead or cadmium content obligations that a market imposes (Appendix G) MUST be evaluated at preflight for that market through the jurisdiction requirement register (§2.2).

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

## 14A. Furniture Extension Profile *(normative; `cds.profile.furniture.v0_2`, requires `cds.profile.homewares.v0_2`)*

Furniture (seating, tables, storage, beds, mattresses, desks, outdoor furniture) is the highest-value and most logistics-intensive homewares family. The profile binds Chapter 15 (assembly types) and the bedding size systems of Chapter 5, reuses the Chapter 6 style vocabulary and Chapter 2–3 materials and fabrics for upholstery, and adds the attributes that furniture retail and regulation demand: assembled and packaged dimensions, weight and load ratings, assembly type and time, seat and bed dimensions, mattress firmness and construction, and stability, flammability and toppling obligations that differ by market.

| Field | Meaning | Type |
|---|---|---|
| MF_assembly_type | Governed value (`assembly_type`: fully assembled, partial, flat-pack, professional installation) | Product |
| MF_assembly_time_min / MF_assembly_person_count | Assembly guidance | Integers |
| MF_dimensions_assembled / MF_dimensions_packaged (per package) | Typed dimensions with unit (R039) | Product / Variant |
| MF_weight_kg / MF_packaged_weight_kg / MF_package_count | Weights and package count | Typed measurements; integer |
| MF_load_rating_kg / MF_seat_height_mm / MF_seat_depth_mm / MF_arm_height_mm | Ergonomic and load measurements | Typed measurements |
| MF_bed_size_system + VAR_bed_size | Bedding size (`size_system` values `au_bedding`, `us_bedding`, `uk_bedding`, `eu_bedding`) with the mattress dimensions the size denotes | Variant |
| MF_mattress_firmness / MF_mattress_construction / MF_mattress_depth_mm | Governed firmness (`mattress_firmness`), construction as governed organisation value, depth | Product / Variant |
| MF_upholstery_material / MF_upholstery_fabric / MF_frame_material / MF_fill_material | Component materials per R035 | Product |
| MF_material_components | Component list with roles | Product |
| MF_delivery_class | Governed logistics class (parcel, oversized, two-person, white-glove) derived under governed rules | Product / Variant |
| MF_warning_statements / CMP_compliance_declarations | Stability, toppling, flammability and general-safety obligations per market (§2.2; Appendix G) | Per market |
| Relationship records | Modular and sectional configurations, matching pieces, replacement parts (CDS-1900 §5) | Product |

**CDS1500-R069** Furniture MUST store assembled dimensions and, per package, packaged dimensions and weight as typed measurements (R039), with package count; a product shipped in several packages MUST NOT report a single packaged dimension.

**CDS1500-R070** Assembly type MUST be a governed `assembly_type` value; delivery class MUST derive from packaged measurements and category rules under governed logic, not be authored per product.

**CDS1500-R071** Bed and mattress sizes MUST identify their size system and MUST store the mattress dimensions the size denotes in that system; a size label such as "Queen" MUST NOT be published without its system where the organisation sells into more than one market.

**CDS1500-R072** Mattress firmness MUST bind to a governed `mattress_firmness` dictionary where the facet is exposed; a brand's numeric firmness scale MUST be mapped to the governed value through an alias mapping with its basis recorded, and the mapping MUST NOT be presented as a measured property.

**CDS1500-R073** Upholstery fabric, frame and fill MUST be component materials (R035) with fibre composition for textile covers (R023 pattern); flammability and chemical-content statements that a market requires (Appendix G) MUST be structured records evaluated at preflight, and MUST NOT be projected as claims or facets.

**CDS1500-R074** Toppling, stability and anchoring warnings that a market requires on the product, its packaging or in the online description (Appendix G) MUST be structured warning records evaluated per market at preflight and projected to the market's listing where the market requires it; presence MUST be verified under CDS-500 (R061).

**CDS1500-R075** Modular and sectional furniture MUST express configurations, matching pieces and replacement parts through relationship records per CDS-1900 §5; a configurator's output MUST be traceable to those records.

## 14B. Garden and Outdoor Living Extension Profile *(normative; `cds.profile.garden.v0_2`, requires `cds.profile.homewares.v0_2`)*

Garden and outdoor living covers outdoor furniture and shade, planters and garden decor, garden tools and equipment, live plants and seeds, growing media, fertilisers and pest control, and barbecue and outdoor cooking. The profile binds Chapter 16 (sun exposure) and reuses the homewares baseline; powered equipment applies CDS-1800, chemicals and gas products apply CDS-1900 §12, and live plants are an organisation extension.

**CDS1500-R076** Outdoor suitability MUST be an explicit governed attribute (indoor, covered outdoor, full outdoor) with the weather-resistance basis recorded; "outdoor" MUST NOT be inferred from category placement.

**CDS1500-R077** Plants, seeds and bulbs MUST be identified by governed botanical and common names as separate attributes, with sun exposure bound to the governed `sun_exposure` dictionary where the facet is exposed; growth, hardiness and climate suitability MUST carry the scheme they are stated in (a hardiness-zone or climate-zone system) and are region-specific; the package deliberately ships no plant taxonomy.

**CDS1500-R078** Fertilisers, pesticides, herbicides, pool chemicals, fuels and gas products MUST carry dangerous-goods declarations and safety data sheet references per CDS-1900 §12 and per-market registration or restricted-sale records where a market regulates them (Appendix G); they MUST NOT be published to a market whose registration is absent.

**CDS1500-R079** Live plants, seeds and growing media MUST carry per-market biosecurity and movement restrictions as governed restricted-sale attributes evaluated at preflight, including sub-national restrictions where they exist (for example interstate plant movement controls).

**CDS1500-R080** Barbecues, heaters and gas appliances MUST apply CDS-1800 §12 for gas and electrical compliance records and CDS-1800 §8 for energy and power facts.

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

**CDS1500-R081** An implementation claiming any industry profile (this chapter or CDS-1600 through CDS-2000) MUST additionally: name profile identifiers from the register (R054) and claim the parent of every extension profile claimed (R055); maintain a jurisdiction requirement register for every market it publishes to (R056); evaluate the register at preflight per market with the declared publication consequences and retain the results (R057); keep verification status visible and never present unverified entries as verified (R058); map unmapped obligations to declared extensions (R059); and project and verify listing elements, warnings and rating labels for each market (R061).

**CDS1500-R082** An implementation claiming the CDS Footwear Profile MUST satisfy the Apparel Profile (R052) and R033, R062–R064 (size system and width as variant options with sort order, component materials, governed footwear dictionaries).

**CDS1500-R083** An implementation claiming the CDS Jewellery and Accessories Profile MUST satisfy the Apparel Profile (R052) and R065–R068 (metal, fineness, plating and stone as separate governed attributes; stone status; size systems; market marking and content obligations evaluated through the register).

**CDS1500-R084** An implementation claiming the CDS Furniture Profile MUST satisfy the Homewares Profile (R053) and R069–R075 (assembled and per-package dimensions, governed assembly and delivery classes, bedding size systems, governed mattress firmness, component materials with flammability and chemical statements as records, toppling warnings projected and verified, configurations as relationship records).

**CDS1500-R085** An implementation claiming the CDS Garden and Outdoor Living Profile MUST satisfy the Homewares Profile (R053) and R076–R080 (explicit outdoor suitability, governed plant naming and sun exposure with region-specific schemes, dangerous-goods and registration records for chemicals and gas products, biosecurity restrictions at preflight, CDS-1800 compliance for gas and electrical appliances).

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
| CDS-ADR-1500-009 | One corpus-wide industry profile register (§2.1); extension profiles require their parent; new verticals get their own chapters (CDS-1600 through CDS-2000) selected by global market research (REVIEW-020) rather than being appended to this chapter | Accepted (2026-09-20 revision; open flag IP1, IP8) |
| CDS-ADR-1500-010 | Regulatory obligations are not encoded in requirement levels; each organisation maintains a jurisdiction requirement register (§2.2) evaluated at preflight per market, seeded per chapter with dated, verification-marked entries for AU, NZ, US, EU, GB and CA | Accepted (2026-09-20 revision; open flag IP9) |
| CDS-ADR-1500-011 | The product relationship record, kits and bundles, and the dangerous-goods declaration are homed in CDS-1900 and cited by every other profile; promotion of the relationship record into CDS-200 is deferred to v0.3 | Accepted (2026-09-20 revision; open flag IP3) |

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

### A.1 Footwear Extension Baseline *(normative; adds to Appendix A)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| VAR_size_label / VAR_size_system | Variant | Text; governed dictionary reference (`size_system`, footwear systems) | R |
| VAR_width_fitting | Variant | Governed dictionary reference (`footwear_width_fitting`) | C — R where width is offered |
| MF_internal_length_mm | Variant | Typed measurement | REC |
| MF_material_components (upper, lining, sole, insole) | Product | Structured component list with canonical material ids | R |
| MF_footwear_style | Product | Governed dictionary reference | REC |
| MF_heel_height_mm / MF_heel_height_band | Product | Typed measurement; derived governed band | C — R for heeled footwear |
| MF_footwear_closure / MF_toe_shape | Product | Governed dictionary references | REC |
| MF_care_instructions / MF_country_of_origin | Product | Per Appendix A | Per Appendix A |

### A.2 Jewellery and Accessories Extension Baseline *(normative; adds to Appendix A)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| MF_jewellery_metal | Product | Governed dictionary reference | R for jewellery and watches |
| MF_metal_fineness | Product | Typed value with scale (karat or parts per thousand) | C — R where fineness is claimed or a market requires marking |
| MF_plating | Product | Governed dictionary reference (`jewellery_metal`) or none | R (explicit none) |
| MF_jewellery_stone / MF_stone_status | Product | Governed dictionary reference; governed status (natural, laboratory-grown, treated, simulated) | C — R where a stone is present |
| MF_stone_carat_weight / MF_stone_grading | Product | Typed value; claim record with evidence | C |
| MF_jewellery_closure / MF_jewellery_style | Product | Governed dictionary references | REC |
| VAR_size_label / VAR_size_system / measured basis | Variant | Text; governed reference (`au_ring`, `us_ring`, `eu_ring`, `head_circumference_cm`, chain length); typed measurement | C — R for sized pieces |
| MF_dimensions / MF_weight_g | Product / Variant | Typed measurements | REC |
| MF_warning_statements / CMP_compliance_declarations | Product (per market) | Structured records (nickel release, lead and cadmium content, hallmarking) | C — per §2.2 |

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

### B.1 Furniture Extension Baseline *(normative; adds to Appendix B)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| MF_assembly_type | Product | Governed dictionary reference (`assembly_type`) | R |
| MF_dimensions_assembled | Product / Variant | Typed dimensions | R |
| MF_dimensions_packaged / MF_packaged_weight_kg / MF_package_count | Product / Variant | Typed dimensions and weight per package; integer | R where the organisation ships |
| MF_weight_kg / MF_load_rating_kg | Product / Variant | Typed measurements | R / C |
| MF_seat_height_mm / MF_seat_depth_mm / MF_arm_height_mm | Product | Typed measurements | C — R for seating |
| MF_bed_size_system / VAR_bed_size / mattress dimensions | Variant | Governed reference; text; typed measurements | R for beds and mattresses |
| MF_mattress_firmness / MF_mattress_depth_mm | Product / Variant | Governed dictionary reference (`mattress_firmness`); typed measurement | R for mattresses where the facet is exposed |
| MF_material_components (upholstery, frame, fill) | Product | Structured component list | R |
| MF_delivery_class | Product / Variant | Governed logistics class (derived) | R where the organisation ships |
| MF_warning_statements / CMP_compliance_declarations | Product (per market) | Structured records (toppling, flammability, chemical content) | C — per §2.2 |
| Relationship records (configurations, matching pieces, parts) | Product | Records per CDS-1900 §5 | C |

### B.2 Garden and Outdoor Living Extension Baseline *(normative; adds to Appendix B)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| MF_outdoor_suitability | Product | Governed value (indoor, covered outdoor, full outdoor) with basis | R |
| MF_botanical_name / MF_common_name | Product | Governed organisation dictionary values | R for plants, seeds and bulbs |
| MF_sun_exposure | Product | Governed dictionary reference (`sun_exposure`) | REC; R for plants where the facet is exposed |
| MF_hardiness_or_climate_zone | Product | Typed value with scheme | C |
| CMP_dangerous_goods / MED_technical_documents (SDS) | Product / Variant | Per CDS-1900 §12 | R (explicit value) |
| CMP_market_registrations / CMP_restricted_sale | Product (per market) | Governed records | R for regulated chemicals, seeds and live plants |
| Gas and electrical compliance records | Product (per market) | Per CDS-1800 §12 | R for appliances |
| Homewares baseline | — | Per Appendix B | R |

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

Referenced by this chapter but not shipped as seed files; organisations supply governed content or adopt future package releases: **country of origin** (MF_country_of_origin), **component roles** (MF_material_components), **weather/season relevance**, **use environment**, **plant naming** (§14B), **mattress construction** (§14A), **licensed properties and skill levels** (CDS-2000). Since package 0.4.0 the **fabric types**, **size systems** and **care instructions** dictionaries listed here in the 2026-08-04 draft are shipped (Chapters 3, 5 and 4); package 0.8.0 adds bedding, ring, bike-frame and head-circumference size systems, mattress firmness (Chapter 15) and the Chapter 17–19 vocabularies bound by CDS-1700 through CDS-2000. Listing here is disclosure, not endorsement of free text: until governed, these fields cannot satisfy R-level requirements (R011).

## Appendix F. Source Acknowledgements *(informative)*

The profile applies the product classification, attribute, value, unit and distribution concepts described in Jorij Abraham, *Product Information Management: Theory and Practice* (Springer, 2014), together with the project-documented PIM-first pipeline, tag governance and store-sequencing practices. CDS extends those foundations with explicit facet dictionaries, channel read-back verification, AI governance and human-readable semantic namespaces. Verification statuses, traffic lights and reason codes are defined solely in CDS-500 (ADR-D3); this chapter states none of its own.

## Appendix G. Jurisdiction Requirement Register — Seed for Apparel, Footwear, Jewellery, Furniture and Garden Goods *(informative seed of the normative register defined in §2.2)*

Conventions: obligation types are those of §2.2. "Verified" means the primary instrument or regulator page was read on 2026-09-20; "retrieved" means a regulator page was retrieved but the instrument text was not read; "unverified" means the entry is seeded from general knowledge for completeness and MUST be verified before adoption (R060); "not seeded" means the organisation supplies the entry. Jurisdiction codes are those of the `jurisdiction` dictionary (package Chapter 19); scheme codes are those of `regulatory_scheme`. Cosmetics-like goods (fragrance, jewellery cleaners) follow CDS-1600 Appendix D; electrical and battery-powered goods (heated apparel, smart watches, powered furniture) follow CDS-1800 Appendix D; chemicals and gas products follow CDS-1900 Appendix D.

### G.1 Australia (AU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-AU-1 | Consumer Goods (Care Labelling for Clothing and Textile Products) Information Standard 2023 (AS/NZS 1957 with ISO 3758 symbols permitted) — ACCC (`au_care_labelling_2023`) | Clothing, household textiles, furnishings, piece goods and yarns, plastic-coated fabrics, suede skins, leathers and furs | labelling_element (permanent care label with care instructions in English, ISO symbols optionally alongside) | Care instructions as structured values → MF_care_instructions (Chapter 4 values with declared symbol set), fibre composition where used to derive care → MF_fibre_composition | Standard commenced 2023 replacing the 2010 standard; transition ended | Verified 2026-09-20 (ACCC mandatory standard page) |
| G-AU-2 | Consumer Goods (Children's Nightwear and Limited Daywear and Paper Patterns for Children's Nightwear) Safety Standard 2017 (AS/NZS 1249) — ACCC (`au_childrens_nightwear_2017`) | Children's nightwear and limited daywear sizes 00–14 | pre_market (fire-hazard category testing); labelling_element (category 1–4 label: "Low fire danger" or "Warning: High fire danger. Keep away from fire") | Fire-hazard category and label text → MF_warning_statements (scheme `au_childrens_nightwear_2017`), CMP_compliance_declarations (test evidence) | Ongoing | Verified 2026-09-20 (ACCC mandatory standard page) |
| G-AU-3 | Consumer Goods (Toppling Furniture) Information Standard 2024 — ACCC (`au_toppling_furniture_2024`) | Clothing storage units, bookcases, hall tables, display cabinets, buffets, entertainment units and similar free-standing furniture ≥ 686 mm high (as defined) | warning_statement (safety warning on the product and packaging); listing_element (warning in the online product description); labelling_element (anchoring instructions and information at point of sale) | Warning text, anchor supply status, online description warning → MF_warning_statements (scheme `au_toppling_furniture_2024`, includes online warning text), MF_anchor_kit_included, listing projection and verification (R074) | Mandatory from 4 May 2025 | Verified 2026-09-20 (ACCC toppling furniture guidance) |
| G-AU-4 | Australian Consumer Law s 29 and s 33 (country of origin and safe-harbour rules), Competition and Consumer Act; no mandatory fibre-content labelling standard for clothing (AS/NZS 2622 voluntary) — ACCC | Country of origin claims on apparel and homewares | restricted_content (origin claims must meet the safe-harbour tests) | Claim records with evidence → MF_country_of_origin, claims per R031 | Ongoing | Retrieved (not spot-verified) |
| G-AU-5 | Trade Practices (Consumer Product Information Standards) — jewellery: no mandatory hallmarking; lead and cadmium limits for children's jewellery under the Consumer Goods (Lead and Other Elements in Children's Toys) and related standards; Consumer Goods (Products Containing Button/Coin Batteries) standards for jewellery and accessories with batteries | Jewellery and accessories | restricted_content; labelling_element | Content limits and battery warnings → CMP_compliance_declarations, MF_warning_statements (per CDS-1800 D-AU-5) | Ongoing | Unverified — organisation to confirm the applicable children's jewellery instrument |
| G-AU-6 | Agricultural and Veterinary Chemicals Code (APVMA registration of garden pesticides and fertiliser-pesticide products); state biosecurity acts (plant movement and prohibited species, for example interstate quarantine); Consumer Goods (Portable Ladders / Trampolines) standards — APVMA, state departments, ACCC | Garden chemicals, seeds and live plants, outdoor equipment | pre_market (APVMA registration and approved label); restricted_content (biosecurity); labelling_element | APVMA number and label → CMP_market_registrations (scheme `au_apvma_agvet_code`); movement restrictions → CMP_restricted_sale per state | Ongoing | Retrieved (APVMA); biosecurity entries unverified |

### G.2 New Zealand (NZ)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-NZ-1 | Consumer Information Standards (Fibre Content Labelling) Regulations 2000; (Care Labelling) Regulations 2000; (Country of Origin (Clothing and Footwear) Labelling) Regulations 1992 — Commerce Commission (`nz_consumer_information_standards_textiles`) | Clothing, footwear, textile goods | labelling_element (fibre content, care instructions, country of origin for clothing and footwear) | → MF_fibre_composition, MF_care_instructions, MF_country_of_origin | Ongoing | Unverified — seeded from general knowledge; confirm current consolidation |
| G-NZ-2 | Product Safety Standards (Children's Nightwear and Limited Daywear Having Reduced Fire Hazard) Regulations 2016 (AS/NZS 1249) — MBIE (`nz_childrens_nightwear_2016`) | Children's nightwear | pre_market; labelling_element (fire-hazard label) | → MF_warning_statements (scheme `nz_childrens_nightwear_2016`) | Ongoing | Unverified — organisation to confirm |

### G.3 United States (US, with California noted)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-US-1 | Textile Fiber Products Identification Act and 16 CFR Part 303; Wool Products Labeling Act and 16 CFR Part 300 — FTC (`us_ftc_textile_wool_labelling`) | Textile and wool apparel and household textiles | labelling_element (generic fibre names and percentages in order of predominance; country of origin; manufacturer or dealer identity by name or Registered Identification Number (RN)); restricted_content (fibre and origin claims in advertising, including online, must be consistent with the label) | → MF_fibre_composition (generic fibre names per 16 CFR 303.7), MF_country_of_origin, CMP_responsible_person (RN or name), claims per R031 | Ongoing | Verified 2026-09-20 (eCFR 16 CFR 303) |
| G-US-2 | Care Labeling Rule, 16 CFR Part 423 — FTC (`us_ftc_care_labeling_423`) | Textile wearing apparel and certain piece goods | labelling_element (permanent care label with washing or dry-cleaning instructions and warnings; ASTM symbols permitted) | → MF_care_instructions with declared symbol set | Ongoing | Verified 2026-09-20 (eCFR 16 CFR 423) |
| G-US-3 | Flammable Fabrics Act; 16 CFR 1610 (general wearing apparel), 16 CFR 1615 and 1616 (children's sleepwear sizes 0–6X and 7–14), 16 CFR 1632 and 1633 (mattresses) — CPSC (`us_cpsc_flammable_fabrics`) | Apparel, children's sleepwear, mattresses and mattress pads | pre_market (testing and certification); labelling_element (sleepwear: flame-resistant or snug-fitting labelling; mattresses: permanent label and manufacturer identification) | → CMP_compliance_declarations (scheme `us_cpsc_flammable_fabrics`, test evidence), MF_warning_statements (sleepwear "wear snug-fitting" hang tag where applicable) | Ongoing | Retrieved (not spot-verified) |
| G-US-4 | STURDY Act; 16 CFR Part 1261 Safety Standard for Clothing Storage Units — CPSC (`us_cpsc_sturdy_16_cfr_1261`) | Clothing storage units (dressers, chests, armoires) ≥ 27 inches high manufactured after 1 September 2023 | pre_market (stability testing; certificate); labelling_element (permanent warning label and product identification; tip-over restraint supplied) | → CMP_compliance_declarations (scheme `us_cpsc_sturdy_16_cfr_1261`), MF_warning_statements, MF_anchor_kit_included | Products manufactured after 1 September 2023 | Verified 2026-09-20 (CPSC STURDY business guidance) |
| G-US-5 | California Technical Bulletin 117-2013 (upholstered furniture flammability; label stating compliance and whether flame-retardant chemicals were added) and SB 1019 (Business and Professions Code 19094) — Bureau of Household Goods and Services (`us_ca_tb117_2013`) | Upholstered furniture sold in California (de facto national labelling) | labelling_element (TB 117-2013 compliance label with flame-retardant chemical statement) | → CMP_compliance_declarations (scheme `us_ca_tb117_2013`), MF_flame_retardant_added (boolean) | SB 1019 labels from 1 January 2015 | Retrieved (not spot-verified) |
| G-US-6 | Proposition 65 (California) — OEHHA (`us_ca_prop65_warning`) | Apparel, jewellery (lead, cadmium), furniture (flame retardants, formaldehyde), garden chemicals | warning_statement; listing_element | Per CDS-1800 D-US-3 | Effective 1 January 2025 | Verified 2026-09-20 (CDS-1800 [E7]) |
| G-US-7 | Consumer Product Safety Improvement Act (lead content and lead paint limits for children's products; children's jewellery); California Metal-Containing Jewelry Law (Health and Safety Code 25214.1–25214.4.2); 16 CFR 1500.19 for accessories with small parts — CPSC, DTSC | Children's jewellery and accessories; jewellery sold in California | restricted_content (content limits); pre_market (children's product certificate); documentation | → CMP_compliance_declarations, MF_metal_fineness and plating facts, CPC reference | Ongoing | Unverified — organisation to confirm current limits |
| G-US-8 | Federal Seed Act (7 CFR 201), state seed laws, state noxious-weed lists; FIFRA (pesticide registration and labelling); state fertiliser registration laws — USDA, EPA, state departments | Seeds, pesticides, fertilisers | pre_market (registration per state and EPA registration number); labelling_element; restricted_content (state prohibited species; restricted-use pesticides) | → CMP_market_registrations (EPA Reg. No., state registrations), CMP_restricted_sale per state | Ongoing | Unverified — organisation to confirm |

### G.4 European Union (EU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-EU-1 | Regulation (EU) No 1007/2011 on textile fibre names and related labelling and marking of the fibre composition of textile products (`eu_textile_labelling_1007_2011`) | Textile products (≥ 80% textile fibres by weight), including apparel, home textiles and upholstery covers | labelling_element (fibre composition using Annex I names in the official language of the member state; non-textile parts of animal origin stated); listing_element (Article 16: the fibre composition must be indicated in a clear, legible and uniform manner and, where products are offered for sale to the consumer, including by electronic means, the information must be visible before purchase) | → MF_fibre_composition (Annex I fibre names, percentages), MF_animal_material ("Contains non-textile parts of animal origin"), localisation per market, listing projection and verification (R061) | Ongoing | Verified 2026-09-20 (EUR-Lex consolidated text) |
| G-EU-2 | Regulation (EU) 2023/988 General Product Safety Regulation (`eu_gpsr_2023_988`) | Apparel, footwear, jewellery, furniture, garden goods (non-harmonised) | listing_element; labelling_element; pre_market (responsible economic operator in the EU) | Per CDS-1800 D-EU-6 → CMP_responsible_person, CMP_product_identifier, MF_warning_statements, listing projection | Applies from 13 December 2024 | Verified 2026-09-20 (CDS-1800 [E13]) |
| G-EU-3 | REACH Regulation (EC) No 1907/2006 Annex XVII entries 27 (nickel release from articles in prolonged skin contact), 23 (cadmium in jewellery), 63 (lead in jewellery), 43 (azo dyes in textiles), 72 (CMR substances in textiles and footwear) — ECHA (`eu_reach_annex_xvii_articles`) | Jewellery, accessories, textiles, footwear | restricted_content (substance limits); documentation (test evidence) | → CMP_compliance_declarations (scheme `eu_reach_annex_xvii_articles`, entries and evidence) | Ongoing; entry 72 applies since 1 November 2020 | Retrieved (not spot-verified) |
| G-EU-4 | Directive 94/11/EC on the labelling of materials used in the main components of footwear (`eu_footwear_labelling_94_11`) | Footwear | labelling_element (material of upper, lining and sock, outer sole, by pictogram or text, at least on one shoe of each pair) | → MF_material_components (upper, lining, sole) with the directive's material categories (leather, coated leather, textile, other) | Ongoing | Unverified — organisation to confirm current status |
| G-EU-5 | Regulation (EU) 2024/1781 ESPR (textiles and furniture are priority product groups; delegated acts pending; unsold-goods destruction disclosure and ban for apparel and footwear for large enterprises from 19 July 2026) (`eu_espr_2024_1781`) | Apparel, footwear, furniture (as delegated acts are adopted) | listing_element; documentation; post_market | Digital product passport identifiers and labels per delegated act → CMP_product_identifier, MED_technical_documents | Framework in force 18 July 2024; product-group acts not seeded | Verified 2026-09-20 (CDS-1800 [E15]) for the framework; textile act not seeded |
| G-EU-6 | Regulation (EU) 2016/2031 plant health (plant passports for movement of plants for planting within the EU, including distance sales to final users); Regulation (EU) 2019/1009 (fertilising products; CE marking) and Regulation (EC) 1107/2009 (plant protection products; national authorisation) | Live plants, seeds, fertilisers, pesticides | pre_market (authorisation, plant passport); labelling_element; restricted_content (distance sales of plants require a plant passport) | → CMP_market_registrations, CMP_restricted_sale, MED_technical_documents (plant passport reference) | Plant health regulation applies since 14 December 2019 | Unverified — organisation to confirm |

### G.5 United Kingdom (GB)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-UK-1 | Textile Products (Labelling and Fibre Composition) Regulations 2012 (retaining Regulation 1007/2011 as assimilated law) — Trading Standards (`uk_textile_labelling_2012`) | Textile products | labelling_element; listing_element (fibre composition visible before purchase including online) | As G-EU-1 with English-language fibre names → MF_fibre_composition, listing projection | Ongoing | Retrieved 2026-09-20 (legislation.gov.uk) |
| G-UK-2 | Furniture and Furnishings (Fire) (Safety) Regulations 1988 (as amended) — OPSS and Trading Standards (`uk_furniture_fire_safety_1988`) | Upholstered furniture, mattresses, cushions and other filled articles supplied in the UK | pre_market (fillings and covers meet the ignition tests); labelling_element (permanent label with the statutory wording and supplier identity; display label at point of sale — including online product pages by guidance) | → CMP_compliance_declarations (scheme `uk_furniture_fire_safety_1988`), MF_warning_statements (statutory label wording), CMP_responsible_person, listing projection | Ongoing (reform consultations continuing) | Retrieved 2026-09-20 (legislation.gov.uk) |
| G-UK-3 | Hallmarking Act 1973 — assay offices and Trading Standards (`uk_hallmarking_act_1973`) | Articles described as gold, silver, platinum or palladium above the exemption weights | labelling_element (UK hallmark before sale and description); restricted_content (description of unhallmarked articles) | → MF_jewellery_metal, MF_metal_fineness, CMP_compliance_declarations (hallmark evidence), dealer's notice display | Ongoing | Unverified — organisation to confirm |
| G-UK-4 | General Product Safety Regulations 2005; UK REACH Annex XVII (nickel, cadmium, lead, azo dyes) — OPSS, HSE | Apparel, footwear, jewellery, furniture, garden goods | restricted_content; labelling_element | As G-EU-2 and G-EU-3 with GB instruments | Ongoing | Unverified — organisation to confirm |
| G-UK-5 | Plant Health (Official Controls and Miscellaneous Provisions) Regulations; UK plant passports; Plant Protection Products Regulations (GB) — Defra, APHA, HSE | Live plants, seeds, garden chemicals | pre_market; restricted_content | → CMP_market_registrations, CMP_restricted_sale | Ongoing | Unverified — organisation to confirm |

### G.6 Canada (CA)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| G-CA-1 | Textile Labelling Act and Textile Labelling and Advertising Regulations — Competition Bureau (`ca_textile_labelling_act`) | Consumer textile articles (apparel, household textiles, upholstery covers) | labelling_element (fibre content by generic name for fibres ≥ 5%, in English and French; dealer identity by name and postal address or CA identification number; country of origin for imports under the Customs Tariff marking rules); restricted_content (advertising representations) | → MF_fibre_composition (generic names, ≥ 5% rule), CMP_responsible_person (CA number), MF_country_of_origin, bilingual localisation per CDS-300 §18 | Ongoing | Verified 2026-09-20 (Competition Bureau guide to the Textile Labelling Act) |
| G-CA-2 | Canada Consumer Product Safety Act — Textile Flammability Regulations; Children's Sleepwear Regulations; Children's Jewellery Regulations (lead and cadmium limits); Consumer Chemicals and Containers Regulations for garden chemicals — Health Canada (`ca_ccpsa_textiles_jewellery`) | Apparel and textiles, children's sleepwear, children's jewellery, consumer chemicals | pre_market (compliance testing); restricted_content (content limits); labelling_element (bilingual warnings) | → CMP_compliance_declarations, MF_warning_statements (EN and FR), CMP_restricted_sale | Ongoing | Unverified — organisation to confirm |
| G-CA-3 | Pest Control Products Act (PMRA registration); Fertilizers Act; Seeds Act; Plant Protection Act — Health Canada, CFIA | Garden pesticides, fertilisers, seeds, live plants | pre_market (registration); labelling_element; restricted_content (import and movement conditions) | → CMP_market_registrations, CMP_restricted_sale | Ongoing | Unverified — organisation to confirm |

### G.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Japan (JP), China (CN), Republic of Korea (KR), India (IN), Brazil (BR) and others | Not seeded | Textile labelling (for example the Japanese Household Goods Quality Labelling Act, China GB 5296.4, India's Legal Metrology packaged-commodity rules), hallmarking (India BIS) and furniture safety regimes differ; organisation supplies entries with local advice. |
