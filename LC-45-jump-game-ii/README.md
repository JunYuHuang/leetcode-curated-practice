# [LC 45. Jump Game II](https://leetcode.com/problems/jump-game-ii/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size `n` in the range \[1, 10^4]
      - of values in the range \[0, 1000]
      - test cases guarantee that `nums[n - 1]` is reachable
  - output:
    - `res`: min int count of steps to reach `nums[n - 1]` from `nums[0]`
- PEDAC: Examples
  - 1-sized `nums` -> 0

## Solution 1: greedy / BFS (NeetCode's modded)

- O(N) T and O(1) S solution
- initialise variables
  - `res`: int that stores the min of jumps needed to reach the last element in `nums` initially set to 0
  - `l`: int that is the left pointer for traversing `nums` set to 0
  - `r`: int that is the right pointer for traversing `nums` set to 0
  - `LAST_POS`: int that is the index of the last element in `nums` set to length of `nums` - 1
- while `r` < `LAST_POS`,
  - `farthest`: int set to 0 that stores the farthest index that can be reached in the current "level" of the window
  - for `i` from `l` to `r` inclusive,
    - if `i` + `nums[i]` > `farthest`,
      - `farthest` = `i` + `nums[i]`
  - `l` = `r` + 1
  - `r` = `farthest`
  - `res++`
- return `res`
