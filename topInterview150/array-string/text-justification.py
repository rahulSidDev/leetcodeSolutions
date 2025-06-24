'''
https://leetcode.com/problems/text-justification/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # result array stores the final output
        result = []
        # current array stores words that are traversed but no yet added to result
        currList = []
        # stores the no. of letters in the current array
        noLetters = 0

        for w in words:
            # if the sum of total letters in current list, the length of current word, 
            # and the length of the current list (minimum no. of spaces between words) is 
            # greater than maxWidth then perform the following steps.
            if noLetters + len(w) + len(currList) > maxWidth:
                # size will be used for adding spaces to all words in currList in a round 
                # robin fashion. max function is used for the occasion where 'len(currList)-1' 
                # could be 0.
                size = max(1, len(currList) - 1)

                for i in range(maxWidth - noLetters):
                    # add space to each word in round robin fashion
                    index = i % size
                    currList[index] += ' '
                
                # add current line of words to the output
                result.append(''.join(currList))
                currList, noLetters = [], 0

            # add current line of words to the output.
            currList.append(w)
            # add the length of current word added to the total length.
            noLetters += len(w)
        
        # add the words of the last line with space in between each into one sentence. then
        # left adjust the last sentence by adding spaces to its left side until the characters
        # are equal to maxWidth. finally append it to the result array.
        result.append(' '.join(currList).ljust(maxWidth))
        return result
