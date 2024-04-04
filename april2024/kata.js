function arrayPlusArray(arr1, arr2) {
    //add arr1 and arr2 together in one array
    //use reduce method on it
    return arr1.concat(arr2).reduce((accum, cv) => accum + cv, 0)
  }

  function minMax(arr){
    //receive an array of integers
    //return [min, max] number from the array
    //[5,6,3, 4, 0] => [0, 6]
    
    //edge case: if the length is one, return it as min and max
    
    //spread out the numbers for min, and max
    //return it as an array
    
    if (arr.length === 1) return [arr[0], arr[0]];
    
    let min = Math.min(...arr);
    let max = Math.max(...arr);
    return [min, max]

    //return [Math.min(...arr), Math.max(...arr)]
  }

  function doubleChar(str) {
    //receive a string
    //return a new string with double the characters
    //'Super' => 'SSuuppeerr'
    
    //iterate through string
    //repeat the same digit
    //return new string
    
    let doubleStr = '';
    
    for (let char of str) {
      doubleStr += char.repeat(2)
    }
  return doubleStr
  }
  
  function dontGiveMeFive(start, end) {
    //receive an integer for start and end
    //return the total amount of all numbers with no 5 in it
    //Five(8, 16) => 8, 9, 10, 11, 12, 13, 14, 16 => 7
    
    //initialize a count to keep track of the numbers seen
    //iterate through starting at start to the end
    //if number does not have a five, add to count
    //return count
    
    let count = 0;
    
    for (let i = start; i <= end; i++) {
      // 1, 2, 3, 4, 6, 7, 8, 9
      // i
      let stringNum = i.toString()
      if (!stringNum.match(/5/)) {
        count++
      }
    }
  return count;
  }

  function bonusTime(salary, bonus) {
    // receiving salary (number), boolean for bonus
      //return the salary + bonus if bonus is true, else return the salary
      //(15000, false) => 15000
      //(20000, true) => 20000 * 10 => 200000
      
      if (bonus === true) {
        let newSalary = salary * 10
        return '\u00A3'+`${newSalary}`
      } else {
        return '\u00A3'+`${salary}`
      }
    }