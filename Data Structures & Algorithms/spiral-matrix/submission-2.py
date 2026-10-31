class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l,t=0,0
        b,r=len(matrix)-1,len(matrix[0])-1
        res=[]

        while( l<=r and b>=t ):
            for i in range(l,r+1):
                res.append(matrix[t][i])
            t+=1
            if b<t:
                break
            for i in range(t,b+1):
                res.append(matrix[i][r])
            r-=1
            for i in range(r,l-1,-1):
                res.append(matrix[b][i])
            b-=1
            # print(res)
            if l>r:
                break
            for i in range(b,t-1,-1):
                res.append(matrix[i][l])
            l+=1
            # print(res)
        return res