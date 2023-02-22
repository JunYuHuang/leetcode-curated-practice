# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# My O(N) time and O(N) space DFS recursive solution
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        res = []
        def dfs(curr):
            if not curr: return
            dfs(curr.left)
            dfs(curr.right)
            res.append(curr.val)
        dfs(root)
        return res