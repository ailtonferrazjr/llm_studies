
import os
from dotenv import load_dotenv

load_dotenv()

# API Keys
OPENAI_KEY = os.environ.get("OPENAI_API_KEY")

# Headers
BROWSER_HEADERS: dict[str, str] = {
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}

