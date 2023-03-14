# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(N) time and O(1) space iterative solution (NeetCode's modded)
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head
        while curr and curr.next:
            # save pointers
            nextPairFirst = curr.next.next
            second = curr.next
            # reverse this pair
            second.next = curr
            curr.next = nextPairFirst
            prev.next = second
            # update pointers
            prev = curr
            curr = nextPairFirst
        return dummy.next