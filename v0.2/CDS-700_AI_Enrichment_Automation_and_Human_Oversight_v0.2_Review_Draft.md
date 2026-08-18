# Commerce Data Standard (CDS)
## CDS-700 — AI Enrichment, Automation and Human Oversight

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 |
| Date | 2026-08-04 |
| Supersedes | CDS-700 Working Draft v0.1; CDS-800 v0.1 §29 (AI governance rules consolidated here per the single-home rule) |
| Normative status | §1, §3, §5–§33 are normative. §2, §4, §34 and Appendices A–D are informative. |
| Findings addressed | SYS-1 (errata manifest §C: all 105 prefix-labelled rules corrected), SYS-2/700-2 (requirement IDs), 700-3, 700-4, 700-5, 700-6, 700-7, 700-8, 700-9; Matrix 2 (D14, open), Matrix 5 (AI single-home); provides the autonomy-scaled monitoring hook for 1400-11 |

CDS-700 is the single authoritative home for AI and probabilistic-automation requirements in CDS (CDS000-R005). Other chapters cite this chapter and do not restate its rules. This chapter in turn cites: statuses and verification — CDS-500; namespace registry — CDS-300; dictionaries and value layers — CDS-400; facets and customer experience — CDS-600; governance roles and change control — CDS-800; platform profiles — CDS-900; conformance levels and the T-AI test suite — CDS-1000; the machine-readable AI-proposal contract — CDS-1100.

---

## 1. Purpose and Scope *(normative)*

CDS-700 defines how artificial intelligence and other probabilistic automation may participate in a PIM-first commerce data environment: extraction, classification, normalisation, dictionary mapping, content generation, translation, media analysis, channel assistance, human review, evaluation and operational governance. It does not select a model vendor, prompting framework or orchestration technology; it defines the information contracts and assurance boundaries that hold regardless of which model, agent or platform performs the work.

**CDS700-R001** AI MUST operate as a producer of proposals, evidence or bounded actions; it MUST NOT become the implicit source of truth for product information.

**CDS700-R002** AI-generated information MUST conform to the same schemas, dictionaries, validation rules and publication controls as information entered by a human or imported from a supplier.

**CDS700-R003** The PIM MUST remain the master product-information layer when AI is used (CDS-200; CDS-P-02).

**CDS700-R004** An implementation MUST make AI participation visible and auditable: authorised operators MUST be able to enumerate the active AI workflows (via the registry of §33) and inspect the work objects (§6) behind any AI-originated value.

## 2. AI Principles *(informative)*

- **Canonical authority remains human-governed.** AI may propose or transform; acceptance into canonical state follows declared policy.
- **Evidence before assertion.** Product facts are supported by eligible evidence (§7).
- **Schema before prose.** AI fills governed fields and controlled values before producing unconstrained text.
- **Abstention is valid.** Returning unknown or requesting review is a first-class outcome, safer than a confident invention.
- **Risk determines autonomy.** Low-risk, reversible tasks may be automated more aggressively than pricing, compliance, safety or product claims.
- **Deterministic rules stay deterministic.** Validation, arithmetic, unit conversion and exact mappings are not delegated to probabilistic reasoning when reliable rules exist.
- **Humans remain legible participants.** AI workflows and field names are understandable without specialist prompt-engineering knowledge (CDS-P-04).
- **Evaluation precedes scale.** A workflow is tested on representative products before it touches a whole catalogue.
- **Publication remains assured.** AI does not bypass CDS-500 expected-state, observation and verification controls.
- **Provenance survives acceptance.** Accepted values retain their source, evidence and AI-generation history without polluting the canonical field name.

## 3. AI Participation Architecture *(normative)*

```
Eligible Source Evidence
        |
        v
Schema + Dictionaries + Rules + Task Policy
        |
        v
AI Proposal / Transformation / Classification
        |
        v
Validation + Confidence + Evidence Check
        |
        +--> Reject / Abstain / Quarantine
        |
        v
Human or Policy Approval
        |
        v
Canonical Acceptance or Draft Content
        |
        v
CDS-500 Publication and Verification
```

**CDS700-R005** Every AI workflow MUST identify its inputs, expected output schema, validation rules, approval policy and permitted destination state.

**CDS700-R006** An AI workflow MUST NOT write directly into a canonical field unless its autonomy level and the field's risk class explicitly permit that action.

*Informative note:* the AI system is one participant in the information lifecycle. The schema, dictionaries, rule engine and verification engine remain separate authorities.

## 4. Roles of AI in Commerce Information *(informative, except R007)*

