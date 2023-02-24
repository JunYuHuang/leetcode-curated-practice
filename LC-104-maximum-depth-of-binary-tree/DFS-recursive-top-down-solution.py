# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My O(N) time and O(N) space DFS recursive top-down solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = [0]
        def dfs(curr, depth):
            if not curr: return
            if not curr.left and not curr.right:
                res[0] = max(res[0], depth)
            dfs(curr.left, depth + 1)
            dfs(curr.right, depth + 1)
        dfs(root, 1)
        return res[0]