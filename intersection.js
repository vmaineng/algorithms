//leetcode 349

const intersection  = (nums1, nums2) => {
//brute force would to have one pointer in the first array at first index
//and look at all the possibilities in second array to see if it matches the value
//time = O(N^2) ? look at each two arrays
//space = O(n) = storing a new array of intersection

//optimized method:
//create start pointer for at the first index in each array
//initialize an array to keep track of same values
//check if they are the same,
//then return the value they intersect at
//tell it to keep going

//can't use let i = 0 by itself; need i to iterate through nums1 array
//can't use  if (nums1[i] === nums2[j]) {
    //     return [nums1[i], nums2[j]]
    // }
//b/c need to keep track of unique values

let sameValuesArray = []

for (let i = 0; i < nums1.length; i++ ) {
for (let j = 0; j < nums2.length; j++) {
    if (nums1[i] === nums2[j]) {
       if (!sameValuesArray.includes(nums1[i])) {
       sameValuesArray.push(nums1[i])
       }
    }
}
}
return sameValuesArray
}

console.log(intersection([4,9,5], [9,4,9,8,4]))