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
                            visited.add(newWord)  # wordList.remove(newWord)
        return 0