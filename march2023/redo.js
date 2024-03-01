function checkParen(string) {
  //receive a string of parenthesis
  //return true if all pairs, else false
  //'))()' => false

  //create an object
  //store the opening as key, and closing as value

  //iterate through the string
  //check if it's an opening
  //add on to stack
  //else if it is a closing
  //check to make sure the stack's length is not empty
  //check the item from stack's length

  //return true if stack's length is empty after checking

  let stack = [];
  let addParen = 0;

  for (let paren of string) {
    if (paren === "(" || paren === "[") {
      //if you are an opening bracket, add to stack
      console.log(paren, stack);
      //if value exists
      stack.push(paren); //add to list
    } else {
      //if you are a closing bracket, check to make sure stack's not empty
      //then pop of the previous one
      if (stack.length > 0) {
        stack.pop();
      } else {//if don't match, keep track for paren
        addParen++;
      }
    }
  }
  addParen += stack.length; //2
  return addParen === 0 ? true : false;
}

console.log(checkParen("([()"));
