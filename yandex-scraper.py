"""
Yandex Search Scraper: A Quick Start Example
See more at: https://apify.com/johnvc/scrape-yandex?fpr=9n7kx3

This script demonstrates how to use the Yandex Search Scraper Actor
to search Yandex and retrieve structured search results.
"""

import os
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from apify_client import ApifyClient

load_dotenv()

# Initialize the ApifyClient with your API token
client = ApifyClient(os.getenv("APIFY_API_TOKEN"))

# Prepare the Actor input
run_input = {
    "text": "python tutorial",
    "yandex_domain": "yandex.com",
    "lang": "en",
    "max_pages": 2,
}

# Run the Actor and wait for it to finish
run = client.actor("y7gc70pJD81ubH2I9").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)