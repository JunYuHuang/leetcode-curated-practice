# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# My O(N) time and O(N) space recursive solution
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def helper(prev, curr):
            if not curr: return prev
            nxt = curr.next
            curr.next = prev
            return helper(curr, nxt)
        return helper(None, head)