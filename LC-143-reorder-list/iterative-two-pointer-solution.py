# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) T and O(1) S two-pointer linked list solution
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head.next: return head
        if not head.next.next: return head

        # find the middle node and split the list in half
        dummy = ListNode(-1, head)
        prevSlow = None
        slow = fast = dummy.next
        while fast and fast.next:
            prevSlow = slow
            slow = slow.next
            fast = fast.next.next
        prevSlow.next = None
        mid = slow

        # reverse the 2nd half of the list starting from `mid`
        # note that this splits the list into 2 lists
        head2 = self.reverse(mid)

        # splice together the new reordered list from the 2 lists
        while head and head2:
            nxt = head.next
            nxt2 = head2.next
            head.next = head2
            # handle the case for when the original list was odd-sized which results
            # in a reversed 2nd half that has 1 more node than the first half
            head2.next = nxt if nxt else nxt2
            head = nxt
            head2 = nxt2
        return dummy.next
    def reverse(self, node):
        prev = None
        while node:
            nxt = node.next
            node.next = prev
            prev = node
            node = nxt
        return prev
