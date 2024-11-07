function solution(number) {
  //receive a number
  //return the sum of all multiples of 3 or 5 below the number

  //15 => 3, 5,6, 9, 10,12 => 45

  //initialize a sum total
  //iterate up to number
  //check if the number can be by number with no remaineder
  //add to the sum

  let sum = 0;
  for (let i = 1; i < number; i++) {
    if (number / i) {
      console.log(i, number);
      sum += i;
    }
  }
  return sum;
}

console.log(solution(10));
