"""
问题描述:在一个二维坐标系中,所有的值都是double类型,那么一个三角形可以由3个点来代表,
给定3个点代表的三角形,再给定一个点(x,y),判断(x,y)是否在三角形中.
"""


class PointInTriangle:
    @classmethod
    def cross_product(cls, x1, y1, x2, y2):
        return x1 * y2 - x2 * y1

    @classmethod
    def is_inside(cls, x1, y1, x2, y2, x3, y3, x, y):
        if cls.cross_product(x3-x1, y3-y1, x2-x1, y2-y1) >= 0:
            x2, x3 = x3, x2
            y2, y3 = y3, y2

        if cls.cross_product(x2-x1, y2-y1, x-x1, y-y1) < 0:
            return False

        if cls.cross_product(x3-x2, y3-y2, x-x2, y-y2) < 0:
            return False

        if cls.cross_product(x1-x3, y1-y3, x-x3, y-y3) < 0:
            return False

        return True


if __name__ == '__main__':
    x1 = -5
    y1 = 0
    x2 = 0
    y2 = 8
    x3 = 5
    y3 = 0
    x = 0
    y = 5
    print(PointInTriangle.is_inside(x1, y1, x2, y2, x3, y3, x, y))