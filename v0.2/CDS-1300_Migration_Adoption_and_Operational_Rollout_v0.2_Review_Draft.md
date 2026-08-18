# Commerce Data Standard (CDS)
## CDS-1300 — Migration, Adoption and Operational Rollout

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-1300 Working Draft v0.1 |
| Normative status | §1–§2, §4–§23 are normative except where marked otherwise. §3, §24, Appendices A–C and all worked scenarios are informative. |
| Findings addressed | SYS-3 (D18), 1300-1..14; ADR-D1 (maturity mapping), ADR-D2, ADR-D4, ADR-D24; Matrix 5 (legacy annex, DF_→CH_ consolidation) |

A governed pathway for moving existing commerce data, teams and channels into a CDS-conformant operating model without losing authority, traceability or business continuity.

---

## 1. Purpose and Scope *(normative)*

CDS-1300 defines how an organisation adopts CDS while continuing to operate existing products, channels and business processes. It covers migration from spreadsheets, hosted-table PIMs, legacy enterprise PIMs, channel-first catalogues and mixed estates into a PIM-first CDS architecture.

The chapter governs both technical migration and operating-model transition. A structurally correct database is not a successful migration if staff continue editing authoritative fields in downstream channels, dictionaries remain uncontrolled, verification is absent, or operational ownership is unclear.

**CDS1300-R001** A migration MUST include an operational transition plan, not only a data-load procedure.

**CDS1300-R002** Business continuity, rollback and verification MUST be designed and approved before production cutover.

Completeness of the migration itself is governed by the inventory-disposition rule (CDS1300-R009): nothing leaves the migration without a recorded disposition. *(This replaces the v0.1 "preserve or explicitly retire every authoritative fact" rule, which was untestable as stated.)*

> Informative note: CDS does not require a big-bang replacement. Incremental adoption is preferred where it reduces risk and maintains traceability.

## 2. Operating Scale and the Small-Team Profile *(normative)*

CDS-1300 names many functions. They are **hats, not headcount**. A sole trader and a hundred-person programme can both conform; what scales is evidence and separation of duties, not the org chart.

**CDS1300-R003** Every function named in this chapter MUST have a named owner. One person MAY hold any number of functions simultaneously. A conformance assessment MUST NOT require distinct individuals per function.

**CDS1300-R004** Where staffing permits, the person who builds a migration artifact (mapping, transformation, load package) SHOULD NOT be the sole acceptor of that artifact. Where one person must do both, the acceptance record MUST note the dual role and the compensating control applied (for example: checklist-driven self-review against frozen criteria, evidence archived for later independent review). Segregation-of-duties expectations and compensating controls are defined in CDS-800 (decision-rights and segregation table); this chapter applies them, it does not redefine them.

**CDS1300-R005** An organisation MAY adopt the **small-team profile** by declaring it in its conformance claim (claim rules: CDS-1000). Under that profile the requirements listed in Table 2-1 apply at the downgraded level shown; **all other requirements apply unchanged**.

**Table 2-1 — Small-team profile downgrades**

| Requirement | Base level | Small-team profile level |
|---|---|---|
| CDS1300-R053 (separate read, write and approval migration credentials) | MUST | SHOULD; a single operator MAY hold combined credentials provided every bulk write is attributable, audit-logged, and the log is reviewed at wave exit |
| CDS1300-R057 (operational readiness demonstrated without project-team intervention) | MUST | The intervention-free clause is waived where the operators and the project team are the same people; the readiness demonstration MUST still be performed and recorded |

Requirements that reference "named owners" or "operational owners" are satisfied under either profile by the hats rule (R003); acceptance and evidence records are never waived, only the requirement for the people involved to be different individuals.

> RESOLVED (was D18 (resolved), owner decision 2026-08-04): accepted — self-declared eligibility, no headcount threshold.

## 3. Adoption Principles *(informative)*

- **Authority before movement** — determine who owns each field before copying values.
- **Profile before transformation** — understand the source data before designing target mappings.
- **Preserve provenance** — retain where a value came from and how it was transformed.
- **Canonical before channel** — resolve canonical values before publishing channel projections.
- **Dictionaries before bulk normalisation** — do not mass-convert values until controlled vocabularies and ambiguity rules exist.
- **Verification before trust** — do not declare migration complete until downstream state is observed and compared.
- **Small reversible releases** — prefer bounded migrations that can be measured and rolled back.
- **Human comprehension** — field names, status displays and review queues must remain understandable to operators.
- **No silent loss** — unsupported fields are quarantined, mapped or explicitly retired, never silently dropped.
- **Evidence over confidence** — completion claims require reproducible evidence.

