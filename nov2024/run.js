function arrayOfProducts(array) {
  //initalize an array of the array's length set it to 1
  //create a multiplier of 1
  //iterate through the array with all the values of the left side
  //iterate through the answer array with all the values from the right side
  //multiple the values from the array with the values from right side

  let answer = new Array(array.length).fill(1);

  let leftMultiplier = 1;
  for (let i = 0; i < array.length; i++) {
    answer[i] = leftMultiplier;
    leftMultiplier *= array[i];
    console.log(answer);
  }

  let rightMultipler = 1;
  for (let i = array.length - 1; i >= 0; i--) {
    answer[i] *= rightMultipler;
    rightMultipler *= array[i];
  }

  return answer;
}

// Do not edit the line below.
exports.arrayOfProducts = arrayOfProducts;

console.log(arrayOfProducts([3, 4, 5]));
//answer of i gets updated from leftmultiplier
//left multiplier moves over to the next value and gets updated
