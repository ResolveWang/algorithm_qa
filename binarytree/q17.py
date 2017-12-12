"""
问题描述：现在有一种新的二叉树节点类型如下：
public class Node{
    public int value
    public Node left
    public Node right
    public Node parent

    public Node(int data){
        this.value = data
    }
}

该结构比普通二叉树节点结构多了一个指向父节点的parent指针。假设有一棵Node类型的节点组成的二叉树，树中每个节点的
parent指针都正确指向自己的父节点，头结点的parent指向None。只给一个在二叉树中的某个节点node，请实现返回node
的后继节点的函数。

在二叉树的中序遍历的序列中，node的下一个节点叫做node的后继节点。
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value


class NextNode:
    @classmethod
    def get_next_node(cls, node):
        if node is None:
            return None

        if node.right is not None:
            return cls.get_most_left(node.right)
        else:
            while node.parent is not None and node.parent.left != node:
                node = node.parent
            return node.parent

    @classmethod
    def get_most_left(cls, node):
        while node.left is not None:
            node = node.left
        return node


if __name__ == '__main__':
    head = Node(6)
    head.parent = None
    head.left = Node(3)
    head.left.parent = head
    head.left.left = Node(1)
    head.left.left.parent = head.left
    head.left.left.right = Node(2)
    head.left.left.right.parent = head.left.left
    head.left.right = Node(4)
    head.left.right.parent = head.left
    head.left.right.right = Node(5)
    head.left.right.right.parent = head.left.right
    head.right = Node(9)
    head.right.parent = head
    head.right.left = Node(8)
    head.right.left.parent = head.right
    head.right.left.left = Node(7)
    head.right.left.left.parent = head.right.left
    head.right.right = Node(10)
    head.right.right.parent = head.right

    test = head.left.left
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.left.left.right
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.left
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.left.right
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.left.right.right
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.right.left.left
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.right.left
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.right
    print(str(test.value) + " next: " + str(NextNode.get_next_node(test).value))
    test = head.right.right
    if not NextNode.get_next_node(test):
        res = 'None'
    else:
        res = str(NextNode.get_next_node(test))
    print(str(test.value) + " next: " + res)