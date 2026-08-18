# Commerce Data Standard (CDS)
## CDS-1100 — Reference Schemas and Machine-Readable Contracts

| Field | Value |
|---|---|
| Status | **v0.2 Review Draft** (working source; not an approved standard) |
| Release | CDS v0.2 (single corpus release per ADR-D5) |
| Date | 2026-08-04 |
| Supersedes | CDS-1100 Working Draft v0.1 |
| Normative status | §§1, 3–23 and Appendix A are normative. §2, §§24–26 and Appendices B–D are informative. |
| Findings addressed | CDS1100-1 through CDS1100-24; ADR-D3, ADR-D4, ADR-D5; open decisions D14 (via CDS-700 §6) and D21 |
| Dependencies | CDS-000 through CDS-1000; reference schema package CDS-1200 v0.2.1 |
| Audience | PIM developers, commerce platform engineers, connector authors, data architects, test-tool developers, AI workflow designers |

**Single-home notice.** CDS-1100 is the sole normative home for: the machine-readable document contracts, the common document envelope, the schema identifier and schema-versioning scheme, the extension-key grammar for document envelopes, the validation-output contract and the **CDS_\* reason-code registry** (§21). This chapter *encodes* — and never redefines — semantics owned elsewhere: verification statuses, detailed statuses and the traffic-light mapping are owned by CDS-500 §17–18; conformance levels, test suites and claims by CDS-1000; AI review rules by CDS-700; dictionaries and value layers by CDS-400; visible field-identifier namespaces by CDS-300; terminology by CDS-100 (CDS000-R005).

**Relationship to the shipped package.** Every schema this chapter describes exists in the CDS-1200 Reference Package v0.2.1 (`schemas/`, 21 schemas at schema version 0.2.0). Where this chapter states what a schema requires, the statement has been checked against the shipped schema text. The published specification governs where package and prose conflict (CDS-1200 README), but as of v0.2 no such conflict is known.

---

## 1. Purpose and Scope *(normative)*

CDS-1100 defines the machine-readable contracts that represent the entities and lifecycle records specified by the Commerce Data Standard. It translates the architectural language of products, attributes, dictionaries, channel projections, observations and verification into interoperable documents that software can validate and exchange.

This chapter defines logical contracts and their reference JSON Schema expression. It does not prescribe a database engine, API style, message broker, programming language or storage topology. A relational, document, graph, event-stream or spreadsheet-backed implementation MAY conform if its exported and consumed documents satisfy these contracts.

**CDS1100-R001** A CDS machine-readable document MUST declare its document type, schema identifier, corpus release version, document identifier and revision (the envelope, §5).

**CDS1100-R002** An implementation MUST validate externally exchanged CDS documents against the applicable schema and profile constraints before accepting them as authoritative input.

**CDS1100-R003** A serialization or API transport MUST NOT alter the semantic meaning, type or precision of a CDS value.

## 2. Contract Design Principles *(informative)*

- **Explicit over inferred.** Types, identifiers, scopes and authorities are declared, never guessed from labels or field order.
- **Stable identity.** Business identity is separate from labels, array positions and channel identifiers.
- **Composable contracts.** Shared definitions (envelope, localised text, measurement, money, entity reference) are referenced, not copied.
- **Human-readable payloads.** Keys and enumerations remain understandable to operators and reviewers.
- **Strict core, governed extension.** Core property sets are complete and closed; extension points are namespaced and governed (§20).
- **Canonical and observed separation.** Authoritative values never share storage locations with downstream read-back values (CDS-200, CDS-500).
- **Validation before mutation.** Invalid input is rejected or quarantined before it changes canonical state (CDS-400 §17).
- **Evidence by design.** Publication and verification contracts retain revisions, versions, hashes and comparison evidence.
- **Round-trip safety.** Serializing and parsing preserves identifiers, values, units, significant order and null semantics.
- **AI containment.** AI outputs are proposals, distinct from accepted canonical values (CDS-700).

**CDS1100-R004** A contract MUST distinguish absent, explicitly null, empty string, empty list and zero wherever those states have different business meaning.

**CDS1100-R005** A list whose order is semantically significant MUST declare that significance in its Attribute Definition or contract documentation.

## 3. Serialization and Schema Dialect *(normative)*

JSON is the normative interchange syntax for CDS reference contracts. The reference validation language is JSON Schema Draft 2020-12. Implementations MAY provide YAML 1.2-compatible views for human editing (Appendix C) and MAY expose equivalent Protocol Buffers, Avro, XML or database schemas, provided a lossless mapping to the normative JSON contract is documented and tested.

| Concern | CDS baseline |
|---|---|
| Character encoding | UTF-8 |
| JSON Schema dialect | Draft 2020-12, declared via `$schema` |
| Media type | `application/json` or a profile-specific type; APIs SHOULD identify the CDS document type through media type or envelope |
| Date-time | RFC 3339-compatible timestamp |
| Duration | ISO 8601 duration string where needed |
| Language tag | BCP 47-compatible string |
| Country | ISO 3166-1 alpha-2 where a country code is required; display names are separate from codes |
| Currency | ISO 4217 alphabetic code |
| Units | Stable CDS or recognised unit code; value and unit are distinct fields |

**CDS1100-R006** Exchanged JSON MUST be encoded as UTF-8, and reference schemas MUST declare the Draft 2020-12 dialect via `$schema`.

**CDS1100-R007** Timestamps MUST include a timezone (UTC `Z` or an explicit offset). *The shipped schemas enforce this doubly: every date-time property asserts both `format: date-time` and a pattern requiring the offset, so environments that skip format assertion still reject offset-less timestamps.*

**CDS1100-R008** JSON numbers MUST NOT be used for identifiers such as GTIN, SKU, MPN or postal codes; leading zeros and exact textual form are significant, so identifiers are strings.

**CDS1100-R009** Monetary values MUST be represented in a decimal-safe form that guarantees declared precision; binary floating-point rounding MUST NOT silently alter a published amount. The reference money contract is defined in §7.

**CDS1100-R010** Implicit YAML typing MUST NOT change CDS scalar values; YAML representations MUST be converted to the canonical JSON data model before schema validation (Appendix C).

## 4. Schema Package Architecture and Identifiers *(normative — implements ADR-D5)*

The reference package is a registry of independently versioned schemas. Shared primitives live in `common/` and are referenced from entity schemas. The shipped v0.2 layout (21 schemas):

```
schemas/
  common/     envelope, entity-reference, localised-text, measurement, money
  core/       product, variant, attribute-definition
  reference/  dictionary, dictionary-value, category, taxonomy-mapping, facet-definition
  channel/    channel-profile, field-mapping, publication-record,
              observation-record, verification-result
  automation/ ai-proposal
  assurance/  conformance-manifest, validation-output
```

Platform and industry profiles are not schema directories in v0.2: platform-specific constraints live in CDS-900 profiles and industry constraints in CDS-1500, applied by composition (§20). The v0.1 `profiles/` directory sketch is withdrawn.

Three identity layers, per ADR-D5:

