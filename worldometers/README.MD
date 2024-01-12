# Countries-Population

## Countries Population Scraper

This project is a web scraper built using Scrapy, a popular web crawling and web scraping framework for Python. The purpose of this scraper is to extract population data by country from the Worldometer website.

### Installation

Before using the scraper, make sure you have Python and Scrapy installed. You can install Scrapy using the following command:

```bash
pip install scrapy
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/jigsaw1313/Python-Webscraper-Projects/tree/master/worldometers
```

2. Change into the project directory:

```bash
cd worldometers
```

3. Run the scraper:

```bash
scrapy crawl countries
```

4. Creating Dataset

```bash
scrapy crawl countries -o <FILENAME.CSV>
```

This command will start the scraper, and the extracted data will be saved in a file.

### Project Structure

The main components of the project are as follows:

- **countries.py**: This file contains the Scrapy spider named `CountriesSpider`, which is responsible for crawling the Worldometer website and extracting population data.

### Spider Overview

- **Name:** countries
- **Allowed Domains:** www.worldometers.info
- **Start URLs:** https://www.worldometers.info/world-population/population-by-country/

#### `parse` Method

This method is responsible for extracting links to individual country pages and initiating the parsing of each country's population data.

#### `parse_country` Method

This method extracts population data for a specific country, including the country's name, year, and population.

### Data Format

The extracted data is stored in a dictionary format with the following fields:

- `country_name`: Name of the country.
- `year`: Year for the population data.
- `population`: Population of the country in the specified year.

### Notes

- Please be respectful and responsible when scraping data from websites. Check the terms of service of the website you are scraping and ensure compliance with ethical guidelines.

- Use the extracted data responsibly and in accordance with applicable laws and regulations.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.