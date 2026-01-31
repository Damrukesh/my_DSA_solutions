class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        c=len(matrix[0])
        r=len(matrix)
        columns=[0]*c
        rows=[0]*r
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    columns[j]=1
                    rows[i]=1
        for i in range(r):
            if rows[i]==1:
                for j in range(c):
                    matrix[i][j]=0
        for j in range(c):
            if columns[j]==1:
                for i in range(r):
                    matrix[i][j]=0          
                
#problem statement:set matrix zeroes if any element is zero in that row or column
#pattern : two arrays to track rows and columns #time complexity : O(m*n)