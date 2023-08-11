# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S BFS iterative solution
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        queue = deque([root])
        if root: queue.append(root)
        while queue:
            res += 1
            levelSize = len(queue)
            for i in range(levelSize):
                curr = queue.popleft()
                if not curr: continue
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
        return res
