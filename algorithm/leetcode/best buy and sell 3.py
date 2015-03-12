class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        profit = 0
        if prices:
            n = len(prices)
            minPrice = prices[0]
            maxPrice = prices[-1]

            dpl = [0]*n
            dpr = [0]*n
            for i in range(1,n):
                minPrice = min(minPrice, prices[i])
                diff = prices[i] - minPrice
                dpl[i] = max(diff, dpl[i-1])
            for i in range(n-2,-1,-1):
                maxPrice = max(maxPrice, prices[i])
                diff = maxPrice - prices[i]
                dpr[i] = max(diff, dpr[i+1])


            for i in range(n):
                profit = max(profit, dpr[i]+dpl[i])
        return profit