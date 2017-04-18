from celery.schedules import crontab


class AppBase:
    def __init__(self, name, celery_app, start_page, schedule=None):
        self.name = name

        queues = ["crawl", "parse", "store"]
        routes = {}
        for queue in queues:
            task_name = "%s.%s" % (self.name, queue)
            routes[task_name] = {"queue": queue}
        if celery_app.conf["CELERY_ROUTES"] is None:
            celery_app.conf["CELERY_ROUTES"] = {}
        celery_app.conf["CELERY_ROUTES"].update(routes)

        self.celery_app = celery_app
        self.routes = routes

        self.start_page = start_page

        if schedule is None:
            schedule = crontab(minute=0, hour=0)
        self.schedule = schedule

    def crawl(self, func):
        return self.celery_app.task(name="%s.crawl" % self.name, routing_key="crawl")(func)

    def parse(self, func):
        return self.celery_app.task(name="%s.parse" % self.name, routing_key="parse")(func)

    def store(self, func):
        return self.celery_app.task(name="%s.store" % self.name, routing_key="store")(func)

    def start(self, func):
        if self.celery_app.conf.beat_schedule is None:
            self.celery_app.conf.beat_schedule = {}
        self.celery_app.conf.beat_schedule["start_%s" % self.name] = {
            "task": "%s.start" % self.name,
            "schedule": self.schedule,
            "args": (),
            "options": {"queue": "crawl"}
        }

        return self.celery_app.task(name="%s.start" % self.name, routing_key="crawl")(func)
