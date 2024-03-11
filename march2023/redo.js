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
          tail.next = current1; //tail's pointer points to new current1's node
          current1 = current1.next //update pointer
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
    
  function LongestRepeat(s, k) {
    //receive a string and integer of how much to replace
    //return length of longest substring that does not exceed k replacement
    //'CRAYYYAB', 2 => 'CYYYYYAB' => 5

    //create track of the letters seen
    //keep track of the length of the window
    //if the window size - current count of replacements done exceeds, k,
    //then shrink window fom left
    //keep iterating through the rest of the string
    //return maxLength captured


    let count = 0;
    let valueCount = {};
    let length = 0;

    let left = 0;
    let right = 0;

    while (right < s.length) {
      const rightChar = s.charAt(right)
      valueCount[rightChar] = valueCount[rightChar] + 1 || 1
      count = Math.max(count, valueCount[rightChar])
  
    if ((right - left + 1) - count > k) {
      const leftChar = s.charAt(left)
      valueCount[leftChar] -=1
      left++
    }

    length = Math.max(length, (right - left + 1))
    right++
  }
  return length;
  }

  console.log(LongestRepeat('ABAB', 2))

  /**
 * @param {number[]} nums
 * @return {number}
 */
var maxFrequencyElements = function(nums) {
  //receive an integer of numbers/
  //return the total of the max frequences shown in nums * how many elements have the max
  //[1, 2, 3, 5, 3, 3, 5, 5] => { 3: 3, 5: 3} => 3 * 2 = 6

  //create an object to store the occurences
  //iterate and keep track of counter

  //then iterate through to find the max value

  //then iterate through to find the keys of the object

  //multiply each other and return the total

  let maxFreqElements = 0;
  let seenValues = {};
  let maxFrequency = 0;

  for (let i = 0; i < nums.length; i++) {
      const numValues = nums[i]
      seenValues[numValues] = seenValues[numValues] + 1 || 1
  }

  for (let key in seenValues) {
      if (seenValues[key] > maxFrequency) {
          maxFrequency = Math.max(maxFrequency, seenValues[key])
      }
  }

for (let key in seenValues) { //multiple max frequency elements
  if (seenValues[key] === maxFrequency) {
maxFreqElements++
  }
}

return (maxFreqElements * maxFrequency)
};

