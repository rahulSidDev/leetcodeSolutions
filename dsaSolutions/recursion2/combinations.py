'''
Given two integers 'n' and 'k', return all possible combinations of 'k' numbers chosen from the range '[1, n]'.
You may return the answer in any order.
'''
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        sol = []
        def backtrack(remain, comb, nextint):
            if remain == 0:
                sol.append(comb.copy())
            else:
                for i in range(nextint, n+1):
                    comb.append(i)
                    backtrack(remain-1, comb, i+1)
                    comb.pop()
        
        backtrack(k, [], 1)
        return sol