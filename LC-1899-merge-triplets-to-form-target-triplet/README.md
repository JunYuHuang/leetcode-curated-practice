# [LC 1899. Merge Triplets to Form Target Triplet](https://leetcode.com/problems/merge-triplets-to-form-target-triplet/)

## General Notes

- PEDAC: Problem
  - input:
    - `triplets`: a non-empty array of 3-sized int arrays
      - of size in range \[1, 10^5]
      - all ints are of values in range \[1, 1000]
    - `target`: an 3-sized int array
      - all ints are of values in range \[1, 1000]
  - output:
    - `res`: bool that is true if it `target` can be gotten as an element of `triplets` else false
  - get `target` from `triplets` by getting the max of each int in the same position from both arrays
  - if `target` can be gotten from `triplets`
    - 1+ elements in `triplets` will be modified
    - each element in `target` must be in the same position in at least one of the arrays in `triplets`
- PEDAC: Examples
  - TODO

## Solution 1: greedy (NeetCode's expl.)

- O(N) T and O(N) S solution
- initialise variables
  - `TRIPLETS_SIZE`: int set to `triplets.length`
  - `invalidIndices`: an empty int set that stores the positions of the invalid triplets in `triplets`
  - `matchedIndices`: an empty int set that stores the positions in `target` that can be found in the valid triplets in `triplets`
- loop for `i` from 0 to `TRIPLETS_SIZE` inclusive,
  - `trip` = `triplets[i]`
  - if a triplet `trip` is invalid
    - means any of its elements `trip[i]` > `target[i]` where `i` is an index in the range \[0, 2]
    - add `i` to `invalidIndices`
    - continue to next triplet
- loop for `i` from 0 to `TRIPLETS_SIZE` inclusive,
  - `trip` = `triplets[i]`
  - if `trip` is an invalid triplet,
    - means `i` is in `invalidIndices`
    - continue
  - loop thru `j` from 0 to 2 inclusive,
    - if `trip[j]` == `target[j]`,
      - add `j` to `matchedIndices`
- return `matchedIndices.length` == 3

## Solution 2: greedy (NeetCode's modded)

- O(N) T and O(N) S solution
- same as solution but
  - loop thru `triplets` only once
  - does not mark invalid triplets
  - uses a long if-statement to skip invalid triplets
