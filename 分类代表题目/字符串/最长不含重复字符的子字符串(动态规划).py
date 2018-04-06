"""
问题描述:请从字符串中找出一个最长的不包含重复字符的子字符串，计算
该最长子字符串的长度。假设字符串中只含有'a~z'的字符。例如，在字符
串'arabcacfr'中，最长不含重复字符的子字符串是'acfr'，长度为4

思路:
分别求必须以i(0<=i<=len-1)结尾的最长不含重复字符的子串长度
"""


class LongestSubStr:
    def get_longest_substr(self, input_str):
        length = len(input_str)
        if length <= 1:
            return length

        dp = [0 for _ in range(length)]
        dp[0] = 1
        index = 1
        while index < length:
            if input_str[index] not in input_str[:index]:
                dp[index] = dp[index-1] + 1
            else:
                pre_index = input_str.rindex(input_str[index], 0, index-1)
                distance = index - pre_index
                if dp[index-1] < distance:
                    dp[index] = dp[index-1] + 1
                else:
                    dp[index] = distance
            index += 1

        return dp[length-1]


if __name__ == '__main__':
    print(LongestSubStr().get_longest_substr('arabcacfr'))