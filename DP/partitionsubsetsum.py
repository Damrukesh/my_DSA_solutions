# Problem: Determine whether an array can be partitioned into two subsets with equal sum.
# Brute force: Try all subset combinations and compare sums, which is exponential.
# Solution approach: Use a set of reachable subset sums and update it for each number.
# Time complexity: O(n * target), Space complexity: O(target).
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target=sum(nums)/2
        ss=set()
        ss.add(0)
        for c in nums:
            news=set()
            for s in ss:
                news.add(c+s)
                news.add(s)
            ss=news
        if target in ss:
            return True
        return False

        
            


        