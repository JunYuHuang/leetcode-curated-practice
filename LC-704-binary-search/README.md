# [LC 704. Binary Search](https://leetcode.com/problems/binary-search/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - sorted in ASC order
      - of only unique (non-duplicate) values
      - of size in range \[1, 10^4]
      - of values in range \[-10^4, 10^4]
    - `target`: an int that may or may not be in `nums`
      - of values in range \[-10^4, 10^4]
  - output:
    - `res`: int that represents the index of the value `target` in `nums` or -1 if `target` is NOT in `nums`
      - in range \[-1, size of `nums` - 1]
  - constraints
    - algorithm must have a `O(LogN)` runtime complexity
- PEDAC: Examples

## Solution 1: binary search

- O(LogN) T and O(1) S solution
- initialise variables
  - `l`: int left pointer for `nums` set to 0
  - `r`: int right pointer for `nums` set to size of `nums` - 1
- while `l` <= `r`
  - `mid` = `l` + (`r` - `l`) // 2
  - if `nums[mid]` == `target`:
    - return `mid`
  - else if `nums[mid]` < `target`:
    - `l` = `mid` + 1
  - else (`nums[mid]` > `target`):
    - `r` = `mid` - 1
- return -1
