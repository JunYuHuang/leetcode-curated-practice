# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# O(LogN) T and O(1) S binary search iterative solution
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        res = root
        low = high = -1
        if p.val < q.val:
            low = p.val
            high = q.val
        else:
            low = q.val
            high = p.val
        while res:
            if low <= res.val <= high:
                return res
            if res.val < low:
                res = res.right
            else: # res.val > low
                res = res.left
