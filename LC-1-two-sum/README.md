# [LC 1. Two Sum](https://leetcode.com/problems/two-sum/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[2, 10^4]
      - of values in range \[-10^9, 10^9]
      - may have duplicate values
    - `target`: int in range \[-10^9, 10]
  - output:
    - int array of size 2 that contains the indices of 2 ints in `nums` that sum up to `target`
    - indices are not the same
  - guaranteed exactly 1 valid answer exists
  - order in output array does not matter
- PEDAC: Examples

## Solution 1: hashmap

- O(N) time and O(N) space solution
- if `nums` is of size 2, return [0, 1]
- initialise empty hashmap `valToPos`
- loop thru each el in `nums`
  - `diff` = `target` - `nums[i]`
  - if `diff` in `valToPos`,
    - return [i, `valToPos[diff]`]
  - add el and its pos (i) to `valToPos`
