from sqlalchemy import Column, Integer, String, Text

from oshe.task.store.sa_store import Model


class Data(Model):
    __tablename__ = 'data'
    id = Column(Integer, primary_key=True)
    collection = Column(String)
    identity = Column(String)
    data = Column(Text)
