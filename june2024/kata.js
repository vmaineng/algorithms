function divisibleBy(numbers, divisor) {
  //receive two array of integers (positive)
  //return back an array of integers from numbers that are divisible by divisor
  //[21, 36, 15], 3 => [21, 36, 15]

  //if anything mod the divisor leaves no remainder, add to the output array

  let outputArray = [];

  for (let i = 0; i <= numbers.length; i++) {
    if (numbers[i] % divisor === 0) {
      outputArray.push(numbers[i]);
    }
  }
  return outputArray;

  //return numbers.filter((number % divisor === 0 )
}

//time: O(n)
//space: O(n)
