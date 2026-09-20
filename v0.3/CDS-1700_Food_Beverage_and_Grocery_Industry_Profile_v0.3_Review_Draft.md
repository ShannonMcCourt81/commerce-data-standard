# Commerce Data Standard (CDS)
## CDS-1700 — Food, Beverage and Grocery Industry Profile

| Field | Value |
|---|---|
| Status | **v0.3 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.3 (single corpus release per ADR-D5); chapter added in the 2026-09-20 industry-profile expansion that produced v0.3 (changelog REVIEW-021) |
| Date | 2026-09-20 |
| Supersedes | Nothing — first edition. Package Chapter 17 (Food & Beverage: allergens, allergen facets, dietary claim types, storage conditions) is shipped with this profile in package 0.8.0. |
| Normative status | §1, §3, §5–§14, §19 and Appendix A are normative. §2 (pointer), §4, §15–§18, §20, §21 and Appendices B–D are informative; Appendix D seeds the jurisdiction requirement register whose record structure and obligations are normative in CDS-1500 §2.2. Every table is individually marked. |
| Primary audience | Grocery and specialty-food merchandisers, regulatory and food-safety owners, data stewards, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1500, especially CDS-200, CDS-300 (CMP_, PRC_ conditional), CDS-400 (dictionaries, units), CDS-500 (preflight, verification), CDS-600 (facets), CDS-700 (evidence, claims), CDS-900 (platform profiles), CDS-1500 (profile model, requirement levels, profile register, jurisdiction requirement register), CDS-1900 (kits, bundles, dangerous goods), CDS-2000 (pet food cross-reference) |
| Companion package | CDS Reference Dictionary: Chapter 17 (Food & Beverage), Chapter 19 (Jurisdictions & Regulatory Schemes); column contract per CDS-1500 Appendix E |
| Profile identifier | `cds.profile.food_beverage.v0_3` (registered in CDS-1500 §2.1) |
| Research basis | REVIEW-020 (global commerce vertical market research, 2026-09-20): food and beverages is a top-three worldwide ecommerce revenue segment (estimated at roughly US$0.9 trillion for 2026, with the fastest growth of the large segments); Food & Drink is the fourth-largest Shopify Plus vertical worldwide (8.3% of Plus stores). |

Terminology follows CDS-100. Attribute requirement levels (R, C, REC, O, N/A) are those of CDS-1500 §4 and are not restated here.

---

## 1. Purpose and Scope *(normative)*

CDS-1700 defines the industry profile for packaged and fresh food, non-alcoholic and alcoholic beverages, and grocery consumables. It covers ambient, chilled and frozen goods; multipacks, cases and hampers; variable-weight products; and the regulated information that every market attaches to a food label: ingredients, allergens, nutrition, quantity, date marking, storage, origin and alcohol content. Dietary supplements and complementary medicines are homed in CDS-1600 §14 and cite this chapter; pet food is homed in CDS-2000 §12 and cites this chapter's allergen and nutrition mechanics.

The data shape is distinctive because most of the record is regulated content whose authority is the label and the manufacturer's specification, because "contains" and "may contain" have different legal meanings, because nutrition values are numeric tables under jurisdiction-specific schemes, and because the sellable unit hierarchy (each, inner, case) and variable weight break the assumptions of a simple product-variant model. In every seeded market, mandatory food information must be available to the consumer before an online purchase is concluded, which makes the completeness of this data a publication gate, not a merchandising nicety.

**CDS1700-R001** An implementation claiming the Food and Beverage Profile MUST represent ingredients, allergen declarations, nutrition values, net quantity, date-marking policy, storage conditions, origin and alcohol content as structured, typed attributes conforming to CDS-200 §7 and CDS-400 §18, never solely as free text.

**CDS1700-R002** An implementation claiming this profile MUST distinguish regulated declarations (allergens, nutrition, origin, alcohol content) from dietary and marketing claims, and MUST govern every claim under CDS-700 §7 and §8 of this chapter.

**CDS1700-R003** An implementation MUST maintain a jurisdiction requirement register (CDS-1500 §2.2) for every market it publishes food to, and publication preflight for a market MUST evaluate the mandatory food information required by that market before the offer is made available.

**CDS1700-R004** This profile MUST NOT weaken any rule of CDS-1500 that it reuses; where this chapter is silent, CDS-1500 and the core chapters govern.

## 2. Profile Model *(informative pointer)*

This profile applies the industry profile model of CDS-1500 §2, the requirement levels of CDS-1500 §4 and the jurisdiction requirement register of CDS-1500 §2.2 without restatement. Its identifier and dictionary bindings are recorded in CDS-1500 §2.1; its seeded jurisdiction entries are in Appendix D.

## 3. Product Model *(normative)*

A food product is a recipe or formulation offered in one or more sellable presentations. The Product is the formulation; Variants are the sellable units that differ by net quantity, pack configuration, flavour or vintage. Above the variant sits the sale-unit hierarchy (each, inner pack, case), each level of which may carry its own trade identifier.

```
Product: Toasted Muesli                          (informative example)
  Product scope:
    CAT_product_type = breakfast_cereal
    MF_ingredient_list = [rolled oats (55%), honey, almonds, ...]   # ordered, with characterising %
    CMP_allergen_declarations = [{allergen: oats, declaration: contains, gluten: true},
                                 {allergen: almond, declaration: contains},
                                 {allergen: milk, declaration: may_contain, basis: shared_line}]
    MF_nutrition_values = {scheme: nip_au_nz, per_100g: {...}, per_serving: {...}, serving_size_g: 45}
    MF_storage_condition = ambient
    MF_date_mark_type = best_before
    CMP_origin_declaration = {jurisdiction: AU, type: made_in_australia, australian_ingredients_band: gte_90_percent}
  Variant scope:
    VAR_net_quantity = {value: 750, unit: gram}
    VAR_gtin = 09300000000001
    VAR_sale_unit_level = each
```

**CDS1700-R005** Net quantity, pack configuration (count of identical units), flavour or variety, and vintage MUST be modelled at variant scope where they identify distinct sellable units (variant boundary rule: CDS-200 §5); ingredients, allergens, nutrition per 100 g or ml, origin and claims MUST remain at product scope unless the fact genuinely differs between variants (a flavour variant normally carries its own ingredient list and allergen declarations).

**CDS1700-R006** Where a flavour or variety variant has its own ingredient list, allergen declarations or nutrition values, those facts MUST be stored at variant scope for that variant and the product-scope values MUST NOT be published as if they applied to it.

**CDS1700-R007** Sale-unit levels (each, inner, case, pallet) MUST be modelled as a declared hierarchy with a level identifier, the quantity of the child unit contained, and the trade identifier of the level (GTIN-13/GTIN-14 or equivalent) where one exists; a case MUST NOT be modelled as an unrelated product.

**CDS1700-R008** A multipack of identical units MUST be represented as a variant with a pack count; a bundle or hamper of different products MUST be represented as a kit with component relationships per CDS-200 §7A.2, with allergen and nutrition information carried by each component and the kit-level declarations derived, never authored.

## 4. Product Families and Category Profiles *(informative baseline; the inheritance rule of CDS1500-R016 applies)*

| Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|
| Ambient packaged food (pantry, snacks, cereals, confectionery) | ingredient list; allergen declarations; nutrition values; net quantity; date-mark type; storage condition; origin per market | dietary claim records; serving size; characterising ingredient percentages | size, flavour, multipack |
| Chilled and frozen food | as ambient plus temperature class and shelf-life policy | thawing/handling instructions; minimum remaining shelf life at dispatch | size, flavour |
| Fresh produce, meat, seafood (variable weight) | net quantity basis (per kg or per unit); origin; storage; catch-weight flag | grade; cut; sustainability certifications | weight band, pack |
| Bakery | ingredient list; allergens; date-mark type | nutrition (where required); prepacked-for-direct-sale status | size |
| Non-alcoholic beverages | ingredient list; allergens; nutrition; net volume; storage; caffeine and sweetener warnings where applicable | serving size; sugar content claims | volume, multipack |
| Alcoholic beverages | alcohol by volume; standard drinks or units where required; allergens; net volume; pregnancy or health warnings per market; age restriction | vintage, varietal, region, closure (wine); style (beer); ingredients and energy where the market requires | volume, vintage, multipack |
| Infant and special-purpose foods | as ambient plus special labelling regime | — | size |
| Grocery non-food consumables (cleaning, paper) | net quantity; hazard statements where chemical | — | size, multipack |
| Meal kits, hampers, gift sets | kit composition; component declarations derived | — | configuration |

## 5. Ingredients *(normative; seed guidance informative)*

| Field | Meaning | Type |
|---|---|---|
| MF_ingredient_list | Ordered statement of ingredients as declared, with compound ingredients expanded or named per the label | Ordered list of entries (name, optional canonical reference, optional percentage, optional function class and additive code, optional sub-ingredients) |
| MF_ingredient_order_basis | Ordering rule applied | Governed value: `descending_by_ingoing_weight` (the rule in every seeded market), with declared exceptions for water, <2% groupings (US) or similar |
| MF_characterising_ingredient_percentages | Quantitative ingredient declarations (QUID) | Structured list (ingredient, percentage) |
| MF_additive_declaration_scheme | How additives are named | Governed value: `function_class_plus_name_or_number`, `name_only` |

**CDS1700-R009** `MF_ingredient_list` MUST be stored as an ordered list whose order is declared significant (CDS400-R040) and MUST preserve the label order; the implementation MUST NOT re-sort or de-duplicate the list without a governed change carrying label or specification evidence.

**CDS1700-R010** Compound ingredients MUST be represented so that their sub-ingredients remain identifiable, because allergen declarations (§6) depend on sub-ingredients still present in the finished food.

**CDS1700-R011** Characterising ingredient percentages MUST be numeric values linked to the ingredient entry (CDS400-R056), never text within the ingredient name alone.

**CDS1700-R012** An ingredient list captured by extraction from label images or supplier documents (evidence class E2 or E3) MUST be reviewed by a human before acceptance regardless of confidence (CDS-700 §19).

## 6. Allergen Declarations *(normative; dictionary seed informative)*

Allergen information is the highest-consequence data in this vertical. The profile separates three things that are routinely conflated: the regulated declared name of an allergen in a given market, the declaration type (present as an ingredient versus precautionary "may contain"), and the customer-facing facet a storefront chooses to expose.

| Field | Meaning | Type |
|---|---|---|
| CMP_allergen_declarations | Allergen declaration records | List of records: allergen (`allergen` dictionary value_id), declaration type (`contains`, `may_contain`, `free_from_claimed`), basis (ingredient, processing aid, cross-contact, shared line), gluten flag where the allergen is a gluten-containing cereal, market naming override where a market requires a different required name |
| CMP_allergen_scheme | The market allergen scheme the declarations are evaluated against | Governed value from `regulatory_scheme` (e.g. `au_fsanz_1_2_3_allergens`, `eu_fic_1169_2011_annex_ii`, `us_falcpa_faster`, `ca_fdr_priority_allergens`) |

**CDS1700-R013** Allergen declarations MUST be stored as structured records bound to the governed `allergen` dictionary, one record per allergen, and MUST NOT be stored only as prose inside the ingredient list or description.

**CDS1700-R014** The declaration type MUST distinguish an allergen present as an ingredient or processing aid (`contains`) from a precautionary cross-contact statement (`may_contain`); the two MUST NOT be merged into one list, and a channel projection MUST label them differently.

**CDS1700-R015** The declared name projected to a market MUST be the required name of that market's scheme (for example the individual tree-nut name required in Australia, or the "nuts" group emphasis in the EU); the canonical dictionary value MUST resolve to the required name through the market mapping, never through free text authored per product.

**CDS1700-R016** Allergen declarations MUST NOT be derived automatically from the ingredient list without human review; AI or rules MAY propose a declaration from an ingredient, but acceptance MUST require review regardless of confidence, and the absence of an allergen in the ingredient list MUST NOT generate a "free from" declaration (CDS700-R018).

**CDS1700-R017** A "free from" or "allergen-free" statement is a claim (§8) and MUST fail validation when the named allergen appears in a `contains` declaration for the same product or variant (the CDS1600-R033 pattern); a `may_contain` declaration for the same allergen MUST trigger review of the claim.

**CDS1700-R018** Allergen declarations MUST be evaluated at publication preflight for each market against the market's scheme: an allergen required by the market that is present in the ingredient list without a declaration MUST block publication to that market (CDS400-R033 pattern).

*Informative — seeded schemes.* The package `allergen` dictionary carries the regulated required names of the seeded jurisdictions as canonical values with an ordered `allergen_facet` mapping to the fourteen EU groups (cereals containing gluten, crustaceans, eggs, fish, peanuts, soybeans, milk, nuts, celery, mustard, sesame, sulphites, lupin, molluscs). Australia's Plain English Allergen Labelling (Standard 1.2.3 and Schedule 9, mandatory from 25 February 2024) requires individual tree nuts, individual gluten cereals (barley, oats, rye when containing gluten), wheat, fish, crustacean, mollusc, egg, milk, lupin, peanut, soy, sesame and sulphites at 10 mg/kg or more, declared in bold in the ingredient list and in a "Contains" summary statement. The United States requires nine major allergens (milk, eggs, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, sesame) with species or type named. Canada's priority allergens add mustard and sulphites. Appendix D records the per-market rules with verification dates.

## 7. Nutrition Values *(normative)*

| Field | Meaning | Type |
|---|---|---|
| MF_nutrition_values | Nutrition declaration | Structured object: scheme (governed: `nip_au_nz`, `eu_nutrition_declaration`, `us_nutrition_facts`, `ca_nutrition_facts_table`, `supplement_facts`, `typical_analysis_pet_food`), basis columns (per 100 g / 100 ml and/or per serving as the scheme requires), serving size as typed measurement, servings per package, nutrient rows (nutrient identifier, value, unit, rounding rule applied, %DV or %RI where the scheme uses it) |
| MF_energy_kj / MF_energy_kcal | Energy values per basis | Typed numbers (derived from the nutrition object) |
| MF_front_of_pack_rating | Voluntary or mandatory front-of-pack scheme result | Structured (scheme, value, calculation version) |

