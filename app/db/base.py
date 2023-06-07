__author__ = "AminHZDEV"
__copyright__ = "Copyright 2023"
__credits__ = []
__license__ = "MIT"
__version__ = "1.0.0"
__maintainer__ = ""
__email__ = "amin.hasan.zarei@gmail.com"
__status__ = "Production"

import pymongo
from utils.my_log import MyLog


class Base(MyLog):
    """
    this class is base of database class and create db if it does not exist
    """

    def __init__(self):
        super().__init__()
        self._mongo_client = pymongo.MongoClient(self.dotenv_values.get("MONGO_URL"))
        self._my_db = self._mongo_client[self.dotenv_values.get("DB_NAME")]

    @property
    def my_db(self):
        return self._my_db

    @my_db.setter
    def my_db(self, a):
        self._my_db = a

    @property
    def mongo_client(self):
        return self._mongo_client

    @mongo_client.setter
    def mongo_client(self, a):
        self._mongo_client = a

    def create_collection(self, name: str = "") -> bool:
        """
        this method used to create collection in mongodb
        :param name:
        :return:
        """
        try:
            self.my_db[name]
            return True
        except Exception as e:
            self.log.error(e)
            return False
