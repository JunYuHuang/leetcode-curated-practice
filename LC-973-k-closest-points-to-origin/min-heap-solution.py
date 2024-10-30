# O(KLogN) T and O(N) S min heap solution (NeetCode's modded)
from math import sqrt
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        POINTS_LEN = len(points)
        distAndPoints = []
        res = []

        for i in range(POINTS_LEN):
            dist = self.euclidDistance(points[i])
            distAndPoints.append([dist, i])
        heapq.heapify(distAndPoints)

        for _ in range(k):
            dist, i = heapq.heappop(distAndPoints)
            res.append(points[i])

        return res

    def euclidDistance(self, point):
        return sqrt(point[0] ** 2 + point[1] ** 2)