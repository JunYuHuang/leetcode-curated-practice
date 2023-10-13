# O(N) T and O(N) S max heap + queue solution (NeetCode's modded)
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = {}
        for t in tasks:
            count[t] = count.get(t, 0) + 1
        maxHeap = []
        for k in count:
            maxHeap.append(-1 * count[k])
        heapq.heapify(maxHeap)
        queue = deque() # of elements [readyTime, count]
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                count = heapq.heappop(maxHeap)
                if count < -1:
                    queue.append([time + n, count + 1])
            if queue and queue[0][0] <= time:
                readyTime, count = queue.popleft()
                heapq.heappush(maxHeap, count)
        return time
