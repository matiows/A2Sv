class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.myPow(x, -1* n)
        if n%2 == 0:
            ans = self.myPow(x, n//2)
            return ans * ans
        else:
            return x * self.myPow(x, n-1)
        
        