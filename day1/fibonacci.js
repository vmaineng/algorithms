// Find the nth element in the Fibonacci series. The Fibonacci sequence starts with a 
// 0 followed by a 1. After that, every value is the sum of the two values preceding it. 
//Here are the first seven values as an example: 0, 1, 1, 2, 3, 5, 8.

function Fibonacci(num) {
//integer of numbers and all positive
//return the sum of last two values
//fib(4) => 0, 1, 1, 2 => 2 + 1 = 3
//fib(7) => 0, 1, 1, 2, 3, 5, 8 => 8 + 5 = 13

//iterative method: 
//if num less than 2, return 0 + 1

//iterate through up to num
//add sum of last two nums
//return sum

// if (num === 0) return 0; 
// if (num === 1) return 1;

// let fib = [0, 1]

// for (let i = 2; i <= num; i++) {
//     fib[i] = fib[ i  - 2] + fib [i - 1]
// }

// return fib[num];

//recursive

if (num === 0) {
    return 0
} else if (num === 1) {
    return 1
} else {
    return Fibonacci(num - 1) + Fibonacci(num - 2)
}


}

console.log(Fibonacci(42))