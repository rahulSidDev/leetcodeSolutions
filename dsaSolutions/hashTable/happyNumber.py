'''
https://leetcode.com/explore/learn/card/hash-table/183/combination-with-other-algorithms/1131/
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        
        while n != 1:
            tempN = n
            digitArr = []
            while tempN != 0:
                digitArr.append(tempN % 10)
                tempN = tempN // 10
            
            n = sum(digit ** 2 for digit in digitArr)
            if n in mem:
                return False
            else:
                mem.add(n)
        
        return True