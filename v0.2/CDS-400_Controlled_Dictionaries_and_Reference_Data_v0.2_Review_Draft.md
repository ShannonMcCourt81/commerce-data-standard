# Commerce Data Standard (CDS)
## CDS-400 — Controlled Dictionaries and Reference Data

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-400 Working Draft v0.1 |
| Normative status | §1, §3–§18, §20–§28 and §30 are normative. §2, §19 (baseline note), §29, §31 and all appendices are informative except where individually marked. |
| Findings addressed | CDS-400-1..10; DICT-1, DICT-2, DICT-3, DICT-5, DICT-9; ADR-D1, ADR-D4; open decisions D28, D29 |

CDS-400 is the authoritative home for dictionaries and the value layers (CDS000-R005). Terminology is defined in CDS-100 §3; verification statuses and reason-code use live in CDS-500; facet presentation and search behaviour live in CDS-600; AI controls live in CDS-700; conformance levels, tests and claims live in CDS-1000.

---

## 1. Purpose *(normative)*

CDS-400 defines how commerce systems govern repeated values such as colours, materials, styles, rooms, finishes, patterns, occasions, conditions, units and channel vocabularies. It separates detailed product truth from the simplified values presented in customer filters, and defines how one canonical value is projected into display labels, facet values, search synonyms and channel-specific outputs without duplicating product data.

**CDS400-R001** A CDS implementation MUST treat governed values as first-class reference-data entities rather than uncontrolled text wherever consistent reuse, filtering, search, validation or channel mapping is required.

**CDS400-R002** The PIM MUST remain the authority for canonical dictionary values and their mappings.

**CDS400-R003** A customer-facing filter MUST NOT be created by exposing every distinct incoming or display value.

## 2. Problem Statement *(informative)*

Commerce data arrives with rich but inconsistent language. A supplier may describe blue products as Navy, French Navy, Ocean, Denim, Royal, Sky, Petrol or Steel Blue. Publishing those terms directly as filter values produces an unusable panel of near-duplicates. Discarding them and storing only "Blue" destroys product detail and merchandising language.

```
Source terms:        French Navy | Navy | Ocean Blue | Royal Blue | Denim | Sky Blue
Bad storefront facet: the same six near-duplicates exposed to customers
Bad canonical model:  all source detail replaced with "Blue"
CDS model:            preserve detail -> normalise meaning -> expose a usable facet -> project to channels
```

The correct response is not less information; it is a layered model that gives each consumer the appropriate representation.

## 3. Dictionary Principles *(normative)*

| Principle | Meaning |
|---|---|
| Preserve source fidelity | Keep the original value and its provenance even when it maps to a canonical value. |
| Stable identity | Values use stable identifiers independent of labels, spelling and localisation. |
| One canonical meaning | Each governed concept has one approved internal semantic representation. |
| Separate customer facets | Filter groupings are designed for usability, never copied from canonical detail. |
| Derive channel output | Channel values are generated from dictionary mappings wherever possible. |
| Govern change | Aliases, deprecations, replacements and mapping changes are versioned and reviewable. |
| Context matters | The same word can mean different things in different dictionaries or attributes. |
| Humans, machines and AI | The model is readable by operators, deterministic for software and explicit for AI. |

**CDS400-R004** A dictionary MUST have a declared semantic scope, a named owner and a declared value identity scheme.

**CDS400-R005** Labels MUST NOT be used as the only permanent identifier for governed values.

## 4. Controlled Value Lifecycle *(normative — per ADR-D4)*

CDS separates intake, internal meaning and projection. Projections branch in parallel from the canonical value (branch model, CDS-100 §7); the layer that feeds each channel is declared per attribute in the Attribute Definition (CDS-200 §7), never assumed.

```
Source Value ── Alias Mapping Record ──> Canonical Value
                    (governed)                |
        +---------------+---------------+----+----------+----------------+
        v               v               v               v                v
  Display Label    Facet Value    Search Synonyms  Channel Repr.   Tag / other
                                                   (per attribute)  projections
```

> **Supersession note.** The v0.1 term "Reference Value" is retired (ADR-D4; CDS-100 §8). The raw input is a **Source Value**; the governed mapping is an **Alias Mapping Record**; the governed dictionary entry is a **Canonical Value**; everything downstream of canonical is a **projection**.

**CDS400-R006** The original source value MUST remain available, verbatim with provenance, for audit and reprocessing.

**CDS400-R007** An Alias Mapping Record MUST resolve to exactly one canonical value within its declared context, unless the mapping is explicitly marked ambiguous and routed for review.

**CDS400-R008** Facet values, display labels, search synonyms and channel representations MUST be derived from or linked to canonical values rather than maintained as unrelated free text.

*Informative:* not every implementation exposes every layer as a visible column; the logical distinctions must still exist.

## 5. Dictionary Entity Model *(normative)*

A Dictionary is the governed container. A Canonical Value is a stable semantic entity. Aliases, facet mappings and channel mappings attach to the value, never repeated on every product. Canonical product data stores the canonical `value_id`; a variant's colour field holds the canonical value, never a raw source spelling (ADR-D4).