## 4. Migration Pathways and Starting States *(normative)*

Organisations begin from different levels of structure. CDS defines migration pathways rather than assuming one starting point.

| Starting state | Primary migration emphasis |
|---|---|
| Channel-first store | A commerce platform currently holds the most complete product data. Extract and profile the channel state first, then establish PIM authority. |
| Spreadsheet or hosted-table PIM | A structured but implementation-specific master exists. Preserve formulas, mappings and validation behaviour while replacing brittle field coupling. |
| Legacy enterprise PIM | A mature PIM lacks CDS dictionaries, channel verification or human-readable namespaces. Adoption may be layered rather than replacing the platform. |
| ERP-led catalogue | The ERP owns identity and commercial data; descriptive enrichment is scattered. CDS introduces a canonical enrichment layer without displacing legitimate ERP authority. |
| Multi-channel fragmented estate | Channels contain competing product versions. Migration requires explicit reconciliation and an authority decision per field. |
| Greenfield | No production catalogue exists. Sequence taxonomy, schemas, dictionaries, channel profiles and test fixtures before product entry. |

**CDS1300-R006** The migration plan MUST identify the declared starting state and MUST NOT assume that a system is authoritative merely because it currently contains the most data.

## 5. Readiness Assessment *(normative)*

Before migration begins, the organisation assesses readiness. **Minimum evidence for every area below: documented findings, a named owner and a risk rating.**

| Area | Assessment scope |
|---|---|
| Data | Record counts, duplicate rate, missing identifiers, uncontrolled values, rich-text quality, media completeness, historical anomalies. |
| Architecture | Current product/variant model, taxonomies, field definitions, formulas, scripts, APIs, manual workarounds, hidden dependencies. |
| Channels | Published fields, channel overrides, collection logic, feed requirements, read-back capability, rate limits. |
| People | Data owners, editors, approvers, knowledge concentration, training needs, resistance risks. |
| Governance | Existing naming standards, change control, incident handling, deprecation rules, audit evidence. |
| Operations | Release windows, peak trading periods, support coverage, rollback capacity, acceptable freeze periods. |
| Security | Credentials, least privilege, tenant separation, personal data, supplier confidentiality. |

**CDS1300-R007** Production migration MUST NOT begin until every critical readiness risk has an owner, a treatment and an acceptance decision.

## 6. Source-System and Data Inventory *(normative)*

The source inventory records every system, file, integration and manual process that creates, alters, enriches, publishes or verifies product information.

```
Source Inventory Record
- source_id            - identifiers
- system_name          - record_count
- owner                - known_quality_issues
- data_domains         - retention_requirement
- extraction_method    - migration_disposition
- update_frequency     - evidence_location
```

**CDS1300-R008** Every source that can change product information MUST appear in the source inventory, including manual spreadsheets and channel-admin edit practices.

**CDS1300-R009** Every inventoried source, field, mapping and rule MUST carry a `migration_disposition` — one of `migrate`, `transform`, `merge`, `quarantine`, `retire`, `out_of_scope` — with an evidence location. Nothing exits the migration without a recorded disposition.

**CDS1300-R010** The inventory MUST distinguish authoritative source data, reference data, derived data, channel projections and observed downstream data.

**CDS1300-R011** Unknown fields MUST be classified (and receive a disposition) before they are transformed or discarded.

## 7. Authority and Ownership Baseline *(normative)*

Migration is the opportunity to remove competing masters. An authority matrix records the current owner, target owner, transition date and permitted read-back behaviour for each domain or field. (Authority is declared per fact — CDS-200 §13.)

