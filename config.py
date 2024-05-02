import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]

LABELS = [
    "funny", 
    "cheesy", 
    "weird", 
    "dark", 
    "cringe",
    "stupid",
]