# [LC 250. Count Univalue Subtrees (Premium)](https://leetcode.com/problems/count-univalue-subtrees/)

## General Notes:

- PEDAC: Problem
  - input:
    - root: head TreeNode of a binary tree, possibly null
  - output:
    - count of uni-value subtrees: int in range (0, 1000)
  - uni-value subtree = all nodes of the subtree have the same value
    - means the count of uni-values trees only counts towards nodes that have the same value
    - only count most dominant or max count of nodes with same value?
- PEDAC: Examples
  - uni-value tree examples:
      - leaf nodes: non-null node with no (L or R) children
      - node with a L or R child or both children who have the same value as the parent node
  - null nodes are not uni-value trees

## Solution 1: DFS recursive bottom-up (aunbr's comment on OldCodingFarmer's modified)

- O(N) time and O(N) space solution
- bottom up approach
  - check leaf nodes and count them
  - root node is a univalue tree's root if
    - recursive calls on both its children return true
    - root's val is the same as its children's value if the children exist
- global res int set to 0
- helper function dfs(node, parent = value of node's parent if parent is not null else null)
  - if node is null, return true
  - store result of calling itself on node's L & R children
  - if both recursive calls returned true, res++
  - return AND'd result of 2 recursive calls and if node's val equals parentVal
- dfs(node, null or some invalid value)
- return res