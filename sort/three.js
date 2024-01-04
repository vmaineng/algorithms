function threeSort(array, order) {
    // an array of integers, and an array of how the integers should be organized
    //return the array sorted accordingly to the order array
    //[3,4,2,2,3,4], [4, 2, 3] => [4,4,2,2,3,3]
  
    //grab the first two values from the ordered array
    //identify the index position in the array (at index 0, index 0 + 1, and last index)
  
    //iterate through
    //if the value matches first index, swap it with second index
    //else increment pointer for secondIdx
    //else swap with last pointer
    //return array
  
    let firstValue = order[0];
    let secondValue = order[1];
  
    let firstIdx = 0; 
    let secondIdx = 0;
    let lastIdx = array.length - 1; 
  
    while (secondIdx <= lastIdx) {
      let value = array[secondIdx];
  
      //if value matches the firstValue from ordered array, then sort it to the  first part of array
      if (value == firstValue) {
        [array[secondIdx], array[firstIdx]] = [array[firstIdx], array[secondIdx]]
       firstIdx++;
        secondIdx++;
      } else if (value == secondValue) {
        secondIdx++;
      } else {
        [array[secondIdx], array[lastIdx]] = [array[lastIdx], array[secondIdx]];
        lastIdx -= 1;
      }
    }
   return array; 
  }

  //objective: create pointers on array
  //grab first two values from ordered array
  //compare the values
  //and swap if found the numbers need to be modified