"""
问题描述:哈希表常见的三个操作是put、get和containsKey，而且这三个操作的时间复杂度
为O(1).现在想加入一个setAll功能,就是把所有记录的value都设置成统一的值.请设计并实
现这种有setAll功能的哈希表,并且put、get、containsKey和setAll四个操作的时间复杂
度都为O(1).
"""


class MyValue:
    def __init__(self, value, last_update):
        self.value = value
        self.last_update = last_update


class MyHashMap:
    def __init__(self):
        self.hash_map = dict()
        self.last_update = 0
        self.all_value = MyValue(None, -1)

    def put(self, key, value):
        self.last_update += 1
        my_value = MyValue(value, self.last_update)
        self.hash_map[key] = my_value

    def set_all(self, value):
        self.last_update += 1
        self.all_value = MyValue(value, self.last_update)

    def contains_key(self, key):
        return key in self.hash_map

    def get(self, key):
        if not self.contains_key(key):
            return
        if self.all_value.last_update > self.hash_map.get(key).last_update:
            return self.all_value.value
        else:
            return self.hash_map.get(key).value


if __name__ == '__main__':
    my_hash_map = MyHashMap()
    my_hash_map.put('Tom', 1)
    my_hash_map.put('James', 2)
    print(my_hash_map.get('Tom'))
    print(my_hash_map.contains_key('James'))

    my_hash_map.set_all(3)
    my_hash_map.get('Tom')
    print(my_hash_map.get('Tom'))
    my_hash_map.put('Tom', 333)
    print(my_hash_map.get('Tom'))
