# [LC 700. Search in a Binary Search Tree](https://leetcode.com/problems/search-in-a-binary-search-tree/)

## General Notes

- PEDAC: Problem
  - input: root node of BST guaranteed to be not null, int val
  - ouput: node whose value equals val or null
  - BST = special binary tree where for each node,
    - node.L.val < node.val < node.R.val
- PEDAC: Examples

## Solution 1: iterative

- O(N) time and O(1) space solution
- initialise curr pointer set to root
- while curr is not null
  - if curr.val == val: return curr
  - if val < curr.val, curr = curr.L
  - else curr = curr.R
- return null

## Solution 2: recursive

- O(N) time and O(N) space solution
- same approach as solution 1 but
  - replace while loop by making function recursive
- if root is null, return null
- if root.val == val, return root
- if val < root.val, return call of itself on (root.L, val)
- else return call of itself on (root.R, val)