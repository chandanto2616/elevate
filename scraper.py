import requests
from bs4 import BeautifulSoup

# Step 1: Choose a website to scrape
URL = "https://www.bbc.com/news"

# Step 2: Send request to fetch the webpage
response = requests.get(URL)

# Step 3: Check if request was successful
if response.status_code == 200:
    # Step 4: Parse HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Step 5: Find all <h2> tags (BBC uses h2 for headlines)
    headlines = soup.find_all("h2")

    # Step 6: Save results to a text file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        for index, h in enumerate(headlines, start=1):
            title = h.get_text(strip=True)  # Extract text
            if title:  # Avoid empty lines
                file.write(f"{index}. {title}\n")
                print(f"{index}. {title}")  # Also show in terminal

    print("\n✅ Headlines saved to headlines.txt")

else:
    print("❌ Failed to fetch webpage. Status code:", response.status_code)
