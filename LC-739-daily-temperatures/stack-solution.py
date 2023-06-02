# O(N) T and O(N) S monotonic decreasing stack solution (NeetCode's modded)
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures)
        answer = [0] * N
        posStack = []

        for i in range(N):
            while posStack and temperatures[posStack[-1]] < temperatures[i]:
                lastPos = posStack.pop()
                daysToWait = i - lastPos
                answer[lastPos] = daysToWait
            posStack.append(i)

        return answer
