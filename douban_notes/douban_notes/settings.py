# Scrapy settings for douban_notes project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'douban_notes'

SPIDER_MODULES = ['douban_notes.spiders']
NEWSPIDER_MODULE = 'douban_notes.spiders'

DOWNLOAD_DELAY = 0.25
RANDOMIZE_DOWNLOAD_DELAY = True
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.95 Safari/537.36'

ITEM_PIPELINES = [
          'scrapymongodb.MongoDBPipeline',
          ]

MONGODB_SERVER = '172.16.121.236'
MONGODB_PORT = 27017
MONGODB_DB = 'scrapy'
MONGODB_COLLECTION = 'items'
MONGODB_UNIQ_KEY = 'nid'
MONGODB_ITEM_ID_FIELD = '_id'
MONGODB_SAFE = True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban_notes (+http://www.yourdomain.com)'
