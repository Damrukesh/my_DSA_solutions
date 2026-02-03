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


#pattern : just a logical trick  #time complexity : O(n)