import scrapy


class Ps4Spider(scrapy.Spider):
    name = "ps4"
    allowed_domains = ["store.playstation.com"]
    start_urls = ["https://store.playstation.com/en-us/category/85448d87-aa7b-4318-9997-7d25f4d275a4/1"]
    total_pages = 284

    def parse(self, response):
        for game in response.xpath("//ul[@class='psw-grid-list psw-l-grid']/li"):
            yield {
                'Title' : game.xpath(".//span[@class='psw-t-body psw-c-t-1 psw-t-truncate-2 psw-m-b-2']/text()").get(),
                'URL' : response.urljoin(game.xpath(".//div/a/@href").get()),
                'Price' : game.xpath(".//div[@class='psw-fill-x psw-price psw-l-inline psw-l-line-left-top']/div/span/text()").get()
            }
            
        # Extract the current page number
        current_page_number = int(response.url.split('/')[-1])
        
        # Check if we have reached the total number of pages
        if current_page_number >= self.total_pages:
            self.log(f'Reached the last page. Stopping the spider. (Total pages: {self.total_pages})')
            return
        # Construct the URL for the next page
        next_page_number = current_page_number + 1
        next_page_link = f"https://store.playstation.com/en-us/category/85448d87-aa7b-4318-9997-7d25f4d275a4/{next_page_number}"

        # Follow the link to the next page and continue parsing
        yield scrapy.Request(url=next_page_link, callback=self.parse)