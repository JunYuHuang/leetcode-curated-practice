# O(N) T and O(K) S sliding window solution
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # max window size = k + 1
        if k + 1 < 2 or len(nums) < 2:
            return False
        visit = set()
        l = 0
        for r in range(len(nums)):
            windowSize = r - l + 1
            if windowSize >= 2 and nums[r] in visit:
                return True
            visit.add(nums[r])
            if windowSize == k + 1:
                visit.remove(nums[l])
                l += 1
        return False