| Role | Typical tasks | Default risk posture |
|---|---|---|
| Extractor | Identify material, colour, dimensions, features or model identifiers from eligible sources | Low to medium |
| Classifier | Suggest product family, type, category or taxonomy mapping | Medium |
| Normalizer | Map source wording to canonical dictionary values | Low to medium |
| Writer | Draft titles, descriptions, bullets, care text or summaries | Medium |
| Translator | Translate and localise governed content | Medium |
| Media analyst | Describe images, detect visible attributes, propose alt text or sequence | Medium |
| Channel assistant | Suggest channel categories, labels, titles or policy fixes | Medium to high |
| Quality analyst | Detect anomalies, missing values, conflicts and likely drift | Low to medium |
| Merchandising assistant | Suggest collections, facets, synonyms, related products or campaign groupings | Medium |
| Workflow coordinator | Route work, request evidence and invoke approved tools | Depends on permissions |

**CDS700-R007** *(normative)* An implementation MUST declare the role an AI workflow performs rather than describing all AI activity as a single generic enrichment step.

## 5. Autonomy Levels *(normative)*

| Level | Name | Permitted behaviour |
|---|---|---|
| A0 | Disabled | No AI processing for the task or field. |
| A1 | Assistive | AI proposes values or content; a human must accept each result. |
| A2 | Governed draft | AI may populate a non-canonical draft or review queue after validation. |
| A3 | Bounded acceptance | AI may accept eligible values into canonical state only under the bounded-A3 controls of R011. |
| A4 | Bounded execution | AI may trigger approved downstream actions for specified low-risk fields or workflows, subject to publication and verification controls (§30) and the enumeration rule R012. |

**CDS700-R008** An organisation MUST declare the autonomy level for each AI workflow.

**CDS700-R009** A4 MUST NOT be interpreted as unrestricted autonomy.

**CDS700-R010** High-risk fields — price, tax, regulated claims, hazardous-use instructions, legal warranties and safety information — MUST NOT use A3 or A4 without an explicit specialist-approved policy.

**CDS700-R011** **Bounded A3** is A3 operated under all four of the following controls. A workflow claiming A3 MUST implement all four; R2-risk tasks (Appendix B) MAY use A3 only in this bounded form:
1. a **per-field policy** declaring which fields and value classes are eligible for automatic acceptance;
2. a **calibrated confidence threshold** derived from representative reviewed examples for that task and field (§17);
3. **mandatory sampled human review** of accepted results at a declared sampling rate;
4. **automatic suspension** of automatic acceptance when the reviewer correction rate breaches a declared threshold.

**CDS700-R012** An A4 workflow MUST enumerate its permitted actions in its workflow definition; any action not enumerated is prohibited for that workflow.

*Informative note:* a single catalogue may use A3 for mapping supplier colour names while requiring A1 for compliance claims and A2 for marketing descriptions.

## 6. AI Work Objects and Review States *(normative)*

AI work is represented as durable objects, not transient chat responses. A work object records the task, source evidence, schema, output, validation, review and final disposition. The machine-readable contract for this record is the CDS-1100 ai-proposal schema; Appendix A lists the recommended semantic fields.

| Property | Purpose |
|---|---|
| work_id | Stable identifier for the AI task |
| product_id / variant_id | Target information record |
| task_type | Extraction, mapping, classification, writing, translation or analysis |
| workflow_version | Approved workflow or agent definition |
| model_id | Model and version used |
| input_evidence | References to eligible source material |
| output_schema | Expected structured result |
| proposal | Generated values or content |
| confidence | Field- or task-level confidence |
| validation_results | Dictionary, schema and business-rule outcomes |
| review_state | See R015 |
| reviewer | Human or policy that authorised acceptance |
| timestamps | Created, completed, reviewed and accepted times |
| cost_and_usage | Optional operational usage data |

**CDS700-R013** AI proposals MUST be stored separately from canonical values until accepted by the declared approval policy.

**CDS700-R014** Rejecting or superseding a proposal MUST NOT erase its audit record.

**CDS700-R015** The review state of an AI proposal MUST use the shared enum: `proposed`, `review_required`, `accepted`, `rejected`, `superseded`, `expired`. This enum is identical in CDS-700 and the CDS-1100 ai-proposal schema — they describe the same record. Execution failure (timeout, malformed output, tool error) is a work-object disposition (§28), not a review state.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D14 (resolved)): Adopted the merged enum proposed/review_required/accepted/rejected/superseded/expired ("accepted" replaces v0.1 "approved"; "expired" adopted from CDS-1100; "review_required" retained from CDS-700; v0.1 "failed" moved to work-object disposition). Alternative: keep two vocabularies with a mapping table — rejected because Matrix 2 shows they describe one record.

## 7. Source Evidence and Input Eligibility *(normative)*

AI quality is constrained by the information it receives. CDS distinguishes eligible evidence from contextual material that may inspire wording but cannot establish a product fact.

