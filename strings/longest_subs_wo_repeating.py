class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st={}
        i,j=0,0
        ans=0
        while j<len(s):
            if s[j] not in st:
                st[s[j]]=j
            else:
                i=max(i,st[s[j]]+1)
                st[s[j]]=j
            ans=max(ans,j-i+1)
            j+=1  
        return ans        

# Time Complexity: O(N) where N is the length of the input string s. We have a single pass through the string to find the longest substring without repeating characters, which takes O(N) time.
# Space Complexity: O(min(M, N)) where M is the size of the character set  
# pattern: Hash Map, Sliding Window 