| Property | Purpose |
|---|---|
| dictionary_id | Stable identifier for the dictionary. |
| dictionary_key | Human-readable machine key such as `colour` or `material`; also the context-scoping key for shared codes (§20). |
| value_id | Stable identifier for one canonical value. |
| canonical_code | Portable code such as `navy` or `organic_cotton`. |
| canonical_label | Default human-readable label. |
| status | Value Lifecycle Status (§17.1). |
| version | Version of this value record; incremented on any governed change (§24). |
| aliases | Alias Mapping Records: recognised source terms, spellings and abbreviations, each with scope, status, provenance and locale. |
| display_labels | Optional labels by locale, brand or product (§9). |
| facet_mappings | Ordered facet memberships; the single authoritative facet mechanism (§10). |
| search_terms | Synonyms and related query terms (behaviour: CDS-600 §21). |
| channel_mappings | Values or identifiers required by channels, with mapping_version. |
| parent_id | Optional broader-value relationship — informative analytics only (§13). |
| related_values | Optional typed relationships (synonym, similar, substitute, compatible, contrast). |
| metadata | Swatch, unit, sort order, notes or other dictionary-specific data. |
| provenance | Who or what introduced and approved the value or mapping. |
| effective_dates | When a value or mapping becomes valid or invalid. |
| replacement_id | Successor value when deprecated. |

**CDS400-R009** Every canonical value MUST have a stable `value_id` or equivalent immutable identity.

**CDS400-R010** A canonical code SHOULD use lowercase ASCII snake_case and MUST remain stable when a display label changes.

## 6. Value Identity and Labels *(normative)*

Identity and presentation are separate. A value called Navy in English may be displayed differently by locale, brand or campaign while its identity is unchanged.

```
value_id:            colour_00017
canonical_code:      navy
canonical_label:     Navy
locale_label_en_AU:  Navy
locale_label_fr_FR:  Bleu marine
facet_mappings:      [blue]
CH_google_colour:    Blue
```

**CDS400-R011** Changing a label MUST NOT create a new value identity when the underlying meaning is unchanged.

**CDS400-R012** Merging or splitting meanings MUST be performed through an explicit governed migration (§24), never a silent label edit.

**CDS400-R013** Display labels MAY contain spaces, punctuation and brand language; canonical codes SHOULD remain portable and stable.

## 7. Source Values and Alias Mapping Records *(normative)*

A Source Value is the exact content received from a supplier, manufacturer, import, manual entry or extraction process. An Alias Mapping Record recognises that source term and links it to exactly one canonical value within a defined context.

```
Source value:      "French Navy"
Source system:     Supplier A
Source attribute:  Colour
Normalised match:  french navy
Alias mapping:     alias_colour_french_navy  (row_type: alias)
Canonical value:   navy                      (row_type: canonical)
```

**CDS400-R014** Source values MUST be retained exactly as received when traceability is required.

**CDS400-R015** An Alias Mapping Record MUST identify the dictionary (via `dictionary_key`) and context in which it is valid.

**CDS400-R016** Supplier-specific mappings SHOULD be supported where the same term has different meanings between suppliers.

*Informative:* alias mappings make supplier onboarding progressively easier — once a term is governed, future imports resolve automatically. Every distinct source value that has been mapped is retained as an alias with provenance (ADR-D4).

## 8. Canonical Values *(normative)*

A Canonical Value is the approved internal representation used for product truth, rules, analytics and derivation. It expresses meaning at the level of detail the business needs, not merely the broadest customer filter. Both granularities are conformant: an organisation may govern `french_navy` as a canonical shade with facet `blue`, or govern only `navy` and keep "French Navy" as a display label (ADR-D4).

**CDS400-R017** Canonical values MUST be semantically distinct within their dictionary.

**CDS400-R018** Canonical values SHOULD preserve commercially useful detail that would be lost in a broader facet value.

**CDS400-R019** A canonical value MUST NOT be created solely because one supplier uses a unique spelling.

**CDS400-R020** A canonical value SHOULD be reused across products and suppliers whenever the meaning is equivalent.

```
Source values                        Canonical value
French Navy, Marine, Deep Navy   ->  navy
Sky, Pale Blue, Baby Blue,
Light Blue                       ->  sky_blue
Royal, Cobalt                    ->  royal_blue
Ocean Blue                       ->  ocean_blue  (only if the business needs the distinction)
```

*Note:* the canonical code for the pale-blue shade is `sky_blue`, matching the shipped reference dictionaries and CDS-1500; the v0.1 code `light_blue` is recorded as an alias of `sky_blue` (resolves DICT-3).

## 9. Display Labels *(normative)*

A Display Label is the wording shown to a customer or operator. It may preserve a supplier or brand name, use a merchandising phrase or provide a localised label. Display labels never define canonical identity.

**CDS400-R021** A product MAY use a display label that differs from the value's canonical label.

**CDS400-R022** A display label MUST remain linked to a canonical value when the field participates in governed filtering, search or channel publication.

**CDS400-R023** A display label SHOULD NOT be used as the only search or facet value.

