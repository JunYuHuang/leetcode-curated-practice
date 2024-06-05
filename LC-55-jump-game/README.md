# [LC 55. Jump Game](https://leetcode.com/problems/jump-game/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size `n` in the range \[1, 10^4]
      - of values in the range \[0, 10^5]
  - output:
    - `res`: a bool true if can reach `nums`' last index else false
- PEDAC: Examples
  - 1-sized `nums` -> true

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- initialise variables
  - `NUMS_LEN`: int count of chars in `nums`
  - `goalPos`: int of last pos to reach in `nums` set to `NUMS_LEN` - 1
- loop thru `nums` for `i` from index `NUMS_LEN` - 2 to 0 inclusive,
  - if `i` + `nums[i]` >= `goalPos`,
    - means can reach `goalPos` from position `i`
    - move goalpost to `i`
      - `goalPos` = `i`
- return `goalPos` == 0
