"""
问题描述:假设函数Math.random()等概率随机返回一个在[0,1)上的数，那么我们
知道在[0,x)区间上的数出现的概率为(0<x<=1).给定一个大于0的整数k，并且可以
使用Math.random()函数,请实现一个函数依然返回在[0,1)范围上的数,但是在[0,x)
区间上的数出现概率为x^k(0<x<=1).
"""
import random


class Random0Tox:
    @classmethod
    def get_random_value(cls, k):
        res = 0
        for i in range(k):
            res = max([res, random.random()])

        return res