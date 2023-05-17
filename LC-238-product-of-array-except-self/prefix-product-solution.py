# NeetCode's O(N) T and O(1) S prefix product solution (NeetCode's modded)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        res = [1] * N
        prod = 1
        for i in range(N):
            res[i] = prod
            prod *= nums[i]
        prod = 1
        for i in range(N - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
        return res
