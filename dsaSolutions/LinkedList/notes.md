# Introduction - Singly Linked Lists

A linked list consists of nodes where each node contains a value and the reference to the next node. The last node in the list points to Null. The 'head' node is used to represent the whole list.
Unlike an array, in order to access an element in the linked list we need to traverse the entire list all the way down to the element which takes O(N) time.

## ADD and DELETE Operations

In order to add a node 'curr' in between the 'prev' and 'next' nodes in the linked list, we first make the 'curr' node's next pointer point to the 'next' node and then the 'prev' node's next pointer points to 'curr' node. This completes the insertion.
The insertion operation takes only O(1) time which is significantly faster than insertion in an array where all the arrays coming after the inserted element must be pushed farther in the array to make space.
In order to insert at the head the 'curr' node's next pointer points at the current head and then the 'curr' node is declared as the new head node.

Deleting a node requires traversing the list down to find the 'prev' node just before the node to be deleted. Then the pointer of 'prev' node is assigned to the 'next' node just after the node to be deleted. In this way the node between 'prev' and 'next' is taken out of the link effectively deleting it.
This process takes O(N) time as traversal of the list is required. Removing the head node simply requires moving the head pointer to the second node in the list.

# Two Pointer Technique

The two pointer technique can be described easily with the following common problem: "Given a linked list, determine if there is a cycle inside of it".
To solve this problem we assign 2 pointers at the head of the linked list. One pointer will move one step at a time while the other will move 2 steps at a time. If there is no cycle in the list then the faster pointer will reach the end of the list first, if there is a cycle then the faster pointer will eventually match up with the slower pointer confirming the existence of a cycle.
This method is known as the two pointer technique.

## Problem: Linked List Cycle 2

Start the solution with the same two pointer method. First pointer only moves one step a time and second moves two steps a time. If the two pointers meet and a cycle is found then the slow pointer is assigned to the head again and another loop is started where both pointers move one step a time until both pointers meet again. The node at which the two pointers meet at again is then returned as it is the node where the cycle starts. Apparently when finding if a cycle exists or not the pointers always meet 'n' nodes before the start of the cycle where 'n' is the no. of nodes before the start of the cycle that don't belong in the cycle. And so, when slow pointer is moved to the head, both slow and fast pointers are exactly 'n' nodes away from the start of the cycle and they end up meeting at the starting node of the cycle.

## Problem: Intersection of Two Linked Lists

Both of the heads of the linked lists are assigned one pointer each. The pointers traverse down their list and when one reaches the end of its list then it is assigned to the head of the other list and the traversal continues down the other list. This continues until the two pointers meet up. When they do the loop is broken and first pointer is returned as it points to the common node where both lists meet. This solution works because the pointer on the shorter list traverses down the common nodes to the end and then swaps to the other list to traverse the difference in the number of nodes between the lists. This is the same no. of nodes that the longer list pointer traverses before swapping to the other list head. When both pointers have swapped to the other side they line up in their positions vertically, and as a result they end up meeting at the node common to both lists always. Also two lists that don't have any node in common can be thought of having the NULL value at each lists end as the common node. Running the same algorithm without any changes will result in NULL being returned for lists that don't intersect.

## Problem: Removing the Nth node from the end of the list

Two pointers fast and slow are set at the head of the list. The fast pointer traverses down 'n' times where 'n' is the no. of node from the end of list that needs to be removed. Then it is checked if fast is NULL or not. If it is then that means that fast pointer reached the end of the list and the 'nth' node to be removed from the list is the head node itself, in this case the second node after head is returned. The fast and slow pointer are then traversed down the list one step a time until the fast pointer reaches the end of the list. The 'nth' element to be removed is the one just after the slow pointer when the iteration is done. And so, it is removed by pointing the slow nodes 'next' pointer to the next node's next node. The head is finally returned after the 'nth' node is removed. This solution works because it gives the fast pointer a head start by making it traverse 'n' times. This creates exactly 'n' nodes gap between slow and fast pointers. As a result when the fast pointer reaches the end the 'nth' node to be removed is exactly one node after the slow pointer.

# Classic Problems

## Problem: Reverse Linked List

In the main function the helper function that takes values 'node' and 'prev' where 'node' is the current node pointer on which the operations will be made and 'prev' is the pointer pointing to the node before the current one. The helper function is passed only the head node pointer in the 'node' argument and the 'prev' argument will be NULL for the first execution of the helper function. On each recursion the list node just after 'node' pointer will be assigned as the 'curr' pointer and the 'node' pointer will point to the 'prev' value. Then the helper function is called again with the 'curr' value passed as 'node' argument and 'node' value passed as 'prev' value for the next recursion. This solution works because on each recursion the current first node is removed from the list and added to the new linked list that is growing backwards. When the 'node' pointer becomes NULL then that means that it has reached the end of the input linked list and the other reversed linked list is complete with its head pointer being 'prev', and so 'prev' pointer is returned.

## Problem: Remove Linked List Elements

