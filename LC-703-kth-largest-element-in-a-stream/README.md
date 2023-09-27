# [LC 703. Kth Largest Element in a Stream](https://leetcode.com/problems/kth-largest-element-in-a-stream/)

## General Notes

- PEDAC: Problem
  - input:
    - for constructor `KthLargest(k, nums)`
      - `k`: an integer that represents the `k`th largest element in `nums`
        - in the range \[1, 10^4]
      - `nums`: an integer array
        - of values in the range \[-10^4, 10^4]
        - may have duplicate values
        - of size in the range \[0, 10^4]
    - for method `add(val)`
      - `val`: an integer in the range \[-10^4, 10^4]
  - output:
    - for constructor `KthLargest(k, nums)`
      - returns an object or instance of the class `KthLargest`
    - for method `add(val)`
      - returns the `k`th larget element in stream after `val` is added to the `nums` stream / array
  - constraints
    - at most 10^4 calls will be made to `add()`
    - guaranteed that there will be >= `k` elements in `nums` when searching for the `kth` element
- PEDAC: Examples

## Solution 1: min heap of size k (NeetCode's expl. modded)

- T & S complexity breakdown
  - `KthLargest()`: O(NLogN) T and O(N) S
  - `add()`: O(MLogK) T and O(1) S
- initialise variables
  - `minHeap`: min heap initialised with elements from `nums` always kept at size <= `k`
- when calling `KthLargest()` constructor,
 - pop elements from `minHeap` while size of `minHeap` > `k`
- when calling `add()` method,
  - if `minHeap` is of at least size `k` and its top (smallest) element's value >= `val`,
    - don't need to push `val` to min heap
    - return top (smallest) element of `minHeap`
  - push `val` to heap
  - while `minHeap`'s size is > `k`,
    - pop from `minHeap`
  - return top (smallest) element of `minHeap`
