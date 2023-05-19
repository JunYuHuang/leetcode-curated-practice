# [LC 271. Encode and Decode Strings](https://leetcode.com/problems/encode-and-decode-strings/)

## General Notes

- PEDAC: Problem
  - input:
    - for `encode` function
      - `strs`: string array
        - of size in range \[1, 200]
        - of elements of size in range \[0, 200]
        - of elements composed of any 256 ASCII chars
    - for `decode` function
      - `s`: string deserializable into a string array
  - output:
    - for `encode` function
      - some serialized string `s`
    - for `decode` function
      - some deserialized string array `strs`
  - follow up
    - should work for any possible set of chars
- PEDAC: Examples

## Solution 1: brute force with arbitrary delimiter (accepted LOL)

- O(N) T and O(N) S solution
- works for strings that don't contain the arbitrary delimiter string e.g. `_)#@$*{|\S1?2~q`
- for `encode` function
  - return `strs` as a string joined with delimiter string
- for `decode` function
  - return `strs` as an array split by `#` delimiter string

## Solution 2: prefix with substring size and arbitrary delimiter (NeetCode's expl.)

- O(N) T and O(N) S solution
- use a prefix delimiter to serialize and deserialize the strings
  - prefix every string in `strs` with this
  - size = size of a string in the array `strs`
  - arbitrary delimiter char `#`
  - prefix delimiter = size + `#`
- for `encode` function
  - initialise empty `res` array
  - loop thru every string `s` in `strs`
    - `serialized` = `s`'s size + `#` char + `s`
    - push `serialized` to `res` array
  - return `res` converted to string
- for `decode` function
  - initialise variables
    - `res`: empty string array
    - `prefL`: int set to 0, represents 1st digit of prefix delimiter string
    - `prefR`: int set to 0, represents last char of prefix delimitir string i.e. should point to `#` once an encoded string is found in `s`
  - loop thru string `s` with index `i`
    - if `s[i]` is a digit, `prefR`++ and continue
    - if `s[i]` is the delimiter char `#`,
      - found the decoded string so push it to `res`
      - `size` = `s[L:R]` converted to an int
      - `start` = `prefR` + 1
      - `end` = `prefR` + `size`
      - `string` = `s[start:end + 1]`
      - push `string` to `res`
      - update the pointers
        - `i` = `end + 1`
        - `prefL` = `end + 1`
        - `prefR` = `prefL`
  - return `res`
