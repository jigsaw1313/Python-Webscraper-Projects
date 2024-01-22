# Books Scraper

This is a web scraping project using Scrapy and Selenium to extract book information from the [Books to Scrape](https://books.toscrape.com) website.

## Overview

This project uses Scrapy, a Python web scraping framework, along with Selenium for browser automation to scrape book details from the Books to Scrape website. It navigates through multiple pages and extracts information such as title, type, price, tax, stock, description, and UPC of each book.

## Prerequisites

Before running the scraper, ensure you have the following dependencies installed:

- Python
- Scrapy
- Selenium
- ChromeDriver

Install dependencies using:

```bash
pip install scrapy selenium
git clone https://github.com/jigsaw1313/Python-Webscraper-Projects
cd book_crawler
scrapy crawl books
```
The scraper will start navigating the website, extracting book details, and saving the data.

## Contributing
Contributions are welcome! Feel free to open issues or pull requests.
