# Web Scraper

import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.shadowfox.in/"

try:
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    headings = soup.find_all(["h1", "h2", "h3"])

    data = []
    for heading in headings:
        text = heading.get_text(strip=True)
        if text:
            data.append(text)

    with open("data.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Shadowfox Website Headings"])

        for i in data:
            writer.writerow([i])
    print("Data extraction completed successfully!")
    print("Total headings extracted:",len(data))
    print("Data saved in data.csv")

except requests.exceptions.RequestException as e:
    print("Website error:",e)

except Exception as error:
    print("An error occurred", error)
