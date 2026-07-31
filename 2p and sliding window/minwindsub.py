# 76. Minimum Window Substring
# Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".
# brute force: check all substrings of s and see if they contain all characters in t, and keep track of the minimum length substring that satisfies the condition. time: O(n^3), space: O(m) where m is the number of unique characters in t
# trick: use two pointers to maintain a sliding window, and a hashmap to count the characters in t and the characters in the current window. When the current window contains all characters in t, try to shrink the window from the left to find the minimum window.
# time: O(n), space: O(m) where m is the number of unique characters in t



class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or len(t)>len(s):
            return ""
        tmap={}
        smap={}
        ans,anslen=[-1,-1],float('inf')
        for c in t:
            tmap[c]=1+tmap.get(c,0)
        i,j=0,0
        have,need=0,len(tmap)
        l=0
        for r in range(len(s)):
            smap[s[r]]=1+smap.get(s[r],0)
            val=s[r]
            if val in tmap and smap[val]==tmap[val]:
                have+=1
            while have==need:
                if (r-l+1)<anslen:
                    ans=[l,r]
                    anslen=(r-l+1)
                smap[s[l]]-=1
                if s[l] in tmap and smap[s[l]]<tmap[s[l]]:
                    have-=1
                l+=1    
        return s[ans[0]:ans[1]+1]

