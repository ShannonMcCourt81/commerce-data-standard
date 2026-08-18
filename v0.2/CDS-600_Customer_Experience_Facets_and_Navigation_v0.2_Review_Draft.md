# Commerce Data Standard (CDS)
## CDS-600 — Customer Experience, Facets and Navigation

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-600 Working Draft v0.1 |
| Normative status | §1, §3, §5–§29 are normative. §2, §4, §30–§32 and all appendices are informative. Examples and notes inside normative sections are informative unless marked otherwise. |
| Findings addressed | SYS-1 (CLEANUP-PASS §C: all 118 prefix-labelled rules corrected — 76 different-inline-keyword, 42 label-strip-only), SYS-2 (requirement IDs), SYS-4, CDS-600-2, CDS-600-3 (D10), CDS-600-4, CDS-600-5, CDS-600-6 (D11), CDS-600-7, CDS-600-8, CDS-600-9, CDS-600-10, CDS-600-11 |

CDS-600 is the single normative home for facets and customer-experience projection (CDS000-R005), including zero-result and unavailable facet-value behaviour (§17, per open decision D10). CDS-1500 and other chapters cite this chapter and do not restate its rules.

---

## 1. Purpose and Scope *(normative)*

CDS-600 defines how canonical product information is projected into customer-facing discovery experiences: site navigation, category and collection pages, facets, search refinement, sorting, product-card presentation, and the governance that keeps those experiences coherent as a catalogue grows. It does not prescribe a visual design system; it specifies the information, behaviour and quality rules beneath the interface so that different storefronts may implement distinct designs without weakening customer comprehension or data integrity.

**CDS600-R001** A CDS implementation MUST derive customer-facing discovery structures from governed product information rather than from uncontrolled labels entered independently in the storefront.

**CDS600-R002** Customer-facing simplification MUST NOT destroy the richer canonical or source information held by the PIM.

**CDS600-R003** A storefront MAY vary presentation by device, market or audience, provided the underlying meaning remains consistent.

## 2. Customer Experience Principles *(informative)*

- **Customer language first** — labels use terms customers understand, even when internal or channel taxonomies use different wording.
- **Progressive disclosure** — reveal enough structure to support a decision without presenting the whole data model at once.
- **Controlled simplicity** — rich canonical data is grouped into concise facets and navigation choices (CDS-P-08).
- **Predictable behaviour** — the same control and value behaves consistently across categories unless a documented category profile requires otherwise.
- **No dead ends** — filtering and search minimise preventable zero-result states and provide useful recovery (§17).
- **Availability-aware discovery** — customers are not encouraged toward choices that cannot produce a purchasable result (§16–§17).
- **Accessible by default** — discovery controls remain understandable and operable without relying on colour, pointer input or visual position alone (§24, normative).
- **Measurable quality** — facet, search and navigation performance is evaluated with behavioural and data-quality evidence (§28).

## 3. Experience Architecture *(normative)*

```
Canonical Product Information
  |-- Internal Taxonomy
  |-- Controlled Dictionaries
  |-- Attribute and Variant Values
  `-- Merchandising Rules
          |
          v
Customer Experience Projection
  |-- Navigation and Category Pages
  |-- Collections and Facets
  |-- Search, Sort and Ranking
  `-- Product Card Presentation
          |
          v
Experience Analytics and Health
```

**CDS600-R004** Customer experience structures MUST be treated as projections of canonical information, not as independent product facts.

**CDS600-R005** The PIM or governed commerce layer SHOULD be able to explain which canonical values and rules produced each customer-facing label, filter and collection membership.

## 4. Shopping Modes and Customer Intent *(informative)*

| Mode | Typical behaviour | Primary support |
|---|---|---|
| Directed search | Customer knows a product, brand, model or requirement | Search, synonyms, identifiers, relevance ranking |
| Category browsing | Customer knows the general kind of product | Navigation, categories, collections, breadcrumbs |
| Attribute refinement | Customer narrows by colour, size, material, room or specification | Facets and counts |
| Inspirational discovery | Customer begins with a style, occasion, campaign or need | Editorial collections, merchandising, cross-links |
| Comparison | Customer evaluates similar products | Consistent attributes, sorting, comparison-ready presentation |

