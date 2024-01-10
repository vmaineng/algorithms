const reverseLL = (head) => {
//iterative

//get a head of a linked list
//if it's empty, return empty;

//create a prev
//capture the current as head
//capture the next node as next
//move the pointer from next to prev
//then move the pointers to the rest of the linked lists

if (!head) return null;

let prev = null;
let current = head;

while (current !== null) {
    const next = current.next;
    current.next = prev;
    prev = current;
    current = next;
}

return prev;

}

//recursive

//base case: if head is null, return prev

//set up prev as a default; 
//capture the next node
//pass in next, 

const recursiveLL = (head, prev = null) => {

if (head === null) return prev;

const next = head.next;
return recursiveLL(next, )


}





