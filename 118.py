# Pascal's Triangle

class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res=[[1]]
        if numRows==1:
            return res
        for i in range(numRows-1):
            curr_row=[1]
            for j in range(1,i+1):
                curr_row.append(prev_row[j-1]+prev_row[j])
            curr_row.append(1)
            prev_row=curr_row[:]
            res.append(curr_row[:])

        return res


if __name__ == '__main__':
    numRows=5
    sol=Solution()
    res=sol.generate(numRows)
    print(res)
