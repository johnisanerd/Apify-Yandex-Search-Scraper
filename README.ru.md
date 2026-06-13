[English](README.md) | **Русский**

# 🔎 Yandex API: структурированная выдача Яндекса в чистом JSON

> Самый эффективный, надёжный и удобный для разработчиков способ работать с Yandex API.

**Страница актора:** [apify.com/johnvc/Scrape-Yandex](https://apify.com/johnvc/Scrape-Yandex?fpr=9n7kx3)
**Схема ввода:** [apify.com/johnvc/Scrape-Yandex/input-schema](https://apify.com/johnvc/Scrape-Yandex/input-schema?fpr=9n7kx3)

Yandex API выполняет поиск в Яндексе по любому запросу и возвращает чистый структурированный JSON. Каждая страница результатов содержит органическую выдачу (заголовок, ссылка, описание, позиция, быстрые ссылки), платную рекламу, карточки графа знаний, блоки изображений и видео, а также метаданные по странице. Поддерживаются 6 доменов Яндекса, 19 языков и таргетинг по более чем 123 000 регионам, с автоматической пагинацией и управлением безопасным поиском.

## Видеообзор

[![Смотреть обзор](https://img.youtube.com/vi/jREWahDGhJM/maxresdefault.jpg)](https://www.youtube.com/watch?v=jREWahDGhJM)

## Быстрый старт

### Требования
- Python 3.11 или новее
- Аккаунт Apify и ключ API ([получить бесплатный ключ](https://apify.com?fpr=9n7kx3))

1. **Клонируйте репозиторий**
   ```bash
   git clone https://github.com/johnisanerd/Apify-Yandex-Search-Scraper.git
   cd Apify-Yandex-Search-Scraper
   ```

2. **Установите зависимости через UV**
   ```bash
   # Установите UV, если его нет:
   curl -LsSf https://astral.sh/uv/install.sh | sh

   # Установите зависимости проекта:
   uv sync
   ```

3. **Настройте ключ API**
   ```bash
   cp .env.example .env
   # Откройте .env и добавьте свой ключ API Apify
   # Получите бесплатный ключ: https://apify.com?fpr=9n7kx3
   ```

4. **Запустите пример**
   ```bash
   uv run python yandex-scraper.py
   ```

### Альтернатива: задать ключ напрямую
```bash
export APIFY_API_TOKEN="your_api_key_here"
uv run python yandex-scraper.py
```

## Почему стоит использовать этот Yandex API?

**Полный охват страницы результатов.** Один вызов возвращает всю страницу результатов Яндекса в виде структурированных данных: органическую выдачу, рекламу, карточки графа знаний, блоки изображений и видео. Вы получаете всю страницу, а не только органические ссылки.

**Создан для русскоязычных рынков и стран СНГ.** Поддерживает 6 доменов Яндекса (yandex.com, yandex.ru, yandex.by, yandex.kz, yandex.uz, yandex.com.tr), 19 языков и более 123 000 идентификаторов регионов. Это удобно для SEO, конкурентной разведки и мониторинга бренда в России, Восточной Европе, Центральной Азии и за их пределами.

**Предсказуемая оплата по факту использования.** Оплата начисляется за запуск и за обработанную страницу, без ежемесячной аренды. Вы платите только за реально выполненные запросы и управляете расходами через лимит страниц.

**Чистый и единообразный JSON.** Каждая страница приходит как структурированный элемент набора данных с одинаковой схемой, поэтому код для разбора пишется один раз и работает для любых запросов, доменов и языков.

**Простая автоматизация.** Вызывайте API из Python в несколько строк или подключите его как инструмент MCP, чтобы ассистенты Claude и Cursor выполняли поиск в Яндексе по вашему запросу.

## Возможности

### Основные возможности
- **Поиск по ключевым словам** в Яндексе с извлечением всей страницы результатов
- **Типы результатов по выбору**: включайте органику, рекламу, граф знаний, изображения и видео по отдельности; каждый выбранный тип возвращается отдельным элементом с полем `item_type`
- **Локализация по доменам** среди 6 доменов Яндекса
- **Таргетинг по языку** с поддержкой 19 языков
- **Таргетинг по региону** с более чем 123 000 идентификаторов локаций (параметр `lr`)
- **Фильтры сортировки и периода**: `sort_mode` (relevance или date) и `period` (all, day, last_two_weeks, month)
- **Безопасный поиск и исправление опечаток**, плюс быстрая параллельная постраничная навигация

### Качество данных
- **Структурированная органическая выдача**: заголовок, ссылка, описание, позиция, отображаемая ссылка, дата и быстрые ссылки
- **Богатые блоки результатов**: реклама, граф знаний, изображения и видео, каждый с `result_count`
- **Метаданные по каждой странице**: домен, язык, локация и сведения о постраничной навигации
- **Единообразный JSON** для каждого запроса
- **Оплата за страницу** для прозрачности при больших объёмах

## Примеры использования

### Базовый пример
Поиск на одну страницу по одному ключевому слову. Самый дешёвый способ попробовать API.
```json
{
  "text": "machine learning",
  "yandex_domain": "yandex.com",
  "max_pages": 1
}
```

### Расширенный пример
Поиск на российском домене на русском языке, с идентификатором региона, увеличенным числом результатов на странице и двумя страницами.
```json
{
  "text": "машинное обучение",
  "yandex_domain": "yandex.ru",
  "lang": "ru",
  "lr": 225,
  "groups_on_page": 20,
  "family_mode": 1,
  "max_pages": 2
}
```

### Совет: фильтрация по дате
Яндекс поддерживает встроенный оператор диапазона дат в тексте запроса. Добавьте `date:YYYYMMDD..YYYYMMDD` к полю `text`, чтобы ограничить результаты периодом. Дополнительные параметры не нужны.
```json
{
  "text": "climate news date:20260317..20260417",
  "yandex_domain": "yandex.com",
  "lang": "en",
  "max_pages": 1
}
```

## Входные параметры

| Параметр | Тип | Обязательный | По умолчанию | Описание |
|-----------|------|----------|---------|-------------|
| `text` | `string` | Да | - | Поисковый запрос. Поддерживает операторы Яндекса, например `site:wikipedia.org python`. |
| `include_organic_results` | `boolean` | Нет | `true` | Возвращать органическую выдачу (`item_type` `organic`). |
| `include_ads` | `boolean` | Нет | `false` | Возвращать рекламу, если присутствует (`item_type` `ads`). |
| `include_knowledge_graph` | `boolean` | Нет | `false` | Возвращать карточку графа знаний (`item_type` `knowledge_graph`). |
| `include_inline_images` | `boolean` | Нет | `false` | Возвращать блок изображений (`item_type` `inline_images`). |
| `include_inline_videos` | `boolean` | Нет | `false` | Возвращать блок видео (`item_type` `inline_videos`). |
| `yandex_domain` | `string` | Нет | `yandex.com` | Домен Яндекса, например `yandex.ru`, `yandex.com.tr`, `yandex.kz` (поддерживается 6). |
| `lang` | `string` | Нет | `en` | Код языка, например `ru`, `en`, `tr`, `de` (поддерживается 19); `null` - не указан. |
| `lr` | `integer` | Нет | (по домену) | Идентификатор региона, например `225` = Россия, `84` = США, `149` = Беларусь. Более 123 000 ID; полная таблица на странице актора. |
| `max_pages` | `integer` | Нет | `2` | Максимум страниц (`0` = без лимита). Применяется ко всем выбранным типам. |
| `sort_mode` | `string` | Нет | `relevance` | Сортировка: `relevance` или `date` (сначала новые). |
| `period` | `string` | Нет | `all` | Период: `all`, `day`, `last_two_weeks`, `month`. |
| `groups_on_page` | `integer` | Нет | `10` | Результатов на странице (от 1 до 20). |
| `family_mode` | `integer` | Нет | `1` | Безопасный поиск: `0` = выкл, `1` = умеренный, `2` = строгий. |
| `fix_typo` | `boolean` | Нет | `true` | Автоисправление опечаток в запросе. |
| `output_file` | `string` | Нет | (нет) | Имя файла для сохранения результатов; создаётся автоматически, если не задано. |

## Формат вывода

Каждый выбранный тип результатов, присутствующий на странице, возвращается отдельным элементом набора данных с полем `item_type` (`organic`, `ads`, `knowledge_graph`, `inline_images`, `inline_videos`) и `result_count`. Ниже показан элемент `organic` для запроса `Apple`; массивы и часть полей сокращены для читаемости.

```json
{
  "item_type": "organic",
  "result_count": 10,
  "text": "Apple",
  "yandex_domain": "yandex.com",
  "lang": "en",
  "lr": "84",
  "page_number": 1,
  "search_domain": "yandex.com",
  "search_domain_description": "United States",
  "search_language": "en",
  "search_language_description": "English",
  "search_location": "84",
  "total_results_found": 10,
  "pages_processed": 1,
  "total_pages": 1,
  "max_pages_set": 1,
  "results_per_page": 10,
  "pagination_limit_reached": true,
  "pagination_stopped_by_limit": true,
  "organic_results": [
    {
      "position": 1,
      "title": "Apple",
      "link": "https://www.apple.com/",
      "displayed_link": "apple.com",
      "snippet": "Apple Payments Services LLC, a subsidiary of Apple Inc., is a service provider of Goldman Sachs Bank USA for Apple Card and Savings accounts."
    },
    {
      "position": 3,
      "title": "Apple Inc. - Wikipedia",
      "link": "https://en.m.wikipedia.org/wiki/Apple_Inc.",
      "displayed_link": "en.m.wikipedia.org",
      "snippet": "Apple Inc. is an American multinational corporation and technology company headquartered in Cupertino, California, in Silicon Valley."
    }
  ],
  "ads_results": [],
  "knowledge_graph": [
    {
      "title": "Apple Inc.",
      "description": "American multinational technology company headquartered in Cupertino, California.",
      "source": { "name": "en.wikipedia.org" }
    }
  ],
  "inline_images": [],
  "inline_videos": []
}
```

---

## Использование как инструмент MCP

Вы можете подключить Yandex API как инструмент MCP, чтобы ассистенты вызывали его за вас. URL сервера MCP предзагружает только этот актор:

```
https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex
```

Авторизуйтесь через OAuth в браузере, когда будет предложено, или с помощью токена API Apify (тот же `APIFY_API_TOKEN`, что и в примере на Python). Получите токен на https://console.apify.com/settings/integrations и бесплатный аккаунт Apify на https://apify.com?fpr=9n7kx3 .

## Установка в Claude Cowork Desktop

![Установка в Claude Cowork Desktop](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_desktop.png)

Cowork - это режим автоматизации в десктоп-приложении. Чтобы дать ему Yandex API как инструмент, добавьте сервер Apify MCP как коннектор.

1. Откройте приложение Claude и перейдите в **Settings → Connectors** (или **Settings → Developer → Edit Config**, чтобы редактировать `claude_desktop_config.json` напрямую).
   - macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
   - Windows: `%APPDATA%\Claude\claude_desktop_config.json`
2. Добавьте сервер Apify MCP, предзагруженный только этим актором:

```json
{
  "mcpServers": {
    "apify": {
      "command": "npx",
      "args": [
        "-y",
        "mcp-remote",
        "https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex"
      ]
    }
  }
}
```

3. Перезапустите приложение. При первом вызове инструмента в Cowork пройдите OAuth в браузере или добавьте токен API Apify в настройках коннектора, чтобы пропустить OAuth.
4. В чате Cowork убедитесь, что инструмент доступен, и попросите запустить Yandex API.

Скачайте приложение и начните бесплатный период: https://claude.ai/referral/uIlpa7nPLg
Подробнее: https://docs.apify.com/platform/integrations/claude-desktop

## Установка в Claude Code

![Установка в Claude Code](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_code.png)

Claude Code - это инструмент командной строки. Добавьте сервер MCP актора одной командой:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex"
```

Чтобы использовать токен вместо OAuth в браузере:

```bash
claude mcp add --transport http apify \
  "https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex" \
  --header "Authorization: Bearer YOUR_APIFY_TOKEN"
```

Затем проверьте через `claude mcp list` или выполните `/mcp` в сессии. Попросите Claude Code вызвать Yandex API.

Попробуйте Claude Code бесплатно: https://claude.ai/referral/uIlpa7nPLg
Документация MCP: https://code.claude.com/docs/en/mcp

## Установка в Claude (веб-сайт)

![Установка в Claude (веб-сайт)](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_claude_ai.png)

На claude.ai вы добавляете Apify как коннектор, затем включаете инструмент именно этого актора.

1. Перейдите в **Settings → Connectors → Browse connectors** и найдите **Apify MCP server**. Установите его (включите или обновите при необходимости).
2. При подключении авторизуйтесь токеном API Apify и включите инструмент `johnvc/Scrape-Yandex`.
3. В любом чате откройте **+ → Connectors** и включите **Apify**.
4. Или выберите **Add custom connector** и вставьте полный URL MCP `https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex`, пройдя OAuth при запросе.
5. Попросите Claude запустить Yandex API.

Откройте Claude в браузере: https://claude.ai

## Установка в Cursor

![Установка в Cursor](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_cursor.png)

Cursor читает серверы MCP из файла проекта `.cursor/mcp.json`.

1. В вашем проекте создайте `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex"
    }
  }
}
```

2. Если предпочитаете токен вместо OAuth, добавьте заголовок:

```json
{
  "mcpServers": {
    "apify": {
      "url": "https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex",
      "headers": { "Authorization": "Bearer YOUR_APIFY_TOKEN" }
    }
  }
}
```

3. Откройте **Cursor → Settings → MCP** и убедитесь, что сервер **apify** подключён (зелёная точка).
4. В Composer или Chat попросите Cursor вызвать Yandex API.

Впервые в Cursor? Скачайте: https://cursor.com/referral?code=XQP4VBLI3NNX

## Установка в ChatGPT

![Установка в ChatGPT](https://raw.githubusercontent.com/johnisanerd/ApifyPublicData/main/assets/guides/install_mcp_into_ChatGPT.png)

ChatGPT подключается к серверу Apify MCP через режим разработчика (доступен в планах ChatGPT Pro, Plus, Business, Enterprise и Education).

1. Нажмите на иконку профиля, затем перейдите в **Settings > Apps**. Если нет кнопки **Create app**, откройте **Advanced settings** и включите **Developer mode**.
2. Нажмите **Create app** и заполните форму:
   - **Name:** Apify
   - **MCP Server URL:** `https://mcp.apify.com/?tools=actors,docs,johnvc/Scrape-Yandex`
   - **Authentication:** OAuth
3. Нажмите **Create** и авторизуйте подключение к Apify.
4. Чтобы использовать приложение в диалоге, нажмите **+** в чате, выберите **Developer mode** и затем **Apify**.

Подробнее: https://docs.apify.com/platform/integrations/mcp

---

[**Сделано с заботой**](https://apify.com/johnvc?fpr=9n7kx3)

*Используйте Yandex API для поисковых и SEO-задач с надёжными структурированными результатами.*

Last Updated: 2026.06.13
