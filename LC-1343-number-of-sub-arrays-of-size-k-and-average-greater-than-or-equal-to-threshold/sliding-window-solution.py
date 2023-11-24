# O(N) T and O(1) S sliding window solution
class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        currSum = 0
        res = 0
        arrLen = len(arr)
        for r in range(arrLen):
            currSum += arr[r]
            if r - l + 1 == k:
                average = currSum / k
                if average >= threshold:
                    res += 1
                currSum -= arr[l]
                l += 1
        return res
