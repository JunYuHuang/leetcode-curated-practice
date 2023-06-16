# [LC 121. Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock//)

## General Notes

- PEDAC: Problem
  - input:
    - `prices`: int array that represents the prices of a stock over 1+ days
      - `prices[i]` represents that price of the stock on the `ith` day
      - of size in range \[1, 10^5]
      - of values in range \[0, 10^4]
  - output:
    - `res`: int that represents that max profit achievable by buying and selling a stock on 2 separate days from `prices`
      - of values in range \[0, 10^4]
      - 0 if no profit is possible
  - constraints
    - stock buy day must be before stock sell day
    - cannot buy and sell the stock on the same day
    - return 0 if cannot profit from selling the stock
    - cannot sort `prices`
- PEDAC: Examples

## Solution 1: sliding window (NeetCode's modded.)

- O(N) T and O(1) S solution
- actually Kadane's algorithm
- initialise variables
  - `res`: int set to 0
  - `l`: int set to 0 that represents the left pointer for `prices`
  - `r`: int set to size of `prices` - 1 that represents the right pointer for `prices`
  - `N`: size of `prices`
- while r < N
  - if `prices[l]` > `prices[r]`,
    - `l` = `r`
  - else
    - calculate `profit`
    - update `res` with `profit` if `profit` > `res`
  - `r++`
- return `res`
