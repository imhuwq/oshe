import json

from oshe.task.crawl.requests_crawl import RequestsCrawl
from oshe.task.parse.xpath_parse import XpathParse
from oshe.task.store.sa_store import SqlalchemyStore
from project.config import Config
from project.demo.model import Data


class CrawlTask(RequestsCrawl):
    """ class to customize your crawl task.
    The headers and cookies are defined as class attributes.
    The default method is "GET". If you want to change it, do as follows:
        1. override corresponding class function, post, option, etc.
        2. override the handler class function (the 'run' function), make it to call the desired method function.
    The crawl result should be sent to parse task to get the data you want.
    """
    headers = {
        'user-agent': 'User-Agent:Mozilla/5.0 (X11; Linux x86_64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/55.0.2883.75 Safari/537.36',
        'connection': 'keep-alive'
    }


class ParseTask(XpathParse):
    """ class to customize your parse task.
    To define your parse process, just override the class function 'parse'.
    The parse result could be sent to crawl task or store class to conduct further actions.
    """

    def parse_title(self):
        title = self.html.xpath("//div[@class='workIntro']/h1/text()")[0]
        return title

    def parse_work_show(self):
        image_urls = list(set(self.html.xpath("//div[@class='workShowLit']/ul/li/@data-img")))
        return image_urls

    def parse(self, data):
        result = {}
        self.build_html(data)

        title = self.parse_title()
        result["title"] = title

        image_urls = self.parse_work_show()
        result["images"] = image_urls

        return result


class StoreTask(SqlalchemyStore):
    """ class to customize your store task.
    To define your store process, override the class function 'store'.
    Store class is the final step of a normal crawl task chain.
    """
    db_uri = Config.DATABASE_URI
    db_table = Data

    def store(self, collection, identity, data):
        data = json.dumps(data.get("images"))
        row = self.db_table(collection=collection, identity=identity, data=data)
        self.session.add(row)
        self.session.commit()
