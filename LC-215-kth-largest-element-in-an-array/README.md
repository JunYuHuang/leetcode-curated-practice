# [LC 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: non-empty int array
      - of size in the range \[`k`, 10^5]
      - of values in the range \[-10^4, 10^4]
        - can have duplicate values
    - `k`: int in the range \[1, size of `nums`]
  - output:
    - `res`: int that represents the `k`th largest element in `nums`
  - constraints
    - solve without sorting
- PEDAC: Examples

## Solution 1: max heap

- O(N + K \* LogN) T and O(N) S solution
- convert `nums` to a max heap
- heap pop from `nums` `k - 1` times
- return top / root of max heap `nums`

## Solution 2: min heap

- O(N + (N - K) \* LogN) T and O(N) S solution
- convert `nums` to a min heap
- loop until `nums`'s length is of size `k`,
  - heap pop from `nums`
- return top / root of min heap `nums`

## Solution 3: sorting

- O(NLogN) T and O(N) S solution
- sort `nums` in ASC order
- return element in `nums` at index `N` - `k`
  - `N` is length of `nums`
