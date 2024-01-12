const mergeLL = (head1, head2) => {
    //get a head of two sorted linked list
    //return one sorted linked list
    //

    //edge cases:
    //if the one of the head is empty, return the other one

    //keep count of odd and even
    //if odd, merge the linked list from the first linked list
    //if even, add in the node from second linked list

    //if left overs from first linked list, add it in
    //if left overs from second linked list, add it in

    //return the head of linked list

    if (!head1) return head2;
    if (!head2) return head1;

    let dummy = new ListNode();
    let tail = dummy;
    let current1 = head1;
    let current2 = head2; 
    let count = 0;

    while (current1 !== null && current2 !== null) {
        if (current1.val < current2.val) {
            tail.next = current1;
            current1 = current1.next; // ! have to assign pointer
        } else {
            tail.next = current2;
            current2 = current2.next; // ! have to create pointer
        }
    }

    if (current1) return tail.next = current1;
    if (current2) return tail.next = current2;
    
return dummy.next;
}