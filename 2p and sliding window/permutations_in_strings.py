# Problem: Check if s1 permutation is substring of s2
# Pattern: Sliding Window with Character Frequency Array - Fixed size window
# Brute Force: Generate all permutations of s1 and search - O(n! * n)
# Method: Use frequency array, slide window of size len(s1) in s2
# Time: O(n), Space: O(1) fixed alphabet

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
# Problem: Check if s1 permutation is substring of s2
# Pattern: Sliding Window with Character Frequency Hashmap - Fixed size window
# Brute Force: Generate all permutations of s1 and search - O(n! * n)
# Method: Use frequency hashmap, slide window of size len(s1) in s2
   
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        needh={}
        for c in s1:
            needh[c]=1+needh.get(c,0)
        need=len(needh)
        have=0
        haveh={}     
        i,j=0,0
        while j<len(s2):
            if j-i==len(s1):
                if s2[i] in needh and haveh[s2[i]]==needh[s2[i]]:
                    have-=1
                haveh[s2[i]]-=1
                i+=1
            haveh[s2[j]]=1+haveh.get(s2[j],0)
            if s2[j] in needh and haveh[s2[j]]==needh[s2[j]]:
                have+=1
                if have==need:
                    return True
            j+=1
        return False

        