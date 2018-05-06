"""
问题: 给定两个单词（beginWord 和 endWord）和一个字典，找到从 beginWord 到 endWord 的最短转换序列的长度。
转换需遵循如下规则：每次转换只能改变一个字母。转换过程中的中间单词必须是字典中的单词。

说明:
如果不存在这样的转换序列，返回 0。
所有单词具有相同的长度。
所有单词只由小写字母组成。
字典中不存在重复的单词。
你可以假设 beginWord 和 endWord 是非空的，且二者不相同。

示例:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog"　＝> 5
"""
import string
import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        queue = collections.deque([(beginWord, 1)])
        wordList = set(wordList)
        # 直接穷举所有字母，常数复杂度
        ls = string.ascii_lowercase
        visited = set()
        while queue:
            word, dist = queue.popleft()
            if word == endWord:
                return dist
            for i in range(len(word)):
                for j in ls:
                    if j != word[i]:
                        newWord = word[:i] + j + word[i + 1:]
                        if newWord not in visited and newWord in wordList:
                            queue.append((newWord, dist + 1))
                            visited.add(newWord)
        return 0

    def ladderLength2(self, beginWord, endWord, wordList):
        # 预处理字典技巧
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            print(d)
            return d

        def bfs_words(begin, end, dict_words):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i + 1:]
                        neigh_words = dict_words.get(s, [])
                        for neigh in neigh_words:
                            if neigh not in visited:
                                queue.append((neigh, steps + 1))
            return 0

        d = construct_dict(wordList | {beginWord, endWord})
        return bfs_words(beginWord, endWord, d)


if __name__ == '__main__':
    begin = "hit"
    end = "cog"
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    r = solution.ladderLength2(begin, end, set(words))
    print(r)