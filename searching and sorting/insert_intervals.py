# Problem: Insert new interval into list of non-overlapping intervals
# Pattern: Interval Merging - Compare new interval with existing ones
# Brute Force: Use output without merging, then sort - O(n log n)
# Method: Compare new interval with each existing interval to find merge range
# Time: O(n), Space: O(n) for output

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