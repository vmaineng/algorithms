const palidromeLL = (head) => {
    //palindrome = same as it is forward as it is backward

    //brute force method
    //convert the linked list into an array and checkng there
    //reverse LL 
    //create pointers to point to prev node
    //iterate through while current node does not equal null
    //if the start equal the same as the last node,
    //return true
    //else it's false
    //creating an array = hurts space complexity

//     if (!head) return [];

//  let nums = []

//     while (current !== null) { //while we havent' end of the list where it is null
//push all values into the array
//        nums.push(head.val)
//        update pointer
//        head = head.next
//     }

//     let left = 0;
//     let right = nums.length - 1
//     while (left < right) {
//         if (nums[left] !== nums[right]) {
//             return false
//         } else {
//             l++
//             right--
//         }
//     }
//     return true

//optimized method w/ fast and slow pointer
//https://leetcode.com/problems/palindrome-linked-list/solutions/1137027/js-python-java-c-easy-floyd-s-reversal-solution-w-explanation/
//start with both pointers at the head
//move fast pointer to move 2x faster
//once the fast pointer reaches the end, the start reaches the middle since it is 2x as fast
//pointers can only go one direction since it is a SLL
//there is an algorithm to reverse LL
//start to reverse LL from middle


let fast = head
let slow = head
let prev;
let temp;

//find middle with the slow pointer
while (fast && fast.next) { //keep traversing through until fast is the last node and we reached the end of the list
    fast = fast.next.next //fast is updated twice ; moving twice as fast
    slow = slow.next //moves one at a time
}

//reverse second half of the list

while (slow) { //start at slow in the middle until we reached the end of the list
    //update and reverse the pointer at slow
    temp = slow.next
    slow.next = prev
    prev = slow
    slow = temp

}

//check if it is a palindrome
//prev will be at the last node
//then it will be slow 
 fast = head
slow = prev
//once right pointer reaches middle, can stop checking
while (slow) {
    console.log(fast.val, slow.val)
    if (fast.val !== slow.val) return false
    
    //keep iterating
    fast = fast.next;
    slow = slow.next;
    
}
return true;
}

console.log(palidromeLL([1,2, 2, 1]))