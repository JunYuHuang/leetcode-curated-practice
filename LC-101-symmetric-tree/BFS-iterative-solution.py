# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My O(N) time and O(N) space BFS iterative solution
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        q = deque([root])
        while q:
            qLen = len(q)
            if not self.isPali(q): return False
            for n in range(qLen):
                curr = q.popleft()
                if curr:
                    q.append(curr.left if curr.left else None)
                    q.append(curr.right if curr.right else None)
        return True
    def isPali(self, nodes: List[TreeNode]) -> bool:
        l, r = 0, len(nodes) - 1
        while l <= r:
            if ((not nodes[l] and nodes[r]) or
                (nodes[l] and not nodes[r]) or
                (nodes[l] and nodes[r] and 
                 nodes[l].val != nodes[r].val)): return False
            l += 1
            r -= 1
        return True