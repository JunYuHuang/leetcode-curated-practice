# [LC 297. Serialize and Deserialize Binary Tree](https://leetcode.com/problems/serialize-and-deserialize-binary-tree/)

## General Notes

- PEDAC: Problem
  - serialize(root)
    - input: root node of a binary tree
    - output: string of binary tree traversed in some order (level, inorder, postorder, etc.)
  - deserialize(data)
    - input: string of binary tree traversed in some order (level, inorder, postorder, etc.)
    - output: root node of a binary tree
  - either root or string array input can be null
- PEDAC: Examples

## Solution 1: DFS recursive preorder (NeetCode's)

- O(N) time and O(N) space solution
- serialize(root)
  - initial res array
  - helper recursive function dfs(node)
    - if null node, push "N" to res and return
    - push node's value to res
    - call recursively on node's L & R children
  - call dfs(root)
  - return res converted to string with , delimiter
- deserialize(data)
  - convert data str into vals array
  - global instance variable i to 0 to traverse array
  - helper recursive function dfs()
    - if vals\[i] is "N", i++ and return
    - create curr node from vals\[i]'s value
    - i++
    - set curr's L & R children to res of their recursive calls
    - return node
  - return res of dfs()