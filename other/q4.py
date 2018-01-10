"""
问题描述:在一个二维坐标系中，所有的值都是double类型,那么一个矩形可以由４个点
来代表,(x1,y1)为最左的点、(x2,y2)为最上的点、(x3,y3)为最下的点、(x4,y4)为
最右的点.给定４个点代表的矩形,再给定一个点(x,y),判断(x,y)是否在矩形中.
"""
import math


class PointInRectangle:
    @classmethod
    def is_inside_simple(cls, x1, y1, x4, y4, x, y):
        if x <= x1:
            return False
        if y1 <= y:
            return False
        if x >= x4:
            return False
        if y <= y4:
            return False

        return True

    @classmethod
    def is_inside(cls, x1, y1, x2, y2, x3, y3, x4, y4, x, y):
        if y1 == y2:
            return cls.is_inside_simple(x1, y1, x4, y4, x, y)
        l = abs(y4 - y3)
        k = abs(x4 - x3)
        s = math.sqrt(l*l+k*k)
        sin = l / s
        cos = k / s

        new_x1 = cos * x1 + sin * y1
        new_y1 = -sin * x1 + y1 * cos
        news_x4 = cos * x4 + sin * y4
        new_y4 = -sin * x4 + y4 * cos

        new_x = cos * x + sin * y
        new_y = -sin * x + y * cos

        return cls.is_inside_simple(new_x1, new_y1, news_x4, new_y4, new_x, new_y)


if __name__ == '__main__':
    print(PointInRectangle.is_inside(0, 3, 3, 7, 4, 0, 7, 4, 4, 3))