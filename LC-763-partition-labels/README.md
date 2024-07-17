# [LC 763. Partition Labels](https://leetcode.com/problems/partition-labels/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: a string
      - whose characters are of only lowercase English letters
      - of size in the range \[1, 500]
  - output:
    - `res`: an int array
      - of size in the range \[1, `s.length`]
      - of ints that represent the size of each substring cut from `s` where concatenating all the substrings in order forms `s`
        - each substring cannot share any chars with any other substring(s)
        - substrings are contiguous
- PEDAC: Examples
  - `s` is size 1 -> return 1

## Solution 1: greedy (NeetCode's modded)

- O(N) T and O(1) S solution
- initialise variables
  - `res`: empty int array that holds result
  - `S_SIZE`: int set to `s.length`
  - `l`: int set to 0 that is the left pointer for the current substring
  - `r`: int set to 0 that is the right pointer for the current substring
  - `lastPos`: hashmap that maps each unique char to its last occurring index in `s`
- build `lastPos` hashmap
- for `i` from 0 to `S_SIZE` - 1,
  - `r` = max(`r`, `lastPos[s[i]]`)
  - if reached the end of the current substring,
    - means `i` == `r`
    - add that substring's size to `res`
      - push `r - l + 1` to `res`
    - if current substring is last substring in `s`,
      - means `r` == `S_SIZE` - 1
      - exit loop
    - reset the pointers for the next substring
      - `l` = `r` + 1
      - `r` = `l`
- return `res`
