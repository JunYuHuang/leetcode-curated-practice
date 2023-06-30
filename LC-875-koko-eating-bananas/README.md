# [LC 875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

## General Notes

- PEDAC: Problem
  - input:
    - `piles`: int array that represents piles of bananas
      - `ith` pile has `piles[i]` bananas
      - of size in range \[1, 10^4]
      - of values in range \[1, 10^9]
    - `h`: int that represents in how many hours the guards will return to watch Koko
      - of value in range \[size of `piles`, 10^9]
  - output:
    - `k`: int that represents Koko's min bananas-per-hour eating speed that will let Koko finish eating all the bananas (`sum(p for p in piles)`) before the guards return (time = `h`)
      - in range \[1, 10^9]
  - Koko likes to eat slowly but wants to finish eating all the bananas before the guards return
- PEDAC: Examples

## Solution 1: binary search (NeetCode's modded)

- O(len(piles) + Log(max(piles))) T and O(1) S solution
- initialise variables
  - `leftK`: int that represents Koko's min or lower bounded bananas-per-hour eating speed set to 1
  - `rightK`: int that represents Koko's max or upper bounded bananas-per-hour eating speed set to max of `piles`
  - `k`: int set to `rightK` (max speed)
- while `leftK` <= `rightK`:
  - `midK` = (`leftK` + `rightK`) // 2
  - calculate the time needed to finish `piles` with bananas-per-hour eating speed of `midK`
    - `time` = 0
    - loop thru `p` for each int el in `piles`
      - `timeToFinish` = (`p` / `midK`) rounded to nearest largest int
        - use `math.ceil()` method in Python 3 for this
      - `time` += `timeToFinish`
  - if `time` <= `h`, decrease the speed of the next `maxK`
    - update `k` if `midK` is slower than it
      - if `midK` < `k`: `k` = `midK`
    - `rightK` = `midK` - 1
  - else (`time` > `h`), increase the speed of the next `maxK`
    - `leftK` = `midK` + 1
- return `k`
