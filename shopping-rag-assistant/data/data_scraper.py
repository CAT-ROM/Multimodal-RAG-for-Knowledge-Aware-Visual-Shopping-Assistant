import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import time

# Folder to save images
IMAGE_DIR = "data/images"
os.makedirs(IMAGE_DIR, exist_ok=True)

# Sample product URLs - replace with your own URLs (e.g., 50 product pages)
product_urls = [
    "https://www.amazon.in/dp/B08N5WRWNW",  # Example product 1 (change this)
    "https://www.amazon.in/dp/B07FZ8S74R",  # Example product 2 (change this)
    # Add more product URLs here...
]

products = []

def download_image(url, filename):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(filename, "wb") as f:
                f.write(response.content)
            print(f"Image saved: {filename}")
    except Exception as e:
        print(f"Failed to download image {url}: {e}")

for i, url in enumerate(product_urls):
    print(f"Scraping product {i+1}/{len(product_urls)}: {url}")
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print(f"Failed to fetch {url}")
        continue

    soup = BeautifulSoup(response.content, "html.parser")

    # Extract Title
    title_tag = soup.find(id="productTitle")
    title = title_tag.get_text(strip=True) if title_tag else "N/A"

    # Extract Price
    price_tag = soup.find("span", {"class": "a-price-whole"})
    price = price_tag.get_text(strip=True) if price_tag else "N/A"

    # Extract category (breadcrumb)
    categories = [crumb.get_text(strip=True) for crumb in soup.select("#wayfinding-breadcrumbs_container ul li span.a-list-item")]
    category = " > ".join(categories) if categories else "N/A"

    # Extract product description/specifications
    desc_tag = soup.find(id="productDescription")
    description = desc_tag.get_text(strip=True) if desc_tag else "N/A"

    # Extract image URL (main image)
    img_tag = soup.find(id="landingImage") or soup.find("img", {"id": "imgBlkFront"})
    img_url = img_tag["src"] if img_tag else None

    # Download image
    img_filename = None
    if img_url:
        img_filename = os.path.join(IMAGE_DIR, f"product_{i+1}.jpg")
        download_image(img_url, img_filename)

    # For demo, reviews and Q&A scraping is skipped due to complexity.
    # You can extend this with scraping reviews and Q&A pages.

    # Save product info
    product_data = {
        "product_id": f"P{i+1:03d}",
        "title": title,
        "price": price,
        "category": category,
        "description": description,
        "image_path": img_filename if img_filename else "N/A",
        # Add fields for reviews, Q&A, specs as you scrape them
    }
    products.append(product_data)

    # Respectful scraping delay
    time.sleep(3)

# Save all products to CSV
df = pd.DataFrame(products)
df.to_csv("data/products_metadata.csv", index=False)
print("Saved product metadata to data/products_metadata.csv")
