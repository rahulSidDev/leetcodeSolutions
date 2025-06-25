'''
https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def simplifyPath(self, path: str) -> str:
        # stack to store the dir names in the input path
        stack = []
        # result list to store the newly formed canonical path
        result = []
        # split the input unix path into a list of directories in the path.
        p = path.split('/')

        for curr in p:
            # if the current dir from p is '..' then go one dir level above by popping 
            # the last element from the stack since '..' in unix filepath means parent dir.
            if stack and curr == '..':
                stack.pop()
            # otherwise if the current dir is not an empty string and not '.' and not '..'
            # then add it to the stack.
            elif curr != '' and curr != '.' and curr != '..':
                stack.append(curr)
        
        # if the stack is empty after adding dir names to stack and doing some path traversal
        # then return the path to the root dir.
        if not stack:
            return '/'

        # iterate over the dir names in stack and append each to the result list with '/'
        # in between each dir name.
        for ele in stack:
            result.append('/')
            result.append(ele)
        
        # join each element in stack into one string and return it.
        return ''.join(result)
