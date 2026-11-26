from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).resolve().parent))
from setuptools import setup
from setuptools.command.build_py import build_py
from tools.build_corpus import copy_corpus

class BuildPyWithCorpus(build_py):
    def run(self):
        super().run()
        copy_corpus(Path(__file__).resolve().parent, self.build_lib)

setup(cmdclass={"build_py": BuildPyWithCorpus})
