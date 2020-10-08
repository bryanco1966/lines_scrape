import scrapy

class LinesSpider(scrapy.Spider):
    name = "lines"

    def start_requests(self):
        urls = [
            'https://sports.intertops.eu/en/Bets/American-Football/NFL-Lines/1018'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        item = GetLinesItem()
        item['home_team']= response.css('div.ustop::text').getall()
        item['away_team']= response.css('div.ustop::text').getall()
        item['home_line']= response.css('span.fleft::text').getall()
        item['money_line'] = response.css('span.odds::text').getall()
        return item
