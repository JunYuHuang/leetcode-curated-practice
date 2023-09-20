# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) DFS recursive solution (NeetCode's modded)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root, float("-inf"), float("inf"))

    def dfs(self, curr, low, high):
        if not curr:
            return True
        if not (low < curr.val < high):
            return False
        isLeftBST = self.dfs(curr.left, low, curr.val)
        isRightBST = self.dfs(curr.right, curr.val, high)
        return isLeftBST and isRightBST