| Domain | Common current owner | Target authority | Migration rule |
|---|---|---|---|
| Product identity | ERP or legacy PIM | PIM or ERP by declared contract | Identifiers remain stable. |
| Descriptive attributes | Files, supplier feeds, channel admin | PIM | Channel edits become drift unless approved overrides exist (CDS-500 §22). |
| Taxonomy | Channel collections, tags, legacy categories | PIM | External taxonomies remain mappings. |
| Price | ERP, PIM or channel | Declared commercial authority | Do not move authority without finance approval. |
| Inventory | Warehouse, ERP or channel | Inventory authority | PIM may consume but not master live stock. |
| Channel observed state | Channel APIs | Observation store | Never merged into canonical values (CDS-500 §15). |
| Verification result | Legacy formulas or none | Verification engine | Reason codes beneath traffic lights (CDS-500 §17–18). |

**CDS1300-R012** Every migrated field MUST have exactly one declared target authority.

**CDS1300-R013** Read-back and verification fields MUST remain separate from authoritative values throughout migration.

**CDS1300-R014** Each authority cutover MUST be evidenced by at least one of: **(a)** a permission or access change that prevents non-authoritative writes to the field; **(b)** drift detection armed on the field (observation plus comparison per CDS-500); or **(c)** a documented acceptance that enforcement is detection-only, naming the residual risk owner.

> Informative note: some platform standard fields cannot be write-protected at all — any admin user can edit them regardless of PIM authority. For such fields option (a) is unavailable by construction; enforcement is necessarily detection-only (b or c), and the training rule CDS1300-R051 is the compensating human control.

## 8. Target-State Design *(normative)*

The target state is designed before bulk transformation: entity boundaries (CDS-200), semantic namespaces (CDS-300), Attribute Definitions, dictionaries (CDS-400), internal taxonomy, channel profiles (CDS-900), publication and observation records (CDS-500), and operating procedures.

```
Canonical PIM                          External Authorities
+-- Products and Variants              +-- ERP / Pricing
+-- Attribute Definitions              +-- Inventory / Warehouse
+-- Dictionaries and Facets            +-- Orders / Customers
+-- Internal Taxonomy
+-- Media and Content
+-- Channel Profiles
+-- Publication Records
+-- Observations
+-- Verification Results
+-- Governance and Audit
```

**CDS1300-R015** The target model MUST be validated with representative products before full mapping begins.

**CDS1300-R016** Target fields MUST NOT be created solely to preserve accidental source-system implementation details; legitimate source provenance and business meaning MUST be preserved even when field names and storage mechanisms change.

## 9. Taxonomy and Classification Migration *(normative)*

Taxonomy migration separates what a product **is** from where it is **merchandised**. Steps (informative): extract all category-like values (tags, product types, collection rules, supplier categories); identify synonyms and overlaps; design a non-overlapping internal tree; assign one primary category per product; map external taxonomies at category level where inheritance is valid; define collection and navigation projections separately; keep a taxonomy decision log for ambiguous types; validate counts, orphans and duplication.

**CDS1300-R017** A channel's collections, tags or product types MUST NOT be assumed to be canonical categories.

**CDS1300-R018** After migration each product MUST have one primary internal category; collections MAY remain many-to-many merchandising projections (rules: CDS-200 §6).

**CDS1300-R019** External taxonomy mappings MUST retain the source taxonomy version and the mapping rationale.

## 10. Attribute and Dictionary Migration *(normative)*

Legacy fields mix source values, canonical values, display labels, facet values and channel output. Migration separates these into the value layers defined by ADR-D4 (definitions: CDS-100 §3; model: CDS-400).

```
Legacy field:  Colour = "French Navy"

Migrated representation (value layers per ADR-D4):
Source value          = "French Navy"      (preserved verbatim, with provenance)
Alias mapping record  = "French Navy" -> colour_french_navy
Canonical value       = colour_french_navy (stored on the variant)
Display label         = "French Navy"
Facet value           = blue
CH_google_colour      = "Blue"             (channel representation)
```

**CDS1300-R020** Distinct source values MUST be profiled before dictionary normalisation begins.

**CDS1300-R021** Ambiguous mappings MUST enter review; they MUST NOT be resolved by first-match or other arbitrary logic.

