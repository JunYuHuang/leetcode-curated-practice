# [LC 80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range [1, 3 * 10^4]
      - of values in the range [-10^4, 10^4]
      - sorted in non-decreasing order
        - diff between `nums[i]` and its prev (`nums[i - 1]`) and next (`nums[i + 1]`) neighbours may be more than 1
  - output:
    - `k`: int count of all unique elements that appear at most twice in `nums`
  - constraints
    - must modify `nums` in-place to so that:
      - unique elements appear at most twice in the first `k` elements of `nums`
      - the relative (non-decreasing) order of elements in `nums` must be kept the same
      - does not matter which elements are in `nums` after the first `k` elements
    - cannot use extra space for another array; must use O(1) extra memory
- PEDAC: Examples

## Solution 1: two pointers (@sergiofranklin8809 on NeetCode's YT solution video's modded)

- O(N) T and O(1) S solution
- summary
  - use 3 pointers `left`, `right`, and `right - 1`
  - `count`: int set to 1
    - count of last unique element in `nums`
  - `left`: int set to 1
    - size of new modified `nums`
    - points to element in `nums` to be updated
  - `right`: int set to 1
    - current element iterated in `nums`
  - `right - 1`: int set to 0
    - points to prev element iterated in `nums`
  - loop for `right` in range [1, size of `nums` - 1],
    - if `nums[right - 1]` == `nums[right]`,
      - found duplicate; `count++`
    - else,
      - found unique; `count` = 1
    - if `count` < 3,
      - means last unique value appeared once or twice
      - update the value at `nums[left]` and move `left` forward by 1
        - why?
      - `nums[left]` = `nums[right]`
      - `left++`
  - return `left`
