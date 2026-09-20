# Commerce Data Standard (CDS)
## CDS-1600 — Beauty, Health and Personal Care Industry Profile

| Field | Value |
|---|---|
| Status | **v0.3 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.3 (single corpus release per ADR-D5); chapter added in the 2026-09-20 industry-profile expansion that produced v0.3 (changelog REVIEW-021) |
| Date | 2026-09-20 |
| Supersedes | Nothing — first edition. The Chapter 10 dictionary vocabularies (beauty skin types, hair types, scent families, formulations, makeup finishes) were shipped ahead of this profile and are bound here for the first time. |
| Normative status | §1, §3, §5–§14, §19 and Appendix A are normative. §2 (pointer), §4, §15–§18, §20, §21 and Appendices B–D are informative; Appendix D seeds the jurisdiction requirement register whose record structure and obligations are normative in CDS-1500 §2.2. Every table is individually marked. |
| Primary audience | Beauty and health merchandisers, regulatory and compliance owners, data stewards, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1500, especially CDS-200 (entity model), CDS-300 (namespaces, incl. CMP_), CDS-400 (dictionaries, units), CDS-500 (verification, preflight), CDS-600 (facets), CDS-700 (evidence classes, claims), CDS-900 (platform profiles), CDS-1500 (profile model, requirement levels, colour architecture, profile register, jurisdiction requirement register), CDS-1700 (allergen and nutrition rules for ingestible products), CDS-1900 (kits, bundles and dangerous-goods declarations) |
| Companion package | CDS Reference Dictionary: Chapter 10 (Beauty & Personal Care), Chapter 1 (Colours), Chapter 19 (Jurisdictions & Regulatory Schemes); column contract per CDS-1500 Appendix E |
| Profile identifier | `cds.profile.beauty_health.v0_3` (registered in CDS-1500 §2.1) |
| Research basis | REVIEW-020 (global commerce vertical market research, 2026-09-20): Beauty & Fitness is the third-largest vertical across all Shopify stores worldwide (11.0%) and the second-largest across Shopify Plus stores worldwide (12.5%); Beauty and Health & Wellness show the highest Plus adoption rates of any vertical globally; beauty and personal care is a top-seven worldwide ecommerce revenue segment. |

Terminology follows CDS-100. Attribute requirement levels (R, C, REC, O, N/A) are those of CDS-1500 §4 and are not restated here.

---

## 1. Purpose and Scope *(normative)*

CDS-1600 defines the industry profile for products applied to, or taken into, the body: cosmetics and skincare, haircare, body and personal care, fragrance, colour cosmetics, sun care, oral care, grooming, and ingestible health products such as vitamins, supplements and complementary medicines. The profile also covers personal-care devices only where their product data is dominated by beauty attributes; devices dominated by technical specifications (hair dryers, electric toothbrushes, massage devices) apply CDS-1800 alongside this profile.

The data shape this profile governs is distinctive: ordered ingredient lists with regulated naming; shade systems layered on the shared colour architecture; net quantities and pack sizes that define sellable units; suitability facts (skin type, hair type) that are frequently confused with benefit claims; ratings under declared regulatory schemes (SPF); and a dense layer of regulated identity, warnings and shelf-life information whose authority is the product's label artwork and product information file, not marketing copy. Every one of those regulated elements differs by jurisdiction, so this profile is the first to be seeded with a per-country requirement register (Appendix D).

**CDS1600-R001** An implementation claiming the Beauty and Health Profile MUST represent ingredient lists, active ingredients, net quantities, regulatory identifiers, ratings and warnings as structured, typed attributes conforming to CDS-200 §7 and CDS-400 §18, never solely as free text or as content embedded in a description.

**CDS1600-R002** An implementation claiming this profile MUST separate declared product facts (ingredients, quantities, suitability, ratings) from benefit, efficacy and ethical claims, and MUST govern every claim under the evidence model of CDS-700 §7 and the claim rules of §11.

**CDS1600-R003** Ingestible health products (supplements, vitamins, complementary and listed medicines) MUST additionally apply the allergen declaration and nutrition-value rules of CDS-1700 §6–§7 as cited in §14.

**CDS1600-R004** This profile MUST NOT weaken any rule of CDS-1500 that it reuses (colour architecture, requirement levels, dictionary binding, jurisdiction requirement register); where this chapter is silent, CDS-1500 and the core chapters govern.

## 2. Profile Model *(informative pointer)*

This profile applies the industry profile model of CDS-1500 §2 (Core → Industry Profile → Product Family → Category Profile), the attribute requirement levels of CDS-1500 §4 and the jurisdiction requirement register of CDS-1500 §2.2 without restatement. Its identifier and dictionary bindings are recorded in the industry profile register, CDS-1500 §2.1; its seeded jurisdiction entries are in Appendix D.

## 3. Product Model *(normative)*

A beauty product is a formulation or design offered in one or more sellable presentations. The Product is the formulation (the serum, the foundation line, the fragrance); Variants are the sellable presentations that differ by shade, net quantity, pack or dispenser.

```
Product: Radiance Serum                         (informative example)
  Product scope:
    CAT_product_type = face_serum
    MF_product_form = serum                     # beauty_formulation dictionary
    MF_ingredient_list = [aqua, glycerin, niacinamide, ...]   # ordered INCI list
    MF_skin_type_suitability = [normal, combination, oily]
    MF_period_after_opening_months = 12
  Variant scope:
    VAR_net_quantity = {value: 30, unit: millilitre}
    VAR_pack_count = 1
    STD_id / VAR_sku = SER-RAD-030
```

**CDS1600-R005** Shade, net quantity, pack count and dispenser or applicator type MUST be modelled at variant scope where they identify distinct sellable units (variant boundary rule: CDS-200 §5); formulation, ingredients, suitability and claims MUST remain at product scope unless the fact genuinely differs between variants.

**CDS1600-R006** Where an ingredient list genuinely differs between shades of one product line (for example pigment-dependent colourants), the implementation MUST store the ingredient list at variant scope for the affected variants and MUST NOT publish the product-scope list as if it applied to every shade. *(Informative: several jurisdictions permit a range-level colourant list introduced by "may contain" or "+/−"; where that convention is used the implementation records the convention explicitly, see §5.)*

**CDS1600-R007** Gift sets, discovery sets and value packs containing distinct formulations MUST be modelled as kits or bundles with component relationships per CDS-200 §7A.2, not as a single product whose ingredient list concatenates the components.

**CDS1600-R008** Testers, samples and professional-size presentations MUST carry the same formulation identity as the retail product and MUST be distinguished by a governed presentation attribute (`MF_presentation_type`), never by a different ingredient list.

## 4. Product Families and Category Profiles *(informative baseline; the inheritance rule of CDS1500-R016 applies)*

| Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|
| Skincare (cleansers, serums, moisturisers, masks) | product form; ingredient list; net quantity; skin type suitability | key active ingredients; period after opening; scent family; texture | size |
| Sun care (primary sunscreens) | SPF and rating scheme; broad-spectrum status; ingredient list; net quantity; regulatory identity per market | water-resistance duration; product form; skin type suitability | size |
| Makeup — face | product form; shade (sellable colour); finish; ingredient list; net quantity | coverage; undertone; shade family; skin type suitability | shade, size |
| Makeup — eyes, lips, nails | product form; shade; finish; ingredient list; net quantity | shade family; applicator type | shade |
| Haircare (shampoo, conditioner, treatment, styling) | product form; ingredient list; net quantity; hair type suitability | scent family; period after opening | size |
| Body and personal care (wash, lotion, deodorant, oral care) | product form; ingredient list; net quantity | scent family; skin type suitability; dangerous-goods status for aerosols | size, pack |
| Fragrance | scent family; fragrance concentration; net quantity; ingredient list | fragrance notes (top/heart/base); dangerous-goods status | size |
| Grooming (shaving, beard care) | product form; ingredient list; net quantity | skin type suitability; scent family | size, pack |
| Supplements and listed medicines (§14) | dosage form; active ingredients with quantity per dose; pack quantity; directions; warnings; regulatory identity per market | allergen declarations; nutrition or supplement facts; storage conditions | pack size, flavour |
| Beauty tools and devices | material; dimensions | power source (CDS-1800) | colour |

## 5. Ingredients *(normative; seed guidance informative)*

Ingredient information is regulated content whose authority is the product's label and product information file. The profile stores it as an ordered, structured list so that it can be validated, searched, projected and compared, and so that free-from statements can be checked mechanically.

| Field | Meaning | Type |
|---|---|---|
| MF_ingredient_list | Ordered list of ingredient names as declared on the label | Ordered list of ingredient entries (name, optional canonical ingredient reference, optional function, optional percentage) |
| MF_ingredient_naming_scheme | The naming convention the list follows | Governed value: `inci`, `english_common`, `aan` (Australian Approved Name), `chemical_name`, `mixed_as_labelled` |
| MF_ingredient_order_basis | The ordering rule the label applies | Governed value: `descending_by_mass_or_volume`, `descending_over_one_percent_then_any_order` |
| MF_range_colourant_convention | Whether colourants are listed per shade or for the whole range | Governed value: `per_shade`, `range_may_contain` |
| MF_active_ingredients | Active or key ingredients with quantities | Structured list (canonical ingredient, quantity as typed measurement or percentage, unit basis) |
| MF_fragrance_disclosure | How fragrance is declared | Governed value: `parfum_placeholder`, `components_listed`, `fragrance_free` |
| CMP_fragrance_allergen_declarations | Declared fragrance allergens under a named jurisdiction list | List of (allergen name, regulatory scheme) |
| MF_nanomaterial_ingredients | Ingredients present as nanomaterials, where a jurisdiction requires "nano" marking | List of ingredient references |

**CDS1600-R009** `MF_ingredient_list` MUST be stored as an ordered list whose order is declared significant in the Attribute Definition (CDS400-R040) and MUST preserve the label order; an implementation MUST NOT re-sort, de-duplicate or "clean" the list without a governed change carrying label evidence.

**CDS1600-R010** The ingredient naming scheme and ordering basis MUST be declared per product (or inherited from a category profile) so that a consumer of the data can interpret the list; a list without a declared scheme MUST NOT satisfy an R-level ingredient requirement.

**CDS1600-R011** Active ingredients MUST carry a numeric quantity with a declared unit or percentage basis (CDS400-R056) wherever the label declares one; a textual strength such as "high strength" MUST NOT be stored as the quantity.

**CDS1600-R012** Ingredient names MAY be linked to a governed ingredient dictionary for search and facet projection, but the label-declared spelling MUST be preserved as the source value with provenance (CDS400-R006, R014).

**CDS1600-R013** An ingredient list captured by extraction from label artwork or packaging images (evidence class E2 or E3 per CDS-700 §7) MUST be reviewed by a human before acceptance, regardless of confidence (CDS-700 §19).

*Informative — ordering conventions across the seeded jurisdictions.* Australia (Consumer Goods (Cosmetics) Information Standard 2020), New Zealand (Cosmetic Products Group Standard 2020), the United States (21 CFR 701.3), the EU (Regulation (EC) 1223/2009 Article 19) and Canada (Cosmetic Regulations) all require descending order by mass, volume or predominance, all permit ingredients under 1% in any order after those above 1%, and all permit colour additives to be listed last. Naming differs: Canada mandates INCI names; Australia and New Zealand accept INCI or English names; the EU uses the common ingredient glossary and requires "nano" in brackets for nanomaterials; the US uses the names established by regulation. The two declared fields above let a PIM record which convention a given label followed rather than guessing; Appendix D records the per-jurisdiction rule with its verification date.

## 6. Product Form, Finish and Scent *(normative; dictionary bindings informative until adopted)*

| Attribute | Dictionary (Chapter 10 unless stated) | Scope |
|---|---|---|
| MF_product_form | `beauty_formulation` (cream, serum, gel, mist, foam, powder, stick, bar, sheet mask, …) | Product |
| MF_makeup_finish | `beauty_makeup_finish` (matte, dewy, satin, shimmer, glossy, natural) | Product |
| MF_scent_family | `beauty_scent_family` (floral, citrus, woody, amber, …) | Product |
| MF_fragrance_concentration | `fragrance_concentration` (parfum, eau de parfum, eau de toilette, eau de cologne, eau fraîche, body mist) — new in package 0.8.0 | Product |
| MF_fragrance_notes | Structured top/heart/base note lists (organisation-governed vocabulary) | Product |

**CDS1600-R014** Product form MUST be a governed dictionary value distinct from the product's classification; "serum" as a form and "face serum" as a product type are related but separately governed facts (classification rules: CDS-200 §6).

**CDS1600-R015** Fragrance concentration MUST be a governed value and MUST NOT be inferred from price, size or marketing tier; where the manufacturer declares no concentration the attribute is unknown, not "eau de toilette".

**CDS1600-R016** Scent family and fragrance notes are merchandising descriptors and MUST NOT be presented as ingredient disclosure.

## 7. Suitability: Skin Type, Hair Type and Audience *(normative)*

Suitability values state which skin or hair conditions a product is presented for. They are manufacturer-declared facts about intended use, not efficacy claims, and the package deliberately excludes benefit and age-state terms (anti-ageing, hypoallergenic, mature) from these vocabularies.

**CDS1600-R017** `MF_skin_type_suitability` and `MF_hair_type_suitability` MUST be multi-value attributes bound to the governed `beauty_skin_type` and `beauty_hair_type` dictionaries, with a declared maximum value count per product (the CDS1500-R029 pattern), and MUST derive from manufacturer or brand declarations (evidence class E1 or E2), never from model inference over marketing copy.

**CDS1600-R018** A suitability value MUST NOT be projected to a customer facet as a benefit ("treats dry skin"); the facet label MUST express intended use ("for dry skin").

**CDS1600-R019** Audience attributes (target gender, age group) MUST be governed values where a channel requires them and MUST NOT be inferred from scent family, colour or packaging.

## 8. Shades and Colour *(normative)*

Colour cosmetics apply the CDS-1500 §7 colour architecture: the sellable shade is a canonical colour value at variant scope, the shade name is its Display Label, and the customer filter uses the governed colour-family facet. Two beauty-specific additions are required: a deterministic shade order within a range, and an optional undertone dimension.

```
Variant: Foundation, shade "Warm Sand 3.5"     (informative example)
  VAR_colour            = colour_warm_sand_3_5       # canonical shade value_id
  MF_colour_display     = Warm Sand 3.5              # Display Label
  MF_colour_facet       = beige                      # governed family facet
  VAR_shade_sort_key    = 035                        # deterministic order in the range
  MF_undertone          = warm                       # optional: warm / cool / neutral / olive
  MF_shade_range_id     = range_foundation_2026      # the range the shade belongs to
```

