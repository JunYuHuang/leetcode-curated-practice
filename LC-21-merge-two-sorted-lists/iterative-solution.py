# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# O(M + N) T and O(1) S iterative linked list solution
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                curr = list1
                list1 = list1.next
            else: # list1.val >= list2.val
                curr.next = list2
                curr = list2
                list2 = list2.next

        # handle cases when `list1` and `list2` are of unequal sizes
        if not list1: curr.next = list2
        if not list2: curr.next = list1

        return dummy.next