**CDS1700-R019** Nutrition values MUST be numeric, unit-bearing values under a declared scheme (CDS400-R056–R057); a scheme MUST be declared because nutrient sets, mandatory bases, rounding and %DV reference amounts differ by market, and one value set MUST NOT be presented as satisfying a scheme it was not prepared for.

**CDS1700-R020** Where a market requires both a per-100 basis and a per-serving basis (Australia and New Zealand), both MUST be present; where a market requires per-serving with a defined serving size (United States, Canada), the serving size MUST be a typed measurement with its household-measure label where the scheme requires it.

**CDS1700-R021** Nutrition values MUST NOT be generated, estimated or "filled in" by AI; extraction from a label image or specification is permitted only as a proposal with mandatory human review (CDS-700 §19), and an accepted value MUST retain provenance to the specification or label it came from (E1/E2).

**CDS1700-R022** A front-of-pack rating (for example a health star rating, a nutrition symbol or a nutrient-profile score) MUST be stored with its scheme and calculation version and MUST NOT be recomputed by the PIM unless the organisation declares itself the calculating authority under CDS-200 §13.

## 8. Dietary Suitability, Claims and Certifications *(normative; dictionary seed informative)*

Dietary suitability is the primary purchase driver in this vertical and the most abused data. The profile treats every dietary statement as a claim record whose type comes from the governed `dietary_claim_type` dictionary and whose acceptance depends on evidence appropriate to the type: a regulated definition (gluten free), a certification (organic, halal, kosher), or a manufacturer declaration where no regulated definition exists (vegan, vegetarian).

| Attribute | Structure | Requirement guidance |
|---|---|---|
| MF_dietary_claims | List of claim records: claim type (governed), evidence class and reference, certifier and certificate where applicable, jurisdictions in which the claim is published, owner, effective/expiry | C — required when any dietary statement is published |
| MF_nutrition_content_claims | Nutrition content claims ("low fat", "source of fibre") with the scheme and condition satisfied | C |
| MF_health_claims | Health claims with the scheme, the permitted relationship and any required dietary-context statement | C |
| MF_certifications | Certification records (scheme, certifier, identifier, scope, expiry) | C |

**CDS1700-R023** A dietary claim MUST exist as a claim record with a governed claim type and an evidence reference; a claim type whose definition is regulated in a market (for example gluten free) MUST carry the regulated threshold or definition satisfied for that market in the claim record.

**CDS1700-R024** Dietary claims MUST NOT be inferred from the ingredient list by rules or AI without human review; a product with no animal ingredients is not thereby "vegan" in the canonical data (CDS400-R066, CDS700-R018).

**CDS1700-R025** Nutrition content claims and health claims MUST reference the scheme under which they are permitted in each market they are published to; publication preflight MUST block a health claim not permitted under the declared scheme for that market or lacking a required accompanying statement.

**CDS1700-R026** A customer facet for dietary suitability MUST be fed only by accepted claim records (a claim-driven facet, the CDS1500-R025 pattern) and MUST NOT be assigned per product from marketing copy or supplier tags.

**CDS1700-R027** Certification expiry MUST withdraw the dependent claim projection without editing any product fact (CDS1500-R032).

## 9. Quantity, Pack Hierarchy, Unit Pricing and Variable Weight *(normative)*

**CDS1700-R028** Net quantity MUST be a typed measurement with a declared unit (gram, kilogram, millilitre, litre, or count) at variant scope; drained weight, where declared, MUST be a separate typed value.

**CDS1700-R029** Pack count MUST be an integer separate from unit net quantity (a "6 × 375 ml" multipack is pack count 6 and net quantity 375 ml), and the total net quantity MUST be derived, never authored.

**CDS1700-R030** Where a market or channel requires unit pricing, the unit-price base measure MUST be derived from the typed net quantity and pack count and the price authority (CDS-200 §13; `PRC_` fields only where the PIM is the declared authority), never keyed by hand.

**CDS1700-R031** Variable-weight (catch-weight) products MUST carry a catch-weight flag, a pricing basis (per kilogram or per unit), and a nominal or average weight as a typed value; they MUST NOT be presented as fixed-weight products, and the sellable unit's actual weight is an order-level observation, not canonical product data.

**CDS1700-R032** Trade identifiers at each sale-unit level MUST be stored with their scheme (GTIN-8/12/13/14 or an organisation-declared alternative) and MUST validate per scheme (CDS-1100 GTIN rules).

## 10. Storage, Temperature, Shelf Life and Date Marking *(normative; dictionary seed informative)*

| Field | Meaning | Type |
|---|---|---|
| MF_storage_condition | Governed storage condition (`storage_condition` dictionary: ambient, store_below_25c, refrigerate, refrigerate_after_opening, frozen, keep_frozen_do_not_refreeze, store_in_cool_dry_place) | Product |
| MF_temperature_class | Logistics temperature class (ambient / chilled / frozen) | Governed value |
| MF_date_mark_type | The date-mark regime the product carries (`best_before`, `use_by`, `baked_on`, `packed_on`, `none_exempt`) | Governed value |
| MF_shelf_life_days | Shelf life from production under declared storage | Integer |
| MF_minimum_remaining_shelf_life_days | Policy: minimum remaining life at dispatch | Integer |
| MF_storage_instructions | Storage and after-opening instructions as labelled | Structured statement records |

**CDS1700-R033** Storage condition and temperature class MUST be governed values; free text such as "keep cool" MUST NOT satisfy the requirement.

**CDS1700-R034** The date-mark type MUST be a governed value that distinguishes a safety-based "use by" from a quality-based "best before"; the actual date on a unit is lot-level and MUST NOT be stored as a canonical product attribute (the CDS1600-R039 pattern), but the shelf-life policy MAY be.

**CDS1700-R035** A product whose date-mark type is `use_by` MUST carry a minimum-remaining-shelf-life policy before publication to a channel that ships to consumers, so that fulfilment can be verified against it.

## 11. Origin and Provenance *(normative)*

| Field | Meaning | Type |
|---|---|---|
| CMP_country_of_origin | Country of origin under the applicable determination rule | Governed country reference |
| CMP_origin_declarations | Per-market origin declaration records | List: jurisdiction, scheme, declaration type (e.g. `grown_in`, `produced_in`, `made_in`, `packed_in`, `product_of`, `origin_statement`), percentage-of-local-ingredients band where the scheme uses one, mark or logo eligibility |
| MF_region_of_origin | Sub-national origin (wine region, PDO/PGI name) | Governed value where a scheme protects the name |

**CDS1700-R036** Origin MUST be stored as a governed country reference plus per-market declaration records; a single free-text origin string MUST NOT be projected to markets whose schemes require a specific declaration form.

**CDS1700-R037** Protected geographical names (designations of origin and geographical indications) MUST be governed values with evidence and MUST NOT be assigned from supplier descriptions without verification.

## 12. Alcoholic Beverages *(normative)*

| Field | Meaning | Type |
|---|---|---|
| MF_alcohol_by_volume | Alcoholic strength by volume at 20 °C | Decimal percentage (typed) |
| MF_standard_drinks / MF_alcohol_units | Standard drinks (or units) per container under the market's definition | Decimal with scheme (e.g. `au_nz_standard_drink_10g`, `uk_unit_8g`) |
| CMP_alcohol_warnings | Mandatory warning statements per market (pregnancy warning, government warning) | Structured statement records with scheme, pictogram version and size class |
| MF_beverage_style | Wine varietal and vintage; beer style; spirit category | Governed values |
| CMP_age_restriction | Minimum purchase age per market | Per-market records |

