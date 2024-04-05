# O(N) T and O(1) S two pointers solution (@sergiofranklin8809's modded)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        NUMS_LEN = len(nums)
        count = 1
        l = 1

        for r in range(1, NUMS_LEN):
            if nums[r - 1] == nums[r]:
                count += 1
            else:
                count = 1
            if count < 3:
                nums[l] = nums[r]
                l += 1

        return l
