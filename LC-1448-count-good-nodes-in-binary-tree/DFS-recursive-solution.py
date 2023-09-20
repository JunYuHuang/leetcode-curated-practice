# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(LogN) S DFS recursive solution
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0

        def dfs(curr, maxVal):
            if not curr: return
            nonlocal res
            if maxVal <= curr.val: res += 1
            if curr.left:
                dfs(curr.left, max(maxVal, curr.val))
            if curr.right:
                dfs(curr.right, max(maxVal, curr.val))

        dfs(root, root.val)
        return res