A taxonomy answers what a product *is*. Merchandising and facets help customers discover why it may be *relevant* to them.

## 5. Taxonomy, Navigation, Collections, Facets and Search *(normative)*

| Construct | Primary question | Typical source |
|---|---|---|
| Taxonomy / category | What is this product? | Internal classification (CDS-200 §6) |
| Navigation | Where should customers begin browsing? | Selected category and collection nodes |
| Collection | Which products should be presented together? | Taxonomy, merchandising rules or curation |
| Facet | Which characteristic should refine the current result set? | Controlled attribute projection (CDS-400) |
| Search | Which products are relevant to this query? | Index, synonyms, attributes, ranking signals |

**CDS600-R006** These constructs MUST remain logically distinct even when a platform implements more than one of them with the same technical feature.

**CDS600-R007** A collection MUST NOT be treated as a substitute for a missing controlled attribute when customers need to refine by that attribute.

**CDS600-R008** A facet MUST NOT be used to redefine a product category.

## 6. Navigation Architecture *(normative)*

Navigation is a curated entry into the catalogue, not a complete rendering of every internal category. It exposes stable, meaningful destinations and defers fine-grained refinement to facets.

**CDS600-R009** Primary navigation SHOULD expose no more than the levels required for customers to orient themselves and reach a useful product set.

**CDS600-R010** Deep internal taxonomy nodes MAY remain available through category pages, search or links without appearing in the main menu.

**CDS600-R011** Navigation labels MUST have clear, non-overlapping meanings within the same level.

**CDS600-R012** A product MAY be discoverable from multiple navigation paths while retaining one primary internal category (CDS-200 §6).

> Informative note: the one-primary-category rule protects classification integrity. Cross-links and collections solve merchandising overlap without duplicating product identity.

## 7. Category and Collection Architecture *(normative)*

Category pages represent product types or taxonomy nodes. Collections represent merchandising groupings such as New Arrivals, Winter Edit or Staff Picks. Both may be customer-facing, but they carry different meanings.

**CDS600-R013** A category page SHOULD inherit its product membership from classification or an equivalent deterministic rule.

**CDS600-R014** A merchandising collection MUST declare whether membership is computed, manually curated or hybrid.

**CDS600-R015** Temporary collections SHOULD have an owner, activation window and retirement rule.

**CDS600-R016** Parent pages SHOULD explain their scope and provide clear paths to child categories or relevant facets.

## 8. Information Scent and Labels *(normative)*

Information scent is the customer's ability to predict what lies behind a label or control. Weak labels force experimentation; strong labels make the catalogue feel smaller and more understandable.

**CDS600-R017** Navigation, collection and facet labels MUST be written in customer language and SHOULD avoid internal abbreviations.

**CDS600-R018** A label MUST distinguish neighbouring choices. Terms such as Other, General or Miscellaneous SHOULD be avoided unless no clearer grouping exists.

**CDS600-R019** Where a term is ambiguous across industries or regions, the label SHOULD include qualifying context.

**CDS600-R020** Synonyms MAY support search, but the interface SHOULD present one preferred label per concept.

## 9. Facet Model and Facet Definitions *(normative)*

A facet is a customer-facing refinement dimension (CDS-100). A Facet Definition governs its label, values, applicability, selection behaviour, ordering, counts, visibility and mapping from canonical attributes.

| Property | Requirement |
|---|---|
| Stable ID | Machine identifier independent of display label |
| Label | Localisable customer-facing name |
| Description | Meaning and inclusion boundaries |
| Source | Canonical attribute or derived rule |
| Eligibility | Applicable categories, collections or search contexts |
| Value model | Dictionary, numeric range, boolean or hierarchy |
| Selection mode | Single-select, multi-select or range |
| Within-facet operator | OR or AND within the facet |
| Count unit and method | Products, purchasable variants or another declared unit; count semantics per §16 |
| Ordering | Semantic, numeric, popularity or alphabetic |
| Disclosure | Expanded, collapsed, hidden or conditional |
| Unavailable-value behaviour | Per §17 |
| Analytics key | Stable event identifier |
| Owner | Responsible data or merchandising role |

