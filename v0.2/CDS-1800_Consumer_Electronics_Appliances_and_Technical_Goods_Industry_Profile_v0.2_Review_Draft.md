# Commerce Data Standard (CDS)
## CDS-1800 — Consumer Electronics, Appliances and Technical Goods Industry Profile

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5); chapter added in the 2026-09-20 industry-profile expansion |
| Date | 2026-09-20 |
| Supersedes | Nothing — first edition. The Chapter 11 dictionary vocabularies (connectivity, screen technologies, power sources, installation types, energy rating systems) were shipped ahead of this profile and are bound here for the first time; battery chemistries and product conditions are added in package 0.8.0. |
| Normative status | §1, §3, §5–§12, §17 and Appendix A are normative. §2 (pointer), §4, §13–§16, §18, §19 and Appendices B–D are informative; Appendix D seeds the jurisdiction requirement register whose record structure and obligations are normative in CDS-1500 §2.2. Every table is individually marked. |
| Primary audience | Electronics and appliance merchandisers, compliance and product-safety owners, data stewards, PIM architects, catalogue managers, UX teams, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1500, especially CDS-200 (entity model, relationships), CDS-300 (CMP_, MED_, SUP_), CDS-400 (dictionaries, units), CDS-500 (preflight, verification), CDS-600 (facets), CDS-700 (evidence), CDS-900 (platform profiles), CDS-1100 (identifier and measurement contracts), CDS-1500 (profile model, requirement levels, profile register, jurisdiction requirement register), CDS-1900 (product relationship record, kits and bundles, dangerous-goods declarations) |
| Companion package | CDS Reference Dictionary: Chapter 11 (Electronics & Appliances), Chapter 18 (Parts, Automotive & Industrial: product conditions, dangerous-goods classes), Chapter 19 (Jurisdictions & Regulatory Schemes) |
| Profile identifier | `cds.profile.electronics.v0_2` (registered in CDS-1500 §2.1) |
| Research basis | REVIEW-020 (global commerce vertical market research, 2026-09-20): consumer electronics is the largest worldwide ecommerce category by revenue (estimated at roughly US$1 trillion for 2026) and the largest category of Amazon's global gross merchandise value (38% in 2025); electronics stores carry among the largest catalogues on Shopify (average above 2,400 products per store), so the vertical's PIM intensity far exceeds its store count. |

Terminology follows CDS-100. Attribute requirement levels (R, C, REC, O, N/A) are those of CDS-1500 §4 and are not restated here. "Technical goods" in this chapter means products whose purchase decision is dominated by measured specifications and compatibility rather than by appearance.

---

## 1. Purpose and Scope *(normative)*

CDS-1800 defines the industry profile for consumer electronics (phones, computers, audio, video, cameras, gaming, wearables, smart home), small and large domestic appliances, and technical accessories (cables, chargers, mounts, storage media). It also governs the technical-specification layer of products homed in other profiles (a beauty device, a power tool, a bicycle computer) where those chapters cite it.

The data shape is distinctive for four reasons: identity is manufacturer-anchored (brand plus manufacturer part number, usually with a GTIN) and variants differ by capacity, colour, region or plug rather than by size; the record is dominated by dozens to hundreds of measured, unit-bearing specifications whose set depends on the product type; compatibility ("works with", "fits", "requires") is a relationship between products or standards, not an attribute; and a large regulated layer (electrical safety marks, radio approvals, energy labels, battery and transport rules, repairability and take-back obligations) differs by jurisdiction and, in several markets, must be shown online next to the price.

**CDS1800-R001** An implementation claiming the Electronics Profile MUST represent technical specifications as typed, unit-bearing attribute values governed by Attribute Definitions (CDS-200 §7, CDS-400 §18), never solely as specification text, tables in descriptions or images of specification sheets.

**CDS1800-R002** An implementation claiming this profile MUST represent compatibility, inclusion and accessory relationships as product relationship records per CDS-1900 §5, never as tags, free text or category membership.

**CDS1800-R003** An implementation MUST maintain a jurisdiction requirement register (CDS-1500 §2.2) for every market it publishes electrical or electronic goods to, and publication preflight for a market MUST evaluate the market's pre-market, marking, energy-label, battery, transport and listing obligations before the offer is made available.

**CDS1800-R004** This profile MUST NOT weaken any rule of CDS-1500 that it reuses; where this chapter is silent, CDS-1500 and the core chapters govern.

## 2. Profile Model *(informative pointer)*

This profile applies the industry profile model of CDS-1500 §2, the requirement levels of CDS-1500 §4 and the jurisdiction requirement register of CDS-1500 §2.2 without restatement. Its identifier and dictionary bindings are in CDS-1500 §2.1; its seeded jurisdiction entries are in Appendix D.

## 3. Product Model *(normative)*

A technical product is a manufacturer model offered in one or more sellable configurations. The Product is the model (the television model, the laptop model line as configured by the manufacturer); Variants are the sellable configurations that differ by capacity, memory, screen size within a model line, colour, region, plug type or bundled accessories. Model families (a generation, a series) are relationships, not product attributes.

```
Product: 65-inch 4K OLED television, model X65Q      (informative example)
  Product scope:
    STD_brand = Example Electronics
    SUP_manufacturer_part_number = X65Q-AU
    CAT_product_type = television
    MF_screen_size_in = 65
    MF_screen_technology = oled                        # screen_technology dictionary
    MF_resolution = {horizontal: 3840, vertical: 2160}
    MF_connectivity = [hdmi, wifi, bluetooth, ethernet]
    MF_hdmi_port_count = 4
    MF_power_consumption_w = 180
    CMP_energy_ratings = [{jurisdiction: AU, scheme: au_energy_rating, value: 4.5, registration_id: ...},
                          {jurisdiction: EU, scheme: eu_energy_label, class: F, eprel_id: ...}]
  Variant scope:
    VAR_region = AU
    VAR_plug_type = AU
    VAR_gtin = 09300000000010
```

**CDS1800-R005** Capacity, memory, storage, screen size within a model line, colour, region and plug type MUST be modelled at variant scope where they identify distinct sellable units (variant boundary rule: CDS-200 §5); specifications shared by every configuration MUST remain at product scope.

**CDS1800-R006** Where a specification differs between configurations (battery capacity, weight, energy rating), the implementation MUST store the differing value at variant scope for the affected variants and MUST NOT publish a product-scope value as if it applied to every configuration.

**CDS1800-R007** Model families, generations and successor relationships MUST be product relationship records (CDS-1900 §5) with typed relationship types, never encoded only in titles or in a free-text "series" field.

**CDS1800-R008** Where a channel's variant-option limit is smaller than the model's configuration dimensions, the implementation MUST apply a documented decomposition strategy (CDS900-R024) and MUST preserve the canonical configuration dimensions in the PIM.

## 4. Product Families and Category Profiles *(informative baseline; the inheritance rule of CDS1500-R016 applies)*

| Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|
| Mobile phones and tablets | brand; MPN; GTIN; screen size and technology; storage; memory; battery capacity; connectivity; operating system; region; charging port type and power; battery chemistry and transport class | ingress-protection rating; energy label per market; repairability class where a market issues one; included charger status | storage, colour, region |
| Computers | brand; MPN; processor; memory; storage; screen size; operating system; ports; battery capacity (portables) | dimensions and weight; energy label per market | configuration, colour |
| Audio (headphones, speakers) | brand; MPN; connectivity; power source; battery capacity where rechargeable | driver size; codec support; ingress rating; case battery | colour |
| Television and video | brand; MPN; screen size; screen technology; resolution; connectivity and port counts; energy rating per market; installation type | HDR formats; refresh rate; smart platform | size |
| Cameras and optics | brand; MPN; sensor format; resolution; lens mount; battery | video capabilities; weather sealing | kit configuration |
| Small appliances | brand; MPN; power source; wattage; capacity; dimensions; electrical safety compliance per market | energy or water rating where regulated; installation type | colour |
| Large and white goods | brand; MPN; capacity; dimensions; energy and water ratings per market; installation type; electrical compliance | noise level; programme features; delivery class | colour, finish |
| Smart home and networking | brand; MPN; connectivity standards and versions; power source; compatibility relationships | hub or ecosystem requirements as relationships | colour |
| Accessories (cables, chargers, mounts, cases) | brand; MPN; connector or mount standard; compatibility relationships; power delivery where applicable | length; material | length, colour |
| Batteries and power banks | chemistry; capacity (Wh and mAh); voltage; cell count; transport classification | charging ports; power delivery | capacity |

