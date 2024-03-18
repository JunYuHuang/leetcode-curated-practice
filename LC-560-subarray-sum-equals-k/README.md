# [LC 560. Subarray Sum Equals K](https://leetcode.com/problems/subarray-sum-equals-k/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range [1, 2 * 10^4]
      - of values in the range [-1000, 1000]
    - `k`: int of a value in the range [-10^7, 10^7]
  - output:
    - `res`: int count of all subarrays in `nums` int elements sum up to `k`
  - subarrays are of size in the range [1, size of `nums`]
- PEDAC: Examples

## Solution 1: prefix sums (NeetCode's modded)

- O(N) T and O(N) S solution
- summary
  - use a hashmap `sumToCount` that maps each prefix sum to its occurrences in `nums`
    - initialize with key-value pair `(0, 1)` to allow for calculating prefix sums that don't need to remove an earlier part of its subarray to sum up to `k`
    - `sumToCount[s]`: means there are `sumToCount` subarrays that sum up to `k` from index 0 to some index `i`
- initialize variables
  - `sumToCount`: hashmap that maps each prefix sum int to its int count in `nums`
  - `res`: int set to 0 that will hold the result
  - `currSum`: int set to 0 used keep a running total sum for deriving the current prefix sum
- loop for `i` in range [0, size of `nums` - 1],
  - `currSum` += `nums[i]`
  - `targetSum`: `currSum` - `k`
  - if `targetSum` is in `sumToCount`,
    - `res` += `sumToCount[targetSum]`
  - `sumToCount[currSum]` += 1
    - create the key-value pair first if it did not exist in `sumToCount` previously
- return `res`
