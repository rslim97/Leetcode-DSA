class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<2:
            return n
        curr=0
        prev_two=0
        prev_one=1
        for i in range(n-1):
            curr=prev_two+prev_one
            prev_two=prev_one
            prev_one=curr

        return curr

    
if __name__ == '__main__':
    n=7
    sol=Solution()
    res=sol.fib(1)
    print(res)