## 5. Identity and Identifiers *(normative)*

| Field | Meaning | Type |
|---|---|---|
| STD_brand | Brand as marketed | Governed brand dictionary value |
| SUP_manufacturer | Legal manufacturer where different from brand | Governed value |
| SUP_manufacturer_part_number | Manufacturer part or model number (MPN) | Identifier |
| MF_model_name | Marketed model name | Text |
| VAR_gtin | Trade item identifier with scheme | Identifier (GTIN-8/12/13/14 or declared alternative) |
| MF_identifier_exists | Whether a manufacturer-assigned trade identifier exists | Boolean |
| MF_series / MF_generation | Family and generation | Relationship records (R007) plus optional governed labels |
| MF_release_date / lifecycle.end_of_sale_date | Market release and end-of-sale dates | Dates |

**CDS1800-R009** Brand and manufacturer part number MUST be governed identity attributes; a GTIN MUST be stored with its scheme and MUST validate per scheme (CDS-1100), and the absence of a manufacturer-assigned identifier MUST be an explicit declaration (`MF_identifier_exists = false`), never an empty field.

**CDS1800-R010** A retailer SKU MUST NOT be substituted for the manufacturer part number in the MPN attribute; the two are distinct identifiers with distinct authority.

**CDS1800-R011** Model name and model number MUST be separate attributes; a regional suffix on a part number (for example a plug-region code) MUST be represented at variant scope, not by forking the product.

**CDS1800-R012** Where a market requires a product identification element (type, batch or serial number) and the manufacturer's identity and address on the product or in the online offer (Appendix D), the product identifier MUST be a governed attribute and the responsible-person record (CDS-1600 §12 pattern; `CMP_responsible_person`) MUST be maintained per market.

**CDS1800-R013** Release date and end-of-sale date MUST be typed dates in the product lifecycle group (CDS-1100 §8); "new" and "discontinued" storefront states MUST derive from them under governed rules (CDS600-R086).

## 6. Technical Specifications *(normative)*

Specifications are the heart of this profile. Every specification is an Attribute Definition with a declared data type, unit, cardinality, validation range and comparison strategy; the set of specifications required for a product type is declared in the category profile, not improvised per product.

| Rule area | Mechanism |
|---|---|
| Specification sets | Each category profile declares its specification set with requirement levels (R/C/REC/O) — for example a television declares screen size, technology, resolution, refresh rate, port counts, power consumption, dimensions with and without stand, weight |
| Units | Every numeric specification carries a governed unit; storage capacity declares its base (decimal gigabyte or binary gibibyte) per organisation policy |
| Standards and versions | Interface and protocol standards (Wi-Fi 6E, Bluetooth 5.3, HDMI 2.1, USB4, DisplayPort 2.1, Thunderbolt 4) are governed dictionary values with version as part of the value, not free text |
| Ranges and "up to" | Manufacturer maximums ("up to 20 hours") are stored as typed values with a basis qualifier (`manufacturer_rated`, `measured_under_scheme`), never as bare numbers implying measurement |
| Provenance | Each accepted specification value carries provenance to the manufacturer specification sheet or regulatory database (evidence class E1) or to an official product page (E2) |

**CDS1800-R014** Every specification exposed for search, filtering, comparison or channel publication MUST be an Attribute Definition with a declared data type, unit (where numeric), validation range and comparison strategy (CDS200-R023, CDS400-R056); a specification that exists only inside description text MUST NOT be treated as populated.

**CDS1800-R015** The specification set for a product type MUST be declared in the category profile with requirement levels; requiredness MUST NOT be evaluated against a flat universal specification list (CDS1500-R009).

**CDS1800-R016** Interface, protocol and standard versions MUST be governed dictionary values that include the version where the version is commercially meaningful (the `connectivity` dictionary pattern), and MUST NOT be free text.

**CDS1800-R017** A manufacturer-rated maximum or typical value MUST carry a basis qualifier distinguishing it from a value measured under a declared scheme; the two MUST NOT be compared as equivalent.

**CDS1800-R018** Specification values MUST carry provenance to an eligible source (CDS-700 §7 E1 or E2); an AI-extracted specification MUST be a proposal with evidence and MUST be validated against the Attribute Definition's unit and range before acceptance, and an implementation MUST NOT accept a specification value with no eligible evidence (CDS700-R018).

**CDS1800-R019** Where two eligible sources disagree on a specification, the conflict MUST be surfaced for review (CDS700-R019); the implementation MUST NOT silently prefer the more favourable value.

## 7. Compatibility and Standards Compliance *(normative)*

Compatibility is the single most-asked question in this vertical and the most-often faked. The profile represents it as relationships and standards, never as inference.

**CDS1800-R020** Compatibility between products (an accessory and the devices it fits, a component and the systems it works in) MUST be expressed as product relationship records of a governed type (`compatible_with`, `accessory_for`, `requires`, `fits`) per CDS-1900 §5, with the target expressed as a product, a model family, a governed standard or an application record; it MUST NOT be expressed as tags, category placement or free text alone.

**CDS1800-R021** "Universal" compatibility MUST be an explicit declaration bound to a governed standard (for example a connector or mount standard) rather than an absence of relationship records.

**CDS1800-R022** Compatibility MUST NOT be inferred from category similarity, title similarity or shared brand by rules or AI; a proposed relationship requires eligible evidence and human review before publication.

**CDS1800-R023** Standards-compliance and certification claims (certified to a wireless, connector, safety or performance standard) MUST be governed claim or certification records with the certifying scheme and evidence (CDS-1600 §11 pattern; `MF_certifications`), and MUST NOT be projected as facets unless fed by accepted records.

**CDS1800-R024** Port and slot counts MUST be typed integer specifications per governed interface value (for example `MF_hdmi_port_count`), never a comma-separated list.

## 8. Power, Batteries and Energy Ratings *(normative; dictionary bindings informative)*

| Field | Meaning | Type |
|---|---|---|
| MF_power_source | Governed value (`power_source` dictionary: mains, rechargeable battery, replaceable battery, USB powered, …) | Product |
| MF_input_voltage_range_v / MF_input_frequency_hz | Electrical input | Typed measurements or ranges |
| VAR_plug_type | Plug or socket standard supplied | Governed value (variant scope; CDS-1500 §13) |
| MF_rated_power_w / MF_power_consumption_w | Rated power and consumption | Typed measurements |
| MF_battery_chemistry | Governed value (`battery_chemistry` dictionary: lithium_ion, lithium_polymer, lithium_metal, nickel_metal_hydride, alkaline, lead_acid, sodium_ion, …) | Product/Variant |
| MF_battery_capacity_wh / MF_battery_capacity_mah / MF_battery_voltage_v | Battery capacity and voltage | Typed measurements (watt-hours mandatory for lithium transport classification) |
| MF_battery_removable / MF_battery_included / MF_battery_count | Battery facts | Booleans and integer |
| CMP_dangerous_goods | Transport declaration | Record per CDS-1900 §12 (UN 3480/3481 lithium-ion, 3090/3091 lithium metal, 3551/3552 sodium-ion, and others) |
| MF_charging_port / MF_charging_power_min_w / MF_charging_power_max_w / MF_usb_pd_supported / MF_charger_included | Charging capabilities as labelled | Governed value; typed watts; booleans |
| CMP_energy_ratings | Per-market energy or water rating records | List: jurisdiction, scheme (`energy_rating_system` dictionary), rating value or class, class range in force, registration identifier, label artefact reference, product information sheet reference, verification date |

