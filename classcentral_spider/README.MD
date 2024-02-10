# ClassCentral Scraper

This is a web scraper built using Scrapy framework in Python to extract information about online courses from Class Central website (www.classcentral.com). The scraper collects data such as course name, provider, workload, start date, rating, reviews, price, description, and URL.

## Installation

To run this scraper locally, you need to have Python and Scrapy installed on your system. You can install Scrapy using pip:

```
pip install scrapy
```

Clone this repository to your local machine:

```
git clone https://github.com/jigsaw1313/Python-Webscraper-Projects
cd classcentral_spider
```

## Usage

To start scraping, run the following command from the project directory:

```
scrapy crawl classcentral
```

You can specify a specific subject to scrape by passing it as an argument:

```
scrapy crawl classcentral -a subject="subject-name"
```

Replace `"subject-name"` with the name of the subject you want to scrape.

The scraped data will be saved in a CSV file named `courses.csv` in the project directory.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

