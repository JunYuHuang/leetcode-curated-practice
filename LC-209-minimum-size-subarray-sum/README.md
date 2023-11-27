# [LC 209. Minimum Size Subarray Sum](https://leetcode.com/problems/minimum-size-subarray-sum/description/)

## General Notes

- PEDAC: Problem
  - inputs
    - `target`: int in range \[1, 10^9]
    - `nums`: int array
      - of size in range \[1, 10^5]
      - of values in range \[1, 10^4]
  - output
    - `res`: int that represents the min length of a subarray in `nums` whose sum is >= `target`
      - of values in range \[0, `nums` size]
      - if no such subarray exists, return 0
  - notes

## Solution 1: sliding window solution

- O(N) T and O(1) S solution
- initialise variables
  - `res`: int set initially to infinity
  - `l`: int left pointer for traversing in `nums` set to 0
  - `r`: int right pointer for traversing in `nums` set to 0
  - `currSum`: int set to `nums[0]`
  - `numsLen`: size of `nums`
- while `l` <= `r` and `r` < `numsLen`
  - `windowSize` = `r` - `l` + 1
  - if `currSum` >= `target`
    - if `windowSize` < `res`
      - `res` = `windowSize`
    - `currSum` -= `nums[l]`
    - `l++`
  - else (`currSum` < `target`)
    - `r++`
    - if `r` < `numsLen`
      - `currSum` += `nums[r]`
- return 0 if `res` is INF else `res`

## Solution 2: sliding window solution (NeetCode's modded)

- O(N) T and O(1) S solution
- same approach as solution 1 but
  - use a while loop nested inside an outer for loop
  - increment `r` pointer every time in outer for loop
  - keep shrinking window (`l++`), potentionally update `res`, and update `currSum` while `currSum` >= `target` for inner while loop
