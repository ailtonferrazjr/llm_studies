#Import Packages
from bs4 import BeautifulSoup
import requests
from typing import Union
from typing import NoReturn
from config import BROWSER_HEADERS

class WebsiteParser:
    """Object to fetch and parse website content"""
    url: str
    soup: BeautifulSoup
    title: str
    text: str

    def __init__(self, url: str) -> None:
        self.url = url
        self.soup = self.get_website_soup()
        self.parse_website_content()

    def get_website_soup(self) -> Union[BeautifulSoup,NoReturn]:
        try:
            response: requests.Response = requests.get(self.url, headers=BROWSER_HEADERS)
            soup: BeautifulSoup = BeautifulSoup(response.content, "html.parser")
            return soup
        except requests.RequestException as e:
            raise WebsiteParserError(f"Failed to fetch the website '{self.url}': {e}")

    def parse_website_content(self) -> None:
        self.title = self.soup.title.string if self.soup.title else "Title not found"
        for irrelevant in self.soup.body(["string", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = self.soup.body.get_text(separator="\n", strip=True)



class WebsiteParserError(Exception):
    pass


