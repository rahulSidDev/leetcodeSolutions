'''
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
'''
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempStack = []
        answer = [0] * len(temperatures)
        
        for i, temperature in enumerate(temperatures):
            while tempStack and temperatures[tempStack[-1]] < temperature:
                index = tempStack.pop()
                answer[index] = i - index
            
            tempStack.append(i)
        
        return answer