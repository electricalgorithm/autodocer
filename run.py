"""This is the main script to use Autodocer."""

from core.autodocer import Autodocer
from core.models import LLaMa2Model, CodeLLaMaModel
from core.datatypes import DocsLanguage


if __name__ == "__main__":
    HOST: str = "localhost"
    PORT: int = 11434

    # Create an instance of Autodocer.
    autodocer = Autodocer()
    
    # Set the model for the Autodocer.
    autodocer.set_model(LLaMa2Model(HOST, PORT))
    # autodocer.set_model(CodeLLaMaModel(HOST, PORT))
    
    # Set the documentation language for the Autodocer.
    autodocer.set_documentation_language(DocsLanguage.EN)
    
    # Add files to be documented.
    autodocer.add_file("examples/input.py")
    # autodocer.add_file("...")

    # Run the magic.
    autodocer.apply_documentations()
    