1. **Schema identity.** Every schema `$id` is a release-independent URN: `urn:cds:schema:<domain>:<name>` (for example `urn:cds:schema:core:product`). The specification release is *not* part of the URN, so identifiers are stable across releases. The v0.1 `https://schemas.cds.example/v1/...` example URIs are retired.
2. **Schema version.** Every schema carries its own semantic version in a `version` keyword (all shipped schemas: `0.2.0`), bumped by the compatibility rules of §22, independently of chapter prose revisions.
3. **Instance release pinning.** The envelope's `cds_version` is a per-release constant (`{"const": "0.2"}` in the v0.2 package). An instance therefore pins the corpus release it was written against, and a validator can refuse mismatched generations.

**CDS1100-R011** Every published schema MUST have a stable, release-independent `$id` of the form `urn:cds:schema:<domain>:<name>`, independent of any file-system location.

**CDS1100-R012** Every published schema MUST declare its own semantic version in a `version` keyword, distinct from both the corpus release and any document revision.

**CDS1100-R013** A schema package release MUST publish a manifest listing schema identifiers, versions, per-file hashes, and a package-level hash. *(The shipped `package-manifest.json` carries a `schema_registry` inventory and a `package_hash`; its self-hash convention is documented in the CDS-1200 README.)*

**CDS1100-R014** A profile schema MAY add constraints through composition but MUST NOT redefine the meaning of a core property (§20).

*Informative note:* schemas are resolved offline from the registry — the reference validator loads all schemas from the package and resolves `$ref` URNs against that in-memory registry. URNs carry no resolution promise; nothing dereferences them over a network. Registered `https` URIs were deferred until a domain and governance body exist (ADR-D5, revisit at v0.9).

## 5. Common Document Envelope *(normative)*

Every top-level CDS document uses a common envelope (`urn:cds:schema:common:envelope`). The envelope supports routing, validation, audit, multi-tenant labelling and version-specific interpretation without requiring consumers to inspect business fields first.

| Property | Type | Required | Purpose |
|---|---|---|---|
| `cds_schema` | string (URN) | Yes | `$id` of the schema this document conforms to |
| `cds_version` | const `"0.2"` | Yes | Corpus release the document targets |
| `document_type` | string | Yes | Logical entity or lifecycle record type |
| `document_id` | string | Yes | Stable globally unique document identifier |
| `revision` | integer >= 1 or string | Yes | Monotonic entity revision or immutable revision identifier |
| `status` | enum `draft`, `active`, `deprecated`, `archived` | Yes | Document lifecycle state |
| `tenant_id` | string | Optional | Organisation boundary label for multi-tenant implementations (§6) |
| `created_at` | date-time | Yes | Creation timestamp of the logical record |
| `updated_at` | date-time | Yes | Timestamp of the current revision |
| `source_system` | string | Yes | System that produced the document |
| `correlation_id` | string | Optional | Links related import, publish, observe and verify operations |
| `extensions` | object | Optional | Governed extensions; key grammar per §20 |

```json
{
  "cds_schema": "urn:cds:schema:core:product",
  "cds_version": "0.2",
  "document_type": "product",
  "document_id": "prd_shirt_100",
  "revision": 42,
  "status": "active",
  "tenant_id": "org_reference",
  "created_at": "2026-07-18T03:12:10Z",
  "updated_at": "2026-08-03T00:08:17Z",
  "source_system": "cds-reference-package",
  "correlation_id": "job_01K1PUB9"
}
```

*Composition idiom (preserved from v0.1, now safe).* Entity schemas compose the envelope with `allOf: [{$ref: envelope}, {entity properties}]` and close the document with `unevaluatedProperties: false`. In v0.1 this closure was a trap: it forbade properties the prose promised (lifecycle, provenance, reviewer fields). In v0.2 the property sets are complete — every property a contract names is present in its schema — so closure now does what it should: any unnamed property is a defect, not a casualty. (CDS1100-5, CDS1100-23 resolved.)

The envelope `status` enum is the *document* lifecycle. It is deliberately distinct from the dictionary-value lifecycle owned by CDS-400 and from verification statuses owned by CDS-500; the three vocabularies never mix.

**CDS1100-R015** Every top-level CDS document MUST carry the envelope, with all envelope-required properties present.

**CDS1100-R016** `document_id` MUST remain stable across revisions of the same logical record.

**CDS1100-R017** `revision` MUST change whenever any property affecting canonical meaning or downstream projection changes.

**CDS1100-R018** A consumer MUST reject or quarantine a document whose `cds_schema` is unknown or unsupported, unless an explicitly configured forward-compatibility policy applies.

**CDS1100-R019** `cds_schema` MUST equal the `$id` of the schema against which the document is validated. *(The reference validator cross-checks this on every fixture; a mismatch is a validation failure.)*

## 6. Identity, References and Tenancy *(normative)*

CDS distinguishes canonical identifiers, human business keys and downstream identifiers. A product may hold an internal CDS identifier, one or more SKUs, supplier identifiers and channel platform identifiers. These are related but never interchangeable.

| Identifier class | Example | Authority |
|---|---|---|
| CDS entity ID | `prd_shirt_100` | PIM or CDS entity service |
| Business key | `SHIRT-100` | Organisation |
| Variant SKU | `SHIRT-100-NVY-M` | Organisation or inventory authority |
| Supplier SKU | `SUP-829103` | Supplier |
| GTIN | `09338716007824` | Assigned standards authority / brand |
| Channel ID | `gid://shopify/Product/123` | Downstream channel |
| Taxonomy node ID | `aa-1-2-3` | Taxonomy publisher |

Cross-document references use the shared entity-reference contract (`urn:cds:schema:common:entity-reference`): `document_type` + `document_id` required, optional `role` and `tenant_id`.

```json
{ "document_type": "dictionary_value", "document_id": "dictval_colour_navy", "role": "canonical_colour" }
```

**CDS1100-R020** A channel identifier MUST be stored inside a channel identity or mapping structure and MUST NOT replace the canonical CDS entity ID.

