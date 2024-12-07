# Introduction to Array

## Problem: Find Pivot index

The 'leftsum' and 'rightsum' are assigned the values 0 and the sum of all elements. Then the array is iterated over and on each iteration the current element is subtracted from the 'rightsum', if the 'leftsum' and 'rightsum' are the same then the index of the current element is returned, and the current element is added to the 'leftsum'. As the array is iterated over the both the 'leftsum' and 'rightsum' are calculated together by adding and subtracting the current element and if at any point they become equal then the index is returned.

## Problem: Largest Number At Least Twice of Others

The largest no. and its index is stored at the beginning. The array is iterated over and if an element whose twice the value is larger than the largest no. exists and that element is not the same as the largest no. then -1 is returned because it means that the largest no. is not atleast twice as every other element in the array. If the array is iterated over and -1 is not returned then the largest no. index stored at the start is returned.

## Problem: Plus One

The array is iterated over and each element is multiplied by 10^(arrayLength-1-currentIndex) and it is added to 'number'. After the iteration the integer no. is stored inside 'number'. One is added to 'number' and it is converted to string. Another array is created by iterating over the string 'number', converting each character to integer and storing it in the empty array. This array contains the digits of the original number incremented by one and so it is returned.

# Introduction to 2D array

## Problem: Diagonal Traversal

An empty hashmap 'd' is created. In the 2D array the diagonal elements have the same (i+j) sum values. The hashmap 'd' will store arrays of diagonal elements from the original given 2D array with each (i+j) sum value as the key. The entire 2D array is iterated over and 'd' is populated. Then an empty array 'ans' is declared which will contain the returned answer. Each item in 'd' is iterated over and if the key of the current item is even then the diagonal array held by the key is reversed and its elements are added to 'ans'. If the key of current item is odd then the elements of the diagonal array held by the key of the current item are added to 'ans'. Finally 'ans' is returned.

## Problem: Spiral Matrix

An empty array 'res' is created which will hold the resulting answer. If the input 2D matrix is empty then the empty 'res' is returned. Four variables are created to represent the starting and ending of current row and current column. A loop is started with the condition that the startings of the current row and current column are less than equal to the endings of current row and columns. Inside this loop 4 seperate smaller loops are there to iterate over the 2D matrix in a clockwise spiral fashion and add elements to the 'res' array. After the end of each of the smaller 4 inner loops the values of current row or current columns ending or beginning is changed to ensure that the spiral pattern traversal is achieved. Finally the 'res' array is returned.

## Problem: Pascal's Triangle

An array 'pascal' is created which contains a pascal's triangle made of just 1s with 'numRows' no. of rows. The 'pascal' array is iterated over with 'i' and 'j' indexes and for each 'i' and 'j' values the 'pascal' elements from the level above ((i-1, j-1), (i-1, j)) are added together and placed inside of 'pascal' at (i, j) position. In this way the full pascal's triangle is created. Finally the 'pascal' triangle is returned.

# Introduction to Strings

## Problem: Add Binary

An empty string variable 'res' is created to hold the resulting answer. Another variable 'carry' is created to store carry values from bit addition. The two given strings are iterated from the end to the start. During each iteration the 'summ' variable is assigned any 'carry' values from the previous iteration. The integer value of current bit char is found by taking the ascii value of the current bit char and subtracting the ascii value of 0 from it. Bit char values from both strings are added to the 'summ' variable. If the 'summ' value after additions is more than 1 then 'carry' is set to 1 else 0 which is in accordance with bit addition. Then the modulus of 'summ' with 2 is converted to string and appended to 'res'. After the iteration is done 'carry' value is converted to string and also appended to 'res' if it is not 0. Finally 'res' string is inverted and returned.

## Problem: Implement Str()

The characters in the 'haystack' string are iterated over. The substring of 'haystack' starting from the current character and of length 'needle' string is checked against 'needle' string itself. If the 'needle' string and the substring match then the current char's index is returned because we've found the 'needle' string in the 'haystack' string. If the iteration completes without the 'needle' string being found then -1 is returned because this means that it is not present inside 'haystack'.

## Problem: Longest Common Prefix

First the string with the shortest length is found inside of given input array and stored inside 'shortest'. This is because the longest common prefix possible would be the shortest array. The 'shortest' string is iterated over, for each current char and its index from 'shortest' it is checked if current char is present in all of the strings from the input array at the same index. If at any point it is found that current char is not present in any of the strings from the input array then that would mean that there is no more common prefix present. At that point the longest common prefix would be the substring up until the current char's index and that substring is returned. If the iterations completed then that means the 'shortest' string is the LCP and it is returned.

# Two pointer Technique

## Problem: Reverse String

A helper function is defined that takes the left index, right index and the original string value. It then swaps the left and right index values and calls itself recursively with left index incremented by 1 and right index decremented by 1. The recursive calls continue until the left value becomes larger than or equal to the right value. The resulting string is completely reversed in place. The helper function is called later with 0 as the left value, 'len(s)-1' as the right value and the original input string value which gives us the desired result.

## Problem: Array Partition 1

In order to get the maximum sum of the minimum of pairs we sort the array in ascending order decrease the difference between elements. This way when we create pairs of elements and take the minimum of each pair we don't lose elements with a larger differences. The algorithm simply sorts the original input array, creates a subarray with only odd values and takes the sum of the subarray. This gives us our answer.

