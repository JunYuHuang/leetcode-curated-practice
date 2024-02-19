# [LC 1929. Concatenation of Array](https://leetcode.com/problems/concatenation-of-array/)

## General Notes:

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[1, 1000]
      - of values in range \[1, 1000]
  - output:
    - `ans`: int array that is the concatenation of two `nums` arrays
      - of size in range \[2, 2000]
      - of values in range \[1, 1000]
- PEDAC: Examples
- PEDAC: DS&A

## Solution 1: array solution

- O(N) T and O(N) S solution
- summary
  - get size of `nums` as `n`
  - loop over `n` times,
    - push `nums[n]` to `nums`
  - return `nums`
