# coding: utf-8 
"""
Created on Tue Sep  5 13:42:26 2017

@author: C
"""
from lxml import html
import requests

i = 0
counts = 0
while i <= 250:
    
    url = 'https://movie.douban.com/top250?start='+str(i)+'&filter='
    i += 25
    r = requests.get(url).content

    sel = html.fromstring(r)
    
    title = sel.xpath('//h1/text()')
    
    texts = sel.xpath('//div[@class="info"]')
    
    
    for text in texts:
        movie_name = text.xpath(
                'div[@class="hd"]/a/span[@class="title"]/text()')[0]
        
        lists = text.xpath(
                'div[@class="bd"]/p[@class=""]/text()')
        directors_actors_1 = lists[0].replace(' ','').replace('\n','')
        
        details =lists[1].replace(' ','').replace('\n','').split('/')
        
        year = details[0]
        
        countries = details[1]
        
        types = details[2]
        
        counts += 1
        
        p = text.xpath('div[@class="bd"]/div[@class="star"]/span/text()')
        
        rate = p[0]
        
        comments = p[1]
        

        with open('top250.txt','a',encoding='utf-8') as f:
            f.write('''
top%s
片名:%s
评分:%s %s
年份:%s
国家:%s
类型:%s
%s
                    ''' 
               % (counts,movie_name,rate,comments,
               year,countries,types,directors_actors_1))
            
            f.write('==========================================================================\n')
            