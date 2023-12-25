# [LC 876. Middle of the Linked List](https://leetcode.com/problems/middle-of-the-linked-list/)

## General Notes

- PEDAC: Problem
  - input(s):
    - `head`: a ListNode that is the start or head of the list
  - output(s):
    - `res`: the middle or second middle (for even-sized lists) ListNode of the linked list that starts with the node `head`
  - constraints
    - `head`: a ListNode with a value in the range \[1, 100]
      - is the head node of a list of a size in range \[1, 100]
      - guaranteed to be not null
  - return `head` if list size is 1

## Solution 1: two pointers linked list solution

- O(N) T and O(1) S solution
- initialise variables
  - `slow`: ListNode pointer that points initially to `head`
  - `fast`: ListNode pointer that points initially to `head`
- while `fast` and `fast.next` are both not null,
  - `slow`: `slow.next`
  - `fast`: `fast.next.next`
- return `slow`
