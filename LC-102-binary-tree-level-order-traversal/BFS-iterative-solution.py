# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# O(N) T and O(N) S BFS iterative solution
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque([root])
        while queue:
            levelSize = len(queue)
            level = []
            for i in range(levelSize):
                curr = queue.popleft()
                level.append(curr.val)
                if curr.left: queue.append(curr.left)
                if curr.right: queue.append(curr.right)
            res.append(level)
        return res