**CDS600-R021** Every customer-facing facet MUST have a governed Facet Definition.

**CDS600-R022** Facet values MUST come from controlled canonical or facet dictionaries (CDS-400), not from unrestricted distinct strings.

**CDS600-R023** The same logical facet SHOULD retain one identifier across channels even where the display label is localised.

**CDS600-R024** A Facet Definition MUST declare its count unit (products, purchasable variants or another declared unit) and its count method (§16).

**CDS600-R025** A Facet Definition MUST declare its selection logic; interfaces MUST NOT rely on undocumented platform defaults.

**CDS600-R026** How facets combine across a result set is a property of the facet set, not of an individual facet. The cross-facet operator MUST be declared at the facet-set (category- or context-profile) level, and a Facet Definition MUST NOT carry its own cross-facet operator. *(Resolves CDS-600-4; see §15 and Appendix A.)*

## 10. Facet Eligibility *(normative)*

Not every attribute should become a filter. Eligibility is determined by customer usefulness, coverage, value distribution, category relevance and interface cost:

| Criterion | Question |
|---|---|
| Decision relevance | Does the attribute meaningfully affect product choice? |
| Coverage | Is the value populated for enough products in the eligible result set? |
| Discrimination | Does the facet divide the catalogue into useful groups rather than one dominant value and many singletons? |
| Comprehension | Will customers understand the values without specialist knowledge? |
| Stability | Are values governed and unlikely to change unpredictably? |
| Result utility | Will selecting a value usually leave a useful product set? |
| Maintenance | Can the organisation govern the dictionary and mappings? |

**CDS600-R027** A field MUST NOT become a facet merely because the platform permits filtering on it.

**CDS600-R028** Facet eligibility SHOULD be reviewed per category profile rather than globally.

**CDS600-R029** Low-coverage or highly fragmented facets SHOULD remain hidden until data quality and grouping are adequate (thresholds per §28).

## 11. Value Projection for Facets *(normative)*

The value-layer model (Source Value -> Alias Mapping Record -> Canonical Value -> projections) is owned by CDS-400 and defined per ADR-D4; terms per CDS-100 §3. Facet Values are one projection branch:

```
Canonical Value
  +--> Display Label
  +--> Facet Value
  +--> Search Synonyms
  +--> Channel Representation
```

**CDS600-R030** Facet values MUST be projections of canonical values and MUST NOT replace those canonical values in the PIM.

**CDS600-R031** Many canonical values MAY map to one broader facet value when that grouping improves customer comprehension.

**CDS600-R032** A canonical value MAY map to more than one facet group only where the secondary membership is deliberate, documented and non-deceptive.

## 12. Colour Facets *(normative)*

Colour is a high-risk facet because suppliers and brands use rich marketing names while customers generally need a concise set of recognisable families. CDS separates the sellable colour, its Display Label and its facet family.

**CDS600-R033** *(Definition — resolves CDS-600-7.)* The **sellable colour** of a Variant is the canonical value of its colour Variant Option (CDS-100 §2–§3). What the customer sees is that canonical value's Display Label (e.g. "French Navy"); what filtering uses is the Facet Value the canonical value maps to (e.g. Blue). Implementations MUST maintain this distinction; the Display Label is never itself the canonical value.

```
Display Label (sellable colour as shown):  French Navy
Canonical value:                           colour_french_navy (shade: navy)
Primary facet family:                      Blue
Optional tone:                             Dark
Search synonyms:                           navy, dark blue, french navy
Swatch:                                    governed visual sample
```

**CDS600-R034** A colour facet MUST use a controlled colour-family dictionary rather than exposing every display colour as a separate filter value.

**CDS600-R035** The storefront MAY display the sellable colour's Display Label on the product card or product page while filtering by the broader family.

**CDS600-R036** Colour swatches MUST NOT be the sole means of communicating a value; a text label MUST remain available (§24).

**CDS600-R037** Multi-colour, transparent, metallic and natural finishes SHOULD be modelled explicitly rather than forced into an inaccurate basic hue. Multicolour is a facet/status value, never a canonical shade (CDS-100 §3).

