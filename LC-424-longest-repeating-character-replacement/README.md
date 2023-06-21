# [LC 424. Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/)

## General Notes

- PEDAC: Problem
  - input:
    - `s`: string of only uppercase English letters
      - of size in range \[1, 10^5]
    - `k`: integer in range \[0, size of `s`]
  - output:
    - `res`: integer that represents the longest substring in `s` composed of a single repeating uppercase English letter with at most `k` character replacements
      - integer in range \[1, size of `s`]
- PEDAC: Examples

## Solution 1: sliding window (NeetCode's expl.)

- O(N) T and O(N) S solution
- use hashmap to count freq of unique chars in window
- keep window valid by maintaining the property `windowSize` - `max(count.values())` <= `k`
- use `maxFreq` to optimise solution run time to O(N) instead of O(26 * N)
  - no need to decrease `maxFreq` because a smaller valid window size will never be greater than our current result (`res`)
- initialise variables
  - `res`: int set to 0
  - `l`: left pointer in `s` set to 0
  - `r`: right pointer in `s` set to 0
  - `maxCount`: int set to 0 that represents the char that occurs most often in the window (`s[l:r + 1]`) substring in `s`
  - `count`: hashmap that maps each unique char in the window substring in `s` to how many times it occurs
  - `N`: size of `s`
- while `r` < `N`
  - increment `s[r]` in `count`
  - update `maxCount` to `count[s[r]]` if `count[s[r]]` > `maxCount`
  - while the current window does not have enough replacement chars i.e. `r` - `l` + 1 - `maxCount` > `k`
    - decrement `s[l]` in `count` and move the `l` pointer (`l++`)
  - `r++`
- return `res`
