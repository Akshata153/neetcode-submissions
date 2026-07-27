class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row=len(matrix)
        col=len(matrix[0])
        l=0
        r=row*col-1
        while l<=r:
            mid=(l+r)//2
            mid_val=matrix[mid//col][mid%col]
            if target==mid_val:
                return True
            elif target>mid_val:
                l=mid+1
            else :
                r=mid-1
        return False

