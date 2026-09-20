# Commerce Data Standard (CDS)
## CDS-1900 — Parts, Automotive, Industrial and Fitment Industry Profile

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5); chapter added in the 2026-09-20 industry-profile expansion |
| Date | 2026-09-20 |
| Supersedes | Nothing — first edition. Package Chapter 18 (Parts, Automotive & Industrial: relationship types, part origin types, product conditions, dangerous-goods classes) is shipped with this profile in package 0.8.0. |
| Normative status | §1, §3, §5–§14, §19 and Appendix A are normative. §2 (pointer), §4, §15–§18, §20, §21 and Appendices B–D are informative; Appendix D seeds the jurisdiction requirement register whose record structure and obligations are normative in CDS-1500 §2.2. Every table is individually marked. **This chapter is the single normative home (CDS000-R005) for three cross-industry mechanisms: the Product Relationship record (§5), kits, bundles and assemblies (§11) and the dangerous-goods declaration (§12).** Other industry chapters cite these sections and do not restate them. |
| Primary audience | Parts and industrial merchandisers, catalogue and fitment data managers, compliance and dangerous-goods owners, B2B ecommerce operators, data stewards, PIM architects, developers and AI enrichment designers |
| Depends on | CDS-000 through CDS-1500, especially CDS-200 (entity model, taxonomy mappings, relationships), CDS-300 (CMP_, SUP_, PRC_ and INV_ conditional), CDS-400 (dictionaries, units, related values), CDS-500 (preflight, verification, observation coverage), CDS-600 (facets), CDS-700 (evidence), CDS-900 (platform profiles, supplier import profile), CDS-1100 (entity references, identifiers), CDS-1500 (profile model, requirement levels, profile register, jurisdiction requirement register), CDS-1800 (technical specification rules, cited) |
| Companion package | CDS Reference Dictionary: Chapter 18 (Parts, Automotive & Industrial), Chapter 19 (Jurisdictions & Regulatory Schemes) |
| Profile identifier | `cds.profile.parts_fitment.v0_2` (registered in CDS-1500 §2.1) |
| Research basis | REVIEW-020 (global commerce vertical market research, 2026-09-20): automotive and hardware-and-tools stores carry the largest catalogues of any Shopify vertical (averages above 5,700 and 4,200 products per store respectively), DIY and hardware is a top-five worldwide ecommerce revenue segment (roughly US$0.4 trillion for 2026), and industrial and scientific categories are among the fastest-growing on Amazon; store counts are modest, PIM intensity per store is the highest of any archetype. |

Terminology follows CDS-100. Attribute requirement levels (R, C, REC, O, N/A) are those of CDS-1500 §4 and are not restated here. "Fitment" means the declared applicability of a part to a vehicle, machine, appliance or other host; "interchange" means equivalence between part numbers.

---

## 1. Purpose and Scope *(normative)*

CDS-1900 defines the industry profile for automotive and powersports parts and accessories, industrial and maintenance supplies, tools and hardware, electrical and plumbing components, hobby components (radio-control, model, craft hardware) and spare parts for appliances and equipment. It also defines, for the whole corpus, how products relate to one another (compatibility, fitment, inclusion, interchange, supersession), how kits and bundles are composed, and how dangerous goods are declared for transport.

The data shape is distinctive because the purchase decision is "will this fit?" rather than "do I like this?": the record is dominated by relationships to hosts and to other parts, by part-number equivalences and supersession chains, by typed technical attributes in the language of an external classification standard, by units of measure and pack quantities that determine what a sale actually delivers, and by hazardous-materials data that determines whether the item can be shipped at all.

**CDS1900-R001** An implementation claiming the Parts and Fitment Profile MUST represent fitment, compatibility, inclusion, interchange and supersession as product relationship records (§5), never as tags, free text, title conventions or category placement.

**CDS1900-R002** An implementation claiming this profile MUST represent units of measure, pack quantities, sale-unit hierarchies and variable-length or variable-quantity sale forms as typed attributes (§10) so that the delivered quantity of every order line is deterministic.

**CDS1900-R003** An implementation MUST declare a dangerous-goods status for every product (§12) and MUST maintain a jurisdiction requirement register (CDS-1500 §2.2) for every market it publishes parts, chemicals or equipment to.

**CDS1900-R004** This profile MUST NOT weaken any rule of CDS-1500 that it reuses; where this chapter is silent, CDS-1500, CDS-1800 (for technical specifications) and the core chapters govern.

## 2. Profile Model *(informative pointer)*

This profile applies the industry profile model of CDS-1500 §2, the requirement levels of CDS-1500 §4 and the jurisdiction requirement register of CDS-1500 §2.2 without restatement. Its identifier and dictionary bindings are in CDS-1500 §2.1; its seeded jurisdiction entries are in Appendix D.

## 3. Product Model *(normative)*

A part is identified by its manufacturer part number under a brand. The Product is the part; Variants are rare and arise only from sellable-unit differences (pack quantity, finish, length cut) — never from the hosts the part fits.

```
Product: Front brake pad set, brand ExampleBrake, part number EB-1234    (informative example)
  Product scope:
    STD_brand = ExampleBrake
    SUP_manufacturer_part_number = EB-1234
    CAT_product_type = brake_pad_set
    MF_part_origin_type = aftermarket               # part_origin_type dictionary
    MF_position = front
    MF_quantity_per_application = 1                  # one set per vehicle
    MF_unit_of_sale = set; MF_units_per_sale = 4     # four pads per set
    relationships:
      - {type: fits, target: application {make: Example, model: Sedan, years: 2018–2023, engine: 2.0L}, position: front}
      - {type: alternative_to, target: external_part {brand: OEM, number: 04465-00000}}
      - {type: superseded_by, target: product EB-1234A, effective: 2026-03-01}
  Variant scope:
    VAR_gtin = 09300000000027
```

**CDS1900-R005** Fitment MUST NOT be modelled as variants; a part that fits many hosts is one product with many `fits` relationship records (§6).

**CDS1900-R006** Pack quantity, finish, colour, length cut and hand (left/right) MAY be variant options where they identify distinct sellable units; position on the host (front, rear, left, right) is a fitment qualifier (§6) unless a distinct part number exists per position, in which case it is a separate product.

**CDS1900-R007** Brand and manufacturer part number MUST be governed identity attributes (CDS-1800 §5 rules R009–R011 apply); the same part number under two brands is two products related by `cross_reference`, never one product with two brands.

## 4. Product Families and Category Profiles *(informative baseline; the inheritance rule of CDS1500-R016 applies)*

