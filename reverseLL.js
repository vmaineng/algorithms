//leetcode 206 - reverse Linked List I
var reverseList = function (head) {
  //if there is a head first, return an empty []

  //Start iterating through at the head(current pointer)
  //look at the next pointer (curr.next)
  //create a previous pointer //initialize it null
  //loop through the original array while current has not hit null
  //then switch the pointers to point to prev null

  if (head === null || head.next === null) return head;

  let current = head;
  let prev = null;

  while (current !== null) {
    let next = current.next; //need the next node
    current.next = prev; // pointer from 3 to pointer 1 //reverse the pointers
    prev = current; //1 becomes 2 //increment prev to current
    current = next; //increment current to = the next node
  }
  return prev; 
};

//console.log(reverseList([1, 2,3,4, 5]))

var reverseBetween = function (head, left, right) {
  //if head contains only one node, return head

  //let current = head
  //create a previous pointer

  //initialize a left pointer
  //initialize a right pointer
  //while left is less than or equal to right,
  //reverse the nodes from left to right
  //return reversed list

  if (head <= 1) return head;

  let current = head.next;
  let prev = null;

  while (left <= right) {
   let next = current.next
    current.next = prev;
    prev = current;
    current = next;
  }
  return prev
};


console.log(reverseBetween([1,2,3,4,5], 2, 4))

//identify which nodes are important to you
//find 4 nodes
//then connect them