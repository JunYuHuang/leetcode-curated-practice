"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
# O(N) T and O(N) S two-pass iterative solution
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # create the node copies
        nodeToCopy = {}
        curr = head
        while curr:
            nodeToCopy[curr] = Node(curr.val)
            curr = curr.next

        # update the `next` and `random` pointers for the node copies
        curr = head
        while curr:
            nodeToCopy[curr].next = nodeToCopy.get(curr.next, None)
            nodeToCopy[curr].random = nodeToCopy.get(curr.random, None)
            curr = curr.next

        return nodeToCopy[head]
