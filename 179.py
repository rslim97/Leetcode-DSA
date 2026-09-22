class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        sorted_nums=self._mergesort(nums)
        largest_num="".join(map(str,sorted_nums))
        return "0" if largest_num[0]=="0" else largest_num


    def _mergesort(self,x):
        if len(x)<=1:
            return x
        else:
            l,r=0,len(x)-1
            mid=l+(r-l+1)//2
            left_array=self._mergesort(x[:mid])
            right_array=self._mergesort(x[mid:])
            return self._merge(left_array,right_array)

    def _merge(self,left_array,right_array):
        i,j=0,0
        tmp=[]
        while i<len(left_array) and j<len(right_array):
            if self._compare(left_array[i],right_array[j]):
                tmp.append(left_array[i])
                i+=1
            else:
                tmp.append(right_array[j])
                j+=1

        tmp.extend(left_array[i:])
        tmp.extend(right_array[j:])
        return tmp

    def _compare(self,num1,num2):
        return str(num1)+str(num2)>str(num2)+str(num1)


if __name__ == '__main__':
    nums=[10,2]
    nums=[3,30,34,5,9]
    sol=Solution()
    res=sol.largestNumber(nums)
    print(res)