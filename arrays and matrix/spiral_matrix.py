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
# Time: O(MN) where M is the number of rows and N is the number of columns in the input matrix. We have a single pass through all the elements of the matrix to add them to the ans list, which takes O(MN) time.
# Space: O(MN) in the worst case, where all elements of the matrix are
#pattern: Simulation, Matrix         
