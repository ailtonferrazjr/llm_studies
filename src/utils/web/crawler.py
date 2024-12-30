# This is a crawler based in selenium and chromium webdriver, in order to extract the html from webpages
# src/utils/web/crawler.py

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


PATH_TO_CHROME_DRIVER = 'src/utils/web/drivers/chromedriver.exe'

class Website:
    url: str
    title: str
    text: str

    def __init__(self, url):
        self.url = url

        options = Options()

        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        service = Service(PATH_TO_CHROME_DRIVER)
        driver = webdriver.Chrome(service=service, options=options)
        driver.get(url)

        # input("Please complete the verification in the browser and press Enter to continue...")
        page_source = driver.page_source
        driver.quit()

        soup = BeautifulSoup(page_source, 'html.parser')
        self.title = soup.title.string if soup.title else "No title found"
        for irrelevant in soup(["script", "style", "img", "input"]):
            irrelevant.decompose()
        self.text = soup.get_text(separator="\n", strip=True)


