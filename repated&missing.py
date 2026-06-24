from collections import defaultdict
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = defaultdict(int)

        # Count frequencies
        for i in range(n):
            for j in range(n):
                count[grid[i][j]] += 1

        double, missing = 0, 0

        # Find repeated and missing numbers
        for num in range(1, n * n + 1):
            if count[num] == 0:
                missing = num
            if count[num] == 2:
                double = num

        return [double, missing]