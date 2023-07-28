# [LC 2. Add Two Numbers](https://leetcode.com/problems/add-two-numbers/)

## General Notes

- PEDAC: Problem
  - input:
    - `l1`, `l2`: `ListNode` heads of 2 linked lists
      - guaranteed to be not null
    - linked list (starting with `head`)
      - of size in range \[1, 100]
      - of `ListNode` nodes of values in range \[0, 9]
      - guaranteed that it does not represent an integer with leading zeroes
      - represents an integer's digits as its nodes in reverse order
  - output:
    - `res`: head `ListNode` of the new linked list
      - sum of integers represented by lists `l1` and `l2`
      - represents sum in reverse order
      - guaranteed to be not null
    - new linked list (starting with `res`)
      - of size in range \[1, 101]
      - of `ListNode` nodes of values in range \[0, 9]
- PEDAC: Examples
  - TODO

## Solution 1: iterative

- O(N) T and O(N) S solution
- initialise variables
 - `dummy`: `ListNode` node whose next pointer will point to the head node of the new resulting reversed sum linked list
 - `carryDigit`: int set to 0 that represents the carried over digit from single-digit addition that results in a 2-digit sum
 - `prev`: `ListNode` pointer that points to the previous node in the resulting linked list that points initially to `dummy`
- while `l1` or `l2`:
  - `l1Val` = `l1.val` if `l1` is not null else 0
  - `l2Val` = `l2.val` if `l2` is not null else 0
  - `intSum` = `l1Val` + `l2Val` + `carryDigit`
  - `carryDigit` = `intSum` // 10
  - `lastDigit` = `intSum` % 10
  - `prev.next` = `ListNode(lastDigit)`
  - `prev` = `prev.next`
  - `l1` = `l1.next` if `l1` is not null else 0
  - `l2` = `l2.next` if `l2` is not null else 0
- if `carryDigit` > 0:
  - `prev.next` = `ListNode(carryDigit)`
- return `dummy.next`
