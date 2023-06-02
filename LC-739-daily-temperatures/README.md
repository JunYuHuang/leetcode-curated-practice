# [LC 739. Daily Temperatures](https://leetcode.com/problems/daily-temperatures/)

## General Notes

- PEDAC: Problem
  - input:
    - `temperatures`: int array representing daily temperatures
      - of size in range \[1, 10^5]
      - of values in range \[30, 100]
  - output:
    - `answer`: int array where each element represents the number of days one must wait after it (the element) to get a warmer temperature
      - same size as `temperatures`
      - of values in range \[0, `temperatures.size - 1`]
      - use value 0 to indicate that there is no future day for which it is warmer than the current day
  - a
- PEDAC: Examples

## Solution 1: monotonic decreasing stack (NeetCode's modded)

- O(N) T and O(N) S solution
- initialise variables
  - `answer`: int array initialised with size `temperatures.size` filled with all 0's
  - `posStack`: empty int array that will acts a monotonic decreasing stack that holds each index in `temperatures`
    - its DESC order will be always be maintained
- loop thru every index `i` for each element in `temperatures`
  - while `posStack` is not empty and the temperature its last element indexes is less than `temperatures[i]`
    - `lastPos` = pop from `posStack`
    - `daysToWait` = `i` - `lastPos`
    - `answer[lastPos]` = `daysToWait`
  - push `i` to `posStack`
- return `answer`
