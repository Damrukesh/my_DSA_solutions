class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        tmap={}
        for c in t:
            if c in tmap:
                tmap[c]+=1
            else:
                tmap[c]=1
        smap={}
        res,reslength=[-1,-1],float('inf')
        l=0
        have=0
        need=len(tmap)
        for j in range(len(s)):
            if s[j] in smap:
                smap[s[j]]+=1
            else:
                smap[s[j]]=1

            if s[j] in tmap and smap[s[j]]==tmap[s[j]]:
                have+=1

            while have==need:
                if (j-l+1)<reslength:
                    res=[l,j]
                    reslength=j-l+1
                smap[s[l]]-=1
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1
        a,b=res                  
        return s[a:b+1] if reslength!=float('inf') else ""   
    
# Time Complexity: O(N) where N is the length of the input string s. We have a single pass through the string to find the minimum window substring, which takes O(N) time.
# Space Complexity: O(M) where M is the size of the character set. We are
#pattern: Hash Map, Sliding Window      
#problem link: https://leetcode.com/problems/minimum-window-substring/description/

        