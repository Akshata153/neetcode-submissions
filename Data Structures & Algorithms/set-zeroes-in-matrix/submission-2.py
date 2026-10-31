class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zerocol=set()
        zerorow=set()

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    zerorow.add(i)
                    zerocol.add(j)

                
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in zerorow or j in zerocol:
                    matrix[i][j]=0
