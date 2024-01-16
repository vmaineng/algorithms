const altLL  = (head1, head2) => {
    //head of two sorted linked lists
    //return one sorted linked list

    //edge cases:
    //if linkedlist1 is empty,return linkedlist2
    //if linkedlist2 is empty, return linkedlist1

    //keep count of odd or even
    //if odd, add from linkedlist1
    //if even, add from linkedlist2
    //add in remaining of LL1 or LL2
    //return head1

    if (!head1) return head2;
    if (!head2) return head1;

    const head = head1;
    let tail = head;
    let current1 = head1.next;
    let current2 = head2;
    let count = 0;


    while (current1 !== null && current2 !== null ) {
        if (count % 2 === 0) {
            tail.next = current2;
            current2 = current2.next; //move the pointer
        } else {
            tail.next = current1; 
            current1 = current1.next;
        }
        tail = tail.next;
        count += 1; // !  have to increment count after looking at the current node
    }

if (current1 !== null)  tail.next = current1;
if (current2 !== null)  tail.next = current2;

return head;

}

// objective:
//move tail to the end of the node, then
// increment count after looking at the Node








const altLL2 = (head1, head2) => {
//head of two linked lists
//return one linked list of the two values

//edge cases: 
//if list1 is empty, then return list2
//if list2 is empty, return list1

//initiate a count
//if odd, add in node from first list
//if even, add in from second list
//then increment counter

//if remaining list1, add rest of list1
//if remaining list2, add rest of list 2

if (!head1) return head2;
if (!head2) return head1;

let count = 0; 
let head = head1;
let tail = head;
let current1 = head1.next;
let current2 = head2;

   

while (current1 !== null && current2 !== null) {
    if (count % 2 === 0) {
        tail.next = current2;
        current2 = current2.next;
    } else {
        tail.next = current;
        current = current.next;
    }
    tail = tail.next;
    count ++
}

if (current) tail.next = current;
if (current2) tail.next = current2;

return tail;

}

//return length === set.size();

function playArray(array) {
    const last = array[array.length - 1];
    console.log(last, array.length-1) //last = value, array.length-1 = index
    return last * (last + 1) /2
}

console.log(playArray([1,2,3]))