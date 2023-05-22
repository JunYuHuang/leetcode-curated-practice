# O(N) T and O(N) S set solution (NeetCode's expl.)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        numsSet = set(nums)
        for n in nums:
            if n - 1 in numsSet:
                continue
            count = 1
            while n + count in numsSet:
                count += 1
            if count > res: res = count
        return res
