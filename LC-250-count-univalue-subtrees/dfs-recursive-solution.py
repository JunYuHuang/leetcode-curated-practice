# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS recursive solution (aunbr's comment on OldCodingFarmer's modified)
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, None)
        return self.res
    def dfs(self, node, parent):
        if not node: return True
        left = self.dfs(node.left, node.val)
        right = self.dfs(node.right, node.val)
        if left and right: self.res += 1 # count leaf nodes
        return left and right and node.val == parent