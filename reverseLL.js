//leetcode 206 - reverse Linked List I
var reverseList = function (head) {
  //if there is a head first, return an empty []

  //Start iterating through at the head(current pointer)
  //look at the next pointer (curr.next)
  //create a previous pointer
  //loop through the original array while current has not hit null
  //

  if (!head) return null;

  let current = head;
  let prev = null;

  while (current !== null) {
    let next = current.next; //need the next node
    current.next = prev; // pointer from 3 to pointer 1 //reverse
    prev = current; //1 becomes 2
    current = next;
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