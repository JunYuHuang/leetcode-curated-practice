# [LC 303. Range Sum Query - Immutable](https://leetcode.com/problems/range-sum-query-immutable/)

## General Notes:

- PEDAC: Problem
  - class methods and inputs
    - `NumArray()` constructor
      - input: int array `nums`
      - output: a `NumArray` object
    - `sumRange(left, right)` method
      - input: int `left`, int `right`
      - output: an int `res` equal to the sum of all ints from a subarray of `nums` from index `left` to `right` inclusive (i.e. `nums[right]` is included)
  - constraints
    - `nums`: int array of size in the range \[1, 10^4]
    - `nums[i]`: an int in the range \[-10^5, 10^5]
    - `left`: an int in the range \[0, `right`]
    - `right`: an int in the range \[`left`, size of `nums` - 1]
    - at most 10^4 calls made to `sumRange()`
- PEDAC: Examples
- PEDAC: DS&A

## Solution 1: brute force

- O(N) T and O(1) S `sumRange()` solution
- summary
  - `sumRange(left, right)` iterates thru `nums` from `left` to `right` and returns the cumulative sum of the subarray

## Solution 2: prefix sums (NeetCode's modded)

- O(1) T and O(1) S `sumRange()` solution
- summary
  - `NumArray(nums)` constructor:
    - create `prefix` int array
      - same size as `nums`
      - `prefix[i]` = running total sum of `nums` from index 0 to `i`
  - `sumRange(left, right)`:
    - `prefixLeft` = 0 if `left` - 1 < 0 else `prefix[left - 1]`
    - return `prefix[right]` - `prefixLeft`