| Class | Eligibility criteria | Examples | Permitted use |
|---|---|---|---|
| E1 — Authoritative | Publisher is the manufacturer, the contracted supplier or the organisation itself, with an identifiable authority chain to the product (specification, signed record, approved internal measurement) | Manufacturer specification, signed supplier record, approved internal measurement | May establish canonical facts subject to validation |
| E2 — Strong secondary | Publisher identity is known and the content originates from a brand-controlled or certified source: an **official product page** (a page whose origin is controlled by the brand owner or authorised distributor), packaging produced by the brand, or a **certified feed** (a data feed whose certifier is named in the evidence record) | Official product page, packaging image, certified data feed | May support facts with provenance and review policy |
| E3 — Observational | Direct observation of the product or its current presentation; publisher authority not required, but the observation itself is verifiable | Product photographs, video, existing storefront copy | May support visible or descriptive attributes; ambiguity must remain explicit |
| E4 — Contextual | No qualifying publisher identity or authority chain | Competitor listings, general web content, related-product text | May inform terminology or review; must not establish unverified product facts |

**CDS700-R016** An evidence record MUST identify the publisher and the basis for its class assignment; evidence that cannot meet the E1–E3 criteria MUST be classed E4. For E2 "certified feed" evidence the certifier MUST be named.

**CDS700-R017** Every factual AI proposal MUST identify the evidence used or explicitly declare that no eligible evidence was available.

**CDS700-R018** AI MUST NOT convert absence of evidence into a positive product claim.

**CDS700-R019** Conflicting eligible sources MUST be surfaced as a conflict rather than silently resolved by model preference.

## 8. Schema-Constrained Generation *(normative)*

AI outputs are constrained by Attribute Definitions, controlled dictionaries, units, cardinality and conditional rules (CDS-200 §7, CDS-400). Free-form generation is reserved for content fields that are intentionally unstructured.

```
Task: Extract apparel attributes
Allowed output:
  MF_material: dictionary(materials), multi-value
  MF_pattern: dictionary(patterns), single-value
  MF_fit: dictionary(fits), single-value
  MF_sleeve_length: dictionary(sleeve_lengths), single-value
  AI_evidence: source references
  AI_confidence: 0.00-1.00
Not allowed:
  new dictionary values
  price claims
  sustainability claims without evidence
```

**CDS700-R020** An AI workflow MUST receive an explicit output schema.

**CDS700-R021** Out-of-schema fields MUST be rejected or quarantined.

**CDS700-R022** When an output requires a dictionary value, the AI MUST select from the allowed identifiers or return an unknown-value proposal (CDS-400 §17).

## 9. Extraction and Normalisation *(normative)*

Extraction identifies candidate facts from source material. Normalisation converts those candidates into canonical units, identifiers and dictionary values. The two stages remain distinguishable for audit and correction.

```
Observed source text: "80% cotton / 20% recycled poly"
Extracted components:
  cotton = 80 percent
  recycled polyester = 20 percent
Canonical composition:
  material.cotton = 80
  material.recycled_polyester = 20
Facet projection:
  Cotton
  Recycled material
```

**CDS700-R023** The original extracted text MUST be preserved when the normalised result may be disputed or reprocessed.

**CDS700-R024** Unit conversion and arithmetic SHOULD be performed by deterministic code after AI extraction, not by unchecked model calculation.

**CDS700-R025** A normalisation step MUST identify whether the result was exact, alias-based, transformed or inferred.

## 10. Classification and Taxonomy Assistance *(normative)*

AI may suggest internal categories, product types and external taxonomy mappings. Classification remains governed because it controls inherited attributes, collections, navigation and channel requirements (CDS-200 §6).

**CDS700-R026** AI classification MUST select from the current approved taxonomy identifiers.

**CDS700-R027** The classifier SHOULD return ranked candidates, confidence and the evidence that distinguished the selected category from nearby alternatives.

**CDS700-R028** A category suggestion MUST NOT automatically create a new category.

**CDS700-R029** External taxonomy suggestions MUST remain channel mappings and MUST NOT replace the internal classification.

*Informative note:* low-confidence classification routes to the taxonomy decision log rather than creating silent inconsistency.

## 11. Dictionary Mapping and Unknown Values *(normative)*

AI's role in mapping supplier values (colour names, materials, fits) to controlled dictionaries is to propose a mapping, not to hide ambiguity. Dictionary governance, aliases and unknown-value quarantine are defined in CDS-400.

| Outcome | Required behaviour |
|---|---|
| Exact canonical or alias match | Use deterministic mapping; AI is unnecessary |
| High-confidence contextual match | AI may propose an existing canonical value with evidence |
| Ambiguous match | Return ranked candidates and require review |
| No suitable value | Create an unknown-value record or dictionary-extension request |
| Potential synonym | Propose an alias; do not add it silently |

**CDS700-R030** AI MUST NOT create a canonical dictionary value merely to avoid returning unknown.

