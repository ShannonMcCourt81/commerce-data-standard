# CDS v0.2 Adoption Workbook

Use this single document as the organisation profile required by the Shopify Setup Runbook. Keep links to evidence rather than pasting logs or secrets into it. A blank field means not decided or not evidenced.

| Field | Value |
|---|---|
| Organisation | |
| Store / environment | |
| Workbook owner | |
| CDS release | v0.2 Review Draft |
| Shopify profile | CDS-SHOPIFY-0.2 |
| Industry profiles | `cds.profile.apparel.v0_2`, `cds.profile.homewares.v0_2` |
| Workbook version | |
| Last updated | |
| Status | Draft / Pilot / Accepted / Superseded |

## 1. Scope and Owners

| Function | Named owner | Backup | Evidence / notes |
|---|---|---|---|
| PIM product owner | | | |
| Taxonomy owner | | | |
| Dictionary owner | | | |
| Shopify channel owner | | | |
| Integration owner | | | |
| Verification owner | | | |
| Security / access owner | | | |
| Conformance reviewer | | | |

**Catalogue scope:**  
**Channels in scope:**  
**Fields outside PIM authority:**  
**Small-team profile declared:** Yes / No  
**Claimed conformance level:** None during pilot / Foundation / Structured / Publisher / Verified / Governed  
**Claimed overlays:** None / CX / AI-Assured / Multi-Tenant  

## 2. Owner Decisions

| Runbook stop | Decision | Owner | Date | Rationale / evidence |
|---|---|---|---|---|
| 0.4 Small-team profile | | | | |
| 1.3 Category tie-break order | | | | |
| 2.2 Colour facet family set | | | | |
| 3.3 Tag suffix format | | | | |
| 4.4 Metafield edit-protection posture | | | | |
| 9.4 Wave go/no-go authority and thresholds | | | | |

## 3. Taxonomy Decision Log

Never overwrite a decision. Add a superseding row and link the earlier row.

| Decision ID | Product type / product | Primary category chosen | Rule applied | Date | Supersedes | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

**Declared tie-break order:**  
**Accessories rule:**  
**Taxonomy source / version:**  

## 4. Dictionary and Facet Adoption

| Item | Adopted version / hash | Owner | Divergence from CDS seed | Evidence |
|---|---|---|---|---|
| CDS Reference Dictionary | | | | |
| Colour family set | | | | |
| Apparel materials | | | | |
| Homewares materials | | | | |
| Size systems | | | | |
| Other governed dictionaries | | | | |

**Unknown-value quarantine owner and review cadence:**  
**Canonical-value approval process:**  
**Deprecation and replacement process:**  

## 5. Tag and Collection Contract

| Namespace / partition | Authority | Generation | Owner | Lifecycle / notes |
|---|---|---|---|---|
| `collection_*` | PARTITIONED_PIM | Computed | | |
| `merch_*` | PARTITIONED_PIM | Governed manual / rule | | |
| `season_*` | PARTITIONED_PIM | Controlled rule | | |
| External app tags | External | External | | Must survive PIM writes |

**Tag suffix format:**  
**Full-replace merge test evidence:**  

## 6. Channel Capability Declaration

Record observed limits and the date checked. Do not copy platform claims forward without rechecking them.

| Capability / limit | Declared value | Verified date | Evidence / result |
|---|---|---|---|
| Shopify product options | Maximum 3 | | |
| Shopify variants per product | Maximum 2,048; connector/theme may support less | | |
| Search & Discovery filters per store | Maximum 25 | | |
| Storefront values per filter | Maximum 100 | | |
| Values shown per filter in app | Maximum 1,000 | | |
| Unique values per filter group | Maximum 200 | | |
| Filter groups store-wide | Maximum 1,000 | | |
| Collection size with filtering | Maximum 5,000 products | | |
| Search result size with filtering | Maximum 100,000 results | | |
| Category filter value grouping | Unsupported | | |
| Variant-scope combination filtering | Present; verify with pilot | | |
| Per-value counts under combined selections | Unknown until Empirical Check 1 | | |
| Combined Listings | Plus / enterprise only; child products excluded from S&D filter results | | |
| Propagation window | | | |
| Critical field set | | | |
| Metafield edit-protection posture | | | |
| Drift actor evidence available | | | |

## 7. Phase Evidence

| Phase | Exit evidence | Owner | Date | Result |
|---|---|---|---|---|
| 0 Prerequisites | PIM readiness, owners and declarations | | | Not run |
| 1 Taxonomy | Tree, mappings and decision log | | | Not run |
| 2 Dictionaries | Adopted dictionaries and Attribute Definitions | | | Not run |
| 3 Tags | Registry and merge semantics | | | Not run |
| 4 Store bootstrap | Permissions, app and metafield definitions | | | Not run |
| 5 Collections | Automated and merchandising collections | | | Not run |
| 6 Filters | Facet definitions, limits and accessibility | | | Not run |
| 7 Navigation | Mobile, breadcrumb and SEO checks | | | Not run |
| 8 Channel wiring | Mappings, expected state and GMC projection | | | Not run |
| 9 Pilot and waves | Pilot evidence and wave decision | | | Not run |
| 10 Verification | Observation, comparison and proving period | | | Not run |

## 8. Vertical-Slice Evidence

### Empirical Check 1: Combined Filter Counts

| Test | Expected | Observed | Result | Evidence |
|---|---|---|---|---|
| Blue + M trap product | Excluded when no purchasable Blue/M variant exists | | Not run | |
| Unselected size counts | Predict result after adding each size | | Not run | |
| Availability + Material | Counts and results follow declared semantics | | Not run | |

**Capability declaration after test:**  
**Defect / follow-up:**  

### Empirical Check 2: Drift Attribution

| Test | Expected | Observed | Result | Evidence |
|---|---|---|---|---|
| Staff edits PIM-owned metafield | EXTERNAL_EDIT detected | | Not run | |
| Staff edits product title | EXTERNAL_EDIT detected | | Not run | |
| Observation history | Previous value, new value and detection interval retained | | Not run | |
| Actor correlation | Identified / class identified / unattributable recorded honestly | | Not run | |
| Repair and re-verification | Governed repair creates new evidence | | Not run | |

## 9. Human Review

Each reviewer completes one real task without coaching, records where they stopped, and proposes the smallest correction.

| Reviewer perspective | Required task | Reviewer | Date | Result / evidence |
|---|---|---|---|---|
| Merchant / operator | Classify and publish one ambiguous product using the runbook | | | Not run |
| PIM / integration engineer | Produce expected, observed and verification documents for one product | | | Not run |
| Data governance reviewer | Trace one requirement through decision, implementation and evidence | | | Not run |
| Accessibility reviewer | Complete the Phase 6.5 filter checks on mobile and desktop | | | Not run |

**Blocking findings:**  
**Accepted changes:**  
**Deferred changes and owner:**  

## 10. Acceptance

No conformance claim is made while a mandatory test is failed, not tested or inconclusive.

| Decision | Name | Date | Evidence / conditions |
|---|---|---|---|
| Pilot go/no-go | | | |
| Production go/no-go | | | |
| Run-state acceptance | | | |
| Conformance statement approval | | | |

