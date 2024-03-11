# O(N) T and O(N) S prefix sums solution
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        NUMS_LEN = len(nums)
        prefixSums = [0] * NUMS_LEN
        for i in range(NUMS_LEN):
            prefixSums[i] = nums[i]
            if i > 0:
                prefixSums[i] += prefixSums[i - 1]
        for i in range(NUMS_LEN):
            leftSum = 0 if i == 0 else prefixSums[i - 1]
            rightSum = 0 if i == NUMS_LEN else (
                prefixSums[NUMS_LEN - 1] - prefixSums[i]
            )
            if leftSum == rightSum:
                return i
        return -1
