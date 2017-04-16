from celery.schedules import crontab


class TaskBase:
    def run(self, *args, **kwargs):
        raise NotImplementedError


class AppTaskChainMeta(type):
    def __new__(cls, cls_name, cls_bases, cls_dict):
        AppTaskChainMeta.check_class_integrity(cls_name, cls_dict)

        celery_app = cls_dict.get("celery_app")

        # update routes
        routes = cls_dict.get("routes")
        if celery_app.conf["CELERY_ROUTES"] is None:
            celery_app.conf["CELERY_ROUTES"] = {}
        celery_app.conf["CELERY_ROUTES"].update(routes)

        # setup schedule
        start_task = cls_dict.get("start", None)
        if start_task is not None and isinstance(start_task, staticmethod):
            if celery_app.conf.beat_schedule is None:
                celery_app.conf.beat_schedule = {}
            celery_app.conf.beat_schedule["start_%s" % cls_name] = {
                'task': 'demo.start',
                'schedule': crontab(minute=0, hour=0),
                'args': (),
                'options': {"queue": "crawl"}
            }
        return type.__new__(cls, cls_name, cls_bases, cls_dict)

    @staticmethod
    def check_class_integrity(cls_name, cls_dict):
        AppTaskChainMeta.check_fields(["app_name", "routes", "celery_app"], cls_name, cls_dict)

    @staticmethod
    def check_fields(fields, cls_name, cls_dict):
        for field in fields:
            value = cls_dict.get(field, None)
            if value is None:
                raise AttributeError("%s is not found in class %s" % (field, cls_name))
