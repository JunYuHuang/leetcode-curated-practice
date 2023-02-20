# [LC 733. Flood Fill](https://leetcode.com/problems/flood-fill/)

## Solution 1: BFS iterative

- O(MN) time and O(MN) space solution
- return image if start cell has same color as given color
- initialise empty visit set (of (r, c)), ROWS, COLS, queue with starting cell
- startColor = starting cell's original color
- while queue is not empty
  - pop (r, c) from queue's front
  - set (r, c) to target color
  - visit (r, c)
  - for (r, c)'s 4 vertical and horizontal neighbours
    - if neighbour is out-of-bounds or visited or whose value is not startColor
      - skip to next loop
    - push neighbour to queue
- return image matrix

## Solution 2: DFS iterative

- O(MN) time and O(MN) space solution
- same approach as BFS iterative but
  - replace queue with stack
    - optional: use array / list instead of deque for stack
  - pop() instead of popleft() to process nodes / cells

## Solution 3: DFS recursive

- O(MN) time and O(MN) space solution
- same approach as DFS iterative but
  - move stack processing logic into a non-pure recursive helper function dfs()
  - for dfs(r, c)
    - make recursive calls to (r, c)'s 4 neighbours
      - optional: use directions array to loop thru and make recursive calls
