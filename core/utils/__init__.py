"""
This file defines the API for the autodocer utilities.
    - The OllamaAdaptor class is used to adapt the Ollama server to the autodocer.
    - The get_logger() function is used to get a logger for the autodocer.

author: @electricalgorithm 
"""

from .logger import get_logger
from .ollama_adaptor import OllamaAdaptor, OllamaRequest, OllamaResponse
from .file_operations import (
    get_absolute_path,
    check_file_exists,
    get_file_extension,
    read_file,
    save_file
)

__all__ = [
    "check_file_exists",
    "get_logger",
    "get_absolute_path",
    "get_file_extension",
    "read_file",
    "save_file",
    "OllamaAdaptor",
    "OllamaRequest",
    "OllamaResponse"
]