**CDS1600-R020** Shades MUST be canonical colour values with stable `value_id`s (CDS400-R009); a brand shade name is a Display Label linked to the canonical value (CDS400-R022) and MUST NOT be the only identity of the shade.

**CDS1600-R021** Shades within a range MUST carry a sort key or an equivalent declared ordering mechanism so that storefronts and channels present the range in the brand's intended order rather than alphabetically (the CDS1500-R027 pattern).

**CDS1600-R022** Undertone, where used, MUST be a governed single-value attribute separate from the colour family facet; it MUST NOT be encoded in the shade name alone.

**CDS1600-R023** Swatch imagery and digital colour values follow CDS400-R061: they MAY be stored but MUST NOT be represented as an exact match of the product on skin.

**CDS1600-R024** A shade discontinued from a range MUST follow dictionary deprecation (CDS400-R080) with a replacement pointer where a successor shade exists, so that historical orders, reviews and analytics remain interpretable.

## 9. Quantity, Pack and Dosage *(normative)*

**CDS1600-R025** Net quantity MUST be a typed measurement with a declared unit (millilitre, gram, or count for unit-dose products) per CDS400-R056, stored at variant scope, and MUST NOT be embedded only in the title or variant label.

**CDS1600-R026** Pack count (number of identical units in the sellable pack) MUST be an integer attribute separate from net quantity per unit; a "3 × 50 ml" presentation is `VAR_pack_count = 3` and `VAR_net_quantity = 50 ml`, never a net quantity of "150 ml" alone.

**CDS1600-R027** Unit-pricing base measures required by a channel or jurisdiction MUST be derived from the typed net quantity and pack count, never authored independently.

**CDS1600-R028** Supplements MUST record serving size, servings per container and the dosage form as typed values (§14).

## 10. Sun Protection and Declared Ratings *(normative)*

Sun protection factor (SPF) is a tested rating under a declared scheme, and in some jurisdictions a primary sunscreen is a regulated therapeutic good or an over-the-counter drug. The profile treats the rating value, the scheme and the regulatory status as three separate governed facts.

| Field | Meaning | Type |
|---|---|---|
| MF_spf_value | Declared SPF as labelled | Integer (with optional "+" flag for capped labels such as "50+") |
| MF_spf_rating_scheme | The standard the rating was determined under | Governed value: `as_nzs_2604`, `iso_24444`, `fda_sunscreen_monograph`, `other_declared` |
| MF_broad_spectrum | Broad-spectrum (UVA) protection status as labelled | Boolean with scheme reference |
| MF_water_resistance_minutes | Labelled water-resistance duration | Integer minutes, or null |
| CMP_regulatory_scheme / CMP_regulatory_id | Regulatory identity per market (§12) | Governed scheme code plus identifier |

**CDS1600-R029** SPF MUST be stored as a numeric value plus a declared rating scheme; a value without a scheme MUST NOT satisfy an R-level requirement, and the scheme MUST NOT be assumed from the target market.

**CDS1600-R030** A sun-protection claim in a title, description or facet MUST be derived from `MF_spf_value` and its evidence; an implementation MUST NOT accept an SPF value whose evidence class is below E2 (CDS-700 §7).

**CDS1600-R031** Where a jurisdiction in the organisation's register classifies a sunscreen as a therapeutic good or drug, the regulatory identifier and any mandated label elements for that market (§12, Appendix D) MUST be present before publication to that market; publication preflight (CDS-500 §8) MUST block a therapeutic sunscreen lacking them.

*Informative.* In Australia primary sunscreens are therapeutic goods regulated by the Therapeutic Goods Administration and carry an AUST L or AUST R number, active-ingredient names and proportions, batch and expiry information and storage conditions; secondary sunscreens may be cosmetics subject to conditions. In New Zealand the Cosmetic Products Group Standard allows a primary sunscreen to be labelled to the Australian Therapeutic Goods Order. In the United States a sunscreen is an over-the-counter drug whose active ingredients are declared in a Drug Facts panel before the cosmetic ingredients. In the EU and UK sunscreens are cosmetics. A retailer selling into several markets therefore records the scheme and identifier per market rather than one global value (Appendix D).

## 11. Claims, Certifications and Free-From Statements *(normative)*

Benefit claims ("reduces the appearance of wrinkles"), ethical claims ("cruelty-free", "vegan"), sustainability claims ("natural", "organic"), and free-from statements ("paraben-free") are the highest-risk content in this vertical. This section applies the corpus claim pattern established for apparel (CDS1500-R025, R031–R032) with beauty-specific mechanics.

| Attribute | Structure | Requirement guidance |
|---|---|---|
| MF_claims | List of claim records: claim type (governed), claim text as labelled, evidence reference and class, scope (product or component), jurisdictions in which the claim is published, approving owner, effective/expiry dates | C — required whenever a claim is published |
| MF_certifications | List of certification records: scheme, certifier, certificate identifier, scope, expiry | C — required when a certification is displayed |
| MF_free_from_statements | List of governed free-from statement records naming the excluded ingredient class | C |
| MF_natural_origin_percent / MF_organic_content_percent | Numeric, component-aware | C — required when a quantified natural or organic claim is made |

**CDS1600-R032** Every published claim MUST exist as a claim record with an evidence reference of class E1 or E2 (CDS-700 §7); a claim MUST NOT be created or accepted from supplier or brand marketing copy alone (CDS400-R066 pattern).

**CDS1600-R033** A free-from statement naming an ingredient or ingredient class MUST fail validation when the named ingredient (or a governed member of the named class) appears in `MF_ingredient_list` or in the variant-scope ingredient list of any variant the statement covers. The validation error MUST be classified as conflicting (CDS200-R035) and MUST block publication of the statement.

**CDS1600-R034** Certification-backed claims (cruelty-free, vegan, organic, halal and comparable schemes) MUST reference the certifying body and certificate scope; expiry of the certificate MUST withdraw the claim projection without altering any product fact (the CDS1500-R032 pattern).

**CDS1600-R035** Benefit and efficacy claims MUST NOT be projected as customer facets unless the organisation declares a claim-driven facet with a documented evidence threshold in its facet governance record (CDS1500-R049); such a facet MUST be fed only by accepted claim records.

**CDS1600-R036** Therapeutic and health claims for ingestible products (§14) MUST be restricted to indications permitted under the applicable regulatory scheme of each market in which they are published and MUST carry the scheme reference in the claim record; a claim record MUST declare the jurisdictions it is published in so that preflight can evaluate it per market.

**CDS1600-R037** AI MAY extract candidate claim language from packaging or copy, but a claim record MUST NOT be accepted at any autonomy level above suggest-only without human review (CDS-700 §5, §19); absence of evidence MUST NOT become a claim (CDS700-R018).

## 12. Regulatory Identity, Responsible Person, Shelf Life, Batch and Expiry *(normative)*

Regulatory identity is a per-market fact. The profile stores it as governed records keyed by jurisdiction and scheme, drawing scheme codes from the `regulatory_scheme` dictionary (package Chapter 19) and evaluating obligations through the jurisdiction requirement register (CDS-1500 §2.2; seed in Appendix D).

