# My hashmap O(n) T + O(1) S solution
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = 0
        maxCount = 0
        elToCount = {}

        for n in nums:
            if n not in elToCount:
                elToCount[n] = 0
            elToCount[n] += 1
            
            if elToCount[n] > maxCount:
                maxCount = elToCount[n]
                res = n

        return res
