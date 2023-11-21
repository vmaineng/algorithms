// read input file into an array
// submit max calories carried by an elf
// spaces mean we should move to a new elf
// 

var fs = require("fs");
var text = fs.readFileSync("./input.txt").toString('utf-8');
var caloriesFile = text.split("\n")
// console.log(textByLine)
// '1000' => 1000 ? parseInt('1000') => 1000
calories = [
    1000, // 0 + parseInt('1000') => 1000
    2000, // 1000 + parseInt('2000') => 3000
    3000, // 3000 + parseInt('3000') => 6000
    0,
    4000,
    0,
    5000,
    6000,
    0,
    7000,
    8000,
    9000,
    0,
    10000
]

function countCalories(input) {
  
let maxCalories = 0;
let calories = 0; 

for(let i = 0; i < input.length; i++) {
    // console.log(calories)
    if (input[i] !== "") {
        // console.log(parseInt(input[i]))
        calories += parseInt(input[i])
        maxCalories = Math.max(maxCalories, calories)
    } else {
        calories = 0;
    }
}
return maxCalories
}

console.log(countCalories(caloriesFile))