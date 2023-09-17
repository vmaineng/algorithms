// create a node constructor
class Node {
    constructor(val) {
        this.val = val; 
        this.next = null; 
    }
}

// create our singly linked list constructor 
class SinglyLinkedList {
    constructor() {
        this.head = null; 
        this.tail = null; 
        this.length = 0; 
    }

    //push 
    push(val) {
        //create a new node using the value passed to the function
        let newNode = new Node(val)

        // if there is no head property on the list, set the head and tail to be the newly craeted node
        if(!this.head) {
            this.head = newNode; 
            this.tail = newNode; 
        } else {
            // otherwise set the next property on the tail to be the new node and set the tail
            // property on the list to be the newly created node

            // this creates our next arrow 
            this.tail.next = newNode; 
            // assign the new tail node to be at new node 
            this.tail = newNode
        }

        // update the length
        this.length++
        return this 
    }

    pop() {
        // if there are no nodes in the list, return undefined
        if(!this.head) return undefined

        let current = this.head; 
        let newTail = current; 

        // loop through the list until you reach the tail, you'll know your at the end if it returns null
        while (current.next) {
            // move the new tail to the current position
            newTail = current; 
            // move to the next node, last one will be null
            current = current.next; 
            console.log(newTail, current)
        }

        // set the tail to be the 2nd to the last node 
        this.tail = newTail; 

        // set the next property of the 2nd to the last node to be null
        this.tail.next = null; 

        // decrement by 1
        this.length--

        if (this.length === 0) {
            this.head = null; 
            this.tail = null; 
        }

        // return the value of the node removed
        return current
    }

    push(val) {
        //create a new node using the value passed to the function
        let newNode = new Node(val)

        // if there is no head property on the list, set the head and tail to be the newly craeted node
        if(!this.head) {
            this.head = newNode; 
            this.tail = newNode; 
        } else {
            // otherwise set the next property on the tail to be the new node and set the tail
            // property on the list to be the newly created node

            // this creates our next arrow 
            this.tail.next = newNode; 
            // assign the new tail node to be at new node 
            this.tail = newNode
        }

        // update the length
        this.length++
        return this 
    }   
}

    const newList = new SinglyLinkedList()
    newList.push(9)
    newList.push(4)
    console.log(newList)