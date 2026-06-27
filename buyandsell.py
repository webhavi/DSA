from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0        # Buying day
        right = 1       # Selling day
        maxp = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxp = max(maxp, profit)
            else:
                left = right

            right = right+1

        return maxp
