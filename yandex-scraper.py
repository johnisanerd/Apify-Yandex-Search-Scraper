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

# Build the Actor input. | Сформируйте входные данные актора.
# Inputs are kept small (one query, max_pages=1) to keep this first run
# inexpensive. Raise these once you have your own API key and know your budget.
# Параметры намеренно небольшие (один запрос, max_pages=1), чтобы первый запуск
# был дешёвым. Увеличьте их, когда у вас будет свой ключ и понятный бюджет.
run_input = {
    "text": "machine learning",    # the only required field | единственное обязательное поле
    # Choose your result types a la carte. Organic is on by default; enable the
    # others to also collect ads, the knowledge graph card, inline images, and
    # inline videos. Each enabled type that appears on the page is returned as
    # its own dataset item, tagged with an "item_type" field.
    # Выберите типы результатов. Каждый выбранный тип возвращается отдельным
    # элементом набора данных с полем "item_type".
    "include_organic_results": True,
    "include_ads": False,
    "include_knowledge_graph": True,
    "include_inline_images": False,
    "include_inline_videos": False,
    "yandex_domain": "yandex.com",  # 6 domains: yandex.com, yandex.ru, yandex.by, yandex.kz, yandex.uz, yandex.com.tr
    "lang": "en",                   # 19 languages: en, ru, tr, de, ...
    "lr": 84,                       # region ID (84 = United States, 225 = Russia)
    "sort_mode": "relevance",       # "relevance" (default) or "date" (newest first)
    "period": "all",                # time window: all | day | last_two_weeks | month
    "groups_on_page": 10,           # results per page (1 to 20) | результатов на странице
    "family_mode": 1,               # safe search: 0 off, 1 moderate, 2 strict | безопасный поиск
    "fix_typo": True,               # auto-correct spelling | автоисправление опечаток
    "max_pages": 1,                 # pages to fetch; kept at 1 to keep the run cheap
}

# Russian-market example. Swap it in to search the Russian index in Russian,
# localized to Moscow (lr=213), sorted newest-first within the last two weeks.
# Пример для российского рынка: русский индекс, локализация по Москве (lr=213),
# сортировка по дате за последние две недели.
# run_input = {
#     "text": "машинное обучение",
#     "yandex_domain": "yandex.ru",
#     "lang": "ru",
#     "lr": 213,
#     "sort_mode": "date",
#     "period": "last_two_weeks",
#     "max_pages": 1,
# }

# Run the Actor and wait for it to finish
run = client.actor("johnvc/Scrape-Yandex").call(run_input=run_input)
if run is None:
    raise SystemExit("The Actor run did not return a result.")

# Read structured results from the run's default dataset
items = list(client.dataset(run.default_dataset_id).iterate_items())
print(f"Returned {len(items)} item(s).\n")

# Each item carries one result type, named by "item_type". Map each type to the
# array that holds its rows so we can print any of them the same way.
ARRAY_KEY = {
    "organic": "organic_results",
    "ads": "ads_results",
    "knowledge_graph": "knowledge_graph",
    "inline_images": "inline_images",
    "inline_videos": "inline_videos",
}

for item in items:
    item_type = item.get("item_type", "organic")
    rows = item.get(ARRAY_KEY.get(item_type, "organic_results")) or []
    print(
        f"[{item_type}] page {item.get('page_number')}  |  "
        f"results in item: {item.get('result_count')}  |  "
        f"total organic found: {item.get('total_results_found')}"
    )
    for row in rows[:5]:
        # organic/ads/images/videos expose title + link; knowledge graph uses title + description.
        title = row.get("title", "")
        detail = row.get("link") or row.get("description", "")
        position = row.get("position")
        prefix = f"  {position}. " if position else "  - "
        print(f"{prefix}{title}")
        if detail:
            print(f"     {detail}")
    print()
