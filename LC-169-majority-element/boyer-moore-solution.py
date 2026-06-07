# NeetCode's Boyer-Moore O(n) T + O(1) S modded solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if count == 0:
                res = n
            if n == res:
                count += 1
            else:
                count -= 1

        return res
