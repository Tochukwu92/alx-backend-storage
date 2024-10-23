#!/usr/bin/env python3


'''creat a redis database'''


import redis
import uuid
from typing import Union


class Cache:
    ''' class cache'''
    def __init__(self):
        '''Initialize redis client and flush the database'''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        '''
        Stores the data in a redis with a random key.

        Args:
            data (str, bytes, int, float): the data to store.

        Return:
            the generated str.
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
