from .base import BaseCache
from .storage.mongodict import MongoDict, MongoPickleDict


class MongoCache(BaseCache):
    """MongoDB cache backend"""

    def __init__(self, db_name='requests-cache', **options):
        """
        :param db_name: database name (default: ``'requests-cache'``)
        :param connection: (optional) ``pymongo.Connection``
        """
        super().__init__(**options)
        self.responses = MongoPickleDict(db_name, 'responses', options.get('connection'))
        self.keys_map = MongoDict(db_name, 'urls', self.responses.connection)