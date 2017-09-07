"""
问题描述：二叉树被记录成文件的过程叫做二叉树的序列化，通过文件内容重建原来二叉树的过程
叫做二叉树的反序列化。给定一棵二叉树的头结点head，并已知二叉树节点值的类型为32位整型，
请设计一种二叉树序列化和反序列化的方案

思路：
1）可以使用先序遍历来做，每个节点用'!'隔开，空节点用'#'表示
2）可以使用层序遍历来做，层序遍历需要结合队列使用
"""

from binarytree.toolcls import Node
from binarytree.q3 import PrintTree


class SerializedTree:
    @classmethod
    def serialized_tree(cls, head, res):
        if head is None:
            return res + '#!'
        res = res + str(head.value) + '!'
        res = cls.serialized_tree(head.left, res)
        res = cls.serialized_tree(head.right, res)
        return res

    @classmethod
    def unserialized(cls, serialized_str):
        if serialized_str.strip() == '' or serialized_str.startswith('#'):
            return None
        res = serialized_str.split('!')
        return cls.unserialized_tree(res)

    @classmethod
    def unserialized_tree(cls, nodes_info):
        cur = nodes_info.pop(0)
        if cur == '#':
            return None
        cur_node = Node(cur)
        cur_node.left = cls.unserialized_tree(nodes_info)
        cur_node.right = cls.unserialized_tree(nodes_info)
        return cur_node

    @classmethod
    def serialized_tree_by_level(cls, head, res):
        if head is None:
            return res + '#!'
        queue = list()
        queue.append(head)

        while len(queue) > 0:
            cur_node = queue.pop(0)
            if cur_node is not None:
                res = res + str(cur_node.value) + '!'
                queue.append(cur_node.left)
                queue.append(cur_node.right)
            else:
                res = res + '#!'
        return res

    @classmethod
    def unserialized_tree2(cls, serialized_str):
        if serialized_str.strip() == '' or serialized_str.startswith('#'):
            return None
        res = serialized_str.split('!')
        return cls.unserialized_tree_by_level(res)

    @classmethod
    def unserialized_tree_by_level(cls, res):
        index = 0
        node = cls.generate_node(res[index])
        index += 1
        queue = list()
        if node is not None:
            queue.append(node)
        head = node
        while len(queue) > 0:
            node = queue.pop(0)
            node_left = cls.generate_node(res[index])
            index += 1
            node_right = cls.generate_node(res[index])
            index += 1
            if node_left is not None:
                node.left = node_left
                queue.append(node_left)
            if node_right is not None:
                node.right = node_right
                queue.append(node_right)
        return head

    @classmethod
    def generate_node(cls, value):
        if value == '#':
            return None
        return Node(value)


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.right.right = Node(5)
    PrintTree.print_tree(head)

    pre = SerializedTree.serialized_tree(head, '')
    print('serialized tree str is ', pre)
    head = SerializedTree.unserialized(pre)
    PrintTree.print_tree(head)

    level = SerializedTree.serialized_tree_by_level(head, '')
    print('serialized2 tree str is ', level)
    head = SerializedTree.unserialized_tree2(level)
    PrintTree.print_tree(head)

