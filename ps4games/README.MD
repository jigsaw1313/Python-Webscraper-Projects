# PlayStation Store Scraper

This Scrapy spider, named `Ps4Spider`, is designed to scrape data from the PlayStation Store website. The spider is specifically tailored to extract information about PS4 games from a paginated category.

## Usage

Before using the spider, make sure you have Scrapy installed:

```bash
pip install scrapy
```

Clone the repository:

```bash
git clone https://github.com/jigsaw1313/Python-Webscraper-Projects.git
```

Change into the project directory:

```bash
cd ps4games
```

Run the spider:

```bash
scrapy crawl ps4 -o output.json
```

This command will start the spider, and the extracted data will be saved in a file named `output.json`.

## Spider Details

### Spider Name

- **Name:** ps4

### Allowed Domains

- `store.playstation.com`

### Start URLs

- The spider starts with the URL: `https://store.playstation.com/en-us/category/85448d87-aa7b-4318-9997-7d25f4d275a4/1`

### Pagination

The spider iterates over multiple pages, with a total of 284 pages set by default. The spider extracts information about PS4 games, including title, URL, and price.

### Data Format

The extracted data is stored in a dictionary format with the following fields:

- `Title`: Title of the game.
- `URL`: URL of the game.
- `Price`: Price of the game.

### Pagination Logic

The spider includes logic to check whether it has reached the last page by comparing the current page number with the total number of pages. If the last page is reached, the spider stops crawling.

## Notes

- Be mindful of the terms of service of the website you are scraping, and ensure compliance with ethical guidelines.

- Use the extracted data responsibly and in accordance with applicable laws and regulations.

- Consider adding appropriate delays and handling anti-scraping mechanisms to avoid potential issues.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.