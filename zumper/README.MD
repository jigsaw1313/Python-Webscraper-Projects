# Zumper House Scraper

This is a web scraper built using Scrapy and Selenium to extract information about houses for rent from Zumper. It scrapes details such as location, status, URL, address, utilities, number of bathrooms, number of bedrooms, and rent in USD. The scraper also supports pagination to scrape multiple pages of listings.

## Prerequisites

- Python 3.x
- Scrapy
- Selenium
- Chrome WebDriver

## Installation

1. Clone the repository:
```bash
git clone https://github.com/jigsaw1313/Python-Webscraper-Projects
cd zumper
```

2. Install dependencies:
```bash
pip install scrapy selenium
```

3. Download and install Chrome WebDriver from [here](https://chromedriver.chromium.org/downloads). Make sure to set the correct path to the Chrome WebDriver in the scraper code.

## Usage

Run the scraper using the following command:

```bash
scrapy crawl zumper_house -o output.csv
```

This will start the scraper, and the scraped data will be saved to the `output.csv` file in CSV format.

## Configuration

You may need to adjust the following configurations in the code:

- `chrome_path`: Set the path to the Chrome WebDriver executable.
- `allowed_domains`: Update the domain name of the website if necessary.
- `start_urls`: Provide the starting URL of the Zumper listings.

## Customization

You can customize the scraper behavior by modifying the following methods:

- `parse`: Defines how to extract data from the website. You can adjust the XPath expressions to match the structure of the website if it changes.
- `closed`: Performs cleanup tasks when the scraper is finished. You can add additional cleanup tasks if needed.

