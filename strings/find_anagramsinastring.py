# Problem: Find all indices where anagrams of p start in s
# Pattern: Hash Map + Sliding Window - Match character frequencies
# Brute Force: Generate all anagrams of p, search in s - O(n! * n)
# Method: Maintain frequency map of p, slide window in s, compare maps
# Time: O(n), Space: O(1) fixed alphabet size

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        h={}
        for c in p:
            if c in h:
                h[c]+=1
            else:
                h[c]=1
        have=0
        need=len(p)
        smap={}
        i,j=0,0   
        while j<len(s):
            if s[j] in smap:
                smap[s[j]]+=1
            else:
                smap[s[j]]=1
            if j-i+1==len(p):
                if smap==h:
                    ans.append(i)
                if smap[s[i]]==1:
                    del smap[s[i]]
                else:
                    smap[s[i]]-=1    
                i+=1
            j+=1    
        return ans            


                

