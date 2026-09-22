class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet=set(wordDict)
        memo=[False]*(len(s)+1)
        memo[0]=True
        for i in range(1,len(s)+1):
            for j in range(i):
                if memo[j] and s[j:i] in wordSet:
                    memo[i]=True
                    break
        
        return memo[len(s)]


if __name__ == '__main__':
    s="leetcode"
    wordDict=["leet","code"]
    sol=Solution()
    res=sol.wordBreak(s,wordDict)
    print(res)