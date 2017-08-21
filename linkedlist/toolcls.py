class PrintMixin:
    @staticmethod
    def print_list(head):
        while head is not None:
            print(head.value, end=' ')
            head = head.next
        print()