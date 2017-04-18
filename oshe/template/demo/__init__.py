from project.demo.app import DemoApp
from project.demo.task import CrawlTask, ParseTask, StoreTask
from project.celery_app import celery_app

demo = DemoApp("demo", celery_app, "http://gallery.artron.net/works/3372_w515366.html")


@demo.crawl
def crawl(target):
    crawler = CrawlTask()
    raw = crawler.run(target)
    parse.delay(raw)


@demo.parse
def parse(raw):
    parser = ParseTask()
    results = parser.run(raw)
    store.delay(results)


@demo.store
def store(data):
    storer = StoreTask()
    collection = "demo"
    identity = data.get("title")
    storer.run(collection, identity, data)


@demo.start
def start():
    crawl.delay(demo.start_page)
