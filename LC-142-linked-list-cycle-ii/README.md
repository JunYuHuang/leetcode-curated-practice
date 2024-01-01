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
    - `res`: `ListNode` node that begins the cycle (node that has 2 nodes whose next pointers point to it) or null if there is no cycle
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