| Field | Meaning | Scope |
|---|---|---|
| CMP_market_registrations | List of records: jurisdiction, regulatory scheme (governed), identifier (e.g. AUST L number, product listing reference), status (registered / listed / notified / exempt / out_of_scope), effective dates, evidence | Product (one record per market) |
| CMP_responsible_person | The responsible person, sponsor or importer of record for the market, with the address that the market requires on the label or listing | Product (per market) |
| MF_period_after_opening_months | Period after opening as labelled | Product |
| MF_minimum_durability_policy | Whether the product carries a date of minimum durability or a period-after-opening symbol | Product |
| MF_shelf_life_days | Shelf life from manufacture, where declared | Product |
| CMP_country_of_origin | Country of origin (required on the label or listing by several markets) | Product |

**CDS1600-R038** Regulatory scheme and identifier MUST be stored per target market as governed records, never as a single global free-text "registration" field; an implementation MUST be able to answer, for a given market, whether the product is registered, listed, notified, exempt or out of scope, and publication preflight for that market MUST evaluate the answer against the register (CDS1500-R057).

**CDS1600-R039** Batch (lot) numbers and expiry dates are lot-level facts. An implementation MUST NOT store a single batch number or expiry date as a canonical product or variant attribute unless it declares a lot-per-variant model; lot-level dates are observed from the inventory or warehouse authority (CDS-200 §13) and MAY be published as channel fields with their authority declared.

**CDS1600-R040** Period after opening and minimum durability policy MUST be typed values; a storefront or channel MUST NOT display a computed expiry as a product fact where only a period after opening is known.

**CDS1600-R041** Withdrawal, recall or regulatory suspension of a product in a market MUST be expressed through lifecycle state and channel withdrawal (CDS-500 §12), never by deleting the product record.

**CDS1600-R042** The responsible person or sponsor of record MUST be a governed per-market attribute; where a market requires that person's name and address on the listing or packaging (Appendix D), the channel projection for that market MUST include it and verification MUST cover it.

## 13. Safety, Warnings and Handling *(normative)*

**CDS1600-R043** Warnings, directions for use and precautionary statements required by a jurisdiction MUST be stored as structured, governed statement records (statement type, text as labelled, jurisdiction, mandating scheme) rather than only within description prose, so that channel projection and verification can confirm their presence per market.

**CDS1600-R044** Products that are dangerous goods for transport (aerosols, alcohol-based fragrances and sanitisers, certain nail products) MUST carry a dangerous-goods declaration per CDS-1900 §12 before publication to a channel or carrier that requires it; the declaration MUST NOT be inferred from category alone.

**CDS1600-R045** Age or purchase restrictions applicable in a market MUST be governed attributes evaluated at publication preflight for that market.

## 14. Ingestible Health Products: Supplements and Listed Medicines *(normative)*

Vitamins, minerals, herbal and nutritional supplements and complementary medicines share the ingredient, claim and regulatory pattern of cosmetics but add dosage, allergen and nutrition-panel obligations. The profile homes them here and cites CDS-1700 for the allergen and nutrition mechanics.

| Field | Meaning | Type |
|---|---|---|
| MF_dosage_form | Tablet, capsule, softgel, powder, liquid, gummy, effervescent, … | Governed value (organisation-governed; a starter vocabulary is a candidate for package 0.9) |
| MF_active_ingredients | Active or medicinal ingredients with quantity per dose unit | Structured list (§5) |
| MF_serving_size / MF_servings_per_container | Dose definition | Typed |
| MF_directions | Directions for use as labelled | Structured statement records |
| CMP_allergen_declarations | Allergen declarations | Per CDS-1700 §6 |
| MF_nutrition_values | Nutrition or supplement-facts values | Per CDS-1700 §7 with scheme `supplement_facts` or `nutrition_information_panel` |
| CMP_market_registrations | Listing, licence or registration per market | §12 |

**CDS1600-R046** Active ingredients MUST be stored with quantity per dose unit as typed measurements; "one-a-day" or "high potency" MUST NOT stand in for quantities.

**CDS1600-R047** Allergen declarations and nutrition values for ingestible products MUST conform to CDS-1700 §6 and §7 respectively, including the distinction between "contains" and precautionary "may contain" declarations and the per-100 versus per-serving basis.

**CDS1600-R048** Indications and health claims MUST reference the permitted-indication or claim scheme of the target market in the claim record (§11), and publication preflight MUST block an indication not permitted under the declared scheme for that market.

**CDS1600-R049** Ingestible products MUST carry storage conditions (CDS-1700 §10 dictionary `storage_condition`) and mandatory warning statements (§13) before publication.

## 15. Customer Facet Design *(informative — normative facet rules live in CDS-600)*

| Facet | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Product form | Governed formulation vocabulary; category-aware (serum is meaningless in fragrance) | Free-text "type" from supplier feeds |
| Skin / hair type | Suitability vocabulary, multi-select OR | Benefit language as facet labels |
| Shade family | Colour-family facet from CDS-1500 Appendix C; swatch plus text label (CDS600-R036) | Every shade name as a checkbox |
| Finish | Makeup finish vocabulary in colour-cosmetics contexts only | Finish exposed on skincare |
| Scent family | Small governed list | Note-level lists of hundreds of ingredients |
| SPF | Numeric range facet (15+, 30+, 50+) derived from `MF_spf_value` | Marketing tiers |
| Size | Net-quantity ranges with unit context | Mixed ml and g in one list |
| Claims | Only claim-driven facets with declared evidence thresholds (R035) | "Clean", "natural", "hypoallergenic" as tags |

Fragmentation and coverage thresholds, zero-result handling and accessibility follow CDS-600 §10, §17 and §24.

## 16. Channel Projection Guidance *(informative — normative rules: CDS-500, CDS-900)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Product form, skin type, scent | Category or custom metafields; storefront filters | Descriptive fields where supported, otherwise `product_detail` |
| Shade | Variant option with linked colour entry (display label); family facet as filter metafield | `color` = landing-page shade name (CDS-900 §5.2 rule); family never published to `color` |
| Net quantity, pack count | Typed metafields; variant title composition per declared title policy (CDS-700 §12) | `unit_pricing_measure` / `unit_pricing_base_measure` where required; `multipack` for identical-unit packs |
| Ingredient list | Rich-text or list metafield generated from the structured list; never hand-edited downstream | Not a standard feed field; carried in description where policy allows |
| SPF, regulatory identifiers, responsible person | Custom metafields; verified by read-back; per-market listing text generated from the register | Description or `product_detail`; regulatory identifiers where the channel requires them |
| Claims and certifications | Only accepted claim records project; expiry withdraws the projection | Certification attributes where the channel defines them |
| Warnings mandated for a market | Generated statement block per market, verified by read-back | Description block per market |

Which layer feeds each channel is declared per attribute in the Attribute Definition (CDS200-R026). Unit-pricing and multipack attributes are required by some feed channels in specific countries; the dated requirements live in the CDS-900 platform profiles and are verified there, not here.

## 17. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Ingredient extraction from label images | Ordered candidate list with per-entry confidence | Mandatory human review (R013); order preserved; naming scheme declared |
| Shade family mapping | Family candidate from swatch and shade name | Dictionary validation; split-shade intake per CDS1500-R020 |
| Suitability values | Candidates only from brand declarations (E1/E2) | Declared maxima; merchandising approval |
| Claim language | Candidate claim records flagged "evidence required" | Never accepted without evidence and human review (R037) |
| SPF and ratings | Parsed value and scheme from label | Scheme validation; evidence class check (R030) |
| Free-from validation | None — deterministic | Mechanical conflict check (R033) |
| Market obligation gaps | Candidate list of register entries a product may trigger | Register evaluation is deterministic; AI never marks an obligation satisfied |

