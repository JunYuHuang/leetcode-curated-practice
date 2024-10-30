# [LC 973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## General Notes

- PEDAC: Problem
  - input:
    - `points`: int matrix that represents a list of points on the X-Y plane
      - of size in range \[k, 10^4]
      - of values for `points[i]` in range \[-10^4, 10^4]
      - guaranteed to be non-empty
    - `k`: int representing the `k` number of points (coordinates) closest to the origin (0, 0) based on Euclidean distance
      - of value in range \[1, `points.length`]
      - guaranteed to be a valid amount
  - output:
    - `res`: int matrix of size `k`
      - of size `k`
      - order of subarrays does not matter
      - of `k` points closest / to the origin (0, 0) based on Euclidean distance
        - i.e. distances with points are the `k` smallest
  - Euclidean between any point (x, y) and the origin (0, 0) is:
    - sqrt((x - 0)^2 + (y - 0)^2)
    - = sqrt(x^2 + y^2)
- PEDAC: Examples

## Solution 1: max heap

- O((N - K) \* LogN) T and O(N) S solution
- helper function `euclidDistance(point)`
  - returns square root of sum of `point[0]` squared and `point[1]` squared
- create `distAndPoints` array of subarrays
  - subarray's first element is `euclidDistance(point)` of some point in `points`
  - subarray's second element is some point in `points`
- make `distAndPoints` a max heap
- heap pop from `distAndPoints` until it is of size `k`
- set `res` to `distAndPoints` transformed where each new element is only the original element's second subarray point element
- return `res`

## Solution 2: min heap (NeetCode's modded)

- O(K \* LogN) T and O(N) S solution
- helper function `euclidDistance(point)`
  - returns square root of sum of `point[0]` squared `point[1]` squared
- set `distAndPoints` array of subarrays
  - subarray's first element is euclid distance float computed from a point
  - subarray's second element is the position of the point in `points`
- make `distAndPoints` into a min heap
- set `res` array to empty array
- iterate `k` times,
  - heap pop `el` from `distAndPoints`
  - push point in `points` at index `el`'s second element to `res`
- return `res`
