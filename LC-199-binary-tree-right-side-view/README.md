# [LC 199. Binary Tree Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - may be null
      - the binary tree
        - has nodes in the range \[0, 100]
        - has nodes with values in the range \[-100, 100]
  - output:
    - `res`: an int array that represents the values of all the right-most nodes from each level (from root to the highest level) of the binary tree whose root node is `root`
  - level order =  root (level 0) -> all level + 1 nodes from left to right -> ...
- PEDAC: Examples
  - TODO

## Solution 1: BFS iterative

- O(N) time and O(N) space solution
- optional: if `root` is null, return an empty array
- initialise variables
  - `res`: empty int array that holds out output solution
  - `queue`: queue / array for traversing the nodes of the binary tree starting from `root` in level order initialised with `root`
- while `queue` is not empty,
  - `levelSize` = length of `queue`
  - loop `i` for `levelSize` times (starting from 0)
    - `curr` = pop 1st element from `queue`
    - skip to next iteration if `curr` is null
    - if `curr` is the right-most or 'last' node of the current level (`i` equals `levelSize` - 1),
      - push `curr.val` to `res`
    - push `curr.left` to `queue` if `curr.left` is not null
    - push `curr.right` to `queue` if `curr.right` is not null
- return `res`
