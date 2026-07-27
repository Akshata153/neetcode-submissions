class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROW=len(matrix)
        COL=len(matrix[0])
        #l,r => (1D matrix) boundary
        #row,col => 2D 
        l,r=0,(ROW*COL)-1
        while l<=r:
            mid=(l+r)//2 #10
            #1d to 2d
            row,col=mid//COL,mid%COL #2 2
            # print(f"{l} {mid} {r}")
            # print(matrix[row][col])
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:
                r=mid-1
            else:
                l=mid+1
        return False