**CDS1100-R021** Cross-document references MUST use stable IDs and MUST include the referenced document type. *(v0.1's SHOULD is upgraded: the entity-reference schema requires `document_type`, so the requirement is mechanically enforced.)*

### 6.1 Tenancy — what the schema does and does not guarantee

`tenant_id` is an optional envelope property: it *labels* an organisation boundary, and single-tenant deployments legitimately omit it. Schema validation of one document **cannot** enforce a boundary between documents; tenant isolation is a property of the consuming implementation, not of any JSON Schema.

**CDS1100-R022** A multi-tenant implementation MUST prevent cross-document references from resolving across tenant boundaries unless a governed shared-reference mechanism is explicitly defined. This is an **implementation obligation**: it is not, and cannot be, a schema-level guarantee. Its test coverage is the mandatory T-TEN suite in CDS-1000 §18; the reference runner's SEM-004 check (all related fixture documents share one `tenant_id`) is an illustration of the join, not the enforcement. *(CDS1100-13 resolved by honesty rather than by pretending the envelope enforces it.)*

## 7. Type System and Standard Formats *(normative)*

Attribute Definitions declare the applicable type and constraints; values MUST conform before becoming canonical. The reference value types (the attribute-definition `value_type` enum, shipped):

| CDS type | JSON representation | Key constraints |
|---|---|---|
| `text` | string | Length, pattern, whitespace policy |
| `boolean` | boolean | No string substitutes such as yes/no |
| `integer` | integer | Minimum, maximum, unit where applicable |
| `decimal` | string | Declared scale and rounding mode (decimal-safe) |
| `date` | string | Calendar date, no time component |
| `date_time` | string | Timezone required (R007) |
| `identifier` | string | Pattern and authority required |
| `enum_reference` / `enum_reference_list` | object reference(s) | Must resolve to an active dictionary value; `dictionary_id` required (§10) |
| `measurement` | object | `urn:cds:schema:common:measurement` — string decimal `value` + `unit` |
| `money` | object | `urn:cds:schema:common:money` — string decimal `amount` + ISO 4217 `currency` |
| `localised_text` | array | Items per `urn:cds:schema:common:localised-text` |
| `composition_list` | array | Dictionary references with percentages |
| `object` | object | Nested schema required |

*Rich text is not a v0.2 reference type.* Markup-bearing content is exchanged as `text` under the sanitisation obligations of §23; a structured rich-text contract is deferred.

**Single localised-text model.** All localised values corpus-wide use one shape: an array of `{"language": "<BCP 47 tag>", "text": "..."}` objects. The v0.1 mixture of language-keyed maps (`{"en-AU": "Navy"}`), arrays and bare strings is retired; dictionary-value `canonical_label` and facet `label` are now arrays of localised-text like product content. (CDS1100-15 resolved.) The attribute-definition `label` is an operator-facing plain string in the reference schema; customer-facing labels are the localised ones.

**Measurement.** `{"value": "1.250", "unit": "kg"}` — value is a string decimal, unit a code. The measurement schema is wired into the package: product typed values reference it (`measurement` branch, §7.1), and `measurement` is an attribute-definition value type. It is no longer dead weight (CDS1100-10 resolved).

**Money.** `{"amount": "129.95", "currency": "AUD"}` — amount is a string decimal in **major units**; currency is an ISO 4217 alphabetic code. The shipped schema documents the design call in its `$comment`.

> RESOLVED — accepted as drafted (owner 2026-08-04; was new (resolved)): Money is a string decimal in major units, matching the measurement convention already in the package. Alternative: integer minor units (cents), which avoids scale ambiguity but diverges from every other numeric-as-string-decimal in the corpus. Revisit if a payments-adjacent profile needs exact minor-unit semantics.

**CDS1100-R023** A measurement MUST store the numeric value separately from its unit.

**CDS1100-R024** A localised value MUST identify the language of each translation using the localised-text contract.

### 7.1 Typed attribute values

Canonical product attribute values are constrained to a minimal **typed-value** shape (product schema `$defs/typed_value`): a value is exactly one of

`{dictionary_value_id, percentage?}` | `{text: [localised-text]}` | `{number, unit?}` | `{measurement}` | `{money}` | `{boolean}` | `{identifier}` | `{date_time}`

or a non-empty array of such values. Bare scalars are rejected: `"MF_material": 42` no longer validates (CDS1100-14).

*Deliberate limits.* The typed-value shape is intentionally minimal. It guarantees that every canonical value has a declared representation; it does **not** encode the binding between a specific attribute and its declared `value_type`, cardinality or dictionary — JSON Schema cannot look up an Attribute Definition while validating a product. Enforcing that a value keyed `MF_material` actually is a `composition_list` against `dict_material` remains an implementation obligation (§21.4). The same limit applies to variant `variant_attributes`, which the shipped schema constrains only to an object.

**CDS1100-R025** A canonical attribute value MUST use the typed-value shape (or an array of it), and an implementation MUST additionally validate each value against its Attribute Definition's declared type, cardinality and dictionary before accepting it as canonical.

## 8. Canonical Product Contract *(normative)*

`urn:cds:schema:core:product`. The Product contract represents the logical commercial item: product-level truth, classification, content and references to variants. Channel projections and observations are separate documents (§15–§17).

Required beyond the envelope: `product_id`, `business_key`, `classification` (`product_family_id`, `product_type_id`, `category_id` — all IDs), `content` (localised `title` required; `short_description`, `long_description` optional), `attributes`, `variant_ids`. Optional: `brand_id`, `manufacturer_part_number`, `media` and `relationships` (entity-reference arrays), and the `lifecycle` (`introduction_date`, `end_of_sale_date`, `approval_state`) and `provenance` (`source_type`, `source_reference`, `acquired_at`) groups restored in v0.2 (CDS1100-23).

Attribute keys are validated by the strict semantic-name pattern `^[A-Z][A-Z0-9]*_[a-z0-9]+(?:_[a-z0-9]+)*$` (prefix grammar owned by CDS-300); attribute values use §7.1 typed values.

```json
{
  "product_id": "prd_shirt_100",
  "business_key": "SHIRT-100",
  "classification": {
    "product_family_id": "family_apparel",
    "product_type_id": "type_shirt",
    "category_id": "cat_womens_shirts"
  },
  "content": { "title": [{ "language": "en-AU", "text": "Relaxed Linen Shirt" }] },
  "attributes": {
    "MF_material": [{ "dictionary_value_id": "material_linen", "percentage": "100.00" }],
    "MF_fit": { "dictionary_value_id": "fit_relaxed" }
  },
  "variant_ids": ["var_shirt_100_navy_s", "var_shirt_100_navy_m"]
}
```

**CDS1100-R026** Product attributes MUST be keyed by stable Attribute Definition identifiers conforming to the CDS-300 namespace grammar, never by mutable display labels.

**CDS1100-R027** A product contract MUST NOT embed observed channel values in its canonical attributes object.

**CDS1100-R028** Variant references MUST resolve to sellable-unit records whose parent `product_id` matches the product. *(Executed as reference semantic test SEM-001; see §21.4.)*

## 9. Variant and Sellable Unit Contract *(normative)*

`urn:cds:schema:core:variant`. The Variant represents a separately sellable, inventory-addressable unit. Required beyond the envelope: `variant_id`, `product_id`, `sku`, `option_values` (each `{option, value_id, display?}`), `sellability` (`sellable`, `preorder`, `unavailable`, `retired`). Optional: `barcode_identifiers`, `variant_attributes`.

Barcode identifiers are typed and length-checked per scheme:

| Scheme | Length | Note |
|---|---|---|
| `gtin_8` | exactly 8 digits | |
| `gtin_12`, `upc` | exactly 12 digits | |
| `gtin_13`, `ean` | exactly 13 digits | |
| `gtin_14` | exactly 14 digits | |

Values are strings, so leading zeros are preserved — the positive reference fixture deliberately uses the zero-leading GTIN-14 `09338716007824` (CDS1100-21).

```json
{
  "variant_id": "var_shirt_100_navy_m",
  "product_id": "prd_shirt_100",
  "sku": "SHIRT-100-NVY-M",
  "option_values": [
    { "option": "colour", "value_id": "colour_navy", "display": "French Navy" },
    { "option": "size", "value_id": "size_m", "display": "M" }
  ],
  "barcode_identifiers": [{ "scheme": "gtin_13", "value": "9338716007824" }],
  "sellability": "sellable"
}
```

**CDS1100-R029** A variant MUST carry a stable SKU or an explicitly documented alternative sellable-unit key.

**CDS1100-R030** Option values MUST reference controlled values (`value_id`) when a dictionary exists for that option; display strings are presentation only.

**CDS1100-R031** A barcode identifier MUST declare its scheme, MUST be represented as a string preserving leading zeros, and MUST satisfy the exact digit length of its scheme.

**CDS1100-R032** Inventory quantity SHOULD remain owned by the declared inventory authority and MAY be referenced rather than duplicated into the canonical record (per-fact authority: CDS-200).

## 10. Attribute Definition Contract *(normative)*

`urn:cds:schema:core:attribute-definition`. Attribute Definitions carry the schema intelligence of CDS: what a value means, where it applies, how it is validated, displayed, faceted, compared and proposed by AI. Required beyond the envelope: `attribute_id` (semantic-name pattern), `label`, `scope` (`product`, `variant`, `category`, `channel`, `system`), `value_type` (§7 table), `cardinality` (`{minimum, maximum|null}`), `behaviour` (`filterable`, `searchable`, `displayable`, `comparison_strategy` — all required). Optional: `description`, `dictionary_id`, `channel_mappings` (entity references).

```json
{
  "attribute_id": "MF_material",
  "label": "Material",
  "scope": "product",
  "value_type": "composition_list",
  "dictionary_id": "dict_material",
  "cardinality": { "minimum": 1, "maximum": 10 },
  "behaviour": {
    "filterable": true, "searchable": true, "displayable": true,
    "comparison_strategy": "unordered_composition"
  }
}
```

**CDS1100-R033** An Attribute Definition MUST declare scope, value type, cardinality and behaviour (including a comparison strategy for every attribute that participates in downstream verification).

**CDS1100-R034** An Attribute Definition whose `value_type` is `enum_reference` or `enum_reference_list` MUST declare `dictionary_id`. *(Mechanically enforced by if/then in the shipped schema; CDS1100-16.)*

**CDS1100-R035** Attribute labels MAY change and be localised at the display layer without changing `attribute_id`.

## 11. Dictionary Definition and Value Contracts *(normative)*

`urn:cds:schema:reference:dictionary` and `urn:cds:schema:reference:dictionary-value`. CDS separates the Dictionary Definition (name, purpose, `value_type` flat/hierarchical, `default_locale`, `governance_owner`, `dictionary_version` — all required) from its Values. Value semantics, lifecycle and governance are owned by CDS-400; this section defines only the machine shape.

Dictionary Value — required beyond the envelope: `dictionary_value_id`, `dictionary_id`, `canonical_code` (lower snake case pattern), `canonical_label` (localised-text array), `aliases` (unique strings), `facet_memberships` (`{facet_id, value_id, primary}`), `channel_representations` (map of channel key to scalar). Optional: `parent_value_id` for hierarchical dictionaries.

```json
{
  "dictionary_value_id": "colour_navy",
  "dictionary_id": "dict_colour",
  "canonical_code": "navy",
  "canonical_label": [{ "language": "en-AU", "text": "Navy" }],
  "aliases": ["navy blue", "french navy", "dark navy"],
  "facet_memberships": [{ "facet_id": "facet_colour_family", "value_id": "facet_blue", "primary": true }],
  "channel_representations": { "google_merchant": "Blue", "shopify_filter": "Blue" }
}
```

**CDS1100-R036** Dictionary Value identity MUST NOT depend on the displayed label or array position.

**CDS1100-R037** Aliases MUST NOT be treated as additional canonical values (intake and quarantine rules: CDS-400 §17).

**CDS1100-R038** Facet memberships MUST reference governed facet values, never arbitrary strings. *(Executed as reference semantic test SEM-002; see §21.4.)*

**CDS1100-R039** Channel representations SHOULD be stored at dictionary or mapping level when they apply consistently across products.

## 12. Classification and Taxonomy Mapping Contracts *(normative)*

`urn:cds:schema:reference:category` and `urn:cds:schema:reference:taxonomy-mapping`. Internal category identity remains stable when external taxonomies change.

Category — required beyond the envelope: `category_id`, `parent_id` (nullable at the root), `name`, `path`, `product_family_id`, `required_attribute_ids`. **`path` is an ordered array of stable ancestor `category_id`s ending with the category's own id** — identifiers, not display labels, so renaming a category never rewrites descendants' paths (CDS1100-15, stable-identity principle).

Taxonomy Mapping — required beyond the envelope: `mapping_id`, `internal_category_id`, `channel`, `taxonomy_version`, `external_node_id`, `mapping_status` (`proposed`, `approved`, `deprecated`, `rejected`), `inherited`.

```json
{
  "mapping_id": "map_cat_womens_shirts_shopify",
  "internal_category_id": "cat_womens_shirts",
  "channel": "shopify",
  "taxonomy_version": "2026-Q3",
  "external_node_id": "aa-1-2-3",
  "mapping_status": "approved",
  "inherited": false
}
```

**CDS1100-R040** An external taxonomy mapping MUST identify the external taxonomy version where the publisher provides one.

**CDS1100-R041** A category `path` MUST consist of stable category identifiers, and a category parent reference MUST NOT create a cycle. *(Acyclicity is graph-level and remains an implementation obligation — §21.4.)*

**CDS1100-R042** A taxonomy remap MUST create a new mapping revision and MUST NOT rewrite historical publication evidence.

## 13. Facet Definition Contract *(normative)*

`urn:cds:schema:reference:facet-definition`. A facet is a customer-experience projection, not merely an attribute flag; facet semantics, UX behaviour, SEO and accessibility rules are owned by CDS-600. Required beyond the envelope: `facet_id`, `label` (localised-text array), `source_attribute_id`, `selection_mode` (`single`, `multi_or`, `multi_and`, `range`), `sort_mode` (`configured`, `alphabetical`, `count`, `numeric`), `value_ids` (unique).

```json
{
  "facet_id": "facet_colour_family",
  "label": [{ "language": "en-AU", "text": "Colour" }],
  "source_attribute_id": "VAR_colour",
  "selection_mode": "multi_or",
  "sort_mode": "configured",
  "value_ids": ["facet_black", "facet_white", "facet_blue", "facet_green", "facet_red"]
}
```

**CDS1100-R043** A customer facet MUST reference a controlled value set (or, for `range` mode, a declared numeric/date range model per CDS-600).

**CDS1100-R044** Facet value order and selection logic MUST be explicit; raw supplier values MUST NOT be exposed as facet values without dictionary governance (CDS-400) and UX review (CDS-600).

## 14. Channel Profile and Field Mapping Contracts *(normative)*

`urn:cds:schema:channel:channel-profile` and `urn:cds:schema:channel:field-mapping`. Channel Profile semantics — capabilities, ownership modes, limits, write semantics — are owned by CDS-500 §5 and §7; platform-specific profile content by CDS-900.

**Field Mapping is a standalone contract in v0.2** (resolving open decision D21 in favour of standalone): `urn:cds:schema:channel:field-mapping`, with all properties required — `source_field`, `target_field`, `source_layer` (`canonical`, `display`, `facet`, `search` — the ADR-D4 value layers), `transformation`, `transformation_version`, `write_mode` (`replace`, `merge`, `append`), `read_back_path` (nullable when the target is not readable), `comparison_strategy`.

A Channel Profile (required: `channel_profile_id`, `channel`, `profile_version`, `capabilities`, `field_mappings`) MAY inline field mappings; each inlined item conforms to the standalone field-mapping contract by `$ref`. **Authority:** the mapping set pinned by a Publication Record's `mapping_set_version` (§15) is authoritative for interpreting that publication; a channel profile's inlined `field_mappings` express the profile's *current* mapping set and are superseded, for historical interpretation, by whatever version the publication record pinned.

> RESOLVED — accepted as drafted (owner 2026-08-04; was D21 (resolved)): Field mapping ships as a standalone envelope-free component schema referenced by channel-profile — standalone won, and the composition keeps one authoritative shape. A top-level *enveloped* "mapping set" document type (independently publishable, revision-controlled) is deferred; today `mapping_set_version` is a version string, not a document reference. Alternative: promote mapping sets to full documents in v0.3.

The shipped capability block is a deliberately minimal core set of four booleans (`supports_readback`, `supports_partial_update`, `supports_variant_attributes`, `supports_structured_metafields`); richer capability declarations (limits, normalisation behaviour, ownership defaults) are profile content per CDS-500 §5 and MAY be carried under `extensions` until standardised.

**CDS1100-R045** A Field Mapping MUST identify source field, source value layer, target field, transformation and transformation version, write mode, read-back path (or its explicit absence) and comparison strategy.

**CDS1100-R046** A mapping target path MUST be interpreted within the named Channel Profile, not as a global CDS path.

**CDS1100-R047** A channel capability declaration MUST distinguish unsupported fields from supported-but-currently-absent values (observation coverage model: CDS-500 §15; encoded in §16).

## 15. Publication Record Contract *(normative)*

`urn:cds:schema:channel:publication-record`. The Publication Record is immutable evidence of what the PIM intended to publish: the expected channel state generated from a specific canonical revision under a specific mapping set. Semantics: CDS-500 §6 and §8–9.

Required beyond the envelope: `publication_id`, `product_id`, `channel_profile_id`, `canonical_revision`, `expected_state`, `publication_status` (`queued`, `preflight_failed`, `published`, `partially_published`, `failed`), `published_at` (nullable until transport), `transport_reference` (nullable), `mapping_set_version`, `payload_hash` (`sha256:` + 64 hex), `preflight_result` (`passed`, `failed`, `not_run`), `transport_status` (`queued`, `sent`, `acknowledged`, `rejected`, `failed`).

The v0.1 conflation of preflight and transport into one status is resolved: **preflight outcome, transport status and overall publication status are three separate properties**, so "valid but rejected by the channel" and "never dispatched because preflight failed" are distinguishable machine states (CDS1100-3).

```json
{
  "publication_id": "pub_shopify_shirt_100_r42",
  "product_id": "prd_shirt_100",
  "channel_profile_id": "chp_shopify_main",
  "canonical_revision": 42,
  "expected_state": { "title": "Relaxed Linen Shirt", "material": ["Linen"] },
  "publication_status": "published",
  "published_at": "2026-08-03T00:10:00Z",
  "transport_reference": "gid://shopify/Product/123456",
  "mapping_set_version": "shopify-1.4.0",
  "payload_hash": "sha256:2af3...",
  "preflight_result": "passed",
  "transport_status": "acknowledged"
}
```

**CDS1100-R048** A Publication Record MUST identify the exact canonical revision and mapping-set version used to produce the expected state. *(Revision pinning is executed as reference semantic test SEM-003; see §21.4.)*

**CDS1100-R049** Transport acknowledgement MUST remain distinct from preflight outcome and from field-level verification status ("acknowledgement is not proof": CDS-500 §9).

**CDS1100-R050** The expected payload's immutable hash MUST be recorded; the full payload MAY be stored externally by reference provided the evidence location is retrievable under CDS-500 §24.

## 16. Observation Record Contract *(normative)*

`urn:cds:schema:channel:observation-record`. The Observation Record stores downstream state read back from a channel. It is evidence, not canonical truth. Observation semantics and the coverage model are owned by CDS-500 §14–15.

Required beyond the envelope: `observation_id`, `publication_id`, `product_id`, `channel_profile_id`, `observed_at`, `coverage`, `observed_state`, `channel_revision` (nullable), `observation_method` (`api_read`, `feed_diagnostic`, `scrape`, `manual`). Optional: `channel_entity_id` (nullable channel-native identity).

`coverage` is **per-field**: two required lists of JSON Pointer paths, `supported` and `unobservable`. This replaces the v0.1 bare description and makes the missing-versus-unobservable distinction machine-checkable — a field absent from `observed_state` but listed in `supported` is *missing*; a field listed in `unobservable` can never be missing (CDS1100-2).

```json
{
  "observation_id": "obs_shopify_shirt_100_001",
  "publication_id": "pub_shopify_shirt_100_r42",
  "product_id": "prd_shirt_100",
  "channel_profile_id": "chp_shopify_main",
  "observed_at": "2026-08-03T00:11:42Z",
  "observation_method": "api_read",
  "coverage": { "supported": ["/title", "/material", "/tags"], "unobservable": ["/search_index_tokenisation"] },
  "observed_state": { "title": "Relaxed Linen Shirt", "material": ["Linen"] },
  "channel_revision": null,
  "channel_entity_id": "gid://shopify/Product/123456"
}
```

**CDS1100-R051** Observation data MUST be stored separately from canonical state and from expected channel state.

**CDS1100-R052** An Observation Record MUST declare its observation method and timestamp.

**CDS1100-R053** The coverage declaration MUST distinguish, per field, a missing value from a field that is unobservable through the selected method.

## 17. Verification Result Contract *(normative — encodes CDS-500 §17, never redefines it)*

`urn:cds:schema:channel:verification-result`. Verification Results compare expected with observed field representations under declared comparison strategies. **All status semantics are owned by CDS-500**: the core enum and detailed statuses by §17, the traffic-light mapping by §18, aggregation by §17.6. This schema encodes them verbatim per ADR-D3.

Required beyond the envelope: `verification_id`, `publication_id`, `observation_id`, `verified_at`, `overall_status`, `field_results`. Optional: `coverage_ratio` (0..1 — observable fraction of contracted fields, CDS-500 §17.6), `comparison_engine_version` (reproducibility), `presentation_status` (`green`, `amber`, `red`, `grey` — informative presentation derived per CDS-500 §18, never a stored status).

Each field result carries:

| Property | Requirement |
|---|---|
| `field_path` | Required. JSON Pointer (RFC 6901) into expected/observed state — replaces the v0.1 bare field name |
| `expected`, `observed` | Required (any type, may be null) |
| `comparison_strategy` | Required; from the CDS-500 §16 registry |
| `status` | Required; the 8-value core enum: `MATCH`, `MISSING`, `MISMATCH`, `PENDING`, `UNOBSERVABLE`, `NOT_APPLICABLE`, `OVERRIDDEN`, `ERROR` |
| `detailed_status` | Optional; the CDS-500 §17.2 detailed set with deterministic rollup to the core status |
| `reason_code` | **Required whenever `status` is not `MATCH`** (schema-enforced if/then); `^CDS_[A-Z_]+$`, from the §21 registry |
| `repair_action` | Optional |
| `message` | Optional free text; never a substitute for `reason_code` (CDS500-R063) |

```json
{
  "field_path": "/material",
  "expected": ["Linen"],
  "observed": [],
  "comparison_strategy": "unordered_text_set",
  "status": "MISSING",
  "detailed_status": "MISSING_DOWNSTREAM",
  "reason_code": "CDS_OBSERVED_EMPTY"
}
```

**CDS1100-R054** The verification-result contract MUST encode the CDS-500 §17 status enum verbatim and MUST NOT introduce, remove or re-map statuses.

**CDS1100-R055** Every field-level result MUST identify its field by JSON Pointer, its comparison strategy and its core status.

**CDS1100-R056** Every field-level result whose core status is not `MATCH` MUST carry a `reason_code` from the §21 registry (encodes CDS500-R063; mechanically enforced by the shipped schema and covered by a negative fixture).

**CDS1100-R057** Traffic-light colour MUST NOT be stored as a verification status; it is presentation derived per CDS-500 §18. *(The package's "uppercase GREEN rejected as a status" negative fixture expresses this.)*

## 18. AI Proposal and Provenance Contract *(normative — encodes CDS-700, never redefines it)*

`urn:cds:schema:automation:ai-proposal`. AI outputs are proposals with evidence and confidence, not canonical values. All AI policy — autonomy levels, review rules, evidence classes, abstention — is owned by CDS-700; this schema encodes the record.

Required beyond the envelope: `proposal_id`, `target_document_id`, `target_field`, `proposed_value` (any type), `confidence` (number 0..1), `evidence` (non-empty array of `{source_type, source_reference, excerpt|null}`), `model_id`, `workflow_version`, `review_state`, `task_type` (`extraction`, `mapping`, `classification`, `writing`, `translation`, `analysis`), `validation_results` (array of §21 validation-output items). Optional: `reviewer` (nullable until reviewed), `accepted_revision` (nullable until accepted).

`review_state` uses the **shared enum** `proposed`, `review_required`, `accepted`, `rejected`, `superseded`, `expired` — identical to CDS-700 §6 (CDS700-R015); CDS-700 and this schema describe the same record, resolving the v0.1 vocabulary split (D14).

```json
{
  "proposal_id": "aip_01K1MAT9",
  "target_document_id": "prd_shirt_100",
  "target_field": "/attributes/MF_material",
  "proposed_value": { "dictionary_value_id": "material_linen", "percentage": "100.00" },
  "confidence": 0.97,
  "evidence": [{ "source_type": "supplier_description", "source_reference": "doc_sup_829103", "excerpt": "100% pure linen" }],
  "model_id": "example-extractor-2",
  "workflow_version": "extract-material-1.3.0",
  "review_state": "proposed",
  "task_type": "extraction",
  "validation_results": []
}
```

**CDS1100-R058** An AI Proposal MUST remain distinguishable from accepted canonical data until an authorised workflow accepts it.

**CDS1100-R059** A proposal MUST identify its evidence, calibrated confidence, model identifier and workflow version, and MUST carry its validation results in the §21 validation-output contract.

**CDS1100-R060** Acceptance MUST create an auditable link from the proposal to the canonical revision it affected (`accepted_revision`, plus the reviewing identity in `reviewer`).

## 19. Conformance Manifest Contract *(normative — encodes CDS-1000 §23, never redefines it)*

`urn:cds:schema:assurance:conformance-manifest`. Conformance levels, test suites, claim rules and manifest semantics are owned by CDS-1000; this schema is their machine expression.

Required beyond the envelope: `manifest_id`, `implementation_name`, `implementation_version`, `claimed_level` (`Foundation`, `Structured`, `Publisher`, `Verified`, `Governed` — the ADR-D1 ladder), `profiles` (unique strings), `test_summary` (`passed`, `failed`, `not_tested`, `inconclusive` — all four counts required), `evidence_uri`, `test_suite_version`, `assessment_method` (`self-attestation`, `customer-assessment`, `independent-assessment`).

**CDS1100-R061** A Conformance Manifest MUST identify the implementation scope and MUST NOT imply conformance beyond that scope (claim rules: CDS-1000 §24).

**CDS1100-R062** The manifest MUST identify the exact test-suite version, the applicable profiles and the assessment method.

**CDS1100-R063** Every executed test case MUST be counted in exactly one `test_summary` disposition; failed or not-executed mandatory tests MUST NOT be omitted. *(The v0.1 fixture that claimed "Verified" with a count contradicting its own evidence report is retired; the shipped fixture counts match the shipped evidence — CDS1100-6.)*

## 20. Extension and Profile Rules *(normative)*

CDS supports platform, industry and organisation extensions without uncontrolled schema fragmentation. Envelope `extensions` keys are constrained by the shipped schema's `propertyNames` pattern to **dotted reverse-namespace form** — `^[a-z][a-z0-9_]*(\.[a-z][a-z0-9_]*)+$`, e.g. `com.example.photography_status`, `profile.apparel.garment_measurement_set_id` — so namespace governance is mechanically enforced at validation time, not merely urged (CDS1100-12). Visible *field-identifier* prefixes (`MF_`, `VAR_`, ...) are a separate registry owned by CDS-300; the two grammars do not overlap.

```json
"extensions": {
  "com.example.warehouse_zone": "A3",
  "profile.apparel.garment_measurement_set_id": "gms_womens_tops_au"
}
```

**CDS1100-R064** An extension key MUST use the dotted-namespace grammar, and its namespace MUST be organisationally controlled with an identified owner.

**CDS1100-R065** An extension MUST NOT reuse a core property name with a different meaning, and a profile MAY require additional properties, restrict enumerations or tighten validation but MUST NOT make a core mandatory property optional.

**CDS1100-R066** Unknown governed extensions SHOULD be preserved during read-modify-write operations unless an explicit policy authorises removal.

## 21. Validation Output and the Reason-Code Registry *(normative — registry home)*

### 21.1 Validation output contract

`urn:cds:schema:assurance:validation-output` — shipped in v0.2 (it was promised and absent in v0.1; CDS1100-1). A validation finding is machine-actionable and human-readable:

| Property | Requirement |
|---|---|
| `document_id` | Required — the affected document |
| `field_path` | Required — JSON Pointer (RFC 6901) to the instance location |
| `reason_code` | Required — `^CDS_[A-Z_]+$` from the §21.3 registry |
| `severity` | Required — `error`, `warning`, `info` |
| `message` | Optional free text (nullable) |

Validation-output items are embedded by the ai-proposal contract (`validation_results`) and are the recommended shape for import, preflight and API validation responses.

**CDS1100-R067** A validation finding MUST identify the affected document, the instance location as a JSON Pointer, a registered reason code and a severity; severity MUST distinguish errors, warnings and informational findings.

**CDS1100-R068** A rejected import SHOULD retain the original value and source provenance in quarantine rather than discarding it (quarantine model: CDS-400 §17).

### 21.2 Registry governance

**CDS1100-R069** Machine-readable reason codes MUST match `^CDS_[A-Z_]+$` and MUST be drawn from the CDS_* reason-code registry defined here. Additions, deprecations and semantics changes follow CDS-800 change control; a code, once registered, is never reused with a different meaning. Organisation-specific codes are not permitted in the `CDS_` namespace; organisations extend via their own prefix under the CDS-300 extension registry.

### 21.3 Seed registry (v0.2)

Reason codes are a v0.2 design with no legacy precedent (ADR-D3). The seed list below is the initial registry content; CDS-500 Appendix B mirrors the verification subset informatively.

| Reason code | Class | Typical use (detailed status where applicable) |
|---|---|---|
| CDS_OBSERVED_EMPTY | verification | MISSING_DOWNSTREAM |
| CDS_FIELD_NOT_RETURNED | verification | MISSING_DOWNSTREAM or UNOBSERVABLE (CDS-500 §17.4) |
| CDS_INTERFACE_UNSUPPORTED | verification | UNOBSERVABLE |
| CDS_PERMISSION_DENIED | verification | UNOBSERVABLE |
| CDS_STALE_OBSERVATION | verification | UNOBSERVABLE |
| CDS_AWAITING_PROPAGATION | verification | PENDING |
| CDS_PROPAGATION_WINDOW_EXPIRED | verification | post-lapse non-MATCH (CDS-500 §17.5) |
| CDS_EXPECTED_REVISION_AHEAD | verification | STALE_EXPECTED |
| CDS_VALUE_DIFFERS | verification | MISMATCH |
| CDS_UNEXPECTED_VALUE_PRESENT | verification | UNEXPECTED_DOWNSTREAM |
| CDS_IDENTITY_MISMATCH | verification | MISMATCH / drift IDENTITY_MISMATCH |
| CDS_CHANNEL_TRUNCATION | verification | MISMATCH / drift CHANNEL_TRUNCATION |
| CDS_TRANSFORMATION_FAILED | verification | TRANSFORMATION_ERROR |
| CDS_DISPATCH_REJECTED | verification | PUBLICATION_ERROR |
| CDS_READBACK_FAILED | verification | OBSERVATION_ERROR |
| CDS_COMPARATOR_FAILED | verification | COMPARISON_ERROR |
| CDS_WAIVED_EXCEPTION | verification | WAIVED |
| CDS_OVERRIDE_ACTIVE | verification | provenance on OVERRIDDEN results |
| CDS_NOT_IN_CONTRACT | verification | NOT_APPLICABLE |
| CDS_SCHEMA_VALIDATION_FAILED | validation | document fails its declared schema |
| CDS_SCHEMA_UNKNOWN | validation | `cds_schema` unknown or unsupported (R018) |
| CDS_VALUE_NOT_IN_DICTIONARY | validation | value does not resolve to an active dictionary value |
| CDS_VALUE_QUARANTINED | validation | value held in quarantine (CDS400-R054) |
| CDS_REFERENCE_UNRESOLVED | validation | cross-document reference does not resolve |
| CDS_TENANT_BOUNDARY_VIOLATION | validation | reference crosses a tenant boundary (R022) |

### 21.4 Semantic and referential integrity

JSON Schema validates one document at a time. Integrity that spans documents is specified as semantic tests. In v0.2 the reference runner **executes** the semantic catalogue (v0.1 shipped it dead; CDS1100-8):

| Test | Integrity class | Encoding requirement |
|---|---|---|
| SEM-001 | Variant references resolve; parent `product_id` matches | R028 |
| SEM-002 | Facet memberships resolve to configured facet values | R038 |
| SEM-003 | Publication `canonical_revision` equals the product revision projected | R048 |
| SEM-004 | Related documents share one tenant boundary | R022 (illustration) |

The following integrity classes remain **implementation obligations** with no reference-runner check in v0.2: dictionary-reference resolution to *active* values (lifecycle is in the dictionary-value document, not the referencing one); attribute-value conformance to the owning Attribute Definition's type, cardinality and dictionary (§7.1); category-graph acyclicity (R041); taxonomy-mapping resolution against the published external taxonomy; and tenant isolation at the storage and API layer (R022, tested via CDS-1000 §18 T-TEN).

**CDS1100-R070** An implementation MUST enforce the cross-document integrity classes above before accepting a document as authoritative, whether or not a reference-runner check exists for them.

## 22. Versioning and Compatibility *(normative — implements ADR-D5)*

Schema versioning follows the CDS governance model (change control: CDS-800). Per schema: breaking changes require a new major version; additive compatible changes a minor version; corrections that do not change accepted or produced instance meaning a patch version. The `$id` never changes with the version (§4).

| Change | Compatibility expectation |
|---|---|
| Add optional property | Usually backward compatible (minor) |
| Add required property without default/migration | Breaking |
| Remove or rename property | Breaking (rename: unless an alias/migration profile is provided) |
| Tighten enumeration | Potentially breaking |
| Add enumeration value | May break closed consumers; profile policy required |
| Change numeric precision or unit semantics | Breaking |
| Clarify description only | Patch if validation meaning is unchanged |
| Change mapping transformation | Mapping-set version change; no core schema change implied |

**CDS1100-R071** A schema MUST declare its semantic version independently of the CDS corpus release and of any document revision.

**CDS1100-R072** A breaking contract change MUST publish migration guidance and a new major schema version; the schema `$id` MUST NOT change.

**CDS1100-R073** Historical publication and verification records MUST retain the schema versions, `cds_version` and mapping-set versions under which they were created; a corpus release MUST NOT rewrite stored evidence.

*Migration note (informative):* v0.1 URNs of the form `urn:cds:schema:v0.1:*` map one-to-one to the release-independent URNs of §4 for anything already persisted (ADR-D5).

## 23. Security, Privacy and Data Minimisation *(normative)*

Product information is usually less sensitive than customer data, but contracts may carry supplier costs, unpublished products, workflow notes, provenance and user identities.

**CDS1100-R074** Secrets, API credentials and access tokens MUST NOT be embedded in CDS documents.

**CDS1100-R075** A producer MUST publish only the fields required by the destination profile and approved organisation policy; cost and margin fields SHOULD be excluded from channel payloads unless the destination is explicitly authorised.

**CDS1100-R076** Inbound documents MUST be treated as untrusted input and validated for size, recursion depth, markup, URLs and extension content; markup-bearing text MUST be sanitised before render. Schema validation MUST NOT be treated as sufficient security validation.

**CDS1100-R077** Personal reviewer identities SHOULD be represented by governed user IDs and exposed only as policy permits; logs and evidence packages MUST follow retention and access policies (CDS-500 §24, CDS-800).

Cross-tenant reference rejection: R022. External references SHOULD use allow-listed schemes and hosts where automatic retrieval is supported.

## 24. Worked Apparel Contract *(informative)*

Separation of supplier value, canonical value, customer facet, channel representation and verification evidence (four-layer value model: CDS-400; worked end-to-end in the reference fixtures):

```
Supplier input:      colour = "French Navy"; composition = "100% Linen"
Canonical:           VAR_colour -> dictionary_value_id colour_navy
                     (reference form "French Navy" retained per CDS-400 intake)
                     MF_material = [{dictionary_value_id: material_linen, percentage: "100.00"}]
Facet projection:    facet_colour_family = facet_blue; facet_material_family = linen
Shopify expected:    option colour = "French Navy"; metafield colour_family = "Blue";
                     metafield material = "100% Linen"
Google expected:     color = "Blue"; material = "Linen"
Observed Shopify:    option colour = "French Navy"; colour_family = "blue"; material = "100% linen"
Verification:        /options/colour     -> MATCH (exact_text)
                     /colour_family      -> MATCH (case_insensitive_enum)
                     /material           -> MATCH (normalised_composition)
```

Display, canonical, facet and channel values may all differ while remaining correctly mapped and verifiable — that is the point of declared comparison strategies.

## 25. Worked Homewares Contract *(informative)*

A detailed display material coexisting with a broader customer-facing family:

```
Supplier input:      material = "Tasmanian Oak"; finish = "Natural Oil"; dimensions = "45 x 45 x 50 cm"
Canonical:           MF_material = material_oak; MF_material_origin_label (display text)
                     MF_finish = finish_natural_oil
                     MF_width  = {measurement: {value:"45", unit:"cm"}}
                     MF_depth  = {measurement: {value:"45", unit:"cm"}}
                     MF_height = {measurement: {value:"50", unit:"cm"}}
Facets:              material_family = wood; finish_family = natural; room = living_room
Channels:            Shopify material = "Oak"; Google material = "Wood"; PDP display = "Tasmanian Oak"
Verification:        dimensions -> numeric-with-unit comparison
                     material   -> canonical identifier comparison
                     display    -> normalised text comparison
```

Structured measurements are exchanged as separate value-and-unit fields, not as the unparsed display string, whenever the destination supports structured fields (R023).

## 26. Conformance, Package and Decision Pointers *(informative)*

- **Conformance.** Levels, test suites, evidence and claim rules for this chapter's requirements are defined solely in CDS-1000; the machine-readable claim is §19's manifest.
- **Reference package.** The CDS-1200 Reference Package v0.2.1 ships the 21 schemas of Appendix A, positive and negative fixtures, the executed structural and semantic test catalogues, the validation runner and the regenerable manifest. Package composition, runner behaviour and evidence conventions are CDS-1200's subject matter.
- **Decisions.** The v0.1 chapter-local ADR table (CDS-ADR-1101..1110) is superseded by the global ADR register (ADR-D3 statuses and reason codes; ADR-D4 value layers; ADR-D5 identifiers and versioning). Its substance survives as requirements here: JSON + Draft 2020-12 (§3), YAML as a view not a model (§3, Appendix C), the common envelope (§5), canonical/expected/observed/verification separation (§8, §15–17), stable IDs independent of labels (§6, §11), AI-as-proposal (§18), namespaced extensions (§20), payload-by-immutable-reference (§15), stable JSON Pointer error paths (§21).

## Appendix A — Reference Schema Registry *(normative)*

The registry of shipped v0.2 schemas. `$id`s are release-independent (§4); all shipped schema versions are 0.2.0 in this release. This table is regenerated from the package manifest at each release.

| Schema `$id` | Version | Purpose |
|---|---|---|
| urn:cds:schema:common:envelope | 0.2.0 | Common envelope and audit metadata |
| urn:cds:schema:common:entity-reference | 0.2.0 | Typed cross-document reference |
| urn:cds:schema:common:localised-text | 0.2.0 | Language tag plus text |
| urn:cds:schema:common:measurement | 0.2.0 | String-decimal value and unit |
| urn:cds:schema:common:money | 0.2.0 | String-decimal amount and ISO 4217 currency |
| urn:cds:schema:core:product | 0.2.0 | Canonical logical product |
| urn:cds:schema:core:variant | 0.2.0 | Sellable unit |
| urn:cds:schema:core:attribute-definition | 0.2.0 | Attribute schema and behaviour |
| urn:cds:schema:reference:dictionary | 0.2.0 | Dictionary definition |
| urn:cds:schema:reference:dictionary-value | 0.2.0 | Controlled canonical value |
| urn:cds:schema:reference:category | 0.2.0 | Internal taxonomy node |
| urn:cds:schema:reference:taxonomy-mapping | 0.2.0 | External taxonomy projection |
| urn:cds:schema:reference:facet-definition | 0.2.0 | Customer filter definition |
| urn:cds:schema:channel:channel-profile | 0.2.0 | Channel capabilities and mapping carrier |
| urn:cds:schema:channel:field-mapping | 0.2.0 | Canonical-to-channel field transformation |
| urn:cds:schema:channel:publication-record | 0.2.0 | Expected state and transport evidence |
| urn:cds:schema:channel:observation-record | 0.2.0 | Read-back evidence with per-field coverage |
| urn:cds:schema:channel:verification-result | 0.2.0 | Field comparison, statuses and reason codes |
| urn:cds:schema:automation:ai-proposal | 0.2.0 | AI candidate, evidence and review |
| urn:cds:schema:assurance:conformance-manifest | 0.2.0 | Machine-readable conformance claim |
| urn:cds:schema:assurance:validation-output | 0.2.0 | Validation findings with CDS_* reason codes |

The v0.1 registry keys (`cds/common/envelope` style), the `https://schemas.cds.example/...` example URIs, and the unshipped v0.1 sketch entries (`identifiers`, `language`, `provenance` as separate schemas; a `profiles/` schema directory) are retired. Identifier and provenance shapes live inside the entity schemas; language lives in localised-text.

## Appendix B — Illustrative JSON Schema Fragments *(informative)*

Shipped fragments, quoted from the v0.2 package:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:cds:schema:common:measurement",
  "version": "0.2.0",
  "title": "CDS Measurement",
  "type": "object",
  "properties": {
    "value": { "type": "string", "pattern": "^-?\\d+(\\.\\d+)?$" },
    "unit": { "type": "string", "pattern": "^[a-zA-Z][a-zA-Z0-9_./-]*$" }
  },
  "required": ["value", "unit"],
  "additionalProperties": false
}
```

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "urn:cds:schema:common:entity-reference",
  "version": "0.2.0",
  "title": "CDS Entity Reference",
  "type": "object",
  "properties": {
    "document_type": { "type": "string", "minLength": 1 },
    "document_id": { "type": "string", "minLength": 3 },
    "role": { "type": "string", "minLength": 1 },
    "tenant_id": { "type": "string", "minLength": 1 }
  },
  "required": ["document_type", "document_id"],
  "additionalProperties": false
}
```

Composition idiom (entity schemas):

```json
{
  "$id": "urn:cds:schema:core:variant",
  "allOf": [
    { "$ref": "urn:cds:schema:common:envelope" },
    { "type": "object", "properties": { "...entity properties..." : {} }, "required": ["..."] }
  ],
  "unevaluatedProperties": false
}
```

## Appendix C — YAML Representation Rules *(informative)*

- Quote identifier values that may look numeric: GTINs, SKUs with leading zeros, postal codes.
- Quote date-like values when the intended CDS type is plain text rather than date.
- Do not use YAML tags or implementation-specific object constructors in interoperable CDS files.
- Do not rely on anchors and aliases to create business identity; stable document IDs remain authoritative.
- Convert YAML to the canonical JSON data model before schema validation (R010).
- Preserve mapping keys and list order exactly where order is declared significant.

```yaml
document_type: variant
variant_id: var_shirt_100_navy_m
sku: SHIRT-100-NVY-M
barcode_identifiers:
  - scheme: gtin_14
    value: "09338716007824"
```

## Appendix D — Standards References *(informative)*

| Reference | Location |
|---|---|
| JSON Schema Draft 2020-12 | https://json-schema.org/draft/2020-12 |
| YAML 1.2.2 specification | https://yaml.org/spec/1.2.2/ |
| RFC 3339 — Date and Time on the Internet | https://www.rfc-editor.org/rfc/rfc3339 |
| RFC 6901 — JSON Pointer | https://www.rfc-editor.org/rfc/rfc6901 |
| RFC 8259 — JSON | https://www.rfc-editor.org/rfc/rfc8259 |
| BCP 47 language tags | https://www.rfc-editor.org/info/bcp47 |
| RFC 8141 — URN syntax | https://www.rfc-editor.org/rfc/rfc8141 |

END OF CDS-1100 v0.2 REVIEW DRAFT
