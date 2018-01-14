"""
问题描述:设计一种结构,该结构具有如下三个功能:
1.insert(key):将某个key加入到该结构,做到不重复加入
2.delete(key):将原本在结构中的某个key删除
3.get_random():等概率随机返回结构中的任意一个key

要求:
insert、delete和get_random方法的时间复杂度都是O(1)
"""
import random


class RandomPool:
    def __init__(self):
        self.size = 0
        self.key_map = dict()
        self.data_map = dict()

    def insert(self, key):
        if key not in self.key_map:
            self.size += 1
            self.data_map[key] = self.size
            self.key_map[self.size] = key

    def delete(self, key):
        if key in self.key_map:
            to_delete_index = self.data_map.pop(key)
            self.key_map.pop(to_delete_index)
            last_key = self.key_map.pop(self.size)
            self.data_map.pop(last_key)
            self.size -= 1
            self.key_map[to_delete_index] = last_key
            self.data_map[last_key] = to_delete_index

    def get_random(self):
        if self.size == 0:
            return

        index = random.randint(1, self.size)
        return self.key_map[index]