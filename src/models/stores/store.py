import uuid

from src.common.database import Database
from src.models.stores import constants


class Store(object):
    def __init__(self, name, url_prefix, tag_name, query, header=None, _id=None):
        self.name = name
        self.url_prefix = url_prefix
        self.tag_name = tag_name
        self.query = query
        self._id = uuid.uuid4().hex if _id is None else _id
        self.header = header

    def save_to_mongo(self):
        Database.insert(constants.collection, self.json())

    def json(self):
        return {
            "name": self.name,
            "url_prefix": self.url_prefix,
            "tag_name": self.tag_name,
            "query": self.query,
            "_id": self._id,
            "header": self.header
        }

    @classmethod
    def all_stores(cls):
        return [cls(**i) for i in Database.find(constants.collection, {})]
