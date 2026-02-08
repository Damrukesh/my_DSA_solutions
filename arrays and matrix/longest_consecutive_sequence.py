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

# Time Complexity: O(N) where N is the number of elements in the input list nums.
# Space Complexity: O(N) for storing the elements in the set s.
# Pattern: Hash Set, Linear Scan     