**CDS600-R038** Where a product contains several meaningful colours, the system SHOULD distinguish primary colour, secondary colour and multicolour status.

> Informative note *(resolves CDS-600-6 per D11)*: the exemplar colour-family baseline — including the core family set and the boundary rules for neighbours such as Cream/Beige/Natural/White and Silver/Grey — is owned by CDS-1500 Appendix C. This chapter deliberately publishes no family list of its own; the exact dictionary remains profile-specific and is adopted from that baseline.

## 13. Size, Fit and Dimension Facets *(normative)*

Size information is frequently variant-level and may use category-specific scales. Fit describes intended garment shape and normally remains product-level. Dimensions may require units and ranges rather than labels.

**CDS600-R039** Size facets MUST preserve the distinction between the displayed size label and the normalised size order or scale.

**CDS600-R040** A category profile MUST define which size system applies (e.g. alpha, numeric apparel, footwear, waist, bedding, dimensional).

**CDS600-R041** Size values MUST sort semantically rather than alphabetically.

**CDS600-R042** Fit MUST NOT be inferred from size alone.

**CDS600-R043** Numeric dimension facets SHOULD use normalised units and MAY present customer-local units.

> Informative note: a size label of 10 may represent different measurements in different markets. CDS therefore requires profile and unit context rather than treating the visible label as a universal canonical value.

## 14. Material, Style, Pattern, Occasion and Room Facets *(normative)*

| Facet | Canonical detail | Typical facet projection |
|---|---|---|
| Material | linen; cotton; oak; stoneware | Linen; Cotton; Wood; Ceramic |
| Composition | 80% cotton / 20% polyester | Cotton or Cotton Blend, per declared policy |
| Pattern | fine white pinstripe | Striped |
| Style | relaxed coastal resort shirt | Coastal and/or Relaxed, per profile |
| Occasion | beach holiday | Beach / Holiday |
| Room | living room cushion | Living Room |
| Finish | natural Tasmanian oak | Natural / Wood |

**CDS600-R044** Material composition MUST remain separately available from the simplified material facet where percentages or blends matter.

**CDS600-R045** Style and occasion facets SHOULD use a small governed vocabulary and MUST NOT become an uncontrolled list of marketing phrases.

**CDS600-R046** Homewares facets SHOULD be category-aware; a Room facet may be useful for decor but irrelevant for cookware components. *(Industry baselines: CDS-1500.)*

## 15. Selection Logic *(normative)*

Selection logic determines how multiple chosen values combine. The intended logic must be explicit because platforms and customers may otherwise interpret the same control differently. Cross-facet combination is declared per facet set (CDS600-R026).

**CDS600-R047** Different facets SHOULD combine with AND logic (Blue AND Linen), as the declared facet-set default.

**CDS600-R048** Multiple values within the same categorical facet SHOULD combine with OR logic (Blue OR Green).

**CDS600-R049** An AND-within-facet mode MAY be used where a product must possess all selected values, but the interface MUST make that behaviour clear.

**CDS600-R050** Single-select facets MUST prevent contradictory simultaneous choices.

**CDS600-R051** A range facet MUST define inclusive boundaries, units and rounding behaviour.

```
Selected:
  Colour: Blue OR Green
  Material: Linen
  Size: M OR L
Result logic:
  (Blue OR Green) AND Linen AND (M OR L)
```

## 16. Counts and Variant Availability *(normative)*

Facet counts can represent products or sellable variants. Availability-aware variant counting ensures that selecting Blue and Size M returns products with a purchasable Blue/M combination, not products that merely have Blue somewhere and M somewhere.

**CDS600-R052** Facet counts MUST declare their counting unit and availability scope (CDS600-R024).

**CDS600-R053** Variant-defined facets SHOULD evaluate valid variant combinations rather than independent product-level unions.

**CDS600-R054** Where the storefront platform supports combination-level availability filtering, a product MUST NOT be counted as satisfying a selected combination unless at least one eligible sellable unit satisfies the complete selected combination.

