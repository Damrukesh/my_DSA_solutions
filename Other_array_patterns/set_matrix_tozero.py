# Problem: Set entire row and column to 0 if element is 0, modify in-place
# Pattern: Use first row/column as markers - Handle edge case with extra variable
# Brute Force: Store zeros positions, then set to 0 - O(m*n) space
# Method: Use matrix[0][j] and matrix[i][0] as markers, track first row separately
# Time: O(m*n), Space: O(1)

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        c=len(matrix[0])
        r=len(matrix)
        extra=5
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    if i==0:
                        extra=0
                    else:
                        matrix[i][0]=0
                    matrix[0][j]=0    
        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
                    
        if matrix[0][0]==0:
            for i in range(r):
                matrix[i][0]=0       

        if extra==0:
            for i in range(c):
                matrix[0][i]=0