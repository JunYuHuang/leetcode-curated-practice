# [LC 110. Balanced Binary Tree](https://leetcode.com/problems/balanced-binary-tree/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - may be null
      - if not null, has a value in the range \[-10^4, 10^4]
    - binary tree whose root node is `root`
      - has nodes in the range \[0, 5000]
      - has nodes whose values are in the range \[-10^4, 10^4]
  - output:
    - `res`: boolean that indicates if the tree whose root is `root` is height balanced or not
  - height-balanced = binary tree in which the diff of depths of the 2 subtrees of every node is in the range \[0, 1]
  - depth = # of nodes on the path from a node to its furthest non-null child?
  - return true if `root` is null
  - return true if `root` is non-null and has no children
- PEDAC: Examples
  - tree with 0 nodes is balanced
  - tree with 1 node is balanced
  - tree with 2 nodes is balanced

## Solution 1: DFS recursive bot-up

- O(N) T and O(N) S solution
- helper function `dfs(curr)`
  - return [true, 0] if `curr` is null
  - return [true, 1] if both children of `curr` are null
  - `isLeftBalanced`, `leftDepth` = `dfs(curr.left)`
  - `isRightBalanced`, `rightDepth` = `dfs(curr.right)`
  - `depth` = 1 + max(`leftDepth`, `rightDepth`)
  - return [false, `depth`] if `isLeftBalanced` is false
  - return [false, `depth`] if `isRightBalanced` is false
  - `isBalanced` = `abs(leftDepth - rightDepth)` < 2
  - return [`isBalanced`, `depth`]
- return `dfs(curr)[0]`
