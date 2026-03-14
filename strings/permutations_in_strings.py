class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        counta=[0]*26
        for c in s1:
            counta[ord(c)-ord("a")]+=1
        count=[0]*26
        i,j=0,0
        while j<len(s2) and i<len(s2):
            count[ord(s2[j])-ord("a")]+=1
            if j-i+1==len(s1):
                if count==counta:
                    return True 
                count[ord(s2[i])-ord("a")]-=1
                i+=1
            j+=1    
        return False

# Time Complexity: O(N) where N is the length of s2
# Space Complexity: O(1) - fixed array of 26 characters
# Pattern: Sliding Window with Character Frequency Array
# Trick: Use fixed array of 26 instead of hashmap to track character frequencies, then compare with sliding window of same size