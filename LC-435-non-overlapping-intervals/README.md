# [LC 435. Non-overlapping Intervals](https://leetcode.com/problems/non-overlapping-intervals/)

## General Notes

- PEDAC: Problem
  - input:
    - `intervals`: array of 2-sized int arrays
      - `intervals[i][0]` <= `intervals[i][1]`
      - of size in the range [1, 10^5]
      - `intervals[i]` is of size 2
      - `intervals[i][0]` is a value in the range [-5 \* 10^4, `intervals[i][1]`]
      - `intervals[i][1]` is a value in the range [`intervals[i][0]`, 5 \* 10^4]
      - NOT always in non-decreasing / ASC order
  - output:
    - `res`: count of min intervals in `intervals` to remove so they are no overlapping intervals in `intervals`
  - overlapping meaning:
    - intervals `intervals[i]` and `intervals[j]` are overlapping if:
      - `intervals[i][0]` is a value in the range [`intervals[j][0]`, `intervals[j][1] - 1`] OR
      - `intervals[i][1]` is a value in the range [`intervals[j][0] + 1`, `intervals[j][1]`]
    - EXCLUDES intervals where one interval's end point is the same as another interval's start point
  - edge cases
    - `intervals` of size 1
- PEDAC: Examples

## Solution 1: merge intervals (NeetCode's modded)

- O(NLogN) T and O(1) S solution
- summary
  - sort `intervals` in non-decreasing order
  - use greedy approach to "remove" intervals
  - initialise variables
    - `res`: int count of removed intervals set to 0
    - `lastEnd`: int endpoint of the last interval set to last endpoint of first interval (`intervals[0][1]`)
  - loop for `i` from 2nd index to last index in `intervals`
    - if `intervals[i]` overlaps with `lastEnd`,
      - means `intervals[i][0]` < `lastEnd`
      - "remove" the longer interval of the two
        - why?
          - it lowers the odds of conflicting / overlapping with the next interval
        - means to keep the interval that ends first
        - set `lastEnd` to min of (`lastEnd`, `intervals[i][1]`)
        - `res++`
    - else,
      - means there is no overlap
      - set `lastEnd` to the current interval's end
        - `lastEnd` = `intervals[i][1]`
  - return `res`
