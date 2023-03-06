# [LC 117. Populating Next Right Pointers in Each Node II](https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - head / root of binary tree that is possibly null
    - nodes not at leaf level may not have both (L & R) children
  - output:
    - head / root of modified binary tree
- PEDAC: Examples

## Solution 1: BFS iterative (brute force?)

- O(N) time and O(N) space solution
- use queue to traverse tree in level order
  - initialise prev Node pointer set to null before processing each level
  - for each level
    - curr = pop from queue front
    - if prev is not null, set prev's pointer to point to curr
    - add curr's children to queue if they exist
    - point prev to curr
- return root

## Solution 2: BFS iterative (DBabichev's modified)

- O(N) time and O(1) space solution
- similar approach to solution 1 BFS iterative but
  - replace queue with 2 pointers to do level-order traversal
  - also use nested 2 loops
- traverse tree in level-order and using existing `.next` connections
  - keep 3 Node pointers:
    - node (to traverse parent level, initially points to root)
    - curr (to traverse next level, initially points to dummy)
    - dummy (ref that points to next level's leftmost node, for updating node)
  - if node.left exists
    - connect (next pointer of) curr to it
    - move curr to next-right node in (next) level
  - do the same for node.right
  - move node to the next-right node in (current) level
  - when node finishes traversing (parent) level (i.e. points to null)
    - move node to next level's leftmost node (dummy.next)
    - optional: point dummy's next pointer to null
- return root
