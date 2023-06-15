//create a class that has two methods
//remove method 
    //- it should print from the number 1
    //if you print a number, you can assume its removed
    //and each time you call print, you should print the next number
    //remove, removes the smallest number starting with 1

//add method:
//add back any removed numbers
//add an integer

//print inifinite numbers

//ex: remove, remove, remove, add(3), add(1), remove, remove
       //1 ,    2 ,     3,     1,    3

class AddRemove{
    constructor(){
        //add map to keep track if the number was added or not
        //use set b/c we only need keys
        //we don't need the values so we don't need to use map

        //this.addedNums = {} //can add any numbers
        this.removedNums = new Set()
        this.pq = new MinPriorityQueue()
        this.pq.enqueue(1)

    }

    //prints the smallest non-removed value, starting from 1
    remove(){

        //find the num to remove

        //it will either be 1 if nothing is removed or the smallest added number
        //or the largest key in removedNums + 1

        //how would you keep track of the smallest amount of number?

        // add to removedNums; can only add it back if it's been removed;
        //check if nums is in the removedNums, then we can add it back

        //if priority queue is empty, always increment by 1 when queue is empty

        //heaps will alwyas be popping off top node and it's a log n
        //looking for smallest one to remove

        //optimized solution:
        //take from pq

        //print

        //check; add to removedNums if necessary from 

    }

    //adds back a number that was removed
    //if we add a number that wasn't removed, it should not be added
    add(num){

        //if number has been removed from the removedNums, it should show up
        if (removedNums[num]) {
            //add it back
            this.pq.enqueue(num)
            this.removedNums.delete()
        }
    }
}