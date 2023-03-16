# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# My O(N) time and O(1) space iterative solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if not head or not head.next: return head
        prev, curr = None, head
        while curr:
            nxt = curr.next # save ref to next node
            curr.next = prev # breaks the list in 2
            prev = curr
            curr = nxt
        return prev