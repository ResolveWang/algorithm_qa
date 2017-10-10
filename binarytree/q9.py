"""
问题描述：给定一棵二叉树的头结点head,分别实现按层打印和ZigZag打印二叉树的函数。例如，二叉树为：
node1 = Node(1)
node2 = Node(2)
node1.left = node2

node3 = Node(3)
node1.right = node3

node4 = Node(4)
node2.left = node4

node5 = Node(5)
node6 = Node(6)

node3.left = node5
node3.right = node6

node7 = Node(7)
node8 = Node(8)
node5.left = node7
node5.right = node8

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