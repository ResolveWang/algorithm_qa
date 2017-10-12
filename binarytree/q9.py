"""
问题描述：给定一棵二叉树的头结点head,分别实现按层打印和ZigZag打印二叉树的函数。例如，二叉树为：
head = Node(1)
head.left = Node(2)
head.right = Node(3)
head.left.left = Node(4)
head.right.left = Node(5)
head.right.right = Node(6)
head.right.left.left = Node(7)
head.right.left.right = Node(8)

按层打印时，输出格式为：
Level 1: 1
Level 2: 2 3
Level 3: 4 5 6
Level 4: 7 8

ZigZag打印时，输出格式为：
Level 1: 1
Level 2: 3 2
Level 3: 4 5 6
Level 4: 8 7

"""

from binarytree.toolcls import Node


class PrintZigzag:
    @classmethod
    def print_by_level(cls, root):
        if root is None:
            return
        last = root.value
        nlast = None

        queue = [root]
        level = 1
        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node == root:
                print('Level {}'.format(level), end=':')
            print(cur_node.value, end=' ')

            if cur_node.left is not None:
                queue.append(cur_node.left)
                nlast = cur_node.left.value
            if cur_node.right is not None:
                queue.append(cur_node.right)
                nlast = cur_node.right.value
            if last == cur_node.value and len(queue) > 0:
                print()
                level += 1
                print('Level {}'.format(level), end=':')
                last = nlast

    @classmethod
    def print_by_zigzag(cls, root):
        if root is None:
            return

        flag = True
        queue = [root]
        last = root.value
        nlast = None
        level = 1
        print('Level {}'.format(level), end=':')
        while len(queue) > 0:
            if flag is True:
                cur_node = queue.pop(0)
                if cur_node.left is not None:
                    queue.append(cur_node.left)
                    if nlast is None:
                        nlast = cur_node.left.value
                if cur_node.right is not None:
                    queue.append(cur_node.right)
                    if nlast is None:
                        nlast = cur_node.right.value

            else:
                cur_node = queue.pop()
                if cur_node.right is not None:
                    queue.insert(0, cur_node.right)
                    if nlast is None:
                        nlast = cur_node.right.value
                if cur_node.left is not None:
                    queue.insert(0, cur_node.left)
                    if nlast is None:
                        nlast = cur_node.left.value
            print(cur_node.value, end=' ')

            if last == cur_node.value and len(queue) > 0:
                last = nlast
                nlast = None
                flag = not flag
                level += 1
                print()
                print('Level {}'.format(level), end=':')


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.left = Node(5)
    head.right.right = Node(6)
    head.right.left.left = Node(7)
    head.right.left.right = Node(8)

    PrintZigzag.print_by_level(head)
    print()
    print()
    PrintZigzag.print_by_zigzag(head)