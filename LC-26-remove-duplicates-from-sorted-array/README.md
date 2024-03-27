# [LC 26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range [1, 3 * 10^4]
      - of values in the range [-100, 100]
      - sorted in non-decreasing order
        - diff between `nums[i]` and its prev (`nums[i - 1]`) and next (`nums[i + 1]`) neighbours may be more than 1
  - output:
    - `res`: int count of all unique elements in `nums`
- PEDAC: Examples

## Solution 1: two pointers (NeetCode's modded)

- O(N) T and O(1) S solution
- summary
  - use 3 pointers: `left`, `right`, and `right - 1`
  - `left`: int index initially set to 1 that points to the value `nums[left]`
    - also the count of all unique elements in `nums`
    - also points to the value to be replaced if we found a new unique value
  - `right`: int index initially set to 1 that points to the value `nums[right]` that is currently traversed
  - `right - 1`: int index that points to the value `nums[right - 1]` used to compare against the value at `nums[right]`
- `left` = 1
- loop for `right` in range [1, size of `nums` - 1],
  - if `nums[right - 1]` == `nums[right]`,
    - we found a duplicate value; skip to the next iteration
  - else we found a new unique value `nums[right]`,
    - update the value at `left` with the unique value
      - `nums[left]` = `nums[right]`
    - move the `left` pointer by 1
      - `left++`
- return `left`
