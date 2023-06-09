# [LC 167. Two Sum II - Input Array Is Sorted](https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/)

## General Notes

- PEDAC: Problem
  - input:
    - `numbers`: int array sorted in non-decreasing order
      - may have duplicate int values
      - treat array as 1-indexed
      - of size in range \[2, 3 * 10^4]
      - of values in range \[-1000, 1000]
    - `target`: int that represents the desired sum of 2 different elements from `numbers`
      - of value in range \[-1000, 1000]
  - output:
    - `res`: int array equal to `\[index1, index2]`
      - `index1`: int in range \[1, index2 - 1]
      - `index2`: int in range \[index1 + 1, `numbers`' size]
      - `index1` != `index2`
      - holds 2 1-indexed indices that represent 2 different elements from `numbers` that sum up to `target`
      - of size 2
      - of values in range \[1, `numbers`' size]
  - constraints
    - guaranteed exactly 1 solution
    - can use each element only once
    - can only use constant extra space; can only use pointers
- PEDAC: Examples

## Solution 1: two pointers

- O(N) T and O(1) S solution
- initialise variables
  - `l`: int set to 0 that represents the left pointer for `numbers`
  - `r`: int set to `numbers`' size - 1 that represents the right pointer for `numbers`
- while `l` < `r`
  - `currSum` = `numbers[l]` + `numbers[r]`
  - if `currSum` == `target`
    - return \[`l` + 1, `r` + 1]
  - else if `currSum` < `target`
    - `l++`
  - else (`currSum` > `target`)
    - `r--`
- don't need to return at end because we are guaranteed that 1 solution exists in `numbers`
