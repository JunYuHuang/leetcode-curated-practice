# [LC 1448. Count Good Nodes in Binary Tree](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - guaranteed to be not null
      - the binary tree
        - has nodes in the range \[1, 100]
        - has nodes with values in the range \[-10^4, 10^4]
  - output:
    - `res`: integer that is the count of (all) good nodes in the binary tree whose root node is `root`
  - good node: a node `curr` in the binary tree whose root node is `root` where
    - all nodes in the path from `root` to `curr` are less than or equal to `curr.val`
  - `root` node is always a good node
  - null nodes are never good nodes
  - non-null nodes are possible good nodes
- PEDAC: Examples
  - tree with 1 node -> 1

## Solution 1: DFS recursive

- O(N) time and O(LogN) space solution
- initialise variables
  - `res`: global int initially set to 0 that represents the count of all good nodes in the binary tree whose root node is `root`
- helper recursive function `dfs(curr, maxVal)`:
  - return if `curr` is null (optional)
  - `res++` if `maxVal` <= `curr.val`
  - if `curr.left` is not null,
    - `dfs(curr.left, max(maxVal, curr.val))`
  - if `curr.right` is not null,
    - `dfs(curr.right, mxa(maxVal, curr.val))`
- `dfs(root, root.val)`
- return `res`
