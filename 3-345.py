class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels=set('aeiouAEIOU')
        l,r=0,len(s)-1
        s=list(s)
        while l<r:
            if s[l] in vowels and s[r] in vowels:
                s[l],s[r]=s[r],s[l]
                l+=1
                r-=1
            if s[l] not in vowels:
                l+=1
            if s[r] not in vowels:
                r-=1
        return ''.join(s)


if __name__ == '__main__':
    s="IceCreAm"
    sol=Solution()
    res=sol.reverseVowels(s)
    print(res)