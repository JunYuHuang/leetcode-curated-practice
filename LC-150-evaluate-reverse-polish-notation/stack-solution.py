# O(N) T and O(N) S stack solution
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opToFn = {
            "+": lambda l, r: l + r,
            "-": lambda l, r: l - r,
            "*": lambda l, r: l * r,
            "/": lambda l, r: int(l / r)
        }
        nums = []
        for c in tokens:
            if c not in opToFn:
                nums.append(int(c))
            elif len(nums) >= 2:
                right = nums.pop()
                left = nums.pop()
                res = opToFn[c](left, right)
                nums.append(res)
        return nums[0]
