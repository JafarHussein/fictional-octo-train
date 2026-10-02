class Solution:
    def maxProfit(self, prices):
        lowest_price=prices[0]
        for i in range(1, len(prices)):
            if prices[i]>=lowest_price:
                continue
            else:
                lowest_price=prices[i]
        highest_price=lowest_price
        for j in range(prices.index(lowest_price), len(prices)):
            if prices[j]<=highest_price:
                continue
            else:
                highest_price=prices[j]
                
        maximum_profit=highest_price - lowest_price
        
        return maximum_profit
            
prices = [7,1,5,3,6,4]  
sol_instance=Solution()
print(sol_instance.maxProfit(prices))