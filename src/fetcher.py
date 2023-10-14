import json
import urllib.parse
from bs4 import BeautifulSoup
from selenium import webdriver

def fetch_data(max_price, min_rarity_rank, max_rarity_rank):
    # Construct the filters object
    filters = {
        "traits": [],
        "hasAsks": True,
        "priceRange": {
            "unit": "ETH",
            "maxAmount": str(max_price)
        },
        "rarityRange": {
            "minRank": str(min_rarity_rank),
            "maxRank": str(max_rarity_rank)
        }
    }

    # Convert the filters object to a JSON string, then URL-encode it
    encoded_filters = urllib.parse.quote(json.dumps(filters))

    # Construct the full URL
    fetchUrl = f'https://core-api.prod.blur.io/v1/collections/proof-moonbirds/tokens?filters={encoded_filters}'
    print(fetchUrl)

    driver = webdriver.Chrome()

    driver.get(url=fetchUrl)
    soup = BeautifulSoup(driver.page_source, 'lxml')
    data = json.loads(soup.text)

    return data
