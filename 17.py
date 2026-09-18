
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        phone={"2":"abc",
               "3":"def",
               "4":"ghi",
               "5":"jkl",
               "6":"mno",
               "7":"pqrs",
               "8":"tuv",
               "9":"wxyz"
               }
        
        res=[]
        track=""
        def helper(track,depth):
            if depth==len(digits):
                res.append(track[:])
                return
            for c in phone[digits[depth]]:
                # Make choice
                track+=c
                helper(track,depth+1)
                # Undo choice/backtrack
                track=track[:-1]

        helper(track,0)
        return res

if __name__ == '__main__':
    digits="23"
    sol=Solution()
    res=sol.letterCombinations(digits)
    print(res)