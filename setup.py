from pathlib import Path
import shutil
from setuptools import setup
from setuptools.command.build_py import build_py

ROOT_FILES = ["README.md", "SKILL.md", "AGENTS.md", "ALL_IN_ONE.md"]
CORPUS_DIRS = ["references", "data", "schemas", "templates", "examples"]

class BuildPyWithCorpus(build_py):
    def run(self):
        super().run()
        root = Path(__file__).resolve().parent
        corpus = Path(self.build_lib) / "viral_shorts" / "corpus"
        corpus.mkdir(parents=True, exist_ok=True)
        for name in ROOT_FILES:
            shutil.copy2(root / name, corpus / name)
        for name in CORPUS_DIRS:
            shutil.copytree(root / name, corpus / name, dirs_exist_ok=True)

setup(cmdclass={"build_py": BuildPyWithCorpus})
