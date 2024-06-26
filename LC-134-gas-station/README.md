# [LC 134. Gas Station](https://leetcode.com/problems/gas-station/)

## General Notes

- PEDAC: Problem
  - input:
    - `gas`: non-empty int circular array
      - of size `n` in the range \[1, 10^5]
      - of values in the range \[0, 10^4]
    - `cost`: non-empty int circular array
      - same as `gas` but with possibly different values
  - output:
    - `res`: int index of gas station that the car starts at that lets the car traverse all stations once clockwise if there it exists else -1
- PEDAC: Examples
  - TODO

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- if sum of `cost` > sum of `gas`,
  - return -1
- initialise variables
  - `SIZE`: int count of all elements in `cost` set to length of `cost`
  - `tank`: int count of current gas units in car set to 0
  - `pos`: int index that stores the result index of the starting gas station in `gas` set to 0
- for `i` from 0 to `SIZE` - 1 inclusive,
  - `tank` += (`gas[i]` - `cost[i]`)
  - if `tank` < 0,
    - `tank` = 0
    - `pos` = `i` + 1
- return `pos`
