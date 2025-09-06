https://apify.com/johnvc/scrape-yandex?fpr=9n7kx3

# 🚀 Yandex Search Scraper 🇷🇺🇺🇸

> **The most efficient, reliable, and developer-friendly Yandex search scraper**

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- An Apify account and API key

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd Apify-Yandex-Search-Scraper
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   # Using venv (Python 3.3+)
   python -m venv venv
   
   # Activate the virtual environment
   # On macOS/Linux:
   source venv/bin/activate
   # On Windows:
   venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   # Install from requirements.txt
   pip install -r requirements.txt

   ```

4. **Configure your API key**
   ```bash
   # Copy the example environment file
   cp .env.example .env
   
   # Edit .env and add your Apify API key
   # Get your API key from: https://apify.com?fpr=9n7kx3
   ```

5. **Run the example**
   ```bash
   python yandex-scraper.py
   ```

### Alternative: Direct API Key Usage
If you prefer not to use a `.env` file, you can set the environment variable directly:
```bash
export APIFY_API_TOKEN="your_api_key_here"
python yandex-scraper.py
```

## 🌟 Why Choose This Scraper?

### "In Soviet Russia, Yandex website scrape you!" 🇷🇺🇺🇸

The Yandex Search data scraper delivers enterprise-grade performance with these advanced capabilities:

**Performance & Reliability**: Built optimized for high-throughput scraping with intelligent rate limiting and pagination handling.

**Cost-Effective**: Provides consistent, reliable results with intelligent pagination management to optimize API usage.

**Lightning-Fast Search & Retrieval**: Search any keyword across Yandex with blazing-fast performance. Retrieve comprehensive results in seconds, not minutes, with intelligent caching and optimization.

**Precision Targeting & Advanced Filtering**: Pinpoint exact search parameters with domain-specific localization, language support, and location targeting. Get precisely the search data you need, when you need it.

**Rich, Structured Data Extraction**: Extract complete search information, including organic results, ads, knowledge graph, inline images, and inline videos. Our advanced parsing ensures you get clean, structured data ready for immediate use.

**Enterprise-Grade Configuration & Flexibility**: Built for developers and businesses who demand reliability. Highly configurable with intuitive controls, comprehensive error handling, and robust logging. Focus on your business logic while we handle the complexity of search scraping.

**No Hidden Costs or Rental Fees**: We do not charge monthly rentals, our scraper operates on a pay-per-use model. Scale up or down based on your actual needs without being locked into expensive subscriptions.

## 🚀 Features

### Core Capabilities
- **Advanced Search**: Support for complex queries with domain-specific localization and language targeting
- **Intelligent Pagination**: Automatic handling of Yandex search pagination with configurable limits
- **Global Localization**: Support for 15+ Yandex domains across different regions
- **Language Support**: 19 officially supported languages including Russian, English, Turkish, and more
- **Location Targeting**: Custom location/region ID support for precise geographic targeting

### Data Quality
- **Clean Output**: Automatic structured data metadata for clean, production-ready data
- **Structured Results**: Consistent JSON structure across all search results
- **Comprehensive Fields**: Organic results, ads, knowledge graph, news, inline images, inline videos, and related searches
- **Metadata Tracking**: Page-level analytics and search performance metrics
- **Per-Page Billing**: Results are pushed as separate dataset items for accurate billing

## 📖 Usage Examples

### Basic Search Example

Search for "python tutorial" with default settings.

```json
{
  "text": "python tutorial"
}
```

### Advanced Search Example 1

Search for "machine learning" with Russian domain, Russian language, and pagination limits.

```json
{
  "text": "machine learning",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "max_pages": 3
}
```

### Advanced Search Example 2

Search for "yandex serp" with Russian domain, Russian language, and pagination limits.

```json
{
  "text": "yandex serp",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "max_pages": 1
}
```

### Advanced Search Example 3

Search for "yandex scrapers" with English domain, English language, and location targeting.

```json
{
  "text": "yandex scrapers",
  "yandex_domain": "yandex.com",
  "lang": "en",
  "lr": "84",
  "max_pages": 2
}
```

## 🔍 Input References
#### Input Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `text` | `str` | ✅ | `"python tutorial"` | Search query |
| `yandex_domain` | `str` | ❌ | `"yandex.com"` | Yandex domain (e.g., `"yandex.ru"` for Russia, `"yandex.com.tr"` for Turkey) |
| `lang` | `str` | ❌ | `"en"` | Language code (e.g., `"ru"` for Russian, `"tr"` for Turkish, `"null"` for unspecified) |
| `lr` | `str` | ❌ | `None` | Location/region ID to limit search results |
| `max_pages` | `Optional[int]` | ❌ | `2` | Maximum pages to fetch (0 = no limit) |
| `output_file` | `Optional[str]` | ❌ | `None` | Custom output filename |

## 📊 Output Format

### Search Result Structure

```json
{
  "text": "machine learning",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "lr": "225",
  "max_pages": 3,
  "total_results_found": 150,
  "pages_processed": 3,
  "search_metadata": {
    "yandex_domain": "yandex.ru",
    "domain_description": "Russia",
    "language": "ru",
    "language_description": "Russian",
    "location": "225",
    "max_pages": 3,
    "pagination_limit_reached": false
  },
  "pagination_info": {
    "total_pages": 3,
    "max_pages_set": 3,
    "pagination_stopped_by_limit": false,
    "results_per_page": 10
  },
  "organic_results": [
    {
      "title": "Machine Learning Tutorial",
      "link": "https://example.com/ml-tutorial",
      "snippet": "Learn machine learning fundamentals...",
      "position": 1,
      "displayed_link": "example.com",
      "thumbnail": "https://thumbnail.url",
      "favicon": "https://favicon.url",
      "date": "2024-01-15",
      "rich_snippet": "Rich snippet content...",
      "sitelinks": [...]
    }
  ],
  "ads_results": [...],
  "knowledge_graph": [...],
  "inline_images": [...],
  "inline_videos": [...],
  "results_by_page": {
    "1": {
      "organic_results": [...],
      "ads_results": [...],
      "knowledge_graph": [...],
      "inline_images": [...],
      "inline_videos": [...]
    }
  }
}
```

**Made with ❤️**

*Transform your search automation with the most reliable and efficient Yandex search scraper on the market.*
Last Updated: 2025.09.06
