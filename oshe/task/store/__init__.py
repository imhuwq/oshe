from oshe.task import TaskBase


class Store(TaskBase):
    def store(self, *args, **kwargs):
        raise NotImplementedError

    def run(self, *args, **kwargs):
        self.store(*args, **kwargs)