AI never manufactures ingredient lists, quantities, ratings, regulatory identifiers or certifications; abstention is a first-class outcome (CDS-700 §17).

## 18. Governance and Organisational Extensions *(informative — rules in CDS-1500 §23 and CDS-800)*

Organisations extend the Chapter 10 vocabularies, add ingredient dictionaries and fragrance-note vocabularies, and declare claim-evidence thresholds under the same rules as any dictionary (CDS1500-R047–R051). The jurisdiction requirement register is maintained per market under CDS-1500 §2.2 with the review cadence declared under CDS-800 §30; the Appendix D seed is a starting point, not a substitute for the organisation's own regulatory advice.

## 19. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS1600-R050** An implementation claiming the CDS Beauty and Health Profile MUST: store ingredient lists as ordered structured lists with declared naming scheme and ordering basis (R009–R010); store active-ingredient quantities, net quantities, pack counts and SPF as typed values with declared units or schemes (R011, R025–R026, R029); apply the CDS-1500 colour architecture to shades with deterministic shade ordering (R020–R021); govern suitability values from manufacturer declarations (R017); govern every claim, certification and free-from statement as an evidence-bearing record with the mechanical free-from conflict check (R032–R035); store regulatory identity and responsible person per market and keep lot-level facts out of canonical product data (R038–R039, R042); maintain and evaluate a jurisdiction requirement register for every market published to (CDS-1500 §2.2); apply category-specific requirements per CDS1500-R009; and publish and verify channel representations under CDS-500.

**CDS1600-R051** An implementation whose scope includes ingestible health products MUST additionally satisfy R046–R049 and the cited CDS-1700 allergen and nutrition rules; a Beauty and Health Profile claim MUST state whether ingestible products are in scope and which jurisdictions its register covers.

## 20. Worked Product Examples *(informative)*

### 20.1 Foundation shade range

```
CAT_family = beauty
CAT_product_type = liquid_foundation
MF_product_form = liquid
MF_makeup_finish = satin
MF_ingredient_naming_scheme = inci
MF_ingredient_order_basis = descending_over_one_percent_then_any_order
MF_range_colourant_convention = range_may_contain
MF_ingredient_list = [aqua, cyclopentasiloxane, glycerin, ..., "+/- ci_77891", "+/- ci_77491"]
MF_skin_type_suitability = [normal, combination]
MF_shade_range_id = range_foundation_2026

Variant (VAR_sku = FND-WS35):
  VAR_colour = colour_warm_sand_3_5      # canonical shade
  VAR_shade_sort_key = 035
  MF_undertone = warm
  VAR_net_quantity = {value: 30, unit: millilitre}

Market registrations:
  {jurisdiction: EU, scheme: eu_cpnp_notification, id: <reference>, status: notified}
  {jurisdiction: GB, scheme: uk_scpn_notification, id: <reference>, status: notified}
  {jurisdiction: US, scheme: us_mocra_product_listing, id: <listing>, status: listed}
  {jurisdiction: CA, scheme: ca_cosmetic_notification, id: <CNF>, status: notified}
  {jurisdiction: AU, scheme: au_cosmetics_information_standard_2020, status: in_scope_no_registration}

Projections:
  MF_colour_display = Warm Sand 3.5
  MF_colour_facet = beige
  CH_google_color = Warm Sand 3.5           # landing-page shade name (CDS-900 §5.2)
  QA_shopify_colour = MATCH
```

### 20.2 SPF 50+ sunscreen sold in Australia and the United States

```
CAT_product_type = sunscreen_lotion
MF_spf_value = 50 (capped_label_plus = true)
MF_spf_rating_scheme = as_nzs_2604              # AU/NZ testing scheme
MF_broad_spectrum = true
MF_water_resistance_minutes = 240
MF_active_ingredients = [{ingredient: zinc_oxide, quantity: 22, basis: percent_w_w}]
CMP_market_registrations =
  [{jurisdiction: AU, scheme: au_artg_listed, id: "AUST L 000000", status: listed},   # placeholder id
   {jurisdiction: US, scheme: us_fda_otc_drug, status: in_scope, evidence: drug_facts_panel}]
CMP_dangerous_goods = not_regulated            # lotion; an aerosol would declare per CDS-1900 §12
VAR_net_quantity = {value: 200, unit: millilitre}
Preflight (AU): ARTG identifier present, TGO 92 label elements present -> publication permitted (R031)
Preflight (US): Drug Facts active-ingredient block present -> publication permitted
```

### 20.3 Vitamin D supplement

```
CAT_product_type = vitamin_supplement
MF_dosage_form = capsule
MF_active_ingredients = [{ingredient: colecalciferol, quantity: 25, unit: microgram, per: capsule}]
MF_serving_size = 1 capsule; MF_servings_per_container = 90
CMP_allergen_declarations = [{allergen: soy, declaration: contains}]      # per CDS-1700 §6
MF_storage_condition = store_below_25c                                     # CDS-1700 §10 dictionary
CMP_market_registrations = [{jurisdiction: AU, scheme: au_artg_listed, id: "AUST L 000001", status: listed},
                            {jurisdiction: CA, scheme: ca_nhp_product_licence, id: "NPN 00000000", status: licensed}]
MF_claims = [{type: health_indication, text: "Supports bone health", scheme: au_permitted_indications,
              jurisdictions: [AU], evidence: E1 sponsor evidence file, owner: regulatory_owner, status: accepted}]
```

## 21. Reference Validation Cases *(informative — the profile's contribution to the cross-industry validation set, REVIEW-020)*

A test dataset supporting a claim of this profile should include, in addition to the CDS-1000 Appendix B negative cases:

- a product whose ingredient list differs by shade (R006);
- a free-from statement that conflicts with the ingredient list and must be blocked (R033);
- a shade range whose brand order differs from alphabetical order (R021);
- a "3 × 50 ml" pack that must not collapse to "150 ml" (R026);
- an SPF value supplied without a scheme, which must not satisfy an R-level requirement (R029);
- a certification whose expiry must withdraw the claim projection without a product edit (R034);
- a therapeutic sunscreen lacking a market regulatory identifier, which preflight must block for that market while permitting publication to a market where it is a cosmetic (R031, R038);
- a supplier feed carrying a batch number in a product field, which must be quarantined rather than stored canonically (R039);
- a product published to the EU after 31 July 2026 whose fragrance allergen declarations follow the pre-2026 list, which the register must flag (Appendix D, D-EU-2).

---

