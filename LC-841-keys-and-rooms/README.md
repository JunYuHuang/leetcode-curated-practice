# [LC 841. Keys and Rooms](https://leetcode.com/problems/keys-and-rooms/)

## Solution 1: BFS iterative

- O(N + M) time and O(N) space solution
- initialise empty visit set, queue with first room's key (0)
- while queue is not empty
  - pop room from front of queue
  - visit room
  - for key in rooms\[room]
    - skip if key visited already
    - add key to queue
- return true if len(visit) == len(rooms) else false

## Solution 2: DFS recursive

- O(N + M) time and O(N)? space solution
- same approach as solution 1 but
  - convert queue algorithm into a helper recursive function
  - inside dfs(room) function
    - return if room visited
    - visit room
    - for each key inside the room, call itself on it recursively
