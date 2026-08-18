# CDS Reference Dictionary

*(Package version: see `manifest.json` — the folder is deliberately unversioned so new chapters never force path changes.)*

**In plain English:** this is the CDS word-book — every controlled vocabulary the standard uses, in one place, organised into chapters like a real dictionary. Each CSV file is one vocabulary (colours, materials, care instructions, heel heights…). The companion `CDS_Dictionary.pdf` at the repository root is the same content as a readable book, generated directly from these files so the two can never disagree. Adopt these values as the starting content of your governed dictionaries; from then on you own and version them under CDS-400.

This package **unifies and supersedes** the former `CDS-1500_Starter_Reference_Dictionaries_v0.2` and `CDS_Dictionary_Expansion_Packs_v0.1` (both archived, contents carried forward unchanged — 28 files, 369 rows, zero data edits at merge).

## Chapters

| Ch. | Chapter | Files (dictionary_key) | Status |
|---|---|---|---|
| 1 | Colours | colour_facets, colour_reference_values | Bound to the published apparel + homewares profiles (CDS-1500) |
| 2 | Materials | apparel_materials, homewares_materials, material_facets | Bound (CDS-1500) |
| 3 | Fabrics & Construction | fabric_types | Bound (fills CDS-1500 E.3; constructions, never fibres) |
| 4 | Care | care_instructions | Bound (fills E.3; descriptive values, not the trademarked symbol set) |
| 5 | Sizing | size_systems | Bound (fills E.3; apparel + footwear systems) |
| 6 | Apparel Attributes | fits, styles, occasions, patterns, necklines, sleeve_types, garment_lengths, swim_styles | Bound (CDS-1500); the style vocabulary is shared across fashion and furniture/homewares |
| 7 | Homewares Attributes | rooms, finishes, shapes | Bound (CDS-1500) |
| 8 | Footwear | footwear_styles, footwear_heel_heights, footwear_closures, footwear_toe_shapes, footwear_width_fittings | Vocabulary ahead of profile — no published CDS profile binds these yet |
| 9 | Jewellery & Accessories | jewellery_metals, jewellery_stones, jewellery_closures, jewellery_styles | Vocabulary ahead of profile |
| 10 | Beauty & Personal Care | beauty_skin_types, beauty_hair_types, beauty_scent_families, beauty_formulations, beauty_makeup_finishes | Vocabulary ahead of profile |
| 11 | Electronics & Appliances | connectivity, screen_technologies, power_sources, installation_types, energy_rating_systems | Vocabulary ahead of profile (brown + white goods) |
| 12 | Sports & Outdoor | sport_activities, wetsuit_styles, wetsuit_thicknesses, wetsuit_zips, wetsuit_seams | Vocabulary ahead of profile ("shop by sport" + surf wetsuit attributes) |
| 13 | Toys & Games | play_types, toy_age_ranges | Vocabulary ahead of profile (retail age bands, not safety marks) |
| 14 | Pet Supplies | pet_types, pet_life_stages, pet_sizes | Vocabulary ahead of profile |
| 15 | Furniture | assembly_types | Vocabulary ahead of profile (styles live in the Chapter 6 style vocabulary; upholstery reuses Fabrics/Materials) |
| 16 | Garden & Outdoor | sun_exposure | Vocabulary ahead of profile (deliberately narrow — plant taxonomies and watering claims excluded) |

"Bound" chapters can carry requirement levels under CDS1500-R011 once adopted as governed data. "Ahead of profile" chapters are ready vocabulary; no requirement level may bind to them until an industry profile chapter exists.

## Key vs value, in one example

Every CSV is one **vocabulary** answering one question about a product. `dictionary_key` names the vocabulary (the *field*); `value_id` is the machine **code** stored as the answer; `label` is what people see. So for a navy cushion: the vocabulary `colour` asks "what colour is it?", the PIM stores the code `french_navy`, the product page shows **French Navy**, the storefront filter shows its broad family **Blue**, and if a supplier writes "dark navy" the aliases match it automatically. (The same worked example, with every PIM and Shopify field name spelled out, is Appendix A of the Setup Runbook.)

