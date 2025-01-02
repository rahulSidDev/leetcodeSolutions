# Design a Hash table

## The principle of hash table

Hash table is a data structure which uses hash functions to order data in a way that makes reading and inserting data very quick. When a value is to be inserted into the hash table it is passed through a hashing function to get an index. This index points to the bucket where the value will be stored. Similarly when a value is to be searched in the hash table the value is again passed into a hashing function to get the bucket index that will point us to the bucket where the value is stored. A simple hash function is `y = x % 5` where `x` is the key and `y` will be the bucket index value. If we want to store value `1987` then it is passed through the hash function `y = x % 5` to get the index value `2` and so it is stored inside bucket `2`. When searching for `1987` again it is passed into the hashing function to get the value `2` and so bucket `2` is searched where `1987` is found.

The hash function is the most important part of a hash table. It depends on the range of key values and the number of buckets. A perfectly designed hash function will ensure that the keys are assigned uniformally to the buckets and that there is a one to one correlation between the key and the buckets. Unfortunately in most cases the hash function will not be perfect and there will be hash collisions present.

A hash collision occurs when two or more keys are assigned to the same bucket. A collision resolution algorithm should tackle the following questions:

1. How to organise the keys in the same bucket?
2. What if too many values are assigned to the same bucket?
3. How to search for a target value in a specific bucket?

## Problem: Design hash set

The buckets are stored inside of a 2D array where each bucket is a 1D array. The number of buckets in the 2D array is set to `10000`. The adding function takes the key and passes it through the hash function: `key % bucketsize` which has been arbitrarily chosen. The hash function will return the bucket index which will be used to find the bucket from the 2D array. The bucket is then searched for the key value to be inserted. If it is already there then the key is not added otherwise it is. For the remove function again the key is passed into the hash function to get the bucket index. The bucket is searched for the key to be removed and if found it is removed. The contain function follows similar logic where the bucket index is found and used to get the bucket array. If the bucket array has the key value then true is returned otherwise false is returned.

## Problem: Design Hash Map

The size of the hashmap is defined, then the 'mult' value is defined, and finally the hashmap data array is defined. The size of the hashmap array is chosen to be atleast the no. of entries that will be made, unfortunately there will always be the possibility of hash collisions existing. To counter collisions each entry of the hashmap array is made a linked list, where each node stores the key-value pair, and which acts as a stack where the latest element inserted is at the head. Navigating linked lists will drop down the look up time from `O(1)`, to counter this a good hash function is required that will convert each key to a unique index. Thus the hashmap trades space complexity for time complexity where the hashmap array is quite big but the searching and inserting operations take constant time depending on the quality of the hash function chosen. The hash function chosen in this problem is a 'simple multiplicative' hashing function and this function is passed the key value to retrieve the hashmap index value. 

## Complexity Analysis - Hash Table

The space complexity of the hash table DS is `O(M)` where `M` is the number of entries in the table. The time complexity will be `O(1)` if a proper hash function is chosen that maps each key value to one hash index (strict one-to-one relation) to access one bucket in the hash table. Each bucket in the table will likely be an array to store multiple values as hash collisions are always possible. If a poor hash function is chosen then it could bring down the time complexity to `O(N)` where `N` is the size of the maximum bucket array. If there are too many values inside a bucket then a height balanced binary search tree can be utilised for each bucket instead which will further bring down the worst case time complexity to `O(logN)`.

# Practical Application - Hash Set

'Hash Set' is an implementation of the 'Set' data structure and it only stores unique values, no repeated ones. Hashsets are commonly used to solve problems with duplicated values present.

Python Hash Set implementation:

```
# 1. initialize the hash set
hashset = set() 

# 2. add a new key
hashset.add(3)
hashset.add(2)
hashset.add(1)
hashset.add(1)

# 3. remove a key
hashset.remove(2)

# 4. check if the key is in the hash set
if (2 not in hashset):
    print("Key 2 is not in the hash set.")

# 5. get the size of the hash set
print("Size of hashset is:", len(hashset))

# 6. iterate the hash set
for x in hashset:
    print(x, end=" ")
print("are in the hash set.")

# 7. clear the hash set
hashset.clear()
print("Size of hashset:", len(hashset))
```

## Problem: Contains Duplicate

A hashset is defined and the elements of the array are iterated over. Each element is added to the hashset if it is not already present in the set, if any element is found to be present in the hashset then `true` is returned since a duplicate value exists inside of the array. If all the elements are successfully entered into the hashset then `false` is returned since no element was repeated in the array.

## Problem: Single Number

