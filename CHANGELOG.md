# Changelog

All notable changes to this project will be documented in this file.

This project follows a candidate-release style during early protocol formation.

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
