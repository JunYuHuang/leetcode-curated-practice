# O(N) T and O(N) S sliding window + monotonic decreasing queue solution (NeetCode's modded)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        q = deque()
        numsLen = len(nums)
        for r in range(numsLen):
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            q.append(r)
            if q[0] < l:
                q.popleft()
            if r - l + 1 == k:
                res.append(nums[q[0]])
                l += 1
        return res
