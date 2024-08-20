"""
The Fibonacci numbers, commonly denoted 'F(n)' form a sequence, called the Fibonacci 
sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1.
That is:
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given 'n', calculate 'F(n)'.
"""
class Solution:
    def fib(self, n: int) -> int:
        cache = {}
        
        def recur(N):
            if N in cache:
                return cache[N]
            
            if N < 2:
                result = N
            else:
                result = recur(N-1) + recur(N-2)
            
            cache[N] = result
            return result
        
        return recur(n)