"""
Yandex API: A Quick Start Example
See more at: https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3
Input schema: https://apify.com/johnvc/Scrape-Yandex/input-schema?fpr=9n7kx3

This script shows how to call the Yandex API on Apify from Python and read its
structured JSON output. It exercises several input parameters so you can see what
is configurable, while keeping the run small so your first call stays cheap.

Get your free Apify API key at: https://apify.com?fpr=9n7kx3
"""

import os
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the Apify client with your API token (read from .env)
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Build the Actor input.
# Inputs are kept small (one query, max_pages=1) to keep this first run
# inexpensive. Raise these once you have your own API key and know your budget.
run_input = {
    "text": "machine learning",    # the only required field
    "yandex_domain": "yandex.com",  # 15+ domains: yandex.com, yandex.ru, yandex.com.tr, ...
    "lang": "en",                   # 19 languages: en, ru, tr, de, ...
    "lr": 84,                       # region ID (84 = United States, 225 = Russia)
    "groups_on_page": 10,           # results per page (1 to 20)
    "max_pages": 1,                 # pages to fetch; kept at 1 to keep the run cheap
}

# Run the Actor and wait for it to finish
run = client.actor("johnvc/Scrape-Yandex").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} item(s).\n")

# Show a few key fields from each page of results.
for item in items:
    print(
        f"Query: {item.get('text')}  |  "
        f"Page: {item.get('page_number')}  |  "
        f"Results found: {item.get('total_results_found')}"
    )
    for result in (item.get("organic_results") or [])[:5]:
        print(f"  {result.get('position')}. {result.get('title')}")
        print(f"     {result.get('link')}")
    print()
