"""
Google Trends module
"""

from google_trends.scraper import GoogleTrendsScraper
from google_trends.normalizer import normalize_trending_searches

__all__ = ["GoogleTrendsScraper", "normalize_trending_searches"] 