**CDS1800-R025** Power source, input electrical characteristics and plug type MUST be governed or typed values; plug type MUST be variant-scoped where it defines the sellable unit.

**CDS1800-R026** Battery chemistry MUST be a governed value and battery capacity MUST be a typed measurement in watt-hours (with milliampere-hours and voltage where labelled) for every product containing or supplied with a battery; these values MUST be present before a dangerous-goods declaration is made.

**CDS1800-R027** Every product containing or packed with a lithium or sodium-ion battery MUST carry a dangerous-goods declaration per CDS-1900 §12 before publication to a channel or carrier that ships it; the declaration MUST distinguish batteries contained in equipment, packed with equipment and shipped alone, and MUST NOT be inferred from category.

**CDS1800-R028** Energy and water ratings MUST be stored as per-market records with the scheme, the rating value or class, the class range in force for the scheme (where a scheme uses a range), the registration identifier where the scheme registers models, and a reference to the label artefact and product information sheet; a rating MUST NOT be stored as a single global number or as a marketing claim.

**CDS1800-R029** Where a market requires the energy label, class arrow, product information sheet or rating icon to be shown online close to the price (Appendix D), the channel projection for that market MUST include the required artefact or class-and-range display, generated from the rating record, and verification MUST cover it.

**CDS1800-R030** Charging capabilities required to be labelled in a market (charging port standard, minimum and maximum charging power, protocol support, whether a charger is included) MUST be typed attributes and, where the market requires the pictogram or label online close to the price, MUST be projected and verified for that market.

**CDS1800-R031** A regulated energy or water rating MUST derive from the scheme's registration or supplier documentation (E1); it MUST NOT be estimated or copied from a similar model.

**CDS1800-R032** Efficiency programme membership that is voluntary in a market (for example a certification programme) is a certification claim under R023, not a rating; the `energy_rating_system` dictionary marks such schemes as evidence-gated.

## 9. Physical Attributes, Installation and Packaging *(normative)*

**CDS1800-R033** Product dimensions and weight MUST be typed measurements distinguishing the product (with and without stand or accessories where relevant) from the packaged unit; packaged dimensions and weight MUST be present for products published to channels that compute shipping.

**CDS1800-R034** Installation and mounting types MUST be governed values (`installation_type` dictionary; mounting standards such as display-mount patterns as governed specifications).

**CDS1800-R035** Delivery class (parcel, oversized, two-person, installation required) MUST be a governed logistics attribute where the organisation ships the product, derived from packaged measurements and category rules, not authored per product.

## 10. Contents, Kits and Accessories *(normative)*

**CDS1800-R036** Items included in the box MUST be represented as `includes` relationship records with quantities (CDS-1900 §11), not only as a descriptive list, so that channel content, warranty and returns processes can rely on them.

**CDS1800-R037** Bundles combining a device with accessories or services MUST be modelled as kits with component relationships per CDS-1900 §11, with each component retaining its own identity, specifications and compliance records.

## 11. Condition, Warranty, Lifecycle and Repair *(normative)*

| Field | Meaning | Type |
|---|---|---|
| MF_condition | Governed value (`product_condition` dictionary: new, refurbished, remanufactured, used) | Variant |
| MF_refurbished_grade | Organisation-governed grade where condition is refurbished | Governed value |
| MF_warranty_months / MF_warranty_type / MF_warranty_provider | Warranty term, type (manufacturer, retailer, extended) and provider, per market | Per-market records |
| MF_software_support_until | Declared operating-system or security update period | Date |
| MF_spare_parts_availability_years / MF_repairability_class | Repair information where a market requires or scores it | Typed values with scheme |

**CDS1800-R038** Condition MUST be a governed value at variant scope; a refurbished or used product MUST NOT share a variant with a new one, and channels that require a condition attribute MUST receive it from this value.

**CDS1800-R039** Warranty MUST be stored per market as typed records; a warranty statement in a description MUST derive from the record.

**CDS1800-R040** Where a market requires repair, spare-part availability or software-support information to be made available (Appendix D), the information MUST be a typed attribute with the scheme and MUST be projected for that market.

**CDS1800-R041** Product recalls and safety withdrawals MUST be expressed through lifecycle state and channel withdrawal (CDS-500 §12), with the affected serial or batch range recorded as an observation, never by deleting the product.

**CDS1800-R042** Region locking, regional software or regional service restrictions MUST be governed variant attributes evaluated at preflight for the target market.

## 12. Compliance, Safety Marks and Technical Documentation *(normative)*

| Field | Meaning | Type |
|---|---|---|
| CMP_compliance_declarations | Per-market compliance records | List: jurisdiction, scheme (`regulatory_scheme` dictionary), obligation type, mark or marking applied, registration or certificate identifier, responsible supplier or economic operator, declaration of conformity reference, evidence, status, dates |
| CMP_responsible_person | Responsible supplier, importer, authorised representative or economic operator per market | Per-market record |
| CMP_product_identifier | Type, batch or serial identification element required by a market | Governed attribute |
| MED_technical_documents | Typed document set | Records: type (user manual, quick start, specification sheet, declaration of conformity, energy label, product information sheet, safety data sheet, test summary), language, version, URL or asset reference |
| MF_warning_statements | Mandatory warnings per market (for example button-battery warnings) | Structured statement records with scheme |

**CDS1800-R043** Compliance with a market's electrical-safety, electromagnetic-compatibility, radio, energy, water, battery, take-back or general-safety regime MUST be a governed compliance record per market referencing the scheme and its evidence; a conformity mark in an image or a phrase in a description MUST NOT be treated as the compliance fact.

**CDS1800-R044** Compliance declarations and conformity marks MUST NOT be projected as customer facets or claims unless fed by accepted records; they MAY be displayed as information where the market requires or permits it.

**CDS1800-R045** Technical documents MUST be typed media records (MED_) with language and version, linked to the product or variant they describe; documents a market requires to be made available online (Appendix D) MUST be projected for that market and their presence verified.

**CDS1800-R046** Mandatory warnings applying to a product type in a market (for example products containing button or coin batteries) MUST be structured statement records evaluated per market at preflight and projected to the market's listing where the market requires or recommends an online warning.

**CDS1800-R047** Where a market requires a battery test summary, a declaration of conformity or a product information sheet to be available to purchasers on request or online, the document reference MUST be present in `MED_technical_documents` before publication to that market.

## 13. Customer Facet Design *(informative — normative facet rules live in CDS-600)*

| Facet | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Brand | Governed brand dictionary | Supplier spellings |
| Specification ranges (screen size, capacity, wattage) | Numeric range facets with units (CDS600-R043) | Text buckets typed per product |
| Connectivity and standards | Governed dictionary values, multi-select OR | Free-text feature lists |
| Compatibility ("works with") | Fed by relationship records; target-model facets only where the catalogue supports them | Tags such as "iphone-compatible" |
| Energy rating | Per-market facet from rating records; display class and range as the market requires | A global star facet applied to every market |
| Condition | Governed condition values | "Like new" free text |
| Installation type | Governed values | — |

