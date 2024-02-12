"""
This module implements basic file operation functionality needed for
Autodecoder project.

author: @electricalgorithm
"""
import os

def get_absolute_path(relative_path: str) -> str:
    """Returns absolute path of a given relative path.
    :param relative_path: The relative path of a filesystem object.
    """
    return os.path.abspath(relative_path)

def check_file_exists(absolute_path: str) -> bool:
    """Returns True if the file in the given path exists.
    :param absolute_path: The file path to check.
    """
    return os.path.isfile(absolute_path)

def get_file_extension(absolute_path: str) -> str:
    """Returns the file extension of the given path.
    :param absolute_path: The file path to check.
    """
    return os.path.splitext(absolute_path)[1][1:]

def read_file(absolute_path: str) -> str:
    """Returns the file content of the given path.
    :param absolute_path: The file path to read."""
    with open(absolute_path, 'r') as file:
        return file.read()
    
def save_file(code_to_save: str,
              original_abs_path: str,
              ending_addition: str) -> str:
    """Saves the code into a new file.
    :param original_abs_path: The absolute path of the
    original file with its extension.
    :param ending_addition: The addition to the end of
    the original file name.
    :param extension: The extension of the original file.
    """
    # Split the file name from its directory location.
    dir_name, original_file_name = os.path.split(original_abs_path)
    
    # Remove the original extension from the file name.
    extension: str = get_file_extension(original_file_name)
    file_name: str = original_file_name[0:-(len(extension)+1)]

    # Create the new file name.
    new_file_name = f"{file_name}{ending_addition}.{extension}"
    
    # Create the new file path.
    new_file_path = os.path.join(dir_name, new_file_name)

    with open(new_file_path, 'w') as file:
        file.write(code_to_save)
    return new_file_path