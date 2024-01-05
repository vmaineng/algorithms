const containDuplicates = function(nums) {
    // for (let i = 0; i < nums.length; i++) {
    //     for (let j = i + 1; j < nums.length; j++) {
    //         console.log(i, j)
    //         if (nums[i] === nums[j]) {
    //             console.log(nums[i], nums[j])
    //             return true;
    //             break;
    //         }
    //     }   
    // }
    //   return false
    

    let i = 0;

for (let j = i+1; j < nums.length; j++) {
    console.log(i, j)
    if (nums[i] === nums[j]) {
        console.log(nums[i], nums[j])
        return true;
        break;
    }
}
return false;

}

console.log(containDuplicates([2,14,18,22,22]))

const reduceString = (string) => {
    let wordSplit = string.split(" ")
    return wordSplit.reduce((acc, cv) => acc + cv, " ")
}

console.log(reduceString("the jack in the box"))