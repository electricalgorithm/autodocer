"""This is the main script to use Autodocer."""

from core.autodocer import Autodocer
from core.models import LLaMa2Model, CodeLLaMaModel
from core.datatypes import DocsLanguage


if __name__ == "__main__":
    HOST: str = "localhost"
    PORT: int = 11434

    # Create an instance of Autodocer.
    autodocer = Autodocer()

    # Use LLAMA2 to generate documentation for the test_file_llama.py file.
    autodocer.set_model(LLaMa2Model(HOST, PORT))
    autodocer.set_documentation_language(DocsLanguage.EN)
    autodocer.add_file("test_file_llama.py")
    autodocer.apply_documentations()

    # Use CodeLLaMa to generate documentation for the test_file_codellama.py file.
    autodocer.set_model(CodeLLaMaModel(HOST, PORT))
    autodocer.set_documentation_language(DocsLanguage.EN)
    autodocer.add_file("test_file_codellama.py")
    autodocer.apply_documentations()
    