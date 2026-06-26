import json
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator


ROOT = Path(__file__).resolve().parents[1]

VALIDATIONS = [
    {
        "name": "Computational Breath Cycle",
        "schema": ROOT / "schemas" / "computational-breath-cycle.schema.json",
        "example": ROOT / "examples" / "computational-breath-cycle.example.yaml",
    },
    {
        "name": "Kata Memory Record",
        "schema": ROOT / "schemas" / "kata-memory-record.schema.json",
        "example": ROOT / "examples" / "kata-memory-record.example.yaml",
    },
    {
        "name": "Edge First Routing Decision",
        "schema": ROOT / "schemas" / "edge-first-routing-decision.schema.json",
        "example": ROOT / "examples" / "edge-first-routing-decision.example.yaml",
    },
    {
        "name": "Breath Trace Link",
        "schema": ROOT / "schemas" / "breath-trace-link.schema.json",
        "example": ROOT / "examples" / "breath-trace-link.example.yaml",
    },
    {
        "name": "Compute Royalty Link",
        "schema": ROOT / "schemas" / "compute-royalty-link.schema.json",
        "example": ROOT / "examples" / "compute-royalty-link.example.yaml",
    },
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return yaml.safe_load(file)


def validate_item(name: str, schema_path: Path, example_path: Path) -> None:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda error: error.path)

    if errors:
        print(f"[error] {name} validation failed")

        for error in errors:
            path = ".".join(str(part) for part in error.path) or "<root>"
            print(f"  - path: {path}")
            print(f"    message: {error.message}")

        raise SystemExit(1)

    print(f"[ok] {name} example is valid")


def main() -> None:
    for item in VALIDATIONS:
        validate_item(
            name=item["name"],
            schema_path=item["schema"],
            example_path=item["example"],
        )


if __name__ == "__main__":
    main()

