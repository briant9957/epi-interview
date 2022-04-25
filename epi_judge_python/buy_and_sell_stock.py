from typing import List

from test_framework import generic_test


def buy_and_sell_stock_once(prices: List[float]) -> float:
    maxProfit = 0
    if not prices:
        return maxProfit
    
    minStock = prices[0]
    for price in prices:
        maxProfit = max(maxProfit, price-minStock)
        minStock = min(minStock, price)

    return maxProfit


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('buy_and_sell_stock.py',
                                       'buy_and_sell_stock.tsv',
                                       buy_and_sell_stock_once))
