# [LC 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: head `ListNode` of a linked list
      - may be null
      - of values in range \[-5000, 5000]
    - linked list
      - of values in range \[-5000, 5000]
      - of size in range \[0, 5000]
  - ouput:
    - `res`: head `ListNode` of reversed linked list (from `head`)
      - may be null
      - of values in range \[-5000, 5000]
  - cannot modify values of nodes?
- PEDAC: Examples

## Solution 1: iterative

- O(N) T and O(1) S solution
- optional: return `head` if `head` is null or `head.next` is null
- initialise variables
  - `prev`: pointer that points to prev `ListNode` in the linked list set to null
  - `curr`: pointer that points to current `ListNode` in the linked list set to `head`
- while `curr` is not null,
  - save the next node in a pointer `nxt`
    - `nxt` = `curr.next`
  - point `curr`'s next pointer to `prev`
    - `curr.next` = `prev`
  - update pointers for `prev` and `next`
    - `prev` = `curr`
    - `curr` = `nxt`
- return `prev`

## Solution 2: recursive

- O(N) time and O(N) space solution
- same approach as solution 1 iterative but
  - replace while loop with recursive helper function
- helper recursive function rev(prev, curr)
  - if curr is null, return prev
  - nxt = curr.next
  - curr.next = prev
  - return (curr, nxt)
- return rev(null, head)
