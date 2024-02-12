"""
This module defines the data types for the possible
languages that the user can use to write the documentation
and select the code from.

author: @electricalgorithm
"""
from enum import Enum, unique
from typing import Any

@unique
class DocsLanguage(Enum):
    """The possible languages for the documentation."""
    EN = "english"
    TR = "turkish"
    PL = "polish"

@unique
class CodeLanguage(Enum):
    """The possible languages for the code."""
    PYTHON = "python"
    CPP = "c++"
    JAVASCRIPT = "javascript"
    RUST = "rust"

    @classmethod
    def from_extension(cls, extension: str) -> 'CodeLanguage':
        """Return the CodeLanguage enumeration using the extension
        of the code file.
        :param extension: The extension of the code file.
        :returns: The CodeLanguage enumeration.
        """
        _converter: dict[str, Any] = {
            "py": cls.PYTHON,
            "cpp": cls.CPP,
            "js": cls.JAVASCRIPT,
            "rs": cls.RUST,
        }

        # Return the corresponding enumeration value.
        try:
            return _converter[extension.lower()]
        except KeyError as exception:
            raise ValueError("The given extension is not recognized.") from exception