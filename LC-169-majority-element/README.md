# [LC 169. Majority Element](https://leetcode.com/problems/majority-element/)

## General Notes

- PEDAC: Problem
  - input:
    - `nums`: int array
      - of length in range \[1, 5 * 10^4]
      - of values `nums[i]` in range \[1, 5 * 10^4]
  - output:
    - `res`: int
      - element in `nums` that appears the most times or more than `n / 2` times where `n` is the length of `nums`
- PEDAC: Examples
  - TODO

## Solution 1: hashmap

- O(n) T + O(n) S solution
- loop thru each int `nums[i]` in `nums`:
  - increment value of key `nums[i]` in hashmap
  - if value is greater than current max count:
    - set current max count to it
    - set current max element to `nums[i]`
- return current max element

## Solution 2: NeetCode's Boyer-Moore voting algorithm modded solution

- O(n) T + O(1) S solution
- works because test cases are guaranteed to have a majority element (i.e, an element that appears more than the count of half the size of `nums`)
- set int `res` to 0
- set int `count` to 0
- for each int `n` in `nums`:
  - if `count` is 0:
    - set `res` to `n`
  - if `n` is `res`:
    - increment `count` by 1
  - else:
    - decrement `count` by 1
- return `res`
