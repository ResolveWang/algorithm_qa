"""
问题描述:有一个机器按自然数序列的方式吐出球(1号球、2号球、3号球...)，你有一个
袋子,袋子最多能装K个球,除了袋子外，没有别的可用空间。设计一种方案，使得当机器
吐出第N个球的时候(N>K),你袋子中的球数是K个,同时可以保证从1号球到N号球中的每一
个，被选进袋子的概率都是K/N.
"""
import random


class KNRandomGetter:
    @classmethod
    def get_res(cls, k, n):
        if k < 1 or n < 1:
            return

        if n <= k:
            return list(range(1, n+1))

        res = list(0 for _ in range(k))

        for i in range(k):
            res[i] = i + 1

        for i in range(k, n-k):
            value = random.randint(1, i+1)
            if value <= k:
                random_index = random.randint(0, k-1)
                res[random_index] = i

        return res


if __name__ == '__main__':
    print(KNRandomGetter.get_res(10, 10000))