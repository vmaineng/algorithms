function reverseWordsInString(string) {
  //receive a string of words in a string
  //return the words reversed
  //'hello world' => "world hello"

  //create a new string
  //iterate at the end of the string
  //add it in to new string
  //check if it is a space, then add space
  //else add in word
  //return new string

  let newString = "";
  let word = "";

  for (let i = string.length - 1; i >= 0; i--) {
    if (string[i] === " ") {
      console.log(string[i]);
      newString += word + " ";
      word = "";
    } else {
      word = string[i] + word;
    }
  }
  return newString + word;
}

// Do not edit the line below.
exports.reverseWordsInString = reverseWordsInString;

console.log(reverseWordsInString("hello world"));

function isValidSubsequence(array, sequence) {
  //receive two arrays of integers (pos and neg)
  //return boolean ; true if sequence is in array, else false
  //[3,225,1,4,7,-78], [3, 7,11,8,9] => false

  //edge case: if sequence's length > array => false

  //create indexs on array and sequence
  //iterate through both arrays
  //if you find that the values match, increment both pointers
  //return if index of seq has reached end of array

  if (sequence.length > array.length) return false;

  let arrayIdx = 0;
  let seqIdx = 0;

  while (arrayIdx < array.length && seqIdx < sequence.length) {
    if (array[arrayIdx] === sequence[seqIdx]) seqIdx++;
    arrayIdx++;
  }
  return seqIdx === sequence.length;
}

// Do not edit the line below.
exports.isValidSubsequence = isValidSubsequence;

function tournamentWinner(competitions, results) {
  //receive an array of array of teams, and an array of results
  //return which team was the winner
  //[
  //  Home        away
  //[ "Fashion", "Makeup"],
  //["Shoes", "Fashion"],
  //["Makeup", "Fashion"]
  //]

  //[0,0,1] => Fashion, Fashion, Fashion => winner Fashion

  //keep track of score with the teams as key
  //iterate through array based on the results received
  //iterate through object to see who has the most point, return the key (team)

  let scores = {};
  let currentBestTeam = "";
  scores[currentBestTeam] = 0;

  for (let i = 0; i < competitions.length; i++) {
    const [homeTeam, awayTeam] = competitions[i]; //good to deconstruct
    const result = results[i];
    const winningTeam = result === 1 ? homeTeam : awayTeam;

    if (!scores[winningTeam]) {
      scores[winningTeam] = 0;
    }
    scores[winningTeam] += 1;

    if (scores[winningTeam] > scores[currentBestTeam]) {
      currentBestTeam = winningTeam;
    }
  }
  return currentBestTeam;
}

// Do not edit the line below.
exports.tournamentWinner = tournamentWinner;
