// For parentheses to be considered balanced, there must an opening parenthesis
//  followed by a matching closing parenthesis. Given a string containing only 
//  parentheses, return the number of additional parentheses needed for the 
//  string to be considered balanced. 
// The input string will have a minimum length of 1.

const balanceParen = (string) => {
    //string of open and closed parenthesis
    //return the total amount of additional parenthesis needed
    //'())' => 1
    //'()())))((()))' => 3

    //if string is less than 1, return 1
    //initialize a count at 0;

    //create an object of opening and closing
    //iterate through the string and check in the object if there is a closing value
    //if so, keep iterating
    //otherwise, increment count to add more parenthesis
    //return count;

    if (string.length === 1) return '1';

    // let missing = 0;
    // let opening = 0;

    // for (let i = 0 ; i < string.length; i++) {
    //     if (string[i] === '(') {
    //         opening++;
    //         continue;
    //     }

    //     if (opening > 0) {
    //         opening--; 
            
    //     } else {
    //         missing++;
    //     }
    // }
    // console.log(opening, missing) //opening = '('; missing = ')'
    // return missing + opening;

    let stack = [];
    let additionalParanetheses = 0; //count how many paranetheses are needed

    for (let i = 0; i < string.length; i++) {
        if (string[i] === '(') {
            stack.push(string[i])
        } e
    }
}

console.log(balanceParen('())))'))