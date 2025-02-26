#!/usr/bin/env python3

import click
import json
from pathlib import Path
from google_trends.scraper import GoogleTrendsScraper
from google_trends.normalizer import normalize_trending_searches

@click.command()
@click.argument('country')
@click.option('-o', '--output', default='trends.json', help='Output file name')
def main(country: str, output: str):
    """CLI tool to scrape Google Trends data"""
    try:
        click.echo(f"Scraping Google Trends data for {country}...")
        
        scraper = GoogleTrendsScraper(country)
        raw_trends = scraper.scrape()
        
        # Normalize the trends data
        normalized_trends = normalize_trending_searches(raw_trends, country.lower())
        
        output_path = Path.cwd() / output
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(normalized_trends, f, indent=2, ensure_ascii=False)
        
        click.echo(f"Successfully saved normalized trends to {output_path}")
    except Exception as error:
        click.echo(f"Error: {str(error)}", err=True)
        raise click.Abort()

if __name__ == '__main__':
    main() 