## Appendix A. Beauty and Health Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_product_form | Product | Governed dictionary reference (`beauty_formulation`) | R for skincare, haircare, body, makeup; N/A for tools |
| MF_ingredient_list | Product (variant where R006 applies) | Ordered structured list | R for formulated products |
| MF_ingredient_naming_scheme / MF_ingredient_order_basis | Product | Governed values | R where an ingredient list is R |
| MF_active_ingredients | Product | Structured list with typed quantities | C — R for sunscreens and ingestibles |
| VAR_colour (shade) | Variant | Canonical value_id (colour dictionary) | C — R for colour cosmetics |
| MF_colour_facet | Product/Variant | Derived facet value | R where shade is R (derived) |
| VAR_shade_sort_key | Variant | Sort key | R where shade is R |
| MF_undertone | Variant | Governed value | O |
| MF_makeup_finish | Product | Governed dictionary reference | REC for colour cosmetics |
| MF_skin_type_suitability / MF_hair_type_suitability | Product | Governed dictionary list with declared maximum | REC |
| MF_scent_family | Product | Governed dictionary reference | REC for fragrance and scented products |
| MF_fragrance_concentration | Product | Governed dictionary reference | R for fragrance |
| VAR_net_quantity | Variant | Typed measurement | R |
| VAR_pack_count | Variant | Integer | C — R for multi-unit packs |
| MF_spf_value / MF_spf_rating_scheme / MF_broad_spectrum | Product | Typed value, governed scheme, boolean | R for sun-care products |
| MF_claims / MF_certifications / MF_free_from_statements | Product | Structured records with evidence | C |
| CMP_market_registrations | Product (per market) | Governed records (`regulatory_scheme` dictionary) | C — R where a market regulates the product |
| CMP_responsible_person | Product (per market) | Governed record | C — R where a market requires it on the label or listing |
| CMP_country_of_origin | Product | Governed country reference | C |
| MF_period_after_opening_months / MF_minimum_durability_policy | Product | Integer / governed value | REC; R where a market mandates one of them |
| MF_warning_statements | Product | Structured statement records | C — R where a jurisdiction mandates warnings |
| CMP_dangerous_goods | Product/Variant | Declaration record per CDS-1900 §12 | C |
| MF_dosage_form / MF_serving_size / MF_servings_per_container | Product/Variant | Governed value and typed values | R for ingestibles |
| CMP_allergen_declarations / MF_nutrition_values | Product | Per CDS-1700 §6–§7 | R for ingestibles where labelling requires them |

## Appendix B. Dictionary Bindings *(informative — becomes governed data on adoption per CDS1500-R011)*

| Dictionary key | Package chapter | Bound attribute(s) | Status at 0.8.0 |
|---|---|---|---|
| beauty_formulation | 10 | MF_product_form | Bound by this profile |
| beauty_makeup_finish | 10 | MF_makeup_finish | Bound |
| beauty_scent_family | 10 | MF_scent_family | Bound |
| beauty_skin_type / beauty_hair_type | 10 | MF_skin_type_suitability / MF_hair_type_suitability | Bound |
| fragrance_concentration | 10 (new, 0.8.0) | MF_fragrance_concentration | Bound |
| colour / colour_facet | 1 | VAR_colour, MF_colour_facet | Bound via CDS-1500 §7 |
| jurisdiction / regulatory_scheme | 19 (new, 0.8.0) | CMP_market_registrations, claim and warning records | Bound via CDS-1500 §2.2 |
| allergen / allergen_facet / storage_condition | 17 (new, 0.8.0) | CMP_allergen_declarations, MF_storage_condition (ingestibles) | Bound via CDS-1700 |
| dangerous_goods_class | 18 (new, 0.8.0) | CMP_dangerous_goods | Bound via CDS-1900 §12 |

Deliberately not shipped: ingredient dictionaries (organisations adopt an INCI-based source under their own governance), benefit and ethical claim vocabularies (evidence-gated claim types are organisation-declared), dosage forms (candidate for package 0.9 after profile use).

## Appendix C. References *(informative; retrieved 2026-09-20 unless stated)*

| Ref | Source | Location | Use in this chapter |
|---|---|---|---|
| [B1] | ACCC Product Safety — Cosmetics ingredients labelling mandatory standard (Consumer Goods (Cosmetics) Information Standard 2020) | productsafety.gov.au/business/search-mandatory-standards/cosmetics-ingredients-labelling-mandatory-standard | Ingredient ordering and naming conventions (§5, D-AU-1) |
| [B2] | Federal Register of Legislation — Consumer Goods (Cosmetics) Information Standard 2020 | legislation.gov.au/F2020L01469 | Ordering alternatives; flavour and fragrance declaration (§5) |
| [B3] | AICIS — Personal care, skincare, make-up and other cosmetic products (2025-02-07) | industrialchemicals.gov.au/cosmetics-and-soap | Business registration and ingredient categorisation (D-AU-2) |
| [B4] | Therapeutic Goods Administration — Australian regulatory guidelines for sunscreens (v1.2, 2019); Labelling medicines to comply with TGO 91 and TGO 92 (March 2026); Understanding labelling and presentation requirements for listed medicines (2025-04-09) | tga.gov.au | Therapeutic sunscreen and listed medicine label elements, AUST L/R (§10, §14, D-AU-3) |
| [B5] | New Zealand EPA — Cosmetic Products Group Standard 2020 (HSR002552, consolidated) | epa.govt.nz | NZ ingredient listing, batch code, nano marking, alternative compliance (D-NZ-1) |
| [B6] | U.S. FDA — Cosmetics Labeling Regulations; Summary of Cosmetics Labeling Requirements (2025-11-18); 21 CFR 701.3 (eCFR, current to 2026-08-27) | fda.gov; ecfr.gov | US label elements and ingredient declaration (D-US-1) |
| [B7] | U.S. FDA — Modernization of Cosmetics Regulation Act of 2022 (MoCRA) (2026-08-10); Guidance: Registration and Listing of Cosmetic Product Facilities and Products | fda.gov/cosmetics | Facility registration, product listing, adverse-event contact, enforcement date (D-US-2) |
| [B8] | U.S. FDA — Dietary Supplement Labeling Guide; 21 CFR 101.4(g) and 101.36 | fda.gov | Supplement Facts, ingredient list placement (§14, D-US-4) |
| [B9] | Regulation (EC) No 1223/2009 on cosmetic products, Article 19 (EUR-Lex; UK retained text on legislation.gov.uk) | eur-lex.europa.eu | EU/UK mandatory label particulars, PAO, batch, CPNP (D-EU-1, D-UK-1) |
| [B10] | Commission Regulation (EU) 2023/1545 (fragrance allergens); HPRA guidance on application dates | eur-lex.europa.eu/eli/reg/2023/1545; hpra.ie | Expanded fragrance allergen labelling, 31 July 2026 / 31 July 2028 (D-EU-2) |
| [B11] | GOV.UK — Submit a cosmetic product notification; Making cosmetic products available to consumers in Great Britain; Regulation 1223/2009 and the Cosmetic Products Enforcement Regulations 2013 guidance (2022-04-27) | gov.uk | UK Responsible Person, SCPN, PIF, serious undesirable effects (D-UK-1) |
| [B12] | Health Canada — Industry Guide for the labelling of cosmetics; Cosmetic Regulations (C.R.C., c. 869) ss. 18, 21.2, 30–31; Cosmetic Notification Form | canada.ca; laws-lois.justice.gc.ca | CNF within 10 days, INCI on outer label, bilingual rule, shade-range colourants (D-CA-1) |
| [B13] | Natural Health Products Regulations (SOR/2003-196) | laws-lois.justice.gc.ca | Product licence (NPN), medicinal ingredient quantity per dosage unit (D-CA-2) |
| [B14] | OEHHA — Proposition 65 Clear and Reasonable Warnings (effective 2025-01-01) and FAQs for businesses | oehha.ca.gov; p65warnings.ca.gov | Internet warning before purchase, short-form transition to 2028 (D-US-5) |
| [B15] | Store Leads — The State of Shopify in 2026; Shopify Plus Statistics 2026 (updated 2026-09-11) | storeleads.app | Market basis (header; REVIEW-020) |

## Appendix D. Jurisdiction Requirement Register — Seed *(informative seed of the normative register defined in CDS-1500 §2.2; verification column states what was checked on 2026-09-20)*

