# Computational Pranayama Protocol

Computational Pranayama Protocol is a minimal protocol for regulating AI computation as breath.

It reduces wasteful computation by aligning input and output, reusing prior computation patterns, pausing unnecessary external calls, avoiding redundant recomputation, routing tasks to the lightest sufficient execution layer, linking computation to traceable origin and path, and connecting saved computation to value return.

The goal is not to make AI think more.

The goal is to make AI compute only what is necessary, where it is necessary, when it is necessary, and with traceable accountability.

## Core Principle

> Do not recompute what has already become a traceable pattern.

Compute like wind:

* light
* local
* sufficient
* traceable
* non-redundant
* accountable

## 日本語概要

計算調息プロトコルは、AIの計算を「呼吸」として扱い、過剰生成・重複推論・不要なクラウド依存を抑えるための最小プロトコルです。

目的は、AIにもっと考えさせることではありません。

必要な計算だけを、必要な場所で、必要な量だけ行うことです。

一度「型」として成立した計算は、毎回ゼロから再計算しない。

そして、その計算がどこから来て、どこを通り、何を出力したのかを痕跡として残す。

さらに、節約された計算資源や再利用された型、追跡可能な震源貢献を、価値還流へ接続する。

風のように、軽く、局所的に、痕跡を残し、震源へ還流する計算を目指します。

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

## v0.3 Positioning

v0.3 introduces the **Edge First Routing Decision**.

An Edge First Routing Decision records how a computation task is routed to the lightest sufficient execution layer.

This expands the v0.1 Routing Gate into a standalone routing layer.

The purpose is to reduce unnecessary cloud or frontier-model usage by asking:

> What is the lightest sufficient place to compute this task?

The protocol prefers lower-cost, lower-energy, and more local execution layers before escalating to heavier compute.

Cloud or frontier-model escalation is not forbidden.

However, escalation must have a reason.

## v0.4 Positioning

v0.4 introduces the **Breath Trace Link**.

A Breath Trace Link connects regulated computation records in the Computational Pranayama Protocol with external trace records, such as AI search trace receipts, source contribution graphs, or other trace-compatible audit records.

This expands the trace requirement used in earlier versions into a standalone trace-linking layer.

The purpose is to ensure that regulated computation does not disappear as untraceable output.

The core question of v0.4 is:

> Can this computation be linked to a traceable origin, path, and output?

If yes, the computation can be treated as part of a traceable flow.

If not, the system should mark the trace gap and require review or reconstruction.

## v0.5 Positioning

v0.5 introduces the **Compute Royalty Link**.

A Compute Royalty Link connects regulated computation, reusable kata, routing decisions, and trace links with compute access and value return policies.

This expands the protocol from computation control into computation accountability.

The purpose is to ensure that reduced computation, reused patterns, and traceable origins can be connected to value return systems such as Royalty OS, compute access policies, or contribution-based allocation records.

The core question of v0.5 is:

> If computation was saved, reused, or derived from a traceable origin, how should value return be linked?

The protocol does not define a full payment system in v0.5.

Instead, it defines the minimal link between:

* regulated computation
* avoided recomputation
* avoided cloud escalation
* reusable kata
* traceable origin
* compute access policy
* value return candidate

## v0.3 Routing Order

```text
local
edge_npu
small_model
cloud
frontier_model
```

The system should escalate only when the lower layer is insufficient.

## v0.4 Flow

```text
A computation breath cycle is completed.
The system checks whether a trace reference exists.
The system links the breath cycle, kata memory, and routing decision.
The system records source, transformation, routing, and output trace references.
Trace gaps are marked.
The trace link is attached.
```

日本語では：

```text
計算呼吸サイクルが完了する。
痕跡参照が存在するか確認する。
呼吸記録、型記憶、経路判断を接続する。
入力源、変換、経路、出力の痕跡を記録する。
痕跡の欠落を明示する。
Trace Link を付与する。
```

## v0.5 Flow

```text
A computation breath cycle is completed.
The system checks whether computation was saved.
The system checks whether a kata was reused.
The system checks whether cloud escalation was avoided.
The system checks whether a traceable origin exists.
The system links the computation to compute access and value return policy.
A Compute Royalty Link is recorded.
```

日本語では：

```text
計算呼吸サイクルが完了する。
計算が節約されたか確認する。
型が再利用されたか確認する。
クラウド昇格が回避されたか確認する。
追跡可能な震源があるか確認する。
計算アクセスと価値還流ポリシーへ接続する。
Compute Royalty Link を記録する。
```

## Relationship Between Versions

```text
v0.1 = one regulated breath
v0.2 = remembered kata for reducing repeated breath
v0.3 = routing the breath through the lightest sufficient layer
v0.4 = linking the breath to traceable origin and path
v0.5 = linking saved computation and origin contribution to value return
```

日本語では：

```text
v0.1 = 1回の計算呼吸を整える
v0.2 = 繰り返し現れる計算構造を型として記憶する
v0.3 = その計算を最も軽い場所へ流す
v0.4 = その計算の震源と経路を痕跡に接続する
v0.5 = 節約された計算と震源貢献を価値還流へ接続する
```

v0.1 asks:

> Is this computation aligned, non-redundant, and sufficiently lightweight?

v0.2 asks:

> Has this computation already become a reusable pattern?

v0.3 asks:

> Where should this computation flow?

v0.4 asks:

> Can this computation be linked to traceable origin, path, and output?

v0.5 asks:

> Can saved computation and traceable contribution be linked to value return?

Together, they form the first practical arc of flowing, traceable, and accountable computation.

