# IMPORT PACKAGES
from services.openai_service import OpenAIClient
from services.web_service import WebsiteParser

class Summarizer():
    def __init__(self, url):
        self.url = url
        self.parsed_website = None  # Initialize the attribute here

    def main(self) -> None:
        self.parse_website()
        self.prepare_prompt()
        return self.run_summary()  # Return the summary

    def parse_website(self) -> None:
        self.parsed_website = WebsiteParser(self.url)

    def prepare_prompt(self) -> None:
        self.system_prompt: str = "You are an expert in summaryizing websites. You will receive a website title and text content and you will need to return a markdown text with the summary of it."
        self.user_prompt: str = self.get_user_prompt()

    def get_user_prompt(self) -> str:
        user_prompt = f"Website title: {self.parsed_website.title}\n\n"
        user_prompt += f"Website content: {self.parsed_website.text}"
        return user_prompt

    def run_summary(self) -> None:
        openai = OpenAIClient()
        return openai.chat_request([
            {"role": "system", "content": self.system_prompt}, 
            {"role": "user", "content": self.user_prompt}
        ])

if __name__ == "__main__":
    summ = Summarizer("https://www.globo.com")
    print(summ.main())
