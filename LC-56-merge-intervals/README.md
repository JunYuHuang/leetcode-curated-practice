# [LC 56. Merge Intervals](https://leetcode.com/problems/merge-intervals/)

## General Notes

- PEDAC: Problem
  - input:
    - `intervals`: array of 2-sized int arrays
      - `intervals[i][0]` <= `intervals[i][1]`
      - of size in the range [1, 10^4]
      - `intervals[i]` is of size 2
      - `intervals[i][0]` is a value in the range [0, `intervals[i][1]`]
      - `intervals[i][1]` is a value in the range [`intervals[i][0]`, 10^5]
      - NOT always in non-decreasing / ASC order
  - output:
    - `res`: `intervals` with all its overlapping intervals merged so that only non-overlapping intervals remain
      - sorted in non-decreasing / ASC order?
  - overlapping meaning:
    - for 2 intervals `intervals[i]` and `intervals[j]`, they are considered to be overlapping if:
      - `intervals[i][0]` is a value in the range [`intervals[j][0]`, `intervals[j][1]`] OR
      - `intervals[i][1]` is a value in the range [`intervals[j][0]`, `intervals[j][1]`]
  - edge cases
    - `intervals` of size 1
- PEDAC: Examples

## Solution 1: merge intervals (NeetCode's modded)

- O(NLogN) T and O(N) S solution
- summary
  - sort `intervals`
  - initialise `res` array with `intervals[0]`
  - loop for `i` in `intervals` from 2nd el to last el,
    - if `intervals[i]` does not overlap `res[-1]`,
      - means `res[-1][1]]` < `intervals[i][0]`
      - push `intervals[i]` to `res`
    - else
      - means `intervals[i]` overlaps `res[-1]`
      - merge them and save it in `res[-1]`
      - `res[-1][1]` = max of (`res[-1][1]`, `intervals[i][1]`)
  - return `res`
