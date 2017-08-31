"""
问题描述：对于二叉树的节点来说，其本身的值域，有指向左孩子和右孩子的两个指针：对双向
链表的节点来说，其本身的值域，有指向上一个节点和下一个节点的指针。在结构上，两种结构
有相似性，对于每个节点来说，原来的right指针等价于转换后的next指针，原来的left指针
等价于转换后的last指针。现在有一颗搜索二叉树，请将其转换一个有序的双向链表，并且返回
转换后的双向链表头结点。
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeToList:
    @classmethod
    def revert(cls, tree_head):
        if tree_head is None:
            return tree_head

        queue = list()
        cls.visit_in_mid_order(tree_head, queue)

        pre = None
        head = None
        count = 1
        while len(queue) > 0:
            cur = queue.pop(0)
            cur.left = pre
            if count == 1:
                head = cur
            if pre is not None:
                pre.right = cur
            pre = cur
            count += 1
        return head

    @classmethod
    def visit_in_mid_order(cls, tree_head, queue):
        if tree_head.left is not None:
            cls.visit_in_mid_order(tree_head.left, queue)
        queue.append(tree_head)
        if tree_head.right is not None:
            cls.visit_in_mid_order(tree_head.right, queue)

    @classmethod
    def convert(cls, tree_head):
        if tree_head is None:
            return tree_head

        end = cls.recursive(tree_head)
        start = end.right
        end.right = None
        return start

    @classmethod
    def recursive(cls, tree_head):
        if tree_head is None:
            return
        left_end = cls.recursive(tree_head.left)
        right_end = cls.recursive(tree_head.right)
        if left_end is None:
            left_start = None
        else:
            left_start = left_end.right

        if right_end is None:
            right_start = None
        else:
            right_start = right_end.right

        if left_end is not None and right_end is not None:
            left_end.right = tree_head
            tree_head.left = left_end
            tree_head.right = right_start
            right_start.left = tree_head
            right_end.right = left_start
            return right_end
        elif left_end is not None:
            left_end.right = tree_head
            tree_head.left = left_end
            tree_head.right = left_start
            return tree_head
        elif right_end is not None:
            tree_head.right = right_start
            right_start.left = tree_head
            right_end.right = tree_head
            return right_end
        else:
            tree_head.right = tree_head
            return tree_head

    @staticmethod
    def print_list(head):
        while head is not None:
            print(head.value, end=' ')
            head = head.right
        print()

if __name__ == '__main__':
    head = Node(5)
    head.left = Node(2)
    head.right = Node(9)
    head.left.left = Node(1)
    head.left.right = Node(3)
    head.left.right.right = Node(4)
    head.right.left = Node(7)
    head.right.right = Node(10)
    head.right.left.left = Node(6)
    head.right.left.right = Node(8)

    # double_list = TreeToList.revert(head)
    # TreeToList.print_list(double_list)

    double_list = TreeToList.convert(head)
    TreeToList.print_list(double_list)