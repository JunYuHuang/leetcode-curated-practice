"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
# My O(V + E) time and O(V + E) space DFS recursive solution
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node: return None
        oldToNew = {} # node -> nodeCopy
        def dfs(curr):
            if curr in oldToNew: return oldToNew[curr]
            oldToNew[curr] = Node(curr.val)
            for nei in curr.neighbors:
                oldToNew[curr].neighbors.append(dfs(nei))
            return oldToNew[curr]
        return dfs(node)
        