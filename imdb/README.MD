# IMDb Top 250 Movies Scraper

This Scrapy spider extracts information from the IMDb Top 250 Movies list.

## Overview

This spider scrapes the IMDb Top 250 Movies list to extract the following information for each movie:

- Title
- Year
- Duration
- Parental Guide
- Rating
- Reviews Count

## Requirements

- Python 3
- Scrapy

## Installation

```bash
git clone https://github.com/your-username/imdb-top-250-scraper.git
cd imdb-top-250-scraper
scrapy crawl movies -o output.json
```
