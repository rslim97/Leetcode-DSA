class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        h,w=len(text1)+1,len(text2)+1
        memo=[[0]*w for _ in range(h)]
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i]==text2[j]:
                    memo[i+1][j+1]=1+memo[i][j]
                else:
                    memo[i+1][j+1]=max(memo[i][j+1],memo[i+1][j])

        return memo[len(text1)][len(text2)]


if __name__ == '__main__':
    text1="abcd"
    text2="abc"
    text1="abcde"
    text2="ace"
    text1="abc"
    text2="def"
    sol=Solution()
    res=sol.longestCommonSubsequence(text1,text2)
    print(res)