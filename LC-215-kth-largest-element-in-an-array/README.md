# [LC 215. Kth Largest Element in an Array](https://leetcode.com/problems/kth-largest-element-in-an-array/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of size in the range \[`k`, 10^5]
      - of values in the range \[-10^4, 10^4]
    - `k`: int in the range \[1, size of `nums`]
  - output:
    - `res`: int that represents the `k`th largest element in `nums`
  - constraints
    - solve without sorting
- PEDAC: Examples

## Solution 1: max heap

- O(N + KLogN) T and O(N) S solution
- initialise variables
  - `maxHeap`: set to `nums` by transformed into a max heap
- pop from `maxHeap` `k` - 1 times
- return top or first element of `maxHeap`

## Solution 2: min heap

- O(N + (N - K) * LogN) T and O(N) S solution
- same approach as solution 1 but
  - use min heap instead of max heap
  - pop from heap N - `k` times
- return top or first element of `minHeap`
