# [LC 226. Invert Binary Tree](https://leetcode.com/problems/invert-binary-tree/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - may be null
      - if not null, has a value in the range \[-100, 100]
    - binary tree whose root node is `root`
      - has nodes in the range \[0, 100]
      - has nodes whose values are in the range \[-100, 100]
  - output:
    - `res`: root of inverted binary tree (whose root is `root`)
      - may be null
      - if not null, has a value in the range \[-100, 100]
  - invert = swap each node's left and right subtrees
- PEDAC: Examples
  - TODO

## Solution 1: BFS iterative

- O(N) T and O(N) S solution
- optional: return null if `root` is null
- initialise variables
  - `queue`: array that holds nodes to process that initially just holds `root`
- while `queue` is not empty:
  - `levelLen` = int snapshot length of `queue`
  - loop for `i` for `levelLen` times:
    - `curr` = pop frontmost node from `queue`
    - skip to next iteration if `curr` is null
    - if `curr.left` is not null,
      - push `curr.left` to `queue`
    - if `curr.right` is not null,
      - push `curr.right` to `queue`
    - skip to next iteration if both of `curr`'s left and right children are null
    - `temp` = `curr.left`
    - `curr.left` = `curr.right`
    - `curr.right` = `temp`
- return `root`
