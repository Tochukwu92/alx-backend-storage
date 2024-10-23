#!/usr/bin/env python3


'''creat a redis database'''


import redis
import uuid
from typing import Union, Callable, Optional


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

    def get(self, key: str, fn: Optional[Calable] = None) -> Optional[
            Union[str, bytes, int, float]]:
        '''
        Retrive data from Redis, optionally applying a conversion function.

        Args:
            key (str): key to retrive data
            fn (callable, optional): a function to apply to retrived data.

        Return:
            union[str, bytes, int float, None]:
                The data converted using fn, or None if key doesn't exist.
        '''
        data = self._redis.get(key)
        if data is None:
            # Preserve the original Redis.get behavior when key doesn't exist
            return None
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """
        Retrieve data as a UTF-8 decoded string.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[str]: The decoded string or None if the key doesn't exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """
        Retrieve data as an integer.

        Args:
            key (str): The key to retrieve.

        Returns:
            Optional[int]: The integer value or None if the key doesn't exist.
        """
        return self.get(key, fn=int)
