class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2:
            return len(s)

        cur = 1
        left = -1
        max_length = 1
        while cur < len(s):
            rindex = cur - 1
            while rindex >= 0:
                if s[rindex] == s[cur]:
                    break
                rindex -= 1

            left = max([left, rindex])
            max_length = max([max_length, cur - left])
            cur += 1

        return max_length