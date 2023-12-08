# [LC 76. Minimum Window Substring](https://leetcode.com/problems/minimum-window-substring/description/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: a string of length `m`
      - `s[i]`: an upper or lower cased alpha char
      - `m`: int in range \[1, 10^5]
    - `t`: a string of length `n` that may be a substring in `s`
      - `t[i]`: an upper or lower cased alpha char
      - `n`: int in range \[1, 10^5]
  - output:
    - `res`: the smallest substring of `s` such that every char in `t` including duplicates is in the window else an empty string if no such substring exists
  - constraints
    - result is guaranteed to be unique
  - follow up
    - make algorithm run in O(`m` + `n`) time
  - notes
    - return an empty string if `t` is an empty string
    - return an empty string if size of `t` > size of `s`
- PEDAC: Examples

## Solution 1: (variable) sliding window solution (NeetCode's modded)

- O(M + N) T and O(N) S solution
- initialise variables
  - `l`: left pointer for traversing `s` that represents the left bound of the window set to int 0
  - `tCount`: hashmap that maps all unique chars in `t` to their counts
  - `sCount`: hashmap that map all unique chars in `t` in `s` with all values set to 0
  - `need`: int set to size of `t`
  - `have`: int set to 0
  - `resL`: int set to 0 that represents the left bound of the minimum window in `s`
  - `resR`: int set to INFINITY that represents the right bound of the minimum window in `s`
- notes
  - keep shrinking window (`l++`) only if the window in `s` has all the chars and their counts from `t`
  - keep expanding window (`r++`) until `r` is out-of-bounds
- loop for `r` from 0 to size of `s` - 1 inclusive
  - if `s[r]` is in `tCount`,
    - `sCount[s[r]]++`
    - if `sCount[s[r]]` <= `tCount[s[r]]`,
      - `have++`
  - while `have` == `need`,
    - if current window size is less than the resulting window size,
      - update `resL` and `resR` accordingly
    - if `s[l]` is in `tCount`,
      - `sCount[s[l]]--`
      - if `sCount[s[l]]` < `tCount[s[r]]`,
        - `have--`
    - `l++`
- return `""` if `resR` is INFINITY else `s[resL:resR + 1]`
