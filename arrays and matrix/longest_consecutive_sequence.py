# Problem: Find length of longest consecutive sequence in unsorted array
# Pattern: Hash Set - Smart iteration from sequence starts
# Brute Force: Sort array and iterate to find consecutive sequences - O(n log n)
# Method: Use set for O(1) lookup, only iterate from sequence starts (n-1 not in set)
# Time: O(n), Space: O(n)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s=set(nums)
        longest=0

        for n in s:
            if n-1 not in s:
                length=1
                while n+length in s:
                    length+=1
                longest=max(longest,length)
        return longest     