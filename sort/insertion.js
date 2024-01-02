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
        [array[j], array[j-1]] = [array[j-1],  array[j]] //swap the numbers
        j -= 1; //decrement j b/c if an element has been pushed in front of what was the current
        //j, compare the next value in line to the newest j
      }
    }
    return array;
  }

  console.log(insertionSort([0, 4, -10, 23, 100, -52]))

  //time: O(n^2)
  //space: O(1)