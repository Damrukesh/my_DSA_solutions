# Problem: Find count of subarrays with XOR equal to k
# Pattern: Prefix XOR + Hash Map - If prefix1 XOR prefix2 = k, then subarray has XOR = k
# Brute Force: Check all subarrays and calculate XOR - O(n^2)
# Method: Use XOR property - if prefix_xor XOR k exists in map, found valid subarrays
# Time: O(n), Space: O(n)

class Solution:
    def subarrayXor(self, arr, k):
        h={}
        prefix=0
        h[prefix]=1
        count=0
        for n in arr:
            prefix=prefix^n
            if prefix^k in h:
                count+=h[prefix^k]
            if prefix not in h:
                h[prefix]=1
            else:
                h[prefix]+=1
        return count    