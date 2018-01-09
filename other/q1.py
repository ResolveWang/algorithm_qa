"""
问题描述:给定一个等概率随机产生1~5的随机函数rand1To5,如下:
public int range1To5(){
    return (int)(Math.random()*5)+1;
}

除此之外,不能使用任何额外的随机机制,请用rand1To5实现等概率随机产生1~7
的随机函数rand1To7.

补充题目:
给定一个以p概率产生0,以1-p概率产生1的函数rand01p如下:
public int rand01p(){
    double p = 0.83;
    return Math.random() < p ? 0:1;
}

除此之外,不能使用任何额外的随机机制,请用rand01p实现等概率随机产生1~6的
随机函数rand1To6.

进阶题目:
给定一个等概率随机产生1~M的随机函数rand1ToM如下:
public int rand1ToM(int m){
    return (int)(Math.random()*m) + 1;
}

除此之外,不能使用任何额外的随机机制,有两个输入参数,分别为m和n,请用rand1ToM(m)
实现等概率随机产生1~N的随机函数rand1ToN.
"""


import random


class RandomProducer:
    @classmethod
    def random1to5(cls):
        return int(random.random()*5) + 1

    @classmethod
    def random0to4(cls):
        return cls.random1to5() - 1

    @classmethod
    def random1to7(cls):
        random_value = cls.random0to4() + cls.random0to4()*5
        while random_value > 20:
            random_value = cls.random0to4() + cls.random0to4() * 5
        else:
            return random_value % 7 + 1

    @classmethod
    def random01p(cls):
        p = 0.83
        return 0 if random.random() < p else 1

    @classmethod
    def random01(cls):
        random_value = cls.random01p()
        while random_value == cls.random01p():
            random_value = cls.random01p()
        else:
            return random_value

    @classmethod
    def random1to3(cls):
        return cls.random01()*2 + cls.random01()

    @classmethod
    def random1to6(cls):
        random_value = cls.random1to3()*4 + cls.random1to3()
        while random_value >= 12:
            random_value = cls.random1to3() * 4 + cls.random1to3()
        else:
            return random_value % 6 + 1


if __name__ == '__main__':
    print(RandomProducer.random1to7())
    print(RandomProducer.random1to6())