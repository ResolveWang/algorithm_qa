"""
问题描述:给定两个不等于0的整数M和N,求M和N的最大公约数.
"""


def get_bigest_public_num(m, n):
    if n == 0:
        return m
    else:
        return get_bigest_public_num(n, m % n)


if __name__ == '__main__':
    print(get_bigest_public_num(10, 23))