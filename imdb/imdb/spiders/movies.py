import scrapy


class MoviesSpider(scrapy.Spider):
    name = "movies"
    allowed_domains = ["imdb.com"]
    start_urls = ["https://www.imdb.com/chart/top"]
    
    def start_requests(self):
        yield scrapy.Request(url="https://www.imdb.com/chart/top",
                                    callback=self.parse, 
                                    headers={
                                        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
                                    })
    

    def parse(self, response):
        for movie in response.xpath("//ul[@class='ipc-metadata-list ipc-metadata-list--dividers-between sc-71ed9118-0 kxsUNk compact-list-view ipc-metadata-list--base']/li"):
                    yield {
            'Title': (movie.xpath(".//a[@class='ipc-title-link-wrapper']/h3/text()").get()).split(". ", 1)[1] ,
            'Year': movie.xpath(".//span[1][@class='sc-935ed930-8 iLiQCS cli-title-metadata-item']/text()").get(),
            'Duration': movie.xpath(".//span[2][@class='sc-935ed930-8 iLiQCS cli-title-metadata-item']/text()").get(),
            'ParentGuide': movie.xpath(".//span[3][@class='sc-935ed930-8 iLiQCS cli-title-metadata-item']/text()").get(),
            'Rating': movie.xpath(".//span[@class='ipc-rating-star ipc-rating-star--base ipc-rating-star--imdb ratingGroup--imdb-rating']/text()").get(),
            'Reviews' : movie.xpath(".//span[@class='ipc-rating-star--voteCount']/text()[2]").get()
        }
        
