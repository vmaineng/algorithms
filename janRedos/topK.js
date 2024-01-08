const topK = (nums, k) => {
//an array of numbers, and an integer
//return the top k amount

//using frequency counter pattern
//use an object to keep track of values
//iterate through the object to find the top keys according to k

let map = new Map();
const bucket = [];
const result = [];

for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
}

//sorting bucket;
//find the values of occurences
//else add a new number
for (let [num, freq] of map) {
    bucket[freq] = (bucket[freq] || new Set()).add(num);
}

for (let i = bucket.length - 1; i >=0; i--) {
    if (bucket[i]) result.push(...bucket[i]);
    if (result.length === k) break;
}
return result;

}

console.log(topK([1,1,1,1,1,3,2,3,4], 3))