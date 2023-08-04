# [LC 287. Find the Duplicate Number](https://leetcode.com/problems/find-the-duplicate-number/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range \[2, 10^5 + 1]
      - of values in the range \[1, 10^5]
      - has 1 number duplicated or repeated at least once
  - output:
    - `res`: the duplicated int number that appears 2+ times in `nums`
      - of a value in the range \[1, 10^5]
  - constraints
    - cannot modify `nums`
    - solve in O(1) space
  - follow-up
    - how to prove at least duplicate number must exist in `nums`?
    - solve in O(N) time
  - return `nums[0]` if `nums` is of size 2
- PEDAC: Examples
  - TODO

## Solution 1: fast and slow pointers (NeetCode's modded)

- O(N) T and O(1) S solution
- brief:
  - treat `nums` like a linked list that is guaranteed to have a cycle where each "node" has the value `i` and points to its next "node" `nums[i]`
  - apply tortoise and hare AKA Floyd's Algorithm on `nums` to find the cycle and return when the cycle is found
  - use `slow` and `fast` pointer with Floyd's Algorithm to find the first "node" that they both point to or meet
    - this node is not necessarily the duplicate number but it is part of the cycle
  - use a second `slow2` pointer that points initially to the first "node" and move it along with where the `slow` pointer was until they both meet
    - this is the duplicate number / "node"
  - duplicate number is the "node" that starts the cycle
    - i.e. it has 2+ other "nodes" that point to it
- initialise variables
  - `slow`: int pointer for traversing `nums` 1 value or 1 "node" at a time set initially to 0 that is the first value or "node" of the list and guaranteed to be outside the cycle b/c no other "node" points to index 0
  - `fast`: int pointer for traversing `nums` 2 values or 2 "nodes" at a time set initially to 0 that is the first value or "node" of the list and guaranteed to be outside the cycle b/c no other "node" points to index 0
- while true
  - `slow` = `nums[slow]`
  - `fast` = `nums[nums[fast]]`
  - if `slow` == `fast`, break
- `slow2` = 0
- while true
  - `slow2` = `nums[slow2]`
  - `slow` = `nums[slow]`
  - if `slow` == `slow2`, return `slow` (or `slow2`)
