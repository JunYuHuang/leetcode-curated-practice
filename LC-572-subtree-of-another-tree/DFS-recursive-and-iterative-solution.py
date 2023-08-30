# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N^2) T and O(N^2) S DFS recursive + iterative solution
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            curr = queue.popleft()
            if self.isSameTree(curr, subRoot): return True
            if curr.left: queue.append(curr.left)
            if curr.right: queue.append(curr.right)
        return False

    def isSameTree(self, p, q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False
        isLeftSame = self.isSameTree(p.left, q.left)
        isRightSame = self.isSameTree(p.right, q.right)
        return isLeftSame and isRightSame
