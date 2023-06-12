# [LC 15. 3Sum](https://leetcode.com/problems/3sum/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: unsorted int array
      - may have duplicate int values
      - of size in range \[3, 3000]
      - of values in range \[-10^5, 10^5]
  - output:
    - `res`: 2D array of int subarrays that collectively represent all unique triplets that sum to 0
      - `res[i]`:
        - int array containing values from `numbers`
        - values may be duplicates
        - cannot use the same element (by index) more than once
        - is of size 3
        - of all of its int elements sum up to 0
- PEDAC: Examples

## Solution 1: two pointers (NeetCode's modded)

- O(N^2) T and O(min(1, N)) S solution
- TLDR; loop thru sorted `nums` and use solution for `LC 1. Two Sum`
- initialise empty `res` array
- sort array `nums`
- loop thru each index `i` in `nums`
  - break out of loop if `nums[i]` is positive b/c we know the window defined by `l` and `r` will never be negative
  - if `i` > 0 and `nums[i]` is the same as the prev el `nums[i - 1]`
    - continue to next iteration
  - initialise pointers for `nums`
    - `l`: int set to `i + 1`
    - `r`: int set to `nums`' size - 1
  - while `l` < `r`
    - `currSum` = `nums[i]` + `nums[l]` + `nums[r]`
    - if `currSum` == 0
      - push `[nums[i], nums[l], nums[r]]` to `res`
      - `l += 1`
      - while `nums[l]` == `nums[l - 1]` and `l` < `r`
        - `l++`
    - else if `currSum` < 0
      - `l++`
    - else (`currSum` > 0)
      - `r--`
- return `nums`
