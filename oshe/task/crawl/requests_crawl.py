import requests

from oshe.task.crawl import Crawl


class RequestsCrawl(Crawl):
    def __init__(self, headers=None, cookies=None, auth=None):
        super(RequestsCrawl, self).__init__(headers, cookies, auth)
        self.requests = requests

    def get(self, url, **kwargs):
        headers = kwargs.pop('headers', None) or self.headers

        cookies = kwargs.pop('cookies', None) or self.cookies

        raw = self.requests.get(url, headers=headers, cookies=cookies, **kwargs).text
        return raw

    def run(self, url, *args, **kwargs):
        return self.get(url, **kwargs)
