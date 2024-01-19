# [LC 701. Insert into a Binary Search Tree](https://leetcode.com/problems/insert-into-a-binary-search-tree/)

## General Notes

- PEDAC: Problem
  - input:
    - `root`: root node of a BST
      - may be null
      - BST
        - has nodes in the range [0, 10^4]
        - has nodes whose values are all unique
        - guaranteed to not have a node with value equal to `val`
    - `val`: int of a node to insert into the BST
      - in the range [-10^8, 10^8]
  - ouput:
    - `root`: root node of the modified BST
  - BST = special binary tree where for each node,
    - node.L.val < node.val < node.R.val
  - if `root` is null,
    - return node with value `val`
  - find parent node for new node with value `val`
    - parent node may be a leaf or node with 1 child
    - parent node can never have 2 children
- PEDAC: Examples

## Solution 1: iterative

- O(LogN) T and O(1) S solution
- if `root` is null,
  - return a new node created with value `val`
- `prev` = null
- `curr` = `root`
- while `curr` is not null,
  - `prev` = `curr`
  - if `curr.val` < `val`,
    - `curr` = `curr.right`
  - else
    - `curr` = `curr.left`
- if `prev.val` < `val`,
  - `prev.right` = `Node(val)`
- else
  - `prev.left` = `Node(val)`
- return `root`

## Solution 2: recursive

- O(LogN) T and O(LogN) S solution
- summary
  - make recursive calls on each node on the path from `root` to the parent node of the to-be inserted new node with value `val`
  - re-updates the pointers (that connect a parent with its left or right child) for each node on the path while traversing down the tree
- make function itself `insertIntoBST(root, val)` recursive
  - if `root` is null,
    - return `TreeNode(val)`
  - if `val` > `root.val`,
    - `root.right` = `insertIntoBST(root.right, val)`
  - else,
    - `root.left` = `insertIntoBST(root.left, val)`
  - return `root`
