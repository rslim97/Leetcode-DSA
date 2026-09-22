class Solution(object):
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def mergesort(x):
            if len(x)<=1:
                return x
            else:
                l,r=0,len(x)-1
                mid=l+(r-l+1)//2
                left_array=mergesort(x[:mid])
                right_array=mergesort(x[mid:])
                i,j=0,0
                res=[]
                while i<len(left_array) and \
                      j<len(right_array):
                    if left_array[i]<right_array[j]:
                        res.append(left_array[i])
                        i+=1
                    else:
                        res.append(right_array[j])
                        j+=1

                if i<len(left_array):
                    res.extend(left_array[i:])
                if j<len(right_array):
                    res.extend(right_array[j:])

                return res

        return mergesort(nums)

        # def mergesort(l,r):
        #     if l>=r:
        #         return [nums[l]]
        #     else:
        #         mid=l+(r-l)//2
        #         left_array=mergesort(l,mid)
        #         right_array=mergesort(mid+1,r)

        #         return merge(left_array,right_array)

        # def merge(left_array,right_array):
        #     tmp=[]
        #     i,j=0,0
        #     while i<len(left_array) and j<len(right_array):
        #         if left_array[i]<right_array[j]:
        #             tmp.append(left_array[i])
        #             i+=1
        #         else:
        #             tmp.append(right_array[j])
        #             j+=1

        #     tmp.extend(left_array[i:])
        #     tmp.extend(right_array[j:])
        #     return tmp

        # return mergesort(0,len(nums)-1)


if __name__ == '__main__':
    nums=[6,17,-1,-11,23,2,1]
    sol=Solution()
    res=sol.sortArray(nums)
    print(res)