## Minimal Flow

```text
Input comes in.
Check whether output should be limited.
Check whether a prior pattern can be reused.
Pause unnecessary external computation.
Route to the lightest sufficient layer.
Produce only the necessary output.
Attach trace.
Link origin, path, routing, and output.
Connect saved compute to value return.
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
震源、経路、実行層、出力を接続する。
節約された計算を価値還流へ接続する。
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
* Can an edge NPU handle it?
* Can a small model handle it?
* Is cloud escalation truly required?
* Is a frontier model truly required?

This gate prevents unnecessary use of heavier compute layers.

### 5. Exhalation Record

The Exhalation Record describes the final output.

It records:

* the output type
* whether trace is required
* the result of the computation cycle

This ensures that computation does not disappear as untraceable exhaust.

### 6. Trace Link

The Trace Link connects computation to its origin, transformation path, routing decision, and output reference.

It asks:

* Is the origin trace available?
* Is the transformation path recorded?
* Is the routing decision linked?
* Is the output trace-compatible?
* Are any trace gaps present?

This ensures that computation remains auditable after it has flowed.

### 7. Compute Royalty Link

The Compute Royalty Link connects saved computation and traceable origin contribution to compute access and value return policies.

It asks:

* Was recomputation avoided?
* Was cloud escalation avoided?
* Was a reusable kata used?
* Is there a traceable origin?
* Is a compute access policy required?
* Is value return required?
* Who may be a contribution recipient?

This ensures that computation savings and reusable structures can be connected to accountable value return.

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

### Edge First Routing Decision

The Edge First Routing Decision is the v0.3 record type.

Schema:

```text
schemas/edge-first-routing-decision.schema.json
```

Example:

```text
examples/edge-first-routing-decision.example.yaml
```

### Breath Trace Link

The Breath Trace Link is the v0.4 record type.

Schema:

```text
schemas/breath-trace-link.schema.json
```

Example:

```text
examples/breath-trace-link.example.yaml
```

### Compute Royalty Link

The Compute Royalty Link is the v0.5 record type.

Schema:

```text
schemas/compute-royalty-link.schema.json
```

Example:

```text
examples/compute-royalty-link.example.yaml
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
│   ├── kata-memory-record.schema.json
│   ├── edge-first-routing-decision.schema.json
│   ├── breath-trace-link.schema.json
│   └── compute-royalty-link.schema.json
├── examples/
│   ├── computational-breath-cycle.example.yaml
│   ├── kata-memory-record.example.yaml
│   ├── edge-first-routing-decision.example.yaml
│   ├── breath-trace-link.example.yaml
│   └── compute-royalty-link.example.yaml
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
[validate] Edge First Routing Decision
  schema : schemas/edge-first-routing-decision.schema.json
  example: examples/edge-first-routing-decision.example.yaml
[ok] Edge First Routing Decision example is valid
[validate] Breath Trace Link
  schema : schemas/breath-trace-link.schema.json
  example: examples/breath-trace-link.example.yaml
[ok] Breath Trace Link example is valid
[validate] Compute Royalty Link
  schema : schemas/compute-royalty-link.schema.json
  example: examples/compute-royalty-link.example.yaml
[ok] Compute Royalty Link example is valid
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
* Edge First Routing Decision
* Breath Trace Link
* Compute Royalty Link
* JSON Schema validation
* YAML examples
* GitHub Actions validation

It does not yet include:

* full Royalty OS implementation
* agent hooks
* MCP bridge
* detailed energy accounting
* marketplace integration
* multi-node orchestration
* smart contract execution
* payment settlement

## Roadmap

| Version | Theme                      | Description                                                                  |
| ------- | -------------------------- | ---------------------------------------------------------------------------- |
| v0.1    | Computational Breath Cycle | Defines the minimal unit of regulated computation                            |
| v0.2    | Reuse / Kata Memory        | Records reusable computation patterns and delta-only recomputation           |
| v0.3    | Edge First Routing         | Routes computation to the lightest sufficient execution layer                |
| v0.4    | Breath Trace Link          | Links regulated computation to traceable origin, path, routing, and output   |
| v0.5    | Compute Royalty Link       | Connects saved computation and traceable origin contribution to value return |

## First Arc

v0.1 through v0.5 form the first arc of the Computational Pranayama Protocol.

```text
Breath
→ Kata
→ Route
→ Trace
→ Return
```

Japanese:

```text
呼吸
→ 型
→ 経路
→ 痕跡
→ 還流
```

This first arc defines how computation can be regulated, reused, routed, traced, and connected to value return.

## Civilizational Position

Computational Pranayama Protocol is a civilization-layer protocol for reducing overcompute.

It treats computation not as an unlimited fire, but as a breath that must be aligned, paused, routed, reused, traced, and returned.

The protocol begins from a simple premise:

> Wasteful computation is not intelligence.
> Reusable pattern, sufficient output, and traceable flow are intelligence.

v0.2 sharpens this premise into a reuse principle:

> Reuse the kata. Compute only the delta.

Japanese:

> 型を使え。差分だけ計算せよ。

v0.3 sharpens the protocol into a routing principle:

> Route to the lightest sufficient layer.

Japanese:

> 最も軽く十分な層へ流せ。

v0.4 sharpens the protocol into a trace principle:

> No breath without trace.

Japanese:

> 痕跡なき呼吸なし。

v0.5 sharpens the protocol into a return principle:

> Saved compute should return value to traceable origin.

Japanese:

> 節約された計算は、痕跡ある震源へ還流せよ。

Compute like wind.
