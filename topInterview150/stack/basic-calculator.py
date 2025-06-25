'''
https://leetcode.com/problems/basic-calculator/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def calculate(self, s: str) -> int:
        # used to store the result of operations in the expression
        result = 0
        # used to store the current no. for calculation while iterating through the expression
        currNum = 0
        # used to store which sign is being dealt with. only has values -1 and 1 representing '-'
        # and '+' respectively.
        sign = 1
        # stack to store the results and retreive them while handling brackets in the expression.
        stack = []

        for token in s:
            # if the current token is a digit then update the current num var. 
            if token.isdigit():
                # current num is multiplied by 10 to handle no.s which have more than 1 digit.
                currNum = currNum * 10 + int(token)
            # if token is a sign add the current no. to the result
            elif token in ['-', '+']:
                # the current no. is added with the sign before the current one attached to it.
                result += sign * currNum
                # assign current no. the value of 0 after adding it to result to handle further no.s 
                # in the expression.
                currNum = 0
                # update the sign to -1 or 1 depending on the current sign token so that the next time
                # a sign occurs this sign can be used to add current num to result. in python true and false
                # values can be represent by 1 and 0 respectively.
                sign = [-1, 1][token == '+']
            # if the current token is an opening bracket then add the current result and sign to the stack
            # and initialise sign and result vars to 1 and 0.
            elif token == '(':
                stack.append(result)
                stack.append(sign)
                sign, result = 1, 0
            # if the current token is a closing bracket ...
            elif token == ')':
                # append the current no. inside the brackets with the right sign to the current result
                # inside the brackets.
                result += sign * currNum
                # get the sign outside of the brackets from the stack and multiply it to the result from
                # inside the bracket so that result has the right sign.
                result *= stack.pop()
                # get the result from outside the bracket and add it to the result from inside the bracket.
                result += stack.pop()
                # make the current num 0 to handle no.s after the bracket.
                currNum = 0
    
        # add the final no. with the last sign in the expression to the result and return it.
        return result + sign * currNum
