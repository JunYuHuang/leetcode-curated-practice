# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(N) T and O(1) S fast and slow pointers solution
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head.next if head else None
        while slow and fast:
            if slow == fast: return True
            slow = slow.next
            fast = fast.next.next if fast.next else None
        return False
