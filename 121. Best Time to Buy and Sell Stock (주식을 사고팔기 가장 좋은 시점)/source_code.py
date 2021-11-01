import sys

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_price = 0

        for i in range(len(prices)-1):
            for j in range(i, len(prices)):
                max_price = max(prices[j] - prices[i], max_price)

        return max_price

    def maxProfit1(self, prices: list[int]) -> int:
        profit  = 0
        min_price = sys.maxsize

        for price in prices:
            min_price = min(price, min_price)
            profit = max(price - min_price, profit)

        return profit





if __name__ == "__main__":
    prices = [7,1,5,3,6,4]

    cs = Solution()

    print(cs.maxProfit1(prices))