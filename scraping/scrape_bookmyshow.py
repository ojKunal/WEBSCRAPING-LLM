import requests
from bs4 import BeautifulSoup

def scrape_bookmyshow(url: str):
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    return soup.get_text()

if __name__ == "__main__":
    text = scrape_bookmyshow("https://in.bookmyshow.com/explore/adventure-bengaluru")
    with open("output/raw_html/bookmyshow.txt", "w", encoding="utf-8") as f:
        f.write(text)
