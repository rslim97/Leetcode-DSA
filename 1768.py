class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        p,q=0,0
        res=''
        while p<len(word1) and q<len(word2):
            res+=word1[p]
            p+=1
            res+=word2[q]
            q+=1
        while p<len(word1):
            # Extend remaining word1
            res+=word1[p]
            p+=1
        while q<len(word2):
            # Extend remaining word2
            res+=word2[q]
            q+=1
        return res


if __name__ == '__main__':
    word1='abc'
    word2='pqr'
    word1='ab'
    word2='pqrs'
    sol=Solution()
    res=sol.mergeAlternately(word1,word2)
    print(res)