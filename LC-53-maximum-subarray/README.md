# [LC 53. Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size in the range \[1, 10^5]
      - of values in the range \[-10^4, 10^4]
  - output:
    - `res`: int sum of subarray with the max sum in `nums`
  - can NOT modify `nums`
- PEDAC: Examples
  - `nums` of all negative ints
  - `nums` of size

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- summary:
  - use modified version of Kadane's algorithm
  - reset current running sum to zero if it is negative
  - if all elements in `nums` are negative, return its max element
- initialise variables
  - `res`: int set to `nums[0]`
  - `curSum`: int set to 0 that tracks the running sum
  - `hasPositive`: bool flag set to false that tracks if `nums` has a positive int or not
  - `maxEl`: int set to `nums[0]` that tracks the max encountered element in `nums`
- loop for each el `n` in `nums`,
  - update `maxEl` and `hasPositive` in case all elements in `nums` are negative
    - `maxEl` = max of (`maxEl`, `n`)
    - if `n` > 0,
      - `hasPositive` = true
  - reset `curSum` if it is negative
    - if `curSum` < 0,
      - `curSum` = 0
  - `curSum` += `n`
  - `res` = max of (`res`, `curSum`)
- return `hasPositive` ? `res` : `maxEl`
