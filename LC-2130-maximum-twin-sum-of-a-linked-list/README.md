# [LC 2130. Maximum Twin Sum of a Linked List](https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/)

## General Notes

- PEDAC: Problem
  - input(s):
    - `head`: a ListNode that is the start or head of the list
      - of a value in the range \[1, 10^5]
      - the head node of an even-sized list of a size in range \[2, 10^5]
      - guaranteed to be not null
  - output(s):
    - `res`: an int that represents the maximum twin sum of all twin nodes in the list that starts with node `head`

## Solution 1: two pointers linked list solution

- O(N) T and O(1) S solution
- summary
  - use `slow` and `fast` pointers to traverse list until `fast` is null
    - `slow` should be pointing to start of 2nd half of list
  - split list into 2 where node before `slow` points to `slow` node
  - reverse 2nd half of list that starts with `slow` node
  - iterate thru both lists at same time start from their head nodes (`head` and original tail node of combined list) to compute sum of each twin node pair
  - return max twin sum
- initialise variables
  - `slow`: slow pointer that points initially to `head`
  - `fast`: fast pointer that points initially to `head`
  - `prev`: pointer that points to node before `fast` that is initially null
  - `res`: int set to 0 that represents the max twin sum of the list
- while `fast` is not null,
  - `prev` = `slow`
  - `slow` = `slow.next`
  - `fast` = `fast.next.next`
- reverse the 2nd half of the list
  - `prev.next` = null
  - `nxt` = null
  - while `slow`,
    - `nxt` = `slow.next`
    - `slow.next` = `prev`
    - `prev` = `slow`
    - `slow` = `nxt`
- iterate thru both equally sized sublists at same time starting from both their heads to get the max twin sum
  - while `head` and `prev`,
    - `res` = `max(res, head.val + prev.val)`
    - `head` = `head.next`
    - `prev` = `prev.next`
- return `res`
