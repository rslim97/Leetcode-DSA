class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)<2:
            return len(s)
        
        def expand_around_center(l,r):
            while l>=0 and r<len(s) and s[l]==s[r]:
                l-=1
                r+=1
            return s[l+1:r]
         
        max_len=0
        for i in range(len(s)):
            palindrome1=expand_around_center(i,i)
            palindrome2=expand_around_center(i,i+1)
            max_len=max(max_len,len(palindrome1),len(palindrome2))

        return max_len


if __name__ == '__main__':
    s="bbbab"
    # s="b"
    # s="cbbd"
    s="bb"
    sol=Solution()
    res=sol.longestPalindromeSubseq(s)
    print(res)