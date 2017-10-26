"""
问题描述：给定一棵二叉树的的头结点head，以及这棵树中的两个节点o1和o2，
请返回o1和o2的最近公共祖先节点。
"""


from binarytree.toolcls import Node


class AncestorFinder:
    @classmethod
    def find_ancestor_by_recurise(cls, head, node1, node2):
        if head is None or node1 == head or node2 == head:
            return head

        left = cls.find_ancestor_by_recurise(head.left, node1, node2)
        right = cls.find_ancestor_by_recurise(head.right, node1, node2)

        if left is not None and right is not None:
            return head

        return left if left else right

    @classmethod
    def find_ancestor_by_hash(cls, head, node1, node2):
        if head is None:
            return head

        my_table = cls.construct_hash_table(head)
        parent1 = my_table[node1]
        node_list = list()
        node_list.append(node1)
        while parent1:
            node_list.append(parent1)
            parent1 = my_table[parent1]

        while node2:
            if node2 in node_list:
                return node2
            node2 = my_table[node2]


    @classmethod
    def construct_hash_table(cls, head):
        if head is None:
            return

        hash_table = dict()
        queue = list()

        queue.append((head, None))
        while len(queue) > 0:
            cur, parent = queue.pop(0)
            hash_table[cur] = parent

            if cur.left:
                queue.append((cur.left, cur))
            if cur.right:
                queue.append((cur.right, cur))

        return hash_table


if __name__ == '__main__':
    head = Node(1)
    head.left = Node(2)
    head.right = Node(3)
    head.left.left = Node(4)
    head.left.right = Node(5)
    head.right.left = Node(6)
    head.right.right = Node(7)
    head.right.right.left = Node(8)

    o1 = head.left.right
    o2 = head.right.left

    print("o1 : " + str(o1.value))
    print("o2 : " + str(o2.value))
    print("ancestor : " + str(AncestorFinder.find_ancestor_by_recurise(head, o1, o2).value))
    print("ancestor : " + str(AncestorFinder.find_ancestor_by_hash(head, o1, o2).value))
    print("===============")

