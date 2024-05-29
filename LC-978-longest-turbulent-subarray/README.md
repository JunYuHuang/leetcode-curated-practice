# [LC 978. Longest Turbulent Subarray](https://leetcode.com/problems/longest-turbulent-subarray/)

## General Notes

- PEDAC: Problem
  - input:
    - `arr`: non-empty int array
      - of size `n` in the range \[1, 4 \* 10^4]
      - of values in the range \[0, 10^9]
  - output:
    - `res`: int length of a max size turbulent subarray of `arr`
  - turbulent subarray:
    - subarray is sorted in alternating ASC or DESC order between each of its adjacent elements
  - can NOT modify `arr`
- PEDAC: Examples
  - TODO

## Solution 1: sliding window (NeetCode's modded)

- O(N) T and O(1) S solution
- summary: sliding window with 3 pointers `l`, `r - 1`, and `r`
- `res`: int set 1 that stores the result
- `prevSign`: string set to `=` that tracks the previous comparison between `arr[r - 1]` and `arr[r]`
- `currSign`: `prevSign` but for the current `arr[r - 1]` and `arr[r]`
- `r` expands on every iteration
- if window is a valid turbulent subarray,
  - subarray is turbulent IFF:
    - `prevSign` is not `>` and `currSign` is `>` OR
    - `prevSign` is not `<` and `currSign` is `<`
  - update `res` to `r` - `l` + 1 if it is greater than `res`
- else reset window by moving `l` pointer
  - if `arr[r - 1]` == `arr[r]`, `l` = `r`
  - else `l` = `r` - 1
- return `res`
