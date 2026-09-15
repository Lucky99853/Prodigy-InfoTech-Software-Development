# Task-05: Web Scraping

import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Send request to the website
response = requests.get(url)

# Check if the website responded successfully
if response.status_code == 200:

    soup = BeautifulSoup(response.text, "html.parser")

    products = []

    # Find all products on the page
    books = soup.find_all("article", class_="product_pod")

    for book in books:

        # Product name
        name = book.h3.a["title"]

        # Product price
        price = book.find("p", class_="price_color").text.strip()

        # Product rating
        rating = book.find("p", class_="star-rating")["class"][1]

        products.append({
            "Product Name": name,
            "Price": price,
            "Rating": rating
        })

    # Create DataFrame
    df = pd.DataFrame(products)

    # Save data to CSV
    df.to_csv("products.csv", index=False)

    print("Web scraping completed successfully!")
    print(f"Total products scraped: {len(df)}")
    print("\nFirst 5 products:")
    print(df.head())

else:
    print("Failed to access the website.")