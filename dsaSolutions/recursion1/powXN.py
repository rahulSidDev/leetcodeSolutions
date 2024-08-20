"""Implement pow(x, n), which calculates 'x' raised to the power 'n' (i.e., x^n)."""
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        if n % 2: # if n is an odd number.
            return x * self.myPow(x, n-1)
        
        return self.myPow(x*x, n/2)
