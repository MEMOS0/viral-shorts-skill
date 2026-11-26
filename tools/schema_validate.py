"""JSON Schema validation for the machine-readable stage files.
usage: python schema_validate.py discovery|storyboard|package file.json"""
import json, os, sys
from skill_root import skill_root
from jsonschema import Draft202012Validator
def root():
    return skill_root()

def validate(kind, doc):
    if kind not in ("discovery", "storyboard", "package"): return [f"unknown schema kind {kind!r}"]
    schema = json.load(open(os.path.join(root(), "schemas", kind + ".schema.json"), encoding="utf-8"))
    out = []
    for e in sorted(Draft202012Validator(schema).iter_errors(doc), key=lambda x: list(x.absolute_path)):
        path = "/" + "/".join(str(x) for x in e.absolute_path)
        out.append((path if path != "/" else "") + ": " + e.message)
    return out

def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) != 2: print(__doc__); return 2
    errors = validate(argv[0], json.load(open(argv[1], encoding="utf-8")))
    for e in errors: print("ERROR", e)
    print("PASS" if not errors else f"FAIL ({len(errors)} errors)")
    return 1 if errors else 0
if __name__ == "__main__": raise SystemExit(main())
