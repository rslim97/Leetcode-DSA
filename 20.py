from collections import deque

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack=deque()
        opens=set(['(','[','{'])
        for i in range(len(s)):
            if s[i] in opens:
                if s[i]=='(':
                    stack.append(')')
                elif s[i]=='[':
                    stack.append(']')
                else:
                    stack.append('}')
            else:
                if stack: 
                    curr=stack.pop()
                else:
                    curr='#'
                if curr!=s[i]:
                    return False

        return not stack

        # stack = []
        # mapping = {')': '(', '}': '{', ']': '['}

        # for char in s:
        #     if char in mapping:
        #         top_element = stack.pop() if stack else '#'
        #         if mapping[char] != top_element:
        #             return False
        #     else:
        #         stack.append(char)

        # return not stack


if __name__ == '__main__':
    # s="()"
    # s="()[]{}"
    # s="(]"
    # s="([])"
    # s="([)]"
    s="["
    s="]"
    sol=Solution()
    res=sol.isValid(s)
    print(res)