'''
https://leetcode.com/problems/zigzag-conversion/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # if the numRows is equal to 1 then the entire string s will be placed onto
        # one single row. if the numRows is greater than the length of s then one letter
        # will be on each row. in both cases the output string will be the same as the original
        # input string.
        if numRows == 1 or numRows >= len(s):
            return s
        
        # each element in the result array is the string resulting from combining letters
        # from a row of the zigzag pattern.
        zigzagArr = [''] * numRows
        ind, step = 0, 1

        for char in s:
            # add the current character into the string that is placed at the 'ind' row
            # in the result array.
            zigzagArr[ind] += char
            # if the index reaches 0 then assign 1 to step so that the index can start moving
            # forward.
            if ind == 0:
                step = 1
            # if the index reaches the 'numRows-1' then assign step to -1 so that the index
            # can start moving backwards.
            elif ind == numRows-1:
                step = -1
            
            # add step to index. the index will oscillate between 0 and 'numRows-1'. the current
            # char will be added to the string at the current index and in this way the input string
            # will be converted into zigzag pattern.
            ind += step
        
        # join the strings in the result array into one string.
        return ''.join(zigzagArr)
