# O(N) T and O(N) S hashmap solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        if N == 2: return [0, 1]
        valToPos = {}
        for i in range(N):
            diff = target - nums[i]
            if diff in valToPos:
                return [i, valToPos[diff]]
            valToPos[nums[i]] = i