**CDS1700-R038** Alcohol by volume MUST be a typed decimal percentage; where a market requires a different expression below a threshold (for example a "contains not more than X% alcohol by volume" statement), the projection MUST derive it from the typed value.

**CDS1700-R039** Standard drinks or units MUST be stored with the definition scheme they were calculated under and MUST NOT be recalculated across schemes without a declared conversion rule (CDS400-R057).

**CDS1700-R040** Mandatory alcohol warnings MUST be structured statement records with the scheme and the pictogram or wording version, evaluated per market at preflight; a product above a market's threshold lacking the market's warning MUST NOT be published to that market.

**CDS1700-R041** Age restriction MUST be a governed per-market attribute evaluated at preflight and projected to channels that support age gating.

## 13. Warnings, Advisory Statements and Restricted Sale *(normative)*

**CDS1700-R042** Warning and advisory statements required by a market (caffeine, phenylalanine, sweeteners, quinine, kava, royal jelly, choking hazards, "contains a source of…" statements) MUST be structured statement records with the mandating scheme, evaluated per market at preflight; the trigger conditions (ingredient present, quantity threshold) MUST be expressed as rules (CDS200-R034).

**CDS1700-R043** Products subject to sale restrictions in a market (alcohol, restricted supplements, tobacco where in scope) MUST carry a governed restriction attribute per market and MUST NOT be published to a channel or market whose capability declaration cannot enforce the restriction.

## 14. Safety, Recalls and Dangerous Goods *(normative)*

**CDS1700-R044** A recall or withdrawal MUST be expressed through lifecycle state and channel withdrawal (CDS-500 §12) with the affected lot range recorded as an observation, never by deleting the product; lot-level recall scope is outside canonical product data but MUST be linkable to the product.

**CDS1700-R045** Grocery consumables that are hazardous chemicals or dangerous goods for transport (aerosols, high-strength spirits, cleaning chemicals) MUST carry a dangerous-goods declaration per CDS-1900 §12 and, where a market requires it, a safety data sheet reference (CDS-1900 §12).

## 15. Customer Facet Design *(informative — normative facet rules live in CDS-600)*

| Facet | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Dietary suitability | Claim-driven facet fed by accepted claim records (R026); labels express the claim type (Gluten free, Vegan) | Facet populated from supplier tags or inferred from ingredients |
| Allergen-free browsing | Exclusion filters driven by `contains` declarations only, with a visible note that precautionary statements are not filtered unless the organisation declares otherwise | Treating "may contain" as absence |
| Category and product form | Classification-driven | Cuisine and occasion mixed with product type |
| Size / pack | Net-quantity ranges and pack counts | Mixed grams and millilitres in one list |
| Origin | Country and region facets from governed values | Free-text origin |
| Storage | Ambient / chilled / frozen for delivery planning | — |
| Alcohol | Style, varietal, region, ABV range | Health claims |

Zero-result handling, coverage thresholds and accessibility follow CDS-600 §10, §17 and §24.

## 16. Channel Projection Guidance *(informative — normative rules: CDS-500, CDS-900)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Ingredient list, allergens, nutrition | Structured metafields generated from canonical records (Shopify's standard taxonomy exposes allergen, dietary and flavour attributes for food categories); read back and verified per market | Description blocks per market; no standard nutrition fields in the seeded feed channels |
| Net quantity, pack count, unit pricing | Typed metafields; variant title composition per declared policy | `unit_pricing_measure` / `unit_pricing_base_measure` where required by country; `multipack`; `is_bundle` for kits |
| Dietary claims | Only accepted claim records project; certification expiry withdraws | Attributes where the channel defines them |
| Alcohol | Age-gating and warning blocks per market | Channel alcohol policies restrict listings; the dated rules live in CDS-900 |
| Storage and temperature class | Fulfilment metafields | Not published |
| Mandatory food information before purchase | Generated per-market information block on the product page (Appendix D) | — |

Which layer feeds each channel is declared per attribute (CDS200-R026); feed-channel requiredness by country is a dated CDS-900 platform fact.

## 17. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Ingredient extraction from labels or specifications | Ordered candidate list | Mandatory review (R012); order preserved |
| Allergen declaration proposals | Candidate `contains` records from ingredients | Mandatory review regardless of confidence (R016); never auto-accepted |
| Nutrition value extraction | Parsed table with scheme candidate | Mandatory review (R021); unit and rounding validation |
| Dietary claim candidates | Candidate claim records flagged "evidence required" | Never accepted without evidence (R024) |
| Origin and protected names | Candidates from specification documents | Verification of protected names (R037) |
| Market obligation gaps | Candidate list of register entries triggered | Register evaluation deterministic; AI never marks obligations satisfied |

## 18. Governance and Organisational Extensions *(informative — rules in CDS-1500 §23 and CDS-800)*

