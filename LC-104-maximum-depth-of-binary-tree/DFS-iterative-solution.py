# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) time and O(N) space DFS iterative solution (NeetCode's modified)
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        stack, res = [[root, 1]], 0
        while stack:
            curr, depth = stack.pop()
            if depth > res: res = depth
            if curr.right: stack.append([curr.right, depth + 1])
            if curr.left: stack.append([curr.left, depth + 1])
        return res