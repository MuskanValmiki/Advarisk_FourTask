# here we store title,posted no,and discription in saperate file .
    
from scrapy import Request,Spider
import scrapy
import json,csv

class NewsSpider(scrapy.Spider):
    name = "india_news"

    def start_requests(self):
        urls = [
            'https://www.ndtv.com/india'
        ]
        for url in urls:
            
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        
        news_title=response.xpath('/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div/div/h2/a/text()').extract()
        posted_on=response.xpath('/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div/div[2]/span/text()').extract()
        discription=response.xpath('/html/body/div[2]/div/div/section/div[3]/article/div/div/div/div[1]/div/div/div[2]/p/text()').extract()
                
        with open('news_title.json','w') as f:
           json.dump(news_title,f,indent=4)
    
        with open('news_title.csv','w') as f:
            for news in news_title:
                f.write(news)
                f.write("\n")
        
        with open('posted_on.json','w') as f1:
            json.dump(posted_on,f1,indent=4)
            
        with open('posted_on.csv','w') as f1:
            for post in posted_on:
                f1.write(post)
                f1.write(post)
                
        with open('discription.json','w') as f2:
            json.dump(discription,f2,indent=4) 
              
        with open('discription.csv','w') as f2:
            for disc in discription:
                f2.write(disc)
                f2.write("\n")
                     
# here we are storing data in one csv file not saperate.