## Column contract (CDS-1500 Appendix E.1)

Every row: `dictionary_key, row_type (canonical|alias), value_id, label, maps_to, aliases, facet_ids, status, provenance, version, locale`. Declared extra columns: `definition` (colour_facets, footwear_heel_heights, energy_rating_systems, pet_life_stages, wetsuit_thicknesses, wetsuit_seams), `material_family` + `scope` (materials files), `care_group` (care_instructions), `scope` (material_facets).

- Delimiters: `;` between aliases, `|` between ordered facet_ids (first = primary).
- Matching: aliases match case-insensitively; codes match exactly.
- Locale: labels are en-GB.
- Row versions record each row's own content version (0.2.0-era rows and 0.1.0-era rows keep their values at this merge; they bump individually on change per CDS-400).
- `facet_ids` are populated only where a separate facet layer exists (colours, materials); chapters 3–10 are themselves facet-level vocabularies.

## Standing rules (carried forward)

- **No silent redefinition:** a published canonical code is never quietly given a new meaning — changes go through deprecation with replacement mappings.
- **Beauty claims exclusion:** benefit/marketing terms (anti-ageing, hypoallergenic, organic, vegan, cruelty-free…) are evidence-gated claims under CDS-700, never filter vocabulary. Same pattern as the Recycled material-facet exclusion.
- **Surfwear exclusions (0.7.0):** fin systems (FCS, Futures) are vendor ecosystems; water-temperature suitability ranges are variable claims (thickness and seam construction are the filterable facts); stretch/warmth marketing tiers (E-series, Ultra Stretch) are trademarked claims. Wetsuit thickness labels use the hyphen form (3-2mm) with the slash notation (3/2mm) as aliases, per the label rule.
- **Swimwear exclusions (0.6.0):** UPF sun-protection ratings are tested claims under AS/NZS 4399 (evidence-gated, numeric — a candidate rating-scheme entry for a profile, not facet vocabulary); "chlorine-resistant" is a durability claim. Swim styles themselves (one-piece, bikini, rash vest) are within-category style facets, same pattern as footwear styles.
- **Research-round exclusions (0.5.0):** toy safety marks and "educational/STEM" benefit terms; pet health claims and breed taxonomies; sports performance claims (moisture-wicking, quick-dry) and skill levels; furniture numeric specs (seating capacity); plant taxonomies and watering/maintenance claims; age-state claims ("mature" skin); trademarked fibres (Tencel, Lycra, Gore-Tex — generic names used instead); "bamboo" alone as a TEXTILE fibre name (prohibited under fibre-labelling rules — apparel uses Bamboo Viscose with bamboo as an alias). Bamboo the plant material remains a valid homewares canonical (furniture, boards, blinds) — the rule is textile-scoped.
- **Electronics exclusions:** compliance marks (CE, RCM) and efficiency *claims* ("energy efficient") are evidence-gated, never filter vocabulary — the regulated rating value under a declared scheme is the filterable fact. Vendor ecosystems (Alexa, HomeKit, Chromecast) and per-category configuration sets (top- vs front-loader; french-door vs side-by-side) are left for an electronics profile chapter. Appliance finishes reuse the Colours/Materials chapters.
- **Country of origin** is deliberately not shipped: generate from the current ISO 3166 list at adoption time.
- Channel mappings are out of scope for seed data; add per-value channel mappings under CDS-400 §11 as needed.

## Integrity

`SHA256SUMS.txt` covers every CSV + this README (`shasum -a 256 -c SHA256SUMS.txt`). `manifest.json` is the version authority (the folder is deliberately unversioned); it lists per-file hashes, the chapter map, and a `package_hash` over the sorted file-hash lines (manifest itself excluded).
