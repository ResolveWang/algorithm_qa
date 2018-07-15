"""
小易喜欢的单词具有以下特性：
1.单词每个字母都是大写字母
2.单词没有连续相等的字母
3.单词没有形如“xyxy”(这里的x，y指的都是字母，并且可以相同)这样的子序列，子序列可能不连续。
例如：
小易不喜欢"ABBA"，因为这里有两个连续的'B'
小易不喜欢"THETXH"，因为这里包含子序列"THTH"
小易不喜欢"ABACADA"，因为这里包含子序列"AAAA"
小易喜欢"A","ABA"和"ABCBA"这些单词
给你一个单词，你要回答小易是否会喜欢这个单词（只要不是不喜欢，就是喜欢）。
输入描述:
输入为一个字符串，都由大写字母组成，长度小于100


输出描述:
如果小易喜欢输出"Likes",不喜欢输出"Dislikes"

输入例子1:
AAA
输出例子1:
Dislikes
"""
import sys


class Solution:
    def get_like_or_dislike(self, strs):
        if len(strs) < 2:
            print('Likes')
            return

        index = 0
        pre = ''
        maps = dict()
        while index < len(strs):
            if pre == strs[index]:
                print('Dislikes')
                return

            if not maps.get(strs[index]):
                maps[strs[index]] = [index]
            else:
                maps[strs[index]].append(index)

            pre = strs[index]
            index += 1

        visited = set()
        for key in maps:
            visited.add(key)
            if len(maps[key]) > 3:
                print('Dislikes')
                return
            if len(maps[key]) < 2:
                continue
            for key2 in maps:
                if key2 in visited:
                    continue
                arr1 = maps[key]
                arr2 = maps[key2]
                if self.matched(arr1, arr2):
                    print('Dislikes')
                    return

        print('Likes')

    def matched(self, arr1, arr2):

        index1 = 0
        index2 = 0
        count1 = 0
        count2 = 0
        big_continued = False

        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] < arr2[index2]:
                index1 += 1
                if not big_continued:
                    count2 += 1
                    big_continued = True
            else:
                index2 += 1
                count1 += 1
                big_continued = False

        if count1 >= 1 and count2 >= 2:
            return True
        else:
            return False


if __name__ == '__main__':
    args = sys.stdin.readline().strip()
    s = Solution()
    s.get_like_or_dislike(args)