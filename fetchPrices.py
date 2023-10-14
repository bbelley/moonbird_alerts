import sqlite3
import json
import datetime
from src.fetcher import fetch_data
from src.db_manager import create_tables, insert_data, update_listing_status

# Assume these values are obtained from user input
max_price = 4
min_rarity_rank = 1
max_rarity_rank = 1000

data = fetch_data(max_price, min_rarity_rank, max_rarity_rank)

# Process data to prepare tokens_data and price_history_data
tokens_data = []
price_history_data = []

for token in data['tokens']:
    token_id = token['tokenId']
    # Convert traits dictionary to a JSON string for storage
    traits = json.dumps(token['traits'])
    listed_at = token['price']['listedAt']
    marketplace = token['price']['marketplace']
    number_owned_by_owner = token['numberOwnedByOwner']
    is_suspicious = token['isSuspicious']
    rarity_rank = token['rarityRank']
    latest_price = token['price']['amount']
    is_listed = True  # Assuming that all tokens in the current data set are listed
    tokens_data.append((token_id, traits, listed_at, marketplace,
                       number_owned_by_owner, is_suspicious, rarity_rank, latest_price, is_listed))

    price = token['price']['amount']
    timestamp = datetime.datetime.utcnow().isoformat() + 'Z'
    price_history_data.append((token_id, price, timestamp))

# Step 3: Store Data
conn = sqlite3.connect('tokens.db')
create_tables(conn)
insert_data(conn, tokens_data, price_history_data)

listed_token_ids = [token['tokenId'] for token in data['tokens']]
update_listing_status(conn, listed_token_ids)
conn.close()
