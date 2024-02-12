"""
This module defines the ollama adaptor. The adaptor is responsible for
sending and recieving request to ollama server.

author: @electricalgorithm
"""
import json
import requests
from typing import Any, Optional
from dataclasses import dataclass

@dataclass
class OllamaRequest:
    """
    This class represents the request to the ollama server. It contains
    the model name, the prompt, and the extra configuration.
    """
    model: str
    """The name of the model."""
    prompt: str
    """The prompt for the model."""
    extra_config: Optional[dict[str, Any]] = None
    """The extra configuration for the model."""

@dataclass
class OllamaResponse:
    """
    This class represents the response from the ollama server. It contains
    the model name, the prompt, the extra configuration, and the generated
    documentation.
    """
    model: str
    """The name of the model."""
    created_at: str
    """The time when the response is created."""
    response: str
    """The response from the model."""
    done: bool
    """Whether the response is done."""
    context: list[int]
    """The context of the response."""
    total_duration: int
    """The total duration of the response."""
    load_duration: int
    """The load duration of the response."""
    prompt_eval_count: int
    """The prompt evaluation count of the response."""
    prompt_eval_duration: int
    """The prompt evaluation duration of the response."""
    eval_count: int
    """The evaluation count of the response."""
    eval_duration: int
    """The evaluation duration of the response."""


class OllamaAdaptor:
    """
    This class implements the ollama adaptor. It is responsible for sending
    and recieving request to ollama server.
    """
    DEFAULT_SERVER_HOST = "localhost"
    DEFAULT_SERVER_PORT = 11434
    DEFAULT_API_ENDPOINT = "/api/generate"

    def __init__(self,
                 server_host: str = DEFAULT_SERVER_HOST,
                 server_port: int = DEFAULT_SERVER_PORT,
                 server_endpoint: str = DEFAULT_API_ENDPOINT
                 ) -> None:
        """
        Initializes the ollama adaptor.
        :param server_host: The host of the ollama server.
        :param server_port: The port of the ollama server.
        :param server_endpoint: The endpoint API of the ollama server's
        generate function.
        """
        self._host = server_host
        self._port = server_port
        self._api_endpoint = server_endpoint

    def send_request(self, request: OllamaRequest) -> OllamaResponse:
        """It sends a request to the ollama server and returns the response.
        :param request: The request to send to the ollama server.
        :return: The response from the ollama server.
        """
        # Construct the URL.
        url = f"http://{self._host}:{self._port}{self._api_endpoint}"
        # Add stream = false to extra_config.
        if request.extra_config is None:
            request.extra_config = {}
        request.extra_config["stream"] = False

        # Send the request.
        json_request = self._request_to_json(request)
        response = requests.post(url, data=json_request)
        
        # Return the response.
        return self._json_to_response(response.text)
    
    def _request_to_json(self, request: OllamaRequest) -> str:
        """Converts the request to a json object.
        :param request: The request to convert to json.
        :return: The JSON string of the request.
        """
        # Convert the request to a dictionary.
        request_dict: dict[str, Any] = {
            "model": request.model,
            "prompt": request.prompt
        }
        if request.extra_config is not None:
            for key, value in request.extra_config.items():
                request_dict[key] = value
        
        # Return the JSON string.
        return json.dumps(request_dict)
    
    def _json_to_response(self, json_response: str) -> OllamaResponse:
        """Converts the JSON response to a response object.
        :param json_response: The json response to convert.
        :return: The response object.
        """
        response_dict = json.loads(json_response)
        return OllamaResponse(**response_dict)