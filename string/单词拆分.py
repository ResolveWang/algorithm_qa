"""
问题:
给定一个非空字符串 s 和一个包含非空单词列表的字典 wordDict，判定 s 是否可以被空格拆分为一个或多个在字典中出现的单词。

说明：
拆分时可以重复使用字典中的单词。
你可以假设字典中没有重复的单词。

示例:
s = "leetcode", wordDict = ["leet", "code"] => true
解释: 返回 true 因为 "leetcode" 可以被拆分成 "leet code"。
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """记忆化搜索，也可以改写成动态规划"""
        if not s:
            return False

        maps = dict()
        # 小优化
        wordDict = set(wordDict)
        return self.process(s, 0, wordDict, maps)

    def process(self, s, index, wordDict, maps):
        if maps.get(index) is not None:
            return maps.get(index)

        if index > len(s):
            return False

        if index == len(s):
            return True

        length = 1
        while index + length <= len(s):
            if maps.get(index + length) is not None:
                res = maps.get(index + length)
                if res:
                    return True
            else:
                if s[index:index + length] in wordDict:
                    res = self.process(s, index + length, wordDict, maps)
                    if res == True:
                        return res
                    else:
                        maps[index + length] = res
            length += 1
        return False