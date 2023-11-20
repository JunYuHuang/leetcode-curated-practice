# [LC 219. Contains Duplicate](https://leetcode.com/problems/contains-duplicate-ii/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in range \[1, 10^5]
      - of values in range \[-10^9, 10^9]
    - `k`: int of value in range \[0, 10^5]
  - output:
    - `res`: boolean
      - true if there is a subarray in `nums` of size in range [2, `k` + 1] where there are int indices `i` and `j` where
        - `i` != `j`
        - `nums[i]` == `nums[j]`
      - else return false
  - notes
    - min window size = 2
    - max window size = `k` + 1
    - return false if
      - `k` + 1 < 2 or `k` < 1
      - size of `nums` < 2
- PEDAC: Examples

## Solution 1: sliding window

- O(N) T and O(K) S solution
- return false if encountered edge cases where
  - max window size < 2
  - OR size of `nums` < 2
- initialise variables
  - `l`: int left pointer for `nums` set to 0
  - `visit`: empty set for tracking encountered elements in `nums`
- loop for every index `r` in `nums`
  - if window size is at least of size 2 and `nums[r]` has been visited before (i.e. it exists in `visit`)
    - return true
  - add `nums[r]` to `visit`
  - if window size is at the max size (`k` + 1)
    - remove `nums[l]` from `visit`
    - move `l` pointer (`l++`)
- return false if exited loop
