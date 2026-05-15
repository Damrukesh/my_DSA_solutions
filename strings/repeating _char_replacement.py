class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i=0
        maxi=0
        ans=0
        count={}
        for j in range(len(s)):
            count[s[j]]=count.get(s[j],0)+1
            maxi=max(maxi, count[s[j]])

            if (j-i+1)-maxi<=k:
                ans=max(ans,j-i+1)
            else:
                count[s[i]]-=1
                i+=1
        return ans
    
# Time Complexity: O(N) where N is the length of the input string s. We have a single pass through the string to find the longest substring, which takes O(N) time.
# Space Complexity: O(M) where M is the size of the character set. We are using a hash map to store the frequency of characters in the current window, which takes O(M) space.
#pattern: Hash Map, Sliding Window
# The algorithm uses a sliding window approach to find the longest substring that can be formed by replacing at most k characters. We maintain a count of characters in the current window and keep track of the maximum frequency of any character in that window. If the length of the current window minus the maximum frequency is less than or equal to k, we can update our answer with the length of the current window. Otherwise, we shrink the window from the left until it satisfies the condition again.