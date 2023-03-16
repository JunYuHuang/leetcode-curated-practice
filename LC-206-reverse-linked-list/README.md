# [LC 206. Reverse Linked List](https://leetcode.com/problems/reverse-linked-list/)

## General Notes

- PEDAC: Problem
  - input: head node of linked list which can be null
  - ouput: head of modified linked list which can be null
  - cannot modify values of nodes
- PEDAC: Examples

## Solution 1: iterative

- O(N) time and O(1) space solution
- optional: if null head or head.next is null, return head
- initialise variables
  - prev Node pointer = null
  - curr = head
- while curr is not null
  - nxt pointer = curr.next
  - curr.next = prev
  - prev = curr
  - curr = nxt
- return prev

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