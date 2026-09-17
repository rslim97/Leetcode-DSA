class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # max_profit=0
        # for i in range(len(prices)-1):
        #     for j in range(i+1,len(prices)):
        #         if prices[i]<prices[j]:
        #             profit=prices[j]-prices[i]
        #             max_profit=max(max_profit,profit)

        # return max_profit

        min_price=float('inf')
        max_profit=0
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]

            profit=prices[i]-min_price
            max_profit=max(max_profit,profit)

        return max_profit


if __name__ == '__main__':
    prices=[7,1,5,3,6,4]
    # prices=[7,6,5,4,3,2]
    sol=Solution()
    res=sol.maxProfit(prices)
    print(res)