
stock_prices = [7,1,5,3,6,4]

#each element signifies stock price for a particular day
#stock must be bought first before they can be sold
#find max profit

def maxProfit(stock_prices):
    left_min = float("inf") #at every step, we keep track of the minimum element to the entire left of current element
    max_profit = float("-inf") #also, we keep track of the max profit till now
    for i in stock_prices:
        left_min = min(left_min,i)
        max_profit = max(max_profit, i-left_min)
    return max_profit

print(maxProfit(stock_prices))