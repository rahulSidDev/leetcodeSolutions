# What is a Trie?

Trie is also called a prefix tree and it is a special kind of 'N-ary' tree. Typically it is used to store strings. Each node in a Trie represents a string (a prefix). Each node might have several children and the paths to different child nodes represent different characters. And the strings the child nodes represent will be the original string plus the character on the path.

All the descendents of a node have a common prefix of the string associated with that node. That is why Trie is also called a prefix tree.

## How to represent a Trie?

First solution is to use array to store children nodes. If we store strings that only contain letters from 'a' to 'z' then we can declare an array containing the 26 letters in each node to store its children. And for a specific character `c` we can use `c - 'a'` as the index to find the corresponding child node in the array. In this method it is very fast to visit a child node and it is comparatively easy to visit a specific child since we can easily transfer a character to an index in most cases. But there is some waste of space with this method as not all child nodes are needed.

The second solution is using the hashmap to store the children nodes. We can declare a hashmap in each node. The key of the hashmap are characters and the value is the corresponding child node. It is even easier to visit a specific child directly from the corresponding character. It is a little slower than using an array but it saves more space since we only store the child nodes we need and its also more flexible because we are not limited by a fixed length and range.

## Insertion into a Trie

When we insert a target value into a Binary Search Tree (BST), in each node we need to decide which child node to traverse to depending on the relationship of the target value to the node value. Similarly when we insert into a trie we decide which child node to go to depending on the target value being inserted. Lets say we want to insert string 'S' into the Trie. We start with the root node and see if any children of the root node match 'S[0]'. If there are no child nodes that match then a child node will be created with the value of 'S[0]'. Then after going to the child node that matches the same steps are repeated for 'S[1]'. The psuedocode will look something like this:

```
1. Initialize: cur = root
2. for each char c in target string S:
3.      if cur does not have a child c:
4.          cur.children[c] = new Trie node
5.      cur = cur.children[c]
6. cur is the node which represents the string S
```

## Searching in a Trie

As mentioned before all descendants of a node will have prefixes of the string associated with that node. And so, it is easy to search if there are any words in the trie that start with a given prefix. Similarly we can go down a trie tree given a certain prefix, if we can no longer find a child node that matches then the search fails. The psuedocode looks something like this:

```
1. Initialize: cur = root
2. for each char c in target string S:
3.   if cur does not have a child c:
4.     search fails
5.   cur = cur.children[c]
6. search successes
```

### Additional notes

Go through the 'Max XOR of Two Numbers' to get better understanding.