# [LC 918. Maximum Sum Circular Subarray](https://leetcode.com/problems/maximum-sum-circular-subarray/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size `n` in the range \[1, 3 \* 10^4]
      - of values in the range \[-3 \* 10^4, 3 \* 10^4]
      - is circular; its end el connects to its start el
      - for any of its subarrays `sub`,
        - it has at most `n` elements
  - output:
    - `res`: int sum of subarray with the max sum in `nums`
      - subarray is non-empty
  - can NOT modify `nums`
- PEDAC: Examples
  - `nums` of all negative ints
  - `nums` of size ?

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- summary
  - use modified version of Kadane's Algorithm
  - loop thru each el `n` in `nums` and manage these variables
    - `curMaxSum`: int set to 0 that is the current max sum equal to itself plus `n` or `n`
    - `maxSum`: int set to `nums[0]` that is the max sum of a subarray encountered in `nums` so far
    - `curMinSum`: `curMaxSum` but for current min sum
    - `minSum`: `maxSum` but for min sum
    - `totalSum`: int set to 0 that is the current running total of `nums`
- if all els in `nums` were negative,
  - means `maxSum` < 0
  - return `maxSum`
- return the max of (`maxSum`, `totalSum` - `minSum`)
