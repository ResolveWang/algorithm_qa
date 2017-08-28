"""
问题描述：假设链表中每个节点的值都在[0,9]之间，那么链表整体就可以代表一个整数，
例如：9->3->7,可以代表整数937.给定两个这种链表的头结点head1和head2，请生
成代表两个整数相加值的结果链表。例如：链表1为9->3->7，链表2为6->3,最后生成
新的结果链表为1->0->0->0.

思路：
1）如果将链表先转化为整数相加，再转成链表，可能会出现溢出
2）可以使用逆序栈将链表节点压入栈，再进行操作
3）利用链表的逆序求解，这样不会占用额外空间复杂度
"""


from linkedlist.toolcls import Node, PrintMixin


class ListAddTool(PrintMixin):
    @staticmethod
    def add_list(head1, head2):
        if head1 is None:
            return head2

        if head2 is None:
            return head1

        reversed_list1 = ListAddTool.revert_linked_list(head1)
        reversed_list2 = ListAddTool.revert_linked_list(head2)

        new_head = None
        new_list = None
        flag = 0

        while reversed_list1 is not None or reversed_list2 is not None:
            if reversed_list1 is None:
                value1 = 0
            else:
                value1 = reversed_list1.value

            if reversed_list2 is None:
                value2 = 0
            else:
                value2 = reversed_list2.value

            temp = value1 + value2 + flag
            if temp/10 >= 1:
                flag = 1
                if new_list is None:
                    new_head = Node(temp % 10)
                    new_list = new_head
                else:
                    new_list.next = Node(temp % 10)
                    new_list = new_list.next
            else:
                flag = 0
                if new_list is None:
                    new_head = Node(temp)
                    new_list = new_head
                else:
                    new_list.next = Node(temp)
                    new_list = new_list.next

            if reversed_list1 is not None:
                reversed_list1 = reversed_list1.next
            if reversed_list2 is not None:
                reversed_list2 = reversed_list2.next

        if flag == 1:
            new_list.next = Node(1)
        reversed_new_head = ListAddTool.revert_linked_list(new_head)
        return reversed_new_head

    @staticmethod
    def revert_linked_list(head):
        pre = None

        while head is not None:
            next = head.next
            head.next = pre
            pre = head
            head = next

        return pre

if __name__ == '__main__':
    node1 = Node(9)
    node1.next = Node(9)
    node1.next.next = Node(9)

    node2 = Node(1)

    ListAddTool.print_list(ListAddTool.add_list(node1, node2))