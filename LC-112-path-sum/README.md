# [LC 112. Path Sum](https://leetcode.com/problems/path-sum/)

## General Notes:

- PEDAC: Problem
  - input: root: TreeNode, targetSum: int
    - node values and targetSum can be negative
    - root may be null
  - output: bool
  - for every path traversed,
    - must start from the root node and end at a leaf node
    - leaf node is a node with no L or R children
    - only need 1 path to return true to return true for the function
- PEDAC: Examples
  - null root
    - return false
  - tree with only positive nodes and has one path = targetSum
    - return true
- PEDAC: DS&A

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- make function recursive
- for each recursive call, keep subtracting from targetSum
- base cases
  - if root is null, return false
  - if root is a leaf node and targetSum - root.val is 0, return true
- left = recursive call on root's L node with targetSum subtract root's val 
- right = recursive call on root's R node with targetSum subtract root's val 
- return true if either left or right return true

## Solution 2: DFS iterative

- O(N) time and O(N) space solution
- same approach as solution 1 DFS recursive but
  - replace recursive calls with explicit stack of elements of recursive call parameters
- optional: return false if root is null
- initialise stack with pair (root, targetSum)
- while stack is not empty:
  - node, currSum = pop from stack top
  - if node is null, skip to next loop
  - res int = currSum - node's value
  - if node is leaf node and res is 0, return true
  - push pairs (node.L, res), (node.R, res) to stack
- if finished processing tree, return false
