# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# O(N) T and O(1) S slow and fast pointers solution
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None

        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast: break
        # return for non-cyclic lists
        if not fast or slow != fast:
            return None

        slow2 = head
        while slow2 != slow:
            slow2 = slow2.next
            slow = slow.next
        return slow2
