# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol formation.

## v0.3.0-candidate

Third candidate release of the Computational Pranayama Protocol.

This release introduces the **Edge First Routing Decision**, a routing record for selecting the lightest sufficient execution layer.

The v0.3 scope expands the v0.1 Routing Gate into a standalone execution-routing layer.

Where v0.1 defines one regulated breath and v0.2 defines a reusable kata, v0.3 defines where the computation should flow.

### Added

* Added `Edge First Routing Decision` as the third core record type.
* Added schema for `edge-first-routing-decision`.
* Added YAML example for a valid edge-first routing decision.
* Expanded the v0.1 Routing Gate into a standalone routing layer.
* Added `task` fields for describing routing target, privacy sensitivity, and compute intensity.
* Added `available_layers` records for local, edge NPU, small model, cloud, and frontier model availability.
* Added `routing_assessment` fields for local sufficiency, kata availability, latency tolerance, cloud need, and frontier need.
* Added `selected_layer` record for final execution-layer selection.
* Added `cloud_escalation_policy` for controlling when cloud escalation is allowed.
* Added `fallback_policy` for defining fallback execution order.
* Added `trace` fields for routing trace requirement and reference.
* Updated validation script to validate v0.1, v0.2, and v0.3 examples.

### Validation

The v0.3 schema and example passed validation.

Expected validation output:

```text
[validate] Computational Breath Cycle
  schema : schemas/computational-breath-cycle.schema.json
  example: examples/computational-breath-cycle.example.yaml
[ok] Computational Breath Cycle example is valid
[validate] Kata Memory Record
  schema : schemas/kata-memory-record.schema.json
  example: examples/kata-memory-record.example.yaml
[ok] Kata Memory Record example is valid
[validate] Edge First Routing Decision
  schema : schemas/edge-first-routing-decision.schema.json
  example: examples/edge-first-routing-decision.example.yaml
[ok] Edge First Routing Decision example is valid
```

### Core Principle

> Route to the lightest sufficient layer.

### Japanese Core Principle

> 最も軽く十分な層へ流せ。

### Positioning

v0.3 turns computation control into routing control.

The protocol no longer only asks whether a computation should be regulated or reused.

It now asks where the computation should flow.

This is the first step toward Local First and Edge First computation inside the Computational Pranayama Protocol.

## v0.2.0-candidate

Second candidate release of the Computational Pranayama Protocol.

This release introduces the **Kata Memory Record**, a reusable computation pattern record for reducing redundant recomputation.

The v0.2 scope expands the v0.1 Reuse Gate into a standalone reusable pattern layer.

Where v0.1 defines one regulated breath, v0.2 defines a remembered kata that can be reused across future breath cycles.

### Added

* Added `Kata Memory Record` as the second core record type.
* Added schema for `kata-memory-record`.
* Added YAML example for a valid kata memory record.
* Expanded the v0.1 Reuse Gate into a standalone reusable pattern layer.
* Added `source` fields for linking a kata to its originating breath cycle and task type.
* Added `kata` fields for name, description, pattern type, reusable parts, non-reusable parts, and stability.
* Added `reuse_policy` fields for reuse permission, reuse mode, and minimum similarity score.
* Added `delta_policy` fields for delta-only computation.
* Added `recompute_policy` fields for defining when full recomputation is allowed.
* Added `verification` fields for verification requirements and scope.
* Added `trace` fields for trace requirement and trace reference.
* Updated validation script to validate both v0.1 and v0.2 examples.

### Validation

The v0.2 schema and example passed validation.

Expected validation output:

```text
[validate] Computational Breath Cycle
  schema : schemas/computational-breath-cycle.schema.json
  example: examples/computational-breath-cycle.example.yaml
[ok] Computational Breath Cycle example is valid
[validate] Kata Memory Record
  schema : schemas/kata-memory-record.schema.json
  example: examples/kata-memory-record.example.yaml
[ok] Kata Memory Record example is valid
```

### Core Principle

> Reuse the kata. Compute only the delta.

### Japanese Core Principle

> 型を使え。差分だけ計算せよ。

### Positioning

v0.2 turns repeated computation into reusable structure.

The protocol no longer only asks whether computation should be regulated.

It now asks whether the computation has already become a traceable pattern that should be reused instead of recomputed.

This is the first step from regulated computation toward remembered computation.

## v0.1.0-candidate

Initial candidate release of the Computational Pranayama Protocol.

This release defines the first minimal breath unit of the protocol: the **Computational Breath Cycle**.

The v0.1 scope is intentionally small. It focuses on recording and validating a single act of regulated computation through alignment, reuse, kumbhaka, routing, and exhalation.

### Added

* Defined computation as a regulated breath cycle.
* Added `Computational Breath Cycle` as the first core record type.
* Added `Alignment Gate` for balancing input freshness, output volume, and overgeneration risk.
* Added `Reuse Gate` for avoiding redundant recomputation.
* Added `Kumbhaka Gate` for pausing unnecessary external access and suppressing wasteful recomputation.
* Added `Routing Gate` for selecting the lightest sufficient execution layer.
* Added `Exhalation Record` for describing output type, trace requirement, and result.
* Added JSON Schema for `computational-breath-cycle`.
* Added YAML example for a valid computational breath cycle.
* Added Python validation script.
* Added GitHub Actions workflow for validating examples on push and pull request.

### Validation

The v0.1 schema and example passed validation.

Expected validation output:

```text
[validate] Computational Breath Cycle
  schema : schemas/computational-breath-cycle.schema.json
  example: examples/computational-breath-cycle.example.yaml
[ok] Computational Breath Cycle example is valid
```

### Core Principle

> Do not recompute what has already become a traceable pattern.

### Japanese Core Principle

> 痕跡ある型となったものを、二度ゼロから考えるな。

### Design Notes

v0.1 intentionally avoids expanding into large infrastructure control.

It does not yet include:

* Royalty OS integration
* Agent hooks
* MCP bridge
* detailed energy accounting
* marketplace integration
* multi-node orchestration

These may be introduced in later versions after the minimal breath cycle is stable.

### Positioning

v0.1 establishes Computational Pranayama Protocol as a minimal protocol for flowing computation.

The aim is not to maximize computation.

The aim is to reduce wasteful computation by making AI compute only what is necessary, where it is necessary, when it is necessary.

Compute like wind.
