# Problem: Find length of longest subarray with sum equal to k
# Pattern: Prefix Sum + Hash Map - Store first occurrence of each prefix sum
# Brute Force: Check all subarrays and calculate their sums - O(n^2)
# Method: Use prefix sum to convert to "find subarray with sum 0" problem
# Time: O(n), Space: O(n)

class Solution:
    def longestSubarray(self, arr, k):  
        ans=0        
        prefix=0
        h={}
        h[prefix]=-1
        for i in range(len(arr)):
            prefix+=arr[i]
            if prefix-k in h:
                ans=max(ans,i-h[prefix-k])
            if prefix not in h:
                h[prefix]=i
        return ans    