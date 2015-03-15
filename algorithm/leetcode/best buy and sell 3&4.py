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

def maxprofit2(prices):
    if not prices or len(prices) == 1:
        return 0
    n = len(prices)
    profit = 0
    for i in range(1, n):
        diff = prices[i] - prices[i-1]
        if diff > 0:
            profit += diff

    return profit


def maxprofit4(k, prices):
    if not prices or len(prices) == 1:
        return 0

    n = len(prices)



    dp = [[0] * (n) for i in range(k+1)]

    for i in range(1, k+1):
        curr_profit = -prices[0]
        for j in range(1, n):
            dp[i][j] = max(dp[i][j-1], curr_profit + prices[j])
            curr_profit = max(curr_profit, dp[i-1][j-1] - prices[j])


    return dp[k][n-1]



k = 4
prices = [1,2,4,2,5,7,2,4,9,0]
print(maxprofit4(k, prices))