# [LC 724. Find Pivot Index](https://leetcode.com/problems/find-pivot-index/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range [1, 10^4]
      - of values in the range [-1000, 1000]
  - output:
    - `res`: int that is the leftmost pivot index or -1 if it does not exist in `nums`
      - pivot index = `i` in `nums` such that `sum(nums[0:i])` == `sum(nums[i + 1:])`
      - of a value in the range \[-1, size of `nums` - 1]
- PEDAC: Examples

## Solution 1: prefix sums

- O(N) T and O(N) S solution
- summary
  - compute prefix sums array for `nums` in `prefixSums`
  - neither `leftSum` or `rightSum` include `nums[i]` where `i` is the pivot index
  - `numsLen` = size of `nums`
  - loop for `i` for range [0, `numsLen` - 1],
    - `leftSum` = `i` == 0 ? 0 : `prefixSums[i - 1]`
    - `rightSum` = `i` == `numsLen` - 1 ? 0 : `prefixSums[numsLen - 1]` - `prefixSums[i]`
    - if `leftSum` == `rightSum`,
      - return `i`
  - return -1

## Solution 2: prefix sums optimized (NeetCode's modded)

- O(N) T and O(1) S solution
- same approach as solution 1 with some changes:
  - simulate computed prefix sums array from solution 1 with `leftSum`, `rightSum`, and `total` variables only
  - `total` = `sum(nums)`
  - compute `leftSum`:
    - initialize as 0
    - when looping thru `nums`, += `nums[i]` before next loop
  - compute `rightSum`:
    - when loop thru `nums`, = `total` - `nums[i]` - `leftSum`