**CDS400-R024** Label precedence MUST be resolved in this order: (1) a product-level display label, valid only when recorded as a governed Display Label link to the canonical value; (2) the value's locale display label for the viewer's locale; (3) the value's canonical label. A product-level free-text label with no Display Label link MUST NOT override the value's labels in governed contexts.

```
Canonical colour:  navy
Product display:   French Navy   (governed Display Label link)
Facet display:     Blue
Search terms:      navy, dark blue, french navy
Google output:     Blue
```

## 10. Facet Values and Facet Mappings *(normative)*

A Facet Value is a customer-facing grouping used for filtering and refinement. Facet design is a user-experience activity, not a database distinct-value query. Facet presentation — labels, storefront order, selection logic, counts — is defined in CDS-600; CDS-400 owns the mapping from canonical values to facet values.

**CDS400-R025** The Facet Dictionary, referenced through the `facet_mappings` property of canonical values, is the single authoritative mechanism for facet membership. Facet membership MUST NOT be derived from the parent hierarchy (§13), from labels or from any other source. *(Resolves CDS-400-2.)*

**CDS400-R026** Facet values MUST be explicitly governed in a Facet Dictionary or equivalent configuration.

**CDS400-R027** A facet dictionary SHOULD minimise unnecessary near-duplicate choices while preserving distinctions that materially affect purchase intent. *(Downgraded from MUST: "minimise" is not mechanically testable; the testable mechanism is CDS400-R028.)*

**CDS400-R028** A new or materially changed facet dictionary MUST have a recorded usability review, covering the §10.1 checklist, before activation.

**CDS400-R029** `facet_mappings` is an ordered list. The first facet value is the primary membership; a canonical value MUST have exactly one primary facet value per facet dimension and MAY have additional secondary memberships where justified.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D28 (resolved)): Call made — multi-facet memberships are ordered, first entry is primary. Alternative — unordered set with an explicit `is_primary` flag. The teal exemplar is aligned to the shipped reference data (`[green, blue]`, green-dominant per CDS-1500); the v0.1 Blue-primary example is corrected accordingly.

**CDS400-R030** A multi-colour or multi-material product MAY participate in multiple facet values; the storefront MUST treat the product as one result, never a duplicate. Multicolour is a facet or status value, never a canonical shade (CDS-100 §3).

*Informative:* for colour, Blue is normally a facet; French Navy is a display label or canonical shade. For material, Wood may be a facet while Tasmanian Oak is the canonical material or display label.

### 10.1 Facet Usability Review *(normative checklist for CDS400-R028)*

The recorded review MUST cover:

- number of values and expected product counts;
- overlap and ambiguity between values;
- labels visible above and below the fold on common devices;
- whether customers search for the broad group or the detailed value;
- whether a value is better represented by search, a swatch, a range or a separate facet;
- behaviour when multiple facet values are selected;
- zero-result and low-count values; and
- localisation and sort order.

## 11. Channel Representations *(normative)*

A Channel Representation is the value, identifier or label required by a specific downstream channel. It is stored once on the dictionary value or mapping definition and derived for every applicable product. Which layer feeds each channel (canonical, display or facet) is declared per attribute in the Attribute Definition (ADR-D4; CDS-200 §7).

```
Canonical value:          navy
CH_shopify_filter_colour: Blue
CH_google_colour:         Blue
CH_meta_colour:           Blue
Product display label:    French Navy
```

**CDS400-R031** Channel representations SHOULD be defined at dictionary level rather than repeated on every product.

**CDS400-R032** A product-level channel override MAY be used only when the product genuinely requires a different output and the reason is recorded (override semantics: CDS-500 §22).

**CDS400-R033** A missing required channel mapping MUST produce a validation or publication error, never silent free-text substitution.

## 12. Search Terms *(normative)*

Search synonyms attach to canonical values as a projection and extend discovery without expanding the visible facet list. Search behaviour, directionality and query handling are defined in CDS-600 §21.

**CDS400-R034** Search synonyms MUST NOT change canonical identity, and a synonym that is ambiguous across dictionaries MUST be scoped to the applicable dictionary or attribute.

## 13. Hierarchies and Relationships *(normative; parent hierarchy informative)*

A dictionary MAY record a parent hierarchy (e.g. `navy` under `blue`, `oak` under `wood`). In v0.2 the parent hierarchy is an **optional, informative structure for analytics, reporting and operator navigation only**. It carries no authority over facets, channel output or validation; the Facet Dictionary is the only facet-mapping mechanism (CDS400-R025). *(Resolves CDS-400-2.)*

**CDS400-R035** Hierarchy and related-value relationships MUST be explicit records and MUST NOT be inferred solely from labels.

**CDS400-R036** A value MUST NOT have circular parent relationships.

**CDS400-R037** A parent relationship MUST NOT erase, replace or auto-merge the child value.

**CDS400-R038** Related-value links SHOULD state their relationship type: synonym, similar, substitute, compatible or contrast.

## 14. Multi-value and Composite Attributes *(normative)*

A product may have multiple values, and some facts are composite rather than simple lists.