**CDS700-R031** A proposed alias MUST retain the source wording, language, supplier and approval status.

## 12. Product Content Generation *(normative)*

AI may draft titles, descriptions, feature bullets, care summaries and other commerce content. Generated content remains grounded in canonical facts and eligible evidence.

**CDS700-R032** Generated content MUST NOT introduce product capabilities, compatibility, certifications, scarcity, sustainability or performance claims that are absent from approved information.

**CDS700-R033** The workflow SHOULD distinguish factual fields, marketing interpretation and stylistic wording.

**CDS700-R034** A generated title MUST preserve the identifiers and distinguishing attributes required by the organisation's declared product-title policy (R035).

**CDS700-R035** An organisation using AI title generation MUST declare a **product-title policy**: a per-catalogue or per-category-profile statement of which identifiers (e.g. brand, model number) and which distinguishing attributes (e.g. colour, size, capacity) a title must preserve, and any ordering or length constraints. The policy is the testable reference for R034.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): The product-title policy had no home chapter in v0.1 (referenced only here), so it is defined here as a declared-policy mechanism. Alternative: relocate to CDS-600 (customer experience) or CDS-200 (canonical model) if a later revision gives titles a fuller treatment.

**CDS700-R036** Generated content SHOULD cite or internally link the canonical fields used, so reviewers can trace each factual statement.

*Informative note:* a strong writing workflow generates from governed facts. It does not treat an old product description as unquestionable truth.

## 13. Translation and Localisation *(normative)*

Translation changes language. Localisation adapts terminology, units, spelling, regulatory wording and market conventions. These are modelled separately.

**CDS700-R037** The canonical source language and approved translation MUST remain linked by version.

**CDS700-R038** Dictionary values SHOULD use locale-specific display labels (CDS-400) rather than being translated independently in every product record.

**CDS700-R039** AI translation MUST preserve product identifiers, measurements, brand names and regulated wording according to field policy.

**CDS700-R040** A translation workflow MUST report omitted, ambiguous or culturally adapted content.

## 14. Image, Video and Document Analysis *(normative)*

AI may analyse product photographs, packaging, diagrams, manuals and video to propose attributes, alt text, media roles or quality findings.

**CDS700-R041** Visual analysis MUST distinguish visible observation from inferred product fact.

**CDS700-R042** AI-generated alt text SHOULD describe relevant visible content concisely and MUST NOT repeat unsupported marketing claims.

**CDS700-R043** Image-derived colour SHOULD be treated as observational (E3) evidence: lighting, editing, display profiles and material reflectance can all shift apparent colour.

**CDS700-R044** Sensitive or private information found in media MUST be handled under the organisation's security policy and MUST NOT be copied into product content by default.

## 15. Channel Optimisation and Mapping Assistance *(normative)*

Channel optimisation is a projection task; it must not alter canonical facts to satisfy one platform (CDS-P-03).

**CDS700-R045** AI channel optimisation MUST operate on expected channel state (CDS-500), not rewrite canonical information to match a channel limitation.

**CDS700-R046** Channel-specific generated text MUST be stored as a CH_ override or draft when it differs from canonical content (CDS-300).

**CDS700-R047** Policy-sensitive marketplace attributes MUST be validated against current channel rules before publication.

**CDS700-R048** An AI suggestion MUST NOT be treated as evidence that a channel will accept or display the value.

## 16. Search, Facet and Merchandising Assistance *(normative)*

AI may assist with synonyms, query interpretation, related-product suggestions, collection candidates and facet-gap analysis. These outputs influence customer discovery and therefore require measurement and governance; facet and search governance is defined in CDS-600.

**CDS700-R049** AI MAY propose search synonyms; dictionary and search owners MUST approve terms that materially broaden or redirect meaning.

**CDS700-R050** AI MUST NOT expose every generated concept as a customer facet.

**CDS700-R051** Merchandising suggestions MUST remain distinguishable from taxonomy classification.

**CDS700-R052** Personalised or generated collection membership SHOULD be explainable by declared signals and MUST respect availability and exclusion rules.

## 17. Confidence, Uncertainty and Abstention *(normative)*

Confidence is a decision aid, not proof. Model scores may be uncalibrated, task-specific or incomparable across versions. Confidence is interpreted together with evidence and validation:

| Signal | Meaning |
|---|---|
| Model confidence | The system's estimate for its own proposal |
| Evidence strength | Authority and directness of source material (§7) |
| Dictionary certainty | Exact, alias, contextual, ambiguous or unknown mapping |
| Validation outcome | Whether schema and business rules pass |
| Risk class | Consequence if the result is wrong (Appendix B) |
| Review requirement | Human, policy or no approval required |

**CDS700-R053** A confidence score MUST NOT be used as the sole acceptance criterion.

**CDS700-R054** The workflow MUST support an explicit abstain or insufficient-evidence outcome.

