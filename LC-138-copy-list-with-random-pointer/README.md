# [LC 138. Copy List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/)

## General Notes

- PEDAC: Problem
  - input:
    - `head`: head `Node` of a linked list
      - may be null
    - linked list (starting with `head`)
      - of size in range \[0, 1000]
      - of `Node` nodes that have values in range \[-10^4, 10^4]
  - output:
    - `res`: new head `Node` of the deep copied / cloned linked list
      - may be null
    - new linked list (starting with `head`)
      - of size in range \[0, 1000]
      - of `Node` nodes that have values in range \[-10^4, 10^4]
  - each `Node` has:
    - `value`: an int property
    - `next`: a pointer that points to the next `Node` in the linked list
    - `random`: a pointer that either points to null or some random `Node` in the linked list
  - constraints:
    - only given the `head` `Node` of the original list
    - return the copied `head` `Node` of the copied list
  - TODO: create a deep copy of the original linked list that starts with `head` that meets the following requirements:
    - for a `copy` `Node` that is a deep copy of some `orig` original `Node`:
      - `copy.val` = `orig.val`
      - `copy.next`: points to the `Node` in the copy list with the value of the original node that `orig.next` points to in the original list
      - `copy.random`:  points to the `Node` in the copy list with the value of the original node that `orig.random` points to in the original list
- PEDAC: Examples
  - TODO

## Solution 1: iterative two-pass

- O(N) T and O(N) S solution
- return null if `head` is null
- initialise variables
  - `nodeToCopy`: initially empty hashmap that will map each `Node` from the original linked list to a copy of it in the copied list
  - `curr`: pointer that points initially to `head`
- iterate thru the original list to create copies for all of its `Node`s
- while `curr` is not null:
  - `nodeToCopy[curr]` = `Node(curr.val)`
  - `curr` = `curr.next`
- iterate thru the original list again to update the pointers for all of `Node`s in the copied list
  - `curr` = `head`
  - while `curr` is not null:
    - `nodeToCopy[curr].next = nodeToCopy[curr.next]`
    - `nodeToCopy[curr].random = nodeToCopy[curr.random]`
    - `curr` = `curr.next`
- return `nodeToCopy[head]`
