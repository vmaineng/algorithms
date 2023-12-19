const reverseList = (head1, head2) => {
    //receive two heads of linked lists
    //return one long linked list
    //1 ->2, 2-> 3 ->8 => 1->2->2-> 3 ->8 

    //edge case: if they're both empty, then return an empty linked list
    //if one linked list has only one node, return the node

    //identify pointers, one to keep track of head
    //one to keep track of the tail, count, head of second linked list
    //iterate until it reaches null
    //if count is even, take it from second LL, else take it from the first LL
    //if a LL Is longer than the other, add the rest of it and vice versa for LL 2
    //return head 

    let current1 = head1;
    let tail = head1.next;
    let current2 = head2;
    let count = 0;

    while (current1 !== null || current2 !== null) {
        if (count % 2 === 0) {
            tail.next = current2; //the pointer will point towards the node from LL2
            current2 = current2.next;
        } else {
            tail.next = current1;
            current1 = current1.next;
        }
        tail = tail.next; //move tail up to the node that just got connencted
        count++
    }
    if (current1 !== null) return current1.next;
    if (current2 !== null) return current2.next;

    return current1;
}

//concept: merge alternatively despite value
//always keep track of nodes in both lists; i.e. - current1, current2
//traverse through both lists until it hits null
//check to see if even or odd, add on to list
//move the tail node to the newest node that got linked to
