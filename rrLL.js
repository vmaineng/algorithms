const reverseLL = (head) => {
//linked list question - receive the first node of list (head)
//return the linked list in reverse
//1 => 2 => 3 => null convert this to => null => 3 => 2 => 1 => null

//if the head is empty, return null
//if head only has one value return the head

//initialize a prev node to null;
//while list is not empty, iterate
//point the first node to null
//keep moving pointers

if (!head) return null;

let current = head;
let prev = null;


while (current !== null) {
    const next = current.next; //to capture next node
    current.next = prev; //switch the pointer to the previous node
    prev = current;  //increment the node
    current = next; //increment the node

}
return prev;
}

const a = new Node("a");
const b = new Node("b");
const c = new Node("c");
const d = new Node("d");
const e = new Node("e");
const f = new Node("f");

a.next = b;
b.next = c;
c.next = d;
d.next = e;
e.next = f;

console.log(reverseLL(a))