# Traversing a tree

A Binary tree is a tree like data structure in which each node has at most 2 children. There are 3 ways to traverse a tree: Pre-order, In-order and Post-order

## In-Order Traversal

Traverse all of left subtree, then visit the root and then the right subtree. Think of left node, root and right node being in order with the root in the middle, hence the name 'in-order'.

> left -> root -> right.

## Pre-Order Traversal

Traverse the root first, then the left subtree and then the right subtree. Think of root node coming before left and right nodes, hence the name 'pre-order'.

> root -> left -> right.

## Post-Order Traversal

Traverse the left subtree, then the right subtree and then the root. Think of root node coming after left and right nodes, hence the name 'post-order'.

> left -> right -> root.

When deleting nodes in a tree post-order traversal is used.

## Level Order Traversal

Level-order traversal is to traverse the tree level by level. Breadth-First Search is an algorithm to traverse or search in data structures like a tree or a graph. The algorithm starts with a root node and visit the node itself first. Then traverse its neighbors, traverse its second level neighbors, traverse its third level neighbors, so on and so forth. When we do breadth-first search in a tree, the order of the nodes we visited is in level order.

## Creating Binary Tree from Postorder and Inorder Traversal

The postorder traversal array will always end with the root node. Take out the root node from the postorder array and find it inside of the inorder array. All the nodes on the left side of found root node in the inorder array will constitute the left subtree and all the nodes on the right will constitute the right subtree. Then the same is done for the next root node from the postorder array (the second last element) and then the next one (the third last) and then the next one and so on.

For creating binary tree from the preorder and inorder traversal, the root node will always be at the start of the preorder array (the first element). And so the root nodes are taken out of the beginning of the preorder array continuously instead of the back.
 