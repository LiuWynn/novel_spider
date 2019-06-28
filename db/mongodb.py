# !/usr/bin/python
# -*- coding: UTF-8 -*-

from db.database import Database
from pymongo import MongoClient
from config.dbs import MONGO_HOST, MONGO_PORT, MONGO_DB


class MongoDB(Database):
    """
    MongoDB 操作类
    """
    def __init__(self, collection_name):
        """
        初始化 MongoDB 连接参数
        :param collection_name: 保存到哪个集合
        """
        super(MongoDB, self).__init__()
        self._host = MONGO_HOST
        self._port = MONGO_PORT
        self._client = MongoClient(host=self._host, port=self._port)
        self._db = self._client[MONGO_DB]
        self._collection = self._db[collection_name]

    def __del__(self):
        """析构函数 释放资源"""
        self._client.close()

    def add(self, data):
        print(data)
        return self._collection.insert_one(data).inserted_id

    def find(self, _id):
        return self._collection.find({'_id': _id})

    def update(self, _id, data):
        self._collection.update_one({'_id': _id}, {'$set': data})

    def append(self, _id, data):
        self._collection.update({'_id': _id}, {'$push': data})