## 14. Channel Projection Guidance *(informative — normative rules: CDS-500, CDS-900)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Specifications | Category metafields where the taxonomy defines them (connectivity, display technology, battery, compatibility attributes exist for many electronics categories), custom metafields otherwise; verified by read-back | `product_detail` name/value pairs; identifiers `brand`, `gtin`, `mpn`, `identifier_exists` |
| Compatibility | Relationship projections (complementary-product and compatibility metafields where supported) | Not a standard feed field in the seeded channels; title and product_detail |
| Energy rating | Per-market metafield plus label artefact; nested class arrow for markets that require it | `energy_efficiency_class` and related attributes are accepted only for specific countries in the Google profile (verified 2026-09-20: Switzerland, Norway, UK); `certification` attribute for EU energy labels — dated facts in CDS-900 |
| Condition | Condition metafield or variant option | `condition` (new / refurbished / used) |
| Battery and transport | Fulfilment metafields; carrier declarations from the DG record | Not published to consumers; carrier integration |
| Warnings and compliance information | Per-market generated blocks; verified | Description blocks where policy allows |

## 15. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Specification extraction from specification sheets (E1) | Typed candidates with units | Unit and range validation; provenance required (R018); conflicts surfaced (R019) |
| Standards and version normalisation | Dictionary candidates | Governed dictionary; unknown versions quarantined |
| Compatibility proposals | Candidate relationships with evidence | Never accepted without evidence and review (R022) |
| Energy and battery data | None — regulatory database or supplier document only | R031, R026 |
| Market obligation gaps | Candidate register entries triggered by category and attributes | Register evaluation deterministic |

## 16. Governance and Organisational Extensions *(informative — rules in CDS-1500 §23 and CDS-800)*

Specification sets per category are organisational schema decisions governed under CDS-800 §23 with impact assessment on facets, channels and comparison. External specification models (ETIM classes and features, GS1 GPC brick attributes, marketplace category attributes) may be adopted as the source of a category's specification set through Taxonomy Mappings and attribute crosswalks (CDS-1900 §8). The jurisdiction requirement register for electrical goods changes frequently (energy-label rescaling, battery regulation phase-ins, charger rules) and is reviewed on the declared cadence with a mandatory review on each market change.

## 17. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS1800-R048** An implementation claiming the CDS Electronics Profile MUST: govern brand, manufacturer part number and trade identifiers with declared schemes and explicit identifier-absence (R009–R011); store every exposed specification as a typed, unit-bearing Attribute Definition value with a declared category specification set, basis qualifiers and provenance (R014–R019); express compatibility, inclusion, family and successor relationships as governed relationship records (R007, R020–R022, R036–R037); store power, battery and per-market energy or water ratings as typed and governed records with dangerous-goods declarations for battery products (R025–R032); store condition, warranty and lifecycle as governed values (R038–R042); maintain per-market compliance records, responsible-person records, typed technical documents and mandatory warnings (R043–R047); maintain and evaluate a jurisdiction requirement register for every market published to (R003); apply category-specific requirements per CDS1500-R009; and publish and verify channel representations under CDS-500, including market-mandated online label and information displays (R029, R030, R045).

**CDS1800-R049** An Electronics Profile claim MUST state which markets its register covers and whether battery-containing products and large appliances are in scope.

## 18. Worked Product Examples *(informative)*

### 18.1 Television sold in Australia and the EU

```
STD_brand = Example Electronics; SUP_manufacturer_part_number = X65Q
CAT_product_type = television
MF_screen_size_in = 65; MF_screen_technology = oled; MF_resolution = {3840, 2160}; MF_refresh_rate_hz = 120
MF_connectivity = [hdmi, wifi, bluetooth, ethernet]; MF_hdmi_port_count = 4; MF_hdmi_version = hdmi_2_1
MF_power_consumption_w = 180; MF_installation_type = freestanding (wall_mounted supported; mount pattern 300x300)
CMP_energy_ratings =
  [{jurisdiction: AU, scheme: au_energy_rating, value: 4.5, registration_id: <GEMS registration>, label_ref: MED-.., verified: 2026-09-20},
   {jurisdiction: EU, scheme: eu_energy_label, class: F, class_range: "A-G", eprel_id: <EPREL model id>, label_ref: MED-.., pis_ref: MED-..}]
CMP_compliance_declarations =
  [{jurisdiction: AU, scheme: au_eess_rcm, level: 2, registration: <EESS>, responsible_supplier: ...},
   {jurisdiction: AU, scheme: au_acma_rcm, ...},
   {jurisdiction: EU, scheme: eu_ce_marking_electrical, directives: [LVD, EMC, RED, RoHS], doc_ref: MED-..},
   {jurisdiction: EU, scheme: eu_weee_2012_19, marking: crossed_out_bin, producer_registration: ...}]
Variant AU: VAR_plug_type = AU; VAR_gtin = 09300000000010
Variant EU: VAR_plug_type = EU; VAR_gtin = 04000000000017
EU projection: class arrow "F" with range A-G adjacent to price; link labelled "Product Information Sheet" -> verified
AU projection: Energy Rating Icon generated from the registration data -> verified
```

### 18.2 Wireless earbuds with charging case

```
CAT_product_type = wireless_earbuds
MF_connectivity = [bluetooth]; MF_bluetooth_version = bluetooth_5_3
MF_battery_chemistry = lithium_polymer
MF_battery_capacity_wh = 0.2 (each earbud); MF_case_battery_capacity_wh = 1.9
MF_battery_removable = false; MF_charging_port = usb_c; MF_charger_included = false
CMP_dangerous_goods = {regulated: true, un_number: "UN3481", proper_shipping_name: "Lithium ion batteries packed with equipment",
                       class: "9", watt_hours_per_battery: 1.9, transport_modes: [road, air], test_summary_ref: MED-..}
CMP_compliance_declarations = [{jurisdiction: EU, scheme: eu_common_charger_2022_2380, pictogram: charger_not_included,
                                charging_label: {min_w: 3, max_w: 5, usb_pd: false}}, ...]
EU projection: charger pictogram and charging label shown close to the price -> verified
```

### 18.3 Dishwasher with energy and water ratings

```
CAT_product_type = dishwasher
MF_installation_type = freestanding; MF_capacity_place_settings = 14
MF_dimensions_mm = {h: 850, w: 600, d: 600}; MF_packaged_weight_kg = 52; MF_delivery_class = two_person
CMP_energy_ratings =
  [{jurisdiction: AU, scheme: au_energy_rating, value: 4.0, registration_id: ...},
   {jurisdiction: AU, scheme: wels_water_rating, value: 5.5, registration_id: ...},
   {jurisdiction: CA, scheme: ca_energuide, annual_kwh: 240, verification_mark: <certification body>},
   {jurisdiction: US, scheme: us_ftc_energyguide, label_ref: MED-.., annual_cost_usd: 30}]
US projection: EnergyGuide label image or icon hyperlink close to the price -> verified
```

## 19. Reference Validation Cases *(informative — the profile's contribution to the cross-industry validation set, REVIEW-020)*

- a specification present only in description text, which must count as unpopulated (R014);
- two eligible sources disagreeing on battery capacity, which must surface a conflict (R019);
- an accessory whose compatibility is asserted only by a tag, which must fail (R020);
- a lithium-battery product lacking watt-hours or a dangerous-goods declaration, which preflight must block for shipping channels (R026–R027);
- a single global "energy rating" number offered to two markets with different schemes, which must not satisfy either (R028);
- an EU listing without the class arrow and product information sheet link, which verification must report (R029);
- a refurbished unit sharing a variant with a new unit (R038);
- a product containing a button battery published to Australia without the mandated warning text in the listing (R046, D-AU-5);
- a phone published to the EU after 20 June 2025 without its energy label and repairability class (D-EU-3);
- a manufacturer part number overwritten by a retailer SKU (R010).

---

