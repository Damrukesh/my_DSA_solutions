# Problem: Rearrange array to next lexicographically greater permutation in-place
# Pattern: Find rightmost ascending pair, swap with larger element, reverse suffix
# Brute Force: Generate all permutations and find next one - O(n! * log(n!))
# Method: (1) Find rightmost i where nums[i] < nums[i+1] (2) Find rightmost j > i with nums[j] > nums[i] (3) Swap (4) Reverse suffix
# Time: O(n), Space: O(1)

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        j=len(nums)-1
        index=-1
        while j>0:
            if nums[j]>nums[j-1]:
                index=j-1
                break
            j-=1    
        if index!=-1:
            for j in range(len(nums) - 1, index, -1):
                if nums[j] > nums[index]:
                    break        
            nums[index],nums[j]=nums[j],nums[index]
        a=index+1
        b=len(nums)-1
        while a<=b:
            nums[a],nums[b]=nums[b],nums[a]
            a+=1
            b-=1