import heapq
from typing import List
import math


class Solution:
    def minimumEffortPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # abs diff graph from start point,dist[i][j] means min effort from (0,0) to (i,j)
        dist = [[math.inf]*n for _ in range(m)]
        dist[0][0] = 0
        # (distance_from_start_to_current,i,j) min heap to get current minimum distance to optimize for further node
        heap = [(0, 0, 0)]
        while heap:
            dis, x, y = heapq.heappop(heap)
            for addx, addy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if 0 <= x+addx < m and 0 <= y+addy < n and max(dis, abs(grid[x][y]-grid[x+addx][y+addy])) < dist[x+addx][y+addy]:
                    dist[x+addx][y +
                                 addy] = max(dis, abs(grid[x][y]-grid[x+addx][y+addy]))
                    heapq.heappush(
                        heap, (dist[x+addx][y+addy], x+addx, y+addy))
        return dist[m-1][n-1]

obj = Solution()
print(obj.minimumEffortPath([[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))