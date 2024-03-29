const selection = (array) => {
    //get an array of integers and use selection sort to arrange numbers accordingly
    //return an array of sorted numbers

    //[34, 5, 2, 8, 9] => [2, 5, 8, 9, 34]
    // i   j
//smallestidx
    //smallestidx      

    //create two sublists - first one is sorted, second is unsorted

    //find smallest number
    //and add it to before

    for (let i = 0; i < array.length - 1; i++) {
        let smallestIdx = array[i]
        for (let j = i + 1; j < array.length; j++) {
            if (array[smallestIdx] > array[j]) {
                smallestIdx = j 
            }
        }
        //smallestIdx is where j is located 
        //swap j's value
        [array[i], array[smallestIdx]] = [array[smallestIdx], array[i]] //! swap with value at i
    }
    return array;

}