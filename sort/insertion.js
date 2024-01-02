function insertionSort(array) {
    // Write your code here.
  
    //an array of integers
    //return the array sorted
    //[0, 4, -10, 23, 100, -52] => [-52, -10, 0 ,4, 23, 100]
  
    //have a pointer on the first number in the array
    //check if the number next to it less than, then swap the number to the left
    //else keep iterating through
    //return the array
  
    for (let i = 1;i  < array.length; i++) {
     let j = i;
      while (j > 0 && array[j] < array[j-1]) {
        [array[j], array[j-1]] = [array[j-1],  array[j]]
        j -= 1;
      }
    }
    return array;
  }