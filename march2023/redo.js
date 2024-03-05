function checkParen(string) {
  //receive a string of parenthesis
  //return true if all pairs, else false
  //'))()' => false

  //create an object
  //store the opening as key, and closing as value

  //iterate through the string
  //check if it's an opening
  //add on to stack
  //else if it is a closing
  //check to make sure the stack's length is not empty
  //check the item from stack's length

  //return true if stack's length is empty after checking

  let stack = [];
  let addParen = 0;

  for (let paren of string) {
    if (paren === "(" || paren === "[") {
      //if you are an opening bracket, add to stack
      console.log(paren, stack);
      //if value exists
      stack.push(paren); //add to list
    } else {
      //if you are a closing bracket, check to make sure stack's not empty
      //then pop of the previous one
      if (stack.length > 0) {
        stack.pop();
      } else {//if don't match, keep track for paren
        addParen++;
      }
    }
  }
  addParen += stack.length; //2
  return addParen === 0 ? true : false;
}

console.log(checkParen("([()"));

var isPalindrome = function(x) {
  //receive a number
  //return true if palindrome, else return false
  //345 => 543 => false
  
  //edge case: if the length is 1, return true
  
  //convert number to String, split it, reverse it, join it back together and see if it's the same
  
  return x.toString().split("").reverse().join("") === x.toString();
  
  };

  /**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
var mergeTwoLists = function(list1, list2) {
  //get the heads of two linked lists
  //return one LL where the nodes are sorted
  
  //if list2 is empty, return list1;
  //if list1 is empty, return list2;
  
  //create a dummy node;
  //capture the head1, head2 as current node in both lists; 
  //check to see which value is less
  //if list2's value is less, add list 2
  //else add in list1
  //then if there's any remaining, add in the remaining from either list1, or list 2
  
  if (!list1) return list2
  if (!list2) return list1
  
  let dummy = new ListNode()
  let tail = dummy;
  let current1 = list1;
  let current2 = list2;
  
  while (current1 !== null && current2 !== null) {
      if (current1.val <= current2.val) {
          tail.next = current1;
          current1 = current1.next //stick out a pointer
      } else {
          tail.next = current2;
          current2 = current2.next;
      }
      tail = tail.next
  }
  
  if (list1) tail.next = current1;
  if (list2) tail.next = current2;
  
  return dummy.next;
  };
    
  