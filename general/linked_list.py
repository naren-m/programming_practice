# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def generate_linkedlist(arr):
    head = None
    for val in arr:
        if head is None:
            head = ListNode(val)
        else:
            n = head
            while n.next is not None:
                n = n.next
            n.next = ListNode(val)

    return head


def print_list(ll):
    head = ll
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()


l = [2, 4, 3]
print_list(generate_linkedlist(l))