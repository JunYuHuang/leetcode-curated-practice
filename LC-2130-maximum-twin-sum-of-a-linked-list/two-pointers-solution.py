# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) T and O(1) S two pointers solution
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        # find and save the 2nd middle node at `slow`
        res = 0
        slow = head
        fast = head
        prev = None
        while fast:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        # split the list and reverse its 2nd half
        prev.next = None
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        head2 = prev
        # compute the max twin sum
        while head and head2:
            twinSum = head.val + head2.val
            if twinSum > res: res = twinSum
            head = head.next
            head2 = head2.next
        return res
