# [LC 50. Pow(x,n)](https://leetcode.com/problems/powx-n/)

## General Notes

- PEDAC: Problem
  - input: 
    - `x`: the base; float in range (-100.0, 100.0)
    - `n`: the power; int in range \[-2^13, 2^31 - 1]
  - ouput: some res float
  - implement a function to get the base `x` to the power of `n`
  - if power `n` is negative, return 1 / result
  - anything to the power of 0 is 1
  - 0 to the power of anything except 1 is 0
- PEDAC: Examples
  - x = 0, n = 0 -> 1
  - x = 1, n = 0 -> 1
  - x = 0, n = 1 -> 0

## Solution 1: iterative (TLE)

- O(N) time and O(1) space solution
- if `n` is 0 or `x` is 0, return 1
- just keep mulitplying `x` by itself `abs(n)` times in res
- return res if n is positive else 1 / res

## Solution 2: recursive (StefanPochmann's modded)

- O(LogN) time and O(LogN) space solution
- make function recursive using tail recursion
- bases cases
  - if n (power) is 0, return 1
  - if x (base) is 0, return 0
  - if n (power) < 0, return 1 / myPow(x, -n)
  - if n (power) is odd, return x * myPow(x, n - 1)
  - n (power) should be positive and even, return myPow(x * x, n / 2)