```
Simple multi-value:       materials = [cotton, linen]
Structured composition:   composition = [{material: cotton, percentage: 80},
                                         {material: polyester, percentage: 20}]
Facet projection:         material facets = [cotton, synthetic]
```

**CDS400-R039** A composition MUST NOT be reduced to an unstructured material label when percentages or component roles are required.

**CDS400-R040** Multi-value order MUST be declared significant or insignificant by the Attribute Definition.

**CDS400-R041** Facet membership MAY be derived from each component while the structured composition remains canonical.

## 15. Normalisation and Matching *(normative)*

Normalisation prepares source terms for matching while preserving the original value. The default text pipeline:

1. Preserve original source text
2. Unicode NFC normalisation
3. Trim leading and trailing whitespace
4. Collapse repeated internal whitespace
5. Apply case-insensitive comparison form
6. Apply dictionary-specific punctuation and spelling rules
7. Match exact governed aliases before fuzzy or AI-assisted suggestions
8. Record the rule and mapping used

**CDS400-R042** Normalisation MUST NOT overwrite the original source value.

**CDS400-R043** Exact governed mappings MUST take precedence over fuzzy or AI-assisted matching.

**CDS400-R044** Numeric and measurement values MUST use type-aware comparison rather than text comparison.

**CDS400-R045** A dictionary MAY define locale-specific or supplier-specific normalisation rules.

## 16. Ambiguity and Context *(normative)*

The same term may mean different things in different contexts. Natural may be a colour, a finish, a fibre claim or marketing copy. Large may be a size, a capacity or a package count.

**CDS400-R046** Every mapping MUST be scoped at least by dictionary (`dictionary_key`) or attribute.

**CDS400-R047** Ambiguous aliases MUST NOT resolve globally without context.

**CDS400-R048** Where context is insufficient to resolve a source term, the term MUST enter review or remain unresolved; it MUST NOT be force-mapped.

```
"Natural" in MF_colour_display  -> colour: natural
"Natural" in MF_finish          -> finish: natural_oil / natural
"Natural" in MF_material_claim  -> no automatic mapping; review required
```

## 17. Unknown Values, Resolution and Quarantine *(normative)*

Unknown source values are expected in a living catalogue. They are data-governance events, never a reason to create uncontrolled canonical values automatically.

### 17.1 Two status enums *(normative — resolves CDS-400-4)*

v0.1 mixed two lifecycles in one vocabulary. v0.2 defines two named enums on two named entities. They share no tokens.

**Value Lifecycle Status** — attribute `value_lifecycle_status` on the **Canonical Value**:

| Status | Meaning |
|---|---|
| proposed | Candidate canonical value awaiting governance review. |
| active | Approved for use in canonical data and projections. |
| deprecated | Still resolvable; identified replacement or declared no-replacement; scheduled for retirement. |
| retired | No longer assignable; retained for history and audit. |
| rejected | Reviewed and refused; never activated. |

**Source-Term Resolution Status** — attribute `resolution_status` on the **Source Value intake record**:

| Status | Meaning |
|---|---|
| resolved | Mapped to an active canonical value via an Alias Mapping Record. |
| promotion_proposed | Term proposed as a new canonical value; a linked `proposed` Canonical Value exists. |
| quarantined | Excluded from canonical data and projections until resolved (§17.2). |
| invalid | Not a legitimate value for any target attribute (junk, corruption, wrong field). |
| ignored | Legitimate content, intentionally not used for the target attribute. |

**CDS400-R049** Implementations MUST record the two statuses as separate enums on their respective entities and MUST NOT conflate them in schemas, UIs or exports.

**CDS400-R050** Unknown source values MUST be surfaced to a review queue or explicit error process; they MUST NOT be silently dropped.

**CDS400-R051** Bulk imports MUST NOT silently create new canonical values. Promotion of a source term to a canonical value is an explicit governed act, performed only by roles authorised under §25 — this applies equally to human, scripted and AI-initiated imports.

**CDS400-R052** A promotion proposal MUST include source evidence, affected products and suggested mappings.

### 17.2 Publication consequence of quarantine *(normative — resolves CDS-400-5)*

**CDS400-R053** While a source term for an attribute is `quarantined`, that attribute value MUST be omitted from every projection (display, facet, search, channel) for the affected products. The raw source value is never published as a stand-in.

**CDS400-R054** Verification of an affected field MUST carry the reason code `CDS_VALUE_QUARANTINED` (reason-code registry: CDS-1100 §21; use in verification: CDS-500). The field is reported as attention-state, not silently skipped.

**CDS400-R055** A quarantined value MUST NOT block publication of the product as a whole unless the affected attribute is declared requiredness-blocking for that channel in its Attribute Definition or channel profile; in that case the product publication fails validation per CDS400-R033.

*Informative:* quarantined items remain in quality denominators (CDS-1400 §5) — quarantine is visible pressure to resolve, never a way to improve a health score. A dictionary dashboard should show recurring unknown values so one governance action resolves many future imports.

## 18. Units and Measurements *(normative)*

Units are governed reference data. Measurements store a numeric value and a unit identifier, never units embedded in free text.

