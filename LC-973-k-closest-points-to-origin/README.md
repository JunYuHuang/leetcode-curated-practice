# [LC 973. K Closest Points to Origin](https://leetcode.com/problems/k-closest-points-to-origin/)

## General Notes

- PEDAC: Problem
  - input:
    - `points`: int matrix that represents a list of points on the X-Y plane
      - of size in range \[k, 10^4]
      - of values for `points[i]` in range \[-10^4, 10^4]
    - `k`: int representing the `k` number of points (coordinates) closest to the origin (0, 0) based on Euclidean distance
      - of value in range \[1, `points.length`]
  - output:
    - `res`: int matrix of size `k` that represents the `k` points closest to the origin (0, 0) based on Euclidean distance
  - Euclidean between any point (x, y) and the origin (0, 0) is:
    - sqrt((x - 0)^2 + (y - 0)^2)
    - = sqrt(x^2 + y^2)
- PEDAC: Examples

## Solution 1: max heap

- O((N - K) * LogN) T and O(N) S solution
- other notes
  - optional to sqrt the Euclidean distance
- initalise variables
  - `maxHeap`: max heap of `[euclidean_distance, [x, y]]` elements treated as min heap initialised as an empty array
  - `res`: int matrix that is initialised as an empty array
- for `i` for size of `points`:
  - `dist` = `sqrt(points[i][0]^2 + points[i][1]^2)`
  - push `[dist, i]` to `maxHeap`
- while size of `maxHeap` > `k`:
  - pop from `maxHeap`
- for each element `e` in `maxHeap`:
  - push `e[1]` (the point / coordinate) to `res`
- return `res`

## Solution 2: min heap (NeetCode's modded)

- O(KLogN) T and O(N) S solution
- same approach as solution 2 but:
  - use min heap instead of max heap
  - pop from heap `k` times instead of `N - k` times
