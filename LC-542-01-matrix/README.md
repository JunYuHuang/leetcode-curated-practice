# [LC 542. 01 Matrix](https://leetcode.com/problems/01-matrix/)

## Solution 1: BFS iterative (hiepit's modified)

- O(MN) time and O(MN) space class solution
- process cells by layer in order from 0-cells to non-zero cells (1-cells and non-processed cells)
- modify matrix in-place to make it the resulting distance matrix
- iterate thru matrix and add positions of 0-cells to queue and mark 1-cells as unvisited (set them to -1)
- while queue is not empty
  - pop from front of queue
  - go thru popped cell's 4 neighbours
    - if neighbour cell is out-of-bounds or processed / visited already (not -1)
      - skip to next loop / neighbour
    - set neighbour cell to popped cell's value + 1 (i.e. dist to nearest 0 cell)
- return modified matrix
