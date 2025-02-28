# Google Trends Scraper

A Python tool for scraping and analyzing trending search data from Google Trends.

## Features

- Scrapes daily trending searches from Google Trends
- Supports multiple countries/regions
- Normalizes search data into structured JSON format
- Command-line interface for easy usage
- Headless browser automation using Selenium

## Installation

1. Clone the repository
2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the scraper using the CLI:

```bash
google-trends [COUNTRY] [OPTIONS]
```

Arguments:
- `COUNTRY`: Two-letter country code (e.g., US, UK, DE)

Options:
- `-o, --output`: Output file name (default: trends.json)

Example:
```bash
google-trends US -o us_trends.json
```

## Output Format

The scraper outputs normalized JSON data with the following structure:

```json
[
  {
    "lang": "us",
    "createdAt": "2024-03-21T10:30:00",
    "title": "Example Search Term",
    "searchCount": 50000,
    "trendPercentage": 150,
    "timing": {
      "hoursAgo": 2,
      "isActive": true,
      "duration": 0
    }
  }
]
```

## Project Structure

- `google_trends/`: Main package directory
  - `scraper.py`: Contains the GoogleTrendsScraper class for web scraping
  - `normalizer.py`: Data normalization utilities
- `cli.py`: Command-line interface implementation
- `setup.py`: Package configuration and dependencies