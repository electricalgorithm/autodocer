"""
This module implements the main Autodocer class. The Autodocer class is used to
generate documentation for code using the selected model. The class reads the given
file and generates documentation for the code in the file using the selected model.
The generated documentation with original code is written into a new file. 
"""

from typing import Optional
from core.datatypes import CodeFileContainer, CodeLanguage, DocsLanguage
from core.utils import (
    get_logger, get_absolute_path,
    check_file_exists, get_file_extension,
    read_file, save_file,
)
from core.models import ModelBase, ModelResponse


class Autodocer:
    """
    This class implements the Autodocer. It generates documentation for code using
    the selected model. The class reads the given file and generates documentation
    for the code in the file using the selected model. The generated documentation
    with original code is written into a new file.
    """
    _POST_FIX: str = "_doc"

    def __init__(self) -> None:
        """The constructor for the Autodocer."""
        # Runtime internal members
        self._model: Optional[ModelBase] = None
        self._files: list[CodeFileContainer] = []
        self._docslang: Optional[DocsLanguage] = None

        # Create a logger instance.
        self._logger = get_logger(__name__, "DEBUG")

    def set_model(self, model: ModelBase) -> None:
        """Selects the model for Autodocer functionality.
        :param model: A Modelbase model class.
        """
        self._model = model
        self._logger.info(f"The selected model is {model.model_name}.")

    def set_documentation_language(self,
                                   docs_language: DocsLanguage
                                   ) -> None:
        """Selects the language used to create documentations.
        :param docs_language: The DocsLanguage enumeration to
        generate documentions in.
        """
        self._docslang = docs_language
        self._logger.info(f"The selected docs language is {docs_language.value.upper()}.")

    def add_file(self, file_path: str) -> None:
        """Adds a file to be documented with AI model.
        :param file_path: The relative path of the file.
        """
        # Recieve absolute path from the relative path.
        abs_path: str = get_absolute_path(file_path)
        if not check_file_exists(abs_path):
            return RuntimeError("The given file does not exists.")

        # Find the programing language.
        file_ext: str = get_file_extension(abs_path)
        code_lang: CodeLanguage = CodeLanguage.from_extension(file_ext)

        # Save the file into the list to check.
        self._files.append(CodeFileContainer(
            path=abs_path,
            code_language=code_lang
        ))

    def add_directory(self, dir_path: str) -> None:
        """Adds a directory of files to be documented with AI model.
        :param dir_path: The relative path of the directory.
        """
        raise NotImplementedError

    def apply_documentations(self, name_appendix: str = _POST_FIX) -> None:
        """Applies the documentation magic into the files selected.
        :param name_appendix: The output files name endings. Default is _doc.
        """
        self._logger.info("The documentation magic is started.")
        for file_container in self._files:
            self._logger.info(f"Working on {file_container.path}...")
            code: str = read_file(file_container.path)
            response: ModelResponse = self._model.generate_response(
                code_language=file_container.code_language,
                docs_language=self._docslang,
                code=code
            )

            # Check if response length is bigger than original.
            if len(response.generated_file) <= len(code):
                self._logger.error("The AI response length is less "
                                   "than original code file length.")
                raise RuntimeError("The AI response length is less "
                                   "than original code file length.")
            self._logger.info("Model result is obtained.")

            # Save file.
            new_file: str =save_file(response.generated_file,
                                     file_container.path,
                                     name_appendix)
            self._logger.info(f"The file has saved as {new_file}.")
