# [LC 49. Group Anagrams](https://leetcode.com/problems/group-anagrams/)

## General Notes

- PEDAC: Problem
  - input:
    - `strs`: string array
      - of size in range \[1, 10^4]
      - whose each string is of size in range \[0, 100]
      - whose each string is only of lowercase alphabet chars
  - output:
    - 2D array or matrix of strings
- PEDAC: Examples
- does order of strings in result subarrays matter? no

## Solution 1: brute force sort

- O(N * MLogM) time and O(N * M) space solution
- initialise empty hashmap `res`
  - maps each sorted anagram string to a list of its unsorted anagram members
- loop thru each string `s` in `strs`
  - `sorted_s` = `s` converted to an array that is sorted then converted back to a string
  - add `sorted_s` to `res` hashmap
    - if key doesn't exist in `res`, initialise it with an array with just `s` in it
    - else key exists in `res`, just push `s` to it
- return `res.values()`

## Solution 2: hashmap (NeetCode's modded)

- O(N * M) T and O(N * M) S solution
- initialise empty hashmap `res`
  - key: tuple of an array of size 26 that maps each index that represents a lowercase alphabet char to the number of times it occurs in a common anagram string
  - value: list of strings from `strs` that can be rearranged in order to be the same anagram
- initialise `startOrd` to ord('a')
  - represents the integer ASCII value of the character 'a'
- loop thru each string `s` in `strs`
  - initialise `count` array of size 26 with default value '0'
    - starts from 0 -> 'a' to 25 -> 'z' for index -> val
  - loop thru each char `c` in string `s`
    - get `c`'s converted 0-based index as `pos`
      - = `ord(c)` - `startOrd`
    - `count[pos]++`
  - push `s` to `res` at key of `count` as a tuple
    - if `res[tuple(count)\]` does not exist,
      - initialise its default value as an empty array first
- return `res.values()`
