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
# Time Complexity: O(N) where N is the length of the input string s. We have a single pass through the string to find all anagrams, which takes O(N) time.
# Space Complexity: O(M) where M is the size of the character set. We are using two hash maps to store the frequency of characters in the pattern and the current window, which takes O(M) space.
#pattern: Hash Map, Sliding Window            


                

