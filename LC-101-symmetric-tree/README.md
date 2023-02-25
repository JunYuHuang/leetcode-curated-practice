# [LC 101. Symmetric Tree](https://leetcode.com/problems/symmetric-tree/)

## General Notes

- root guaranteed to be not null i.e. tree has at least 1 node

## Solution 1: BFS iterative

- O(N) time and O(N) space solution
- traverse tree in level order using queue
  - add both null (if L or R child curr doesn't exist) and non-null nodes to queue
  - if popped node is null, don't do anything
- for every level in tree while queue is not empty
  - return false if nodes in current level aren't a palindrome
- if finish processing entire queue, return true

## Solution 2: DFS recursive (Nick White's modified)

- O(N) time and O(N) space solution
- helper recursive function mirror(L, R) to recursively compare the root's L and R subtrees
  - if both L and R are null, return true
  - if one of either L or R is null but the other is not, return false
  - return if L's val equals R's val and recursive call on (L.L, R.R) and (L.R, R.L)
- return mirror(root.L, root.R)

## Solution 3: DFS iterative (OldCodingFarmer's modified)

- O(N) time and O(N) space solution
- same approach as solution DFS recursive but
  - replace recursive calls and implicit call stack with explicit stack
  - use stack of pairs (nodeLeft, nodeRight) for stack
  - initialise stack with a pair from root's L and R nodes
- optional: return true if root is empty
- while stack is not empty
  - l, r = pop pair from stack
  - skip to next loop if both nodes are null
  - if one either l or r is null but the other isn't return false
  - if their values aren't equal, return false
  - add pairs to stack: (l.l, r.r), (l.r, r.l)
- return true if finished processing tree with stack
