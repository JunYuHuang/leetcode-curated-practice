# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) T and O(1) S two pointers solution (NeetCode's modded)
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        left = dummy
        right = head

        # move the `right` pointer until it reaches its offset (from `left`)
        while n > 0:
            right = right.next
            n -= 1

        # move both `left` and `right` pointers until `left` points to
        # the node before the node to delete and `right` points to null
        while right:
            left = left.next
            right = right.next

        # delete the nth node
        deleted = left.next
        left.next = deleted.next
        deleted.next = None # optional

        return dummy.next
