from playwright.sync_api import sync_playwright

def scrape_tripadvisor(url: str) -> str:
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url)
        page.wait_for_timeout(5000)
        content = page.content()
        browser.close()
        return content

if __name__ == "__main__":
    html = scrape_tripadvisor("https://www.tripadvisor.in/Attractions-g297604-Activities-zft12163-Goa.html")
    with open("output/raw_html/tripadvisor.html", "w", encoding="utf-8") as f:
        f.write(html)
