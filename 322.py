class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        # memo=[float('inf')]*(amount+1)
        # memo[0]=0
        # for a in range(1,amount+1):
        #     for coin in coins:
        #         if coin<=a:
        #             memo[a]=min(memo[a],memo[a-coin]+1)

        # return memo[amount] if memo[amount]!=float('inf') else -1

        
        h,w=len(coins)+1,amount+1
        memo=[[float('inf')]*w for _ in range(h)]

        for i in range(h):
            memo[i][0]=0

        for i in range(1,h):
            coin=coins[i-1]
            for j in range(1,w):
                if j>=coin:
                    memo[i][j]=min(1+memo[i][j-coin],memo[i-1][j])
                else:
                    memo[i][j]=memo[i-1][j]
        return -1 if memo[h-1][w-1]==float('inf') else memo[h-1][w-1]


if __name__ == '__main__':
    coins=[1,4,6]
    amount=9
    # coins=[1,2,5]
    # amount=11
    # coins=[3]
    # amount=2
    # coins=[1]
    # amount=0
    # coins=[2147483647]
    # amount=2
    sol=Solution()
    res=sol.coinChange(coins, amount)
    print(res)