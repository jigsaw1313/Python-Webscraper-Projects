from scrapy import Spider
from scrapy.http import Request


class ClasscentralSpider(Spider):
    name = "classcentral"
    allowed_domains = ["www.classcentral.com"]
    start_urls = ["https://www.classcentral.com/subjects"]

    # Initilizing init method.
    def __init__(self, subject=None):
        self.subject = subject

    def parse(self, response):
        """
        Parses the response from the main subjects page.
        Args:
            response (scrapy.http.Response): The response object containing the main subjects page.
        Yields:
            scrapy.Request: A request to scrape the subject-specific page for each subject found.
        """

        # If a specific subject is specified, extract the URL related to that subject
        if self.subject:
            subject_url = response.xpath("//li[a[contains(., '" + self.subject + "')]]/a/@href").extract_first()
            absolute_subject_url = response.urljoin(subject_url)
            # Send a request to scrape the subject-specific page
            yield Request(absolute_subject_url,
                            callback=self.parse_subject)
        else:
            self.log('Scraping All Subjects')
            # If no specific subject is specified, extract URLs for all subjects
            subjects = response.xpath("//li/a[@class='no-underline filter-tabs__tab-control']/@href").extract()
            for subject in subjects:
                absolute_subject_url = response.urljoin(subject)
                # Send a request to scrape the subject-specific page for each subject
                yield Request(absolute_subject_url,
                            callback=self.parse_subject)

    def parse_subject(self, response):
        # Recording subject of each scraped course information.
        subject_name = response.xpath("//h1/text()").extract_first()
        
        # this variable includes the course content.
        courses =  response.xpath("//li[@itemprop='itemListElement']")
        
        # Iterate over all courses and scrape below information by using their xpath selector.
        for course in courses:          
            course_name = course.xpath(".//h2[@itemprop='name']/text()").extract_first()
            producer = course.xpath(".//img[@class='block']/@title").extract_first()
            provider = course.xpath("//a[@aria-label='Provider']/text()").extract_first()
            workload_duration = course.xpath('.//span[@aria-label="Workload and duration"]/text()').extract_first()
            start_date = course.xpath('.//span[@aria-label="Start date"]/text()').extract_first()
            course_rate = course.xpath(".//a[@class='hover-underline color-charcoal text-3 margin-left-xsmall line-tight']/text()").extract_first()
            reviews = course.xpath(".//span[@class='text-3 color-gray margin-left-xxsmall']/text()").extract_first()
            price = course.xpath('.//span[@aria-label="Pricing"]/text()').extract_first()
            description = course.xpath(".//a[@class='color-charcoal block hover-no-underline break-word']/text()").extract_first()
            course_url = response.urljoin(course.xpath(".//a[@itemprop='url']/@href").extract_first())
            
            # Check if variables are not None before calling strip()
            if reviews:
                reviews = reviews.strip()
            if provider:
                provider = provider.strip()
            if workload_duration:
                workload_duration = workload_duration.strip()
            if start_date:
                start_date = start_date.strip()
            if course_rate:
                course_rate = course_rate.strip()
            if price:
                price = price.strip()
            if description:
                description = description.strip()
                    
            
            # Yielding scraped information.
            yield {
                'Subject_Name': subject_name,
                'Course_Name': course_name,
                'Producer': producer,
                'Provider': provider,
                'Workload': workload_duration,
                'Start_Date': start_date,
                'Rating': course_rate,
                'Reviews': reviews,
                'Price': price,
                'URL': course_url,
                "Description": description
            }

        # Handling pagagation by using xpath selector of next page 'href' property.
        next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
        if next_page:
            next_page_url = response.urljoin(next_page)
            yield Request(next_page_url, callback=self.parse_subject)
