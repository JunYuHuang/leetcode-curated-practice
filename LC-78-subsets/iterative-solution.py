# O(N * 2^N) T and O(2^N) S iterative backtracking solution
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        NUMS_LEN = len(nums)
        res = []
        stack = [[0, []]]  # of [i, subset] elements

        while stack:
            i, sub = stack.pop()
            if i >= NUMS_LEN:
                res.append(sub)
                continue
            sub.append(nums[i])
            stack.append([i + 1, sub[:]])
            sub.pop()
            stack.append([i + 1, sub[:]])

        return res