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

    def cut(self, string, head):
        _, ans = string.split(head)
        return ans.strip()

    def crawlData(self, response):
        races = response.css("table tr h2::text").getall()
        # print("race: ", races)
        times = response.css("table tr h2 span.join::text").getall()
        # print("time: ", times)
        cols = response.css("table tr td div.row-fluid div.span2 p span::text").getall()
        # print("col: ", cols)
        rows = response.css(".span5 table.table.table-bordered tbody tr td::text").getall()
        # print("row: ", rows)
        p = 0
        for i in range(0, len(races)):
            race = races[i][:-3]
            time, course = times[i].split(' ')
            distance = self. cut(cols[3*i], 'Distance:')
            runners = self.cut(cols[3*i+1], 'Runners:')
            favourite = self.cut(cols[3*i+2], 'Favourite:')
            visit = False
            while p < len(rows):
                placed = rows[p]
                card_no = rows[p + 1]
                name = rows[p + 2]
                if(visit and placed == '1st'): break
                visit = True
                p += 3
                yield {
                    "race": race,
                    "time": time,
                    "course": course,
                    "distance": distance,
                    "runners": runners,
                    "favourite": favourite,
                    "placed": placed,
                    "card_no": card_no,
                    "name": name
                }

    def parse(self, response):
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
                            yield response.follow(link, callback=self.crawlData)
                            yield link
                        pass    
                pass
            except:
                yield {"error": "error"}
            
        pass






