import os
from typing import Final

import requests
from bs4 import BeautifulSoup

TELEGRAM_API_TOKEN: Final = os.getenv("TELEGRAM_API_TOKEN")
CHAT_IDS: Final = os.getenv("CHAT_IDS").split(",")

G_SUPS_URL = (
    "https://www.gsuplementos.com.br/creatina-250g-creapure-growth-supplements-p985824"
)


def get_available(g_supplements_item_url: str) -> bool:
    """ """

    req = requests.get(
        g_supplements_item_url,
        headers={
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36"
        },
    )
    doc = BeautifulSoup(req.text, "html.parser")
    prices = doc.find_all("button", {"class": "btIndisponivel"})
    return prices == []


def send_telegram_msg() -> None:
    """ """
    for chat_id in CHAT_IDS:
        url = f"https://api.telegram.org/bot{TELEGRAM_API_TOKEN}/sendMessage"
        params = {
            "chat_id": chat_id,
            "text": f"Creatina Creapure Growth Suplementos 250g disponível!!!\nCompre agora:\n{G_SUPS_URL}",
        }
        response = requests.get(url, params=params)
        response.raise_for_status()  # Throw an exception if the request fails


def main():
    available = get_available(G_SUPS_URL)
    if available:
        send_telegram_msg()

    return 0


if __name__ == "__main__":
    main()

# doctl serverless deploy .
# doctl serverless functions invoke supplement_scraper/main
