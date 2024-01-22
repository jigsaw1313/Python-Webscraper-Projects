import scrapy
import time

from scrapy.selector import Selector
from scrapy.http import Request

from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def start_requests(self):
        # Initialize ChromeDriver and open the main page
        self.s = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://books.toscrape.com")
        
        # Extract book URLs from the main page and send requests to parse_book callback
        select = Selector(text=self.driver.page_source)
        books = select.xpath("//h3/a/@href").extract()
        for book in books:
            url = f"https://books.toscrape.com/{book}"
            yield Request(url, callback=self.parse_book)
        
        # Continuously navigate to the next page and extract book URLs until there are no more pages
        while True:
            try:
                
                next_page = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='next']")))
                time.sleep(2)
                self.logger.info("Seelping for 2 seconds...")
                next_page.click()
                
                # Extract book URLs from the current page and send requests to parse_book callback
                select = Selector(text=self.driver.page_source)
                books = select.xpath("//h3/a/@href").extract()
                for book in books:
                    url = "https://books.toscrape.com/catalogue/" + book
                    yield Request(url, callback=self.parse_book)
                    
            except NoSuchElementException as e:
                self.logger.info('No More Pages to Load....')
                self.driver.quit() # Close the browser when there are no more pages
                break
            
    def parse_book(self, response):
        # Extract book details from the book page
        title = response.css("h1::text").extract_first()
        price = response.xpath("//*[@class='price_color']/text()").extract_first()
        book_type = response.xpath("//th[text()='Product Type']/following-sibling::td/text()").extract_first()
        
        img_url = response.xpath("//img/@src").extract_first()
        img_url = img_url.replace("../..", "http://books.toscrape.com")
        
        rating = response.xpath("//*[contains(@class, 'star-rating')]/@class").extract_first()
        rating = rating.replace("star-rating", "")
        
        description = response.xpath("//article[@class='product_page']/p/text()").get()
        tax = response.xpath("//th[text()='Tax']/following-sibling::td/text()").extract_first()
        upc = response.xpath("//th[text()='UPC']/following-sibling::td/text()").extract_first()
        stock = response.xpath("//th[text()='Availability']/following-sibling::td/text()").get()
        
        # Yield the extracted data as a dictionary
        yield {
            'Title': title,
            'Image_URL': img_url,
            'Book Type': book_type,
            'Price': price,
            'Tax': tax,
            'Description': description,
            'UPC': upc,
            'Stock': stock 
        }
