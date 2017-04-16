from oshe.task import TaskBase


class Crawl(TaskBase):
    headers = None
    cookies = None

    def __init__(self, headers=None, cookies=None, auth=None):
        if headers is not None:
            self.headers = headers

        if cookies is not None:
            self.cookies = cookies

        self.auth = auth

    def get(self, url, **kwargs):
        raise NotImplementedError

    def post(self, url, **kwargs):
        pass

    def option(self, url, **kwargs):
        pass

    def delete(self, url, **kwargs):
        pass

    def login(self, **kwargs):
        pass

    def logout(self):
        pass

    def run(self, *args, **kwargs):
        raise NotImplementedError
