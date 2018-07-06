import datetime
import uuid

from src.common.database import Database
from src.models.alerts import constants as Constants
from src.models.items.item import Item


class Alert(object):

    def __init__(self, user_email, price_limit, item_id = None, active=True, last_checked=None, _id=None):
        self.user_email = user_email
        self.price_limit = price_limit
        self.item_id = item_id
        self._id = uuid.uuid4().hex if _id is None else _id
        self.active = active
        self.last_checked = datetime.datetime.utcnow() if last_checked is None else last_checked

    def json(self):
        return {
            "user_email": self.user_email,
            "price_limit": self.price_limit,
            "item_id": self.item_id,
            "active": self.active,
            "last_checked" : self.last_checked,
            "_id": self._id
        }

    def save_to_mongo(self):
        Database.update(Constants.collection,{"_id":self._id},self.json())



    @classmethod
    def get_by_email(cls, user_email):
        return [cls(**i) for i in Database.find(Constants.collection, {"user_email":user_email})]

    @classmethod
    def get_by_itemid(cls, item_id):
        return cls(**Database.find_one(Constants.collection, {"item_id":item_id}))

    @classmethod
    def get_by_alertid(cls,_id):
        return cls(**Database.find_one(Constants.collection, {"_id":_id}))

    @staticmethod
    def get_itemobject_by_id(_id):
        return Item.get_by_id(_id)

    def get_item_price(self):
        return Item.get_by_id(self.item_id).price

"""Database.initialize()
alert = Alert("ganpat@gmail.com", 35.00, "1fc955f96bdf4ba79fd780f651d21047", True, datetime.datetime.utcnow())
alert.save_to_mongo()

print(Database.find("alerts", {"email":"ganpat@gmail.com"}))
print(Alert.get_by_email("ganpat@gmail.com")[1].user_email)
"""