# [LC 133. Clone Graph](https://leetcode.com/problems/clone-graph/)

## Solution 1: DFS recursive

- O(E + V) time and O(E + V) space class solution
- return null if node is null
- hashmap of (node) -> nodeCopy pairs
- helper recursive function dfs(node) -> Node:
  - if node in hashmap, return hashmap\[inputNode\]
  - create nodeCopy initialised with its original's value
  - add (node, nodeCopy) to hashmap
  - for each neighbour of node
    - add (return of) dfs(neighbour) to nodeCopy's neighbor list
  - return hashmap\[node\]
- return dfs(node)
