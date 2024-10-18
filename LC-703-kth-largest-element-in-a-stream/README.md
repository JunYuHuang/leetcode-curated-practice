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
      - returns the `k`th largest element in stream after `val` is added to the `nums` stream / array
  - constraints
    - at most 10^4 calls will be made to `add()`
    - guaranteed that there will be >= `k` elements in `nums` when searching for the `kth` element
- PEDAC: Examples
  - k = 3, scores = [2, 4, 5, 8]
    - add(3)
      - scores = [2, 3, 4, 5, 8]
      - -> 4
    - add(5)
      - scores = [2, 3, 4, 5, 5, 8]
      - -> 5
    - add(10)
      - scores = [2, 3, 4, 5, 5, 8, 10]
      - -> 5

## Solution 1: K-sized min heap

- T and S complexity
  - `KthLargest()`: O((N - K) \* LogN) T and O(N) S
  - `add()`: O(LogK) T and O(1) S
- `KthLargest(k, nums)`
  - set `k` to instance int variable
  - set `nums` to instance array variable
  - convert `nums` to min heap
  - while `nums`' size is greater than `k`,
    - heap pop from `nums`
- `add(val)`
  - heap push `val` to `nums`
  - if `nums`'s length is greater than `k`,
    - heap pop from `nums`
  - return top / root of `nums`
