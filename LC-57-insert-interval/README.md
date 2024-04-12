# [LC 57. Insert Interval](https://leetcode.com/problems/insert-interval/)

## General Notes

- PEDAC: Problem
  - input:
    - `intervals`: array of 2-sized int arrays
      - sorted in ascending order by `intervals[i][0]`
      - `intervals[i][0]` <= `intervals[i][1]`
      - of size in the range [0, 10^4]
      - `intervals[i]` is of size 2
      - `intervals[i][0]` is a value in the range [0, `intervals[i][1]`]
      - `intervals[i][1]` is a value in the range [`intervals[i][0]`, 10^5]
    - `newInterval`: int array of size 2
      - `interval[0]` <= `interval[1]`
  - output:
    - `res`: `intervals` with `newInterval` inserted into it so that `intervals` is still sorted in ascending order and has NO overlapping intervals
    - overlapping intervals must be merged
  - overlapping meaning:
    - for 2 intervals `intervals[i]` and `intervals[j]`, they are considered to be overlapping if:
      - `intervals[i][0]` is a value in the range [`intervals[j][0]`, `intervals[j][1]`] OR
      - `intervals[i][1]` is a value in the range [`intervals[j][0]`, `intervals[j][1]`]
  - edge cases
    - `intervals` of size 0
      - return array of size 1 composed of `newInterval`
- PEDAC: Examples

## Solution 1: merge intervals (NeetCode's modded)

- O(N) T and O(N) S solution
- store modified result in empty array `res`
- deal with 3 cases when looping thru `intervals`
  - `newInterval` is before `intervals[i]`
    - return new array whose first element is `newInterval` and the rest of it are all the elements in `intervals` from index `i` to the last index
  - `newInterval` is after `intervals[i]`
    - push `intervals[i]` to `res`
  - `newInterval` overlaps with `intervals[i]`
    - merge `newInterval` and `intervals[i]` into a new interval
    - new interval's
      - start: min of (`newInterval[0]`, `intervals[i][0]`)
      - end: max of (`newInterval[1]`, `intervals[i][1]`)
- if exited loop,
  - push `newInterval` to `res` and return `res`
