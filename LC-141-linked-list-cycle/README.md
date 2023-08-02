# [LC 141. Linked List Cycle](https://leetcode.com/problems/linked-list-cycle/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: first `ListNode` node of a linked list
      - may be null
    - linked list (that starts with `head`)
      - has nodes in the range \[0, 10^4]
      - has nodes of values in the range \[-10^5, 10^5]
  - output:
    - `res`: a boolean that represents if there is a cycle in the list (true) or not (false)
  - can return false if `head` is null
- PEDAC: Examples
  - TODO

## Solution 1: fast and slow pointers

- O(N) T and O(1) S solution
- initialise variables
  - `slow`: `ListNode` pointer that points initially to `head` and will traverse the list one node at a time
  - `fast`: `ListNode` pointer that points initally to `head.next` if `head` is null else null and will traverse the list two nodes at a time
- while both `slow` and `fast` are not null:
  - return true if both `slow` and `fast` are pointing to the same node
    - if `slow` == `fast`, return true
  - update the pointers to continue traversing the list
    - `slow` = `slow.next`
    - `fast` = `fast.next.next` if `fast.next` is not null else `null`
- return false

## Solution 2: fast and slow pointers (NeetCode's modded)

- O(N) T and O(1) S solution
- initialise variables
  - `slow`: `ListNode` pointer that points initially to `head` and will traverse the list one node at a time
  - `fast`: `ListNode` pointer that points initally to `head` and will traverse the list two nodes at a time
- while `fast` is not null and `fast.next` is not null
  - `slow` = `slow.next`
  - `fast` = `fast.next.next`
  - if `slow` == `fast`, return true
- return false
