import scrapy
import datetime
from dateutil import parser
import logging

logging.info("sdfasdfasdf")
class PlacePotSpider(scrapy.Spider):
    name = 'placepot'
    start_urls = ['https://www.scoop6.co.uk/placepot-results/']

    def __init__(self, st, ed, course):
        print("++++++++", st, ed, course)
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

        
    def parse(self, response):
        for items in response.css('.span10 p'):
            date = self.getDate(items.getall()[0])
            if date == False:
                continue

            if date >= self.startDate and date <= self.endDate:

                courses = items.css('a')
                for course in courses:
                    text = course.css('::text').get()
                    if text == self.course:
                        print("=============>", course.attrib['href'])
                        yield course.attrib['href']
                    pass    
            pass
        pass






