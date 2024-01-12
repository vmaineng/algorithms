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