Obligation types are those of CDS-1500 §2.2 (pre_market, labelling_element, listing_element, warning_statement, rating_label, restricted_content, transport, documentation, post_market). Each jurisdiction is split into **verified seed entries** (the primary instrument or a regulator publication was read on the stated date; adoptable into the operative register under CDS1500-R060) and **research candidates** (retrieved without reading the instrument, partially verified, seeded from secondary sources, or not seeded; non-normative and excluded from the operative register until verified against the primary instrument, CDS1500-R086). "Not seeded" means the organisation supplies the entry. Jurisdiction codes are those of the `jurisdiction` dictionary (package Chapter 19); scheme codes are those of `regulatory_scheme`.

### D.1 Australia (AU)

#### D.1.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-1 | Consumer Goods (Cosmetics) Information Standard 2020 — ACCC (`au_cosmetics_information_standard_2020`) | Cosmetics made or imported for sale in Australia | labelling_element | Ingredient list on container (or product, or displayed at point of sale where size prevents): descending by mass or volume, or ≥1% descending then <1% any order then colour additives; INCI or English names; flavour/fragrance as such or by components → MF_ingredient_list, MF_ingredient_naming_scheme, MF_ingredient_order_basis, MF_fragrance_disclosure. Hand sanitiser with alcohol as primary active: alcohol % v/v and warning statements → MF_active_ingredients, MF_warning_statements | Products manufactured after the 2020 standard's transition | Verified 2026-09-20 [B1][B2] |
| D-AU-2 | Industrial Chemicals Act 2019 — AICIS (`au_aicis_registration`) | Importers and manufacturers of cosmetics containing industrial chemicals | pre_market (business-level) | Business registration before import or manufacture; ingredient categorisation (exempted / reported / assessed); annual declaration by 30 November → organisation-level record; CMP_market_registrations status `in_scope_business_registered` | Any commercial import; no value threshold | Verified 2026-09-20 [B3] |
| D-AU-3 | Therapeutic Goods Act 1989; TGO 92 (non-prescription medicine labels); Australian regulatory guidelines for sunscreens — TGA (`au_artg_listed`, `au_artg_registered`) | Primary sunscreens; listed and registered complementary medicines and supplements | pre_market; labelling_element; warning_statement | ARTG listing/registration number (AUST L / AUST R); sponsor name and address; active ingredients by Australian Approved Name with proportions; net quantity; batch number; expiry; storage conditions; permitted indications; mandatory excipient declarations; minimum text sizes → CMP_market_registrations (id, sponsor), MF_active_ingredients, VAR_net_quantity, MF_directions, MF_warning_statements, MF_claims (scheme `au_permitted_indications`) | Before supply in Australia | Verified 2026-09-20 [B4] |
| D-AU-5 | Australian Dangerous Goods Code edition 7.9 — NTC/state regulators (`au_adg_code_7_9`) | Aerosols, flammable liquids (alcohol-based fragrance, sanitiser), certain nail products | transport | Dangerous-goods declaration per CDS-1900 §12 | Mandatory from 1 October 2025 | Verified 2026-09-20 (CDS-1900 Appendix C) |

#### D.1.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-4 | Poisons Standard (SUSMP) scheduling of ingredients — TGA/states | Cosmetics and health products containing scheduled substances | restricted_content | Scheduling status per ingredient; label statements where scheduled → MF_warning_statements | Ingredient-dependent | Retrieved (not spot-verified) |

### D.2 New Zealand (NZ)

#### D.2.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-1 | Cosmetic Products Group Standard 2020 (HSR002552) — EPA (`nz_cosmetic_products_group_standard_2020`) | Cosmetic products imported or manufactured in NZ | labelling_element; pre_market (nano notification) | Ingredient list (≥1% descending, <1% any order, colour additives, flavour/fragrance wording) → MF_ingredient_list, MF_ingredient_order_basis; manufacturer source or batch code → lot-level (R039); "nano" marking → MF_nanomaterial_ingredients; nanomaterial notification to the EPA at first import → CMP_market_registrations. Alternative compliance: a label compliant with AU, US, CA, UK or EU cosmetic labelling requirements satisfies the ingredient-list and schedule conditions → CMP_market_registrations status `alternative_compliance` with the relied-on jurisdiction recorded | Group Standard in force from 30 April 2021; four-year transition to 30 April 2025 for Labelling, SDS and Packaging Notices | Verified 2026-09-20 [B5] |

#### D.2.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-2 | Sunscreen (Product Safety Standard) Act 2022 — MBIE (`nz_sunscreen_product_safety_standard`) | Primary sunscreens | pre_market; rating_label | Compliance with AS/NZS 2604 (SPF, broad-spectrum, water resistance testing) → MF_spf_value, MF_spf_rating_scheme; the Group Standard also permits labelling to the Australian Therapeutic Goods Order for primary sunscreens | From September 2022 | Retrieved (not spot-verified) |
| D-NZ-3 | Dietary Supplements Regulations 1985 / natural health products reform — MPI/Medsafe | Supplements | labelling_element | Not seeded — organisation supplies | — | Not seeded |

### D.3 United States (US, with California noted)

#### D.3.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-1 | FD&C Act and Fair Packaging and Labeling Act; 21 CFR parts 701 and 740 — FDA (`us_fda_cosmetic_labeling_21cfr701`) | Cosmetics sold at retail | labelling_element; warning_statement | Principal display panel: identity statement and net quantity (US customary units, metric optional) → VAR_net_quantity; information panel: name and place of business (with "Manufactured for" / "Distributed by" where applicable) → CMP_responsible_person; ingredient declaration in descending order of predominance, colour additives and ≤1% ingredients in any order, "fragrance"/"flavor" permitted, cosmetic-drug products declare active ingredients first → MF_ingredient_list, MF_ingredient_order_basis, MF_active_ingredients; required warnings (aerosols, feminine deodorant sprays, children's bubble bath, flammables; "safety not determined" where unsubstantiated) → MF_warning_statements; English mandatory | Ongoing | Verified 2026-09-20 [B6] |
| D-US-2 | Modernization of Cosmetics Regulation Act of 2022 (MoCRA), FD&C Act s. 607 — FDA (`us_mocra_product_listing`) | Cosmetics distributed in the US (small-business exemptions apply, with exclusions) | pre_market (facility registration, product listing); post_market (adverse events); labelling_element | Facility registration (biennial renewal); product listing including ingredients, updated annually; responsible person contact for adverse-event reporting on the label; serious adverse events reported within 15 business days → CMP_market_registrations (listing reference), CMP_responsible_person | Enforcement of registration and listing from 1 July 2024; listing within 120 days of first marketing | Verified 2026-09-20 [B7] |
| D-US-4 | Dietary Supplement Health and Education Act; 21 CFR 101.36 — FDA (`us_fda_dietary_supplement_labeling`) | Dietary supplements | labelling_element | Statement of identity, net quantity, Supplement Facts panel (serving size, servings per container, dietary ingredients and amounts, %DV), ingredient list immediately below the panel, structure/function claim disclaimer, name and place of business → MF_serving_size, MF_servings_per_container, MF_nutrition_values (scheme `supplement_facts`), MF_ingredient_list, MF_claims, CMP_responsible_person | Ongoing | Verified 2026-09-20 [B8] |
| D-US-5 | Proposition 65 (California), 27 CCR 25602–25603 — OEHHA (`us_ca_prop65_warning`) | Products causing exposure to listed chemicals, sold to California consumers by businesses with 10+ employees | warning_statement (listing_element for internet sales) | Warning on the product display page, a clearly marked "WARNING" hyperlink, or a warning prominently displayed before purchase; new short-form content names at least one chemical per endpoint; retailers have 60 days to update online warnings after notice → MF_warning_statements (jurisdiction US-CA), projected to listings | Amended regulations effective 1 January 2025; products manufactured and labelled before 1 January 2028 may use the prior short-form | Verified 2026-09-20 [B14] |