## Appendix A. Electronics Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| STD_brand / SUP_manufacturer_part_number / VAR_gtin / MF_identifier_exists | Product / Variant | Governed identity values | R |
| CAT_product_type | Product | Governed classification reference | R |
| Category specification set | Product / Variant | Typed Attribute Definitions per category profile | Per category profile (R/C/REC/O) |
| MF_connectivity | Product | Governed dictionary list | R where the product has interfaces |
| MF_screen_technology / MF_screen_size_in / MF_resolution | Product | Governed value; typed measurements | R for display products |
| MF_power_source / MF_input_voltage_range_v / VAR_plug_type / MF_rated_power_w | Product / Variant | Governed and typed values | R for mains-powered products |
| MF_battery_chemistry / MF_battery_capacity_wh / MF_battery_removable / MF_battery_included | Product / Variant | Governed value; typed measurement; booleans | R for battery products |
| CMP_dangerous_goods | Product / Variant | Declaration per CDS-1900 §12 | R for battery and other regulated products |
| MF_charging_port / MF_charging_power_min_w / MF_charging_power_max_w / MF_charger_included | Product | Governed and typed values | C — R where a market mandates charging labelling |
| CMP_energy_ratings | Product / Variant (per market) | Rating records (`energy_rating_system` dictionary) | R where a market regulates the product type |
| MF_installation_type | Product | Governed dictionary reference | REC; R for appliances |
| MF_dimensions / MF_weight / packaged equivalents | Product / Variant | Typed measurements | R |
| Relationship records (`compatible_with`, `includes`, `accessory_for`, `requires`, `successor_of`) | Product | Records per CDS-1900 §5 | C — R where compatibility or contents are published |
| MF_condition | Variant | Governed dictionary reference (`product_condition`) | R |
| MF_warranty_months / MF_warranty_type / MF_warranty_provider | Product (per market) | Typed records | REC; R where a market requires warranty disclosure |
| CMP_compliance_declarations / CMP_responsible_person / CMP_product_identifier | Product (per market) | Governed records | R where a market regulates the product |
| MED_technical_documents | Product / Variant | Typed media records | REC; R where a market requires online availability |
| MF_warning_statements | Product | Structured statement records | C — R where a market mandates a warning |
| MF_spare_parts_availability_years / MF_repairability_class / MF_software_support_until | Product | Typed values with scheme | C |

## Appendix B. Dictionary Bindings *(informative — becomes governed data on adoption per CDS1500-R011)*

| Dictionary key | Package chapter | Bound attribute(s) | Status at 0.8.0 |
|---|---|---|---|
| connectivity | 11 | MF_connectivity and interface versions | Bound by this profile |
| screen_technology | 11 | MF_screen_technology | Bound |
| power_source | 11 | MF_power_source | Bound |
| installation_type | 11 | MF_installation_type | Bound |
| energy_rating_system | 11 | CMP_energy_ratings.scheme | Bound |
| battery_chemistry | 11 (new, 0.8.0) | MF_battery_chemistry | Bound |
| product_condition | 18 (new, 0.8.0) | MF_condition | Bound (shared with CDS-1900) |
| relationship_type | 18 (new, 0.8.0) | Relationship records | Bound via CDS-1900 §5 |
| dangerous_goods_class | 18 (new, 0.8.0) | CMP_dangerous_goods | Bound via CDS-1900 §12 |
| jurisdiction / regulatory_scheme | 19 (new, 0.8.0) | CMP_* records | Bound via CDS-1500 §2.2 |

Deliberately not shipped: per-category specification sets (adopt ETIM, GS1 GPC or marketplace attribute sets under CDS-1900 §8), brand dictionaries, mount-pattern and connector registries beyond the connectivity vocabulary, vendor ecosystem lists (excluded by the package rules).

## Appendix C. References *(informative; retrieved 2026-09-20 unless stated)*

| Ref | Source | Location | Use in this chapter |
|---|---|---|---|
| [E1] | EESS — Registration of in-scope electrical equipment; Marking of electrical equipment; In-scope equipment definitions and risk levels v4.3 (2024); ACMA requirements — use of RCM | eess.gov.au | AU Levels 1–3 registration, RCM marking, responsible supplier (D-AU-1, D-AU-2) |
| [E2] | Energy Rating (energyrating.gov.au) — Displaying the label and icon; Register a product | energyrating.gov.au | AU/NZ GEMS registration, mandatory label products, online icon (D-AU-3) |
| [E3] | ACCC Product Safety — Button and coin batteries mandatory standards; Products containing button/coin batteries information standard (2026-02-19); Consumer Goods (Products Containing Button/Coin Batteries) Safety and Information Standards 2020 | productsafety.gov.au; legislation.gov.au | Secure compartments, warnings on packaging, instructions and online listings (D-AU-5) |
| [E4] | WorkSafe New Zealand — Supplier declaration of conformity; High and medium risk products; Electrical safety compliance; Electricity (Safety) Regulations 2010 reg 83 (as at 2026-01-15); RSM Step 4 (SDoC) | worksafe.govt.nz; legislation.govt.nz; rsm.govt.nz | NZ declared medium/high risk articles, SDoC, RCM, radio SDoC (D-NZ-1, D-NZ-2) |
| [E5] | FCC — Equipment Authorization: RF Device; KDB 784748 D01 (labelling) and D02 (e-labelling) | fcc.gov; apps.fcc.gov | SDoC and certification labelling, FCC ID, e-labels (D-US-1) |
| [E6] | FTC — 16 CFR 305.27 Paper catalogs and websites; EnergyGuide Labeling FAQs | ecfr.gov; ftc.gov | EnergyGuide label or icon online near price (D-US-2) |
| [E7] | OEHHA — Proposition 65 warnings for internet purchases (regulations effective 2025-01-01) | oehha.ca.gov; p65warnings.ca.gov | Online warning before purchase (D-US-3) |
| [E8] | California SB 244 Right to Repair Act (Public Resources Code 42488–42488.3), operative 2024-07-01 | leginfo.legislature.ca.gov | Parts, tools and documentation availability 3 or 7 years (D-US-4) |
| [E9] | European Commission — EPREL: Dealers; Suppliers; Commission Implementing Regulation (EU) 2024/994; Dealers webinar on smartphones and slate tablets (June 2025) | energy-efficient-products.ec.europa.eu | Online label and product information sheet display, nested arrow, QR (D-EU-2, D-EU-3) |
| [E10] | Commission Delegated Regulation (EU) 2023/1669 (energy labelling of smartphones and slate tablets); Commission Regulation (EU) 2023/1670 (ecodesign) | eur-lex.europa.eu | Label content, repairability class, spare parts and information requirements from 20 June 2025 (D-EU-3) |
| [E11] | Regulation (EU) 2023/1542 concerning batteries (consolidated 2024-07-18) | eur-lex.europa.eu | Separate collection symbol from 18 August 2025, general label from 18 August 2026, QR code from 18 February 2027 (D-EU-4) |
| [E12] | Directive (EU) 2024/884 amending the WEEE Directive 2012/19/EU (marking per EN 50419:2022) | eur-lex.europa.eu | Crossed-out wheeled bin marking (D-EU-5) |
| [E13] | Regulation (EU) 2023/988 General Product Safety Regulation (applies from 13 December 2024) | eur-lex.europa.eu | Traceability, responsible economic operator, online offer information (D-EU-6) |
| [E14] | Directive (EU) 2022/2380 (common charger) | eur-lex.europa.eu | USB-C receptacle, charging label and pictogram close to the price in distance selling from 28 December 2024 (laptops from 28 April 2026) (D-EU-7) |
| [E15] | Regulation (EU) 2024/1781 Ecodesign for Sustainable Products (ESPR) | eur-lex.europa.eu | Digital product passport framework, dealer obligations in distance selling (D-EU-8) |
| [E16] | GOV.UK — Placing UKCA or CE marked products on the market in Great Britain (2026-03-31); Product regulations by sector (2026-03-31); Electrical Equipment (Safety) Regulations 2016 guidance; Product Safety and Metrology etc. (Amendment) Regulations 2024 explanatory memorandum | gov.uk; legislation.gov.uk | Indefinite CE recognition from 1 October 2024, UKCA labelling flexibilities to 31 December 2027, manufacturer and importer labelling (D-UK-1) |
| [E17] | The Waste Electrical and Electronic Equipment Regulations 2013 (as amended to 2025-02-27) | legislation.gov.uk | Distance-seller producer obligations, crossed-out bin and date mark (D-UK-2) |
| [E18] | Natural Resources Canada — Introduction to the Regulations (2026-06-19); EnerGuide label for appliances; Energy Efficiency Regulations, 2016 (SOR/2016-311) ss. 4, 5, 13; Energy Efficiency Act s. 4 | natural-resources.canada.ca; laws-lois.justice.gc.ca | Verification mark, energy efficiency report, EnerGuide label products (D-CA-1) |
| [E19] | CSA Group — US/Canada (FCC/ISED) certification for household appliances (2019) | csagroup.org | ISED SDoC and IC certification pattern (D-CA-2; retrieved) |
| [E20] | IATA — Lithium Battery Guidance Document (2026 edition) | iata.org | UN numbers 3480/3481/3090/3091/3551/3552, 30% state of charge, test summary availability (§8) |
| [E21] | ECDB — Amazon product categories by revenue 2025; secondary reporting of Statista Market Insights ecommerce revenue by segment (2026) | ecdb.com; statista.com | Market basis (REVIEW-020) |

