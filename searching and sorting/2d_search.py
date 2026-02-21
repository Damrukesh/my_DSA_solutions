class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l=0
        r=len(matrix[0])-1
        a=0
        b=len(matrix)-1
        while a<=b:
            mid2=(a+b)//2
            if target>matrix[mid2][r]:
                a=mid2+1
            elif target<matrix[mid2][0]:
                b=mid2-1
            else:
                break           
        while l<=r:
            mid1=(l+r)//2
            if matrix[mid2][mid1]==target:
                return True
            if target<matrix[mid2][mid1]:
                r=mid1-1
            else:
                l=mid1+1
        return False            

        