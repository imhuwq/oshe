from oshe.task.crawl.requests_crawl import RequestsCrawl
from oshe.task.parse.xpath_parse import XpathParse
from oshe.task.store.sa_store import SqlalchemyStore

from ...config import Config
from ..model.sample_model import Data

CrawlTask = type("AppCrawlTask", (RequestsCrawl,), {})
ParseTask = type('AppParseTask', (XpathParse,), {})
StoreTask = type('AppStoreTask', (SqlalchemyStore,), dict(db_url=Config.DATABASE_URI, db_table=Data))