**CDS600-R055** Where the storefront platform does not support combination-level availability filtering, the implementation MUST disclose that limitation in its platform profile (CDS-900) and SHOULD approximate combination behaviour as closely as the platform allows. *(Resolves CDS-600-2.)*

> RESOLVED (was CDS-600-2 (resolved); verified 2026-08-04, REVIEW-006A): the conditional structure of R054/R055 stands (it is the correct platform-neutral form), and the pending question is answered — **native Shopify Search & Discovery evaluates variant-option and availability filters at variant scope** (`filter.v.option.*`, `filter.v.availability`; different filters AND at variant level), so the Shopify profile declares the capability present (CDS-900 §4.7). Per-value count accuracy under combined selections remains a vertical-slice empirical check.

> Informative note *(preserved)*: R054 prevents the classic false-positive result where a shirt has Blue only in Small and Medium only in White, yet appears after Blue + Medium is selected.

**CDS600-R056** *(Disjunctive count semantics — resolves CDS-600-5.)* Within a multi-select OR facet, the count displayed for an unselected value MUST be computed against the result set produced by all *other* facet selections, excluding that facet's own current selection, so that the count predicts the effect of adding the value rather than reporting the already-filtered set. The count method in force MUST be declared in the Facet Definition (CDS600-R024).

**CDS600-R057** The interface SHOULD update counts or availability after each selection so customers can anticipate the effect of another filter.

## 17. Unavailable Values and Zero-Result Recovery *(normative — single normative home per D10)*

This section is the corpus-wide normative home for zero-result and unavailable facet-value behaviour. CDS-1500 §19 and any other chapter cite this section and MUST NOT restate or vary these rules. The stricter CDS-1500 wording is adopted here as the governing MUST. *(Resolves CDS-600-3.)*

**CDS600-R058** A facet value whose selection would produce no truthful available result in the current context MUST be disabled or hidden.

**CDS600-R059** As a governed exception to R058's hiding branch, out-of-stock values MAY remain visible for discovery only where the interface presents a clear unavailable state; unavailable values MUST be distinguished from purchasable options and MUST NOT be presented as normally selectable.

**CDS600-R060** When no results remain, the interface MUST preserve the selected filters and provide a clear recovery action.

**CDS600-R061** Recovery SHOULD identify the narrowest selected constraint or offer removal of one filter at a time.

**CDS600-R062** A zero-result message MUST NOT imply that the store has no relevant products when the result is caused by an over-restrictive combination.

## 18. Ordering, Defaults and Disclosure *(normative)*

Facet order and value order are part of the merchandising experience. Alphabetical sorting is appropriate only when it matches how customers think about the values.

**CDS600-R063** High-value decision facets SHOULD appear before secondary descriptive facets.

**CDS600-R064** Size, numeric ranges and lifecycle stages MUST use semantic order rather than alphabetical order.

**CDS600-R065** Colour families MAY use a stable merchandising order or a visual palette order, provided labels remain accessible.

**CDS600-R066** Long value lists SHOULD use search, grouping or progressive disclosure rather than expanding the page indefinitely.

**CDS600-R067** A facet SHOULD be expanded by default only when it is broadly useful in the current context.

## 19. Mobile and Responsive Filtering *(normative)*

**CDS600-R068** Mobile filtering MUST expose the number of active filters and provide a persistent way to clear or edit them.

**CDS600-R069** An apply action MAY defer result updates inside a mobile filter panel; where it does, the apply control MUST display a preview of the result count that will apply, and selected counts and availability SHOULD remain understandable while the panel is open. *(Resolves CDS-600-9.)*

**CDS600-R070** Filter controls MUST remain operable with touch targets, keyboard navigation and assistive technology (§24).

**CDS600-R071** A long mobile facet list SHOULD support internal search or grouping rather than forcing excessive scrolling.

**CDS600-R072** Closing the filter interface MUST preserve current selections unless the user explicitly cancels them.

## 20. Search, Synonyms and Query Understanding *(normative)*

Search and facets share dictionaries but serve different interactions: search interprets free-form intent; facets expose governed choices.

**CDS600-R073** Search indexes SHOULD include canonical values, display labels, approved aliases and relevant facet families.