## Problem: Two Sum II - Input array is sorted

The two pointer technique is used where one pointer is placed at the array's end and another at the starting. The sum of elements at both pointers is calculated and if the sum matches with the target an array containing first pointer plus 1 and second pointer plus 1 is returned. Otherwise the beginning pointer is incremented if the sum is less than target or the end pointer is decremented by 1 if sum is greater than target.

## Problem: Remove Elements

A slow and a fast index is created. The fast index iterates over the entire array of integers and if the current element is not the same as the target value given then the current element at fast index gets assigned to the slow index position in the array and the slow index is incremented by 1. When the element at fast index matches the target value the assignment to slow pointer is not done which causes a gap to occur between the two indices. As a result at the end of the iteration the difference between the two indices will be the no. of elements that match the target value and all non matching elements will be placed at the front of the resulting array with the slow index at the end of the non matching elements. And so the slow index will also indicate the no. of elements that don't match the target value and it will be returned.

## Problem: Max Consecutive Ones

Two variables 'maxcount' and 'count' are initialised to 0. The array of integers is iterated over and the consecutive occurences of 1s is counted by incrementing 'count'. If a no. other than 1 is encountered then that means the chain of 1s is broken and the maximum between 'count' and 'maxcount' is stored in 'maxcount' and 'count' is reset to 0. This ensures that the longest consecutive occurence of 1s is always stored in 'maxcount'. At the end of the iteration the max between 'count' and 'maxcount' is returned.

## Problem: Minimum Size Subarray Sum

The sliding window approach is used using the left and right pointers. Initially both right and left pointers are set at 0, the 'currSum' variable which stores the sum of elements in the subarray contained between left and right pointers is set to 0, and the 'minLength' variable that stores the minimum length out of all subarrays that are greater than or equal to the given target value is set to 'len(nums)+1' because the no valid subarray will have a length greater than 'len(nums)+1'. The right pointer iterates over the elements of the array and the values are continuously added to the 'currSum'. As soon as 'currSum' becomes greater than or equal to 'target' as smaller iteration is started to find the valid subarray with minimum length. If the length of the current subarray is smaller than the previous 'minLength' then 'minLength' is updated with the new value as a new valid subarray with smaller length has been found. Then the length of the subarray is shortened by subtracting the left pointer element from 'currSum' and incrementing the left pointer. The smaller loop continues until the 'currSum' becomes smaller than 'target' and the subarray is no longer valid, then the iteration continues with the outer loop. When all iterations are done if a valid subarray with minimum length was found then 'minLength' is returned else 0 is returned.

# Conclusion

## Problem: Rotate Array

The length of the given array is calculated and stored in 'n'. Then the effective position of 'k' is calculated (in the case 'k' is larger than the length of the given array). The subarray from the (n-k) position to the end is calculated and the subarray from the beginning to the (n-k) position is calculated. The former subarray is concatenated with the latter to give the array with values shifted 'k' positions to the right.

## Problem: Pascal's Triangle 2

An array 'row' is created with 'rowIndex + 1' many zeroes to store the 'rowIndex'th row in the pascal's triangle and its first element is assigned the value 1. The elements of the array are iterated over from index 1 to the end and there is an inner iteration that goes from the current index back to index 1 for each outer iteration. During each inner iteration the current element is assigned the sum of itself and the previous element, doing so builds up the 'rowIndex'th row of the pascal's triangle. After the iteration the 'row' will be completed and returned.

## Problem: Reverse Words in a String

Take the original input string, remove any trailing and leading spaces using the 'strip()' function, split the string based on spaces between them into an array of words, reverse the array and join the words in the array with spaces between them. This gives us a string with the words reversed.

## Problem: Reverse Words in a String 3

Take the original input string, split the string into based on spaces between them into an array of words, iterate over the words in the array, reverse each word and store each it into the same place in the array and finally join the array of words into a sentence string with spaces between each word. This will the string with each word reversed with the same order as before.

## Problem: Remove Duplicates from Sorted Array

Two indices 'left' and 'right' are placed at index 1 of the input array. Both the indices move through the array but only the 'right' index moves ahead if the elements are being repeated. This and the fact that 'left' index is initialised to 1 ensures that when 'right' index element doesn't match element just before 'left' index the 'left' index will be pointing to the second element in a group of repeating elements. And so, the 'right' element can be assigned to the 'left' element and then the 'left' index can be incremented which ensures that the duplicated are removed with the original order of elements being preserved. After the iteration ends 'left' index will indicate the no. of unique elements in the original array from the starting and so it will be returned.

## Problem: Move Zeroes

Two pointers 'left' and 'right' are initialised at the start of the array. The 'right' pointer iterates over the input array. If the 'right' pointer element is not 0 then it is swapped with the 'left' pointer element and the 'left' pointer is incremented. This causes the 0 elements to gradually shift to the end of the array as the left pointer points to the end of the non zero array elements from the start of the array. Just like how larger elements bubble to the end of the array in bubble sort algorithm similarly here 0 elements bubble to the end of the array. Finally the array is returned after the end of the iteration with the non 0 elements at the start of the array.