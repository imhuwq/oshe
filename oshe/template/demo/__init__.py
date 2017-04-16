from oshe.task import AppTaskChainMeta

from project.celery_app import celery_app
from project.demo.task.sample_task import CrawlTask, ParseTask, StoreTask


class DemoTaskChain(metaclass=AppTaskChainMeta):
    app_name = "demo"
    start_page = "http://gallery.artron.net/works/3372_w515366.html"
    routes = {
        "demo.crawl": {"queue": "crawl"},
        "demo.parse": {"queue": "parse"},
        "demo.store": {"queue": "store"}
    }
    celery_app = celery_app

    @staticmethod
    @celery_app.task(name="demo.crawl", routing_key="crawl")
    def crawl(target):
        crawler = CrawlTask()
        raw = crawler.run(target)
        DemoTaskChain.parse.delay(raw)

    @staticmethod
    @celery_app.task(name="demo.parse", routing_key="parse")
    def parse(raw):
        parser = ParseTask()
        results = parser.run(raw)
        DemoTaskChain.store.delay(results)

    @staticmethod
    @celery_app.task(name="demo.store", routing_key="store")
    def store(data):
        store = StoreTask()
        collection = "demo"
        identity = data.get("title")
        store.run(collection, identity, data)

    @staticmethod
    @celery_app.task(name="demo.start", routing_key="crawl")
    def start():
        if DemoTaskChain.start_page is not None:
            DemoTaskChain.crawl.delay(DemoTaskChain.start_page)
