# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) T and O(N) S recursive linked list solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev, curr):
            if not curr:
                return prev
            nxt = curr.next
            curr.next = prev
            return reverse(curr, nxt)
        return reverse(None, head)
