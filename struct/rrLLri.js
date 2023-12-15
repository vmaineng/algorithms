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
      //head will replace prev
      //return the new head of the linked list
    
    };

    //time:O(n)
    //space:O(n)


    // class Node {
//   constructor(val) {
//     this.val = val;
//     this.next = null;
//   }
// }

const zipperLists = (head1, head2) => {

  
  //two linked lists that are not empty
    //return one linked list alternating nodes
    //a->b->c, e-> f -> g => a->e->b->f->c->g
    
    //create a dummy node
    //create a count - odd(take from first list) & even (then take second list)
    //iterate through the linked list until it's null
    //have dummy node point to first linked list
    //then point to second list
    //return dummy.next 
    
    let dummy = null;
    let count = 0;
    let current1 = head1;
    let current2 = head2;
    
    while (current1 !== null && current2 !== null) {
      if (count % 2 === 0){
      dummy.next = current2
        current2 = current2.next;
  } else {
     dummy.next =current1
        current1 = current1.next;
  }
      dummy = dummy.next=current1    
      count += 1;
  }
  
  if (current1 !== null) tail.next = current1;
    if (current2 !== null) tail.next = current2;
  
  return dummy.next;
  };
