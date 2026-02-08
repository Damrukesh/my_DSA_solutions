class Solution:
    def longestPalindrome(self, s: str) -> str:
        anso=""
        anse=""
        #odd centre
        for i in range(len(s)):
            a,b=i,i+1
            while a>=0 and b<len(s):
                if s[a]==s[b]:
                    if (b-a+1)>len(anso):
                        anso=s[a:b+1]
                    a-=1
                    b+=1
                else:
                    break
        for i in range(len(s)):
            c,d=i,i
            while c>=0 and d<len(s):
                if s[c]==s[d]:
                    if (d-c+1)>len(anse):
                        anse=s[c:d+1]
                    c-=1
                    d+=1
                else:
                    break

        if len(anso)>len(anse):
            return anso
        else:
            return anse                    

# Time: O(N^2) where N is the length of the input string s. We have two nested loops, and in the worst case, we may need to check all possible substrings of s, which takes O(N^2) time.
# Space: O(1) if we don't consider the space used to store the output string. We are using a constant amount of extra space to store the longest palindromic substring found so far (anso and anse). The space complexity is O(1) because we are not using any additional data structures that grow with the input size.
# pattern: Two Pointers, Expand Around Center

            