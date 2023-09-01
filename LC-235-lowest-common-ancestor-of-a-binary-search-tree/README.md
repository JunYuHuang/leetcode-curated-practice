# [LC 235. Lowest Common Ancestor of a Binary Search Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary search tree (BST)
      - not null
      - the BST
        - has nodes in the range \[2, 10^5]
        - has nodes with values in the range \[-10^9, 10^9]
        - has nodes with values that are all unique
    - `p`: a node of the BST whose root is `root`
      - not null
      - not or equal to `q`
      - of a value in the range \[-10^9, 10^9]
      - exists in the BST
    - `q`: a node of the BST whose root is `root`
      - not null
      - not or equal to `p`
      - of a value in the range \[-10^9, 10^9]
      - exists in the BST
  - output:
    - `res`: node of the BST whose root is `root` that is the LCA of `p` and `q`
      - may be any non-null node of the BST including `root`, `p`, or `q`
  - lowest common ancestor (LCA):
    - lowest node in a binary tree that has both `p` and `q` as descendants
    - a node can be a descendant of itself
- PEDAC: Examples
  - TODO

## Solution 1 - binary search / iterative

- O(LogN) T and O(1) S solution
- initialise variables
  - `res`: pointer that points to the LCA node in the BST whose root node is `root` that is initially set to `root`
  - `low`: int set to -1 that represents the lower valued node from the nodes `p` and `q`
  - `high`: int set to -1 that represents the higher valued node from the nodes `p` and `q`
- if `p.val` is less than `q.val`,
  - `low` = `p.val`
  - `high` = `q.val`
- else
  - `low` = `q.val`
  - `high` = `p.val`
- while `res` is not null,
  - if `low` <= `res.val` <= `high`,
    - return `res`
  - if `res.val` < `low`
    - `res` = `res.right`
  - else
    - `res` = `res.left`
