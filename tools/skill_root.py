"""Locate the skill corpus in a source checkout or an installed package."""
import os

def skill_root() -> str:
    override = os.environ.get("VIRAL_SHORTS_ROOT")
    if override:
        return os.path.abspath(override)
    here = os.path.dirname(os.path.abspath(__file__))
    checkout = os.path.dirname(here)
    if os.path.isfile(os.path.join(checkout, "SKILL.md")):
        return os.path.abspath(checkout)
    packaged = os.path.join(here, "corpus")
    if os.path.isfile(os.path.join(packaged, "SKILL.md")):
        return os.path.abspath(packaged)
    return os.path.abspath(checkout)
