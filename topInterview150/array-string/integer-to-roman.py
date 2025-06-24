'''
https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150
'''
class Solution:
    def intToRoman(self, num: int) -> str:
        decToRoman = {
            1000: 'M',
            500: 'D',
            100: 'C',
            50: 'L',
            10: 'X',
            5: 'V',
            1: 'I'
        }

        decExceptions = {
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }

        allDigits = list(str(num))
        romanNo = ''
        for i in range(len(allDigits)):
            intDigit = int(allDigits[i])
            if intDigit == 4 or intDigit == 9:
                romanNo += decExceptions[intDigit * 10 ** (len(allDigits)-1-i)]
            elif intDigit >= 5:
                romanNo += decToRoman[5 * 10 ** (len(allDigits)-1-i)]
                intDigit -= 5
                romanNo += decToRoman[1 * 10 ** (len(allDigits)-1-i)] * intDigit
            else:
                romanNo += decToRoman[1 * 10 ** (len(allDigits)-1-i)] * intDigit
        
        return romanNo
