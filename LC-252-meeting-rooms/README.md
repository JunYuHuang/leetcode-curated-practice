# [LC 252. Meeting Rooms (Premium)](https://leetcode.com/problems/meeting-rooms/)

## General Notes

- PEDAC: Problem
  - input:
    - `intervals`: array of 2-sized int arrays
      - `intervals[i][0]` <= `intervals[i][1]`
      - of size in the range [0, 10^4] (can be empty)
      - `intervals[i]` is of size 2
      - `intervals[i][0]` is a value in the range [0, `intervals[i][1] - 1`]
      - `intervals[i][1]` is a value in the range [`intervals[i][0] + 1`, 10^6]
      - NOT always in non-decreasing / ASC order
  - output:
    - `res`: true if can attend all meetings else false
  - overlapping meaning:
    - 2 intervals are overlapping if:
      - one interval's start
        - EQUALS another interval's start
        - is BETWEEN another interval's start and BEFORE another interval's end
      - EXCLUDES cases when one interval's end EQUALS another interval's start
    - else intervals are NOT overlapping
  - edge cases
    - `intervals` of size 0
    - `intervals` of size 1
- PEDAC: Examples

## Solution 1: merge intervals

- O(NLogN) T and O(1) S solution
- (optional): return true if `intervals` is of size 0 or 1
- sort `intervals` in non-decreasing order
- loop thru i from the 2nd element in `intervals` to its last
  - `prev` = `intervals[i - 1]`
  - `curr` = `intervals[i]`
  - if `curr` does NOT overlap `prev`,
    - means:
      - `prev`'s end == `curr`'s start OR
      - `prev`'s end < `curr`'s start
    - skip to next iteration
  - return false
- return true if exited loop