The given array is iterated over and for each element we add it to a hashset if it is not present there else we remove it if it is already there. Since all elements appear twice in the array except for one, after the iteration of all elements only the non repeated element which we are looking for will be left in the hashset. This element is popped from the hashset and returned as answer.

## Problem: Intersection of two Arrays

Two hashsets are created for both the input arrays and the two arrays are iterated over seperately. During each arrays iteration the elements are added to their respective hashset. After the iteration of both arrays the two hashsets contain the unique elements of both arrays. Taking the intersection of both hashsets gives the common unique elements in both the arrays and iterating over the intersection hashset and appending each element into a new array results in the desired array result.

## Problem: Happy Number

A hashset is defined that will store all sum of squares. If the during the iteration it is found that any sum of squares is already in the hashset then that would mean that sum of square values are being repeated and the input integer is not a happy number. Then iteration is done until sum of sqaures turns out to be one. In each iteration the previous sum of squares' digits are seperated and put in a list, the new sum of squares is calculated, if its not inside the hashset then it is added there otherwise false is returned. In the iteration only two possible outcomes will occur, either the sum of sqaures becomes one which confirms that the original input integer is 'happy' in which case 'true' is returned after the iteration, or the sum of squares value is found present inside the hashset which proves that the sum of square values are going in a loop and the original input integer is not a 'happy' no. in which case 'false' is returned immediately.

# Practical Application - Hash Map

A 'Hash Map' is an implementation of the 'Map' data structure which is specifically used for storing `(key, value)` pairs.

Implementation of the Hash Map in Python:

```
# 1. initialize a hash map
hashmap = {0 : 0, 2 : 3}

# 2. insert a new (key, value) pair or update the value of existed key
hashmap[1] = 1
hashmap[1] = 2

# 3. get the value of a key
print("The value of key 1 is: " + str(hashmap[1]))

# 4. delete a key
del hashmap[2]

# 5. check if a key is in the hash map
if 2 not in hashmap:
    print("Key 2 is not in the hash map.")

# 6. both key and value can have different type in a hash map
hashmap["pi"] = 3.1415

# 7. get the size of the hash map
print("The size of hash map is: " + str(len(hashmap)))

# 8. iterate the hash map
for key in hashmap:
    print("(" + str(key) + "," + str(hashmap[key]) + ")", end=" ")
print("are in the hash map.")

# 9. get all keys in hash map
print(hashmap.keys())

# 10. clear the hash map
hashmap.clear()
print("The size of hash map is: " + str(len(hashmap)))
```

## Scenario I - Provide More Information

A Hash Map is used in situations where more information storing is desired. For e.g. in the problem: "Given an array of integers, return indices of the two numbers such that they add up to a specific target." using a Hash Set would have been sufficient to find if two no.s adding to the desired target exist or not. But since it is required to return the indices we need to use Hash Map to store the index and array element as key-value pairs. More information was needed to be stored so Hash Map was used. Sometimes more information is needed to return and sometimes more information is needed to help make better descisions in our algorithm, in both cases Hash Map is used.

## Problem: Two Sum

Each element in the input array has its partner element which can be calculated by subtracting the element itself from the target value. The partner values calculated for each element is stored inside of a hash map during the iteration of the input array. If during the iteration the current element is found to match one of the partner values in the hash map then that means a pair of elements that add up to the target has been found. The current element and the previous element whose partner element matched with the current element would make up the pair that sum to the target value. Their indices are put in an array and returned.

## Problem: Isomorphic String

Two strings are considered isomorphic if string 'A' can be turned into string 'B' and vice versa by changing the existing characters in place. For this two maps are created to store the character mappings to convert 'A' to 'B' and vice versa in the form of key-value pairs. The string elements are iterated over (they are of equal length) and during each iteration each char of both strings is checked whether it is present in the maps. If the current char of one string is present and it is mapped to some char other than the current char of the other string then that means that one character is being mapped to two chars which makes the two input string not isometric and so 'false' is returned. The mapping of current chars from string 'A' and string 'B' is added to the first map and the vice versa is added to the second map as the iteration goes on. If the iteration completes then that means that there were no incorrect mappings between 'A' and 'B' and the two strings isometric and so 'true' value is returned.

## Problem: Minimum Index Sum of Two Lists

The first array is iterated over and the strings are stored inside of the hashmap as keys with the strings' indices as the values. This is done in order to check whether each string from 'list2' appears inside 'list1' or not in `O(1)` time. While iterating through 'list2' if a string appears inside 'list1' then the string is added to the second hashmap as a key with the sum of its indices in 'list1' and 'list2' as the value. After the iteration of 'list2' the second hashmap will contain strings that are common in both arrays with their sum of indices in both arrays stored as values in the second hashmap. Then the second hashmap is iterated over and the strings that have the lowest sum of indices are extracted into a seperate array. This array forms our answer and it is returned.

