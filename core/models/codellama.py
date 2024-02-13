"""
This module implements the LLaMa2 model. It uses the interface defined in
core/models/interface.py to implement the model. The model generates
documentation for code using the LLaMa2 AI model.

author: @electricalgorithm
"""

from core.models.base import ModelBase
from core.datatypes import DocsLanguage, CodeLanguage


class CodeLLaMaModel(ModelBase):
    """
    This class implements the CodeLLaMa model. It generates documentation for code
    using the CodeLLaMa AI model.
    """

    @property
    def model_name(self) -> str:
        """Returns the name of the model. It is used
        to identify the model in the server.
        :return: The name of the model.
        """
        return "codellama"

    @property
    def allowed_code_languages(self) -> list[CodeLanguage]:
        """Returns the list of allowed code languages for the model.
        The get_prompt method must control the languages that are allowed.
        :return: The list of allowed code languages for the model.
        """
        return [CodeLanguage.PYTHON,
                CodeLanguage.RUST,
                CodeLanguage.JAVASCRIPT,
                CodeLanguage.CPP]

    @property
    def allowed_docs_languages(self) -> list[DocsLanguage]:
        """Returns the list of allowed documentation languages for the model.
        The get_prompt method must control the languages that are allowed.
        :return: The list of allowed documentation languages for the model.
        """
        return [DocsLanguage.EN]

    @property
    def prompt_file(self) -> str:
        """Returns the name of the prompt file for the model.
        :return: The name of the prompt file for the model.
        """
        return "llama2.txt"
