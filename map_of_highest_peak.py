from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        def getNeighborhood(i, j):  # get l, r, u, d if possible
            neighbors = []
            if i+1 < N:
                neighbors.append((i+1, j))
            if i-1 > -1:
                neighbors.append((i-1, j))
            if j+1 < M:
                neighbors.append((i, j+1))
            if j-1 > -1:
                neighbors.append((i, j-1))
            return neighbors

        N = len(isWater)
        M = len(isWater[0])
        grid = [[float("inf") if not isWater[i][j] else 0 for j in range(
            len(isWater[0]))] for i in range(len(isWater))]
        waters = deque([])

        for i in range(N):  # get all waters
            for j in range(M):
                if isWater[i][j]:
                    waters.append((i, j))

        while waters:  # BFS
            x, y = waters.popleft()
            for i, j in getNeighborhood(x, y):
                if not isWater[i][j] and abs(grid[x][y] - grid[i][j]) > 1:
                    grid[i][j] = grid[x][y] + 1
                    waters.append((i, j))

        return grid

obj = Solution()
print(obj.highestPeak([[0,0,1],[1,0,0],[0,0,0]]))
