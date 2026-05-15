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
# The algorithm uses a sliding window approach to find the longest substring without repeating characters. We maintain a hash map to store the last index of each character in the current window. We iterate through the string with two pointers, i and j, where j is the end of the current window and i is the start. If we encounter a character that is already in the hash map, we move the start pointer i to the right of the last index of that character to ensure that there are no repeating characters in the current window. We update our answer with the length of the current window at each step and return it at the end.