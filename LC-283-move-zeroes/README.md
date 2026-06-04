# [LC 283. Move Zeroes](https://leetcode.com/problems/move-zeroes/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of length in range \[1, 10^4]
      - of values in range \[-2^31, 2^31 - 1]
  - output:
    - null
  - side effects:
    - `nums`: int array is modified so that
      - its stays the same size
      - it has the same elements
      - elements are reordered so that all 0's are moved to the end of the array
      - all non-zero elements are shift to the start of the array with their relative order preserved
  - must modify `nums` in-place without making a copy of it
    - i.e., space complexity is at most O(1) 
- PEDAC: Examples

## Solution 1: NeetCode's quicksort / 2-pointer modded solution

- O(N) T + O(1) S solution
- gist: move all non-zero elements to the left side of the `nums` array
- set int index `l` to 0
- for each int index `r` in `nums` from 0 to length of `nums` - 1 inclusive:
  - if `nums[r]` is not 0,
    - swap values in `nums[l]` and `nums[r]` with each other
    - increment `l` by 1
