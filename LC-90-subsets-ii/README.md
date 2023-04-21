# [LC 90. Subsets II](https://leetcode.com/problems/subsets-ii/)

## General Notes

- PEDAC: Problem
  - input: 
    - `nums`: int array of size in range \[1, 10] and of values in range \[-10, 10]
  - output:
    - array of int subarrays that represent all possible unique subsets (power set)
      - order of subarrays doesn't matter
      - size ranges from 0 to N
      - order of ints in a subarray doesn't matter (we look for combinations not permutations)

- PEDAC: Examples

## Solution 1: recursive backtracking (NeetCode's expl.)

- O(N * 2^N) T & and O(N * 2^N) S solution
- sort input array `nums`
- initialise empty `res` array
- helper recursive function `backtrack(curr, i)`
  - if `i` is out of bounds,
    - push copy of `curr` to `res` and return
  - include `nums[i]`
    - push `nums[i]` to `curr`
    - backtrack(curr, i + 1)
  - exclude `nums[i]` and its duplicates
    - pop from `curr`
    - while `i + 1` is inbounds and `nums[i]` equals `nums[i + 1]`,
      - i++
    - backtrack(curr, i + 1)
- backtrack([], 0)
- return res