#### D.3.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-3 | OTC drug labelling (Drug Facts), 21 CFR 201.66 and the sunscreen monograph — FDA (`us_fda_otc_drug`) | Sunscreens, antiperspirants, anti-dandruff and other cosmetic-drug products | labelling_element | Drug Facts panel with active ingredients and purposes before cosmetic ingredients; SPF and broad-spectrum statements per monograph → MF_active_ingredients, MF_spf_value, MF_spf_rating_scheme=`fda_sunscreen_monograph`, MF_warning_statements | Ongoing | Verified in part 2026-09-20 [B6] (21 CFR 701.3(d)); monograph text not read |

### D.4 European Union (EU)

#### D.4.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-1 | Regulation (EC) No 1223/2009 on cosmetic products, Articles 4, 11, 13, 19 — European Commission and member-state authorities (`eu_cosmetics_regulation_1223_2009`, `eu_cpnp_notification`) | Cosmetics made available in the EU | pre_market (Responsible Person, CPNP notification, product information file); labelling_element | Responsible Person name and address (EU) on container and packaging; country of origin for imported products; nominal content by weight or volume (exemptions <5 g/ml, samples, single-application); date of minimum durability (hourglass or "best used before the end of") where durability ≤30 months, otherwise period after opening symbol with months; particular precautions; batch number or product reference; function unless obvious; list of ingredients preceded by "ingredients", descending order by weight at time of addition, <1% any order, colourants may be listed last, "parfum"/"aroma", nanomaterials marked "(nano)", range colourants with "may contain"/"+/−"; product information file kept 10 years; notification of label and packaging photograph → CMP_responsible_person, CMP_country_of_origin, VAR_net_quantity, MF_minimum_durability_policy, MF_period_after_opening_months, MF_warning_statements, MF_ingredient_list, MF_ingredient_order_basis, MF_range_colourant_convention, MF_nanomaterial_ingredients, CMP_market_registrations | Ongoing | Verified 2026-09-20 [B9] |
| D-EU-2 | Commission Regulation (EU) 2023/1545 amending Annex III (fragrance allergens) (`eu_fragrance_allergens_2023_1545`) | Cosmetics containing listed fragrance allergens above 0.001% (leave-on) or 0.01% (rinse-off) | labelling_element | Individual naming of each listed allergen in the ingredient list in addition to "parfum"/"aroma" → CMP_fragrance_allergen_declarations, MF_ingredient_list | Products placed on the market from 31 July 2026 must comply; products placed earlier may be made available until 31 July 2028 | Verified 2026-09-20 [B10] |
| D-EU-4 | Regulation (EU) 2023/988 General Product Safety Regulation (`eu_gpsr_2023_988`) | Non-harmonised consumer products in this profile (beauty tools, accessories) and cross-cutting distance-selling duties | listing_element; labelling_element | Online offers must show manufacturer name, postal and electronic address, product identifier (type/batch/serial), warnings and safety information and a picture; an EU-established responsible economic operator → CMP_responsible_person, CMP_product_identifier, MF_warning_statements | Applies from 13 December 2024 | Verified 2026-09-20 (CDS-1800 Appendix C) |

#### D.4.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-3 | Regulation (EU) No 655/2013 (common criteria for claims) | Cosmetic claims | restricted_content | Claims must satisfy legal compliance, truthfulness, evidential support, honesty, fairness and informed decision-making criteria → MF_claims evidence records | Ongoing | Retrieved (not spot-verified) |

### D.5 United Kingdom (GB)

#### D.5.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-1 | Regulation (EC) 1223/2009 as retained (UK Cosmetics Regulation) and Cosmetic Products Enforcement Regulations 2013 — OPSS (`uk_cosmetics_regulation`, `uk_scpn_notification`) | Cosmetics made available in Great Britain | pre_market (UK Responsible Person; SCPN notification before placing on the market; PIF); labelling_element; post_market (serious undesirable effects) | UK Responsible Person with a UK established address (not a PO box or mail-forwarding address) named on packaging (mandatory for all products from 31 December 2022 for those previously on the EU market); notification through the Submit Cosmetic Product Notification service with category, name, RP, PIF address, urgent contact, nanomaterials, CMR substances, ingredient summary, label image and packaging photograph; label elements as per Article 19 in English → CMP_responsible_person, CMP_market_registrations (scheme `uk_scpn_notification`), same label fields as D-EU-1 | New products since 1 January 2021 | Verified 2026-09-20 [B9][B11] |

#### D.5.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-2 | Fragrance allergen labelling in GB | Cosmetics with fragrance allergens | labelling_element | GB retained the pre-2023 Annex III allergen list at the end of the transition period; whether GB adopts the expanded list is a register review item → CMP_fragrance_allergen_declarations with scheme `uk_fragrance_allergens_retained` | Review each release | Not verified — organisation confirms current GB Annex III |

### D.6 Canada (CA)

#### D.6.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-CA-1 | Food and Drugs Act; Cosmetic Regulations (C.R.C., c. 869) ss. 18, 21.2–21.5, 30–31; Consumer Packaging and Labelling Act — Health Canada (`ca_cosmetic_notification`) | Cosmetics sold in Canada | pre_market (notification); labelling_element | Cosmetic Notification Form within 10 days after first sale, including product name, function (leave-on / rinse-off), ingredient list with exact concentrations or concentration ranges, form, manufacturer or importer name and address in Canada; revised notification within 10 days of any inaccuracy; ingredient list on the outer label using INCI names (or chemical name where none; Schedule EU technical name / INCI / French equivalent alternatives), botanicals by genus and species, shade-range colourants with "+/−" or "may contain/peut contenir"; all other required label information in English and French; Cosmetic Ingredient Hotlist restrictions → CMP_market_registrations (CNF reference), MF_ingredient_list (naming scheme `inci`), MF_range_colourant_convention, CMP_responsible_person, localisation dimension per CDS-300 §18 | Within 10 days of first sale; sale prohibited after the 10-day period if not notified | Verified 2026-09-20 [B12] |
| D-CA-2 | Natural Health Products Regulations (SOR/2003-196) — Health Canada (`ca_nhp_product_licence`) | Vitamins, minerals, herbal remedies and other natural health products | pre_market (product licence); labelling_element | Product licence (NPN) before sale; application includes medicinal ingredients with proper and common names, quantity per dosage unit and potency, non-medicinal ingredients with purpose, label text; licence changes notified within 60 days → CMP_market_registrations (id = NPN), MF_active_ingredients, MF_ingredient_list | Before sale | Verified 2026-09-20 [B13] |

#### D.6.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

*None.*

### D.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Japan (JP), China (CN), Singapore (SG), Republic of Korea (KR), India (IN), Brazil (BR) | Not seeded | The `jurisdiction` dictionary carries codes so an organisation can extend the register; China's cosmetics regime (CSAR, NMPA filing and registration) and Japan's Pharmaceutical and Medical Device Act notably differ from the seeded markets and require local regulatory advice before publication. |

END OF CDS-1600 v0.3 REVIEW DRAFT
