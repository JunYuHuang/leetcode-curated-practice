"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
# My O(N) time and O(N) space BFS iterative solution
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return None
        q = deque([root])
        while q:
            prev = None
            for i in range(len(q)):
                curr = q.popleft()
                if prev: prev.next = curr
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
                prev = curr
        return root