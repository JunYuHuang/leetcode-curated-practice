# [LC 236. Lowset Common Ancestor of a Binary Tree](https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - head / root of binary tree
    - p node and q node
      - will be different; have different values and be different nodes
      - guaranteed to be in tree
  - output:
    - LCA node (not just its value)
  - all nodes in tree have unique values
  - LCA (lowest common ancestor) = lowest nodes in T that has both p & q as descendents
    - node can be a descendant of itself
- PEDAC: Examples
  - q is a descendant of p
  - p and q are in root's L and R subtrees
  - p and q are under the same subtree (L or R) of root

## Solution 1: DFS recursive (StefanPochmann's modified)

- O(N) time and O(N) space solution
- if the current subtree has both p and q
  - return current node / subtree
- if only 1 of function result (from calling on L and R subutrees) is in that subtree
  - resut is one of them
- if neither are in subtree, result is null (impossible case due to LC constraints)