const mergeTwo = (list1, list2) => {
    //get the head of two sorted linked lists
    //return one linked lists with two lists combined in order
    //1 -> 2 -> 6 -> 8, 3 -> 5 -> 10 -> 11 -> 12
    // => 1 -> 2 ->3 -> 5 ->  -> 6 -> 8-> 10 -> 11 -> 12

    //edge cases: if one of the linked lists is empty, return the other one

    //create a dummy node
    //check if the value from L1 is < L2, add in l1
    //else add in the node from l2
    //if there's remaining nodes from L1, add the rest in
    //if there's remaining nodes from L2, add the rest in 
    //return the node after dummy

    let dummy = new ListNode();
    let tail = dummy;
    let current1 = list1;
    let current2 = list2;

    if (!current1) return current2;
    if (!current2) return current1;

    while (current1 !== null && current2 !== null) {
        if (current1.val < current2.val) {
            tail.next = current1;
            current1 = current1.next;
        } else {
            tail.next = current2;
            current2 = current2.next;
        }
        tail = tail.next;
    }

    if (current1 !== null) tail.next = current1;
    if (current2 !== null) tail.next = current2;

    return dummy.next;
}