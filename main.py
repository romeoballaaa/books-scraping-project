import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"
EXCHANGE_API_URL = "https://api.exchangerate.host/latest"


def scrape_books(limit_pages=10):
    books = []

    for page in range(1, limit_pages + 1):
        print(f"Scraping page {page}...")
        url = BASE_URL.format(page)
        response = requests.get(url)
        response.encoding = "utf-8"

        if response.status_code != 200:
            print(f"Page {page} not found. Stopping scraping.")
            break

        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")

        if not articles:
            break

        for book in articles:
            title = book.h3.a["title"]
            price_text = book.find("p", class_="price_color").text.strip()
            price_text = price_text.replace("£", "").replace("Â", "")
            price_gbp = float(price_text)
            rating = book.find("p")["class"][1]

            books.append({
                "title": title,
                "price_gbp": price_gbp,
                "rating": rating
            })

    return books


def convert_gbp_to_eur(books):
    print("Fetching exchange rate GBP -> EUR from API...")

    # Marrim kursin GBP -> EUR nga endpoint /latest
    try:
        response = requests.get(EXCHANGE_API_URL, params={"base": "GBP", "symbols": "EUR"})
        data = response.json()
        rate = data["rates"]["EUR"]
        print(f"Current exchange rate: 1 GBP = {rate} EUR")
    except Exception as e:
        print(f"Failed to get exchange rate: {e}")
        rate = None

    for book in books:
        if rate is not None:
            book["price_eur"] = round(book["price_gbp"] * rate, 2)
        else:
            book["price_eur"] = None

    return books


def save_to_csv(data, filename="output.csv"):
    if not data:
        print("No data to save!")
        return

    keys = data[0].keys()
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)


def main():
    print("Starting scraping...")
    scraped_data = scrape_books(limit_pages=10)

    print("Converting prices using exchange rate API...")
    final_data = convert_gbp_to_eur(scraped_data)

    save_to_csv(final_data)
    print("Done! Data saved in output.csv")


if __name__ == "__main__":
    main()
