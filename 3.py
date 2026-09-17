class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen=set()
        max_len=0
        l=0
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l+=1
            
            seen.add(s[r])
            length=r-l+1
            max_len=max(max_len,length) 

        return max_len
            
        # seen=dict()
        # max_len=0
        # l=0
        # for r in range(len(s)):
        #     if s[r] in seen and seen[s[r]]>=l:
        #         l=seen[s[r]]+1

        #     seen[s[r]]=r
        #     max_len=max(max_len,r-l+1)

        # return max_len


if __name__ == '__main__':
    s="abcabc"
    s="bbbbb"
    s="pwwkew"
    # s="abc"
    # s="ccbbcc"
    sol=Solution()
    res=sol.lengthOfLongestSubstring(s)
    print(res)