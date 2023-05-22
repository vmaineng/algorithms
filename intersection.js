//leetcode 349

const intersection  = (nums1, nums2) => {
//create start pointer for each index in the array
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
        i++;
        j++;
       } else if ()
    }
}
}

}

console.log(intersection([4,9,5], [9,4,9,8,4]))