**CDS700-R055** Thresholds SHOULD be calibrated on representative reviewed examples for the specific task and field; for bounded A3 this calibration is mandatory (R011).

## 18. Evidence, Provenance and Explainability *(normative)*

Explainability in CDS is practical lineage, not a demand that a model reveal internal reasoning.

**CDS700-R056** An AI proposal MUST record the source references, model, workflow version, timestamp and validation results.

**CDS700-R057** Where feasible, extracted facts SHOULD include a source snippet, document region, image region or field reference.

**CDS700-R058** The implementation MUST NOT require or expose private model chain-of-thought as an audit mechanism.

**CDS700-R059** A human-readable decision summary SHOULD explain the evidence, mapping and policy outcome without revealing sensitive internal reasoning.

## 19. Human Review and Approval *(normative)*

Human review is a governed task, not a decorative approve button. Reviewers need the proposal, current value, evidence, validation results, impact and available actions in one place.

| Review action | Meaning |
|---|---|
| Accept | Write the proposal to the permitted target state |
| Edit and accept | Correct the proposal while preserving original AI output |
| Reject | Do not apply; record reason |
| Request evidence | Return to the workflow for additional eligible sources |
| Create dictionary request | Escalate an unknown or missing controlled value |
| Defer | Keep pending without acceptance |
| Bulk accept | Apply only when preview, scope and rollback are available |

**CDS700-R060** A reviewer MUST be able to see which fields will change before acceptance.

**CDS700-R061** Bulk approval MUST provide a summary of affected products, values, risks and validation exceptions.

**CDS700-R062** Human corrections SHOULD be captured as evaluation data, subject to privacy and governance policy.

## 20. Deterministic and Probabilistic Boundaries *(normative)*

A robust system combines AI with deterministic software. AI handles ambiguity and interpretation; deterministic components handle exact rules and repeatable transformations.

| Prefer deterministic logic | Prefer AI assistance |
|---|---|
| Arithmetic and tax calculation | Extracting a price from unstructured text |
| Unit conversion after unit identification | Identifying a unit in a diagram |
| Exact dictionary aliases | Suggesting a mapping for a new supplier term |
| Required-field validation | Inferring which attributes are described in prose |
| Identifier format validation | Classifying a product from mixed evidence |
| Known channel transformation | Drafting a channel-specific summary |

**CDS700-R063** An implementation SHOULD use deterministic logic whenever the same inputs should always produce one objectively correct result.

**CDS700-R064** For each task the workflow registry (§33) marks as deterministic-eligible, the registry entry MUST either name the deterministic implementation used or record why no reliable deterministic rule exists. *(This replaces the untestable v0.1 rule "AI MUST NOT be used to obscure a missing deterministic rule" with an auditable mechanism.)*

## 21. Validation and Guardrails *(normative)*

Guardrail layers: schema validation (types, cardinality, required fields, structure); dictionary validation (approved identifiers, aliases, unknown-value handling); business validation (conditional requirements, incompatibilities, range limits); evidence validation (eligible sources, conflicts); content validation (prohibited claims, duplicate wording, field length); channel validation (allowed values, required fields, destination limits); publication validation (authority, workflow state, expected-state generation).

**CDS700-R065** Guardrails MUST be evaluated after AI output and before canonical acceptance or publication.

**CDS700-R066** A failed guardrail MUST produce a specific reason code rather than a generic AI error.

**CDS700-R067** A model instruction alone MUST NOT be treated as a sufficient guardrail for critical rules that can be enforced deterministically.

## 22. AI Semantic Namespace *(normative)*

`AI_` is a registered core semantic namespace in the CDS-300 v0.2 namespace registry, reserved for AI work metadata and proposals. The prefix identifies the role of a field without changing the semantic identity of an accepted canonical value. Naming patterns are listed in Appendix C; the registry itself is owned by CDS-300.

**CDS700-R068** AI_ fields MUST represent proposals, provenance, confidence or workflow metadata; they MUST NOT replace the canonical field namespace.

**CDS700-R069** After acceptance, the value MUST be stored in its semantic canonical field (e.g. MF_material) while AI provenance remains linked in the audit record.

*Informative note:* MF_material means material. AI_material_suggestion means an AI proposal about material. The prefix communicates role immediately to humans, software and AI agents.

## 23. Prompt, Model and Configuration Versioning *(normative)*

AI behaviour can change when the model, system instruction, prompt template, tool set, retrieval source, dictionary or validation policy changes. Reproducibility depends on a versioned workflow, not the model name alone.

**CDS700-R070** Every production AI result MUST identify the model and workflow version used.

**CDS700-R071** Prompt templates, tool permissions, retrieval sources, output schemas and thresholds SHOULD be versioned together as one deployable configuration.

