from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from douban_notes.items import DoubanNotesItem
import re


class NotesSpider(CrawlSpider):
    name = 'notes'
    allowed_domains = ['www.douban.com']
    start_urls = ['http://www.douban.com/']

    rules = (
        Rule(SgmlLinkExtractor(allow=[r'note/\d+/$'], deny=r'accounts/'), callback='parse_note'),
    )

    def parse_start_url(self, response):
        for x in xrange(100000000, 999999999):
        #for x in xrange(295886140, 295886155): #test
            yield Request('http://www.douban.com/note/%s/' % x)

    def parse_note(self, response):
        hxs = HtmlXPathSelector(response)
        i = DoubanNotesItem()
        i['nid'] = response.url.split('/')[-2]
        owner_html = hxs.select('//*[@id="db-usr-profile"]/div[1]/a').extract()[0]
        i['owner'] = re.search('/people/(.+)/', owner_html).groups()[0]
        i['title'] = hxs.select('//*[@id="note-%s"]/div[1]/h1/text()'% i['nid']).extract()[0]
        i['url'] = response.url
        content = ''
        for c in hxs.select('//*[@id="link-report"]/text()').extract():
            content += c
        i['content'] = content

        for candidate in hxs.re('http://www.douban.com/note/\d+/'):
            if i['nid'] != re.findall('http://www.douban.com/note/(\d+)/', candidate)[0]:
                yield Request(re.findall('http://www.douban.com/note/\d+/', candidate)[0])

        yield i
