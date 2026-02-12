"""
The cost of a stock on each day is given in an array, find the max profit
that you can make by buying and selling in those days.
For example, if the given array is {100, 180, 260, 310, 40, 535, 695},
the maximum profit can earned by buying on day 0, selling on day 3.
Again buy on day 4 and sell on day 6. If the given array of prices is sorted
in decreasing order, then profit cannot be earned at all.

Solution : https://www.geeksforgeeks.org/stock-buy-sell/
"""

"""
Problem : https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Logic:
You buy stock by today price and hold, price is hold, if price at next day
is less than Today's price, hold is replace.
Otherwise, sold stock, but if next day, the profit is higher, you sold by
next profit.

Dynamic Programming
"""


def max_profit_single_transaction(prices):
    """Find max profit with single buy-sell transaction."""
    if not prices or len(prices) < 2:
        return 0

    hold = prices[0]
    profit = 0

    for p in prices[1:]:
        if p < hold:
            hold = p
        else:
            if p - hold > profit:
                profit = p - hold
    return profit


def get_max_profit(arr):
    """Find all buy-sell opportunities for maximum profit."""
    arr_size = len(arr)
    # Price must be there for minimum 2 days.
    if arr_size == 1:
        return

    x = 0
    while x < (arr_size - 1):
        # Getting minimum price and comparing with next element
        while (x < (arr_size - 1)) and (arr[x + 1] <= arr[x]):
            x += 1
        if x == arr_size - 1:
            break
        buy_stock = x
        x += 1
        # Getting Maximum Element
        while (x < arr_size) and (arr[x] >= arr[x - 1]):
            x += 1
        sell_stock = x - 1
        print("Buy on day: ", buy_stock, "\t", "Sell on day: ", sell_stock)


def max_profit_multiple_transactions(prices):
    """Find max profit with multiple buy-sell transactions."""
    if not prices or len(prices) < 2:
        return 0

    run_profit = 0
    for i in range(len(prices)):
        if i == 0:
            buy = prices[i]
        else:
            diff = prices[i] - buy

            if diff > 0:
                run_profit = diff if diff > run_profit else run_profit
            else:
                buy = prices[i]
    return run_profit


# Test cases
arr = [100, 180, 260, 310, 40, 535, 695]
print("Max profit (single transaction):", max_profit_single_transaction(arr))
# Output: Max profit (single transaction): 655

print("\nBuy-Sell opportunities:")
get_max_profit(arr)
# Output: Buy on day:  0    Sell on day:  3
#         Buy on day:  4    Sell on day:  6
