class Solution:
    def tribonacci(self, n: int) -> int:
        self.res={0:0,1:1,2:1}

        def func(x):
            if x in self.res:
                return self.res[x]
            
            # print(f"{x} {res}")
            self.res[x]=func(x-1)+func(x-2)+func(x-3)
            return self.res[x]
        # func(n)
        return func(n)