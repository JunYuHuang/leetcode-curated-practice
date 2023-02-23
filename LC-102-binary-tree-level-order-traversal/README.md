# [LC 102. Binary Tree Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/)

## General Notes

- level order =  root (level 0) -> all level + 1 nodes from left to right -> ...

## Solution 1: BFS iterative

- O(N) time and O(N) space solution
- return empty array if root is null
- initialise empty res array and queue with root
- while queue is not empty
  - initialise empty level array
  - loop thru i for queue's current length (snapshot):
    - curr = pop from queue front 
    - push curr's value to level
    - if curr.L is not null, push it to queue
    - if curr.R is not null, push it to queue
  - push level to res
- return res