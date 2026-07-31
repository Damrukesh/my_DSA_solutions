# Problem: Determine whether a string can be segmented into a sequence of dictionary words.
# Brute force: Try every partition of the string and check each segment, which is exponential.
# Solution approach: Use dynamic programming to mark reachable positions in the string.
# Time complexity: O(n * m * k) where m is number of words and k is average word length, Space complexity: O(n).class Solution:
def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    n=len(s)
    dp=[False]*(n+1)
    dp[n]=True
    while n>=1:
        for word in wordDict:
            if n-1+len(word)<len(s)+1 and s[n-1:n-1+len(word)]==word:
                dp[n-1]=dp[n-1+len(word)]
            if dp[n-1]:
                break
        n-=1
    return dp[0]
    
            



    