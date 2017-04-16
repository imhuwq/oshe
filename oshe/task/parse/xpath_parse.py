from lxml import etree
from oshe.task.parse import ParseBase


class XpathParse(ParseBase):
    def __init__(self):
        super(XpathParse, self).__init__()
        self.html = None

    def build_html(self, data):
        html = etree.HTML(data)
        if self.html is None:
            self.html = html
        return html

    def parse(self, data):
        raise NotImplementedError