**CDS700-R072** A workflow change that may alter accepted outputs MUST pass evaluation (§24) before production rollout.

**CDS700-R073** Historical proposals MUST remain associated with the configuration that generated them.

## 24. Evaluation and Benchmark Sets *(normative)*

Evaluation uses representative, reviewed commerce examples, including ordinary products and difficult boundary cases.

| Metric | Example application |
|---|---|
| Precision | How often accepted material mappings are correct |
| Recall | How often available attributes are successfully found |
| Exact-match rate | Category or dictionary identifier selection |
| Schema-valid rate | Structured output validity |
| Unsupported-claim rate | Generated content grounding |
| Abstention quality | Whether uncertain cases are correctly deferred |
| Reviewer correction rate | Human effort required after generation |
| Downstream verification rate | Whether accepted AI output publishes faithfully |

**CDS700-R074** An AI workflow MUST be evaluated before bulk production use.

**CDS700-R075** The benchmark set SHOULD include diverse suppliers, categories, languages, missing data, conflicting evidence and unknown dictionary values.

**CDS700-R076** Evaluation results MUST be associated with the exact workflow version.

## 25. Drift, Regression and Change Detection *(normative)*

Model providers, prompts, dictionaries and product distributions change. A workflow that performed well previously may degrade without an obvious software error.

**CDS700-R077** Production workflows SHOULD be re-evaluated after material model, prompt, schema, dictionary or source changes.

**CDS700-R078** The implementation SHOULD monitor changes in acceptance rate, correction rate, unknown-value rate, content violations and downstream mismatch rate.

**CDS700-R079** A significant regression MUST be able to pause or roll back the affected workflow.

**CDS700-R080** Previously accepted canonical values MUST NOT be silently regenerated merely because a model version changed.

**CDS700-R081** Monitoring obligations MUST scale with the declared autonomy level of a workflow: segmented monitoring that distinguishes AI-originated from human-originated values MUST apply to A3 and A4 workflows, SHOULD apply to A2 workflows, and MAY be limited to volume and sampled quality checks for A1. Operational monitoring mechanics are defined in CDS-1400, which cites this rule for its AI segmentation requirement.

## 26. Security, Privacy and Data Handling *(normative)*

AI workflows may process supplier records, internal prices, unpublished products, contracts, customer material or credentials. The organisation controls what data leaves its boundary and which tools an agent may invoke.

**CDS700-R082** Each AI workflow definition MUST declare the data classes it may receive as input; supplying data outside the declared classes is non-conformant. Declared inputs SHOULD be the minimum necessary for the task.

**CDS700-R083** Secrets and credentials MUST NOT be included in model input. This prohibition admits no policy exception.

**CDS700-R084** Private customer data MUST NOT be included in model input unless a declared data-handling policy explicitly permits it and states the safeguards applied (such as minimisation, masking or pseudonymisation, retention limits and access controls).

**CDS700-R085** Tool permissions MUST be scoped to the workflow; read access MUST NOT imply write or publication access.

**CDS700-R086** Logs and evidence records MUST follow retention and access-control policy.

## 27. Rights, Claims and Restricted Content *(normative)*

Commerce content may include copyrighted supplier text, trademarks, certifications, environmental claims and regulated statements. AI does not remove the need to establish rights and factual authority.

**CDS700-R087** An AI workflow MUST NOT infer regulated or rights-bearing claims — such as certifications, origin claims, sustainability claims, medical claims or legal warranties — from style, context or similar products. *Informative note:* which claim categories are regulated, and how, is jurisdiction-dependent; the categories named here are examples, and organisations MUST rely on their declared claim policies for the binding list in each market.

**CDS700-R088** Generated content MUST NOT reproduce supplier or third-party content beyond the rights the organisation holds to use it.

**CDS700-R089** Generated content SHOULD avoid close stylistic imitation of identifiable third-party content even where reproduction rights are not directly at issue.

**CDS700-R090** Brand and trademark wording MUST follow approved source and brand policy.

**CDS700-R091** Restricted or regulated categories SHOULD use specialist review profiles and narrower autonomy levels.

## 28. Failure Modes and Recovery *(normative)*

| Failure | Required response |
|---|---|
| Malformed output | Reject and retry only under bounded policy |
| Unsupported dictionary value | Quarantine or dictionary review (CDS-400 §17) |
| Conflicting evidence | Human review; preserve both sources |
| Tool or retrieval failure | Mark incomplete; do not fabricate missing input |
| Model timeout or refusal | Record status and preserve work object |
| Hallucinated claim | Reject, record reason and include in evaluation set |
| Bulk anomaly | Pause batch and provide rollback or staged recovery |
| Publication mismatch | Use CDS-500 reconciliation; do not assume AI output was accepted |

**CDS700-R092** Retries MUST be bounded and MUST NOT conceal repeated failure.

