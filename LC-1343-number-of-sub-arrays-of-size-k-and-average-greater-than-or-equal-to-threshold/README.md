# [LC. 1343 Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold](https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/)

## General Notes

- PEDAC: Problem
  - input:
    - `arr`: int array
      - of size in range \[1, 10^5]
      - of values in range \[1, 10^4]
    - `k`: int in range \[1, `arr` size]
    - `threshold`: int in range \[0, 10^4]
  - output:
    - `res`: int count of all subarrays in `arr` of size `k` whose average is >= `threshold`
  - notes
    - calculated average of each subarray is a float value
- PEDAC: Examples

## Solution 1: sliding window

- O(N) T and O(1) S solution
- summary
  - set `l` and `r` int pointers to 0
  - set `currSum` int to 0
  - set `res` int to 0
  - while `r` is in bounds
    - `currSum` += `arr[r]`
    - if current window size equals `k` (`r` - `l` + 1 == `k`)
      - get average of current window = `currSum` / `k`
      - if average >= `threshold`,
        - `res++`
      - `currSum` -= `arr[l]`
      - `l++`
    - `r++`
  - return `res`