**CDS600-R074** A search synonym MUST map to a preferred concept or query expansion and MUST NOT create an uncontrolled duplicate value.

**CDS600-R075** Brand, SKU, MPN and GTIN identifiers SHOULD be indexed according to access and relevance requirements.

**CDS600-R076** Search query interpretation MAY infer a facet selection, but the resulting refinement SHOULD be visible to the customer.

**CDS600-R077** Misspelling tolerance and semantic expansion MUST NOT override exact product identifiers or create materially misleading results.

```
Query: "navy linen shirt"
Interpreted intent:
  Product type = Shirt
  Colour facet = Blue / canonical navy
  Material facet = Linen
Visible refinements:
  Shirts | Blue | Linen
```

## 21. Sorting and Ranking *(normative)*

**CDS600-R078** Every sort option MUST declare the data and tie-breakers used.

**CDS600-R079** Price sorting MUST use the same customer-visible price basis used in the current market and tax context.

**CDS600-R080** Newness SHOULD use a governed publication or arrival date, not an arbitrary last-edit timestamp.

**CDS600-R081** Relevance ranking MAY use behavioural signals, but product-data completeness and availability SHOULD remain quality inputs.

**CDS600-R082** Sponsored or commercially influenced ranking MUST be identifiable where applicable.

> Informative note: Best Selling, Featured and Recommended are not self-defining technical fields. Each requires a documented calculation or merchandising owner.

## 22. Product Cards and Variant Presentation *(normative)*

**CDS600-R083** A product card SHOULD display the attributes necessary to distinguish neighbouring products without reproducing the entire product page.

**CDS600-R084** Variant swatches or size indicators MUST reflect actual eligible variants and availability.

**CDS600-R085** A colour swatch SHOULD use the governed Display Label and visual sample, while its filter behaviour uses the facet family.

**CDS600-R086** Product-card badges such as New, Sale, Clearance or Exclusive MUST originate from governed lifecycle or merchandising rules.

**CDS600-R087** A product card MUST NOT show an unavailable price or variant as though it were the active purchasable choice.

## 23. Breadcrumbs, Cross-Links and Merchandising Overlap *(normative)*

**CDS600-R088** Breadcrumbs SHOULD reflect the chosen customer navigation context while remaining consistent with the primary category model.

**CDS600-R089** Cross-links MAY surface a product to another audience without assigning a second primary category.

**CDS600-R090** Editorial and campaign pages SHOULD link back to stable category or collection destinations where customers can continue browsing.

**CDS600-R091** A product appearing in several collections MUST retain one canonical identity and one primary classification.

## 24. Accessibility *(normative)*

**CDS600-R092** Facet groups and controls MUST have programmatically determinable labels.

**CDS600-R093** Selected state, disabled state and result counts MUST be exposed to assistive technology.

**CDS600-R094** Colour swatches and colour indicators MUST include text alternatives, and colour MUST NOT be the sole signal for any value, state or distinction.

**CDS600-R095** Keyboard focus MUST follow a logical order and remain visible.

**CDS600-R096** Changes to result counts MUST be announced to assistive technology without causing disruptive focus movement.

**CDS600-R097** Clear-all and remove-filter controls MUST have unambiguous accessible names.

**CDS600-R098** Range controls MUST expose current values, minimum, maximum and units.

## 25. Performance and Resilience *(normative)*

**CDS600-R099** An implementation MUST declare a response-time target for facet and filter interactions and MUST monitor performance against that declared target. *(Resolves CDS-600-8; replaces the untestable "quickly enough" wording.)*

> Informative note: the intent of the target is that the interface preserves a direct, perceptible relationship between a selection and its response.

**CDS600-R100** The storefront MUST fail safely when a facet service is unavailable; product browsing SHOULD remain possible.

**CDS600-R101** Cached counts MUST identify their freshness and MUST NOT be presented as live availability when they are materially stale relative to the declared target and propagation windows.

**CDS600-R102** Large dictionaries SHOULD support indexed lookup rather than rendering all values unconditionally.

**CDS600-R103** Performance optimisation MUST NOT change selection semantics or counts without explicit disclosure.

