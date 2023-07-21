# [LC 19. Remove Nth Node From End of List](https://leetcode.com/problems/remove-nth-node-from-end-of-list/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: head `ListNode` of a linked list
      - guaranteed to be not null
    - linked list (starting with `head`)
      - of size in range \[1, 30]
      - of `ListNode` nodes that have values in range \[1, 100]
    - `n`: the `nth` node from the linked list counting from the end starting with 1
      - int in range \[1, size of linked list]
  - output:
    - `res`: new head `ListNode` of the linked list (with the old head `head`) with the `nth` node removed
      - guaranteed to be not null
    - new linked list (starting with `head`)
      - of size in range \[1, 100]
      - of `ListNode` nodes that have values in range \[1, 100]
  - follow-up
    - complete solution in 1-pass
- PEDAC: Examples
  - TODO

## Solution 1: iterative 2-pass

- O(N) T and O(1) S solution
- initialise pointers
  - `i`: int set to 0 that will represent the `ith` node that is currently traversed
  - `size`: int set to 0 that will count the size of the linked list starting with the node `head`
  - `dummy`: `ListNode` node pointer with arbitiary value that points to `head`
  - `prev`: node pointer that initially points to `dummy`
  - `curr`: node pointer that initially points to `head` or `dummy.next` that represents then node to delete
  - `nxt`: node pointer that initially points to `head.next`
- iterate thru list via `head` pointer to count and save its size in `size`
  - while `curr` is not null:
    - `size++`
    - `curr` = `curr.next`
- `curr` = `head`
- while `size` - `i` is not `n`:
  - move the pointers and update the `i` int count variable
    - `prev` = `curr`
    - `curr` = `curr.next`
    - `nxt` = `curr.next`
    - `i++`
- delete the node from the list
  - `prev.next` = `nxt`
  - `curr.next` = null
- return `dummy.next`

## Solution 2: two pointers 1-pass (NeetCode's modded)

- O(N) T and O(1) S solution
- initialize variables
  - `dummy`: `ListNode` node that points to dummy with some arbitrary value
  - `left`: node pointer that points initially to `dummy`
  - `right`: node pointer that points initally to `head`
- move `right` until it points to the 1-indexed `n`th node from the start of the linked list (that starts with node `head`)
  - while `n` > 0 and `right` is not null:
    - `right` = `right.next`
    - `n--`
- move the pointers `left` and `right` while maintaining their offset difference until `right` reaches the end of the list (is null)
  - while `right`:
    - `left` = `left.next`
    - `right` = `right.next`
- delete the `n`th node
  - `deleted` = `left.next`
  - `left.next` = `deleted.next`
  - `deleted.next` = null (optional)
- return `dummy.next`
