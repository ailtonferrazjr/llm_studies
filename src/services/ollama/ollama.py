# src/services/ollama/ollama.py
import requests
from config import OLLAMA_API, LLAMA_MODEL
from typing import Literal

Roles = Literal["user", "system"]

class Prompt():
    def __init__(self, user_content: str, system_content: str):
        self.message = {}
        self.system = self.create_message(role="system", content=system_content)
        self.user = self.create_message(role="user", content=user_content)
        self.message = [self.system, self.user] 

    def create_message(self, role: Roles, content: str) -> dict[str, str]:
        return { "role": role, "content": content}
    
class Ollama():
    def __init__(self):
        self.url = OLLAMA_API
        self.model = LLAMA_MODEL
        self.header = { "Content-Type": "application/json"}

    def make_request(self, prompt: Prompt):
        payload = self.create_payload(prompt.message)
        response = requests.post(OLLAMA_API, json=payload, headers=self.header)
        
        try:
            response_json = response.json()
            result = response_json['message']['content']
            print(result)
            return result
        except Exception as e:
            print(f"Error type: {type(e)}")
            print(f"Error message: {str(e)}")

    def create_payload(self, messages: dict[str, str]):
        return {
            "model": self.model,
            "messages": messages,
            "stream": False
        }
                
if __name__ == "__main__":
    prompt = Prompt(
        system_content="You are an expert in AI and LLMs", 
        user_content="Describe some of the business applications of Generative AI"
    )
    ollama = Ollama()
    ollama.make_request(prompt)

