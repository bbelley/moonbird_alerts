# Moonbird Alerts

A Python-based application to fetch, monitor, and store token data from the Moonbirds NFT marketplace. This project is structured to fetch data based on certain filters, store it in a local SQLite database, and will later be expanded to send email alerts based on user-set price thresholds.

## Dependencies

- Python 3.x
- BeautifulSoup
- Selenium
- SQLite
- Chrome WebDriver

## Usage

1. Install the required dependencies:

```bash
pip install beautifulsoup4 selenium sqlite
```

1. Download the Chrome WebDriver and place it in your system's PATH or in the project directory.
2. Run the script:

```bash
python scripts/fetchPrices.py
```

This will fetch the data from the API, store it in the tokens.db SQLite database, and update the price history.

## Directory Structure

- `src/`
  - `__init__.py`
  - `fetcher.py` - Module for fetching data from the API.
  - `db_manager.py` - Module for managing the database operations.
- `scripts/`
  - `fetchPrices.py` - Main script to execute the fetching and storing process.
- `README.md`
- `tokens.db` - SQLite database to store the token data.
- `requirements.txt` - File listing all the Python dependencies.
