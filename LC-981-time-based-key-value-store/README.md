# [LC 981. Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/)

## General Notes

- PEDAC: Problem
  - `TimeMap()` class design:
    - `set(key, value, timestamp)`
      - stores the key `key` with value `value` at the given time `timestamp`
      - returns null
      - `key`: a string
        - of lowercase alphanumeric chars only
        - of size in range \[1, 100]
      - `value`: a string
        - of lowercase alphanumeric chars only
        - of size in range \[1, 100]
      - `timestamp`: an int
        - of values in range \[1, 10^7]
        - will all be passed with strictly increasing values
    - `get(key, timestamp)`
      - returns a value that set was called prev with `timestamp_prev <= timestamp`
        - returns latest or largest `timestamp_prev` if multiple values exist
        - returns an empty string `""` if there are no values
      - returns a string `value`
      - `value`: a string
        - of lowercase alphanumeric chars only
        - of size in range \[1, 100]
      - `key`: a string
        - of lowercase alphanumeric chars only
        - of size in range \[1, 100]
      - `timestamp`: an int
        - of values in range \[1, 10^7]
        - will all be passed with strictly increasing values
- PEDAC: Examples

## Solution 1: binary search (NeetCode's modded)

- O(N) space class solution
- O(1) time and O(N) space `set()` method solution
- O(LogN) time and O(1) space `get()` method solution
- `TimeMap()` constructor
  - initialise variables
    - `store`: hashmap that stores sub-hashmaps where each sub-hashmap stores an array of 1 of the following:
      - arrays of size 2 where `array[0]` stores the int timestamp and `array[1]` stores the string value
      - OR hashmaps that hold:
        - `timestamp` key that stores an int timestamp
        - `value` key that stores a string value
- `set(key, value, timestamp)` method
  - if `key` is NOT in this object's `store`,
    - add a new key `key` to `store` and map it to an empty array
  - push `[timestamp, value]` to `store[key]`
- `get(key, timestamp)` method
  - initialise variables
    - `values` = empty array or `store[key]` if `key` exists in `store`
    - `l`: int set to 0 that represents the left pointer in `store[key]`
    - `r`: int set to size of `values` - 1 that represents the right pointer in `values`
    - `res`: int set to null
  - while `l` <= `r`:
    - `m` = `l` + (`r` - `l`) // 2
    - if `values[m][0]` == `timestamp`,
      - return `values[m][1]`
    - else if `values[m][0]` < `timestamp`,
      - res = `values[m][1]`
      - search upper right half of `values`
      - `l` = `m` + 1
    - else (`values[m][0]` > `timestamp`),
      - search lower left half of `values`
      - `r` = `m` - 1
  - return `res` if `res` is not null else an empty string `""`

