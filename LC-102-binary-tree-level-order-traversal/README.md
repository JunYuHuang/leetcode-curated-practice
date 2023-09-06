# [LC 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - may be null
      - the binary tree
        - has nodes in the range \[0, 2000]
        - has nodes with values in the range \[-1000, 1000]
  - output:
    - `res`: a matrix of int values that represent the values of all the nodes from the binary tree whose root node is `root` traversed in level order
  - level order =  root (level 0) -> all level + 1 nodes from left to right -> ...
- PEDAC: Examples
  - TODO

## Solution 1: BFS iterative

- O(N) time and O(N) space solution
- brief: use a queue and a nested loop to process the nodes
- initialise variables
  - `queue`: a special array or double-ended queue that allows for removing both its first and last elements in O(1) time initialised with `root` as its first and only element
  - `res`: the resulting int matrix (2D array) to return
- if `root` is null, return an empty list
- while `queue` is not empty,
  - `levelSize` = length of `queue`
  - `level` = empty array
  - loop `levelSize` times,
    - `curr` = remove 1st el from `queue`
    - optional: skip to next iteration if `curr` is null
    - push `curr.val` to `level`
    - if `curr.left` is not null,
      - push `curr.left` to `queue`
    - if `curr.right` is not null,
      - push `curr.right` to `queue`
  - push `level` to `res`
- return `res`
