# Problem: Rotate n x n matrix 90 degrees clockwise in-place
# Pattern: Transpose then Reverse - Matrix transformation technique
# Brute Force: Create new matrix and copy rotated elements - O(n^2) space
# Method: (1) Reverse rows (top-bottom swap) (2) Transpose matrix (swap elements)
# Time: O(n^2), Space: O(1)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        t=0
        b=len(matrix)-1
        while t<=b:
            matrix[t],matrix[b]=matrix[b],matrix[t]
            t+=1
            b-=1
        n=len(matrix)
        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]