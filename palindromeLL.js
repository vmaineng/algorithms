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

//     if (!head) return [];

//  let nums = []

//     while (current !== null) {
//        nums.push(head.val)
//        //update pointer
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



}

console.log(palidromeLL([1,2]))