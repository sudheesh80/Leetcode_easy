class Solution:
    def maxProfit(self, prices) -> int:
        max_profit = 0
        price_low ,price_high = prices[0],prices[0]
        for i in range(len(prices)):
            p = prices[i]
            if (p < price_low):
                price_low, price_high = p,p
            if (p > price_high):
                price_high = p
            if ( price_high- price_low > max_profit):
                max_profit = price_high- price_low
        return(max_profit)
prices = [7,6,4,3,1]
ans = Solution()
run = ans.maxProfit(prices)
print(run)