The entire list is traversed using recursion and passing the next value of the current 'head' pointer as the 'head' for the next recursion. After the recusion reaches the end of the list and the function calls start to return back then the 'val' of the current 'head' node is checked. If it doesn't match then the current 'head' is returned as is, if it does then the next value of the current 'head' node is returned. This causes the node whose value matches to fall off from the list as the node immediately after it gets stored as the next value of the node before it. When the recursion returns end all matching nodes are dropped from the list.

## Problem: Odd Even Linked List

The solution assigns an 'odd' pointer to the first node, an 'even' and an 'evenhead' pointer to the second node. Then the list is iterated through and on each iteration the 'odd' and 'even' nodes are joined with the node that is next to next of them (2 places ahead of them). This causes a splitting of the Linked list into parts where one contains only odd nodes and other contains only even with 'evenhead' pointer at its head. Finally the odd nodes' list's end is joined to the even nodes' list by pointing it to 'evenhead'. This joins the two lists to result in one list and the solution is complete.

## Problem: Palindrome Linked List

The solution is to assign two pointers 'fast' and 'slow' to the head of the list and iterate through the list with the 'slow' pointer moving one step a time and the 'fast' pointer moving two steps a time. After the iteration ends the 'slow' pointer will point to the middle of of the list. Then another iteration is run which uses the 'slow' pointer to the reverse the second half of the list. After the iteration ends we will have a pointer pointing to the end of the end of the reversed second half of the list. A third iteration is run where two pointers one from the head and one from the end will move towards the middle of the list and at each iteration the values of the nodes will be compared. If the node values differ at any point then that means the list is not palindrome otherwise it is.

# Doubly linked lists

A Doubly linked list is one where each node stores reference to the next node and previous node as well. This makes it possible to traverse the list in both directions: forwards and backwards.

Adding a node in doubly linked lists is simply done in two steps: link the 'prev' value of the 'curr' node to the previous node where we want to insert the node and the 'next' value of the 'curr' node to the node after where we want to insert the node; then link the 'next' value of the node before to 'curr' and the 'prev' value of the node after to 'curr'. This addition operation takes O(1) time.

Deleting a node 'curr' can be done by linking the 'next' value of the node before to the 'next' value of the node after 'curr'. This removes the 'curr' node from the linked list and effectively deletes.

## Problem: Merge Two Sorted Lists

The solution goes down the two linked lists using recursion based on which current node's value is lesser and returns list node when one of the lists has reached its end. The order in which the nodes return when the recursive function calls return is decreasing and as they return they get linked to the 'next' value of the current node. This way when the recursion ends the list node returned is the head of the merged list.

## Problem: ADD two numbers

The solution is to initialise a 'dummyHead' node with the value 0, assign a 'tail' pointer at this node, and initialise a 'carry' value to 0. Then iteration is done until list1 pointer is not None or list2 pointer is not None or 'carry' value is not None. In each iteration we take out the values of both list1 and list2 and add both of them with the carry from previous iteration. Then the unit digit and the carry of the sum are extracted and a new node with the unidigit as its value is created and it is assigned to the next value of the tail node. The 'tail' node is moved forward one node and list1 and list2 are moved forwards as well and the iteration continues. Finally the node right after the 'dummHead' one is returned since that is where the list actually starts from.

## Problem: Flatten a Multilevel Doubly Linked List

Create a dummy node and assign a 'prev' pointer to the dummy node. Also initialise an empty stack and add the head node to it. Iterate until the stack runs empty. In each iteration take out the topmost 'root' node in the stack, connect it to the 'prev' node by assigning 'prev' to the previous value of 'root' and assigning 'root' to the next value of 'prev'. Then if there exists a node after 'root' it is added to the stack, if there also exists a child node of the 'root' then it is added to the stack too. The 'prev' node is moved onto the 'root' node and the iteration continues. This causes the nodes to be popped off from the stack and connected to the 'prev' node in the order that is desired and the correct flattened list is formed as the iteration goes. Finally the node right after the dummy node is returned because that is where the flattened list starts from.

## Problem: Copy List with Random Pointer

This problem is solved by iterating through the list and creating a new node each iteration with the same value as the current node and inserting the new node right after the current one. At the end of the iteration we have a list with each node duplicated and the list being twice the size of the original. Then the second iteration is started where the each random connection between current node and the other node is copied creating a random connection between current node's duplicate and other node's duplicate. After this second iteration a third one is run in which the original nodes and the duplicated nodes are seperated creating two lists. The list consisting of new nodes is returned and it is the copied list with all 'next' pointers and 'random' pointers copied.

## Problem: Rotate List

The solution starts by assigning a 'lastEle' pointer to the head and iterating to the end of the list with this pointer so that by the end of the iteration 'lastEle' will point to the end of the list. While iterating to the end of the list the no. of nodes will also be counted and stored. The value of 'k' is assigned the value of the modulus between 'k' and the length of the list, this is done to address the cases where 'k' is larger than the length of the array, by taking the modulus it is ensured that we don't to cycle around the list multiple times. Then the list is iterated over (length-k-1) times from the head which ensures that we stop at the node right before the one which will become new head. This 'to be new head' node is saved and returned after the node before it is linked to NULL. This creates a new list where the nodes have rotated 'k' times correctly.