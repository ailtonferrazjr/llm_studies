from utils.web.crawler import Website
from services.ollama.ollama import Ollama, Prompt


class SummarizerWithOllama():
    
    def __init__(self, website: Website):
        self.title = website.title
        self.text = website.text
        self.ollama = Ollama()

    def main(self):
        self.run_summary()

    def run_summary(self):
        self.prompt = Prompt(user_content=self.get_user_prompt(), system_content=self.get_system_prompt())
        self.ollama.make_request(prompt=self.prompt)

    def get_user_prompt(self):
        user_prompt = f"Website title: {self.title}\n\n"
        user_prompt += f"Website content: {self.text}"
        return user_prompt
    
    def get_system_prompt(self):
        return "You are an expert in summaryizing websites. You will receive a website title and text content and you will need to return a markdown text with the summary of it."
        
    
if __name__ == "__main__":
    web = Website("https://www.hltv.org/")
    summ = SummarizerWithOllama(website=web)
    summ.main()
