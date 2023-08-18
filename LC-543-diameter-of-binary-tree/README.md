# [LC 543. Diameter of Binary Tree](https://leetcode.com/problems/diameter-of-binary-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a binary tree
      - guaranteed to be not null
      - if not null, has a value in the range \[-100, 100]
    - binary tree whose root node is `root`
      - has nodes in the range \[1 10^4]
      - has nodes whose values are in the range \[-100, 100]
  - output:
    - `res`: int that represents the diameter of the tree whose root node is `root`
      - in the range \[0, 10^4]
  - tree diameter = length of longest path between any 2 nodes in a tree
    - length of path is count of edges between those 2 nodes
    - may pass thru `root`
- PEDAC: Examples
  - tree with 1 node with no children has diameter 0
  - tree with 3 nodes each with no children has diameter 1
  - tree that has no nodes has diameter -1

## Solution 1: DFS recursive bot-up (NeetCode's modded)

- O(N) T and O(N) S solution
- brief
  - considers null nodes as having height -1
  - considers nodes with no children as having height 0
  - calculates diameter of a node = L's height + R's height + 2
  - calculates height of a node = 1 + max(L's height, R's height)
- initialise variables
  - `res`: int set to 0 that represents the max diameter of the tree that starts with the root node `root`
- helper recursive function `dfs(curr)` that returns the height of node `curr` and updates `res` if a new max diameter was found
  - return -1 if `curr` is null
  - `leftHeight` = `dfs(curr.left)`
  - `rightHeight` = `dfs(curr.right)`
  - `diameter` = `leftHeight` + `rightHeight` + 2
  - if `diameter` > `res`, update `res` to be `diameter`
  - `height` = `leftHeight` + `rightHeight` + 2
  - return `height`
- `dfs(root)`
- return `res`
