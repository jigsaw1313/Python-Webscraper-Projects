import os
import glob
import csv
import scrapy
from pyodbc import connect
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.selector import Selector
from urllib.parse import urljoin


class JobsSpider(scrapy.Spider):
    name = "zumper_house"
    allowed_domains = ["www.zumper.com"]
    start_urls = ["https://www.zumper.com/apartments-for-rent/toronto-on/cheap?bathrooms-range=2"]

    # Initialize init method.
    def __init__(self, *args, **kwargs):
        super(JobsSpider, self).__init__(*args, **kwargs)
        self.chrome_path = "PATH_TO_CHROMEDRIVER" # Put path into chromedriver
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless") # set selenium in headless mode.
        self.service = Service(self.chrome_path)  # Path of chromedriver
        self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

    def parse(self, response):
        self.driver.get(response.url)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//div[@class='css-8a605h']"))) # Waiting time to load more content from website.
        sel = Selector(text=self.driver.page_source)
        listings = sel.xpath("//div[@class='css-8a605h']") # Container of listings
        
        # Iterate over listings to find houses and scraper their data.
        for listing in listings:
            yield {
                "Location" : listing.xpath(".//section/div/div[2]/div/div[2]/div/a/text()").extract_first(),
                "Status": listing.xpath(".//section/div/div[2]/div[1]/div[1]/div/div/p/text()").extract_first(),
                "URL": urljoin(response.url, listing.xpath(".//section/div/div[2]/div/div[2]/div/a/@href").extract_first()),
                "Address" : listing.xpath(".//section/div/div[2]/div/div[2]/div/div[1]/p[1]/text()").extract_first(),
                "Utilities": listing.xpath(".//section/div/div[2]/div/div[2]/div/div[2]/p/text()")[0:3].extract(),
                "Bathroom": listing.xpath(".//section/div/div[2]/div/div[2]/div[2]/div[1]/p[2]/text()").extract(),
                "Bedroom": listing.xpath(".//section/div/div[2]/div/div[2]/div[2]/div[1]/p[1]/text()").extract(),
                "Rent_USD": listing.xpath(".//section/div/div[2]/div/div[2]/div[2]/div[2]/p/text()").extract(),
            }

        # Next Page
        next_button = response.xpath("//a[@class='chakra-button css-1ta7ioi']/@href").extract_first()
        if next_button:
            next_url = urljoin(response.url, next_button)
            yield scrapy.Request(next_url, callback=self.parse)

    def closed(self, reason):
        csv_file = max(glob.iglob('*.csv'), key=os.path.getctime)
        
        
        # SqlServer Connection. You may need to configure below variables as per 
        # Your local machine's sql server configuration.
        db = connect(Driver='{ODBC Driver 18 for SQL Server}',
                        Server='<SQL_SERVER_ADDRESS',
                        Database= "<DB_NAME>",
                        Trusted_Connection='yes',
                        TrustServerCertificate='yes')
        # Creating Cursor
        cursor = db.cursor()
        
        with open(csv_file, 'r') as file:
            csv_data = csv.reader(file)
            row_count = 0
            for row in csv_data:
                if row_count != 0:
                    cursor.execute("""INSERT INTO zumper(Location, Status, URL, Address,Utilities, 
                                    Bathroom, Bedroom, Rent) VALUES(?, ?, ?, ?, ?, ?, ?, ?)""", row)
                row_count += 1
        db.commit()
        cursor.close()
        self.driver.quit()