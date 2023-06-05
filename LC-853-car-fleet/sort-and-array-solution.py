# O(NLogN) T and O(N) S sort + array solution (lee215's modded)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        slowestTimeToTarget = 0
        res = 0
        cars = [[position[i], speed[i]] for i in range(0, len(speed))]
        cars.sort(reverse = True)

        for [pos, spd] in cars:
            timeToTarget = (target - pos) / spd
            if timeToTarget > slowestTimeToTarget:
                slowestTimeToTarget = timeToTarget
                res += 1
        return res
