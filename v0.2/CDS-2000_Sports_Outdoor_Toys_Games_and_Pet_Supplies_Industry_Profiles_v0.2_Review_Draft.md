# Commerce Data Standard (CDS)
## CDS-2000 — Sports and Outdoor, Toys and Games, and Pet Supplies Industry Profiles

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5); chapter added in the 2026-09-20 industry-profile expansion |
| Date | 2026-09-20 |
| Supersedes | Nothing — first edition. The Chapter 12 (Sports & Outdoor), Chapter 13 (Toys & Games) and Chapter 14 (Pet Supplies) dictionary vocabularies were shipped ahead of these profiles and are bound here for the first time; pet food forms are added in package 0.8.0. |
| Normative status | §1, §3, §5–§8, §13 and Appendix A are normative. §2 (pointer), §4, §9–§12, §14, §15 and Appendices B–D are informative; Appendix D seeds the jurisdiction requirement register whose record structure and obligations are normative in CDS-1500 §2.2. Every table is individually marked. |
| Primary audience | Sports, outdoor, toy and pet merchandisers, product-safety and compliance owners, data stewards, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1500, especially CDS-200, CDS-300, CDS-400, CDS-500, CDS-600, CDS-700, CDS-900, CDS-1100, CDS-1500 (profile model, requirement levels, profile register, jurisdiction requirement register, apparel size and colour rules), CDS-1600 (claims, ingredients and restricted-sale patterns), CDS-1700 (ingredient, nutrition and net-quantity patterns), CDS-1800 (technical specifications, batteries), CDS-1900 (relationships, kits, dangerous goods) |
| Companion package | CDS Reference Dictionary: Chapters 12, 13, 14, 5 (size systems), 19 (Jurisdictions & Regulatory Schemes) |
| Profile identifiers | `cds.profile.sports_outdoor.v0_2`, `cds.profile.toys_games.v0_2`, `cds.profile.pets.v0_2` (registered in CDS-1500 §2.1) |
| Research basis | REVIEW-020 (global commerce vertical market research, 2026-09-20): sports, toys and hobbies, and pet supplies are each mid-sized worldwide store populations (roughly 2–6% of Shopify Plus stores each) with above-average catalogue depth (sports stores average more than 1,200 products) and, for toys, the densest product-safety regulation of any consumer vertical. They are grouped in one chapter because they share three mechanisms — activity or audience targeting, safety-driven age and warning data, and technical attributes inherited from other profiles — rather than because they share a market. |

Terminology follows CDS-100. Attribute requirement levels (R, C, REC, O, N/A) are those of CDS-1500 §4 and are not restated here. Each of the three profiles in this chapter is claimed independently (§13).

---

## 1. Purpose and Scope *(normative)*

