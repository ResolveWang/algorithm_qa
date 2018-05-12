"""
问题:
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了三次。找出那个只出现了一次的元素。
要求空间复杂度为O(1)
示例 1:
输入: [2,2,3,2]
输出: 3

延伸:
给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现了K次。找出那个只出现了1次的元素。


思路:
一个通用思路是使用位运算，除了要找的那个元素之外，每个元素出现了k次，那么将元素表示为32位整数，则这些整数
每个位置相加之后，分别对k取余，则一定能整除，所以算上剩下的那一个元素，剩下的一定是该元素。做法概括起来就是
统计每一位1的个数，然后对k取余

注意，负数做位运算会有坑。有的时候可以使用n&0x7FFFFFFF将其转换为正数
"""


class Solution:
    def singleNumber(self, arr):
        res = 0
        for i in range(32):
            bit_sum = 0
            for j in arr:
                bit_sum += ((j >> i) & 1)
            res |= ((bit_sum % 3) << i)
        return self.convert(res)

    def convert(self, num):
        if num >= 2 ** 31:
            num -= 2**32
        return num


if __name__ == '__main__':
    s = Solution()
    array = [-2, 3, 3, 3]
    print(s.singleNumber(array))