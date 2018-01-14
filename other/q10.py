"""
问题描述:设计一种缓存结构,该结构在构造时确定大小,假设大小为K,并且有两个功能,
1.set(key, value):将记录(key, value)插入该结构
2.get(key):返回key对应的value值.

要求:
1.set和get方法的时间复杂度为O(1)
2.某个key的set或者get操作一旦发生,认为这个key的记录成了最经常使用的.
3.当缓存的大小超过Ｋ时,移除最不经常使用的记录,即set或者get最久的.
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.pre = None


class DoubleNodeList:
    def __init__(self):
        self.tail = None
        self.head = None

    def add(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.pre = self.tail
            self.tail = node

    def move_to_tail(self, node):
        if self.tail == node:
            return

        if self.head == node:
            self.head = node.next
            self.head.pre = None
        else:
            node.pre.next = node.next
            node.next.pre = node.pre

        node.next = None
        self.tail.next = node
        node.pre = self.tail
        self.tail = node

    def remove_head(self):
        if self.head is None:
            return
        res = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            res.next = None
            self.head.pre = None

        return res


class LRUCache:
    def __init__(self, k):
        self.cap = k
        self.data_container = dict()
        self.key_container = dict()
        self.node_list = DoubleNodeList()

    def set(self, key, value):
        if key in self.data_container:
            node = self.data_container[key]
            node.value = value
            self.node_list.move_to_tail(node)
        else:
            node = Node(value)
            self.data_container[key] = node
            self.key_container[node] = key
            self.node_list.add(node)
            if len(self.data_container) > self.cap:
                res = self.node_list.remove_head()
                key = self.key_container.get(res)
                self.data_container.pop(key)

    def get(self, key):
        if key not in self.data_container:
            return

        node = self.data_container[key]
        self.node_list.move_to_tail(node)

        return node.value

    def get_all(self):
        return [node.value for node in self.data_container.values()]


if __name__ == '__main__':
    cache = LRUCache(3)
    cache.set('A', 1)
    cache.set('B', 2)
    cache.set('C', 3)
    print(cache.get('A'))
    cache.set('D', 4)
    print(cache.get_all())
