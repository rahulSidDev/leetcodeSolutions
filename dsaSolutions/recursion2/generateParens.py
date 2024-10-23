'''
Given 'n' pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def helper(left, right, ans, string):
            if right < left:
                return
            if not left and not right:
                ans.append(string)
                return
            if left:
                helper(left-1, right, ans, string+'(')
            if right:
                helper(left, right-1, ans, string+')')
        
        if not n:
            return
        
        left, right, ans = n, n, []
        helper(left, right, ans, "")
        return ans