```
Measurement:  value: 40, unit_id: centimetre
Display:      40 cm      Channel conversion: 15.75 in      Comparison base: 0.4 m
```

**CDS400-R056** Measurements MUST separate numeric value from unit identity.

**CDS400-R057** Unit conversions MUST use declared conversion rules and precision.

**CDS400-R058** An implementation MUST distinguish similarly named units with different definitions, such as short ton and metric tonne.

**CDS400-R059** Display units MAY differ by locale or channel while the canonical measurement remains stable.

## 19. Colour Dictionaries *(normative; baseline note informative)*

Colour requires multiple representations: product label, canonical shade, broad filter family, search language and channel vocabulary are not always the same.

| Layer | Example |
|---|---|
| Canonical shade | navy |
| Display label | French Navy |
| Facet mappings (ordered) | [blue] — or [green, blue] for a green-dominant teal |
| Search terms | navy blue, dark blue, marine |
| Swatch metadata | Optional representative colour; not a guarantee of physical appearance |
| Channel mapping | Blue |

**CDS400-R060** A colour dictionary SHOULD distinguish canonical shade from broad colour family.

**CDS400-R061** Hex, RGB or other digital swatch values MAY be stored but MUST NOT be treated as an exact representation of physical material colour unless measured under a defined process.

**CDS400-R062** A product with a branded colour name SHOULD retain that name for display while participating in one or more governed colour facets.

**CDS400-R063** Pattern and colour MUST remain separate attributes even when a supplier combines them in one phrase.

*Informative — baseline ownership:* the reference colour facet family list (including `natural` as a top-level facet and `multicolour` as a facet-only value) is owned by CDS-1500 Appendix C. CDS-400 appendices cite that baseline and use consistent exemplars (resolves CDS-400-3 / DICT-2).

## 20. Material and Composition Dictionaries *(normative)*

Material dictionaries support specific materials, broader families, blends and structured composition. A storefront may filter by Cotton while displaying 80% Cotton / 20% Polyester.

**CDS400-R064** Specific material identity and material family MUST be separate where both are useful.

**CDS400-R065** Composition percentages SHOULD be stored as structured values and SHOULD sum according to the organisation's declared tolerance rules.

**CDS400-R066** Claims such as organic, recycled, vegan or certified MUST NOT be inferred solely from the material name unless governed evidence supports the claim.

**CDS400-R067** There is one materials dictionary per organisation. Where the same canonical code needs different family or facet treatment in different commercial contexts (e.g. cotton in apparel vs homewares), the treatment MUST be expressed as context-scoped family and facet mappings keyed by `dictionary_key` scope (e.g. `material.apparel`, `material.homewares`) on the shared canonical value — never by forking the canonical meaning into duplicate values. *(Resolves DICT-5.)*

> RESOLVED — accepted as drafted (owner 2026-08-04; was D29 (resolved)): Call made — one materials dictionary with context scoping via `dictionary_key` scoped families; shared codes keep one meaning with per-context family/facet mappings. Alternative — two independent apparel/homewares dictionaries permitted to diverge on shared codes.

```
Canonical composition:  cotton 80, polyester 20
Facet projection:       Cotton, Synthetic
Display:                80% Cotton, 20% Polyester
```

## 21. Size and Fit Dictionaries *(normative)*

Size labels are contextual: S, M and L are not universal measurements, and numeric sizes vary by market, gender category, brand and product type.

**CDS400-R068** A size value MUST be scoped to a declared size system or scale when the label is not globally unambiguous.

**CDS400-R069** Display size, canonical size code and measurement chart MUST be separable.

**CDS400-R070** Size conversion tables SHOULD be represented as governed mappings with provenance and effective dates.

**CDS400-R071** Fit descriptors such as slim, regular, relaxed and oversized MUST be maintained separately from size.

```
Size system: apparel_womens_au   Display size: 10   Canonical code: au_10
Approximate mappings: US 6, EU 38   Product measurements: stored separately   Fit: relaxed
```

## 22. Localisation *(normative)*

Localisation changes presentation, never canonical identity.

**CDS400-R072** Canonical codes and value identifiers MUST remain language-neutral or follow a stable declared base-language policy.

**CDS400-R073** Localised labels MUST identify locale, not merely language, where regional wording differs.

**CDS400-R074** A missing translation SHOULD fall back according to a declared locale policy and SHOULD be visible as a completeness issue.

**CDS400-R075** Search synonyms MAY vary by locale and market.

## 23. Provenance and Audit *(normative)*

Every important mapping answers: who created it, why it exists, which source introduced it and which products it affects.

| Field | Purpose |
|---|---|
| created_by | User, import process or AI agent. |
| approved_by | Data steward or authorised reviewer. |
| source_system | Supplier, manufacturer, channel or internal team. |
| source_value | Exact original value. |
| evidence | Description, image, document or rule supporting the mapping. |
| created_at / changed_at | Audit timestamps. |
| version / mapping_version | Value-record and mapping versions used during a publication or verification run. |
| affected_count | Products or variants currently relying on the mapping. |

