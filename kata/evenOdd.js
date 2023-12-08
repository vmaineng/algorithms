function evenOrOdd(number) {
//whole positive integer
//return even if number is even, and return odd if number is odd
//14 => even; -2 => even

//edge case: 
//if someone typed in a non-number, return please enter a number

//if module is 0, then it's even,
//else it's odd

if (!Number.isInteger(number)) {
    return "please put in a number"
}

return number % 2 === 0 ? "Even" : "Odd";

}

console.log(evenOrOdd(3))