## Appendix D. Jurisdiction Requirement Register — Seed *(informative seed of the normative register defined in CDS-1500 §2.2)*

Conventions as in CDS-1600 Appendix D.

### D.1 Australia (AU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-1 | Electrical Equipment Safety System (EESS) under state and territory electrical safety laws; AS/NZS 4417 — ERAC/state regulators (`au_eess_rcm`) | In-scope electrical equipment (household-type, ≤ certain ratings) sold in participating jurisdictions | pre_market (responsible supplier registration; Level 2 and 3 equipment registration in the national database; Level 3 certificate of conformity); labelling_element (RCM marking) | Responsible supplier registration; equipment level (1/2/3); equipment registration and, for Level 3, certificate of conformity; compliance folder or evidence of compliance with the relevant standard; RCM marked per AS/NZS 4417.1 near the model identification → CMP_compliance_declarations (scheme `au_eess_rcm`, level, registration, certificate), CMP_responsible_person, marking flag | Ongoing; Level 3 registrations for 1, 2 or 5 years | Verified 2026-09-20 [E1] |
| D-AU-2 | Radiocommunications (Compliance Labelling) notices incl. EMC Notice 2017 — ACMA (`au_acma_rcm`) | Radiocommunications, EMC, telecommunications and EME-regulated devices | pre_market (responsible supplier registration on the national database); labelling_element (RCM); documentation (compliance records) | Supplier registration (ACMA-only registration has no fee); compliance level 1/2/3 (ACMA levels do not correlate with EESS levels); RCM applied; compliance records held → CMP_compliance_declarations (scheme `au_acma_rcm`, level), CMP_responsible_person | Ongoing | Verified 2026-09-20 [E1] |
| D-AU-3 | Greenhouse and Energy Minimum Standards (GEMS) Act 2012 and product determinations — Energy Rating (`au_gems_energy_rating`) | Regulated products (clothes dryers, washers, dishwashers, refrigerators and freezers, televisions, computer monitors, air conditioners up to 30 kW, pool pumps and other MEPS products) | pre_market (registration before supply); rating_label (label in stores; icon for online sales) | Registration in the Energy Rating Product Registration System (brand, model number, energy performance); Energy Rating Label displayed when supplying in Australian retail stores; the Energy Rating Icon may be used online and in advertising and can be generated from the regulated product data extract → CMP_energy_ratings (scheme `au_energy_rating`, star rating, annual kWh, registration id, icon artefact) | Ongoing; cancelled registrations on determination updates | Verified 2026-09-20 [E2] |
| D-AU-4 | Water Efficiency Labelling and Standards (WELS) Act 2005 (`au_wels_water_rating`) | Washing machines, dishwashers, taps, showers, toilets, urinals, flow controllers | pre_market (registration); rating_label | WELS registration; star rating and water consumption on the label; display of the label or rating in advertising and online → CMP_energy_ratings (scheme `wels_water_rating`) | Ongoing | Retrieved (not spot-verified) |
| D-AU-5 | Consumer Goods (Products Containing Button/Coin Batteries) Safety Standard 2020 and Information Standard 2020; Consumer Goods (Button/Coin Batteries) Safety and Information Standards 2020 — ACCC (`au_button_battery_standards_2020`) | Consumer goods containing or supplied with button or coin batteries; button and coin batteries | pre_market (compliance testing of representative samples); labelling_element; warning_statement; listing_element (recommended) | Secure battery compartment (tool or two independent movements) for consumer-replaceable batteries; batteries must not release under foreseeable use or misuse; captive fasteners; warnings in instructions, on packaging (safety alert symbol on the front panel) or attached to unpackaged goods covering: alert word, symbol, hazard and keep-away statement, lithium 2-hour severe-injury statement or non-lithium serious-injury statement, seek-immediate-medical-attention advice; child-resistant packaging for batteries; online listings should include the warning in the product description → MF_battery_chemistry (button/coin form), MF_warning_statements (scheme `au_button_battery_standards_2020`), CMP_compliance_declarations (test evidence), listing projection | Mandatory from 22 June 2022 | Verified 2026-09-20 [E3] |
| D-AU-6 | Australian Dangerous Goods Code 7.9 (lithium batteries UN 3480/3481 etc.) (`au_adg_code_7_9`) | Battery products for road and rail transport | transport | Dangerous-goods declaration per CDS-1900 §12 | Mandatory from 1 October 2025 | Verified 2026-09-20 (CDS-1900 Appendix C) |

### D.2 New Zealand (NZ)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-1 | Electricity (Safety) Regulations 2010 regs 81–86A — WorkSafe Energy Safety (`nz_electricity_safety_regulations_2010`) | Declared medium-risk articles (SDoC required; list includes lithium-ion/polymer batteries) and declared high-risk articles (approval or recognised certification, or EESS registration by an NZ-registered responsible or affiliated supplier deemed approval) | pre_market; documentation (SDoC available to purchasers on request within 10 days) | Supplier Declaration of Conformity (description, standard cited from Schedule 4 or AS/NZS 3820, ISO/IEC 17050-1 form) with supporting test report; approval number or RCM on high-risk articles; SDoC available to consumers and to WorkSafe within 10 days → CMP_compliance_declarations (scheme `nz_electricity_safety_regulations_2010`, article class, SDoC reference), MED_technical_documents (SDoC, test report) | Ongoing | Verified 2026-09-20 [E4] |
| D-NZ-2 | Radiocommunications Act 1989 supplier compliance — RSM (`nz_rsm_sdoc`) | Radio and EMC products | pre_market (SDoC per product or significant variation); labelling_element (R-NZ mark or RCM) | SDoC for Level of Conformity 1 radio products and all Level 2, 3, A1–A3 products; Australian SDoC recognised under the mutual recognition notice → CMP_compliance_declarations (scheme `nz_rsm_sdoc`) | Ongoing | Verified 2026-09-20 [E4] |
| D-NZ-3 | Energy Efficiency (Energy Using Products) Regulations 2002 — EECA (`nz_eeca_meps`) | MEPS and MEPL regulated products | pre_market (registration in NZ or in Australia under trans-Tasman mutual recognition); rating_label | Registration and Energy Rating Label per the joint scheme; icon rules differ from Australia → CMP_energy_ratings (scheme `au_energy_rating`, jurisdiction NZ) | Ongoing | Verified in part 2026-09-20 [E2][E4] |

