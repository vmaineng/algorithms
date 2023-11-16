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
        } else if (string[i] === ')') {
            if(stack.length > 0) {
                stack.pop()
            } else {
                additionalParanetheses++;
            }
        }
    }
    // additionalParanetheses += stack.length; //+= stack.length to capture the remaining opening paranthesis left in stack;
    // console.log(additionalParanetheses, stack.length);
    return additionalParanetheses
}

//create a stack structure
//a counter
//iterate through the string
//if found an opening paraenthesis, add it to the stack
//if found a closing paranethesis, check if the stack has any paranethesis added
//if it does, then pop off the opening paranthesis
//otherwise, add to counter for missing paranthesis
//take the missing parantheses and subtract from the length

console.log(balanceParen('())))'))