class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str, lowercase English letters
        :rtype: bool
        """
        return len(set(sentence))==26


if __name__ == '__main__':
    s="thequickbrownfoxjumpsoverthelazydog"
    sol=Solution()
    res=sol.checkIfPangram(s)
    print(res)