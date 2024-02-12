"""
This file defines the API of the datatypes module. The datatypes module is
responsible for defining the data types that are used in the application.

author: @electricalgorithm
"""

from .languages import DocsLanguage, CodeLanguage
from .file_containers import CodeFileContainer, CodeDirectoryContainer

__all__ = [
    "DocsLanguage",
    "CodeLanguage",
    "CodeFileContainer",
    "CodeDirectoryContainer",
]