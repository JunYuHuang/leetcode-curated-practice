# [LC 98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a BST
      - guaranteed to be non-null
      - whose BST
        - has nodes in the range \[1, 10^4]
        - has nodes with values in the range \[-2^31, 2^31 - 1]
        - has nodes with possible duplicate values
  - output:
    - `res`: boolean that is true if the binary tree of `root` is a BST else false
  - a node `curr` is the root of a BST IFF:
    - `curr` is null
    - `curr` is not null and has no children
    - if `curr` has a (non-null) left child,
      - `curr.left.val` < `curr.val`
      - `curr.left` is recursively a BST
    - if `curr` has a (non-null) right child,
      - `curr.right.val` > `curr.val`
      - `curr.right` is recursively a BST
- PEDAC: Examples
  - both null and leaf nodes are BSTs

## Solution 1: DFS recursive (NeetCode's modded)

- O(N) T and O(N) S solution
- make helper recursive method `dfs(curr, low, high)`
  - if `root` is null, return true
  - if not (`low` < `root` < `high`), return false
  - `isLeftBST` = `dfs(curr.left, low, curr.val)`
  - `isRightBST` = `dfs(curr.right, curr.val, high)`
  - return the result of `isLeftBST` AND'd with `isRightBST`
- return `dfs(root, NEGATIVE_INFINITY, POSITIVE_INFINITY)`
