"""
This spider function is same as books spider but we do not use selenium to parse pages.
we are going to navigate each page by using scrapy framework which is lot faster than 
selenium framework.
"""
import glob
import os
import scrapy
from scrapy.http import Request


class Books2Spider(scrapy.Spider):
    name = "books2"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    def parse(self, response):
        books = response.xpath("//h3/a/@href").extract()
        for book in books:
            absolute_url = response.urljoin(book)
            yield Request(absolute_url, callback=self.parse_book)
            
        # Process next page
        next_page_url = response.xpath("//a[text()='next']/@href").extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield Request(absolute_next_page_url, callback=self.parse)

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

    def close(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        os.rename(csv_file, 'output.csv')