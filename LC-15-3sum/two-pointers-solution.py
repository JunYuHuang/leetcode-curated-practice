# O(N^2) T and O(min(1, N)) S sorted + two pointers solution (NeetCode's modded)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, N = [], len(nums)
        nums.sort()

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, N - 1
            while l < r:
                currSum = nums[i] + nums[l] + nums[r]
                if currSum == 0:
                    res.append([nums[i], nums[l], nums[r]])
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif currSum < 0:
                    l += 1
                else:
                    r -= 1
        return res
