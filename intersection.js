//leetcode 349

const intersection  = (nums1, nums2) => {
//create start pointer for each index in the array
//check if they are the same,
//then return the value they intersect at
//tell it to keep going


for (let i = 0; i < nums1.length; i++ ) {
for (let j = 0; j < nums2.length; j++) {
    if (nums1[i] === nums2[j]) {
        return [nums1[i], nums2[j]]
    }
}
}

}

console.log(intersection([4,9,5], [9,4,9,8,4]))