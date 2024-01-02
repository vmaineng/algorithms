function insertionSort(array) {
    // Write your code here.
  
    //an array of integers
    //return the array sorted
    //[0, 4, -10, 23, 100, -52] => [-52, -10, 0 ,4, 23, 100]
  
//keep a pointer on the second element
//compare that number to the first number in array
//if it is less, swap the numbers
//then move the pointer down by 1 to compare the rest of the numbers to the newest low numbers

  
    for (let i = 1;i  < array.length; i++) { //
     let j = i;
      while (j > 0 && array[j] < array[j-1]) { //if pointer j is equal to index 0, it's false
        [array[j], array[j-1]] = [array[j-1],  array[j]] //swap the numbers
        //also this is destructing it
        j -= 1; //decrement j b/c if an element has been pushed in front of what was the current
        //j, compare the next value in line to the newest j
      }
    }
    return array;
  }

  console.log(insertionSort([0, 4, -10, 23, 100, -52]))

  //time: O(n^2)
  //space: O(1)