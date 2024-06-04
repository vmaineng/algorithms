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

function order(words) {
  //receive a string with space and chars and letters
  //return the string back in order '1', '2', '3'
  //'hi2 kit3 air1' => 'air2 hi2 kit3'

  //edge case: if string is empty, return string
  if (!words) return "";

  //split the string into an array to get individual words
  //iterate through the array to find 1, then add to new string
  //add count?
  //join them back together

  let splitWords = words.split(" ");
  const sortedWords = splitWords.sort((a, b) => {
    const numA = parseInt(a.match(/\d/)[0]);
    const numB = parseInt(b.match(/\d/)[0]);
    console.log(numA, numB);
    return numA - numB;
  });
  console.log(sortedWords);
  return sortedWords.join(" ");
}
function reverseWords(str) {
  //receive a string of words and spaces
  //return the string back reversed and spaces in same order
  //'this fish' => 'hsif siht'

  //split the words
  //take the word and reverse it
  //join the word back into one
  //then join it back with spaces

  let newStr = [];

  let splitStr = str.split(" ");
  for (let i = 0; i < splitStr.length; i++) {
    splitStr[i] = splitStr[i].split("").reverse().join("");
    newStr.push(splitStr[i]);
  }
  return newStr.join(" ");
}

console.log(order("is2 Thi1s T4est 3a"));
