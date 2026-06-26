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

## v0.2 Positioning

v0.2 introduces the **Kata Memory Record**.

A Kata Memory Record captures a reusable computation pattern that should not be recomputed from scratch once it has become stable and traceable.

This expands the v0.1 Reuse Gate into a standalone reusable pattern layer.

The purpose is to reduce redundant AI computation by storing reusable structures such as:

* protocol definition patterns
* release note patterns
* schema design patterns
* validation flow patterns
* reasoning templates
* output formatting patterns

The core question of v0.2 is:

> Has this computation already become a reusable kata?

If yes, the system should reuse the existing pattern and compute only the necessary delta.

## v0.2 Flow

```text
A computation pattern appears repeatedly.
The pattern becomes stable.
The pattern is recorded as a Kata Memory Record.
Future tasks check whether the kata applies.
If applicable, the system reuses the kata.
Only the delta is computed.
Trace is attached.
```

日本語では：

```text
同じ計算構造が何度も現れる。
その構造が安定する。
型記憶として記録する。
次回以降、その型が使えるか確認する。
使えるなら型を再利用する。
差分だけ計算する。
痕跡を残す。
```

## Relationship Between v0.1 and v0.2

```text
v0.1 = one regulated breath
v0.2 = remembered kata for reducing repeated breath
```

日本語では：

```text
v0.1 = 1回の計算呼吸を整える
v0.2 = 繰り返し現れる計算構造を型として記憶する
```

v0.1 asks:

> Is this computation aligned, non-redundant, and sufficiently lightweight?

v0.2 asks:

> Has this computation already become a reusable pattern?

Together, they form the first practical layer of flowing computation.

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

## Core Records

### Computational Breath Cycle

The Computational Breath Cycle is the v0.1 record type.

Schema:

```text
schemas/computational-breath-cycle.schema.json
```

Example:

```text
examples/computational-breath-cycle.example.yaml
```

### Kata Memory Record

The Kata Memory Record is the v0.2 record type.

Schema:

```text
schemas/kata-memory-record.schema.json
```

Example:

```text
examples/kata-memory-record.example.yaml
```

## Repository Structure

```text
computational-pranayama-protocol/
├── README.md
├── CHANGELOG.md
├── .github/
│   └── workflows/
│       └── validate.yml
├── schemas/
│   ├── computational-breath-cycle.schema.json
│   └── kata-memory-record.schema.json
├── examples/
│   ├── computational-breath-cycle.example.yaml
│   └── kata-memory-record.example.yaml
└── scripts/
    └── validate_examples.py
```

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
[validate] Kata Memory Record
  schema : schemas/kata-memory-record.schema.json
  example: examples/kata-memory-record.example.yaml
[ok] Kata Memory Record example is valid
```

## Current Scope

The current protocol includes:

* Computational Breath Cycle
* Alignment Gate
* Reuse Gate
* Kumbhaka Gate
* Routing Gate
* Exhalation Record
* Kata Memory Record
* JSON Schema validation
* YAML examples
* GitHub Actions validation

It does not yet include:

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
| v0.2    | Reuse / Kata Memory        | Records reusable computation patterns and delta-only recomputation         |
| v0.3    | Edge First Routing         | Adds lightweight execution routing and Local First policies                |
| v0.4    | Trace Integration          | Links breath cycles with AI Search Trace Receipt records                   |
| v0.5    | Compute / Royalty Link     | Connects computation control with value return and compute access policies |

## Civilizational Position

Computational Pranayama Protocol is a civilization-layer protocol for reducing overcompute.

It treats computation not as an unlimited fire, but as a breath that must be aligned, paused, routed, reused, and traced.

The protocol begins from a simple premise:

> Wasteful computation is not intelligence.
> Reusable pattern, sufficient output, and traceable flow are intelligence.

v0.2 sharpens this premise into a second principle:

> Reuse the kata. Compute only the delta.

Japanese:

> 型を使え。差分だけ計算せよ。

Compute like wind.