### D.3 United States (US, with California noted)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-1 | 47 CFR Parts 2, 15 and 18 equipment authorization — FCC (`us_fcc_equipment_authorization`) | RF devices: unintentional radiators (most digital devices) via Supplier's Declaration of Conformity; intentional radiators (transmitters) via certification | pre_market (SDoC or certification before marketing or import); labelling_element (FCC ID for certified devices; unique identification and compliance information statement for SDoC; e-labelling permitted with a temporary physical label); documentation (compliance statement, Part 15 user information) | FCC ID or SDoC compliance information (responsible party in the US, identification, statement), Part 15.19/15.105 statements in manuals or packaging, e-label access in ≤3 steps → CMP_compliance_declarations (scheme `us_fcc_equipment_authorization`, procedure, FCC ID, responsible party), MED_technical_documents | Ongoing | Verified 2026-09-20 [E5] |
| D-US-2 | Energy Labeling Rule, 16 CFR Part 305 (§305.27 websites and catalogs) — FTC (`us_ftc_energyguide`) | Covered products (refrigerators, freezers, room and portable air conditioners, clothes washers, dishwashers, ceiling fans, water heaters, pool heaters, central air conditioners, heat pumps, furnaces, televisions, lamps; plumbing products by text disclosure) | rating_label (EnergyGuide/Lighting Facts label); listing_element (websites) | Website pages with price and detailed description must display a recognisable, legible label image close to the price, or hyperlink via the FTC EnergyGuide icon without requiring download; manufacturers post labels online and report data via DOE CCMS → CMP_energy_ratings (scheme `us_ftc_energyguide`, annual cost or efficiency, label artefact), listing projection | Website display since 15 January 2014 | Verified 2026-09-20 [E6] |
| D-US-3 | Proposition 65 (California), 27 CCR 25602–25603 — OEHHA (`us_ca_prop65_warning`) | Products exposing California consumers to listed chemicals (common for cables, cords, batteries, plastics) | warning_statement; listing_element | Warning on the product display page, "WARNING" hyperlink or prominent pre-purchase warning; new short-form names a chemical per endpoint; 60-day online update window → MF_warning_statements (jurisdiction US-CA) | Effective 1 January 2025; transition to 1 January 2028 | Verified 2026-09-20 [E7] |
| D-US-4 | Right to Repair Act (California SB 244, PRC 42488) and comparable state laws (`us_right_to_repair_state`) | Electronic and appliance products first sold in California on or after 1 July 2021 with wholesale price ≥ US$50 | post_market (parts, tools and documentation for 3 years at US$50–99.99 wholesale, 7 years at ≥ US$100) | Availability of documentation, functional parts and tools on fair and reasonable terms; independent repairer notices → MF_spare_parts_availability_years (scheme `us_ca_sb244`), MED_technical_documents | Operative 1 July 2024; other states (for example New York, Minnesota, Oregon, Colorado) have their own effective dates — not seeded | Verified 2026-09-20 [E8] (California); other states retrieved (not spot-verified) |
| D-US-5 | DOE conservation standards and certification (10 CFR 429/430); UL/NRTL safety listing (voluntary but retailer-required); 49 CFR hazardous materials (batteries) | Appliances; electrical products; battery shipments | pre_market; documentation; transport | DOE certification in CCMS; NRTL listing marks; hazmat declarations → CMP_compliance_declarations, CMP_dangerous_goods | Ongoing | Retrieved (not spot-verified) |

### D.4 European Union (EU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-1 | Low Voltage Directive 2014/35/EU, EMC Directive 2014/30/EU, Radio Equipment Directive 2014/53/EU, RoHS Directive 2011/65/EU — CE marking (`eu_ce_marking_electrical`) | Electrical, electronic and radio equipment | pre_market (conformity assessment, EU declaration of conformity, technical file); labelling_element (CE marking; manufacturer and importer name, trade mark, postal address; type, batch or serial number) | CE marking; manufacturer and importer identification; product identification element; DoC available; instructions and safety information in the required language → CMP_compliance_declarations (scheme `eu_ce_marking_electrical`, directives, DoC ref), CMP_responsible_person, CMP_product_identifier, MED_technical_documents | Ongoing | Retrieved (not spot-verified this pass; directive texts not read) |
| D-EU-2 | Energy Labelling Regulation (EU) 2017/1369; product-specific delegated regulations; Commission Implementing Regulation (EU) 2024/994 (EPREL) (`eu_energy_label_2017_1369`) | Energy-labelled product groups (dishwashers, washing machines, washer-dryers, refrigerators, electronic displays, light sources, tyres, smartphones and tablets, and others) | pre_market (supplier registers the model in EPREL before placing on the market); rating_label; listing_element (dealers, including online stores) | Online stores must show the energy label and product information sheet close to the price (nested display permitted: class arrow pointing left, letter at least the size of the price, full label on click or hover; link named "Product Information Sheet" in the local language; also on list pages and basket pages); QR code readable; suppliers communicate the EPREL registration number to dealers; advertisements show class and range → CMP_energy_ratings (scheme `eu_energy_label`, class, range, EPREL id, label and PIS artefacts), listing projection and verification | Ongoing; EPREL implementing act 2024 | Verified 2026-09-20 [E9] |
| D-EU-3 | Commission Delegated Regulation (EU) 2023/1669 (energy labelling of smartphones and slate tablets) and Commission Regulation (EU) 2023/1670 (ecodesign) (`eu_smartphone_energy_label_2023_1669`) | Smartphones and slate tablets (labelling); also mobile and cordless phones (ecodesign) | rating_label; listing_element; post_market (spare parts, OS updates, repair information) | Label: energy efficiency class A–G and range, battery endurance per cycle, repeated free-fall reliability class, repairability class, battery endurance in cycles, ingress protection rating; product information sheet in EPREL; dealers show label and PIS online near the price; suppliers publish ingress rating, minimum battery endurance in cycles, recycled content, critical raw material ranges, and make spare parts available to professional repairers for 7 years after end of placement → CMP_energy_ratings (scheme `eu_smartphone_energy_label_2023_1669`, class, endurance, repairability class, IP rating), MF_spare_parts_availability_years, MF_repairability_class, MED_technical_documents | Units placed on the market from 20 June 2025 | Verified 2026-09-20 [E9][E10] |
| D-EU-4 | Regulation (EU) 2023/1542 concerning batteries and waste batteries (`eu_batteries_2023_1542`) | Batteries, including batteries incorporated in appliances, sold by distance contracts | labelling_element; documentation; post_market (producer responsibility; distance sellers established elsewhere are producers) | Separate collection symbol on all batteries from 18 August 2025; general information label from 18 August 2026; QR code linking to information (and, for certain batteries, the battery passport) from 18 February 2027; carbon footprint declaration accompanying industrial and EV batteries until accessible via QR; producer registration → CMP_compliance_declarations (scheme `eu_batteries_2023_1542`, markings applied, producer registration), MF_battery_chemistry, MF_battery_capacity_wh | Phased 2025–2027 | Verified 2026-09-20 [E11] |
| D-EU-5 | WEEE Directive 2012/19/EU as amended by Directive (EU) 2024/884 (`eu_weee_2012_19`) | Electrical and electronic equipment | labelling_element (crossed-out wheeled bin per EN 50419:2022, date mark); post_market (producer registration, distance sellers via authorised representative) | Crossed-out bin marking (on packaging, instructions and warranty only in exceptional cases); producer registration number per member state → CMP_compliance_declarations (scheme `eu_weee_2012_19`) | Ongoing | Verified 2026-09-20 [E12] |
| D-EU-6 | Regulation (EU) 2023/988 General Product Safety Regulation (`eu_gpsr_2023_988`) | All consumer products (cross-cutting distance-selling duties also for harmonised products) | listing_element; labelling_element; pre_market (responsible economic operator established in the EU) | Product bears type, batch or serial number and manufacturer name, trade mark, postal and electronic address (importer details where applicable); online offers show the manufacturer's (or responsible operator's) name, address and contact, product identification information, warnings and safety information, and a picture; warnings and instructions in a language easily understood; traceability records 6 years → CMP_responsible_person, CMP_product_identifier, MF_warning_statements, listing projection | Applies from 13 December 2024 | Verified 2026-09-20 [E13] |
| D-EU-7 | Directive (EU) 2022/2380 amending the Radio Equipment Directive (common charger) (`eu_common_charger_2022_2380`) | Handheld mobile phones, tablets, cameras, headphones, headsets, handheld videogame consoles, portable speakers, e-readers, keyboards, mice, navigation systems, earbuds (from 28 December 2024); laptops (from 28 April 2026) rechargeable by wired charging | labelling_element; listing_element | USB Type-C receptacle; label with charging specifications (minimum and maximum power in watts, USB PD support) printed in the instructions and on packaging; pictogram indicating whether a charging device is included; in distance selling the pictogram and label displayed close to the price → MF_charging_port, MF_charging_power_min_w, MF_charging_power_max_w, MF_usb_pd_supported, MF_charger_included, listing projection | 28 December 2024; laptops 28 April 2026 | Verified 2026-09-20 [E14] |
| D-EU-8 | Regulation (EU) 2024/1781 Ecodesign for Sustainable Products (ESPR) and delegated acts (`eu_espr_2024_1781`) | Product groups as delegated acts are adopted (digital product passport, labels, unsold-goods rules) | listing_element; documentation | Dealers and online marketplaces make the data carrier or unique product identifier accessible to potential customers in distance selling; labels displayed as delegated acts specify → CMP_product_identifier (DPP link), MED_technical_documents | Framework in force 18 July 2024; obligations per delegated act | Verified 2026-09-20 [E15] (framework); product-group acts not seeded |