**CDS400-R076** A mapping change SHOULD record the previous value, the new value, the actor and the affected product count.

**CDS400-R077** AI-created suggestions MUST record model or process identity, confidence and evidence where available (full AI provenance requirements: CDS-700).

## 24. Versioning, Deprecation, Migration and Breaking Changes *(normative)*

Dictionary changes can alter thousands of products without editing those products directly. They therefore require versioning and impact review. Corpus-level version policy is ADR-D5; this section governs value- and mapping-level versioning.

**CDS400-R078** Every canonical value record MUST carry a `version`, and every alias, facet and channel mapping MUST carry a `mapping_version`, incremented on any governed change.

**CDS400-R079** A canonical value MUST NOT be deleted while products, aliases, rules or channel mappings reference it.

**CDS400-R080** Deprecated values MUST identify a replacement or state that no direct replacement exists.

**CDS400-R081** Mapping changes SHOULD support preview of affected products and expected downstream changes before activation.

### 24.1 Breaking changes *(normative — resolves CDS-400-7)*

**CDS400-R082** The following changes are breaking changes to value meaning:

1. **Facet remap** — moving a canonical value's primary facet membership to a different facet value;
2. **Alias retarget** — repointing an existing Alias Mapping Record to a different canonical value;
3. **Meaning narrowing** — restricting what an existing canonical value denotes so that some current usages become incorrect.

A breaking change MUST either (a) create a new value identity (new `value_id`, old value deprecated with `replacement_id`), or (b) be executed through a **governed migration record** that captures the old and new state, the actor and approver, affected product and collection counts, the activation date and the expected verification changes. A breaking change MUST NOT be applied as an in-place edit without one of these two paths.

```
Status transition:  proposed -> active -> deprecated -> retired

Deprecated value:
  canonical_code: petrol_blue
  replacement_id: teal
  migration_note: Consolidated after merchandising review
  active_until:   2026-09-30
```

## 25. Dictionary Governance *(normative)*

Governance defines who may propose, approve, change and retire values, and prevents dictionaries from becoming another uncontrolled tag list. Role definitions and change-control machinery are owned by CDS-800; this section states the dictionary-specific obligations.

| Role | Responsibility |
|---|---|
| Dictionary owner | Accountable for scope, quality and policy. |
| Data steward | Reviews new values, aliases, mappings and deprecations. |
| Merchandising owner | Approves customer facet labels, grouping and order. |
| Channel owner | Maintains external channel vocabularies and requirements. |
| Search owner | Maintains search synonyms and query behaviour. |
| AI process | May propose; never authoritative by default (CDS-700). |

**CDS400-R083** Every dictionary MUST have a named owner.

**CDS400-R084** The organisation MUST define which roles may create canonical values and which may only propose them.

**CDS400-R085** Facet changes SHOULD include merchandising or customer-experience review; channel mapping changes SHOULD include channel validation or test publication.

## 26. Publication and Verification *(normative)*

Dictionary mappings form part of the expected channel state. Verification compares the value generated by the active mapping version with the value read back from the channel. The verification model, status enum, comparison strategies and reason codes are owned by CDS-500; this section states what dictionaries contribute.

```
Canonical value: navy            Mapping version: colour_map_v12
Expected Shopify facet: Blue     Observed: blue     Strategy: case-insensitive     Result: MATCH
Expected Google colour: Blue     Observed: blank                                   Result: MISSING
```

**CDS400-R086** Publication records SHOULD identify the dictionary version and `mapping_version` used to generate channel output, so the expected value is reproducible.

**CDS400-R087** Verification MUST compare the expected representation (generated from the active mapping version) with the observed representation under the declared comparison strategy (CDS-500 §16).

**CDS400-R088** A dictionary change that alters expected output SHOULD trigger re-publication or re-verification for affected records.

## 27. AI Participation *(normative)*

AI may classify source terms, suggest aliases, recommend canonical values, propose facet memberships and detect anomalies — always inside the governed dictionary model. Autonomy levels, evidence classes, proposal storage and review flow are owned by CDS-700; the dictionary-side constraints are:

**CDS400-R089** AI MUST receive the applicable dictionary, attribute context and allowed values before proposing a mapping where practical.

**CDS400-R090** AI suggestions outside the dictionary MUST be marked as promotion proposals or unknown and routed under §17 and §25; AI MUST NOT silently create a new active canonical value (CDS400-R051 applies; autonomy ceilings: CDS-700 §5).

**CDS400-R091** AI SHOULD return confidence, evidence and alternative candidates for ambiguous values; abstention is a first-class outcome (CDS-700).

```
Input: "French Navy"    Context: apparel colour
Allowed candidates: navy, royal_blue, ocean_blue, black
AI suggestion: navy     Confidence: 0.97
Evidence: supplier colour name and product image
Decision: auto-accept only if policy threshold and evidence rules pass (CDS-700)
```

## 28. Performance and Implementation Considerations *(informative except CDS400-R092)*

CDS specifies logical behaviour, not a storage engine. Implementations should avoid recalculating the entire catalogue for every dictionary lookup:

