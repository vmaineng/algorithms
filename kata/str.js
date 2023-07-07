// Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

// If no occurrences can be found, a count of 0 should be returned.

function strCount(str, letter) {
    // let count = 0;
  
    // for (let i = 0; i < str.length; i++) {
    //   if (str[i] == letter)
    //     count++;
    // }
    
    // return count;

   // return str.split('').filter(c => c == letter) => ["l", "l"]

    return str.split('').filter(c => c == letter).length;
}

console.log(strCount("Hello", "l"))

// ("Hello", "o")  ==>  1
// ("Hello", "l")  ==>  2
// ("", "z")       ==>  0
// str_count("Hello", 'o'); // returns 1
// str_count("Hello", 'l'); // returns 2
// str_count("", 'z'); // returns 0