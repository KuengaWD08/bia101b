# Buying and selling stock
#using 2 pointer
#use line graph to explain
class Solution:
    def maxProfit(self, prices)
     left = 0
     right= 1
     max_profit = 0

     while right < len(prices):
         current_profit = prices(right) - prices(left)
         if current_profit > 0:#if not negative
             if max_profit < current_profit:
                max_profit = current_profit
         right = right + 1

     else:
            left = left +1
            right = right + 1

       1 #if negative