const reverseList = (head) => {
    // todo
  //head of a linked list
    //if there is no head, then return null 
    //create a prev node 
    //assign current to the head
    //iterate through linked list until it reaches null
    //capture the next node after current
    //assign the pointer to look back at prev node
    //increment prev and current node to next node
    //return prev
    
    let prev = null;
    let current = head;
    
    while (current !== null) {
  let next = current.next;
      current.next = prev; 
      prev = current;
      current = next;
  }
    return prev;
  };
  

  const reverseListRecursive = (head, prev = null) => {
    //recursively
      //base case: if head reaches null; return the prev
      //call the function on prev node;
      if (head === null) return prev;
      const next = head.next;
      head.next = prev;
      return reverseList(next, head) //next will replace head in the paramenters
      //head will replace prev=null
    
    };