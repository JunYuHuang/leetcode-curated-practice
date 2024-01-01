# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(N) T and O(N) S brute force solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        visit = set()
        curr = head
        while curr:
            if curr in visit:
                return curr
            visit.add(curr)
            curr = curr.next
        return None