- immutable value identifiers and indexed alias lookups;
- cached active dictionary and channel mappings with version identifiers;
- recomputation of affected products when a `mapping_version` changes;
- product-to-value and value-to-product indexes for impact analysis;
- source values and observed channel values kept separate from canonical values;
- bulk review and approval for recurring unknown values;
- dictionary health metrics: unknown rate, deprecated-use count, unmapped-channel count.

**CDS400-R092** Optimisation MUST NOT remove provenance, `mapping_version` or the ability to reproduce expected output.

## 29. Worked Examples *(informative)*

### 29.1 Apparel Colour

```
Source supplier colour: French Navy
Alias Mapping Record:   french navy -> navy
Canonical value stored on variant: value_id of navy
Display label:          French Navy
Facet mappings:         [blue]
Search terms:           navy, dark blue, french navy
Shopify filter value:   Blue        Google colour: Blue
Verification comparison: normalised text (CDS-500)
```

### 29.2 Teal with Ordered Multi-Facet Membership

```
Canonical value:  teal
Facet mappings:   [green, blue]   (ordered; green primary — green-dominant per CDS-1500 baseline)
Display label:    Deep Teal
Search terms:     teal, blue green, green blue
Policy:           product appears once even when both Green and Blue are selected
```

### 29.3 Cotton Blend

```
Source description:     80% Cotton, 20% Polyester
Canonical composition:  cotton = 80, polyester = 20
Display:                80% Cotton, 20% Polyester
Facets:                 Cotton, Synthetic
Google material:        Cotton/Polyester
Claims:                 no organic or recycled claim without governed evidence
```

### 29.4 Tasmanian Oak Homeware

```
Source material:   Tasmanian Oak
Canonical value:   oak   (family via material.homewares scope: wood)
Display label:     Tasmanian Oak
Facet:             Wood
Search terms:      timber, oak, tasmanian oak
Google material:   Wood
```

### 29.5 Unknown Supplier Colour (Moonlit Harbour)

```
Source value:     Moonlit Harbour
Dictionary match: none
AI suggestion:    navy (confidence 0.61)
Policy threshold: 0.90
Result:           resolution_status = quarantined
Publication:      colour omitted from projections; verification reason code
                  CDS_VALUE_QUARANTINED; product still publishes (colour not
                  requiredness-blocking on this channel)
Action:           human review
Outcome:          alias "Moonlit Harbour" -> navy; display label remains Moonlit Harbour
```

### 29.6 Facet Remap as a Governed Migration (breaking change)

Moving `petrol_blue` from facet Blue to facet Green is a **facet remap** — a breaking change under CDS400-R082. It cannot be applied as an in-place mapping edit; it proceeds as a governed migration record:

```
Migration record: MIG-2026-014
  Change:      petrol_blue facet_mappings [blue] -> [green]
  Actor:       merchandising owner   Approver: dictionary owner
  Impact:      127 products, 3 Shopify collections, 1 Google supplemental feed
  Activation:  2026-09-01
  Expected verification changes calculated before activation;
  re-publication and re-verification scheduled for affected records (CDS400-R088)
```

## 30. Conformance *(normative)*

Conformance levels, test suites and claim rules are owned by CDS-1000 (Foundation -> Structured -> Publisher -> Verified -> Governed; ADR-D1). CDS-400 defines **dictionary capability badges**: cumulative capability declarations inside the Structured evidence set. Each badge requires everything in the badges before it.

| Badge | Requires | Minimum capability |
|---|---|---|
| Dictionary Core | — | Stable canonical values, aliases, the two lifecycle/resolution enums, quarantine, provenance. |
| Dictionary Facet | Dictionary Core | Governed Facet Dictionary, ordered facet mappings, recorded usability review. |
| Dictionary Channel | Dictionary Facet | Channel representations, `mapping_version`s, channel validation. |
| Dictionary Round-Trip | Dictionary Channel | Expected-state publication and downstream verification of dictionary-derived output (CDS-500). |

> **Supersession note.** The v0.1 badge "Dictionary Verified" is renamed **Dictionary Round-Trip** to avoid colliding with the global Verified level, and the badges are now strictly cumulative (ADR-D1; resolves CDS-400-9).

**CDS400-R093** A dictionary capability badge MUST NOT be claimed unless all lower badges are also satisfied; badge claims are made and evidenced under CDS-1000.

The chapter's core obligations for any conformant implementation are CDS400-R001..R009 (governed values, layers, identity), R025/R028/R029 (single facet mechanism), R049..R055 (statuses and quarantine), R078..R082 (versioning and breaking changes) and R086..R088 (reproducible expected output).

## 31. Architecture Decisions *(informative)*

The v0.1 chapter-local ADR table (CDS-ADR-007..013) is superseded by the single global ADR register (CDS000-R006). The decisions binding this chapter are ADR-D1 (conformance ladder and badges), ADR-D4 (value-layer terminology and variant storage) and ADR-D5 (version and identifier policy).

---

## Appendix A — Recommended Dictionary Schema *(informative; field-presence rules normative where marked Required)*

One row set holds both canonical values and alias mappings; `row_type` disambiguates (ADR-D4; resolves DICT-1, CDS-400-6). Machine-readable schema: CDS-1100.