**CDS1300-R022** Every source value mapped during migration MUST be retained as an alias (an Alias Mapping Record, CDS-400) with provenance. *(v0.1's "where useful" qualifier is deleted: aliases are what future imports and read-back comparison match against — discarding them breaks verification later.)*

**CDS1300-R023** Facet values MUST be designed for customer usability (CDS-600), not inferred solely from current distinct-value counts.

## 11. Product and Variant Migration *(normative)*

Product and variant migration resolves parent–child relationships, SKU identity, shared attributes and sellable differences (variant boundary rule: CDS-200 §5).

| Control | Migration requirement |
|---|---|
| Identity continuity | Preserve SKU, GTIN, MPN, source IDs and channel IDs where continuity is required. |
| Parent grouping | Confirm variants genuinely represent sellable forms of one logical product. |
| Option definition | Only values that create distinct sellable units become options. |
| Shared data lifting | Move identical values from variants to the parent product. |
| Variant truth | Do not create unavailable combinations by Cartesian expansion. |
| Duplicate detection | Detect same SKU, same GTIN, same MPN/brand and near-identical records. |
| Lifecycle state | Preserve active, draft, archived, discontinued and pre-order meaning. |

**CDS1300-R024** A migration MUST NOT create new SKU identities merely to fit a target platform unless a governed re-identification plan exists.

**CDS1300-R025** Every variant consolidation or split MUST be evidenced by an approved old-to-new cross-reference table. The cross-reference table is the **primary** control; mechanical reversibility of a restructure is rarely available on production channels and MUST NOT be assumed or claimed without test evidence.

**CDS1300-R026** The wave design MUST check migrated products against the declared structural limits of each target channel profile (variants per product, option count, value lengths — CDS-900) **at design time**, before mapping is finalised, not at load time.

## 12. Content, Media and Digital Assets *(normative)*

Checklist (informative): preserve original source content separately from enriched content where provenance matters; normalise rich text without silently removing meaningful structure; retain asset identifiers, source URLs, checksums, rights and usage restrictions; define primary image, sequence, variant association and alt-text rules; quarantine broken, duplicate, low-resolution or unsupported assets; verify downstream media ordering and variant-image association after publication.

**CDS1300-R027** Asset migration MUST preserve available rights and provenance metadata.

**CDS1300-R028** Asset transfer success MUST NOT be treated as proof that the channel displays the correct asset in the correct order; media ordering and variant association are in verification scope (CDS-500).

## 13. Channel Mapping and Publication Migration *(normative)*

Channel migration converts legacy output fields and direct-admin practices into governed channel profiles and publication records. The canonical model is not redesigned to mirror channels.

```
Canonical attribute -> channel mapping -> expected representation
                    -> publication -> observation -> verification
```

**CDS1300-R029** Each migrated channel field MUST identify its canonical source, transformation, destination and comparison strategy.

**CDS1300-R030** Channel overrides MUST be explicit, attributable and bounded (override records: CDS-500 §22).

**CDS1300-R031** New channel fields MUST use the `CH_` namespace (ADR-D24; registry: CDS-300). Legacy `DF_` names MAY persist during transition only as registered deprecated aliases with provenance. Per ADR-D24 §3, a field is a feed-layer projection **iff it is a literal serialized feed column**; such projections live under `CH_` and the feed artifact is verified end to end at the formatted-output layer.

**CDS1300-R032** Generated tags, collections and feed outputs MUST be reproducible from governed source data or rules; they MUST NOT be imported as independent canonical truth.

*(v0.1's "retain DF_ only where useful" and "metafield-equivalent" qualifiers are resolved by ADR-D24 and ADR-D2 respectively; the MF_/STD_ boundary is the CDS-300 enumeration, never a judgement call.)*

## 14. SEO and URL Continuity *(normative — new in v0.2)*

After data loss, the largest business risk in a commerce migration is losing accumulated search equity. URL and search continuity is migration scope, not an afterthought.

**CDS1300-R033** A migration that changes customer-facing URLs, handles, slugs or channel identifiers MUST, for every existing customer-facing URL, either preserve the URL or serve a permanent redirect to its successor.

**CDS1300-R034** SEO-critical fields — page titles, meta descriptions, canonical URLs, and any structured-data fields declared in the channel profile — MUST be included in the pre-cutover baseline (§15) and in post-cutover verification scope.

**CDS1300-R035** Redirect coverage SHOULD be verified after cutover by sampling pre-cutover URLs, and index-status and organic-traffic signals SHOULD be monitored through the wave's proving period.

> Informative note: redirect behaviour is a channel-profile capability check. Some platforms create redirects automatically when a handle changes; others require explicit redirect records; some feed-based channels key on identifiers where "redirect" means identifier continuity. Record the mechanism per channel in the CDS-900 profile before cutover.

## 15. Verification Baseline and Downstream Read-Back *(normative)*

Before changing production data, capture what downstream channels currently contain. This separates pre-existing drift from migration-induced drift — the strongest available defence against blaming the migration for old defects, or missing new ones.

```
Baseline: extract current channel state -> store observed values
          -> compare against current expected state -> record pre-existing mismatches
          -> freeze baseline evidence -> begin migration
```

**CDS1300-R036** A downstream baseline MUST be captured and frozen before production cutover wherever read-back is technically available, and the frozen baseline MUST be retained at least until the wave passes its exit gates (it is also the rollback republication source — R042).

**CDS1300-R037** Pre-existing mismatches MUST be recorded and distinguished from mismatches introduced by migration.

**CDS1300-R038** Fields that cannot be observed MUST be recorded with the `UNOBSERVABLE` status from the CDS-500 enum; they MUST NOT be reported as verified. Verification statuses, reason codes and traffic-light presentation are owned by CDS-500 §17–§18 and are not restated here.

## 16. Cutover Strategies *(normative)*

| Strategy | Use and risk |
|---|---|
| Big bang | Everything switches together. Highest coordination risk; only for small, well-tested, easily reversible estates. |
| Wave by category | Bounded category groups; useful for dictionary and taxonomy validation. |
| Wave by brand or supplier | Supports source-specific mappings and operational ownership. |
| Wave by channel | Establish PIM authority, then migrate one downstream channel at a time. |
| Shadow publication | Generate expected output without writing production; compare against current channel state. |
| Dual run | Old and new pipelines run simultaneously with controlled reconciliation — see R040. |
| Pilot cohort | A small representative product set migrated end to end before scale-out. |

**CDS1300-R039** The chosen strategy MUST define scope, entry criteria, exit criteria, rollback point and evidence package.

**CDS1300-R040** At any moment, exactly **one** pipeline MUST be the declared writer for a given channel field-set. On a channel with a single write target, a "dual run" therefore MUST operate as shadow publication on the non-authoritative side: the non-authoritative pipeline generates expected output and compares, and MUST NOT write. Reconciliation happens on evidence, never by both pipelines writing.

**CDS1300-R041** Each wave plan MUST declare its proving period (the post-cutover observation window that must elapse defect-free before exit) before cutover.

> Informative note: typical proving periods run one to four weeks and should cover at least one full business cycle for the affected products (including any weekly ordering, feed or campaign rhythm).

## 17. Rollback, Recovery and Business Continuity *(normative)*

Rollback is a designed capability, not an emergency improvisation.

**CDS1300-R042** Every production migration wave MUST have a tested rollback or compensating recovery procedure. **Channel-side rollback is defined as republication of the frozen pre-cutover baseline (R036)** through the governed publication path, followed by observation and verification — not as restoration of channel-internal state, which most channels cannot provide.

**CDS1300-R043** Rollback MUST NOT overwrite the evidence required to determine what changed and why (publication records, observations, verification results, decision log).

Rollback design checklist (informative): freeze pre-cutover source and channel state; version transformation rules, mappings, dictionaries and payloads; maintain old-to-new identifier cross-references; define stop conditions and escalation authority; test restoration of data, credentials and scheduled jobs; reconcile publication attempts made before failure; preserve evidence from failed runs.

> Informative — irreversibility classes. Republication restores content state but cannot reverse everything. Classes to enumerate per wave: (1) customer interactions bound to channel identifiers (orders, reviews, wishlists) — never reversible; (2) search-engine indexing and ranking signals accumulated against changed URLs (mitigated by §14, not reversed); (3) feeds, emails and ads already consumed downstream; (4) channel-side identifiers destroyed by deletion (recreated objects get new identities); (5) analytics history continuity; (6) third-party caches and syndication copies. A rollback plan states, per class, whether the exposure exists and what compensating action applies.
>
> Informative — commerce activity during rollback: orders, payments and fulfilment are mastered outside CDS scope (CDS-000 §2) and proceed on their own systems. The migration team's obligation is product-data remediation: identify products sold while incorrect data was live, correct the data forward, and hand any customer-impact assessment to the responsible business owner.

## 18. Operational Rollout and Run-State Transition *(normative)*

Migration ends only when the new operating model is stable and owned.

| Run-state area | Required operational definition |
|---|---|
| Publishing | Schedules, queue monitoring, retries, rate limits, incident ownership. |
| Verification | Read-back cadence, mismatch triage, health thresholds, escalation. |
| Dictionaries | New-value review, alias creation, facet governance, deprecation. |
| Taxonomy | Category-change procedure, mapping review, decision log. |
| Imports | Supplier onboarding, schema-change detection, quarantine, delta-sync monitoring. |
| AI | Proposal review, thresholds, benchmarks, model-change handling (CDS-700). |
| Support | Operator runbooks, dashboards, alert routing, service expectations (CDS-1400). |
| Release management | Versioning, change windows, approvals, rollback ownership. |

**CDS1300-R044** Project completion MUST include recorded acceptance by the named run-state owners (who MAY be the same people as the project team — §2).

**CDS1300-R045** Temporary migration scripts and credentials MUST be retired, governed, or incorporated into supported operations.

## 19. Data Quality Remediation *(normative)*

Migration surfaces defects that may have existed for years. CDS separates blocking defects, remediable defects and accepted historical imperfections.

| Class | Treatment |
|---|---|
| Blocking | Missing product identity, duplicate SKU, invalid variant relationship, unsafe price, critical compliance data. |
| High priority | Unmapped category, dictionary ambiguity, missing required channel field, broken media. |
| Improvement | Weak descriptions, missing optional attributes, poor search synonyms, non-critical legacy formatting. |
| Accepted debt | Known issue with documented reason, owner, review date and impact assessment. |

**CDS1300-R046** Quality thresholds MUST be defined before acceptance testing begins.

**CDS1300-R047** Quality and completeness denominators MUST include failed and quarantined records. A record MAY leave a denominator only through a disclosed `migration_disposition` (R009). Reporting completeness over a silently reduced population is non-conformant. *(This is the corpus's strongest anti-gaming control; see also CDS-1400 §6.)*

## 20. AI-Assisted Migration *(normative)*

AI may accelerate classification, attribute extraction, dictionary suggestions, duplicate review, content cleanup and anomaly detection. It remains a **proposal mechanism** governed entirely by CDS-700 (proposals separate from canonical state, evidence classes, confidence, abstention, autonomy levels, review). This section adds only the migration-specific rules.

**CDS1300-R048** AI-generated migration values MUST carry the provenance CDS-700 requires (model/workflow version, evidence, confidence where available) and MUST pass the same schema and dictionary validation as any other input.

**CDS1300-R049** AI MUST NOT silently resolve identifier conflicts, legal claims, safety attributes or other high-risk discrepancies; these MUST enter human review.

**CDS1300-R050** Human review samples SHOULD include both accepted and rejected proposals, to detect systematic error in either direction.

## 21. People, Functions, Training and Change Management *(normative)*

A CDS rollout changes responsibilities and habits. Teams must understand not only new screens but why canonical authority, dictionaries and verification exist.

The migration **functions** (hats — one person MAY hold several, per R003):

| Function | Primary accountability |
|---|---|
| Executive sponsor | Scope, risk and organisational priority. |
| Programme lead | Migration plan, dependencies, acceptance. |
| Data architect | Target model, mappings, technical integrity. |
| Data steward | Dictionaries, taxonomy quality, exceptions. |
| Channel owner | Platform mappings and operational behaviour. |
| Migration engineer | Extraction, transformation, load and evidence automation. |
| Verifier / QA | Expected-versus-observed validation and test evidence. |
| Business editor | Usability, product meaning, workflow fit. |
| Operations owner | Runbooks, monitoring, incidents, support obligations. |

**CDS1300-R051** Training MUST cover authority, namespaces, dictionaries, publication states, verification and exception handling — and specifically **which channel-admin edits will be overwritten or treated as drift**.

## 22. Security, Privacy and Tenant Isolation *(normative)*

Migration often requires broad temporary access and bulk extraction; controls stay proportionate and time-bounded.

**CDS1300-R052** Migration tooling MUST preserve tenant and organisation boundaries (no cross-organisation mixing of dictionary, publication or observation records).

**CDS1300-R053** Migration credentials MUST follow least privilege, and read, write and approval credentials MUST be separated. *(Small-team profile: downgraded per Table 2-1 — combined credentials permitted with full attributable audit logging reviewed at wave exit.)*

**CDS1300-R054** Temporary extracts MUST have a retention and destruction decision; temporary credentials MUST be rotated or revoked after each phase.

Checklist (informative): encrypt exports; restrict supplier-pricing and confidential data; exclude unnecessary customer or order data from product migration datasets; record who executed bulk writes and which package revision was used; validate archive retention against policy.

## 23. Metrics, Acceptance Criteria and Exit Gates *(normative)*

Acceptance criteria are defined at product, wave, channel and programme levels.

| Metric | Acceptance evidence |
|---|---|
| Record reconciliation | Source, transformed, loaded, quarantined and retired counts reconcile (dispositions per R009). |
| Identifier integrity | No unapproved duplicate or changed SKU/GTIN/MPN identities. |
| Schema validity | Required records pass structural and semantic validation. |
| Dictionary coverage | Distinct values mapped, quarantined or explicitly excluded — with aliases retained (R022). |
| Taxonomy coverage | Valid primary categories and expected external mappings. |
| Publication success | Expected payloads accepted without unhandled failure. |
| Observation coverage | Expected fields read back or explicitly `UNOBSERVABLE` (CDS-500). |
| Verification health | Mismatch and missing rates below approved thresholds. |
| SEO continuity | URL/redirect coverage verified per §14. |
| Operational stability | Queues, schedules, retries and alerts operate through the declared proving period (R041). |
| User acceptance | Readiness demonstration per R057. |

**CDS1300-R055** Acceptance thresholds MUST be approved before the migration wave executes.

**CDS1300-R056** A wave MUST NOT exit merely because all jobs completed; quality, verification, SEO-continuity and operational gates also apply.

**CDS1300-R057** Operational readiness MUST be demonstrated by named operators completing representative workflows without project-team intervention, and the demonstration recorded. *(Small-team profile: intervention-free clause waived per Table 2-1.)*

## 24. Conformance *(normative)*

Conformance levels, test suites and claim rules are owned by CDS-1000. A CDS-1300 conformance claim is a claim against the requirement set CDS1300-R001–R057 (with Table 2-1 substitutions where the small-team profile is declared), evidenced per CDS-1000. Recommended practices — pilot cohorts, automated evidence generation, versioned mapping packages, a migration issue/decision register, use of the CDS-1200 fixtures for deterministic validation, and a post-cutover retrospective with debt handover — are SHOULD-level and MAY be cited as supporting evidence in a claim.

## 25. Worked Migration Scenarios *(informative)*

### 25.1 Legacy hosted-table PIM (Airtable) to CDS

```
Legacy layers                             CDS role
Import_*                 -> source ingestion records
Airtable_*               -> canonical core values
MF_Airtable_*            -> canonical structured attributes
DF_Airtable_SEO_*        -> channel/feed projections (Data Feed layer — ADR-D24)
Shopify_* / MF_Shopify_* -> downstream observations
Match_* / MF_Match_*     -> verification results
```

Migration outcome: preserve formula intent as explicit transformations; replace implicit behaviour with Attribute Definitions and rules; retain read-back and traffic-light concepts (CDS-500); map general downstream fields into `CH_*`; register `DF_*` as deprecated aliases (feed-column projections continue under `CH_` per R031).

**CDS1300-R058** Legacy formulas MUST be catalogued and tested before they are replaced by code or rules — hidden business rules must not be lost even where implementation details change.

> Informative note: Airtable formula *logic* is not extractable through the data API — the API returns computed results, not formula text. Catalogue formulas from the schema/UI, exported documentation, or maintained records, and budget for this as a manual step.

### 25.2 Channel-First Clothing Store

Current state: platform products are master; `collection_*` tags drive navigation; colours contain 80+ distinct values; some attributes live in description text.

Migration:
1. extract products, variants, tags, collections and structured fields
2. profile current colour values
3. build canonical colour and facet dictionaries
4. establish internal taxonomy
5. create PIM records and expected channel state
6. shadow compare before write (R040)
7. pilot one category
8. publish, read back and verify
9. expand by category wave

### 25.3 Multi-Supplier Homewares Catalogue

```
Current state                      Target
Supplier A: "Tasmanian Oak"        Source values preserved; aliases retained (R022)
Supplier B: "Oak Timber"           Canonical material = oak or wood, per evidence
Supplier C: "Natural Wood"         Facet material = wood
                                   Display label remains source-appropriate
                                   Channel values follow each channel profile
```

Ambiguous "Natural Wood" **enters review** rather than being auto-mapped to oak (R021): the term may mean oak, pine, or an unspecified species; first-match mapping would fabricate a material claim.

## 26. Architecture Decisions *(informative)*

Per CDS000-R006, ADRs live in the single global register. Decisions originating in this chapter, now recorded there: staged reversible adoption preferred; operational handover is part of migration; pre-cutover downstream baseline required; legacy formula intent preserved before replacement; quality denominators include quarantined records; AI assists but does not silently arbitrate conflicts. The v0.1 record CDS-ADR-1300-005 (DF_→CH_) is **superseded by ADR-D24**.

## Appendix A — Migration Phase Checklist *(informative)*

Each phase exits on evidence accepted by a named accountable owner (one person MAY own several or all phases — §2; builder/acceptor separation per R004).

| Phase | Exit evidence |
|---|---|
| A. Mobilise | Scope, sponsor, programme lead, risk register, release constraints, communication plan approved. |
| B. Discover | Sources, fields, formulas, integrations, channels, users and hidden processes inventoried. |
| C. Profile | Counts, duplicates, nulls, distinct values, taxonomies, variants and media quality measured. |
| D. Design | Target model, ownership, namespaces, dictionaries, taxonomy, mappings and rules approved. |
| E. Build | Extraction, transformation, load, publication, observation and verification workflows implemented. |
| F. Test | Schema, semantic, negative, round-trip, performance, security and rollback tests passed. |
| G. Pilot | Representative cohort migrated and operated through a proving period. |
| H. Cut over | Approved wave executed with monitoring, reconciliation and rollback readiness. |
| I. Stabilise | Mismatches triaged, operational metrics stable, documentation and training completed. |
| J. Close | Operational acceptance, debt register, retrospective, evidence archive, temporary-access retirement completed. |

## Appendix B — Legacy Airtable PIM Mapping *(informative — organisation example)*

This table records one organisation's legacy naming as a worked example. It is not normative reference data; the normative prefix registry is CDS-300.

| Legacy pattern | CDS role | Migration treatment |
|---|---|---|
| `Import_*` | Source ingestion | Retain as source records; never canonical. |
| `Airtable_*` | Resolved core data | Map to canonical product/variant fields. |
| `MF_Airtable_*` | Resolved structured data | Map to governed attributes and values; MF_ per the ADR-D2 enumeration boundary. |
| `DF_Airtable_SEO_*` | Data Feed output (ADR-D24) | Map to `CH_google_*` or feed-column projections under `CH_`. |
| `Shopify_*` | Observed standard fields | Map to observation records (CDS-500 §15). |
| `MF_Shopify_*` | Observed metafields | Map to observation fields. |
| `Match_*` / `MF_Match_*` | Comparison formulas | Map to verification results with reason codes and comparison strategies (CDS-500). |
| `collection_*` tags | Computed collection signals | Regenerate from taxonomy/collection rules; never import as independent canonical truth. |
| Traffic lights | Operator QA display | Retain as presentation over detailed statuses (CDS-500 §18). |

## Appendix C — Adoption Maturity Mapping *(informative)*

The single conformance ladder is owned by CDS-1000 (ADR-D1): Foundation → Structured → Publisher → Verified → Governed. The v0.1 maturity levels of this chapter map as follows and are retained only as adoption-narrative labels:

| v0.1 maturity level | CDS-1000 ladder |
|---|---|
| Level 0 — Fragmented | pre-Foundation |
| Level 1 — Canonical | Foundation |
| Level 2 — Structured | Structured |
| Level 3 — Publisher | Publisher |
| Level 4 — Verified | Verified |
| Level 5 — Governed | Governed |

END OF CDS-1300 v0.2 REVIEW DRAFT
