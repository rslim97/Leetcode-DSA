class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        res=[]
        intervals.sort()
        st,ed=intervals[0]
        for s,e in intervals[1:]:
            if s>ed:
                res.append([st,ed])
                st,ed=s,e
            else:
                # Extend end
                ed=max(ed,e)
        res.append([st,ed])

        return res


if __name__ == '__main__':
    intervals=[[1,3],[2,6],[8,10],[15,18]]
    intervals=[[1,4],[4,5]]
    intervals=[[4,7],[1,4]]
    sol=Solution()
    res=sol.merge(intervals)
    print(res)