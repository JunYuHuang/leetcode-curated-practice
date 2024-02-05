# [LC 145. Binary Tree Postorder Traversal](https://leetcode.com/problems/binary-tree-postorder-traversal/)

## General Notes

- PEDAC: Problem
  - inputs
    - `root`: root `TreeNode` of a binary tree that
      - has nodes in the range \[0, 100]
      - has nodes of values in range \[-100, 100]
  - output
    - `res`: int array that holds the values of the nodes in the binary tree whose root is `root` ordered in postorder
  - notes
  - postorder = L subtree -> R subtree -> root

## Solution 1: DFS recursive

- O(N) time and O(N) space solution
- initialise variables
  - `res`: empty int array
- define helper `dfs(node)` function
  - return if `node` is null
  - `dfs(node.left)`
  - `dfs(node.right)`
  - push `node.val` to `res`
- `dfs(root)`
- return `res`

## Solution 2: DFS iterative ([StefanPochmann's comment on heiswyd's solution modified](https://leetcode.com/problems/binary-tree-postorder-traversal/discuss/45582/A-real-Postorder-Traversal-.without-reverse-or-insert-4ms/432681))

- O(N) time and O(N) space solution
- same approach as DFS recursive but
  - simulate implicit call stack with explicit stack
  - push R node before L node to stack b/c stack pops from end
    - need to process L node before R node for postorder
- push each node twice on the stack
- when popping a node
  - if popped node is the same node at the stack's top
    - have not reached first leftmost node yet
    - keep pushing popped node's children (R first then L) to stack if they exist
  - else if stack is empty or stack's top is not the popped node
    - finished searched with popped node
    - can process node i.e. push it to res array
