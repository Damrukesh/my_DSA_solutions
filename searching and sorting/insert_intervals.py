class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ni=newInterval
        it=intervals
        if not it:
            return [ni]
        ans=[]
        for i in range(len(it)):
            t=it[i]
            if ni[1]<t[0]:
                ans.append(ni)
                return ans+it[i:]
            elif ni[0]>t[1]:
                ans.append(t)
            else:
                ni=[min(ni[0],t[0]),max(ni[1],t[1])]
        ans.append(ni)
        return ans
# trick: compare the new interval with each existing interval to find the correct position for insertion. If the new interval does not overlap with the current interval, add it to the answer list. If it overlaps, merge the intervals by taking the minimum start and maximum end. Finally, add any remaining intervals to the answer list.     