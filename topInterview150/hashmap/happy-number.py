'''
https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def isHappy(self, n: int) -> bool:
        # set to store intermediate values when finding the happy no.
        mem = set()
        
        # iterate until n becomes 1.
        while n != 1:
            # store n into a temporary variable.
            tempN = n
            # create an empty list to store all the digits of current n value.
            digitArr = []

            # iterate until no digits are left in tempN.
            while tempN != 0:
                # extract the rightmost digit of tempN and append it to the digitArr list.
                # update tempN with the value that doesn't have the rightmost digit.
                digitArr.append(tempN % 10)
                tempN = tempN // 10
            
            # square each digit value from the digit list and sum them all. assign this sum
            # value to n.
            n = sum(digit ** 2 for digit in digitArr)

            # if the new n value is found to be inside the set then that means the intermediate
            # values are looping and continuously repeating the process will not result in reaching 1.
            # and so the input no. is not a happy no. and false is returned.
            if n in mem:
                return False
            # otherwise add the current intermediate value of 'n' into the set.
            else:
                mem.add(n)
        
        # if the iteration ends then that means 1 was reached finally and the input no. is indeed
        # a happy no. and so true is returned.
        return True