**CDS700-R093** A fallback model or workflow MUST meet the same schema, evidence and evaluation requirements as the primary.

## 29. Agent and Workflow Orchestration *(normative)*

Agentic systems may coordinate extraction, validation, research, review routing and publication tools. An agent is not exempt from field authority, permissions or evidence rules.

```
Orchestrator
  |-- Evidence Reader (read only)
  |-- Attribute Extractor (proposal only)
  |-- Dictionary Mapper (proposal only)
  |-- Validator (deterministic)
  |-- Human Review Queue
  `-- Publisher (explicitly authorised, CDS-500 controlled)
```

**CDS700-R094** Each agent or tool MUST have a declared role and least-privilege permission set.

**CDS700-R095** The orchestrator MUST preserve task lineage across delegated steps.

**CDS700-R096** An agent MUST NOT grant itself broader authority based on its own confidence or task interpretation.

**CDS700-R097** A human-readable workflow name and state SHOULD be visible to operators.

## 30. Publication Boundaries *(normative)*

AI acceptance and channel publication are separate events. A value may be approved as canonical yet still fail channel mapping, preflight validation or downstream publication.

**CDS700-R098** AI workflows MUST NOT bypass CDS-500 expected channel state and publication preflight.

**CDS700-R099** AI-generated channel overrides MUST be visibly channel-specific and independently reviewable.

**CDS700-R100** Direct AI publication MAY be used only under A4 for an explicitly approved, low-risk workflow with rollback and downstream verification.

**CDS700-R101** Price, inventory, legal status and safety-critical changes SHOULD remain outside direct AI publication unless governed by a specialist standard and deterministic controls.

## 31. Verification and Reconciliation *(normative)*

AI output is verified at two boundaries: against the canonical schema and evidence at acceptance, and against the observed downstream state after publication (CDS-500).

```
AI proposal
  -> Canonical validation and approval
  -> Expected channel representation
  -> Publication
  -> Channel observation
  -> Semantic comparison
  -> Health and reconciliation
```

**CDS700-R102** An accepted AI value MUST be included in ordinary CDS-500 field-level verification when published.

**CDS700-R103** Before a downstream mismatch involving AI-originated content is dispositioned as an AI-content defect, its triage record MUST evidence that mapping, transformation and channel behaviour were checked and excluded.

**CDS700-R104** AI MAY assist with anomaly triage; repair actions remain governed by field ownership and CDS-500 policy.

## 32. Audit, Observability and Cost *(normative)*

Recommended operational telemetry: work volume and completion status; acceptance, rejection and correction rates; unknown and abstention rates; validation and guardrail failures by reason code; model, workflow and dictionary versions; latency, token or compute usage and cost; human review time; downstream publication and verification outcomes.

**CDS700-R105** An implementation MUST retain sufficient audit data to reconstruct how an AI proposal reached canonical or published state.

**CDS700-R106** Operational metrics SHOULD distinguish quality, throughput, cost and human effort.

**CDS700-R107** A cost-optimisation change MUST NOT alter a workflow's declared evidence-class requirements, validation configuration or required review rate except through the workflow change process (§23, §33). *(This replaces the untestable v0.1 rule "cost optimisation MUST NOT silently reduce quality" with a reviewable mechanism.)*

## 33. Governance, Ownership and the Workflow Registry *(normative)*

AI governance belongs inside normal data governance (CDS-800), not in a separate experimental layer. Attribute owners, dictionary owners, channel owners and risk owners remain accountable for their domains. This section is the single home for AI governance rules; CDS-800 cites it.

**CDS700-R108** Every production AI workflow MUST have an accountable owner, a declared autonomy level, a risk class, evaluation evidence and approved destination permissions.

**CDS700-R109** Organisations operating production AI workflows MUST maintain a registry of approved workflows recording, per workflow: owner, role (§4), autonomy level, risk class, permitted fields and destinations, input data classes (R082), deterministic-eligibility disposition (R064) and current version. The registry is the mechanism behind R004's visibility requirement.

**CDS700-R110** Workflow changes MUST follow versioning, evaluation, approval and rollback policy (§23–§25); model or prompt changes that can alter output semantics MUST pass change and regression controls before rollout.

**CDS700-R111** AI-generated canonical changes MUST retain provenance and applicable human-review evidence (§18–§19).

**CDS700-R112** Deprecated workflows MUST be disabled for new work while historical audit records remain readable.

*Informative note:* AI exceptions and waivers follow the CDS-800 exception process (expiry and review included); conformance levels, the AI-Assured overlay profile and the T-AI test suite are defined in CDS-1000, which traces its tests to the CDS700-Rmmm identifiers in this chapter.

## 34. Worked Examples *(informative)*

### 34.1 Apparel colour mapping

```
Source evidence: supplier value "French Navy" (E1 supplier record)
Task: dictionary mapping
AI proposal: canonical colour = navy
Dictionary status: existing canonical value
Facet projection: blue
Autonomy: A3 (bounded, R011 controls active) for approved supplier
Validation: pass
Canonical write: MF_colour = navy
Provenance retained: AI work object + source value
Publication: channel displays "French Navy", filter "Blue"
Verification: observed values match expected
```

### 34.2 Unknown homewares finish

```
Source evidence: "smoked eucalypt finish"
AI proposal candidates: smoked_wood (0.54), dark_wood (0.49)
Dictionary status: no exact or approved alias
Outcome: ABSTAIN
Action: create dictionary review request
Canonical value: unchanged
Customer facet: not published until approved
```

### 34.3 Product description generation

```
Inputs: canonical title, material, dimensions, care, included items;
        approved brand voice; prohibited-claim rules
