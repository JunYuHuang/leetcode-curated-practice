# [LC 24. Swap Nodes in Pairs](https://leetcode.com/problems/swap-nodes-in-pairs/)

## General Notes

- PEDAC: Problem
  - input: head node of linked list which can be null
  - ouput: head of modified linked list which can be null
  - cannot modify values of nodes
- PEDAC: Examples

## Solution 1: iterative (NeetCode's)

- O(N) time and O(1) space solution
- initialise variables
  - dummy Node whose next points to head
  - prev = dummy, curr = head
- while both curr and curr.next are not null (since we are only swapping each pair)
  - save pointers
    - nextPair = curr.next.next
    - second = curr.next
  - reverse this pair
    - second.next = current
    - curr.next = nextPair
    - prev.next = second
  - update pointers
    - prev = curr, curr = nextPair
- return dummy.next
  - somehow points to head.next from original list??

<!-- ## Solution 2: recursive

- O(N) time and O(N) space solution -->