Organisations extend the allergen, storage and claim-type dictionaries under CDS-400 governance; regulated allergen lists change (Australia's 2024 required names, the US sesame addition) and are handled as governed dictionary migrations, never silent edits. The jurisdiction requirement register is reviewed on the cadence declared under CDS-800 §30, with a mandatory review whenever a market changes a mandatory particular.

## 19. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS1700-R046** An implementation claiming the CDS Food and Beverage Profile MUST: store ingredients as ordered structured lists with compound ingredients identifiable (R009–R011); store allergen declarations as structured records distinguishing "contains" from "may contain", bound to the governed allergen dictionary, with market required-name mapping and preflight evaluation (R013–R018); store nutrition values as numeric, unit-bearing values under a declared scheme with the bases the scheme requires (R019–R022); govern every dietary, nutrition-content and health claim as an evidence-bearing record with claim-driven facets (R023–R027); store net quantity, pack count, sale-unit hierarchy and variable-weight facts as typed values (R028–R032); store storage, date-mark type and shelf-life policy as governed values with lot dates kept out of canonical data (R033–R035); store origin and alcohol facts per market (R036–R041); maintain and evaluate a jurisdiction requirement register for every market published to (R003, CDS-1500 §2.2); apply category-specific requirements per CDS1500-R009; and publish and verify channel representations under CDS-500.

**CDS1700-R047** A Food and Beverage Profile claim MUST state which markets its register covers and whether alcoholic beverages and variable-weight products are in scope.

## 20. Worked Product Examples *(informative)*

### 20.1 Granola with tree nuts and a precautionary milk statement (Australia and EU)

```
CAT_product_type = breakfast_cereal
MF_ingredient_list = [rolled oats (55%), honey (12%), almonds (8%), sunflower oil, coconut, pepitas, cinnamon]
CMP_allergen_declarations =
  [{allergen: oats, declaration: contains, gluten: true, basis: ingredient},
   {allergen: almond, declaration: contains, basis: ingredient},
   {allergen: milk, declaration: may_contain, basis: shared_line}]
Market projections:
  AU (scheme au_fsanz_1_2_3_allergens): ingredient list with "oats", "almonds" in bold;
     summary statement "Contains: gluten, oats, almond"; precautionary line "May contain milk"
  EU (scheme eu_fic_1169_2011_annex_ii): "oats" and "almonds" emphasised; allergen group facets
     gluten_containing_cereals, tree_nuts; precautionary statement kept separate
MF_nutrition_values = {scheme: nip_au_nz, serving_size: 45 g, servings_per_package: 16.7,
                       per_100g: {energy_kj: 1850, protein_g: 9.1, fat_g: 18.2, saturated_g: 4.0,
                                  carbohydrate_g: 55.0, sugars_g: 14.2, sodium_mg: 12},
                       per_serving: {...}}
MF_dietary_claims = []                              # "gluten free" would fail R017 (oats contain gluten)
VAR_net_quantity = {value: 750, unit: gram}
CMP_origin_declarations = [{jurisdiction: AU, scheme: au_cool_2016, type: made_in_australia,
                            australian_ingredients_band: gte_90_percent, standard_mark: true}]
Preflight AU: allergens declared for every required allergen present -> pass
```

### 20.2 Craft gin (Australia, UK)

```
CAT_product_type = gin
MF_alcohol_by_volume = 42.0
MF_standard_drinks = {value: 23.3, scheme: au_nz_standard_drink_10g}      # 700 ml container
MF_alcohol_units = {value: 29.4, scheme: uk_unit_8g}
CMP_alcohol_warnings = [{jurisdiction: AU, scheme: au_fsanz_2_7_1_alcohol, statement: pregnancy_warning_mark,
                         size_class: "over 200 ml to 800 ml"}]
CMP_age_restriction = [{jurisdiction: AU, minimum_age: 18}, {jurisdiction: GB, minimum_age: 18}]
CMP_allergen_declarations = []                     # none; ingredient list not required >1.2% ABV in GB/EU
VAR_net_quantity = {value: 700, unit: millilitre}
CMP_dangerous_goods = {regulated: true, un_number: "UN3065", class: "3", packing_group: "III",
                       limited_quantity_eligible: true}                   # per CDS-1900 §12
Preflight AU: pregnancy warning present, age restriction enforceable on channel -> pass
```

### 20.3 Chilled catch-weight product

```
CAT_product_type = whole_chicken
MF_catch_weight = true
MF_pricing_basis = per_kilogram
MF_nominal_weight = {value: 1.6, unit: kilogram, tolerance: "±0.3"}
MF_temperature_class = chilled
MF_storage_condition = refrigerate
MF_date_mark_type = use_by
MF_minimum_remaining_shelf_life_days = 4
CMP_origin_declarations = [{jurisdiction: AU, scheme: au_cool_2016, type: grown_in_australia}]
Order-level observation: actual weight 1.52 kg -> price computed by the pricing authority, not the PIM
```

## 21. Reference Validation Cases *(informative — the profile's contribution to the cross-industry validation set, REVIEW-020)*

- a product whose ingredient list contains a required allergen with no declaration, which preflight must block per market (R018);
- a "gluten free" claim on a product with a `contains` declaration for a gluten cereal, which must fail (R017);
- a "may contain" statement that a channel projection must keep distinct from "contains" (R014);
- an allergen whose required name differs between Australia (individual tree nut) and the EU (nuts group), resolved by dictionary mapping (R015);
- a nutrition panel prepared for one scheme offered to a market with another scheme, which must not satisfy the requirement (R019);
- a flavour variant with its own ingredient list (R006);
- a "6 × 375 ml" multipack that must not collapse to "2.25 l" (R029);
- a catch-weight product presented as fixed weight (R031);
- a use-by product without a minimum-remaining-shelf-life policy (R035);
- an alcoholic beverage above threshold lacking the market's warning (R040);
- a case-level GTIN-14 that must validate and link to its each-level GTIN (R032);
- a hamper whose kit-level allergen summary must derive from components (R008).

---

## Appendix A. Food and Beverage Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_ingredient_list / MF_ingredient_order_basis | Product (variant per R006) | Ordered structured list; governed value | R for multi-ingredient foods; N/A for single-ingredient exempt foods |
| MF_characterising_ingredient_percentages | Product | Structured list | C — R where a market requires quantitative declaration |
| CMP_allergen_declarations / CMP_allergen_scheme | Product (variant per R006) | Structured records (`allergen` dictionary) | R |
| MF_nutrition_values | Product (variant per R006) | Structured object with declared scheme | R unless exempt in every target market |
| MF_front_of_pack_rating | Product | Structured (scheme, value) | C |
| MF_dietary_claims / MF_nutrition_content_claims / MF_health_claims / MF_certifications | Product | Structured records with evidence | C |
| VAR_net_quantity | Variant | Typed measurement | R |
| VAR_pack_count | Variant | Integer | C — R for multipacks |
| VAR_sale_unit_level / VAR_gtin | Variant and sale-unit levels | Governed level; identifier with scheme | R where trade identifiers exist |
| MF_catch_weight / MF_pricing_basis / MF_nominal_weight | Product/Variant | Boolean; governed value; typed measurement | R for variable-weight products |
| MF_storage_condition / MF_temperature_class | Product | Governed dictionary references | R |
| MF_date_mark_type / MF_shelf_life_days / MF_minimum_remaining_shelf_life_days | Product | Governed value; integers | R / REC / C (R for use-by products sold online) |
| CMP_country_of_origin / CMP_origin_declarations | Product | Governed country; per-market records | R where a market requires origin |
| MF_alcohol_by_volume / MF_standard_drinks / CMP_alcohol_warnings / CMP_age_restriction | Product/Variant | Typed values; statement records; per-market records | R for alcoholic beverages |
| MF_warning_statements | Product | Structured statement records | C — R where a market mandates a statement |
| CMP_responsible_person | Product (per market) | Governed record | R where a market requires the food business operator's name and address |
| CMP_dangerous_goods | Product/Variant | Declaration record per CDS-1900 §12 | C |
| CMP_market_registrations | Product (per market) | Governed records | C |

## Appendix B. Dictionary Bindings *(informative — becomes governed data on adoption per CDS1500-R011)*

| Dictionary key | Package chapter | Bound attribute(s) | Status at 0.8.0 |
|---|---|---|---|
| allergen | 17 (new) | CMP_allergen_declarations | Bound by this profile |
| allergen_facet | 17 (new) | Customer-facing allergen grouping; EU group mapping | Bound |
| dietary_claim_type | 17 (new) | MF_dietary_claims.type | Bound (claim-type registry; evidence-gated) |
| storage_condition | 17 (new) | MF_storage_condition | Bound |
| jurisdiction / regulatory_scheme | 19 (new) | CMP_* market records, claim and warning schemes | Bound via CDS-1500 §2.2 |
| dangerous_goods_class | 18 (new) | CMP_dangerous_goods | Bound via CDS-1900 §12 |

Deliberately not shipped: nutrient identifier lists per scheme (organisations adopt their regulator's nutrient set), country lists (ISO 3166 at adoption), protected geographical name registers, flavour vocabularies (open-ended), wine varietal and region lists (organisation- or registry-sourced).

## Appendix C. References *(informative; retrieved 2026-09-20 unless stated)*

| Ref | Source | Location | Use in this chapter |
|---|---|---|---|
| [F1] | FSANZ — Allergen labelling for food businesses (Standard 1.2.3, Schedule 9; PEAL from 25 February 2024); DAFF IFN 10-25 | foodstandards.gov.au/business/labelling/allergen-labelling; agriculture.gov.au | Required allergen names, bold and summary statement (§6, D-AU-1) |
| [F2] | FSANZ — Standard 1.2.8 Nutrition information requirements (compilation 2024-10-29); Food Standards Code compilation (March 2026) | legislation.gov.au/F2015L00395 | NIP content, per-serving and per-unit-quantity bases (§7, D-AU-2) |
| [F3] | FSANZ — Standard 1.2.7 Nutrition, health and related claims (compilation 2025-08-13); Schedule 4 | legislation.gov.au/F2015L00394 | General and high-level health claims, NPSC, dietary context statements (§8, D-AU-3) |
| [F4] | FSANZ — Standard 2.7.1 Labelling of alcoholic beverages (compilation 2025-08-13); Labelling of alcoholic beverages (2025-09-10) | legislation.gov.au/F2015L00469; foodstandards.gov.au | ABV statement, standard drinks, pregnancy warning label sizes (§12, D-AU-4) |
| [F5] | Country of Origin Food Labelling Information Standard 2016; business.gov.au guidance | legislation.gov.au/F2016L00528; business.gov.au | Standard mark, bar chart, kangaroo logo, origin statement (§11, D-AU-5) |
| [F6] | FSANZ — Call for information: Health Star Rating and NIP (Nov 2024) | consultations.foodstandards.gov.au | HSR voluntary status and 70% uptake target by 14 November 2025 (D-AU-6) |
| [F7] | Consumer Information Standards (Origin of Food) Regulations 2021 (NZ) | legislation.govt.nz/regulation/public/2021/0097 | NZ origin disclosure for regulated fresh and single-ingredient foods from 12 February 2022 (D-NZ-1) |
| [F8] | U.S. FDA — Food Labeling Guide; 21 CFR 101.3, 101.4, 101.5, 101.7, 101.9 (eCFR) | fda.gov; ecfr.gov | Identity, net quantity, ingredient order, Nutrition Facts, name and place of business (§5, §7, §9, D-US-1) |
| [F9] | U.S. FDA — Food Allergies; FALCPA; FASTER Act (sesame from 1 January 2023); Guidance Edition 5 (2025) | fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies | Nine major allergens, species and type naming, "Contains" statement (§6, D-US-2) |
| [F10] | EFSA — Food allergens (EU 14) (2025-04-22); Regulation (EU) No 1169/2011 Articles 9, 12, 14, 18, 21 (EUR-Lex; UK retained text) | efsa.europa.eu; eur-lex.europa.eu | EU mandatory particulars, distance-selling availability before purchase (§1, §6, D-EU-1) |
| [F11] | Regulation (EU) 2021/2117 (wine ingredient and nutrition labelling) | eur-lex.europa.eu | Wine sector labelling from 8 December 2023 (D-EU-2) |
| [F12] | Food Standards Agency (UK) — PPDS allergen labelling (Natasha's Law, 1 October 2021); Food allergen labelling technical guidance; Food Information Regulations 2014 (as at 2021-10-01) | food.gov.uk; legislation.gov.uk/uksi/2014/1855 | UK allergen rules, gluten-free 20 mg/kg, distance selling (D-UK-1) |
| [F13] | The Food (Promotion and Placement) (England) Regulations 2021; Food (Promotion and Presentation) (Wales) Regulations 2025 | legislation.gov.uk/uksi/2021/1368; legislation.gov.uk/wsi/2025/395 | HFSS online placement and volume price promotion restrictions (D-UK-2) |
| [F14] | Canadian Food Inspection Agency — Food labelling requirements checklist; Front-of-package nutrition symbol (compliance 1 January 2026); Health Canada FOP guide v3 | inspection.canada.ca; canada.ca | Bilingual labelling, NFt, priority allergens, FOP symbol (D-CA-1) |
| [F15] | Store Leads — Shopify Plus Statistics 2026 (updated 2026-09-11); global ecommerce revenue by segment (Statista Market Insights, March 2026, via secondary reporting) | storeleads.app; statista.com | Market basis (REVIEW-020) |

## Appendix D. Jurisdiction Requirement Register — Seed *(informative seed of the normative register defined in CDS-1500 §2.2)*

Conventions as in CDS-1600 Appendix D.

### D.1 Australia (AU)

#### D.1.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-1 | Australia New Zealand Food Standards Code, Standard 1.2.3 and Schedule 9 (allergen declarations) — FSANZ; enforced by state and territory agencies and DAFF for imports (`au_fsanz_1_2_3_allergens`) | Food for sale requiring a label (and unlabelled food via other means) | labelling_element | Required names: wheat, fish, crustacean, mollusc, egg, milk, lupin, peanut, soy, sesame, almond, Brazil nut, cashew, hazelnut, macadamia, pecan, pine nut, pistachio, walnut, barley/oats/rye when containing gluten, sulphites ≥10 mg/kg; declared in bold in the statement of ingredients and in a separate bold "Contains" summary statement in the same field of view; "gluten" listed with wheat and for gluten-containing cereals → CMP_allergen_declarations (scheme `au_fsanz_1_2_3_allergens`), projection rules | Food manufactured or produced from 25 February 2024 | Verified 2026-09-20 [F1] |
| D-AU-2 | Standard 1.2.8 Nutrition information requirements; Schedule 12 format (`au_fsanz_1_2_8_nip`) | Packaged food unless exempt (e.g. standardised alcoholic beverages, herbs, tea, single-ingredient produce, small packages) | labelling_element | Nutrition information panel: servings per package, serving size (g/ml), unit quantity (100 g/ml), energy (kJ, optionally kcal), protein, fat, saturated fat, carbohydrate, sugars (g), sodium (mg), plus any claimed nutrient; per serving and per 100 g/ml; ≤3 significant figures → MF_nutrition_values (scheme `nip_au_nz`) | Ongoing | Verified 2026-09-20 [F2] |
| D-AU-3 | Standard 1.2.7 Nutrition, health and related claims; Schedule 4 (permitted claims); Schedule 5 (NPSC) (`au_fsanz_1_2_7_claims`) | Foods bearing nutrition content or health claims | restricted_content | Health claims only where the food meets the nutrient profiling scoring criterion and the food–health relationship is in Schedule 4 (high level) or Schedule 4 / self-substantiated and notified (general level); dietary context statement; claims prohibited on kava, infant formula and most alcohol >1.15% → MF_health_claims, MF_nutrition_content_claims (scheme `au_fsanz_1_2_7_claims`) | Ongoing | Verified 2026-09-20 [F3] |
| D-AU-4 | Standard 2.7.1 Labelling of alcoholic beverages (`au_fsanz_2_7_1_alcohol`) | Beverages ≥0.5% ABV; food containing alcohol | labelling_element; warning_statement | Alcohol content as % ABV (or mL/100 mL) for >1.15%; "contains not more than X% alcohol by volume" for 0.5–1.15%; statement of approximate number of standard drinks (10 g ethanol) for >0.5%; pregnancy warning pictogram or mark for >1.15% with size classes by container volume (≤200 ml pictogram ≥8 mm; >200–800 ml mark ≥6 mm; >800 ml ≥9 mm; outer packs ≥11 mm); energy statement for prescribed beverages → MF_alcohol_by_volume, MF_standard_drinks (scheme `au_nz_standard_drink_10g`), CMP_alcohol_warnings | Pregnancy warning mandatory since 1 August 2023 | Verified 2026-09-20 [F4] |
| D-AU-5 | Country of Origin Food Labelling Information Standard 2016 — ACCC (`au_cool_2016`) | Food sold in Australia (priority and non-priority foods; imported foods) | labelling_element | Standard mark (kangaroo logo where grown, produced or made in Australia; bar chart with percentage of Australian ingredients; explanatory text; box) for priority foods grown, produced, made or packed in Australia; country of origin statement ("Made in X", "Product of X") for non-priority and imported foods, boxed for packaged priority foods → CMP_origin_declarations (scheme `au_cool_2016`, declaration type, ingredient band, mark eligibility) | Ongoing | Verified 2026-09-20 [F5] |
| D-AU-6 | Health Star Rating system (voluntary front-of-pack) — Food ministers/FSANZ (`au_health_star_rating`) | Packaged foods | rating_label (voluntary) | HSR value and calculator version where displayed; ministers set a 70% uptake target by 14 November 2025 with mandating under consideration → MF_front_of_pack_rating (scheme `au_health_star_rating`) | Voluntary; review 2026 | Verified 2026-09-20 [F6] |

#### D.1.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-7 | Standards 1.2.4 (statement of ingredients), 1.2.5 (date marking), 1.2.6 (directions for use and storage), 1.2.10 (characterising ingredients) | Food requiring a label | labelling_element | Ingredients in descending ingoing weight; best-before / use-by regime; storage directions; characterising ingredient percentages → MF_ingredient_list, MF_date_mark_type, MF_storage_instructions, MF_characterising_ingredient_percentages | Ongoing | Retrieved 2026-09-20 (Code compilation index; standard texts not read in full) |
| D-AU-8 | Unit Pricing Code (Competition and Consumer (Industry Codes—Unit Pricing) Regulations) — ACCC (`au_unit_pricing_code`) | Grocery retailers above the floor-area threshold and online grocery retailers | listing_element | Unit price per prescribed unit of measure displayed with the selling price online → derived per R030 | Ongoing | Retrieved (not spot-verified) |

### D.2 New Zealand (NZ)

#### D.2.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-1 | Australia New Zealand Food Standards Code (joint standards 1.2.3, 1.2.7, 1.2.8, 2.7.1 apply in NZ) — MPI | Food for sale in NZ | as D-AU-1 to D-AU-4 | Same data elements as the joint standards; Standard 1.2.10 (characterising ingredients) is Australia-only; country of origin under the Code does not apply in NZ → CMP_allergen_scheme, MF_nutrition_values, CMP_alcohol_warnings as for AU | Ongoing | Verified 2026-09-20 [F2] (Code compilation notes application) |
| D-NZ-2 | Consumer Information Standards (Origin of Food) Regulations 2021 — MBIE/Commerce Commission (`nz_origin_of_food_2021`) | Regulated single-ingredient fresh or thawed fruit, vegetables, meat, fish and seafood (and certain frozen items) | listing_element; labelling_element | Origin information disclosed when the item is supplied, offered or advertised for sale, including online; replacement statements where origin changes often → CMP_origin_declarations (scheme `nz_origin_of_food_2021`) | From 12 February 2022 (frozen items later per the regulations) | Verified 2026-09-20 [F7] |

#### D.2.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

*None.*

### D.3 United States (US)

#### D.3.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-1 | FD&C Act; Fair Packaging and Labeling Act; 21 CFR part 101 — FDA (`us_fda_food_labeling_21cfr101`) | Packaged food under FDA jurisdiction (USDA regulates meat, poultry and egg products) | labelling_element | Statement of identity and net quantity on the principal display panel (weight, measure or count; fluid measure for liquids); ingredient statement by common or usual name in descending order of predominance by weight (≤2% grouping permitted); name and place of business ("Manufactured for"/"Distributed by" qualifiers); Nutrition Facts per 21 CFR 101.9 (serving size in household measure plus metric, servings per container, calories, mandatory nutrients incl. added sugars, vitamin D, calcium, iron, potassium, %DV, dual-column rules) → VAR_net_quantity, MF_ingredient_list, CMP_responsible_person, MF_nutrition_values (scheme `us_nutrition_facts`) | Nutrition Facts compliance since 2020/2021 | Verified 2026-09-20 [F8] |
| D-US-2 | FALCPA 2004 and FASTER Act 2021 (FD&C Act s. 403(w)) — FDA (`us_falcpa_faster`) | FDA-regulated packaged foods and dietary supplements | labelling_element | Nine major allergens (milk, egg, fish, crustacean shellfish, tree nuts, peanuts, wheat, soybeans, sesame) declared by food source in the ingredient list or in a "Contains" statement immediately after it; type of tree nut, species of fish and crustacean named → CMP_allergen_declarations (scheme `us_falcpa_faster`), projection rules | Sesame effective 1 January 2023 | Verified 2026-09-20 [F9] |
| D-US-6 | Proposition 65 (California) — OEHHA (`us_ca_prop65_warning`) | Foods causing exposure to listed chemicals sold to California consumers | warning_statement; listing_element | Food-specific short-form or full warning (no triangle symbol required for food; food web address); internet warning before purchase → MF_warning_statements (jurisdiction US-CA) | Amended regulations effective 1 January 2025 | Verified 2026-09-20 (CDS-1600 [B14]) |

#### D.3.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-3 | FDA gluten-free labeling rule (21 CFR 101.91) (`us_fda_gluten_free`) | Foods labelled "gluten-free" | restricted_content | Claim permitted only where gluten is below 20 ppm and no gluten-containing grain ingredient is used unless processed to remove gluten → MF_dietary_claims (type `gluten_free`, threshold 20 ppm) | Ongoing | Retrieved (not spot-verified) |
| D-US-4 | USDA National Organic Program (7 CFR part 205) (`us_usda_nop_organic`) | Foods labelled organic | restricted_content; documentation | "100% organic", "organic" (≥95%), "made with organic" categories; certifier named on the information panel → MF_dietary_claims (type `organic`), MF_certifications | Ongoing | Retrieved (not spot-verified) |
| D-US-5 | Federal Alcohol Administration Act; 27 CFR parts 4, 5, 7 and 16 — TTB (`us_ttb_alcohol_labeling`) | Wine, distilled spirits, malt beverages | labelling_element; warning_statement; pre_market (COLA) | Brand name, class or type, alcohol content, net contents, name and address, country of origin for imports, sulfite declaration ≥10 ppm, Government Warning statement; certificate of label approval before sale in interstate commerce → MF_alcohol_by_volume, VAR_net_quantity, CMP_alcohol_warnings (scheme `us_ttb_alcohol_labeling`), CMP_market_registrations (COLA) | Ongoing | Retrieved (not spot-verified) |

### D.4 European Union (EU)

#### D.4.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-1 | Regulation (EU) No 1169/2011 on food information to consumers (FIC), Articles 9, 12, 14, 16, 18, 21, 30 and Annexes II–V — European Commission and member states (`eu_fic_1169_2011`) | Prepacked food; distance selling of prepacked and non-prepacked food | labelling_element; listing_element | Mandatory particulars: name of the food; list of ingredients (descending by weight as recorded at use); allergens (Annex II: 14 groups) emphasised in the ingredient list; quantity of certain ingredients (QUID); net quantity; date of minimum durability or use-by date; special storage conditions or conditions of use; name or business name and address of the food business operator; country of origin or place of provenance where required; instructions for use where needed; actual alcoholic strength for beverages >1.2% ABV; nutrition declaration (energy, fat, saturates, carbohydrate, sugars, protein, salt per 100 g/ml; exemptions in Annex V; not mandatory for >1.2% ABV). Distance selling (Article 14): all mandatory information except the date mark must be available before the purchase is concluded on the material supporting the sale, free of charge; all particulars at delivery → MF_ingredient_list, CMP_allergen_declarations (scheme `eu_fic_1169_2011_annex_ii`), MF_characterising_ingredient_percentages, VAR_net_quantity, MF_date_mark_type, MF_storage_instructions, CMP_responsible_person, CMP_origin_declarations, MF_alcohol_by_volume, MF_nutrition_values (scheme `eu_nutrition_declaration`); preflight rule R003 | Ongoing | Verified 2026-09-20 [F10] |
| D-EU-2 | Regulation (EU) 2021/2117 amending Regulation (EU) No 1308/2013 (wine) and (EU) No 251/2014 (aromatised wine) (`eu_wine_labelling_2021_2117`) | Wine and aromatised wine products | labelling_element | Nutrition declaration and list of ingredients compulsory; energy value may be on-label with full declaration and ingredients provided electronically (no tracking or marketing); allergens remain on the label; de-alcoholised products <10% ABV carry a date of minimum durability → MF_nutrition_values, MF_ingredient_list, CMP_allergen_declarations, electronic-label link record | Applies to wine produced from 8 December 2023 (existing stocks may be sold through) | Verified 2026-09-20 [F11] |

#### D.4.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-3 | Regulation (EC) No 1924/2006 nutrition and health claims (`eu_claims_1924_2006`); Commission Implementing Regulation (EU) No 828/2014 (gluten) (`eu_gluten_828_2014`) | Foods bearing claims | restricted_content | Only authorised health claims and defined nutrition claims; "gluten-free" ≤20 mg/kg, "very low gluten" ≤100 mg/kg → MF_health_claims, MF_nutrition_content_claims, MF_dietary_claims | Ongoing | Verified in part 2026-09-20 [F12] (gluten thresholds via FSA); claims regulation retrieved |
| D-EU-4 | Regulation (EU) 2018/848 organic production and labelling (`eu_organic_2018_848`) | Foods labelled organic | restricted_content; documentation | EU organic logo conditions, code number of the control body, origin statement → MF_dietary_claims (type `organic`), MF_certifications | Ongoing | Retrieved (not spot-verified) |

### D.5 United Kingdom (GB)

#### D.5.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-1 | Assimilated Regulation (EU) No 1169/2011 and the Food Information Regulations 2014 (England; Wales and NI equivalents; Scotland separate) — FSA/FSS and local authorities (`uk_fir_2014`) | Prepacked, non-prepacked and prepacked-for-direct-sale (PPDS) food; distance selling | labelling_element; listing_element | Same mandatory particulars as D-EU-1 (assimilated); 14 allergens emphasised; PPDS food must carry the name and a full ingredients list with allergens emphasised (from 1 October 2021); distance selling: mandatory allergen information available before purchase and at delivery; gluten-free ≤20 mg/kg; alcohol >1.2% ABV exempt from ingredient list but allergens must be declared → as D-EU-1 with scheme `uk_fir_2014` | PPDS from 1 October 2021 | Verified 2026-09-20 [F12] |
| D-UK-2 | The Food (Promotion and Placement) (England) Regulations 2021; Food (Promotion and Presentation) (Wales) Regulations 2025 — DHSC/Welsh Government (`uk_hfss_promotion_placement`) | Qualifying businesses (50+ employees) offering specified less-healthy (HFSS) prepacked food online | listing_element (placement); restricted_content (promotions) | Specified food must not be offered on the online home page, in non-related browsing or search results (with exceptions), on pop-ups, favourites (except previously bought), or checkout pages; volume price promotions (multibuys, extra free) prohibited; nutrient profiling score determines "specified food" → MF_hfss_classification (jurisdiction GB), channel placement rules | Placement restrictions since October 2022; England volume-price promotion restrictions from 1 October 2025; Wales regulations 2025 | Verified 2026-09-20 [F13] |

#### D.5.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-3 | Alcohol labelling (assimilated FIC Article 16; Weights and Measures; voluntary UK unit guidance) (`uk_alcohol_labelling`) | Alcoholic beverages | labelling_element | ABV >1.2%; units (8 g ethanol) and pregnancy logo are voluntary industry practice → MF_alcohol_by_volume, MF_alcohol_units (scheme `uk_unit_8g`) | Ongoing | Retrieved (not spot-verified) |

### D.6 Canada (CA)

#### D.6.1 Verified seed entries *(adoptable into the operative register under CDS1500-R060)*

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-CA-1 | Food and Drugs Act and Regulations; Safe Food for Canadians Act and Regulations; Consumer Packaging and Labelling — CFIA and Health Canada (`ca_fdr_food_labelling`) | Prepackaged food sold in Canada | labelling_element | Common name; net quantity in metric; list of ingredients with priority allergens, gluten sources and added sulphites declared by prescribed source names in the list or a "Contains" statement, with cross-contamination statements permitted; Nutrition Facts table (serving size in household measure and metric, energy and 12 core nutrients, %DV, format families, small-package exemptions); bilingual English and French for mandatory information (dealer name and address may be in one language); country of origin declaration "Product of [country]" where required; date marking and storage → MF_ingredient_list, CMP_allergen_declarations (scheme `ca_fdr_priority_allergens`), MF_nutrition_values (scheme `ca_nutrition_facts_table`), VAR_net_quantity, CMP_origin_declarations, localisation dimension per CDS-300 §18 | Ongoing | Verified 2026-09-20 [F14] |
| D-CA-2 | Food and Drug Regulations B.01.350–B.01.354 (front-of-package nutrition symbol) — Health Canada/CFIA (`ca_fop_nutrition_symbol`) | Prepackaged foods at or above thresholds of saturated fat, sugars or sodium (≥15% DV default; ≥10% for reference amounts ≤30 g/ml; ≥30% for main dishes), with exemptions and prohibitions | rating_label | Nutrition symbol on the principal display panel in prescribed bilingual format; multipack and assortment rules → MF_front_of_pack_rating (scheme `ca_fop_nutrition_symbol`) | Compliance from 1 January 2026, no enforcement discretion | Verified 2026-09-20 [F14] |

#### D.6.2 Research candidates *(non-normative; excluded from the operative register until verified against the primary instrument, CDS1500-R086)*

*None.*

### D.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Japan (JP), China (CN), Singapore (SG), Republic of Korea (KR), India (IN), Brazil (BR) and others | Not seeded | China's GB 7718 labelling standard and Japan's Food Labeling Act differ materially (allergen lists, nutrition bases, language); the organisation extends the register with local advice before publishing food to those markets. |

END OF CDS-1700 v0.3 REVIEW DRAFT
