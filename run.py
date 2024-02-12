"""This is the main script to use Autodocer."""

from core.autodocer import Autodocer
from core.models import LLaMa2Model
from core.datatypes import DocsLanguage


if __name__ == "__main__":
    autodocer = Autodocer()
    autodocer.set_model(LLaMa2Model("localhost", 11434))
    autodocer.set_documentation_language(DocsLanguage.EN)

    autodocer.add_file("test_file.py")
    autodocer.apply_documentations()
    