"""Copy the canonical repository corpus into the built Python package."""
from pathlib import Path
import shutil

ROOT_FILES = ["README.md", "SKILL.md", "AGENTS.md", "ALL_IN_ONE.md"]
CORPUS_DIRS = ["references", "data", "schemas", "templates", "examples"]

def copy_corpus(root: str | Path, build_lib: str | Path) -> Path:
    root = Path(root)
    corpus = Path(build_lib) / "viral_shorts" / "corpus"
    shutil.rmtree(corpus, ignore_errors=True)
    corpus.mkdir(parents=True, exist_ok=True)
    for name in ROOT_FILES:
        shutil.copy2(root / name, corpus / name)
    for name in CORPUS_DIRS:
        shutil.copytree(root / name, corpus / name, dirs_exist_ok=True)
    return corpus