## 26. Faceted Navigation and SEO *(normative)*

Faceted combinations can create an unbounded number of URLs. CDS does not prescribe one search-engine policy, but requires explicit governance so that customer refinement does not accidentally generate a duplicate crawl space.

**CDS600-R104** An implementation MUST define which facet combinations are indexable, canonicalised, blocked or represented without unique URLs.

**CDS600-R105** Indexable landing pages SHOULD have stable intent, sufficient product depth and unique explanatory content.

**CDS600-R106** Transient or extremely narrow combinations SHOULD NOT become indexable pages by default.

**CDS600-R107** The canonical category and collection structure MUST remain discoverable independently of facet-generated URLs.

**CDS600-R108** SEO policy MUST NOT weaken customer filter behaviour merely to simplify crawling.

## 27. Personalisation and AI *(normative)*

AI proposal, evidence, approval and autonomy rules are owned by CDS-700; dictionary authority by CDS-400. This section carries only the customer-experience rules.

**CDS600-R109** Personalisation MAY reorder facets, values or products but MUST NOT change the semantic meaning of a facet.

**CDS600-R110** A personalised interface MUST retain a predictable way to access the full applicable filter set.

**CDS600-R111** Sensitive personal inference MUST NOT be required for ordinary product discovery.

> Informative note: AI may suggest facet mappings, synonyms, labels and collection memberships only as proposals under CDS-700 governance; governed dictionaries and approval rules remain authoritative (CDS-400, CDS-700).

## 28. Measurement and Analytics *(normative)*

| Measure | Examples *(informative)* |
|---|---|
| Facet usage | Selections, removals, clear-all events and sequence |
| Result quality | Zero-result rate, low-result rate and recovery |
| Coverage | Percentage of eligible products populated per facet |
| Fragmentation | Number of values, singleton values and long-tail share |
| Discovery | Search-to-filter transitions and navigation depth |
| Conversion support | Outcome after facet or search interaction |
| Performance | Response latency against the declared target (R099) |
| Accessibility | Keyboard and assistive-technology defects |
| Data drift | Unexpected values or missing mappings |

**CDS600-R112** Analytics identifiers MUST remain stable when display labels change.

**CDS600-R113** Facet analytics SHOULD distinguish exposure, interaction and resulting product-set size.

**CDS600-R114** The organisation MUST declare its thresholds for facet usage and facet coverage. A facet whose usage exceeds the declared usage threshold while its coverage falls below the declared coverage threshold MUST trigger data-quality review rather than automatic removal. *(Resolves CDS-600-11; replaces the untestable "high-use facet with poor coverage".)*

## 29. Governance and Change Management *(normative)*

Roles, decision rights and change control in general are owned by CDS-800; dictionary and mapping workflows by CDS-400. This section carries the facet-specific rules.

**CDS600-R115** Every facet MUST have an owner responsible for definition, dictionary, coverage and retirement.

**CDS600-R116** New facet values MUST enter through the governed dictionary or mapping workflows defined in CDS-400.

**CDS600-R117** Renaming a visible label SHOULD preserve the stable facet and value identifiers.

**CDS600-R118** Merging or splitting values MUST include migration, publication, search and analytics impact analysis.

**CDS600-R119** Facet changes SHOULD be tested against representative categories, devices and product combinations before release.

**CDS600-R120** Deprecated values MUST retain aliases or redirects long enough to protect imports, saved URLs and historical analytics where applicable.

## 30. Worked Examples *(informative)*

### 30.1 Apparel: colour and size

```
Product: Relaxed Linen Shirt
Variants:
  French Navy / S / in stock
  French Navy / M / out of stock
  White / M / in stock
Canonical:
  colour: colour_french_navy -> facet Blue (Display Label "French Navy")
  colour: colour_white       -> facet White
  size scale: Alpha Apparel
Customer selects Blue + M:
  Product excluded — no purchasable Blue/M variant exists (R054).
Customer selects Blue:
  Product included; product card shows "French Navy" (R035).
```

### 30.2 Homewares: material and room

