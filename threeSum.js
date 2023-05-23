const threeSum = (nums) => {
  //initialize an array to capture results

  //brute force = O(n^3)
  //three for nested loops
  //see if i and j k = target,
  //push answer into array

  //optimized method:
  //sort from ascending order
  //iterate through the loop
  //do two pointers on left and right
  //see if they match target

  let answer = [];
  nums.sort((a, b) => a - b);

  //iterate through where nums.length - 2 b/c we need to output 3 answers
  for (let i = 0; i < nums.length - 2; i++) {
    if (i === 0 || nums[i] !== nums[i - 1]) {
      let left = i + 1;
      let right = nums.length - 1;

      while (left < right) {
        if (nums[i] + nums[left] + nums[right] === 0) {
          answer.push([nums[i], nums[left], nums[right]]);
          while (left < right && nums[left] === nums[left + 1]) left++;
          while (left < right && nums[right] === nums[right - 1]) right--;
          left++;
          right--;
        } else if (nums[left] + nums[right] < 0) {
          left++;
        } else {
          right--;
        }
      }
    }
  }

  return answer;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