| Product family / category | Required | Recommended | Typical variant options |
|---|---|---|---|
| Automotive replacement parts | brand; MPN; part origin type; fitment records with declared vocabulary source; position and quantity per application; condition; interchange records | supersession; technical attributes per category; core charge status; warranty; compliance marks per market (E-mark, DOT, CARB EO) | pack quantity |
| Automotive accessories and consumables (oils, fluids, care) | brand; MPN; fitment or universal declaration; dangerous-goods declaration; SDS reference where hazardous; net quantity | specification standards (viscosity grade, approvals as certifications) | size, multipack |
| Tyres and wheels | brand; MPN; size designation; load index; speed rating; regulated tyre label per market; DOT/E-mark compliance | season; run-flat; noise class | — |
| Tools and hardware | brand; MPN; technical attributes (size, drive, material, rating); unit of sale and pack quantity; hazardous status for chemicals | compatibility with systems (battery platforms as relationships); external classification code | size, pack |
| Electrical and plumbing components | brand; MPN; class attributes per an adopted classification model (e.g. ETIM class features); certification records per market; unit of sale (each / metre / box) | — | length, pack |
| Industrial MRO supplies | brand; MPN; classification code (UNSPSC/ETIM/GPC); unit of sale; MOQ and order multiple where B2B | SDS; shelf life for chemicals | pack |
| Hobby components (RC, model, craft) | brand; MPN; compatibility records; scale or standard; battery and DG where applicable | included items (kits) | colour, pack |
| Appliance and equipment spare parts | brand; MPN; fitment to appliance models (fits records); original vs compatible origin type | exploded-view diagram reference | — |

## 5. Product Relationship Record *(normative — single home for the corpus)*

CDS-200's entity model gives products a `relationships` collection of entity references; this section defines the record that collection carries. A product relationship is a governed, directed, typed link from a product (or variant) to a target, with the evidence and lifecycle of any other governed fact.

| Property | Meaning | Requirement |
|---|---|---|
| relationship_id | Stable identifier | Required |
| source | Product or variant reference | Required |
| relationship_type | Governed value from the `relationship_type` dictionary (package Chapter 18): `fits`, `compatible_with`, `accessory_for`, `requires`, `includes`, `part_of_set`, `replaces`, `superseded_by`, `alternative_to`, `cross_reference`, `successor_of`, `variant_family_of` | Required |
| target_kind | `product`, `variant`, `model_family`, `standard`, `application`, `external_part`, `external_product` | Required |
| target | Reference or embedded record appropriate to the kind (a product reference; a governed standard value; an application record per §6; an external part record with brand and number) | Required |
| quantity | Quantity of the target per source (for `includes`, `requires`) or of the source per application (for `fits`) | Conditional |
| qualifiers | Governed qualifiers (position, side, drive, engine code, option code, notes from a governed qualifier vocabulary) | Optional |
| direction | `directed` or `symmetric` (declared per relationship type in the dictionary) | Required |
| status | Lifecycle per CDS-400 §17.1 (proposed / active / deprecated / retired / rejected) | Required |
| effective_from / effective_to | Validity window (supersession dates, model years) | Optional |
| provenance | Source, evidence class, actor, timestamps (CDS-400 §23; CDS-700 for AI proposals) | Required |
| version | Record version | Required |

**CDS1900-R008** Every product relationship MUST be a record conforming to this section, carried in the product's `relationships` collection (CDS-1100 §8) or an equivalent governed structure, with a governed `relationship_type`, a typed target and provenance.

**CDS1900-R009** Relationship types MUST be governed dictionary values whose direction (directed or symmetric) is declared in the dictionary; an implementation MUST NOT invent relationship semantics per product.

**CDS1900-R010** Relationships MUST NOT be stored as tags, in free-text fields, in titles or in category membership as the system of record; such projections MAY be generated from relationship records.

**CDS1900-R011** A relationship whose target is another product in the catalogue MUST reference that product's stable identifier; a relationship whose target is outside the catalogue (an OEM number, a competitor part, a vehicle) MUST use the external target kinds with the identifying scheme declared.

**CDS1900-R012** Relationships MUST carry provenance and evidence class (CDS-700 §7); an AI-proposed relationship MUST be a proposal with evidence and MUST NOT be published without human review (CDS-700 §19), because a wrong fitment or compatibility is a safety and returns event.

**CDS1900-R013** Relationships are versioned governed facts: changes follow CDS-400 §24 (versioning, deprecation with replacement, breaking-change migration) and a superseded relationship MUST be retained with its validity window, never deleted.

**CDS1900-R014** Where a channel accepts relationship data (compatibility lists, complementary products, fitment tables), the projection MUST be generated from relationship records, declared in the Field Mapping with its comparison strategy, and verified under CDS-500; where the channel exposes no read-back for relationships, the verification status MUST be UNOBSERVABLE, not MATCH.

**CDS1900-R015** Symmetric relationships (`compatible_with`, `alternative_to`, `part_of_set`) MUST be stored once and evaluated in both directions; directed relationships MUST NOT be assumed to hold in reverse.

**CDS1900-R016** Cycles in `superseded_by` and `replaces` chains MUST be rejected at validation (the CDS400-R036 pattern).

## 6. Fitment and Application Data *(normative)*

