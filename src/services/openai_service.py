# Load Imports
from typing import Iterable, Optional
from openai import OpenAI
from openai.types import ChatModel
from openai.types.chat import ChatCompletionMessageParam
from dataclasses import dataclass
from common.logger import get_logger
from config import OPENAI_KEY

# Load Logger
logger = get_logger("openai_service")

# Error Handling
class OpenAIError(Exception):
    """Custom exception for OpenAI-related errors"""
    def __init__(self):
        super().__init__(self)
        logger.error(f"There was an error in OpenAI Service: {self.args}")

# Default Settings
@dataclass
class DefaultConfig:
    model: ChatModel = "gpt-3.5-turbo"
    max_retries: int = 3
DEFAULTS = DefaultConfig()

# Open AI Client
class OpenAIClient:
    client: OpenAI

    def __init__(self) -> None:
        try:
            if not OPENAI_KEY:
                raise OpenAIError("OpenAI API key is not set!")
            self.client = OpenAI(api_key=OPENAI_KEY)
            logger.info("OpenAI Client Initialized Succesfully!")
            
        except Exception as e:
            raise OpenAIError(f"Failed to initialize OpenAI client: {str(e)}")

    def chat_request(
        self,
        messages: Iterable[ChatCompletionMessageParam],
        model: Optional[ChatModel] = None,
    ) -> Optional[str]:
        """
        Make a chat completion request to OpenAI.

        Args:
            messages: The messages to send OpenAI
            model: The model to use, defaults to 'gpt-3.5-turbo' if None

        Returns:
            The response content or None if no content

        Raises:
            OpenAIError: If the request fails or return no choices
        """

        # 1. Default parameter handling
        model_to_use = model or DEFAULTS.model

        try:
            response = self.client.chat.completions.create(
                model=model_to_use, 
                messages=messages
            )

            if not response.choices:
                raise OpenAIError("No response choices returned!")
            
            return response.choices[0].message.content
        
        except OpenAIError:
            raise
        except Exception as e:
            raise OpenAIError(f"Chat completion failed: {str(e)}") from e 

