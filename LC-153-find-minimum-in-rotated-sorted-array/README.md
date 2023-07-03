# [LC 153. Find Minimum in Rotated Sorted Array](https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: size of `nums` array
    - `nums`: ASC sorted int array that is rotated from 1 to `n` times inclusive
      - of size in range \[1, 5000]
      - of values in range \[-5000, 5000]
      - guaranteed to only have unique values
  - output:
    - `res`: int that is the min element found in `nums`
      - of values in range \[-5000, 5000]
  - constraints
    - must write algorithm with O(LogN) (run) time complexity
  - not given the number of times `nums` is rotated
  - each rotation moves each el in `nums` 1 position towards the right or end of `nums`
    - last el of original `nums` rotated is placed at `nums`' start or first el
  - when using binary search, how to know if found min?
- PEDAC: Examples

## Solution 1: binary search (camoenv3572's modded)

- O(LogN) T and O(1) space solution
- idea:
  - always do binary search in lower (subarray with min value) sorted half of `nums`
  - return `nums[l]` if
    - found the midpoint `nums[m]` with the properties:
      - `nums[l]` <= `nums[m]` and `nums[m]` <= `nums[r]`
    - OR while loop (`l` <= `r`) breaks
- initialise variables
  - `l`: left pointer in `nums` set to 0
  - `r`: right poitner in `nums` set to size of `nums` - 1
- while `l` <= `r`:
  - `m` = `l` + (`r` - `l`) // 2
  - if `nums[m]` > `nums[r]`:
    - `nums[m]` is in left and upper half of `nums`
    - search in right and lower half of `nums`
    - `l` = `m` + 1
  - else if `nums[m]` < `nums[r]`
    - `nums[m]` is in right and lower half of `nums`
    - search in this (half) of `nums` including `nums[m]`
    - `r` = `m`
  - else `nums[m]` == `nums[l]`
    - return `nums[l]`
