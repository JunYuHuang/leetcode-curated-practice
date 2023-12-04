# [LC 239. Sliding Window Maximum](https://leetcode.com/problems/sliding-window-maximum/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array of size in range \[1, 10^5]
      - `nums[i]` of a value in range \[-10^4, 10^4]
    - `k`: int size of fixed subarray / window in `nums` that can be seen
      - of values in range \[1, `nums` size]
  - output:
    - `res`: int array containing the max value from each window / subarray of size `k` in `nums`
  - constraints
    - sliding window moves right by one position every iteration
  - notes
    - a
- PEDAC: Examples

## Solution 1: sliding window solution (TLE)

- O((N - K) * K) T and O(K) S solution
- initialise variables
  - `windowVals`: double-ended queue initially set to an empty array
  - `res`: empty array to hold result
  - `l`: int left pointer for `nums` set to 0
  - `numsLen`: size of `nums`
- loop for `r` from 0 to `numsLen` - 1 inclusive
  - push `nums[r]` to `windowVals`
  - `windowSize` = `r` - `l` + 1
  - if `windowSize` == `k`,
    - push `max(windowVals)` to `res`
    - remove first element from `windowVals`
    - `l++`
- return `res`

## Solution 2: sliding window + monotonic decreasing queue solution (NeetCode's modded)

- O(N) T and O(N) S solution
- initialise variables
  - `q`: double-ended queue that holds indices in `nums`
  - `l`: int left pointer for `nums` set to 0
  - `res`: int array to hold result set to empty array
  - `numsLen`: size of `nums`
- loop for `r` from 0 to `numsLen` - 1 inclusive
  - while `q` is not empty and `nums[q[-1]]` < `nums[r]`,
    - pop last element from `q`
  - push `r` to `q`
  - if `q[0]` < `l`
    - remove first element from `q`
  - if window size (`r` - `l` + 1) is `k`,
    - push `nums[q[0]]` to `res`
    - `l++`
- return `res`
