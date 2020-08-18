import scrapy
pages=int(input('How much pages do you want to scrape?'))
numbers={'One':1,'Two':2,'Three':3,'Four':4,'Five':5}
class thespider(scrapy.Spider):
    name='books'
    start_urls=['http://books.toscrape.com/catalogue/page-{}.html'.format(i+1)for i in range(pages)]


    def parse(self,response):
        data={}
        body=response.css('ol.row')
        for book in body:
            for b in book.css('article.product_pod'):
                data['title']=b.css('a::attr(title)').getall()
                data['price']=b.css('div.product_price p.price_color::text').getall()
                data['Stock']=b.css('div.product_price p.instock.availability::text').getall()[1].strip()
                data['Star']=b.css('p::attr(class)').getall()[0][11:]
                data['Star']=[v for k,v in numbers.items() if k in data['Star']][0]
                yield data