# [LC 33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)

## General Notes

- PEDAC: Problem
  - input:
    - `n`: size of `nums` array
    - `k`: unknown pivot index of values in range \[1, `n` - 1]
      - indicates position of new first el of rotated array
    - `nums`: ASC sorted int array that is rotated at an unknown pivot point index `k`
      - of size in range \[1, 5000]
      - of values in range \[-10^4, 10^4]
      - guaranteed to only have unique values
    - `target`: int value that is or is not in `nums`
      - of values in range \[-10^4, 10^4]
  - output:
    - `res`: int that is the index of `target` in `nums` or -1 if it is not in `nums`
      - of values in range \[-1, `n` - 1]
  - constraints
    - must write algorithm with O(LogN) (run) time complexity
  - not given the number of times `nums` is rotated
  - each rotation moves each el in `nums` 1 position towards the right or end of `nums`
    - last el of original `nums` rotated is placed at `nums`' start or first el
- PEDAC: Examples

## Solution 1: binary search (NeetCode's modded)

- O(LogN) T and O(1) space solution
- initialise variables
  - `l`: left pointer in `nums` set to 0
  - `r`: right pointer in `nums` set to size of `nums` - 1
- while `l` <= `r`:
  - `m` = `l` + (`r` - `l`) // 2
  - if `nums[m]` == `target`:
    - return `m`
  - else if `nums[l]` <= `nums[m]`:
    - `nums[m]` is in left and upper half of `nums`
    - if `target` is in this subarray (`nums[l:m + 1]`), search this half
      - if `nums[l]` <= `target` <= `nums[m]`:
        - `r` = `m` - 1
    - else search the other right half
      - else
        - `l` = `m` + 1
  - else `nums[l]` > `nums[m]`
    - `nums[m]` is in right and lower half of `nums`
    - if `target` is in this subarray (`nums[m:r + 1]`), search this half
      - if `nums[m]` <= `target` <= `nums[r]`:
        - `l` = `m` + 1
    - else search the other right half
      - else
        - `r` = `m` - 1
- return -1
