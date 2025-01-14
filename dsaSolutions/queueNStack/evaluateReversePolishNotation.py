'''
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1394/
'''
class Solution:
    def performOperation(self, firstNum, secondNum, operation):
        if operation == '+':
            return secondNum + firstNum
        if operation == '-':
            return secondNum - firstNum
        if operation == '*':
            return secondNum * firstNum
        if operation == '/':
            return int(secondNum / firstNum)
    
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = ['+', '-', '*', '/']
        
        for token in tokens:
            if token not in operations:
                stack.append(token)
            else:
                firstNum, secondNum = stack.pop(), stack.pop()
                result = self.performOperation(int(firstNum), int(secondNum), token)
                stack.append(str(result))

        return int(stack.pop())