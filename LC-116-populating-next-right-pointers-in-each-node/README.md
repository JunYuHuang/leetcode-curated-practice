# [LC 116. Populating Next Right Pointers in Each Node](https://leetcode.com/problems/populating-next-right-pointers-in-each-node//)

## General Notes

- PEDAC: Problem
  - input:
    - head / root of perfect binary tree that is possibly null
  - output:
    - head / root of modified perfect binary tree
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

## Solution 2: BFS iterative (NeetCode's modified)

- O(N) time and O(1) space solution
- similar approach to solution 1 BFS iterative but
  - replace queue with 2 pointers to do level-order traversal
- initialise curr pointer to root node, nxt pointer to curr's L child else null
- curr points to a node in a level
- nxt always points to the first node in level + 1 (relative to curr)
- while nxt is not null (means there is another layer to connect)
  - connect curr's L child to curr's R child
  - if curr has an adjacent neighbour node in its level (curr.next is not null)
    - connect curr's R child to neighbour's L child
    - move curr to its next R neighbour & skip to next loop
  - else we reached end of current level (curr.next is null)
    - update curr and nxt pointers
- return root
