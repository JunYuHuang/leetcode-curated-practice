# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My O(N) time and O(N) space BFS iterative solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res, q = [], deque([root])
        while q:
            level = []
            qLen = len(q)
            for n in range(qLen):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left: q.append(curr.left)
                if curr.right: q.append(curr.right)
            res.append(level)
        return res