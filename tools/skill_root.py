"""Locate the skill corpus in a source checkout or an installed wheel."""
import os, sys

def skill_root() -> str:
    override = os.environ.get("VIRAL_SHORTS_ROOT")
    if override:
        return os.path.abspath(override)
    checkout = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if os.path.isfile(os.path.join(checkout, "SKILL.md")):
        return os.path.abspath(checkout)
    installed = os.path.join(sys.prefix, "viral-shorts-skill")
    if os.path.isfile(os.path.join(installed, "SKILL.md")):
        return os.path.abspath(installed)
    return os.path.abspath(checkout)
