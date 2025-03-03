import threading
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# List of websites to scrape
urls = [
    "https://www.python.org",
    "https://www.github.com",
    "https://www.wikipedia.org",
    "https://www.bbc.com",
    "https://www.cnn.com"
]

# Function to fetch content
def fetch_content(url):
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()  # Raise error for bad responses
    except requests.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract title
    title = soup.title.string.strip() if soup.title else "No title found"

    # Extract meta description
    meta_desc = soup.find("meta", attrs={"name": "description"})
    description = meta_desc["content"].strip() if meta_desc else "No description found"

    # Extract first 5 links (to keep output readable)
    links = [urljoin(url, a["href"]) for a in soup.find_all("a", href=True)][:5]

    # Print results
    print(f"\n🔹 {url}")
    print(f"Title: {title}")
    print(f"Description: {description}")
    print("Top 5 Links:")
    for link in links:
        print(f"  - {link}")

# Creating and starting threads
threads = []
for url in urls:
    t = threading.Thread(target=fetch_content, args=(url,))
    threads.append(t)
    t.start()

# Waiting for all threads to finish
for t in threads:
    t.join()

print("\n✅ Finished scraping all websites!")
