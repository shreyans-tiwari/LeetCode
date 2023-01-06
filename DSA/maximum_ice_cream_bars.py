"""
It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n,
where costs[i] is the price of the ith ice cream bar in coins.
The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
Return the maximum number of ice cream bars the boy can buy with coins coins.
Note: The boy can buy the ice cream bars in any order.
"""

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()

        for i in range(len(costs)):
            coins = coins-costs[i]
            if coins < 0:
                return i

        return i+1
      
