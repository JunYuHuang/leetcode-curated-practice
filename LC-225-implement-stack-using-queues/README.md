# [LC 225. Implement Stack using Queues](https://leetcode.com/problems/implement-stack-using-queues/)

## Solution 1: queue (StefanPochmann's modified)

- O(N) time and O(N) space class solution
- use queue and maintain it as a "stack" (reversed stack order)
- pop(), top(), empty = use queue equivalent operations
- push(): push to q, pop from top and push to q for q size - 1 times
