# [LC 253. Meeting Rooms II (Premium)](https://leetcode.com/problems/meeting-rooms-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `intervals`: array of 2-sized int arrays
      - `intervals[i][0]` <= `intervals[i][1]`
      - of size in the range [1, 10^4] (has at least 1 meeting)
      - `intervals[i]` is of size 2
      - `intervals[i][0]` is a value in the range [0, `intervals[i][1] - 1`]
      - `intervals[i][1]` is a value in the range [`intervals[i][0] + 1`, 10^6]
      - NOT always in non-decreasing / ASC order
  - output:
    - `res`: count of min rooms for hosting all meetings so that there are no conflicting meeting times
      - only add a room if two meetings overlap
      - always need at least one room because there is at least one meeting in `intervals`
  - overlapping meaning:
    - 2 intervals are overlapping if:
      - one interval's start
        - EQUALS another interval's start
        - is BETWEEN another interval's start and BEFORE another interval's end
      - EXCLUDES cases when one interval's end EQUALS another interval's start
    - else intervals are NOT overlapping
  - edge cases
    - `intervals` of size 1
- PEDAC: Examples

## Solution 1: intervals (NeetCode's modded)

- O(NLogN) T and O(N) S solution
- initialise variables
  - `starts`: all start times in `intervals` (i.e. `intervals[i][0]`) sorted in ASC order
  - `ends`: all end time in `intervals` (i.e. `intervals[i][1]`) sorted in ASC order
  - `s`: int pointer set to 0 for traversing `starts`
  - `e`: int pointer set to 0 for traversing `ends`
  - `INTERVALS_LEN`: size of `intervals`
  - `count`: int count of ongoing meetings
  - `res`: int count of max ongoing meetings of all time
- while `s` < `INTERVALS_LEN`,
  - if a meeting started or there is overlap,
    - means `starts[s]` < `ends[e]`
    - `count++`
    - `res` = max of (`res`, `count`)
    - `s++`
  - else,
    - means a meeting ended or there is no overlap
    - `count--` - `e++`
- return `res`
