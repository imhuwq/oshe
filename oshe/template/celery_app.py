from celery import Celery

from .demo.task.sample_task import CrawlTask, ParseTask, StoreTask

celery_app = Celery("tasks")


@celery_app.task
def crawl_task(target):
    crawler = CrawlTask()
    raw = crawler.run(target)
    parse_task.delay(raw)


@celery_app.task
def parse_task(raw):
    parser = ParseTask()
    results = parser.run(raw)
    for result in results:
        store_task.run(result)


@celery_app.task
def store_task(data):
    store = StoreTask()
    collection = "demo"
    identity = data.get("title")
    store.run(collection, identity, data)
