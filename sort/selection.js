function selectionSort(array) {
    // create two sublists - one sorted and one unsorted
    //objective:
    //find the smallest number in the sublist of unsorted numbers
    //and push it to the sorted list
  
    //an array of integers
    //return the array using selection sort
    //[42, 5, -88, 100, 234] => [-88, 5, 42, 100, 234]
  
    //have a pointer on the first number
    //create another pointer to see if the number is less than the first number
    //if so, then push it to the end of the list
    //return the array

    //create a pointer starting on teh first number
    //loop til the number efore the end of the array b/c last number is assumed to be in the correct order
    //have another pointer to find if there's another smaller number
    //if so swap it
  
 for(let i =0; i < array.length - 1; i++) {
    let smallestIdx = i;
   for (let j = i + 1; j < array.length; j++) {
    if (array[smallestIdx] > array[j]) {
        smallestIdx = j
    }
   }
   [array[i], array[smallestIdx]] = [array[smallestIdx], array[i]]
 }
    return array;
  }
  
//   function swap(i, j, array) {
//   [array[i], array[j]] = [array[j], array[i]]
//   }