```
Product: Tasmanian Oak Side Table
Canonical material: oak            Display material: Tasmanian Oak
Material family facet: Wood        Room facets: Living Room, Bedroom
Style facet: Contemporary
Filters on Side Tables collection: Material, Colour, Style, Shape, Width, Price
Room may remain available on a broader Furniture collection (R046).
```

### 30.3 Pattern simplification

```
Display pattern: Fine White Pinstripe
Canonical pattern: pinstripe
Facet value: Striped
Search aliases: pinstripe, stripe, striped
```

The customer sees "Striped" in filters and "Fine White Pinstripe" on the product page.

## 31. Conformance *(informative)*

Conformance levels, test suites and claim rules are defined solely in CDS-1000 (CDS000-R012). CDS-600 conformance is assessed against the requirement IDs in this chapter; the UX-oriented test suite (T-UX) covers them per CDS-1000. No conformance content is defined here.

## 32. Design Decision Summary *(informative)*

Chapter-level ADRs from v0.1 are queued for the single global ADR register (CDS000-R006). Their substance, as carried forward:

| v0.1 ADR | Decision as carried into v0.2 |
|---|---|
| CDS-ADR-601 | Facet values are projections, separate from canonical values (§11) |
| CDS-ADR-602 | Taxonomy and collections remain distinct (§5, §7) |
| CDS-ADR-603 | Colour filters use controlled families; the exemplar baseline is owned by CDS-1500 App C (§12, D11) |
| CDS-ADR-604 | Within-facet OR and cross-facet AND are the defaults; cross-facet combination is a facet-set property (§15, CDS-600-4) |
| CDS-ADR-605 | Variant combinations determine availability-aware results, conditional on platform capability with mandatory disclosure (§16, CDS-600-2) |
| CDS-ADR-606 | Facet Definitions are first-class governed entities (§9) |
| CDS-ADR-607 | Faceted SEO policy is implementation-specific but mandatory (§26) |

---

## Appendix A. Recommended Facet Definition and Facet-Set Schemas *(informative)*

Per-facet definition (cross_facet_operator removed per CDS600-R026):

```
facet_id
label
localised_labels
source_attribute_ids
eligible_category_ids
value_dictionary_id
selection_mode
within_facet_operator
count_unit
count_method            # incl. disjunctive-count semantics per R056
availability_policy     # unavailable-value behaviour per section 17
value_sort_strategy
facet_sort_priority
default_disclosure
mobile_presentation
accessible_label
analytics_id
owner
status
version
created_at
updated_at
```

Facet-set / category-context profile (holds what was per-facet in v0.1):

```
facet_set_id
context                 # category, collection or search context
member_facet_ids        # ordered
cross_facet_operator    # normally AND (R047)
response_time_target    # declared per R099
owner
version
```

## Appendix B. Industry Facet Baselines *(informative)*

The apparel and homewares facet profiles and the exemplar colour-family baseline formerly in this chapter's Appendices B and C are owned by CDS-1500 (industry dictionaries and profiles; colour families in CDS-1500 Appendix C). *(Resolves CDS-600-10.)*

## Appendix C. Platform Implementation Profiles *(informative)*

Platform-specific guidance (including the former Shopify implementation notes) lives in versioned, dated CDS-900 profiles. Platform declarations relevant to this chapter: combination-level availability filtering capability (R054/R055) and any facet value/group limits.

## Appendix D. Operational Review Checklist *(informative)*

- Are primary categories and collections clearly distinguished?
- Does every visible facet have a definition, owner and controlled value source?
- Are colour values grouped into a manageable customer-facing dictionary (per the CDS-1500 baseline)?
- Are size values ordered by the correct category and market scale?
- Do variant combinations produce truthful availability-aware results, or is the platform limitation disclosed?
- Are low-coverage and highly fragmented facets hidden or remediated against declared thresholds?
- Can customers recover easily from zero results?
- Are mobile controls accessible, and do deferred-apply controls preview the result count?
- Are search synonyms governed rather than invented per product?
- Are facet URLs and indexing rules documented?
- Are facet analytics stable across display-label changes?
- Are customer-facing values verified after publication (CDS-500)?
- Is the declared response-time target being monitored?