| Field | Type | Requirement | Purpose |
|---|---|---|---|
| dictionary_id | string / UUID | Required | Stable dictionary identity. |
| dictionary_key | string | Required | Portable semantic key and context scope (§20). |
| row_type | enum | Required | `canonical` or `alias`. |
| value_id | string / UUID | Required | Stable canonical value identity (target value for alias rows). |
| canonical_code | string | Required (canonical rows) | Lowercase snake_case portable code. |
| canonical_label | string | Required (canonical rows) | Default label. |
| alias_text | string | Required (alias rows) | The recognised source term. |
| alias_scope | object | Optional | Supplier, locale or attribute scope of the alias. |
| status | enum | Required | Value Lifecycle Status (canonical rows) or Source-Term Resolution Status (alias rows) — §17.1. |
| version | integer | Required | Value-record version (§24). |
| mapping_version | integer | Required (alias/facet/channel mappings) | Mapping version used in publication and verification. |
| locale | string | Required where localised | Locale of labels and synonyms (e.g. `en-AU`). |
| parent_value_id | reference | Optional | Broader value — informative analytics only (§13). |
| display_labels | localised list | Optional | Merchandising or locale labels. |
| facet_mappings | ordered list | Optional | Facet memberships; first entry is primary (§10). |
| search_terms | localised list | Optional | Synonyms and related queries. |
| channel_mappings | map | Optional | Channel identifiers and labels, each with mapping_version. |
| metadata | object | Optional | Swatches, sort order, unit data, notes. |
| provenance | object | Required | Creation, source and approval data (§23). |
| valid_from / valid_to | datetime | Optional | Effective period. |
| replacement_value_id | reference | Conditional | Required when deprecated if a direct replacement exists. |

## Appendix B — Apparel Colour Example *(informative)*

Facet families cite the CDS-1500 Appendix C colour baseline, which owns the reference family list; `natural` is a top-level facet there and is used as such here (resolves CDS-400-3 / DICT-2). Canonical `sky_blue` per DICT-3, with `light blue` as an alias.

| Aliases | Canonical | Display | Facet mappings (ordered) | Search | Channel |
|---|---|---|---|---|---|
| french navy | navy | French Navy | [blue] | navy; dark blue; marine | Google: Blue; Shopify facet: Blue |
| royal; cobalt | royal_blue | Royal Blue | [blue] | royal; bright blue | Google: Blue; Shopify facet: Blue |
| sky; pale blue; baby blue; light blue | sky_blue | Sky Blue | [blue] | sky; pale blue | Google: Blue; Shopify facet: Blue |
| teal | teal | Teal | [green, blue] | teal; blue green | Google: Green; Shopify facets: Green, Blue |
| natural; undyed; ecru | natural | Natural | [natural] | natural; undyed; ecru | Google: Beige; Shopify facet: Natural |

## Appendix C — Homewares Material Example *(informative)*

One materials dictionary; family and facet treatment scoped by `dictionary_key` context (§20, D29 resolved).

| Source | Canonical | Scope: material.homewares family | Display | Facet | Search | Channel |
|---|---|---|---|---|---|---|
| Tasmanian Oak | oak | wood | Tasmanian Oak | Wood | timber; oak | Google: Wood |
| American Walnut | walnut | wood | American Walnut | Wood | timber; walnut | Google: Wood |
| Stoneware | stoneware | ceramic | Stoneware | Ceramic | ceramic; pottery | Google: Ceramic |
| Rattan | rattan | natural_fibre | Rattan | Natural Fibre | cane; wicker; rattan | Google: Rattan |
| 80% Cotton / 20% Polyester | structured composition | textile | 80% Cotton, 20% Polyester | Cotton; Synthetic | cotton blend | Google: Cotton/Polyester |

## Appendix D — Legacy Alignment *(informative)*

The legacy production PIM already separated raw supplier input, resolved authoritative values, channel outputs and read-back verification. CDS-400 makes those layers explicit entities: `Import_*` fields correspond to Source Values with provenance; lookup-map normalisation corresponds to Alias Mapping Records; resolved authoritative fields correspond to Canonical Values; legacy `DF_*` feed fields correspond to Channel Representations (`CH_*` in new design, ADR-D24); read-back match fields correspond to verification results (CDS-500). Legacy lookup maps import directly as Alias Mapping Records with provenance; every distinct source value that was mapped is retained as an alias (ADR-D4).

## Appendix E — Platform Notes *(informative)*

Platform-specific mappings and constraints live in the versioned, dated profiles of CDS-900. In summary for any storefront platform: platform attribute stores and metafield-equivalents are publication targets, never the dictionary master; storefront filters use governed facet values, not distinct raw values; a product page may display a governed Display Label while the filter shows the facet value; tags are not the primary store for controlled attributes when typed fields exist; read-back is normalised and compared with expected values generated from the active `mapping_version`; manual downstream edits to PIM-owned values are reported as drift unless an approved override exists (CDS-500 §22).

END OF CDS-400 v0.2 REVIEW DRAFT
