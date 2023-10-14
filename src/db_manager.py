
def create_tables(conn):
    c = conn.cursor()

    # Create tokens table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS tokens (
            tokenId TEXT PRIMARY KEY,
            traits TEXT,
            listedAt TEXT,
            marketplace TEXT,
            numberOwnedByOwner INTEGER,
            isSuspicious BOOLEAN,
            rarityRank INTEGER,
            latestPrice FLOAT,
            isListed BOOLEAN
        )
    ''')

    # Create price_history table if it doesn't exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tokenId TEXT,
            price FLOAT,
            timestamp TEXT,
            FOREIGN KEY(tokenId) REFERENCES tokens(tokenId)
        )
    ''')
    conn.commit()


def insert_data(conn, tokens_data, price_history_data):
    c = conn.cursor()
    # Insert new token data, ignoring conflicts
    c.executemany('''
        INSERT OR IGNORE INTO tokens (
            tokenId, traits, listedAt, marketplace, 
            numberOwnedByOwner, isSuspicious, rarityRank, 
            latestPrice, isListed
        )
        VALUES (?,?,?,?,?,?,?,?,?)
    ''', tokens_data)

    # Update existing token data
    c.executemany('''
        UPDATE tokens SET
            traits = ?,
            listedAt = ?,
            marketplace = ?,
            numberOwnedByOwner = ?,
            isSuspicious = ?,
            rarityRank = ?,
            latestPrice = ?,
            isListed = ?
        WHERE tokenId = ?
    ''', [(traits, listed_at, marketplace, number_owned_by_owner, is_suspicious, rarity_rank, latest_price, is_listed, token_id) for token_id, traits, listed_at, marketplace, number_owned_by_owner, is_suspicious, rarity_rank, latest_price, is_listed in tokens_data])

    # Insert price history data
    c.executemany('''
        INSERT INTO price_history (tokenId, price, timestamp)
        VALUES (?,?,?)
    ''', price_history_data)
    conn.commit()


def update_listing_status(conn, listed_token_ids):
    c = conn.cursor()
    # After processing all the current tokens, update the isListed field for any tokens not in the current data set:
    placeholders = ','.join('?' * len(listed_token_ids))
    c.execute(
        f'UPDATE tokens SET isListed = 0 WHERE tokenId NOT IN ({placeholders})', listed_token_ids)
    conn.commit()
