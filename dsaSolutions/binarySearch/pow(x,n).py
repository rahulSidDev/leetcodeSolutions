'''
https://leetcode.com/explore/learn/card/binary-search/137/conclusion/982/
'''
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # if n is 0 then the answer will always be 1 since anything raised to the power 0 is 1.
        if n == 0:
            return 1
        
        # if n is less than 0 then the function is called again with negative n (which will make the negative n positive)
        # and the returned value is set as 1 / returnvalue.
        if n < 0:
            return 1 / self.myPow(x, -n)
        
        # if n is odd then on x is taken out and the function calls itself with n-1
        if n % 2:
            return x * self.myPow(x, n-1)
        
        # if n is even then the search space of n is halved by calling the function again by passing in x * x.
        return self.myPow(x*x, n/2)