## Scenario II - Aggregate by Key

Another way to use hashmaps is by aggregating all information by key. For e.g. take this problem: "Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.". To solve this problem we can use a hash map where each character of the string is the key and the value corresponding to each key is the count of the character. Then the hashmap can be searched to find the first non recurring character. The key to solving these kinds of problems is to decide your strategy when you encounter an existing key.

## Problem: First Unique Character in a String

The string is iterated over and each character during the iteration is checked to be inside of the hashmap. If the character is not there in the hashmap then it is added as a key with '1' as the corresponding value since this is the first occurence of this character. If it is there then the count of the character already there is incremented since the character is occuring for the second time. The hashmap is then iterated over and the index of the first character whose occurence turns out to be '1' is returned. If no character with '1' occurence is found in the iteration then '-1' is returned.

## Problem: Intersection of Two Arrays II

The first string is iterated over and the occurence of each no. is stored in the hash map. Then the second array is iterated over and if the no. is present in the hash set then that means the no. is common in both arrays. In that case the no. is appended to a seperate array, the occurence of the no. is decremented by 1 because each common no. must appear as many times as it shows in both arrays, and if the occurence of current no. drops to 0 in the hash map then it is deleted from the hash map. After the iteration the seperated array will have all the common no.s from both arrays and it is returned.

## Problem: Contains Duplicate II

The array is iterated over and each element is checked to be in the hashmap. If it is not there then it is added to the hashmap as a key and its index as the value, if it is there then that means the element is repeating in the array and the first condition of 'nums[i] == nums[j]' is true. After the first condition is found to be true the second condition of 'abs(i - j) <= k' is checked. If the second condition is also true then that means that we've found two indices 'i' and 'j' that fulfill both conditions and so 'True' is returned. If the second condition check fails then the value of the element in the hashmap is updated with the new index. If the iteration ends without reaching the return statement then there are no distinct indices in the array and 'False' is returned.

# Practical Application - Design the key

In the previous problems, the choice of key is comparatively straightforward. Unfortunately, sometimes you have to think it over to design a suitable key when using a hash table. For e.g. take the following problem: "Given an array of strings, group anagrams together". For this problem we cannot use the strings directly as keys and we need to find a way to design keys that represent the types of anagrams.

Designing a key by yourself involves using creating a mapping function that takes the original information and maps it to the actual keys that are to be used inside of the hashmap. When designing a key the following two points need to be guaranteed:

1. All values belonging to the same group will be mapped to the same group.
2. Values that don't belong to the same group will not be mapped to the same group.

The mapping function needs to fulfill these two conditions, however the hash function doesn't need to fulfill the second condition, this is the main difference between the mapping function and a hash function.

## Problem: Group Anagrams

Each string in the input array is iterated over and sorted based on each characters ascii value. This sorted string becomes the custom key to store the anagram types. Since anagram strings contain the same characters sorting them turns into the same string which can be used to map all of them into one group in the hashmap. This is exactly what is done in the algorithm, the sorted strings are keys in the hashmap that map to arrays containing the strings corresponding to the anagram group. Then the hashmap is iterated over and the arrays of each anagram group is appended to another empty array to build the desired answer and return it.

## Problem: Valid Sudoku

A hash map is initialised with keys corresponding to all rows, all columns, and every mini box and every key maps to an empty array. This hash map is used to map the occurence of each non empty value from the board in the row, column and the mini-square that the value occurs in. If it is found that the value is already present in the row, columns, or the mini-square it is located in then that means the rules of sudoku validity is broken and the input board is not a valid sudoku and so 'False' is returned. If the iteration completes without any repeating occurences of values happening then that means the board is a valid sudoku and 'True' is returned.

## Problem: Find Duplicate Subtrees

A recursive function is defined that traverses the binary tree depth-first or in pre-order. As the tree is traversed downwards a string is constructed that contains the value of the current node followed by the nodes left of it and then the nodes right of it and this string is called 'path'. For 'null' nodes char '#' is used to denote it. The 'path' string is the representation of the subtrees present in the overall tree and it is used as keys in the hashmap to store the occurences of each subtree. After the recursion reaches the leaf nodes the 'path' string is checked if it is inside of the hashmap or not, if it is then its count is incremented by 1 otherwise the 'path' string is added to the hasmap with count 1. If the count of 'path' is found to be 2 then that means the subtree represented by 'path' is duplicated in the tree. In that case the current node in the recursion which is also the parent node of the duplicate subtree is added to a seperate array. After the recursive array completes execution the 'res' array will have all the duplicate stubtrees' parent nodes which will be the final answer.

