'''
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def performOperation(self, firstNum, secondNum, operation):
        # match the input operation and perform said operation on first and second input
        # num. then return the result of the operation.
        if operation == '+':
            return secondNum + firstNum
        if operation == '-':
            return secondNum - firstNum
        if operation == '*':
            return secondNum * firstNum
        if operation == '/':
            return int(secondNum / firstNum)
    
    def evalRPN(self, tokens: List[str]) -> int:
        # stack to store the tokens and the result of operations.
        stack = []
        operations = ['+', '-', '*', '/']
        
        for token in tokens:
            # if current token is not an operation token then add it to the stack.
            if token not in operations:
                stack.append(token)
            # otherwise pop the last two nums from the stack, pass both and the operation 
            # token to the 'performOperation' function, get the result of operation and 
            # append the result num to the stack.
            else:
                firstNum, secondNum = stack.pop(), stack.pop()
                result = self.performOperation(int(firstNum), int(secondNum), token)
                stack.append(str(result))

        # after the tokens are iterated over there will be just one element in the stack
        # which will be the final answer.
        return int(stack.pop())
