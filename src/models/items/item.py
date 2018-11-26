import datetime
import uuid
import re
import requests
from bs4 import BeautifulSoup

from src.common.database import Database
from src.models.items import constants as Constants
from src.models.stores.store import Store


class Item(object):
    def __init__(self, name, url, price=None, _id=None):
        self.name = name
        self.url = url
        self.price = price if price is not None else Item.load_price(url)
        self._id = uuid.uuid4().hex if _id is None else _id

    def json(self):
        return {
            "name": self.name,
            "url": self.url,
            "price": self.price,
            "_id": self._id

        }

    def save_to_mongo(self):
        Database.insert(Constants.collection, self.json())

    @classmethod
    def get_by_id(cls, _id):
        return cls(**Database.find_one(Constants.collection, {"_id": _id}))

    @staticmethod
    def load_price(url):
        if url[4]=='s':
            temp=url[:4]
            url=temp+url[5:]


        stores = Store.all_stores()
        for store in stores:
            reg = re.compile(store.url_prefix + "*")
            found = re.match(reg, url)
            if found is not None:
                request = requests.get(url, verify=False, headers = store.header)
                content = request.content
                soup = BeautifulSoup(content, "html.parser")
                find = soup.find(store.tag_name, store.query)
                if find is None:
                    return False
                return (find.text.strip()[1:])
        return False


