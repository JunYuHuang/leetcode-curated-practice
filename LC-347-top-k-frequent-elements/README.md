# [LC 347. Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: integer array
      - of size in range \[1, 10^5]
      - of values in range \[-10^4, 10^4]
    - `k`: int in range \[1, unique elements in `nums`]
  - output:
    - int array that contains the `k` most frequent elements in `nums`
      - order of ints does not matter
- PEDAC: Examples

## Solution 1: max heap

- O(KLogN) T and O(N) S max heap solution
- initialise variables
  - `res`: empty array
  - `valToCount`: empty hashmap that maps all unique values in `nums` to their occurrences
- loop thru `nums` and build `valToCount` hashmap
- build max heap `maxH` from `valToCount`'s (value, key), pairs
- pop `k` times from `maxH`
  - for each popped el,
    - push its key from (value, key) to `res`
- return `res`

## Solution 2: bucket sort (NeetCode's modded)

- O(N) T and O(N) S bucket sort solution
- initialise variables
  - `res`: empty array
  - `valToCount`: empty hashmap that maps all unique values in `nums` to their occurrences
  - `maxCount`: max count of any unique int in `nums` = 0
- loop thru `nums`
  - build `valToCount` hashmap
  - update `maxCount` as needed
- initialise `countToVal`: empty 2d array of ints that maps each index of the outer array ('count' excluding index 0) to an array of unique ints that occur that many times in `nums` of size (1 + `maxCount`)
- loop thru `valToCount` for (key, value)
  - build `countToVal` 2D array
- loop thru `countToVal` 2D array in reverse order from index `maxCount` to 1 inclusive
  - if size of `res` is `k`, break from loop
  - loop thru the subarray in `countToVal[i]`
    - if size of `res` is `k`, break from loop
    - push the popped value from `countToVal[i]` to `res`
- return `res`
