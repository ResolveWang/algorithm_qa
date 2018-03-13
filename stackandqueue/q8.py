"""
构造数组的MaxTree.首先定义二叉树节点如下：
public class Node{
    public int value;
    public Node left;
    public Node right;
    public Node(int data){
        this.value = data;
    }
}

一个数组的MaxTree定义如下：
1）数组没有重复元素
2）MaxTree是一棵二叉树，数组的每个值对应二叉树一个节点
3）包括MaxTree树在内且在其中的每一棵子树上，值最大的节点都是树的头

要求：给定一个没有重复元素的数组arr，写出生成这个数组的MaxTree函数，
要求时间复杂度为O(N),额外空间复杂度为O(N)

思路：按照下面要求建立的树即满足题目需求
1）每一个数的父节点是它左边第一个比它大的数和它右边第一个比它大的数中，较小的那个
2）如果某个节点左边和右边都没有比它大的数，那么它就是根节点
3）使用单调栈和hashmap可以完成需求
"""


class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class MaxTree:
    @classmethod
    def get_max_tree(cls, arr):
        node_arr = list()
        for i in arr:
            node_arr.append(Node(i))

        stack = list()
        lmap = dict()
        rmap = dict()

        for node in node_arr:
            while len(stack) != 0 and stack[-1].value < node.value:
                # pop and keep the relation
                cls.pop_and_keep_relation(stack, lmap)
            stack.append(node)
        while len(stack) != 0:
            cls.pop_and_keep_relation(stack, lmap)

        for node in node_arr[::-1]:
            while len(stack) != 0 and stack[-1].value < node.value:
                cls.pop_and_keep_relation(stack, rmap)
            stack.append(node)
        while len(stack) != 0:
            cls.pop_and_keep_relation(stack, rmap)

        head = None
        for node in node_arr:
            left_big = lmap.get(node)
            right_big = rmap.get(node)
            if left_big is None and right_big is None:
                head = node
            elif left_big is None:
                if right_big.left is None:
                    right_big.left = node
                else:
                    right_big.right = node
            elif right_big is None:
                if left_big.left is None:
                    left_big.left = node
                else:
                    left_big.right = node
            else:
                if left_big.value < right_big.value:
                    if left_big.left is None:
                        left_big.left = node
                    else:
                        left_big.right = node
                else:
                    if right_big.left is None:
                        right_big.left = node
                    else:
                        right_big.right = node
        return head

    @classmethod
    def pop_and_keep_relation(cls, stack, cmap):
        node = stack.pop()
        if len(stack) == 0:
            cmap.setdefault(node, None)
        else:
            cmap.setdefault(node, stack[-1])

    @classmethod
    def previsit(cls, tree_node):
        if tree_node is None:
            return
        print('{} '.format(tree_node.value), end='')
        cls.previsit(tree_node.left)
        cls.previsit(tree_node.right)

    @classmethod
    def get_max_tree_by_heap(cls, arr):
        if not arr:
            return
        length = len(arr)
        node_list = list()
        value_pos = dict()
        res = [-1 for _ in range(length)]
        for index, value in enumerate(arr):
            node_list.append(Node(value))
            value_pos[value] = index

        for index in range(length):
            cls.heap_insert(node_list, index)

        cls.get_relation(None, node_list[0], res, value_pos)

        return res

    @classmethod
    def get_relation(cls, parent, cur, res, relation_map):
        if cur is None:
            return
        if parent is None:
            res[relation_map[cur.value]] = -1
        else:
            res[relation_map[cur.value]] = relation_map[parent.value]
        cls.get_relation(cur, cur.left, res, relation_map)
        cls.get_relation(cur, cur.right, res, relation_map)

    @classmethod
    def heap_insert(cls, heap, index):
        if heap[index].value <= heap[int((index-1)/2)].value and index != int((index-1)/2):
            if heap[int((index-1)/2)].left is None:
                heap[int((index-1)/2)].left = heap[index]
            else:
                heap[int((index-1)/2)].right = heap[index]
            return

        while heap[index].value > heap[int((index-1)/2)].value:
            parent_value = heap[int((index-1)/2)].value
            cur_value = heap[index].value
            heap[index].value, heap[int((index-1)/2)].value = parent_value, cur_value
            if heap[int((index-1)/2)].left is None:
                heap[int((index-1)/2)].left = heap[index]
            elif heap[int((index-1)/2)].right is None:
                heap[int((index - 1) / 2)].right = heap[index]
            index = int((index-1)/2)


if __name__ == '__main__':
    cur_arr = [3, 1, 4, 2]
    cur_head = MaxTree.get_max_tree(cur_arr)
    MaxTree.previsit(cur_head)
    res = MaxTree.get_max_tree_by_heap(cur_arr)
    print(res)