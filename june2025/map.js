// function map(array, callback) {
//   const result = [];
//   for (i = 0; i < array.length; i++) {
//     const newEle = callback(array[i], i, array);
//     result.push(newEle);
//   }
//   return result;
// }
// const result = map([1, 2, 3, 4], (x) => x ** 2);
// console.log(result);

const fiveSort = (nums) => {
  if (!nums.length) return nums;
  if (!nums.includes(5)) return nums;

  let i = 0,
    j = nums.length - 1;

  while (i < j && nums.slice(i, j).includes(5)) {
    while (nums[j] === 5) j--;
    console.log("first:", { i, j, nums });
    if (nums[i] === 5) {
      console.log(nums[i], nums[j], i, j);
      [nums[i], nums[j]] = [nums[j], nums[i]];
    } else i++;
  }
  return nums;
};

console.log(fiveSort([5, 5, 6, 5, 5, 5, 5]));

//thought -> act -> observe

//User: What to make for dinner tonight that is Italian?

//Thought
//Agent: User need Italian recipes so I will access a tool that fetches Italian recipes

//Action:
//Agent: I will use get_recipe tool

// {
// 'action': 'get_recipes',
// 'action_input: {
//    'type': 'Italian'
//}
//}

//Observation:
//Agent: "Here is a list of Italian recipes that might fit your liking"
