class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sh={}
        th={}
        for i in range(len(s)):
            a,b=s[i],t[i]
            if (a in sh and sh[a]!=b) or (b in th and th[b]!=a):
                return False
            sh[a]=b
            th[b]=a
        return True    