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
}

//concept: merge alternatively despite value