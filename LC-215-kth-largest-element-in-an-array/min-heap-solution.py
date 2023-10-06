# O(N + (N - K) * LogN) T and O(N) S min heap solution
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        return nums[0]
