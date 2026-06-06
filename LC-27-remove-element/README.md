# [LC 27. Remove Element](https://leetcode.com/problems/remove-element/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of length in range \[0, 100]
      - of values `nums[i]` in range \[0, 50]
    - `val`: int
      - of values in range \[0, 100]
  - output:
    - `k`: int
      - = length of `nums` - occurrences of `val` in `nums`
      - of value in range \[0, 100]
  - side effects:
    - reorders ints in `nums` so that:
      - all occurrences of `val` are moved to the end of `nums`
      - relative order of non-`val` elements can be disregarded and be in any order
- PEDAC: Examples
  - TODO

## Solution 1: NeetCode's 2-pointer (quicksort select) modded solution

- O(n) T + O(1) S solution
- set int `numsLen` to length of `nums`
- set int `k` to 0
- for index int `i` from 0 to `numsLen` - 1 inclusive:
  - if `nums[i]` != `val`:
    - set `nums[k]` = `nums[i]`
    - increment `k` by 1
- return `k`
