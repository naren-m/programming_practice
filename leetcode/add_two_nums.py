# Problem: https://leetcode.com/problems/add-two-numbers/description/


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = s = 0
        head = n = ListNode(-1)
        while l1 or l2 or carry > 0:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            s = v1 + v2 + carry
            carry = s // 10
            s = s % 10

            n.next = ListNode(s)
            n = n.next

        return head.next


def generate_linkedlist(arr):
    prev_node = None
    for val in reversed(arr):
        node = ListNode(val)
        node.next = prev_node
        prev_node = node

    return node


def print_list(ll):
    head = ll
    while head is not None:
        print(head.val, end=' ')
        head = head.next
    print()


def test(inp):
    for l in inp:
        l1 = generate_linkedlist(l[0])
        l2 = generate_linkedlist(l[1])
        print_list(l1)
        print_list(l2)

        s = Solution()
        print_list(s.addTwoNumbers(l1, l2))
        print("==================================")


inp = [([5, 5, 5], [5, 5, 5]), ([2, 4, 3], [7, 6, 4]), ([4, 4, 3], [7, 6, 4]),
       ([2, 4, 3], [5, 6, 4])]

test(inp)