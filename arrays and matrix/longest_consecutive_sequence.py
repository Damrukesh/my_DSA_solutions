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
# method: We use a hash set to store the unique elements of the input list for O(1) average time complexity lookups. We iterate through each number in the set, and for each number that is the start of a sequence (i.e., n-1 is not in the set), we count how long the consecutive sequence is by checking for n+1, n+2, etc. We keep track of the longest sequence found and return it at the end.     