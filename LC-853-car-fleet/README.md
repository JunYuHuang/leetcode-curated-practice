# [LC 853. Car Fleet](https://leetcode.com/problems/car-fleet/)

## General Notes

- PEDAC: Problem
  - input:
    - `target`: int representing the distance in miles of some destination in the range \[0, 10^6]
    - `position`: int array
      - represents the initial positions of the `ith` car
      - represents how much distance in miles that the `ith` car has travelled from some origin towards `target`
      - of size in range \[1, 10^5] == size of `speed`
      - of values in range \[0, `target` - 1]
      - every `position[i]` is **unique**
    - `speed`: int array
      - represents the initial speeds in miles per hour of the `ith` car
      - of size in range \[1, 10^5] == size of `position`
      - of values in range \[1, 10^6]
  - output:
    - `res`: int representing the count of car fleets that will arrive at the destination (i.e. when all cars reach `target`)
      - in range \[1, size of `position`]
  - initially faster cars behind slower cars that catch up will slow down to the slower cars' speed
  - cars that are behind will never pass the cars in front of it
  - a car fleet is a set of cars driving at the same position and same speed and a single car may be a fleet
- PEDAC: Examples

## Solution 1: sort + array solution (lee215's modded)

- O(NLogN) T and O(N) S solution
- initialise variables
  - `cars`: int 2D array where each element is an array of size 2 equal to `[position[i], speed[i]]` sorted in reverse (descending) order of `position[i]`
  - `res`: int set to 0 representing the count of car fleets when all cars have reached `target`
  - `slowestTimeToTarget`: float set to 0 representing the previous car's time needed to reach `target`
- loop thru each element `pos, spd` in `cars`
  - `timeToTarget` = (`target` - `pos`) / `spd`
  - if the current car is slower than the previous slowest car
    - i.e.`timeToTarget` > `slowestTimeToTarget`
    - means we found the leading / first of a new car fleet
    - `res++`
    - `slowestTimeToTarget` = `timeToTarget`
- return `res`
