"""
问题描述：实现一个字典树（又称前缀树）,假设组成的单词字符仅是"a"~"z"，请实现
字典结构，并且支持下面四种功能：
1.insert(word) 添加word，可重复添加
2.delete(word) 删除word，如果word添加过多次,仅删除一个
3.search(word)　查询word是否在字典树中
4.prefix_number(pre)　返回以字符串pre为前缀的单词数量
"""


class TrieNode:
    def __init__(self):
        self.path = 0
        self.end = 0
        self.map = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        if not word:
            return

        parent = self.root
        for i in word:
            if i not in parent.map:
                parent.map[i] = TrieNode()
            parent.path += 1
            parent = parent.map[i]
        parent.end += 1

    def search(self, word):
        if not word:
            return False

        parent = self.root
        for i in word:
            if i not in parent.map:
                return False
            parent = parent.map[i]

        if parent.end > 0:
            return True
        return False

    def prefix_number(self, word):
        if not word:
            return 0

        parent = self.root
        for i in word:
            if i not in parent.map:
                return 0
            parent = parent.map[i]

        return parent.path

    def delete(self, word):
        if not word:
            return

        if not self.search(word):
            return

        parent = self.root
        for i in word:
            parent.map[i].path -= 1
            if parent.map[i].path == 0:
                del parent.map[i]
                break
            parent = parent.map[i]
        parent.end -= 1


if __name__ == '__main__':
    trie = Trie()
    print(trie.search("zuo"))
    trie.insert("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuo")
    trie.insert("zuo")
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.delete("zuo")
    print(trie.search("zuo"))
    trie.insert("zuoa")
    trie.insert("zuoac")
    trie.insert("zuoab")
    trie.insert("zuoad")
    trie.delete("zuoa")
    print(trie.search("zuoa"))
    print(trie.prefix_number("zuo"))