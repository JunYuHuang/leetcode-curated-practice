# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S DFS recursive (D&C?) solution (NeetCode's modded)
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(curr, leftBound, rightBound):
            if not curr: return True
            if not (leftBound < curr.val < rightBound): return False
            return (dfs(curr.left, leftBound, curr.val) and
                    dfs(curr.right, curr.val, rightBound))
        
        return dfs(root, -math.inf, math.inf)
        