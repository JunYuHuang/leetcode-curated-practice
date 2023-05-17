# [LC 238. Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[2, 10^5]
      - of values in range \[-30, 30]
  - output:
    - `answer`: int array
      - whose size = `nums`'s size
      - whose `answer[i]` = product of every int in `nums` except `nums[i]`
  - constraints
    - must write O(N) time algorithm
    - cannot use division operator
    - follow up = solve in O(1) space (excludes output array)
- PEDAC: Examples

## Solution 1: prefix product (NeetCode's modded)

- O(N) T and O(1) S solution
- use prefix and postfix arrays
  - that are of same size as input array `nums`
  - where `prefix[i]` = product of all ints left of `nums[i]`
  - where `postfix[i]` = product of all ints right of `nums[i]`
  - if `nums[i]` has no ints to its left or right,
    - `prefix[i]` or `postfix[i]` = 1
  - multiply `prefix[i]` and `postfix[i]` to get result for `nums[i]`
- can "store" both prefix and postfile arrays in a single `res` array to save space
- initialise varialbes
  - `res`: array of all 1's to the same size as `nums`
  - `cumProduct`: int set to 1 that represents cumulative product of consecutive ints in `nums` at a certain point of time
- loop thru `nums` with index `i` and build prefix array
  - `res[i]` = `cumProduct`
  - `cumProduct` *= `nums[i]`
- `cumProduct` = 1
- loop thru `nums` with index `i` in reverse and multiply postfix array with prev prefix array
  - `res[i]` *= `cumProduct`
  - `cumProduct` *= `nums[i]`
- return `res`
