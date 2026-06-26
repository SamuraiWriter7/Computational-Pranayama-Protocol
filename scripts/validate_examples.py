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
    }
]


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def load_yaml(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def validate_item(name: str, schema_path: Path, example_path: Path) -> None:
    print(f"[validate] {name}")
    print(f"  schema : {schema_path.relative_to(ROOT)}")
    print(f"  example: {example_path.relative_to(ROOT)}")

    schema = load_json(schema_path)
    example = load_yaml(example_path)

    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(example), key=lambda e: e.path)

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
        validate_item(item["name"], item["schema"], item["example"])


if __name__ == "__main__":
    main()
