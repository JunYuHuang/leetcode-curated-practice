# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) T and O(1) S iterative 2-pass solution
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # count the size of the list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next

        # find the nth node to delete
        i = 0
        dummy = ListNode(-1, head)
        prev = dummy
        curr = head
        nxt = head.next
        while size - i != n:
            prev = curr
            curr = curr.next
            nxt = curr.next
            i += 1

        # delete the nth node and return the head
        prev.next = nxt
        curr.next = None
        return dummy.next
