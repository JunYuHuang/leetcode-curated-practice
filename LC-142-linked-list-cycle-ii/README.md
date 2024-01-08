# [LC 142. Linked List Cycle II](https://leetcode.com/problems/linked-list-cycle-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: first `ListNode` node of a linked list
      - may be null
    - linked list (that starts with `head`)
      - has nodes in the range \[0, 10^4]
      - has nodes of values in the range \[-10^5, 10^5]
      - may not have a cycle
      - if has a cycle, there exists a valid node that starts the cycle
      - nodes may have duplicate values
  - output:
    - `res`: `ListNode` node that begins the cycle or null if there is no cycle
      - for a non-null node that starts the cycle,
        - it has 2 nodes pointing to it if it is not the head node
        - it has 1 node pointing to it if it is the head node
  - constraints
    - cannot modify list
  - follow-up
    - solve in O(1) memory
- PEDAC: Examples
  - TODO

## Solution 1: brute force

- O(N) T and O(N) S solution
- summary
  - use `cur` pointer to traverse list in order while `cur` is not null
  - use `visit` set to store visited `ListNode` nodes
  - in while loop,
    - if `cur` is in `visit`,
      - return `prev`
    - add `cur` to `visit`
    - `cur` = `cur.next`
  - if exited while loop,
    - return null

## Solution 2: slow and fast pointers (2 pointers)

- O(N) T and O(1) S solution
- summary
  - return null if list is empty (null `head`) or list is non-cyclic and of size 1 (null `head.next`)
  - set `fast` and `slow` pointers initially to `head`
  - while both `fast` and `fast.next` are not null,
    - move `slow` pointer forward (in list) by 1 node
    - move `fast` pointer forward (in list) by 2 nodes
    - break out of loop if both pointers are pointing at the same node
  - if list is non-cyclic,
    - even-sized non-cyclic lists have a null `fast` pointer
    - odd-sized non-cyclic lists have a null `fast.next` pointer
    - return null
  - set `slow2` pointer pointing initially to `head`
  - while both `slow2` and `slow` pointers are not pointing at the same node,
    - move each pointer forward (in list) by 1 node
  - return either pointer
- TODO: proof and explanation for why this algorithm works
