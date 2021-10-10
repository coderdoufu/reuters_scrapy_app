# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapydemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    pass


class ScrapySectionCategoriesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    section_name = scrapy.Field()
    section_cats = scrapy.Field()
    section_cats_url = scrapy.Field()
