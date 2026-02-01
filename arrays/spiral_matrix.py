class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        l=0
        r=len(matrix[0])-1
        t=0
        b=len(matrix)-1
        while l<=r and t<=b: 
            for i in range(l,r+1):
                ans.append(matrix[t][i])
            t+=1    
            for i in range(t,b+1):
                ans.append(matrix[i][r])
            r-=1   
            if not(l<=r and t<=b):
                break  
            for i in range(r,l-1,-1):
                ans.append(matrix[b][i])
            b-=1    
            for i in range(b,t-1,-1):
                ans.append(matrix[i][l])
            l+=1    

    
        return ans      
