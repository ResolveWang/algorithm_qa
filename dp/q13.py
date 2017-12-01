"""
问题描述：给定一个只由0(假)、1(真)、&(逻辑与)、|（逻辑或）和^(异或)五种字符组成的字符串
express,再给定一个布尔值desired。返回express能有多少种组合方式，可以达到desird的结果。

举例
express="1^0|0|1"，desired=false
只有1^((0|0)|1)和1^(0|(0|1))的组合可以得到false，所以返回2.
express="1"，desired=false
无组合可以得到false，所以返回0.
"""


class ExpectionNums:
    @classmethod
    def is_valid(cls, exp):
        if not exp or len(exp) % 2 == 0:
            return False

        for i in exp[::2]:
            if i not in ['0', '1']:
                return False

        for i in exp[1::2]:
            if i not in ['&', '|', '^']:
                return False

        return True

    @classmethod
    def get_nums_by_way1(cls, exp, desired):
        if not cls.is_valid(exp):
            return 0

        return cls.get_nums_detail1(exp, desired, 0, len(exp)-1)

    @classmethod
    def get_nums_detail1(cls, exp, desired, start, end):
        if start == end:
            if desired:
                if exp[start] == '1':
                    return 1
                else:
                    return 0
            else:
                if exp[start] == '1':
                    return 0
                else:
                    return 1

        res = 0
        if desired:
            i = start + 1
            while i < end:
                if exp[i] == '&':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                if exp[i] == '|':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, not desired, i+1, end)
                    res += cls.get_nums_detail1(exp, not desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                if exp[i] == '^':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, not desired, i+1, end)
                    res += cls.get_nums_detail1(exp, not desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)

                i += 2

        else:
            i = start + 1
            while i < end:
                if exp[i] == '&':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                    res += cls.get_nums_detail1(exp, not desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, not desired, i+1, end)
                if exp[i] == '|':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                if exp[i] == '^':
                    res += cls.get_nums_detail1(exp, desired, start, i-1) * cls.get_nums_detail1(exp, desired, i+1, end)
                    res += cls.get_nums_detail1(exp, not desired, start, i-1) * cls.get_nums_detail1(exp, not desired, i+1, end)
                i += 2

        return res


if __name__ == '__main__':
    mystr = '1^0&0|1&1^0&0^1|0|1&1'
    mydesird = True
    print(ExpectionNums.get_nums_by_way1(mystr, mydesird))