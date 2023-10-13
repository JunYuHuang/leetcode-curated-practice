# [LC 621. Task Scheduler](https://leetcode.com/problems/task-scheduler/)

## General Notes

- PEDAC: Problem
  - input:
    - `tasks`: ordered list of tasks for a CPU to complete represented by a string array
      - of size in the range \[1, 10^4]
      - of uppercase English letters / chars values only
    - `n`: CPU cooldown time represented by an int
      - in the range \[0, 100]
      - there must also be `n` units of time between any two same tasks
  - output:
    - `res`: int that represents the min units of time needed (i.e. fastest time) for the CPU to complete all tasks in `tasks`
  - cooldown time `n` applies between 2 consecutive and identical tasks only
  - cooldown time is calcuated AFTER a task is done
  - time is incremented by 1 after a task is done
  - if no task can be done because of cooldowns, time still progresses
- PEDAC: Examples

## Solution 1: max heap + queue solution (NeetCode's modded)

- O(N) T and O(N) S solution
- initialise variables
  - `time`: int that represents the current CPU time initially set to 0
  - `count`: hashmap that maps each unique task to its number of occurrences in `tasks` initially set to an empty hashmap
  - `maxHeap`: max heap of elements `count` (that represents the quantity of each unique task in `tasks`) initially set to an empty array that is maintained so `count` is less than 0
  - `queue`: int array processed as a queue whose each element `[readyTime, count]` represents the when a task is ready to be processed and how many of that task is left
- loop thru every element `t` in `tasks` to build `count` hashmap
- loop thru every key-value pair in `count` hashmap to build `maxHeap` array
- heapify `maxHeap` array as a max heap
- while either `maxHeap` or `queue` is not empty,
  - `time++`
  - if `maxHeap` is not empty,
    - `count` = pop from `maxHeap`
    - if `count` > 1,
      - push `[time + n, count - 1]` to `queue`
  - if `queue` is not empty and `queue[0][0]` == `time`,
    - dequeue or pop 1st element `[readyTime, count]` from `queue`
      - push `count` to `maxHeap`
- return `time`