AI output: draft short description and bullets
Validation: no unsupported claims; measurements match canonical fields
Autonomy: A2 governed draft
Human action: edit and accept
Publication: ordinary channel workflow
```

### 34.4 Channel category assistance

```
Internal category: Homewares > Living Room > Cushions
AI suggestion: candidate mappings for two external channel taxonomies
Result: channel mapping proposals only; no change to internal category
Review: channel specialist approves mappings
Publication: expected channel state generated and verified
```

---

## Appendix A — Recommended AI Work Object Fields *(informative)*

The normative machine-readable contract is the CDS-1100 ai-proposal schema. Recommended semantic fields:

```
AI_work_id, AI_task_type,
SYS_product_id, SYS_variant_id,
AI_workflow_version, AI_model_id,
AI_input_evidence[], AI_output_schema_version,
AI_proposal{}, AI_confidence{},
AI_validation_results[],
AI_review_status, AI_reviewed_by, AI_reviewed_at,
AI_disposition_reason, AI_generated_at,
SYS_created_at, SYS_updated_at
```

The exact storage model may differ; the semantic information and lineage remain available.

## Appendix B — Risk and Review Matrix *(informative)*

Category examples in this matrix are informative; the binding list of regulated categories is jurisdiction-dependent (R087).

| Risk class | Examples | Maximum default autonomy | Review expectation |
|---|---|---|---|
| R1 — Low | Aliases, internal suggestions, alt-text drafts, anomaly flags | A3 | Sampled or exception review |
| R2 — Moderate | Material mapping, classification, search synonyms, ordinary content | A2, or A3 only in bounded form (R011) | Human review or calibrated policy with sampling |
| R3 — High | Compatibility, origin, sustainability claims, channel policy attributes | A1 or A2 | Qualified human approval |
| R4 — Critical | Price, tax, safety, regulated claims, hazardous-use instructions, legal warranty | A1 | Specialist approval; deterministic controls required |

## Appendix C — Recommended AI Field Naming *(informative)*

The AI_ namespace registration lives in the CDS-300 registry; these patterns illustrate its use.

| Pattern | Example | Meaning |
|---|---|---|
| AI_<field>_suggestion | AI_material_suggestion | Proposed value for a governed field |
| AI_<field>_confidence | AI_material_confidence | Task-specific confidence |
| AI_<field>_evidence | AI_material_evidence | Evidence references |
| AI_<task>_status | AI_classification_status | Workflow state |
| AI_model_id | AI_model_id | Model/version identifier |
| AI_workflow_version | AI_workflow_version | Versioned instruction, tools and policy |
| AI_reviewed_by | AI_reviewed_by | Human or policy that authorised disposition |

Human-facing identifiers SHOULD remain descriptive even when the underlying implementation uses structured work-object properties.

## Appendix D — Platform Profiles *(informative)*

Platform-specific guidance for AI-assisted publication (including the Shopify profile that appeared as v0.1 Appendix D) lives in CDS-900. The invariants are platform-independent: AI suggestions are created and reviewed in the PIM; accepted values publish through ordinary channel mappings; channel-only AI text uses CH_ overrides; read-back verifies AI-originated values exactly as human-originated ones; manual downstream edits to PIM-owned fields are drift unless an authorised override exists.

## Appendix E — Operational Review Checklist *(informative)*

- Is the task role and autonomy level declared?
- Are the source materials eligible and referenced, with evidence classes assigned?
- Is the output schema explicit?
- Are dictionary values and unknown handling defined?
- Are deterministic validations applied, and deterministic-eligibility recorded in the registry?
- Can the workflow abstain?
- Is risk-appropriate review configured (including bounded-A3 controls where claimed)?
- Are model and workflow versions recorded?
- Can the change be previewed and rolled back?
- Will accepted values pass through normal publication and read-back verification?
- Are quality, correction rate and downstream mismatch monitored at the level the autonomy class requires?
- Can a new operator understand the AI fields and statuses without separate notes?
