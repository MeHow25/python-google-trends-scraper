from setuptools import setup, find_packages

setup(
    name="google_trends_scraper",
    version="0.1.0",
    description="A tool for scraping Google Trends data",
    packages=find_packages(),
    install_requires=[
        "requests>=2.25.0",
        "pandas>=1.2.0",
        "beautifulsoup4>=4.9.0",
    ],
    entry_points={
        'console_scripts': [
            'google-trends=cli:main',
        ],
    },
    python_requires=">=3.6",
) 