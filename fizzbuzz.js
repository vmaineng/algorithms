// Given a number as an input, print out every integer from 1 to that number. 
// However, when the integer is divisible by 3, print out “Fizz”; 
// when it’s divisible by 5, print out “Buzz”; 
// when it’s divisible by both 3 and 5, print out “Fizz Buzz”.



const fizz = (number) => {
    //get number as an input
    //return if # is / 3 = "fizz", # is / 5 = "buzz", # is / 3 & / 5 = "fizz buzz"
    //fizz(35) => "buzz", divisible by 5

//if number is empty, return null; 
//check if number is divisble by 3, then "fizz"
//check if number is divisible by 5, then "buzz",
//check if nubmer is divisible by 3 and 5, then "fizz buzz"
//else return number

    if (!number) return null; 

    if (number % 3 === 0 && number % 5 === 0) {
        return "fizz buzz"
    } else if (number % 5 === 0) {
        return "buzz"
    } else if (number % 3 === 0) {
        return "fizz"
    } else {
        return number
    }

}

console.log(fizz(23))