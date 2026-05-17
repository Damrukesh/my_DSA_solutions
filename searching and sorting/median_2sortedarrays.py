# Problem: Find median of two sorted arrays
# Pattern: Binary Search - Partition arrays to find median position
# Brute Force: Merge arrays and find median - O((m+n) log(m+n))
# Method: Binary search on smaller array, find valid partition where all left <= all right
# Time: O(log(min(m,n))), Space: O(1)

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=[]
        total=len(nums1)+len(nums2)
        half=total//2
        if len(nums1)>len(nums2):
            A,B=nums2,nums1
        else:
            A,B=nums1,nums2
        l,r=0,len(A)-1
        while True:
            m=(l+r)//2
            m2=half-m-2
            l1=A[m] if m>=0 else float('-inf')
            r1=A[m+1] if (m+1)<len(A) else float('inf')
            l2=B[m2] if m2>=0 else float('-inf')
            r2=B[m2+1] if (m2+1)<len(B) else float('inf')

            if l1<=r2 and l2<=r1:
                if total%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return min(r1,r2)    
            elif l1>r2:
                r=m-1
            else:
                l=m+1