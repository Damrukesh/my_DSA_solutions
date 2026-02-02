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

#problem statement:rotate the matrix by 90 degree clockwise
#pattern : transpose and reverse #time complexity : O(n*n)