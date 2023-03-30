# [LC 98. Validate Binary Search Tree](https://leetcode.com/problems/validate-binary-search-tree/)

## General Notes

- PEDAC: Problem
  - input: 
    - `root`: root node of a BST, guaranteed to be non-null
  - output: boolean depending on if binary tree of `root` is a BST or not
  - is BST IFF:
    - root has no children
    - root has L child only and
      - L's val < root's val and
      - L is a BST and
      - all of L's children's vals < root's val
    - root has R child only and
      - R's val > root's val and
      - R is a BST and
      - all of R's children's vals > root's val
    - root has both children and
      - previous 2 conditions are true minus the only child clauses
    previous
- PEDAC: Examples
  - both null and leaf nodes are BSTs

## Solution 1: DFS recursive (NeetCode's modded)

- O(N) time and O(N) space solution
- if root has no children, return true
- return dfs(root, -infinity, +infinity)
- helper recursive function dfs(curr, leftBound, rightBound)
  - if curr is null, return true
  - bool isCurrValid = leftBound < curr.val < rightBound
  - return isCurrValid and dfs(curr.left, leftBound, curr.val) and dfs(curr.right, curr.val, rightBound)