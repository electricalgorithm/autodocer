"""
This module defines the logger for the application. The logger is used to log
information, warnings, and errors to the console and to a file and stdout.

author: @electricalgorithm
"""

import logging
from logging.handlers import RotatingFileHandler
import sys
import os

class Logger:
    """
    This class is used to create a logger for the application. The logger
    logs information, warnings, and errors to the console and to a file.
    """
    DEFAULT_LOG_FILE = './.logs/autodocer.log'

    def __init__(self, name: str, level: int | str) -> None:
        """The constructor for the Logger class.
        :param name: The name of the logger.
        :param level: The level of the logger.
        """
        # Create directory if not exists.
        os.makedirs(os.path.dirname(self.DEFAULT_LOG_FILE), exist_ok=True)

        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)

        # Create handlers
        stream_handler = logging.StreamHandler(sys.stdout)
        file_handler = RotatingFileHandler(self.DEFAULT_LOG_FILE,
                                           maxBytes=50000,
                                           backupCount=3)

        # Set the level of handlers
        stream_handler.setLevel(logging.INFO)
        file_handler.setLevel(level)

        # Create formatters and add it to handlers
        # Set the formatting of the logger.
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )

        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)

        # Add handlers to the logger
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)

    def debug(self, msg, *args, **kwargs) -> None:
        self.logger.debug(msg, *args, **kwargs)

    def info(self, msg, *args, **kwargs) -> None:
        self.logger.info(msg, *args, **kwargs)

    def warning(self, msg, *args, **kwargs) -> None:
        self.logger.warning(msg, *args, **kwargs)

    def error(self, msg, *args, **kwargs) -> None:
        self.logger.error(msg, *args, **kwargs)

    def exception(self, msg, *args, **kwargs) -> None:
        self.logger.exception(msg, *args, **kwargs)


def get_logger(name: str, level: int | str = logging.DEBUG) -> 'Logger':
    """Get the logger instance.
    :param name: The name of the logger.
    :param level: The level of the logger.
    :return: The logger instance.
    """
    return Logger(name, level)