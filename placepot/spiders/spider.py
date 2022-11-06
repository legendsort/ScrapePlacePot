import scrapy
import datetime
from dateutil import parser
import logging

logging.info("sdfasdfasdf")
class PlacePotSpider(scrapy.Spider):
    name = 'placepot'
    start_urls = ['https://www.scoop6.co.uk/placepot-results/']

    def __init__(self, st, ed, course):
        self.startDate = parser.parse(st)
        self.endDate = parser.parse(ed)
        self.course = course
        pass

    def getDate(self, string):
        dateString = string.split(":")[0][3:]
        try:
            return parser.parse(dateString)
        except:
            return False

    def getData(self, response):
        # race response.css("table tr h2::text").get()
        # time & course response.css("table tr h2 span.join::text").get() 
        # distancer, runners, favourite, response.css("table tr td div.row-fluid div.span2 p span::text")
        # data response.css(".span5 table tbody tr td::text")  
        yield {
            "here": "here"
        }
    def parse(self, response):
        print("-=-=-================>")
        for items in response.css('.span10 p'):
            try: 
                date = self.getDate(items.getall()[0])
                if date == False:
                    continue

                if date >= self.startDate and date <= self.endDate:

                    courses = items.css('a')
                    for course in courses:
                        text = course.css('::text').get()
                        if text == self.course:
                            link = course.attrib['href']
                            print("=============>", link)
                            yield response.follow(link, callback=self.getData)
                            yield {"link": link}
                        pass    
                pass
            except:
                yield {"error": "error"}
            
        pass






