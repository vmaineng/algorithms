var removeNthFromEnd = function(head, n) {
    //head of a linked list, and an integer of how much to move
    //return a new linked list with the node removed
    //1-> 2-> 3-> 4-> 5->6, 4 => 1-> 2-> 4-> 5->6

    //could reverse in-place and start from the right
    
    //another method (Two Pointers):
    //create a dummy node
    //initialize right pointer
    //iterate through it and decrement from n
    //tell the pointer to point to the next node
    //return dummy.next

    let dummy = new ListNode(0, head);
    let left = dummy;
    let right = head;

    while (n > 0 && right !== null) { //loop to increment pointers to keep shifting right
right = right.next
n -= 1 //once it equals 0, we have shifted enough;
    }

    while (right !== null) { //keep shifting til we reach end of the list
        left = left.next; //shift pointers
        right = right.next; //shift pointers
    }

left.next = left.next.next //delete node - have pointer point to the next node after removed node

    return dummy.next;

};