## Design the Key - Summary

Here are some pointers on how to design the key:

1. When the order of each element in the string/array doesn't matter then the sorted array/string can be used as the key.
2. If the offset of each element is what matters then the offset from the first element can be used as the key.
3. In a binary tree using serialization of the subtree is better to use as keys than using the treenode directly.
4. In a matrix the row index or the column index is better to use as the key.
5. In a the rows and column indices can be combined to identify which block the element belongs to ((i, j) -> (i/3) * 3 + (j/3)).
6. Sometimes in a matrix aggregating the diagonal lines is better to use for keys. (i+j for anti-diag and i-j for diag).

# Conclusion

## Problem: Jewels and Stones

An empty hash map is created to store every element that occurs in the 'jewels' array as keys mapping to the value of 0. Then the elements of 'stones' array are iterated over and each element that occurs in the hashmap as a key, i.e. each stone that is also a jewel, has the value mapped to it incremented by 1. After the iteration is complete the hash map will have the count of each stone that is also a jewel. The hash map keys are iterated over and all the count values are added up to get a total value and that total value is then returned.

## Problem: Longest Substring Without Repeating Characters

First the edge case of the length of the input string being 1 is handled, if the length is 1 then the longest substring will be of length 1 and so 1 is returned. Using nested loops all substrings are considered. The substrings considered go starting from the current character all the way to the end of the string. At the start of every new substring starting from a new current char an empty set is defined to store all the unique chars appearing in the substring. As the substring grows from the current char to the end of the string each new char is added to the set if it is not already in there and the 'maxcount' value is updated if the length of the current substring exceeds the current 'maxcount' value. If the new char is already in the set then that means that duplicate chars are present in the substring and the current substring can no longer be counted and so the loop is broken to start counting the next substring. After the iteration is done all the valid substrings will have been counted and the 'maxcount' value will have the length of the longest substring and it will be returned.

## Problem: 4Sum II

An empty hash map is defined to store the occurences of the sum of two array elements each from the first two arrays. A variable 'tupleCount' is defined to store the no. of valid indice tuples. Using two nested loops every possible pair of elements from the first two arrays is considered and the occurences of every pair's sum is added to the hashmap. Then again a double nested loop is used to traverse every possible pair of elements in the third and fourth input arrays. For each pair of array elements we check if `0 - nums3[k] - num4[l]` is present in the hashmap or not, if it does then the 'tupleCount' variable is incremented by the no. of occurences of `0 - nums3[k] - num4[l]` from the hash map. The logic of this code works because the condition `nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0` can be manipulated to form the new condition `nums1[i] + nums2[j] == 0 - nums3[k] + nums4[l]`. The problem of finding indices from the 4 arrays is divided into two parts where the `nums1[i] + nums2[j]` values are recorded in the hashmap in the first part and in the second part `0 - nums3[k] + nums4[l]` values are searched in the hashmap and their occurences are added. Finally the 'tupleCount' variable will have the total count and it is returned.

## Problem: Top K frequent Elements

The input array is iterated over and the occurences of each element is recorded in the first hash map. The keys in the first hash map are iterated over and each key's (array element) occurence value is stored as a key in the second hashmap with the list of keys from the first array as the values in the second hashmap. Also as the occurence of keys from the first hashmap are added as keys in the second hashmap the occurence values are also appended to the 'allKeys' array. After the iteration the second hashmap will have the occurence values mapped to arrays of elements that occured that many times. The 'allKeys' array is sorted backwards and it is iterated over. All of the elements from the highest occurences are added to the result array. Finally splicing the result array into just the starting 'k' values gives us the resulting answer which is returned.

## Problem: Insert Delete GetRandom O(1)

The 'setdata' array stores the elements added to the set and the 'datapos' dictionary stores the position of each element in the 'setdata' array for faster lookup times. The insert function checks if the input value is in the 'setdata' array, if it is not then it is added to the array and its position is stored inside 'datapos' and 'true' is returned, otherwise 'false' is returned. The remove function checks if the input value is in the array, if it is then its position is extracted, the last element in the array is extracted, the last element is placed in the position of the value in the array, the position of the last element is updated to the position of the input value, the value is removed from the array and the hashmap, and finally 'true' is returned. Otherwise false is returned. The getRandom function uses the 'random' module in python to get a random no. between 0 and length of the 'setdata' array minus 1 and use this randomly generated no. to return a random value form the 'setdata' array.