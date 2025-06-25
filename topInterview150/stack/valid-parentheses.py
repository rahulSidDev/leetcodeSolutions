'''
https://leetcode.com/problems/valid-parentheses/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isValid(self, s: str) -> bool:
        # dictionary to map each kind of opening bracket to its respective
        # closing bracket.
        bracketMap = {
            '(': ')', '{': '}', '[': ']'
        }

        # stack to store opening brackets.
        bracketStack = []
        
        for char in s:
            # current char is an opening bracket then add it to the stack.
            if char in bracketMap:
                bracketStack.append(char)
            # otherwise if current char is a closing bracket then perform these
            # steps
            else:
                # if the stack is empty then the that means the input string starts
                # with a closing bracket which cannot be valid so false is returned.
                if not bracketStack:
                    return False
                
                # take out the last opening bracket from the stack.
                lastBrac = bracketStack.pop()

                # get the corresponding closing bracket from the dict. if the last opening
                # bracket doesn't match with its closing bracket then a non-matching 
                # bracket pair has been found which makes the input string not valid, and
                # so false is returned.
                if bracketMap[lastBrac] != char:
                    return False
        
        # if the input string is valid then every opening bracket must be matched with
        # a closing one and the stack must be empty. if the stack is not empty after 
        # the iteration is done then the input string is not valid and false is returned.
        return not bracketStack
