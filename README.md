# Computational Pranayama Protocol

Computational Pranayama Protocol is a minimal protocol for regulating AI computation as breath.

It reduces wasteful computation by aligning input and output, reusing prior computation patterns, pausing unnecessary external calls, avoiding redundant recomputation, and routing tasks to the lightest sufficient execution layer.

The goal is not to make AI think more.

The goal is to make AI compute only what is necessary, where it is necessary, when it is necessary.

## Core Principle

> Do not recompute what has already become a traceable pattern.

Compute like wind:

* light
* local
* sufficient
* traceable
* non-redundant

## 日本語概要

計算調息プロトコルは、AIの計算を「呼吸」として扱い、過剰生成・重複推論・不要なクラウド依存を抑えるための最小プロトコルです。

目的は、AIにもっと考えさせることではありません。

必要な計算だけを、必要な場所で、必要な量だけ行うことです。

一度「型」として成立した計算は、毎回ゼロから再計算しない。

風のように、軽く、局所的に、痕跡を残しながら流れる計算を目指します。

## v0.1 Positioning

v0.1 defines the **Computational Breath Cycle**.

A Computational Breath Cycle is the smallest recordable unit of regulated AI computation.

It represents one cycle of:

1. receiving input
2. checking output balance
3. reusing prior patterns
4. pausing unnecessary external computation
5. routing to the lightest sufficient execution layer
6. producing only the necessary output
7. attaching trace

In this version, the protocol does not attempt to control all AI infrastructure.

Instead, it defines a minimal structure for observing and validating whether a single act of computation is aligned, non-redundant, and sufficiently lightweight.

## Minimal Flow

```text
Input comes in.
Check whether output should be limited.
Check whether a prior pattern can be reused.
Pause unnecessary external computation.
Route to the lightest sufficient layer.
Produce only the necessary output.
Attach trace.
```

日本語では：

```text
入力を吸う。
吐きすぎを抑える。
過去の型を探す。
不要な外部計算を止める。
最も軽い場所へ流す。
必要な分だけ出す。
痕跡を残す。
```

## Core Gates

### 1. Alignment Gate

The Alignment Gate checks whether the output volume is appropriate for the input.

It asks:

* Is the input fresh enough?
* Is the output minimal and sufficient?
* Is there a risk of overgeneration?

This gate prevents unnecessary expansion of generated content.

### 2. Reuse Gate

The Reuse Gate checks whether a prior computation pattern can be reused.

It asks:

* Has a similar pattern already been computed?
* Can the existing structure be reused with only a delta update?
* Is full recomputation actually required?

This gate prevents redundant reasoning.

### 3. Kumbhaka Gate

The Kumbhaka Gate pauses unnecessary external computation.

It asks:

* Can the system reuse internal trace?
* Can the system avoid an external call?
* Can recomputation be suppressed?

This gate introduces a reflective pause before escalation.

### 4. Routing Gate

The Routing Gate selects the lightest sufficient execution layer.

It asks:

* Can this task run locally?
* Can a small model handle it?
* Is cloud escalation truly required?

This gate prevents unnecessary use of heavier compute layers.

### 5. Exhalation Record

The Exhalation Record describes the final output.

It records:

* the output type
* whether trace is required
* the result of the computation cycle

This ensures that computation does not disappear as untraceable exhaust.

## Repository Structure

```text
computational-pranayama-protocol/
├── README.md
├── CHANGELOG.md
├── schemas/
│   └── computational-breath-cycle.schema.json
├── examples/
│   └── computational-breath-cycle.example.yaml
└── scripts/
    └── validate_examples.py
```

## Schema

The v0.1 schema is located at:

```text
schemas/computational-breath-cycle.schema.json
```

It defines the required structure for a Computational Breath Cycle record.

## Example

The v0.1 example is located at:

```text
examples/computational-breath-cycle.example.yaml
```

It demonstrates a minimal valid breath cycle with alignment, reuse, kumbhaka, routing, and exhalation records.

## Validation

Run:

```bash
python scripts/validate_examples.py
```

Expected result:

```text
[validate] Computational Breath Cycle
  schema : schemas/computational-breath-cycle.schema.json
  example: examples/computational-breath-cycle.example.yaml
[ok] Computational Breath Cycle example is valid
```

## v0.1 Scope

v0.1 includes:

* Computational Breath Cycle definition
* Alignment Gate
* Reuse Gate
* Kumbhaka Gate
* Routing Gate
* Exhalation Record
* JSON Schema validation
* YAML example

v0.1 does not yet include:

* Royalty OS integration
* Agent hooks
* MCP bridge
* detailed energy accounting
* marketplace integration
* multi-node orchestration

## Roadmap

| Version | Theme                      | Description                                                                |
| ------- | -------------------------- | -------------------------------------------------------------------------- |
| v0.1    | Computational Breath Cycle | Defines the minimal unit of regulated computation                          |
| v0.2    | Reuse / Kata Memory        | Expands reusable pattern records and recomputation control                 |
| v0.3    | Edge First Routing         | Adds lightweight execution routing and Local First policies                |
| v0.4    | Trace Integration          | Links breath cycles with AI Search Trace Receipt records                   |
| v0.5    | Compute / Royalty Link     | Connects computation control with value return and compute access policies |

## Civilizational Position

Computational Pranayama Protocol is a civilization-layer protocol for reducing overcompute.

It treats computation not as an unlimited fire, but as a breath that must be aligned, paused, routed, and traced.

The protocol begins from a simple premise:

> Wasteful computation is not intelligence.
> Reusable pattern, sufficient output, and traceable flow are intelligence.

Compute like wind.
