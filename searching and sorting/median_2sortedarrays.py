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


# pattern: binary search on the smaller array, calculate the partition of the larger array based on the partition of the smaller array, check if the partition is valid by comparing the left and right elements of both partitions. If it's valid, calculate the median based on the total length of the combined arrays. If it's not valid, adjust the binary search range accordingly.
# trick: use float('-inf') and float('inf') to handle edge cases when the partition is at the beginning or end of the array.

# Goat problem: https://leetcode.com/problems/median-of-two-sorted-arrays/description/