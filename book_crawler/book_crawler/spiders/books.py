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
        self.s = Service("chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.s)
        self.driver.get("https://books.toscrape.com")
        
        
        select = Selector(text=self.driver.page_source)
        books = select.xpath("//h3/a/@href").extract()
        for book in books:
            url = f"https://books.toscrape.com/{book}"
            yield Request(url, callback=self.parse_book)
            
        while True:
            try:
                
                next_page = WebDriverWait(self.driver, 2).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[text()='next']")))
                time.sleep(2)
                self.logger.info("Seelping for 2 seconds...")
                next_page.click()
                
                select = Selector(text=self.driver.page_source)
                books = select.xpath("//h3/a/@href").extract()
                for book in books:
                    url = "https://books.toscrape.com/catalogue/" + book
                    yield Request(url, callback=self.parse_book)
                    
            except NoSuchElementException as e:
                self.logger.info('No More Pages to Load....')
                self.driver.quit()
                break
            
    def parse_book(self, response):
        title = response.xpath("//h1/text()").get()
        type = response.xpath("//tbody/tr[2]/td/text()").get()
        price = response.xpath("//div[@class='col-sm-6 product_main']/p[1]/text()").get()
        tax = response.xpath("//th[text()='Tax']/following-sibling::td/text()").get()
        stock = response.xpath("(//div[@class='col-sm-6 product_main']//p)[2]/text()[2]").get()
        description = response.xpath("//article[@class='product_page']/p/text()").get()
        upc = response.xpath("//tbody/tr/td/text()").get()
        
        yield {
            'Title': title,
            'Type': type,
            'Price': price,
            'Tax': tax,
            'Stock': stock,
            'Description': description,
            'UPC': upc
        }
