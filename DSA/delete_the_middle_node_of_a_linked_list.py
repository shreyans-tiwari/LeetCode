"""
You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.
The middle node of a linked list of size n is the [n / 2]th node from the start using 0-based indexing, where [x]
denotes the largest integer less than or equal to x.
For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        n = 0

        while cur != None:
            n += 1
            cur = cur.next

        if n == 1:
            return None

        prev = head
        cur = prev.next
        i = 1

        while cur != None:
            if i == n // 2:
                prev.next = cur.next
                break

            print(prev.val, cur.val)

            prev = prev.next
            cur = cur.next
            i += 1

        return head
