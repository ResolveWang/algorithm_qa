"""
问题描述：给定彼此独立的两棵树头结点分别为t1和t2，判断t1中是否有与t2树拓扑结构完全相同的子树。

思路：
1）使用二叉树序列化的方法将二叉树序列化成一个字符串
2）使用KMP算法判断t1字符串是否包含t2字符串

由于目前对KMP算法还不是很了解，所以直接使用了in进行判断
"""


from binarytree.toolcls import Node


class TopTreeTool:
    @classmethod
    def is_all_top(cls, head1, head2):
        str_t1 = cls.pre_order_visit(head1)
        str_t2 = cls.pre_order_visit(head2)
        if str_t2 in str_t1:
            return True

    @classmethod
    def pre_order_visit(cls, head):
        if head is None:
            return '#!'

        s = ''

        s += str(head.value)
        s += '!'

        s += cls.pre_order_visit(head.left)
        s += cls.pre_order_visit(head.right)
        return s


if __name__ == '__main__':
    t1 = Node(1)
    t1.left = Node(2)
    t1.right = Node(3)
    t1.left.left = Node(4)
    t1.left.right = Node(5)
    t1.right.left = Node(6)
    t1.right.right = Node(7)
    t1.left.left.right = Node(8)
    t1.left.right.left = Node(9)

    t2 = Node(2)
    t2.left = Node(4)
    t2.left.right = Node(8)
    t2.right = Node(5)
    t2.right.left = Node(9)

    print(TopTreeTool.is_all_top(t1, t2))