CDS-2000 defines three industry profiles: **Sports and Outdoor** (equipment, activewear and footwear where sold by activity, camping and outdoor gear, cycling, water sports, fitness), **Toys and Games** (toys, games, puzzles, hobby kits, ride-ons, children's play equipment) and **Pet Supplies** (pet food and treats, accessories, habitats, grooming, health products). Apparel and footwear sold in these verticals apply CDS-1500 for size, colour and composition; electronic and battery-powered goods apply CDS-1800; kits, compatibility and dangerous goods apply CDS-1900; ingredients and nutrition apply CDS-1700 patterns; claims apply CDS-1600 §11.

What distinguishes these verticals is who or what the product is for and what it is for: a sport or activity, a child's age and developmental stage, an animal's species, life stage and size. Those targeting attributes drive navigation ("shop by sport", "shop by age", "shop by pet") and, for toys and pet food, they are also regulated facts (age warnings, nutritional adequacy) that must be kept separate from the merchandising attributes that resemble them.

**CDS2000-R001** An implementation claiming any profile in this chapter MUST represent the targeting attributes of that profile (activity, age band, pet type, life stage, pet size) as governed dictionary values, never as tags or free text, and MUST keep merchandising targeting distinct from regulated safety or adequacy statements (§6, §7).

**CDS2000-R002** An implementation claiming any profile in this chapter MUST apply CDS-1500, CDS-1800 and CDS-1900 for the apparel, technical and relationship layers of its products where those layers are present, without claiming those profiles.

**CDS2000-R003** An implementation MUST maintain a jurisdiction requirement register (CDS-1500 §2.2) for every market it publishes toys, children's products, protective equipment, pet food or pet health products to, and publication preflight for a market MUST evaluate the market's obligations before the offer is made available.

**CDS2000-R004** These profiles MUST NOT weaken any rule of CDS-1500 that they reuse; where this chapter is silent, CDS-1500 and the core chapters govern.

## 2. Profile Model *(informative pointer)*

The three profiles apply the industry profile model of CDS-1500 §2, the requirement levels of CDS-1500 §4 and the jurisdiction requirement register of CDS-1500 §2.2 without restatement. Their identifiers and dictionary bindings are in CDS-1500 §2.1; their seeded jurisdiction entries are in Appendix D.

## 3. Shared Product Model *(normative)*

Products in these verticals follow the standard product and variant model. Variant options are typically size (apparel and footwear sizes under CDS-1500 §9; equipment sizes under a declared size system), colour, pack or bag size (pet food), and configuration (piece count, player count edition). Targeting attributes are product-scope descriptive attributes, never variant options.

```
Product: Adult cycling helmet, model Ridge            (informative example)
  Product scope:
    CAT_product_type = bicycle_helmet
    MF_sport_activity = [cycling, mountain_biking]     # sport_activities dictionary
    MF_certifications = [{scheme: as_nzs_2063, evidence: E1}, {scheme: cpsc_16_cfr_1203, evidence: E1}]
    MF_size_system = head_circumference_cm             # size_systems dictionary (0.8.0)
    MF_weight_g = 310
  Variant scope:
    VAR_size_label = "M (55-59 cm)"; VAR_size_min = 55; VAR_size_max = 59
    VAR_colour = matte_black
```

**CDS2000-R005** Sport or activity, age band, play type, pet type, life stage and pet size MUST be product-scope governed attributes; where a product genuinely serves several values (a multi-sport shoe, a toy for two age bands, a food for dogs and cats) the attribute MUST be multi-valued with a declared maximum (the CDS-1500 §10 pattern), not duplicated products.

**CDS2000-R006** Equipment sizes (helmets, frames, boards, wetsuits, harnesses, pet collars and coats) MUST identify their size system (the CDS1500-R026 pattern) and MUST store measured bounds (head circumference, frame size, chest or neck girth, pet weight range) as typed measurements where the size is defined by a measurement, so that size guides and facets derive from data.

**CDS2000-R007** Kits, sets and bundles (a tent with footprint, a game with expansion, a starter aquarium) MUST follow CDS-1900 §11; batteries and rechargeable products MUST follow CDS-1800 §8 and CDS-1900 §12.

**CDS2000-R008** Included and required-but-not-included items (batteries, balls, mounting hardware, food bowls) MUST be `includes` and `requires` relationship records (CDS-1900 §5) so that "batteries not included" and similar statements derive from data.

## 4. Product Families and Category Profiles *(informative baseline; the inheritance rule of CDS1500-R016 applies)*

| Profile | Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|---|
| Sports & Outdoor | Activewear and sports footwear | CDS-1500 apparel or footwear baseline; sport activity | performance attributes with basis qualifiers; weather suitability | size, colour |
| Sports & Outdoor | Cycling (bikes, components) | brand; MPN; frame size system and size; wheel size; compatibility records (CDS-1900 §5); weight | groupset, gearing, geometry as typed values; e-bike battery and motor per CDS-1800 | frame size, colour |
| Sports & Outdoor | Water sports (surf, swim, paddle) | sport activity; wetsuit style, thickness, zip entry and seam (wetsuits); board dimensions and volume | fin system as relationship; buoyancy certification (PFDs) | size, colour |
| Sports & Outdoor | Camping and outdoor gear | capacity (persons, litres); packed and assembled dimensions; weight; season or temperature rating with basis | materials; waterproof rating with scheme; fuel type (stoves) with dangerous goods per CDS-1900 §12 | size, colour |
| Sports & Outdoor | Fitness equipment | dimensions; weight; user weight limit; power source (if powered) | assembly type; connectivity per CDS-1800 | weight/resistance level |
| Sports & Outdoor | Protective equipment (helmets, guards, eyewear) | size system and size; certification records per market; sport activity | replacement date guidance; lens category (sunglasses) | size, colour |
| Toys & Games | Toys (0–12 years) | retail age band; play type; safety age warning where applicable; piece count; battery facts; compliance records per market | material; dimensions; educational themes as governed values | colour |
| Toys & Games | Games and puzzles | player count (min, max); recommended age; play time; piece count; language | complexity or difficulty as governed value | edition, language |
| Toys & Games | Hobby kits and models | scale; skill level as governed value; included and required items; paint or adhesive dangerous goods | assembled dimensions | — |
| Toys & Games | Ride-ons and outdoor play | age band and weight limit; dimensions; assembly type; compliance records; battery facts for powered ride-ons | — | colour |
| Pet Supplies | Pet food and treats | pet type; life stage; pet size where formulated by size; food form; ingredient list; typical or guaranteed analysis; nutritional adequacy statement and scheme; net quantity; feeding guide reference | breed size; dietary claims with evidence; storage condition | bag size, flavour |
| Pet Supplies | Pet health and supplements | pet type; active ingredients; registration per market; restricted sale status; dosage form | — | pack size |
| Pet Supplies | Accessories (collars, leads, beds, apparel) | pet type; size system and measured bounds; material | colour facet; washable status | size, colour |
| Pet Supplies | Habitats and equipment (aquariums, cages, feeders) | pet type; dimensions and capacity; power source where powered (CDS-1800) | compatibility records for consumables (filters, cartridges) | size |

## 5. Sports and Outdoor Profile *(normative; dictionary bindings informative)*

| Field | Meaning | Dictionary / type |
|---|---|---|
| MF_sport_activity | Activities the product is designed for | `sport_activity` (Chapter 12), multi-valued with declared maximum |
| MF_wetsuit_style / MF_wetsuit_thickness / MF_wetsuit_zip / MF_wetsuit_seam | Wetsuit construction | Chapter 12 dictionaries |
| MF_size_system + VAR_size_label + measured bounds | Equipment sizing | `size_system` (Chapter 5, incl. `bike_frame_cm`, `head_circumference_cm` at 0.8.0) |
| MF_temperature_rating / MF_season_rating / MF_waterproof_rating | Performance ratings | Typed values with scheme and basis qualifier (CDS-1800 R017 pattern) |
| MF_user_weight_limit_kg / MF_capacity_persons / MF_capacity_l | Limits and capacities | Typed measurements |
| MF_certifications | Safety and performance certifications (helmet, PFD, eyewear, climbing standards) | Certification records with scheme and evidence (CDS-1600 §11 pattern) |
| Relationship records | Compatibility (components, fin systems, mounts), included items | CDS-1900 §5 |

**CDS2000-R009** Sport or activity MUST be a governed multi-valued attribute bound to the `sport_activity` dictionary (or its governed extension) and MUST NOT be derived from category placement alone; the "shop by sport" facet is a projection of this attribute (CDS-600).

**CDS2000-R010** Performance ratings (temperature or season rating, waterproof or breathability rating, buoyancy, load rating) MUST be typed values carrying the rating scheme and a basis qualifier (manufacturer-rated or measured under a named standard); ratings with different schemes MUST NOT be compared or filtered as equivalent.

**CDS2000-R011** Protective equipment (helmets, personal flotation devices, eye protection, climbing and fall-protection equipment) MUST carry certification records naming the standard and the evidence for each market it is sold to; a certification MUST NOT be projected as a facet or claim unless fed by an accepted record, and a market that mandates the certification (Appendix D) MUST block publication when the record is absent.

**CDS2000-R012** Wetsuit style, thickness, zip entry and seam construction MUST be governed values bound to the Chapter 12 dictionaries where those facets are exposed; thickness MUST be stored as the governed thickness value with its millimetre components, not as free text.

**CDS2000-R013** Cycling and other component-based equipment MUST express component compatibility (frame, wheel size, drivetrain, mount standards) through relationship records or governed standard values per CDS-1900 §5 and §7; "fits most bikes" MUST be an explicit universal-fit declaration within a governed scope (CDS1900-R018).

**CDS2000-R014** Powered sports equipment (e-bikes, e-scooters, electric surfboards, fitness machines) MUST apply CDS-1800 §8 and §12 for battery, energy and compliance facts, and CDS-1900 §12 for transport declarations.

**CDS2000-R015** Skill level, intended use environment and performance tier, where exposed, MUST be governed organisation dictionaries (the package deliberately ships none because they are not comparable across brands); they MUST NOT be projected as claims.

**CDS2000-R016** Fuel, gas cartridges, bear spray, marine flares and similar outdoor consumables MUST carry dangerous-goods declarations per CDS-1900 §12 and restricted-sale flags where a market restricts them.

**CDS2000-R017** Apparel and footwear sold under this profile MUST satisfy the CDS-1500 apparel or footwear baseline; this profile adds activity and performance attributes and does not replace them.

## 6. Toys and Games Profile *(normative; dictionary bindings informative)*

The profile separates three age facts that are routinely conflated: the **retail age band** (a merchandising recommendation), the **manufacturer's recommended age** (a product fact from the maker), and the **safety age warning** (a regulated statement such as "Not suitable for children under 36 months" with its hazard, required by law in most markets and, in several, required to be visible online before purchase).

| Field | Meaning | Dictionary / type |
|---|---|---|
| MF_age_band | Retail age band for navigation | `toy_age_range` (Chapter 13), multi-valued with declared maximum |
| MF_recommended_age_min_months / MF_recommended_age_max_months | Manufacturer's recommended age | Integers (months) |
| MF_safety_age_warning | Regulated age warning with hazard statement and scheme | Structured statement record (MF_warning_statements) |
| MF_play_type | Play type | `play_type` (Chapter 13) |
| MF_piece_count | Number of pieces or parts | Integer |
| MF_player_count_min / MF_player_count_max / MF_play_time_min / MF_play_time_max | Game facts | Integers |
| MF_language | Language content of games and books | Governed language codes (CDS-300 §18) |
| MF_small_parts / MF_contains_magnets / MF_contains_button_batteries / MF_projectile / MF_cord_length_mm | Hazard-relevant facts driving warnings | Booleans and typed measurements |
| Battery fields | Per CDS-1800 §8 | — |
| CMP_compliance_declarations / CMP_responsible_person / CMP_product_identifier | Per-market compliance (toy safety marking, children's product certificate, tracking label, importer identity) | Governed records (CDS-1800 §12 pattern) |
| MF_weight_limit_kg | User weight limit for ride-ons and play equipment | Typed measurement |

**CDS2000-R018** Retail age band, manufacturer's recommended age and safety age warning MUST be three separate attributes; a safety age warning MUST NOT be derived from the retail age band or the manufacturer's recommendation, and the retail age band MUST NOT contradict a safety age warning (a product warned as unsuitable under 36 months MUST NOT carry the 0–2 years band).

**CDS2000-R019** Safety age warnings and hazard warnings (small parts, magnets, cords, projectiles, balloons, small balls, button batteries) MUST be structured statement records with the applicable scheme per market, derived from hazard-relevant facts under governed rules with human review, and MUST be projected to a market's listing where the market requires the warning to be visible before purchase (Appendix D); their presence MUST be verified under CDS-500.

**CDS2000-R020** Hazard-relevant facts (small parts present, magnets, button or coin batteries, projectiles, cords, sharp points or edges) MUST be explicit boolean or typed declarations with provenance, never inferred from category by rules or AI; an unknown value MUST be quarantined, not defaulted to false.

**CDS2000-R021** Play type and age band MUST be governed values bound to the Chapter 13 dictionaries (or governed extensions); "educational" and developmental-benefit statements are claims under CDS-1600 §11 pattern rules and MUST NOT be facets unless fed by accepted records.

**CDS2000-R022** Game facts (player count, play time, recommended age, language, edition) MUST be typed attributes; player count MUST be a bounded range with integer minimum and maximum (CDS1500-R041 pattern).

**CDS2000-R023** Per-market toy-safety compliance (conformity marking, declaration or certificate of conformity, third-party test reports, tracking or batch labels, importer or responsible-person identity) MUST be governed compliance records (CDS-1800 §12 pattern) and MUST be evaluated at preflight for each market; a conformity mark visible in an image MUST NOT be treated as the compliance fact.

**CDS2000-R024** Products with batteries MUST satisfy CDS-1800 §8 and CDS-1900 §12; products containing button or coin batteries MUST additionally carry the market-mandated warnings (R019) and secure-compartment compliance evidence where required.

**CDS2000-R025** Piece count MUST be an integer; where a product's piece count varies by variant (edition, size), it MUST be variant-scoped.

**CDS2000-R026** Licensed character and franchise properties MUST be governed values in an organisation dictionary distinct from brand, so that licence-based facets and expiry are governable; they MUST NOT be stored as tags.

**CDS2000-R027** Toys that are also apparel (dress-ups), electronics (children's tablets) or sports equipment (junior bikes) MUST satisfy the applicable layers of CDS-1500, CDS-1800 or §5 in addition to this profile.

## 7. Pet Supplies Profile *(normative; dictionary bindings informative)*

| Field | Meaning | Dictionary / type |
|---|---|---|
| MF_pet_type | Species the product is for | `pet_type` (Chapter 14), multi-valued with declared maximum |
| MF_pet_life_stage | Life stage the product is formulated or designed for | `pet_life_stage` (Chapter 14) |
| MF_pet_size | Size class where formulated or designed by size | `pet_size` (Chapter 14) with measured bounds (weight range) |
| MF_breed_suitability | Breed or breed-size targeting | Governed organisation dictionary (the package ships none) |
| MF_pet_food_form | Food form (dry kibble, wet, raw, freeze-dried, treats, …) | `pet_food_form` (Chapter 14, new at 0.8.0) |
| MF_ingredient_list / MF_ingredient_naming_scheme | Ordered ingredients | CDS-1700 §5 pattern |
| MF_nutrition_values | Typical or guaranteed analysis | CDS-1700 R019 with scheme `typical_analysis_pet_food` or `guaranteed_analysis_pet_food` |
| MF_nutritional_adequacy | Adequacy statement, scheme and life stage (complete and balanced / complementary / treat) | Structured record with scheme (AAFCO, FEDIAF, AS 5812 or market scheme) and evidence |
| MF_feeding_guide | Feeding directions | Structured table or document reference |
| VAR_net_quantity | Net weight or volume | CDS-1700 §9 pattern |
| MF_storage_condition / MF_date_mark_type | Storage and date marking | CDS-1700 §10 pattern |
| CMP_market_registrations / CMP_restricted_sale | Registration and restricted-sale status for veterinary medicines, parasiticides and supplements | CDS-1600 §12 and §14 patterns |
| MF_active_ingredients / MF_dosage_form / MF_dosage_by_weight | Health-product facts | CDS-1600 §14 pattern |

**CDS2000-R028** Pet type MUST be a governed multi-valued attribute bound to the `pet_type` dictionary (or its governed extension) and MUST be present for every pet product; life stage and pet size MUST be governed values where the product is formulated or designed by them.

**CDS2000-R029** Pet size classes MUST carry measured bounds (the weight range each class covers, as declared by the organisation or the manufacturer) so that "medium dog" is comparable across brands only where bounds match; a size class without bounds MUST NOT feed a numeric filter.

**CDS2000-R030** Pet food ingredients MUST be stored as ordered structured lists per CDS-1700 §5 (naming scheme declared; composite ingredients expanded where the market requires); "grain-free", "single-protein" and similar dietary statements are claims requiring evidence under CDS-1700 §8 pattern rules.

**CDS2000-R031** Typical or guaranteed analysis MUST be stored as typed nutrition values with the analysis scheme and basis (as-fed or dry-matter) per CDS-1700 R019, never as text; a channel that displays the analysis MUST receive it from the record.

**CDS2000-R032** Nutritional adequacy MUST be a structured record naming the scheme (a feeding-trial or nutrient-profile standard), the life stage it applies to and whether the product is complete and balanced, complementary or a treat; the statement MUST NOT be inferred from ingredients or from the merchandising life stage, and a market requiring the statement (Appendix D) MUST block publication when it is absent.

**CDS2000-R033** Food form MUST be a governed value bound to the `pet_food_form` dictionary; net quantity, unit pricing and pack counts follow CDS-1700 §9.

**CDS2000-R034** Pet health products (veterinary medicines, parasiticides, supplements, prescription diets) MUST carry per-market registration and restricted-sale records under the CDS-1600 §12 and §14 patterns; a product restricted to veterinary prescription or authorised sellers in a market MUST be blocked from channels in that market that cannot enforce the restriction.

**CDS2000-R035** Accessories designed by size (collars, harnesses, coats, crates, beds) MUST declare the size system and measured bounds (neck or chest girth, pet weight, crate internal dimensions) per R006.

**CDS2000-R036** Live animals, live feeder insects and live plants for aquaria MUST NOT be modelled under this profile without an organisation extension declaring the welfare, biosecurity and carriage rules that apply; the package ships no live-animal vocabulary.

**CDS2000-R037** Consumable compatibility (filter cartridges for a filter model, litter for a system, replacement parts for feeders) MUST be `compatible_with`, `accessory_for` or `fits` relationship records per CDS-1900 §5.

## 8. Warnings, Restricted Sale and Recalls *(normative)*

**CDS2000-R038** All mandatory warnings under the three profiles MUST be structured statement records (`MF_warning_statements`) with scheme, market and hazard, evaluated per market at preflight and projected to listings where a market requires or recommends online display (Appendix D); free-text warnings in descriptions MUST derive from the records.

**CDS2000-R039** Restricted-sale status (age-restricted sporting goods such as knives and air guns, prescription pet medicines, products banned in a market) MUST be governed per-market attributes evaluated at preflight (the CDS-1700 §12 pattern).

**CDS2000-R040** Recalls and safety withdrawals MUST be handled through lifecycle state and channel withdrawal (CDS-500 §12) with affected batch or date ranges recorded as observations; deletion of the product record is prohibited (CDS-200 §14).

## 9. Customer Facet Design *(informative — normative facet rules live in CDS-600)*

| Facet | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Shop by sport | Governed `sport_activity` values, multi-select OR, top-level navigation entry | Category per sport duplicating products |
| Shop by age | Governed `toy_age_range` bands; never the safety warning | Bands typed per product; "3+" as text |
| Play type | Governed values | Marketing theme tags |
| Players / play time | Numeric range facets | Text buckets |
| Shop by pet | Governed `pet_type` values; life stage and size as secondary facets | Species from category name |
| Food form / dietary | Governed `pet_food_form`; dietary claims only from accepted claim records | "Grain-free" tag without evidence |
| Size (equipment) | Size-system-qualified facets with measured bounds | Unqualified "M" across systems |
| Certification | Never a facet unless fed by accepted records | "CE certified" tag |

## 10. Channel Projection Guidance *(informative — normative rules: CDS-500, CDS-900)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Sport activity, age band, pet type | Category metafields where the taxonomy defines them (activity, age group, pet type attributes exist in the seeded channel taxonomy), custom metafields otherwise | Title and `product_detail`; Google `age_group` is an apparel audience attribute (newborn, infant, toddler, kids, adult), not a toy age band — do not map toy age bands to it |
| Safety age and hazard warnings | Per-market generated blocks near the price or in the description, verified | Description; where a market requires visibility before purchase, the listing must carry it |
| Nutritional adequacy and analysis | Structured metafields; generated description block | `product_detail` |
| Certification and compliance | Information blocks generated from records | Not published as attributes |
| Restricted sale | Channel exclusion rules | Channel exclusion; `adult` flag where the channel uses it |

## 11. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Activity, play type, pet type from copy and images | Dictionary candidates with evidence | Governed dictionaries; review for multi-value maxima |
| Age band suggestion | Retail band candidates | Never the safety warning (R018–R020) |
| Hazard facts | None from category; extraction from packaging or test reports (E1) as proposals | Human review; unknown quarantined (R020) |
| Ingredient and analysis extraction | Structured candidates from labels (E1) | Scheme and unit validation (CDS-1700 §5–§6) |
| Nutritional adequacy | None — manufacturer statement only | R032 |
| Compatibility (components, consumables) | Candidate relationships with evidence | CDS-1900 §5 review rules |

## 12. Governance and Organisational Extensions *(informative — rules in CDS-1500 §23 and CDS-800)*

The Chapter 12–14 vocabularies are extended under CDS-400. Organisations add skill-level, breed, franchise, use-environment and theme dictionaries as governed extensions (§5 R015, §6 R026, §7 R028). Toy-safety and pet-food regimes change on multi-year cycles with long transition periods (for example the EU toy regulation's 2030 application date); the register review cadence should align to those transitions and to any market's list changes for mandatory standards.

## 13. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS2000-R041** An implementation claiming the CDS Sports and Outdoor Profile MUST: govern sport or activity as a multi-valued dictionary attribute (R005, R009); identify equipment size systems with measured bounds (R006); store performance ratings with scheme and basis (R010); maintain certification records for protective equipment with per-market preflight (R011); bind wetsuit attributes to governed dictionaries where exposed (R012); express compatibility and inclusion through relationship records (R008, R013); apply CDS-1800 and CDS-1900 for powered equipment and consumables (R014, R016); satisfy the CDS-1500 apparel and footwear baselines for apparel sold under the profile (R017); maintain warnings, restricted-sale and recall handling (R038–R040); maintain a jurisdiction requirement register for every market published to (R003); and publish and verify channel representations under CDS-500.

**CDS2000-R042** An implementation claiming the CDS Toys and Games Profile MUST: keep retail age band, manufacturer's recommended age and safety age warning as separate attributes (R018); maintain structured hazard facts and market-specific warnings projected and verified where required online (R019–R020, R024, R038); bind age band and play type to governed dictionaries (R021); store game facts as typed values (R022, R025); maintain per-market compliance records evaluated at preflight (R023); govern licensed properties (R026); apply other profiles' layers where present (R027); handle restricted sale and recalls (R039–R040); maintain a jurisdiction requirement register for every market published to (R003); and publish and verify channel representations under CDS-500.

**CDS2000-R043** An implementation claiming the CDS Pet Supplies Profile MUST: govern pet type, life stage and size with measured bounds (R028–R029, R035); store ingredients, analysis and nutritional adequacy as structured records with schemes and evidence (R030–R032); bind food form to the governed dictionary (R033); maintain per-market registration and restricted-sale records for health products (R034); exclude live animals absent a declared extension (R036); express consumable compatibility through relationship records (R037); handle warnings, restricted sale and recalls (R038–R040); maintain a jurisdiction requirement register for every market published to (R003); and publish and verify channel representations under CDS-500.

## 14. Worked Product Examples *(informative)*

### 14.1 Toy — Magnetic building set

```
CAT_product_type = construction_toy; MF_play_type = [construction, stem]
MF_age_band = [age_3_5, age_6_8]; MF_recommended_age_min_months = 36
MF_contains_magnets = true; MF_small_parts = true; MF_piece_count = 100
MF_safety_age_warning = {scheme: eu_toy_safety_2009_48, statement: "Warning. Not suitable for children under 36 months. Small parts. Choking hazard.", hazard: [small_parts]}
MF_warning_statements += {scheme: eu_toy_safety_2009_48, statement: "Warning. This toy contains magnets or magnetic components..."},
                         {scheme: us_cpsc_16_cfr_1500_19, statement: "WARNING: CHOKING HAZARD - Small parts. Not for children under 3 yrs."},
                         {scheme: au_toys_containing_magnets_2020, statement: <mandatory warning text>}
CMP_compliance_declarations = [{jurisdiction: EU, scheme: eu_toy_safety_2009_48, mark: CE, doc_ref: MED-..},
                               {jurisdiction: US, scheme: us_cpsia_children_product, cpc_ref: MED-.., tracking_label: true},
                               {jurisdiction: AU, scheme: au_toys_containing_magnets_2020, test_report: MED-..}]
EU listing: warning visible before purchase -> verified; US listing: cautionary statement displayed -> verified
```

### 14.2 Pet food — Dry dog food, large breed adult

```
CAT_product_type = dog_food_dry; MF_pet_type = [dog]; MF_pet_life_stage = adult; MF_pet_size = large {weight_min_kg: 25, weight_max_kg: 45}
MF_pet_food_form = dry_kibble
MF_ingredient_list = [chicken_meal, brown_rice, ...] (scheme: manufacturer_declared, order: descending_by_weight)
MF_nutrition_values = {scheme: guaranteed_analysis_pet_food, basis: as_fed, values: [{crude_protein, min, 26, %}, {crude_fat, min, 12, %}, {crude_fibre, max, 4, %}, {moisture, max, 10, %}]}
MF_nutritional_adequacy = {scheme: aafco_dog_food_nutrient_profiles, life_stage: adult_maintenance, status: complete_and_balanced, evidence: E1}
Variants: 3 kg (VAR_net_quantity = {3, kilogram}), 12 kg, 20 kg; unit price per kilogram derived
AU: complies with AS 5812 (voluntary) recorded as certification; US: state feed registration recorded per state where required
```

### 14.3 Sports — Wetsuit

```
CAT_product_type = wetsuit; MF_sport_activity = [surfing]
MF_wetsuit_style = full_suit; MF_wetsuit_thickness = t_3_2 (3/2 mm); MF_wetsuit_zip = chest_zip; MF_wetsuit_seam = glued_blind_stitched
VAR_size_system = <brand_wetsuit_size_system>; VAR_size_label = "MT"; measured bounds: height 178-185 cm, chest 96-101 cm
MF_temperature_rating = {value_min: 12, value_max: 17, unit: celsius, basis: manufacturer_rated}
```

## 15. Reference Validation Cases *(informative — the profiles' contribution to the cross-industry validation set, REVIEW-020)*

- a safety age warning derived from the retail age band (must fail R018);
- a toy with `MF_contains_magnets` unknown defaulted to false (must quarantine, R020);
- an EU toy listing without the age warning visible before purchase (verification must report, R019, D-EU-1);
- a US internet listing of a small-parts toy without the cautionary statement (R019, D-US-1);
- a helmet sold into Australia without a bicycle-helmet certification record (must block, R011, D-AU-2);
- a sport activity encoded as a category rather than an attribute (R009);
- a temperature rating compared across two different schemes (R010);
- a pet food with adequacy "inferred" from ingredients (R032);
- a "medium dog" size class with no weight bounds feeding a weight filter (R029);
- a prescription pet medicine published to a marketplace that cannot enforce the restriction (R034);
- a wetsuit thickness stored as free text "3/2mm" (R012);
- a "batteries not included" statement with no `requires` record (R008).

---

## Appendix A. Attribute Baselines *(normative — dictionary bindings per CDS1500-R011)*

### A.1 Sports and Outdoor

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_sport_activity | Product | Governed dictionary list (`sport_activity`) | R |
| VAR_size_system / VAR_size_label / measured bounds | Variant | Governed system; text; typed measurements | R for sized equipment and apparel |
| MF_wetsuit_style / MF_wetsuit_thickness / MF_wetsuit_zip / MF_wetsuit_seam | Product | Governed dictionary references | R for wetsuits where exposed; REC otherwise |
| MF_temperature_rating / MF_waterproof_rating / MF_season_rating | Product | Typed values with scheme and basis | C |
| MF_user_weight_limit_kg / MF_capacity_persons / MF_capacity_l | Product | Typed measurements | C — R where a limit exists |
| MF_certifications | Product (per market) | Certification records | R for protective equipment |
| Relationship records (`compatible_with`, `includes`, `requires`, `fits`) | Product | Records per CDS-1900 §5 | C |
| Battery and power fields | Product / Variant | Per CDS-1800 §8 | R for powered products |
| CMP_dangerous_goods | Product / Variant | Declaration per CDS-1900 §12 | R (explicit value) |
| MF_warning_statements / CMP_restricted_sale | Product (per market) | Structured records | C |
| Apparel and footwear baseline | — | Per CDS-1500 Appendices A and A.1 | R where applicable |

### A.2 Toys and Games

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_age_band | Product | Governed dictionary list (`toy_age_range`) | R |
| MF_recommended_age_min_months / MF_recommended_age_max_months | Product | Integers | REC; R where a market requires the manufacturer's age |
| MF_safety_age_warning | Product | Structured statement record | C — R where a market mandates it |
| MF_play_type | Product | Governed dictionary list (`play_type`) | REC |
| MF_piece_count | Product / Variant | Integer | C |
| MF_player_count_min / MF_player_count_max / MF_play_time_min / MF_play_time_max | Product | Integers | R for games |
| MF_language | Product / Variant | Governed language codes | C |
| MF_small_parts / MF_contains_magnets / MF_contains_button_batteries / MF_projectile / MF_cord_length_mm | Product | Booleans; typed measurement | R (explicit values; unknown quarantined) |
| MF_warning_statements | Product (per market) | Structured records | C — R where mandated |
| CMP_compliance_declarations / CMP_responsible_person / CMP_product_identifier | Product (per market) | Governed records | R where a market regulates toys |
| Battery and power fields / CMP_dangerous_goods | Product / Variant | Per CDS-1800 §8, CDS-1900 §12 | R for battery products |
| MF_licensed_property | Product | Governed organisation dictionary | C |
| MF_weight_limit_kg | Product | Typed measurement | R for ride-ons and play equipment |

### A.3 Pet Supplies

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| CAT_product_type | Product | Governed classification reference | R |
| MF_pet_type | Product | Governed dictionary list (`pet_type`) | R |
| MF_pet_life_stage | Product | Governed dictionary reference (`pet_life_stage`) | C — R for food formulated by life stage |
| MF_pet_size | Product | Governed dictionary reference (`pet_size`) with bounds | C |
| MF_pet_food_form | Product | Governed dictionary reference (`pet_food_form`) | R for food and treats |
| MF_ingredient_list / MF_ingredient_naming_scheme | Product | Ordered structured list | R for food, treats and supplements |
| MF_nutrition_values | Product | Typed values with scheme and basis | R for food where a market requires analysis; REC otherwise |
| MF_nutritional_adequacy | Product | Structured record with scheme | R for complete foods; C otherwise |
| MF_feeding_guide | Product | Structured table or document | REC; R where a market requires feeding directions |
| VAR_net_quantity | Variant | Typed measurement | R |
| MF_storage_condition / MF_date_mark_type | Product | Governed values | C |
| CMP_market_registrations / CMP_restricted_sale / MF_active_ingredients / MF_dosage_form | Product (per market) | Governed records | R for health products |
| Relationship records (`compatible_with`, `accessory_for`, `fits`) | Product | Records per CDS-1900 §5 | C |
| MF_warning_statements | Product (per market) | Structured records | C |

## Appendix B. Dictionary Bindings *(informative — becomes governed data on adoption per CDS1500-R011)*

| Dictionary key | Package chapter | Bound attribute(s) | Status at 0.8.0 |
|---|---|---|---|
| sport_activity | 12 | MF_sport_activity | Bound by this chapter |
| wetsuit_style / wetsuit_thickness / wetsuit_zip / wetsuit_seam | 12 | MF_wetsuit_* | Bound |
| play_type / toy_age_range | 13 | MF_play_type / MF_age_band | Bound |
| pet_type / pet_life_stage / pet_size | 14 | MF_pet_type / MF_pet_life_stage / MF_pet_size | Bound |
| pet_food_form | 14 (new, 0.8.0) | MF_pet_food_form | Bound |
| size_system (`bike_frame_cm`, `head_circumference_cm` added at 0.8.0) | 5 | VAR_size_system | Bound |
| storage_condition, allergen, dietary_claim_type | 17 | Per CDS-1700 patterns where used | Bound via CDS-1700 |
| battery_chemistry, product_condition, relationship_type, dangerous_goods_class | 11, 18 | Per CDS-1800 and CDS-1900 | Bound via those chapters |
| jurisdiction / regulatory_scheme | 19 | CMP_* records, warning schemes | Bound via CDS-1500 §2.2 |

Deliberately not shipped: skill levels, performance tiers, breed lists, licensed-property registries, theme and character vocabularies, live-animal vocabularies, pet nutrient profiles (scheme-published).

## Appendix C. References *(informative; retrieved 2026-09-20 unless stated)*

| Ref | Source | Location | Use in this chapter |
|---|---|---|---|
| [S1] | ACCC Product Safety — mandatory standards: Toys for children up to and including 36 months (Consumer Goods (Toys for Children up to and including 36 months of age) Safety Standard 2023, AS/NZS ISO 8124.1:2023); Toys containing magnets (2020); Projectile toys (2020); Bicycle helmets (2024); Sunglasses and fashion spectacles (2017); Products containing button/coin batteries (2020) | productsafety.gov.au; legislation.gov.au | D-AU-1 to D-AU-4 (retrieved; instrument texts not read this pass except button batteries, see CDS-1800 [E3]) |
| [S2] | Standards Australia — AS 5812:2023 Manufacturing and marketing of pet food (voluntary; referenced by the Pet Food Industry Association of Australia); APVMA — Agvet Code registration of veterinary chemical products | standards.org.au; apvma.gov.au | D-AU-5, D-AU-6 (retrieved) |
| [S3] | New Zealand — Product Safety Standards (Children's Toys) Regulations 2005; ACVM Act 1997 (pet food exemptions and standards) | legislation.govt.nz; mpi.govt.nz | D-NZ-1, D-NZ-2 (retrieved) |
| [S4] | US CPSC — Consumer Product Safety Improvement Act 2008 (children's product certificate, third-party testing, tracking labels); 16 CFR 1500.19 (small parts and other cautionary labelling), 16 CFR 1500.20 (labelling in internet and catalogue advertising), 16 CFR 1501 (small parts test), 16 CFR 1250 (ASTM F963 toy standard), 16 CFR 1203 (bicycle helmets) | cpsc.gov; ecfr.gov | D-US-1 to D-US-3 (retrieved; not spot-verified this pass) |
| [S5] | US FDA — Pet food labelling (21 CFR 501); AAFCO — Model Regulations for pet food and specialty pet food (product name, guaranteed analysis, ingredient statement, nutritional adequacy statement, feeding directions, quantity, manufacturer); state feed control laws | fda.gov; aafco.org | D-US-4 (retrieved) |
| [S6] | Directive 2009/48/EC on the safety of toys (warnings determining the decision to purchase visible before purchase including online); Regulation (EU) 2025/2509 on the safety of toys (in force 1 January 2026; applies from 1 August 2030; digital product passport; online offers) | eur-lex.europa.eu | D-EU-1 (regulation verified 2026-09-20; directive detail retrieved) |
| [S7] | Regulation (EU) 2016/425 on personal protective equipment; Regulation (EU) 2023/988 (GPSR) | eur-lex.europa.eu | D-EU-2, D-EU-3 |
| [S8] | Regulation (EC) No 767/2009 on the placing on the market and use of feed (labelling of pet food); Regulation (EC) No 1831/2003 (feed additives); FEDIAF Code of Good Labelling Practice for Pet Food | eur-lex.europa.eu; europeanpetfood.org | D-EU-4 (retrieved) |
| [S9] | UK — Toys (Safety) Regulations 2011; Personal Protective Equipment (Enforcement) Regulations 2018 with retained 2016/425; General Product Safety Regulations 2005; retained Regulation 767/2009 — OPSS, Defra | legislation.gov.uk; gov.uk | D-UK-1 to D-UK-3 (retrieved) |
| [S10] | Canada — Canada Consumer Product Safety Act; Toys Regulations (SOR/2011-17); Consumer Packaging and Labelling Act (bilingual); CFIA guidance on pet food (imports and labelling) | laws-lois.justice.gc.ca; inspection.canada.ca | D-CA-1, D-CA-2 (retrieved) |
| [S11] | StoreLeads (Shopify Plus category distribution, 2026-09-11); StoreInspect (average products per store by category, 2026-09-19) | storeleads.app; storeinspect.com | Market basis (REVIEW-020) |

## Appendix D. Jurisdiction Requirement Register — Seed *(informative seed of the normative register defined in CDS-1500 §2.2)*

Conventions as in CDS-1600 Appendix D. Most entries in this chapter were retrieved from regulator pages without reading the instrument text in this pass and are marked accordingly; organisations verify before relying on them.

### D.1 Australia (AU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-1 | Consumer Goods (Toys for Children up to and including 36 months of age) Safety Standard 2023 (AS/NZS ISO 8124.1:2023 provisions on small parts, sharp points and edges, cords); Consumer Goods (Toys Containing Magnets) Safety Standard 2020; Consumer Goods (Projectile Toys) Safety Standard 2020 — ACCC and state regulators (`au_toys_under_36_months_2023`, `au_toys_containing_magnets_2020`, `au_projectile_toys_2020`) | Toys for children up to 36 months; toys containing magnets; projectile toys | pre_market (compliance with the referenced standard provisions); warning_statement (magnet toys: mandatory warning on packaging or the toy); labelling_element | Small-parts, magnet and projectile compliance evidence; magnet warning text → MF_small_parts, MF_contains_magnets, MF_projectile, MF_warning_statements, CMP_compliance_declarations (test evidence) | Ongoing (2023 standard replaced the 2020 standard) | Retrieved 2026-09-20 [S1] (not spot-verified) |
| D-AU-2 | Consumer Goods (Bicycle Helmets) Safety Standard 2024 (AS/NZS 2063 and recognised international standards) — ACCC (`au_bicycle_helmets_2024`) | Bicycle helmets supplied in Australia | pre_market (certification to an accepted standard); labelling_element (certification marking) | Standard and certification evidence → MF_certifications (scheme `au_bicycle_helmets_2024`), CMP_compliance_declarations | Ongoing | Retrieved 2026-09-20 [S1] |
| D-AU-3 | Consumer Goods (Sunglasses and Fashion Spectacles) Safety Standard 2017 (AS/NZS 1067.1:2016 lens categories) — ACCC (`au_sunglasses_2017`) | Sunglasses and fashion spectacles | labelling_element (lens category and required markings) | Lens category 0–4 and marking → MF_lens_category, MF_warning_statements | Ongoing | Retrieved 2026-09-20 [S1] |
| D-AU-4 | Button and coin battery safety and information standards 2020 — ACCC (`au_button_battery_standards_2020`) | Toys and products containing button or coin batteries | As CDS-1800 D-AU-5 | Per CDS-1800 D-AU-5 → MF_contains_button_batteries, MF_warning_statements, listing projection | Mandatory from 22 June 2022 | Verified 2026-09-20 (CDS-1800 [E3]) |
| D-AU-5 | AS 5812:2023 Manufacturing and marketing of pet food (voluntary industry standard; PFIAA membership requirement) (`au_as_5812_pet_food`) | Pet food | documentation (voluntary labelling: product name, species, life stage, complete or complementary statement, ingredient list, typical analysis, feeding guide, net quantity, batch and best-before, manufacturer details) | Elements → MF_pet_type, MF_pet_life_stage, MF_nutritional_adequacy (scheme `au_as_5812_pet_food`), MF_ingredient_list, MF_nutrition_values, MF_feeding_guide, VAR_net_quantity | Voluntary (no mandatory national pet-food standard as at 2026-09-20; state stock-food laws apply in some states) | Retrieved 2026-09-20 [S2] |
| D-AU-6 | Agricultural and Veterinary Chemicals Code Act 1994 — APVMA (`au_apvma_agvet_code`) | Veterinary medicines, parasiticides and treatments for animals | pre_market (registration and approved label); restricted_content (scheduled medicines; prescription-only products); labelling_element | APVMA registration number, approved label, schedule and supply restrictions → CMP_market_registrations (scheme `au_apvma_agvet_code`), CMP_restricted_sale, MF_active_ingredients | Ongoing | Retrieved 2026-09-20 [S2] |

### D.2 New Zealand (NZ)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-1 | Product Safety Standards (Children's Toys) Regulations 2005 (AS/NZS ISO 8124.1 provisions for toys for children under 36 months) — MBIE and Commerce Commission (`nz_childrens_toys_regulations_2005`) | Toys for children under 36 months | pre_market (compliance with the referenced provisions) | Small parts, sharp points, cords compliance → MF_small_parts, CMP_compliance_declarations | Ongoing | Retrieved 2026-09-20 [S3] |
| D-NZ-2 | Agricultural Compounds and Veterinary Medicines Act 1997 — MPI (`nz_acvm_act_1997`) | Pet food (exempt from registration subject to conditions) and veterinary medicines (registration) | pre_market (veterinary medicines); documentation (pet food exemption conditions) | Registration or exemption status → CMP_market_registrations (scheme `nz_acvm_act_1997`) | Ongoing | Retrieved 2026-09-20 [S3] |

### D.3 United States (US)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-1 | Federal Hazardous Substances Act; 16 CFR 1500.19 (cautionary labelling for small parts, small balls, marbles, balloons) and 16 CFR 1500.20 (cautionary statements in internet and catalogue advertising) — CPSC (`us_cpsc_16_cfr_1500_19`) | Toys and games intended for children 3 to under 6 years with small parts; balloons; small balls; marbles | warning_statement; listing_element (the same cautionary statement must appear in internet advertising that offers direct purchase) | Statutory cautionary statement text and format → MF_safety_age_warning / MF_warning_statements (scheme `us_cpsc_16_cfr_1500_19`), listing projection and verification | Ongoing | Retrieved 2026-09-20 [S4] |
| D-US-2 | Consumer Product Safety Improvement Act 2008; 16 CFR 1250 (ASTM F963 toy safety standard); 16 CFR 1107 (third-party testing); 16 CFR 1130 (tracking labels) — CPSC (`us_cpsia_children_product`) | Children's products (designed or intended primarily for children 12 and under) | pre_market (Children's Product Certificate based on accredited third-party testing); labelling_element (tracking label with manufacturer, location and date of production, batch); documentation | CPC reference, test reports, tracking label data → CMP_compliance_declarations (scheme `us_cpsia_children_product`, CPC ref), CMP_product_identifier, MED_technical_documents | Ongoing | Retrieved 2026-09-20 [S4] |
| D-US-3 | 16 CFR 1203 Safety Standard for Bicycle Helmets — CPSC (`us_cpsc_16_cfr_1203`) | Bicycle helmets | pre_market (certification); labelling_element | Certification evidence and label → MF_certifications (scheme `us_cpsc_16_cfr_1203`) | Ongoing | Retrieved 2026-09-20 [S4] |
| D-US-4 | Federal Food, Drug, and Cosmetic Act and 21 CFR 501 (animal food labelling) — FDA; state feed laws adopting the AAFCO Model Regulations (product name, net quantity, guaranteed analysis, ingredient statement, nutritional adequacy statement, feeding directions, manufacturer or distributor name and address; state registration and licensing) (`us_fda_21_cfr_501_pet_food`, `us_aafco_state_feed_law`) | Pet food and treats sold in the US | labelling_element; documentation; pre_market (state product registration where required) | Elements → MF_nutrition_values (scheme `guaranteed_analysis_pet_food`), MF_nutritional_adequacy (scheme `aafco_*_nutrient_profiles` or feeding trial), MF_ingredient_list, MF_feeding_guide, VAR_net_quantity, CMP_responsible_person, CMP_market_registrations per state | Ongoing | Retrieved 2026-09-20 [S5] |
| D-US-5 | Proposition 65 (California) — OEHHA (`us_ca_prop65_warning`) | Toys, sporting goods and pet products causing listed-chemical exposure | warning_statement; listing_element | Per CDS-1800 D-US-3 | Effective 1 January 2025 | Verified 2026-09-20 (CDS-1800 [E7]) |

### D.4 European Union (EU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-1 | Directive 2009/48/EC on the safety of toys (CE marking, EC declaration of conformity, manufacturer and importer identification, warnings including age warnings and specific warnings for toys in Annex V; warnings that determine the decision to purchase must be clearly visible before purchase including online) — to be replaced by Regulation (EU) 2025/2509 (applies from 1 August 2030; digital product passport; online offers to display warnings and safety information) (`eu_toy_safety_2009_48`, `eu_toy_safety_regulation_2025_2509`) | Toys (products designed or intended for use in play by children under 14) | pre_market (conformity assessment; DoC; technical file); labelling_element (CE marking; manufacturer and importer name and address; type/batch/serial); warning_statement; listing_element | Warning texts (preceded by "Warning"), age warning with hazard where applicable, CE marking, identification, DoC reference → MF_safety_age_warning, MF_warning_statements (scheme `eu_toy_safety_2009_48`), CMP_compliance_declarations, CMP_responsible_person, CMP_product_identifier, listing projection | Directive in force until 1 August 2030; regulation in force 1 January 2026 | Regulation verified 2026-09-20 [S6]; directive online-visibility detail retrieved (not spot-verified) |
| D-EU-2 | Regulation (EU) 2016/425 on personal protective equipment (`eu_ppe_2016_425`) | Helmets, eye protection, flotation aids, protective sports equipment classified as PPE (Category I–III) | pre_market (conformity assessment by category; DoC; notified body for II/III); labelling_element (CE marking; identification; instructions) | Category, standard, notified body number where applicable, DoC → MF_certifications, CMP_compliance_declarations (scheme `eu_ppe_2016_425`), MED_technical_documents | Ongoing | Retrieved 2026-09-20 [S7] (not spot-verified) |
| D-EU-3 | Regulation (EU) 2023/988 General Product Safety Regulation (`eu_gpsr_2023_988`) | Non-harmonised sports equipment, pet accessories and other consumer products; cross-cutting online-offer duties | listing_element; labelling_element; pre_market (responsible economic operator) | Per CDS-1800 D-EU-6 | Applies from 13 December 2024 | Verified 2026-09-20 (CDS-1800 [E13]) |
| D-EU-4 | Regulation (EC) No 767/2009 on the placing on the market and use of feed (Chapter 4 labelling: type of feed, feed business operator, net quantity, composition, analytical constituents, additives, moisture, best-before, batch, instructions for proper use, species and category of animal, complete or complementary designation); Regulation (EC) No 1831/2003 (additives); FEDIAF labelling code (`eu_feed_labelling_767_2009`) | Pet food (feed for pet animals) | labelling_element; documentation | Elements → MF_pet_type, MF_pet_life_stage, MF_nutritional_adequacy (complete/complementary; scheme `fediaf_nutritional_guidelines` where claimed), MF_ingredient_list (composition by category or ingredient), MF_nutrition_values (scheme `eu_analytical_constituents`), MF_feeding_guide, VAR_net_quantity, MF_date_mark_type, CMP_responsible_person | Ongoing | Retrieved 2026-09-20 [S8] (not spot-verified) |
| D-EU-5 | Regulation (EU) 2019/6 on veterinary medicinal products (`eu_veterinary_medicines_2019_6`) | Veterinary medicines and medicated products | pre_market (marketing authorisation); restricted_content (prescription status; online retail rules per member state) | Authorisation and prescription status → CMP_market_registrations, CMP_restricted_sale | Applies from 28 January 2022 | Retrieved (not spot-verified) |

### D.5 United Kingdom (GB)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-1 | Toys (Safety) Regulations 2011 — OPSS (`uk_toys_safety_regulations_2011`) | Toys placed on the GB market | pre_market (UKCA or CE marking with indefinite CE recognition from 1 October 2024; DoC; technical file); labelling_element; warning_statement (warnings visible before purchase including online) | As D-EU-1 with GB marking and importer identification → MF_safety_age_warning, MF_warning_statements (scheme `uk_toys_safety_regulations_2011`), CMP_compliance_declarations, CMP_responsible_person | Ongoing; CE recognition indefinite from 1 October 2024 | Retrieved 2026-09-20 [S9] |
| D-UK-2 | Regulation (EU) 2016/425 as retained (PPE) with the Personal Protective Equipment (Enforcement) Regulations 2018; General Product Safety Regulations 2005 — OPSS (`uk_ppe_retained_2016_425`, `uk_gpsr_2005`) | PPE (helmets, eyewear, flotation); non-harmonised consumer products | pre_market; labelling_element | Certification and identification → MF_certifications, CMP_compliance_declarations | Ongoing | Retrieved 2026-09-20 [S9] |
| D-UK-3 | Regulation (EC) 767/2009 as retained (animal feed labelling); Veterinary Medicines Regulations 2013 (as amended 2024) — Defra, VMD (`uk_feed_labelling_retained_767_2009`, `uk_veterinary_medicines_regulations`) | Pet food; veterinary medicines | labelling_element; pre_market; restricted_content (distribution categories POM-V, POM-VPS, NFA-VPS, AVM-GSL) | As D-EU-4; authorisation and distribution category → CMP_market_registrations, CMP_restricted_sale | Ongoing | Retrieved 2026-09-20 [S9] |

### D.6 Canada (CA)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-CA-1 | Canada Consumer Product Safety Act; Toys Regulations (SOR/2011-17) (small parts, magnets, cords, noise, toxic substances, age-related requirements); Consumer Packaging and Labelling Act (bilingual identity, net quantity, dealer) — Health Canada (`ca_toys_regulations_2011`) | Toys and children's products | pre_market (compliance; no certificate regime but records on request); warning_statement (bilingual); labelling_element | Bilingual warnings and identity → MF_warning_statements (scheme `ca_toys_regulations_2011`, EN and FR), CMP_responsible_person, localisation per CDS-300 §18 | Ongoing | Retrieved 2026-09-20 [S10] |
| D-CA-2 | Pet food: Consumer Packaging and Labelling Act and Competition Act (labelling and representations); Feeds Act (largely excludes pet food); Health of Animals Act import conditions — CFIA and Competition Bureau (`ca_pet_food_labelling`) | Pet food sold in Canada | labelling_element (bilingual identity, net quantity, dealer identity); documentation (import conditions) | Elements → MF_pet_type, VAR_net_quantity, CMP_responsible_person; voluntary AAFCO-style adequacy statements → MF_nutritional_adequacy | Ongoing | Retrieved 2026-09-20 [S10] |

### D.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Japan (JP), China (CN), Republic of Korea (KR), India (IN), Brazil (BR) and others | Not seeded | Toy safety marks (ST mark, CCC, KC), PPE and pet-food regimes differ; organisation supplies entries with local advice. |

END OF CDS-2000 v0.2 REVIEW DRAFT