### D.5 United Kingdom (GB)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-1 | Electrical Equipment (Safety) Regulations 2016; Electromagnetic Compatibility Regulations 2016; Radio Equipment Regulations 2017; RoHS Regulations 2012; Product Safety and Metrology etc. (Amendment) Regulations 2024 — OPSS (`uk_electrical_equipment_regulations_ukca_ce`) | Electrical, electronic and radio equipment placed on the GB market | pre_market (UK or EU declaration of conformity; UKCA or CE marking — CE recognition continued indefinitely from 1 October 2024; "Fast-Track UKCA" on EU conformity assessment); labelling_element (manufacturer name, registered trade name or mark, postal address, type/batch/serial; importer details, which may be on packaging or documents until 31 December 2027; UKCA on a label or accompanying document permitted until 31 December 2027) | Conformity marking choice, DoC reference, manufacturer and importer identification, product identifier → CMP_compliance_declarations (scheme `uk_electrical_equipment_regulations_ukca_ce`), CMP_responsible_person, CMP_product_identifier | CE recognition indefinite from 1 October 2024; labelling flexibilities to 31 December 2027 | Verified 2026-09-20 [E16] |
| D-UK-2 | The Waste Electrical and Electronic Equipment Regulations 2013 (as amended, incl. online marketplace provisions 2025) — Environment Agency (`uk_weee_2013`) | EEE placed on the UK market, including by distance sellers established outside the UK and via online marketplaces | labelling_element (crossed-out wheeled bin; date mark); post_market (producer scheme membership; distributor take-back) | Crossed-out bin symbol and post-13 August 2005 date mark; producer registration; distributor take-back or scheme membership → CMP_compliance_declarations (scheme `uk_weee_2013`) | Ongoing; marketplace provisions 2025 | Verified 2026-09-20 [E17] |
| D-UK-3 | Energy Information Regulations 2011 (GB energy label) and Ecodesign for Energy-Related Products Regulations 2010 (`uk_energy_information_2011`) | Energy-labelled product groups | rating_label; listing_element | GB energy label and product information sheet displayed online close to the price in the same manner as the EU scheme (UK label, no EPREL) → CMP_energy_ratings (scheme `uk_energy_label`, existing `energy_rating_system` value) | Ongoing; CE recognition for ecodesign continued from 1 October 2024 | Retrieved 2026-09-20 [E16] (sector table); regulation text not read |
| D-UK-4 | Waste Batteries and Accumulators Regulations 2009; Batteries and Accumulators (Placing on the Market) Regulations 2008 — Defra (`uk_batteries_2009`) | Batteries and battery-containing products | labelling_element (crossed-out bin); post_market (producer registration; distributor take-back) | Markings and producer registration; no conformity marking required in GB (EU battery CE marking applies only in Northern Ireland) → CMP_compliance_declarations (scheme `uk_batteries_2009`) | Ongoing; UK considering its approach to the EU regulation | Retrieved 2026-09-20 [E16] (sector table) |

### D.6 Canada (CA)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-CA-1 | Energy Efficiency Act (S.C. 1992, c. 36) and Energy Efficiency Regulations, 2016 (SOR/2016-311) — Natural Resources Canada (`ca_energy_efficiency_regulations_2016`) | Regulated energy-using products imported or shipped between provinces for sale or lease (appliances, water heaters, HVAC, lighting, electronics, commercial equipment) | pre_market (energy efficiency report to NRCan before import or interprovincial shipment; product meets the standard; energy efficiency verification mark from an SCC-accredited certification body or equivalent province); rating_label (bilingual EnerGuide label on clothes washers, dryers, dishwashers, refrigerators, freezers, ranges, room air conditioners and others; lighting labels; walk-in nameplates) | Verification mark (readily visible; on packaging for chargers, power supplies and lamps); energy efficiency report (product name, brand, model number, manufacturer, certification body); EnerGuide label with annual kWh (or CEER) attached before first retail sale; NRCan does not currently require labels to be posted online → CMP_energy_ratings (scheme `ca_energuide`, annual kWh, verification body), CMP_compliance_declarations (report reference) | Ongoing | Verified 2026-09-20 [E18] |
| D-CA-2 | Radio Standards Specifications and ICES standards — ISED (`ca_ised_radio_equipment`); electrical product safety certification required by provincial and territorial electrical safety authorities (`ca_electrical_safety_certification`) | Radio equipment (IC certification or SDoC per RSS/ICES); electrical products (certification mark from an accredited body before sale in each province) | pre_market; labelling_element | IC certification number or SDoC statement; recognised certification mark (for example cCSAus, cULus) → CMP_compliance_declarations | Ongoing | Retrieved 2026-09-20 [E19] (not spot-verified against ISED or provincial authorities) |
| D-CA-3 | Consumer Packaging and Labelling Act and Regulations; Canada Consumer Product Safety Act — CFIA/Health Canada | Prepackaged consumer products | labelling_element | Bilingual product identity, net quantity and dealer identity; mandatory safety information → localisation dimension per CDS-300 §18, CMP_responsible_person | Ongoing | Retrieved (not spot-verified) |

### D.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Singapore (SG), Japan (JP), China (CN) | Energy-label schemes only | The `energy_rating_system` dictionary already carries `sg_energy_label`, `jp_energy_label` and `cn_energy_label`; safety, radio and transport regimes for those markets are not seeded. |
| Republic of Korea (KR), India (IN), Brazil (BR) and others | Not seeded | Organisation supplies entries with local advice (for example KC marking, BIS registration, INMETRO certification). |

END OF CDS-1800 v0.2 REVIEW DRAFT
