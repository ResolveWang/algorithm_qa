"""
设计一个支持以下两种操作的数据结构：
void addWord(word)
bool search(word)
search(word) 可以搜索文字或正则表达式字符串，字符串只包含字母 . 或 a-z 。 . 可以表示任何一个字母。
示例:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true
"""


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.word = True

    def search(self, word):
        return self.searchFrom(self.root, word)

    def searchFrom(self, node, word):
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for k in node.children:
                    if self.searchFrom(node.children[k], word[i + 1:]):
                        return True
                return False
            elif c not in node.children:
                return False
            node = node.children[c]
        return node.word