# O(1) T and O(1) S prefix sums solution (NeetCode's modded)
class NumArray:
    def __init__(self, nums: List[int]):
        total = 0
        numsLen = len(nums)
        self.prefix = [0 for i in range(numsLen)]

        for i in range(numsLen):
            self.prefix[i] = total + nums[i]
            total += nums[i]

    def sumRange(self, left: int, right: int) -> int:
        prefixLeft = 0 if left == 0 else self.prefix[left - 1]
        return self.prefix[right] - prefixLeft


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
