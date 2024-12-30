# IMPORT PACKAGES
import os
from dotenv import load_dotenv
from services import OpenAI
from web_service import WebsiteParser


load_dotenv()

# CONSTANTS
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")
BROWSER_HEADERS: dict[str, str] = {
 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

class Summarizer():
    def __init__(self, url):
        self.url=url
        pass

    def main(self) -> None:
        self.parse_website()
        self.prepare_prompt()
        self.run_summary()

    def parse_website(self) -> None:
        self.parsed_website = WebsiteParser(self.url)

    def prepare_prompt(self) -> None:
        self.system_prompt: str = "You are an expert in summaryizing websites. You will receive a website title and text content and you will need to return a markdown text with the summary of it."
        self.user_prompt: str = self.get_user_prompt()

    def get_user_prompt(self) -> str:
        user_prompt = f"Website title: {self.parse_website.title}\n\n"
        user_prompt += f"Website content: {self.parse_website.text}"
        return user_prompt

    def run_summary(self) -> None:
        openai = OpenAI
        


