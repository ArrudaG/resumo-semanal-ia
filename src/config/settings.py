import os

from dotenv import load_dotenv

load_dotenv()

EMAIL_USER = os.getenv("EMAIL_USER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = os.getenv("EMAIL_TO")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = "gemini-2.5-flash"
url = "https://newsapi.org/v2/everything"
params = {
    "q": "(Ibovespa OR B3 OR Petrobras OR Banco Santander OR Ouro OR Itau OR CSN OR Banco Central OR inflação)",
    "language": "pt",
    "pageSize": 10
}