
function removeDuplicatesFromLinkedList(linkedList) {
    // Write your code here.
    //linked list of nodes
    //return a new list that removes duplicates
    //
  
    //if it's empty, return null
  
    //create a dummy node
    //add the tail
    //go through the linked list
    //make the tail point to the next node
    //if the next node's value is not the same, add it in, otherwise keep iterating
    //return dummy.next
  
    let current = linkedList;
  
    while (current !== null) {
     let nextDistinct = current.next; //captures the next node
          while (nextDistinct !== null && nextDistinct.value === current.value){
       //skip to the next node
      nextDistinct = nextDistinct.next; //setting pointer to the next node
     
    }
    current.next = nextDistinct; //move pointer to the new node
    current = nextDistinct; //move the current pointer to the next distinct node
  }
    return linkedList;
  }
   