Fitment is a `fits` relationship whose target is an application record: a description of the host (vehicle, machine, appliance model) drawn from a declared vocabulary. The corpus ships no vehicle or equipment tables — the leading reference databases are licensed (for example the Auto Care Association's vehicle configuration database used by the ACES standard, or manufacturer model lists) — so the organisation declares which vocabulary and release each application record uses.

| Application record property | Meaning |
|---|---|
| vocabulary_source | Governed value naming the reference vocabulary and release (for example `aces_vcdb_<release>`, `manufacturer_model_list_<brand>_<version>`, `organisation_vehicle_dictionary_v3`) |
| host_type | vehicle, powersport, marine, equipment, appliance, other |
| make / model / submodel / body / series | Governed values from the vocabulary |
| year_from / year_to (or model year list) | Typed integers |
| engine / transmission / drive / fuel / region qualifiers | Governed qualifier values from the vocabulary |
| equipment or appliance model identifiers | Governed values where the host is not a vehicle |
| position | Governed value (front, rear, left, right, upper, lower, inner, outer, …) |
| quantity_per_application | Integer |
| notes | Governed qualifier statements only (from a qualifier vocabulary), never free text |

**CDS1900-R017** Every fitment MUST be a `fits` relationship with an application record whose vocabulary source and release are declared; application values MUST be governed values of that vocabulary, never free text.

**CDS1900-R018** Universal fitment MUST be an explicit declaration (`MF_fitment_scope = universal` with the governed scope it is universal within), never the absence of fitment records; a part with neither fitment records nor a universal declaration MUST NOT satisfy an R-level fitment requirement.

**CDS1900-R019** Position and quantity per application MUST be typed qualifiers on the fitment record where the part's applicability depends on them.

**CDS1900-R020** Fitment MUST NOT be derived from titles, descriptions, supplier category names or image text by rules or AI without human review; a proposed fitment carries evidence (manufacturer application catalogue, E1; certified data feed, E2) and review state.

**CDS1900-R021** Model years MUST be typed integers or ranges; a fitment record MUST NOT encode years in free text.

**CDS1900-R022** When the declared vocabulary releases a new version, the organisation MUST record the migration of affected application records as a governed dictionary migration (CDS400-R082 pattern); records bound to a retired vocabulary release MUST be flagged for review, not silently re-pointed.

**CDS1900-R023** Fitment published to a channel (a vehicle compatibility table, a fitment metafield, a "fits your vehicle" lookup) MUST be generated from fitment records and verified under CDS-500 where the channel exposes read-back; otherwise reported UNOBSERVABLE (R014).

**CDS1900-R024** A storefront "shop by vehicle" or "shop by model" selector is an application filter over fitment records, distinct from customer facets (CDS-600); it MUST use the same governed vocabulary as the fitment records and MUST NOT be populated from free-text vehicle tags.

## 7. Interchange, Cross-Reference and Supersession *(normative)*

**CDS1900-R025** Original-equipment part numbers, competitor and aftermarket equivalents MUST be `alternative_to` or `cross_reference` relationships with external part targets that carry the issuing brand and its identifier scheme; the organisation's own SKU MUST NOT be stored in a manufacturer- or OEM-number attribute (CDS-1800 R010).

**CDS1900-R026** Supersession MUST be a directed `superseded_by` relationship with an effective date; a superseded part's lifecycle state MUST reflect its status and its record MUST be retained (R013) so that searches for the old number resolve to the replacement.

**CDS1900-R027** Equivalence ("alternative_to") MUST declare its basis (form-fit-function equivalent, functional equivalent, manufacturer-declared) as a governed qualifier; an equivalence asserted without a basis MUST be treated as a proposal.

**CDS1900-R028** Where a channel or marketplace uses interchange data for search, the projection MUST be generated from relationship records (R014).

**CDS1900-R029** Cross-reference numbers MUST be searchable through governed search synonyms or identifier indexing (CDS600-R075) without being exposed as facets.

## 8. Technical Attributes and External Classification *(normative)*

Technical attributes follow the specification rules of CDS-1800 §6 (typed, unit-bearing, category specification sets, basis qualifiers, provenance). This section adds the mechanism for adopting an external classification and attribute model as the source of a category's specification set.

| External model (informative) | What it provides |
|---|---|
| ETIM (electro-technical, HVAC, building, tools, shipbuilding sectors) | Classes with typed features (alphanumeric from value lists, numeric with units, logical, range); one class per product; released in versions |
| GS1 Global Product Classification (GPC) | Segment / family / class / brick with brick attributes and values; 8-digit codes; updated twice yearly |
| UNSPSC | Procurement commodity codes (segment / family / class / commodity); no attributes |
| Auto Care Association PCdb and PAdb (used by ACES/PIES) | Part terminology and part attributes for the automotive aftermarket; licensed |
| Marketplace category attribute sets | Channel-specific required attributes |

**CDS1900-R030** An organisation MAY adopt an external classification model as the source of a category's specification set; where it does, each external class or brick MUST be mapped to an internal category through a Taxonomy Mapping (CDS-200 §6) with the model's version, and each external feature MUST be mapped to an Attribute Definition with a declared crosswalk (name, unit, value list mapping).

**CDS1900-R031** External classification codes MUST be stored as Taxonomy Mappings or governed identifiers with their model version, never as free text, and a product MUST be assigned to exactly one class in any one model.

**CDS1900-R032** Values drawn from an external value list MUST be governed dictionary values with alias mappings for the external codes (CDS-400 §7), so that a change of model version is a governed migration.

**CDS1900-R033** Dimensional, threaded and tolerance attributes MUST be structured (nominal value, unit, tolerance, thread standard) rather than a single text token such as "M8x1.25".

**CDS1900-R034** Weight and dimensions used for logistics MUST be typed measurements of the sale unit (§10), distinguished from the technical dimensions of the part.

## 9. Origin Type, Brand, Manufacturer and Condition *(normative; dictionary bindings informative)*

| Field | Meaning | Dictionary |
|---|---|---|
| MF_part_origin_type | Genuine (original equipment as sold by the vehicle or equipment maker), original equipment supplier (OES), aftermarket | `part_origin_type` (Chapter 18) |
| MF_condition | new, refurbished, remanufactured, used | `product_condition` (Chapter 18) |
| STD_brand / SUP_manufacturer / MF_remanufacturer | Brand as sold; legal manufacturer; remanufacturer where condition is remanufactured | Governed values |
| PRC_core_charge | Core charge where the PIM is the pricing authority | Conditional (CDS-300 §14) |

**CDS1900-R035** Part origin type MUST be a governed value and MUST NOT be inferred from brand alone; a "genuine" claim MUST carry evidence (E1/E2) because it is a claim about the maker's supply chain.

**CDS1900-R036** Condition MUST be a governed variant-scope value; remanufactured MUST be distinguished from refurbished and from used, and a channel that supports fewer condition values MUST receive a declared mapping (for example remanufactured → refurbished) recorded on the Attribute Definition.

**CDS1900-R037** Brand, manufacturer and remanufacturer MUST be separate attributes where they differ.

**CDS1900-R038** Core-charge and exchange-part terms MUST be typed attributes under the pricing authority and MUST NOT be encoded in titles.

## 10. Units of Measure, Pack Quantity and B2B Terms *(normative)*

| Field | Meaning | Type |
|---|---|---|
| MF_unit_of_sale | The unit one order line delivers (each, pair, set, box, roll, metre, litre, kilogram) | Governed value |
| MF_units_per_sale | Number of base units in the sale unit (pads per set, pieces per box) | Integer |
| MF_sold_by_measure | Whether the item is sold by cut length, weight or volume rather than by count | Boolean |
| MF_measure_increment / MF_measure_minimum / MF_measure_maximum | Increments and bounds for cut-length or measured sales | Typed measurements |
| MF_minimum_order_quantity / MF_order_multiple | B2B ordering constraints | Integers (conditional on authority) |
| VAR_sale_unit_level | each / inner / case / pallet with contained quantities and identifiers | Per CDS-1700 R007 pattern |

**CDS1900-R039** Every product MUST declare its unit of sale and the number of base units per sale unit; a "set of four" and a single unit MUST be distinguishable without reading the title.

**CDS1900-R040** Products sold by cut length, weight or volume MUST declare the measure, its increment and bounds as typed values; the delivered quantity is an order-level fact and MUST NOT be a product variant per length unless the organisation sells fixed pre-cut lengths.

**CDS1900-R041** Sale-unit levels (each, inner, case) MUST follow the hierarchy rules of CDS1700-R007 with trade identifiers per level where they exist.

**CDS1900-R042** Minimum order quantities, order multiples and B2B price breaks MUST be typed attributes under the declared pricing or commercial authority (CDS-200 §13; `PRC_`/`INV_` only where the PIM is the authority) and MUST be evaluated at preflight for channels that enforce them.

**CDS1900-R043** Logistics measurements (packaged dimensions and weight of the sale unit) MUST be typed and distinct from technical dimensions (R034); oversized and hazardous handling classes MUST be derived under governed rules.

## 11. Kits, Bundles and Assemblies *(normative — single home for the corpus)*

A kit is a product whose sellable content is composed of other products. The corpus distinguishes a **stocked kit** (a manufacturer or retailer-assembled item with its own identifier and inventory), a **virtual bundle** (assembled at order time from component inventory) and an **assembly** (a product whose components are also sold separately as spare parts).

**CDS1900-R044** A kit, bundle or assembly MUST be a product whose composition is expressed as `includes` relationship records with quantities (§5); component identity, specifications, compliance records and declarations remain on the components.

**CDS1900-R045** The kit kind (stocked kit, virtual bundle, assembly) MUST be a governed attribute (`MF_kit_kind`), because inventory authority, trade identifiers and channel projection differ: a stocked kit MAY carry its own GTIN; a virtual bundle MUST NOT claim a trade identifier it does not have.

**CDS1900-R046** Kit-level declarations that depend on components (allergens and nutrition for food hampers per CDS-1700; ingredients for beauty sets per CDS-1600; dangerous-goods status per §12; battery facts per CDS-1800) MUST be derived from the component records under declared rules and MUST NOT be independently authored.

**CDS1900-R047** Where a channel supports bundle semantics (a bundle flag, component listing, bundle pricing), the projection MUST be generated from the relationship records and declared in the Field Mapping; availability of a virtual bundle MUST be derived from component availability under the inventory authority and MUST be verifiable (CDS-500).

**CDS1900-R048** Removing or replacing a component MUST be a governed relationship change (R013) with the kit's revision advanced (CDS-200 §14), so that a published kit state can be traced to its composition.

## 12. Hazardous Materials and Dangerous Goods *(normative — single home for the corpus)*

Whether a product can be shipped, by which mode, in what packaging and with which documents is determined by its classification under the transport-of-dangerous-goods regimes, and whether it must be accompanied by a safety data sheet is determined by workplace and consumer chemical regimes. The declaration is a product fact; the carrier's documentation is a projection of it.

| Property | Meaning |
|---|---|
| CMP_dangerous_goods.regulated | Boolean: whether the product (or any component of a kit) is regulated for transport in any declared mode; **an explicit `false` is a declaration, not a default** |
| un_number | UN number (e.g. UN3480) |
| proper_shipping_name | Proper shipping name |
| class_or_division | Governed value from the `dangerous_goods_class` dictionary (Chapter 18) |
| subsidiary_hazards | Governed values |
| packing_group | I / II / III or none |
| quantity_per_package / net_quantity_basis | Typed measurements used for limited and excepted quantity determination |
| limited_quantity_eligible / excepted_quantity_eligible | Booleans with the regime they were evaluated under |
| transport_modes | Modes and regimes evaluated (road/rail under the national code, sea under IMDG, air under ICAO/IATA) |
| battery_specifics | Watt-hours or lithium content, cells or batteries per package, contained-in/packed-with/alone, state of charge constraints, test summary reference (CDS-1800 §8) |
| sds_reference | Safety data sheet document (MED_) with format (GHS revision) and date |
| hazard_communication | GHS pictograms, signal word, hazard and precautionary statements as labelled |
| declared_by / declared_at / evidence | Provenance |

**CDS1900-R049** Every product MUST carry a dangerous-goods declaration record whose `regulated` value is an explicit declaration; a product with no record MUST NOT be published to a channel or carrier integration that requires shipping data, and the absence of a record MUST be reported as a missing required value (CDS200-R035), never treated as "not regulated".

**CDS1900-R050** A regulated product's declaration MUST carry the UN number, proper shipping name, class or division and packing group (where applicable) from the governing regime, and the quantity facts needed to evaluate limited or excepted quantity provisions.

**CDS1900-R051** Dangerous-goods classification MUST NOT be inferred from category, title or description by rules or AI; it MUST derive from the safety data sheet, the manufacturer's declaration or a competent classification (E1) and MUST be reviewed by a person accountable for dangerous-goods compliance before acceptance.

**CDS1900-R052** Where a product is a hazardous chemical in a market that requires a safety data sheet to be prepared or supplied (Appendix D), the SDS MUST be a typed document record with its GHS revision and date, linked to the product, and its presence MUST be evaluated at preflight for that market; a consumer-market exemption from SDS supply MUST be recorded as the reason where relied on.

**CDS1900-R053** GHS hazard communication elements as labelled (pictograms, signal word, hazard and precautionary statements) MUST be structured statement records where a market requires them, and MUST NOT be projected as customer facets.

**CDS1900-R054** Kits inherit the most restrictive dangerous-goods status of their components under declared rules (R046); a kit containing a regulated component MUST be declared regulated.

**CDS1900-R055** Carrier and channel shipping declarations MUST be projections of the record, declared in the Field Mapping with write semantics and verified under CDS-500 where read-back exists; a carrier rejection MUST be imported as an observed quality event, not written into the canonical record.

**CDS1900-R056** Products whose transport is prohibited in a mode (for example damaged, defective or recalled lithium batteries by air) MUST carry the prohibition as a governed attribute evaluated at preflight for channels shipping by that mode.

## 13. Compliance, Certifications and Vehicle Standards *(normative)*

**CDS1900-R057** Regulatory compliance marks and approvals for parts (vehicle-component type approvals, emissions executive orders, design-rule compliance, electrical and machinery conformity marks, tyre labels) MUST be governed compliance records per market (the CDS-1800 §12 pattern: scheme, identifier, evidence, responsible party, status, dates) and MUST NOT be treated as populated because a mark appears in an image or a phrase in copy.

**CDS1900-R058** Where a market requires a label or class information to be shown online close to the price (tyre labels in the EU and GB, Appendix D), the projection MUST be generated from the compliance record and verified.

**CDS1900-R059** Performance and quality standards a part is claimed to meet (viscosity grades, industry specifications, manufacturer approvals) MUST be certification or claim records with evidence (CDS-1600 §11 pattern); they MAY feed claim-driven facets only under CDS1500-R049 governance.

**CDS1900-R060** Country of origin and tariff classification, where required for cross-border sale, MUST be governed attributes (`CMP_country_of_origin`, `CMP_tariff_code` with scheme and version) with provenance.

## 14. Media and Technical Documentation *(normative)*

**CDS1900-R061** Exploded-view diagrams, installation instructions, technical data sheets, safety data sheets and certificates MUST be typed media records (MED_) with language, version and the product or relationship they document; a diagram callout that identifies a part MUST link to the part's product record.

**CDS1900-R062** Documents a market requires to be available to purchasers (Appendix D) MUST be present before publication to that market and their presence verified.

## 15. Customer Facet and Navigation Design *(informative — normative facet rules live in CDS-600)*

| Construct | Recommended baseline behaviour | Anti-pattern |
|---|---|---|
| Shop by vehicle / model | Application filter over fitment records using the governed vocabulary (R024) | Free-text vehicle tags; category per vehicle |
| Brand | Governed brand dictionary | Supplier spellings |
| Position / side | Governed qualifier values | Free text |
| Origin type | Genuine / OES / aftermarket from the governed value | Unevidenced "genuine" |
| Condition | Governed condition values | — |
| Technical attributes | Typed specification facets with units and ranges per category | Text buckets |
| Universal fit | Explicit declaration facet | Absence of fitment treated as universal |
| Hazardous handling | Never a customer facet; a fulfilment attribute | — |

## 16. Channel Projection Guidance *(informative — normative rules: CDS-500, CDS-900)*

| Canonical concept | Metafield-style channel (informative) | Feed-style channel (informative) |
|---|---|---|
| Fitment | Fitment metafields or app-managed compatibility tables generated from records; read back where the app exposes it, otherwise UNOBSERVABLE | The seeded feed channels (Google Merchant Center, Meta) define no fitment attributes (verified 2026-09-20); carry vehicle applicability in `product_detail` and titles under a declared policy. Marketplaces with fitment models (for example automotive parts marketplaces) are candidates for future CDS-900 platform profiles |
| Interchange and supersession | Search synonyms and redirects generated from records | Not published |
| Unit of sale and pack | Typed metafields; title composition policy | `multipack`, `is_bundle`, `unit_pricing_measure` where relevant |
| Condition | Condition metafield or option | `condition`; remanufactured mapped per R036 |
| Dangerous goods | Fulfilment metafields; carrier declarations | Not consumer-facing |
| Compliance labels required online (tyre label) | Generated per-market block near price | Description where policy allows |

## 17. AI Enrichment and Review *(informative — normative AI rules live in CDS-700)*

| Task | AI may propose | Deterministic or human control |
|---|---|---|
| Fitment extraction from application catalogues | Candidate `fits` records bound to the declared vocabulary | Mandatory review (R020); vocabulary validation |
| Cross-reference proposals | Candidate `alternative_to` / `cross_reference` records with evidence | Mandatory review; equivalence basis required (R027) |
| Technical attribute extraction | Typed candidates (CDS-1800 §15) | Unit and range validation; provenance |
| External class assignment | Candidate ETIM/GPC class | Taxonomy mapping governance; one class per model (R031) |
| Dangerous-goods classification | None — SDS or manufacturer declaration only | R051 |
| Kit composition | Candidate component lists from documents | Relationship governance (R044) |

## 18. Governance and Organisational Extensions *(informative — rules in CDS-1500 §23 and CDS-800)*

The relationship-type, origin-type and condition dictionaries are extended under CDS-400; the declared application vocabulary is a governed external dictionary with release-based migration (R022). Dangerous-goods classification changes (a new UN entry, a regime edition such as the Australian Code 7.9 replacing 7.8) are handled as governed dictionary and record migrations with an accountable dangerous-goods owner (CDS-800 §5). The jurisdiction requirement register for parts and chemicals is reviewed on the declared cadence and whenever a market changes a transport, chemical or vehicle-equipment rule.

## 19. Conformance Requirements *(normative — claims and levels per CDS-1000)*

**CDS1900-R063** An implementation claiming the CDS Parts and Fitment Profile MUST: represent every fitment, compatibility, inclusion, interchange and supersession fact as a governed product relationship record with provenance, versioning and verification (R001, R008–R016); bind fitment to a declared application vocabulary with typed years, positions and quantities and explicit universal-fit declarations (R017–R024); keep OEM and cross-reference numbers as external targets and supersession as dated directed relationships (R025–R029); adopt external classification models only through governed Taxonomy Mappings and attribute crosswalks (R030–R034); govern origin type, condition, brand and manufacturer (R035–R038); declare unit of sale, pack quantity, measured sale forms and B2B constraints as typed values (R039–R043); model kits as `includes` relationships with derived kit-level declarations (R044–R048); declare dangerous-goods status explicitly for every product with SDS and hazard-communication records where required (R049–R056); maintain per-market compliance records and required documents (R057–R062); maintain and evaluate a jurisdiction requirement register for every market published to (R003); apply category-specific requirements per CDS1500-R009; and publish and verify channel representations under CDS-500.

**CDS1900-R064** A Parts and Fitment Profile claim MUST name the application vocabulary sources and releases in use, state whether hazardous chemicals are in scope, and state which markets its register covers. Implementations claiming other industry profiles that cite §5, §11 or §12 of this chapter MUST satisfy the cited sections without claiming this profile.

## 20. Worked Product Examples *(informative)*

### 20.1 Brake pad set with fitment, cross-reference and supersession

```
STD_brand = ExampleBrake; SUP_manufacturer_part_number = EB-1234; CAT_product_type = brake_pad_set
MF_part_origin_type = aftermarket; MF_condition = new
MF_unit_of_sale = set; MF_units_per_sale = 4; MF_quantity_per_application = 1
relationships:
  {type: fits, target: application {vocabulary_source: aces_vcdb_2026_08, host_type: vehicle,
       make: Example, model: Sedan, submodel: GT, year_from: 2018, year_to: 2023, engine: "2.0L L4 turbo"},
   qualifiers: {position: front}, provenance: {source: manufacturer_application_catalogue, class: E1}}
  {type: fits, target: application {..., model: Wagon, year_from: 2019, year_to: 2023}, qualifiers: {position: front}}
  {type: cross_reference, target: external_part {brand: ExampleMotors, scheme: oem_part_number, number: "04465-00000"},
   qualifiers: {basis: form_fit_function}}
  {type: superseded_by, target: product EB-1234A, effective_from: 2026-03-01}
CMP_dangerous_goods = {regulated: false, declared_by: dg_owner, declared_at: 2026-09-01}
CMP_compliance_declarations = [{jurisdiction: EU, scheme: eu_unece_type_approval, mark: "E-mark R90", certificate: ...}]
Channel: fitment table generated from `fits` records; feed channel carries applicability in product_detail;
         verification: metafield MATCH; feed UNOBSERVABLE (no read-back of fitment)
```

### 20.2 Hydraulic hose sold by the metre

```
CAT_product_type = hydraulic_hose
MF_sold_by_measure = true; MF_unit_of_sale = metre; MF_measure_increment = {0.5, metre}
MF_measure_minimum = {1, metre}; MF_measure_maximum = {50, metre}
MF_inside_diameter = {nominal: 12.7, unit: millimetre}; MF_working_pressure = {value: 210, unit: bar}
Taxonomy mapping: ETIM class EC0xxxxx (release 10.0) -> internal category Hydraulics > Hoses; feature crosswalk declared
Order line: 7.5 m -> delivered quantity computed at order time, not a variant
```

### 20.3 Engine oil (dangerous goods and SDS)

```
CAT_product_type = engine_oil
VAR_net_quantity = {value: 5, unit: litre}
MF_viscosity_grade = sae_5w_30 (governed); MF_certifications = [{scheme: api_service_category, value: "SP", evidence: E1}]
CMP_dangerous_goods = {regulated: false, transport_modes: [road, air], basis: "not classified under ADG 7.9 / IATA",
                       sds_reference: MED-sds-2026-01 (GHS rev 7, 2026-01-10), declared_by: dg_owner}
CMP_country_of_origin = AU; CMP_tariff_code = {scheme: hs_2022, code: "2710.19"}
AU preflight: SDS present (hazardous chemical for workplace supply; consumer retail exemption not relied on) -> pass
```

### 20.4 Radio-control servo with compatibility

```
CAT_product_type = rc_servo
relationships:
  {type: compatible_with, target: standard {standard: "servo_connector_jr_3_pin"}, direction: symmetric}
  {type: accessory_for, target: model_family {brand: ExampleRC, family: "Crawler 1/10"}}
MF_voltage_range_v = {min: 4.8, max: 8.4}; MF_torque_kg_cm = 25
MF_kit_kind = none; MF_unit_of_sale = each
```

## 21. Reference Validation Cases *(informative — the profile's contribution to the cross-industry validation set, REVIEW-020)*

- a fitment held only in a tag or title, which must fail (R001, R010);
- a part with neither fitment records nor a universal declaration offered as "fits all", which must not satisfy an R-level requirement (R018);
- a fitment with free-text years ("2018–current") (R021);
- a vocabulary release change that must produce a governed migration rather than silent re-pointing (R022);
- a `superseded_by` cycle that validation must reject (R016);
- an OEM number stored in the organisation's own SKU attribute (R025);
- a "set of four" whose unit of sale is not declared, making the delivered quantity ambiguous (R039);
- a product with no dangerous-goods record published to a shipping channel, which must be reported as missing (R049);
- a kit containing a lithium-battery component declared "not regulated" at kit level (R054);
- a dangerous-goods classification proposed by AI from a category, which must be refused (R051);
- a tyre listed in the EU without the tyre label near the price (R058, D-EU-3);
- an aftermarket emissions part sold into California without an Executive Order reference (D-US-3);
- a "genuine" origin claim without evidence (R035).

---

## Appendix A. Parts and Fitment Attribute Baseline *(normative — dictionary bindings per CDS1500-R011)*

| Field | Scope | Type | Baseline requirement |
|---|---|---|---|
| STD_brand / SUP_manufacturer_part_number / VAR_gtin | Product / Variant | Governed identity values | R |
| CAT_product_type | Product | Governed classification reference | R |
| MF_part_origin_type | Product | Governed dictionary reference (`part_origin_type`) | R |
| MF_condition | Variant | Governed dictionary reference (`product_condition`) | R |
| `fits` relationship records or MF_fitment_scope = universal | Product | Relationship records / declaration | R for application-specific parts |
| `alternative_to` / `cross_reference` / `superseded_by` / `replaces` records | Product | Relationship records | C — R where interchange or supersession is published |
| `includes` records / MF_kit_kind | Product | Relationship records / governed value | R for kits and bundles |
| Category technical attributes | Product | Typed Attribute Definitions (CDS-1800 §6; external crosswalk per §8) | Per category profile |
| CMP_external_classifications | Product | Taxonomy Mappings with model and version | REC; R where a trading partner requires the code |
| MF_unit_of_sale / MF_units_per_sale | Product | Governed value; integer | R |
| MF_sold_by_measure / MF_measure_increment / MF_measure_minimum / MF_measure_maximum | Product | Boolean; typed measurements | R for measured sale forms |
| VAR_sale_unit_level | Variant / levels | Governed level with quantities and identifiers | C |
| MF_minimum_order_quantity / MF_order_multiple | Product | Integers (authority-conditional) | C |
| Logistics dimensions and weight of the sale unit | Product / Variant | Typed measurements | R where the organisation ships |
| CMP_dangerous_goods | Product / Variant | Declaration record (§12) | R (explicit `regulated` value for every product) |
| MED_technical_documents (SDS, diagrams, certificates, instructions) | Product | Typed media records | C — R where a market requires availability |
| CMP_compliance_declarations | Product (per market) | Governed records | C — R where a market regulates the part |
| CMP_country_of_origin / CMP_tariff_code | Product | Governed values | C — R for cross-border sale |
| MF_warranty_months / MF_warranty_type | Product (per market) | Typed records | REC |

## Appendix B. Dictionary Bindings *(informative — becomes governed data on adoption per CDS1500-R011)*

| Dictionary key | Package chapter | Bound attribute(s) | Status at 0.8.0 |
|---|---|---|---|
| relationship_type | 18 (new) | Product relationship records (§5) | Bound (corpus-wide) |
| part_origin_type | 18 (new) | MF_part_origin_type | Bound |
| product_condition | 18 (new) | MF_condition | Bound (shared with CDS-1800) |
| dangerous_goods_class | 18 (new) | CMP_dangerous_goods.class_or_division | Bound (corpus-wide) |
| jurisdiction / regulatory_scheme | 19 (new) | CMP_* records | Bound via CDS-1500 §2.2 |
| connectivity, power_source, battery_chemistry | 11 | Technical attributes where relevant | Bound via CDS-1800 |

Deliberately not shipped: vehicle and equipment application vocabularies (licensed or manufacturer-sourced; declared per organisation), part terminology and attribute databases (licensed), the full UN dangerous-goods list (regime-published; only the class and division vocabulary is seeded), units of measure (CDS-400 §18 reference data), qualifier statement vocabularies (organisation- or standard-sourced).

## Appendix C. References *(informative; retrieved 2026-09-20 unless stated)*

| Ref | Source | Location | Use in this chapter |
|---|---|---|---|
| [P1] | Auto Care Association — Data Standards; ACES 5.0 and PIES 8.0 release (2026-04-02); supporting databases (VCdb, Qdb, PCdb, PAdb, Brand Table) | autocare.org | Fitment and product information exchange model, licensed reference databases (§6, §8) |
| [P2] | ETIM International — Classification Guidelines (v3, 2020) | etim-international.com | Class/feature/value model, one class per product, IXF release format (§8) |
| [P3] | GS1 — Global Product Classification Development & Implementation Guide (2023); How GPC works | gs1.org | Segment/family/class/brick with attributes; 8-digit coding (§8) |
| [P4] | National Transport Commission — Australian Dangerous Goods Code edition 7.9 (usable from 1 October 2024, mandatory from 1 October 2025) | ntc.gov.au | Classes and divisions, limited and excepted quantities, lithium battery mark (§12, D-AU-1) |
| [P5] | Safe Work Australia — Adoption of GHS 7 (mandatory from 1 January 2023); model Code of Practice: Preparation of safety data sheets (2023); Suppliers and users information sheet (June 2023) | safeworkaustralia.gov.au | SDS obligations for hazardous chemicals incl. consumer products supplied to workplaces (D-AU-2) |
| [P6] | IATA — Lithium Battery Guidance Document (2026) | iata.org | UN 3480/3481/3090/3091/3551/3552, 30% state of charge, test summary availability (§12) |
| [P7] | Regulation (EU) 2020/740 on the labelling of tyres (applies from 1 May 2021); UK retained text | eur-lex.europa.eu; legislation.gov.uk | Tyre label content and display close to the price in distance selling; product information sheet (D-EU-3, D-UK-2) |
| [P8] | Regulation (EU) 2023/988 General Product Safety Regulation (applies from 13 December 2024) | eur-lex.europa.eu | Traceability and online offer information (D-EU-4) |
| [P9] | ICC Compliance Center — Consumer chemical products and GHS SDS requirements (Canada CCCR 2001 / HPR; OSHA HazCom consumer-use exemption; REACH Article 31(4)) (2022) | thecompliancecenter.com | Consumer-product SDS exemptions by jurisdiction (D-CA-1, D-US-2, D-EU-2; retrieved, secondary) |
| [P10] | OEHHA — Proposition 65 amendments effective 2025-01-01 including tailored warnings for passenger or off-highway motor vehicle parts and recreational marine vessel parts | oehha.ca.gov | Vehicle-parts warning content and internet warnings (D-US-4) |
| [P11] | StoreInspect — Best Shopify categories to target in 2026 (updated 2026-09-19); ECDB Amazon marketplace report (2026) | storeinspect.com; ecdb.com | Catalogue-size and growth basis (REVIEW-020) |

## Appendix D. Jurisdiction Requirement Register — Seed *(informative seed of the normative register defined in CDS-1500 §2.2)*

Conventions as in CDS-1600 Appendix D. Vehicle-equipment type-approval and emissions regimes are seeded at summary level; most were retrieved but not spot-verified this pass and are marked accordingly.

### D.1 Australia (AU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-AU-1 | Australian Code for the Transport of Dangerous Goods by Road and Rail, edition 7.9 (aligned to UN Model Regulations 23rd revised edition), given force by state and territory dangerous goods transport laws — NTC and state competent authorities (`au_adg_code_7_9`) | Dangerous goods of Classes 2–6, 8 and 9 consigned by road or rail (Classes 1 and 7 under other laws) | transport; documentation | Classification (UN number, proper shipping name, class/division, packing group), packaging and marking incl. limited-quantity and lithium battery marks, transport documentation and emergency information; very small consignment and limited quantity provisions → CMP_dangerous_goods (all properties), carrier projection | Usable from 1 October 2024; mandatory from 1 October 2025 | Verified 2026-09-20 [P4] |
| D-AU-2 | Model WHS Regulations (as adopted by each jurisdiction) — GHS Revision 7 classification, labelling and safety data sheets — Safe Work Australia and state regulators (`au_ghs7_sds`) | Hazardous chemicals manufactured or imported for use, handling or storage at workplaces, including hazardous chemicals intended as consumer products (exemptions include potable liquids that are consumer products at retail premises) | documentation (SDS prepared before first supply to a workplace, reviewed at least every 5 years, Australian manufacturer or importer contact details); labelling_element (GHS 7 labels) | SDS in the Australian 16-section format with GHS 7 classification, signal word, pictograms, hazard and precautionary statements, transport information; supplier must provide the SDS with supply to a workplace → MED_technical_documents (SDS, GHS rev 7, date), CMP_dangerous_goods.hazard_communication | GHS 7 only from 1 January 2023 | Verified 2026-09-20 [P5] |
| D-AU-3 | Road Vehicle Standards Act 2018 and Australian Design Rules; state vehicle standards for modifications — Department of Infrastructure and state regulators (`au_adr_vehicle_standards`) | Replacement components and accessories subject to design rules (lighting, tyres, child restraints via mandatory standards, seatbelts) and modifications | pre_market (component certification where an ADR applies); labelling_element (markings) | ADR compliance evidence and markings per component; tyre markings → CMP_compliance_declarations (scheme `au_adr_vehicle_standards`) | Ongoing | Retrieved (not spot-verified) |
| D-AU-4 | Proposition-style warnings do not apply; Australian Consumer Law mandatory safety and information standards apply to specific products (for example quad bikes, portable ladders, vehicle jacks) — ACCC | Specific consumer products | labelling_element; warning_statement | Product-specific mandatory standard elements → MF_warning_statements, CMP_compliance_declarations | Product-specific | Not seeded (organisation supplies per product type) |

### D.2 New Zealand (NZ)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-NZ-1 | Land Transport Rule: Dangerous Goods 2005 (aligned to the UN Model Regulations / ADG) — Waka Kotahi NZ Transport Agency (`nz_dangerous_goods_rule_2005`) | Dangerous goods transported by land | transport; documentation | Classification and documentation as for AU with NZ variations → CMP_dangerous_goods | Ongoing | Retrieved (not spot-verified) |
| D-NZ-2 | Hazardous Substances and New Organisms Act 1996; Hazardous Substances (Labelling) Notice 2017 and (Safety Data Sheets) Notice 2017 — EPA and WorkSafe (`nz_hsno_labelling_sds`) | Hazardous substances, including consumer chemical products | labelling_element; documentation (SDS) | GHS-aligned labels; SDS supplied with substances for workplaces → MED_technical_documents (SDS), CMP_dangerous_goods.hazard_communication | Ongoing (Group Standards provide alternative compliance routes) | Retrieved (not spot-verified) |

### D.3 United States (US, with California noted)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-US-1 | Hazardous Materials Regulations, 49 CFR parts 171–180 — PHMSA/DOT (`us_49cfr_hazmat`) | Hazardous materials offered for transport in commerce (road, rail, air, water; air also under ICAO/IATA) | transport; documentation | UN number, proper shipping name, hazard class, packing group, limited quantity and ORM-D-style consumer commodity provisions (as amended), lithium battery mark and test summary → CMP_dangerous_goods | Ongoing | Retrieved (not spot-verified) |
| D-US-2 | Hazard Communication Standard, 29 CFR 1910.1200 (updated 2024 to GHS Revision 7) — OSHA (`us_osha_hazcom`) | Hazardous chemicals in workplaces; consumer products exempt where workplace use mirrors consumer use in duration and frequency | documentation (SDS); labelling_element | 16-section SDS and GHS labels for workplace-supplied hazardous chemicals → MED_technical_documents (SDS), exemption reason where relied on (R052) | 2024 update with phased compliance | Retrieved 2026-09-20 [P9] (secondary; not spot-verified) |
| D-US-3 | California Air Resources Board aftermarket parts Executive Orders (Vehicle Code 27156) (`us_carb_executive_order`) | Aftermarket emissions-related parts sold or installed in California (and states adopting California standards) | pre_market (Executive Order exemption); labelling_element (EO number) | CARB Executive Order number for the part and applications → CMP_compliance_declarations (scheme `us_carb_executive_order`, EO number), fitment scope | Ongoing | Retrieved (not spot-verified) |
| D-US-4 | Proposition 65 (California), 27 CCR 25607.50–25607.53 tailored warnings for passenger or off-highway motor vehicle parts and recreational marine vessel parts; internet warning rules — OEHHA (`us_ca_prop65_warning`) | Vehicle and vessel parts causing exposure to listed chemicals sold to California consumers | warning_statement; listing_element | Tailored safe-harbour warning content; warning on the product display page, "WARNING" hyperlink or prominent pre-purchase display → MF_warning_statements (jurisdiction US-CA, scheme with the vehicle-parts variant), listing projection | Effective 1 January 2025 | Verified 2026-09-20 [P10] |
| D-US-5 | Federal Motor Vehicle Safety Standards and equipment marking (49 CFR part 571; DOT tire identification number 49 CFR 574) — NHTSA (`us_fmvss_equipment`) | Regulated motor vehicle equipment (lighting, brake hoses, tyres, glazing, child restraints) | pre_market (self-certification); labelling_element (DOT symbol, tire identification number) | DOT marking and TIN → CMP_compliance_declarations | Ongoing | Retrieved (not spot-verified) |

### D.4 European Union (EU)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-EU-1 | European Agreement concerning the International Carriage of Dangerous Goods by Road (ADR) as applied by Directive 2008/68/EC; IMDG and ICAO/IATA for sea and air (`eu_adr_transport`) | Dangerous goods in transport | transport; documentation | Classification, packaging, marking, documentation → CMP_dangerous_goods | Biennial ADR editions | Retrieved (not spot-verified) |
| D-EU-2 | REACH Regulation (EC) No 1907/2006 Article 31 (safety data sheets); CLP Regulation (EC) No 1272/2008 (classification, labelling, packaging) — ECHA and member states (`eu_reach_sds_article_31`, `eu_clp_1272_2008`) | Hazardous substances and mixtures | documentation (SDS to professional users; for products sold to the general public an SDS need not be supplied where sufficient information is provided, but must be supplied on request by a downstream user or distributor); labelling_element (CLP pictograms, signal word, hazard and precautionary statements) | SDS document, CLP hazard communication elements → MED_technical_documents (SDS), CMP_dangerous_goods.hazard_communication | Ongoing | Verified in part 2026-09-20 [P9] (Article 31(4) via secondary source; regulation text not read) |
| D-EU-3 | Regulation (EU) 2020/740 on the labelling of tyres (`eu_tyre_label_2020_740`) | C1, C2 and C3 tyres (passenger, light and heavy commercial), retreads once a test method exists | rating_label; listing_element; documentation (product information sheet); pre_market (supplier enters values in the product database, EPREL) | Tyre label with fuel efficiency class (A–E), wet grip class (A–E), external rolling noise class and dB value, severe-snow and ice-grip pictograms; product information sheet (supplier, tyre type identifier, size designation, load index, speed symbol, classes, production start and end dates); label displayed close to the price in distance selling and online (nested display permitted), PIS accessible and printable on request; hosting service providers enable the display → CMP_compliance_declarations (scheme `eu_tyre_label_2020_740`, classes, EPREL id), MF_tyre_size_designation, MF_load_index, MF_speed_rating, MED_technical_documents (label, PIS), listing projection | Applies from 1 May 2021 | Verified 2026-09-20 [P7] |
| D-EU-4 | Regulation (EU) 2023/988 General Product Safety Regulation (`eu_gpsr_2023_988`) | Non-harmonised consumer products (many tools, accessories, hobby components) and cross-cutting online duties | listing_element; labelling_element; pre_market (responsible economic operator) | Manufacturer name, address and electronic contact; product identifier; warnings and safety information; picture in online offers → CMP_responsible_person, CMP_product_identifier, MF_warning_statements | Applies from 13 December 2024 | Verified 2026-09-20 [P8] |
| D-EU-5 | UNECE type-approval regulations for vehicle components (E-mark), Regulation (EU) 2018/858 and (EU) 2019/2144 (general safety); Machinery Regulation (EU) 2023/1230 (CE marking for machinery and tools, applies from 20 January 2027) (`eu_unece_type_approval`, `eu_machinery_regulation_2023_1230`) | Replacement components subject to type approval (lighting, braking components, tyres, mirrors, glazing); machinery and power tools | pre_market (type approval; conformity assessment); labelling_element (E-mark with approval number; CE marking) | Approval number and marking → CMP_compliance_declarations | Ongoing; machinery regulation from 20 January 2027 | Retrieved (not spot-verified) |

### D.5 United Kingdom (GB)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-UK-1 | Carriage of Dangerous Goods and Use of Transportable Pressure Equipment Regulations 2009 (ADR as applied in GB); UK REACH and GB CLP — HSE (`uk_carriage_dangerous_goods_2009`, `uk_reach_clp`) | Dangerous goods in transport; hazardous substances and mixtures | transport; documentation (SDS); labelling_element | As for D-EU-1 and D-EU-2 with GB-specific formats → CMP_dangerous_goods, MED_technical_documents (SDS) | Ongoing | Retrieved (not spot-verified) |
| D-UK-2 | Regulation (EU) 2020/740 as retained in GB (tyre labelling) — DfT/OPSS (`uk_tyre_label_retained_2020_740`) | C1, C2 and C3 tyres | rating_label; listing_element | Tyre label and product information sheet displayed close to the price online, as in the EU scheme (no EPREL) → CMP_compliance_declarations (scheme `uk_tyre_label_retained_2020_740`), listing projection | Ongoing | Verified in part 2026-09-20 [P7] (retained text on legislation.gov.uk read; post-2021 GB amendments not checked) |
| D-UK-3 | Supply of Machinery (Safety) Regulations 2008; UKCA or CE marking with indefinite CE recognition from 1 October 2024 — OPSS (`uk_machinery_regulations_2008`) | Machinery and power tools | pre_market; labelling_element | Conformity marking choice, DoC, manufacturer and importer identification → CMP_compliance_declarations | CE recognition indefinite from 1 October 2024 | Verified in part 2026-09-20 (CDS-1800 [E16] sector table lists machinery among the 2024 regulations) |

### D.6 Canada (CA)

| Ref | Instrument / regulator | Applies to | Obligation | Required data elements → CDS field | Trigger / dates | Verification |
|---|---|---|---|---|---|---|
| D-CA-1 | Transportation of Dangerous Goods Act 1992 and Regulations — Transport Canada (`ca_tdg_regulations`); Hazardous Products Act and Hazardous Products Regulations (WHMIS 2015, GHS-aligned) for workplace products; Consumer Chemicals and Containers Regulations 2001 (CCCR) under the Canada Consumer Product Safety Act for consumer chemical products (no SDS requirement, consumer labelling instead) — Health Canada (`ca_whmis_2015`, `ca_cccr_2001`) | Dangerous goods in transport; workplace hazardous products; consumer chemical products sold at retail | transport; documentation (SDS for workplace products only); labelling_element (CCCR hazard symbols and bilingual statements for consumer products) | TDG classification → CMP_dangerous_goods; SDS for products not sold at retail in the same container size → MED_technical_documents with exemption reason (R052); CCCR consumer labelling → MF_warning_statements (bilingual) | Ongoing | Verified in part 2026-09-20 [P9] (secondary source on the HPA consumer-product exclusion; regulations not read) |
| D-CA-2 | Motor Vehicle Safety Act; Canada Motor Vehicle Safety Standards (CMVSS) — Transport Canada (`ca_cmvss_equipment`) | Regulated motor vehicle equipment (tyres, lighting, brake hoses, child restraints) | pre_market; labelling_element (national safety mark or DOT equivalents as recognised) | Compliance marking → CMP_compliance_declarations | Ongoing | Retrieved (not spot-verified) |

### D.7 Other markets

| Jurisdiction | Status | Note |
|---|---|---|
| Japan (JP), China (CN), Republic of Korea (KR), India (IN), Brazil (BR) and others | Not seeded | Vehicle-equipment approval (for example JIS marks, CCC certification, KC marks, BIS, INMETRO) and chemical regimes differ; organisation supplies entries with local advice. All UN Model Regulations-aligned transport regimes share the UN number, class and packing-group vocabulary seeded in the `dangerous_goods_class` dictionary. |

END OF CDS-1900 v0.2 REVIEW DRAFT
