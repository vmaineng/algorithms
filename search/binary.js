function binarySearch(array, target) {
    //an array of integers, a target to meet
      //return the index of the target if found
      //[3, 4, 5, 6, 12, 44], 44 => 5
    
    //if array is empty, return -1;
    
      //create a left pointer
      //create a right pointer
      //start with the middle number to see if < than the target
      //if so, iterate on the right side
      //return the index position
    
      if (!array) return -1;
    
      let left = 0;
      let right = array.length-1;
    
      while (left <= right) {
        let middle = Math.floor((left + right)/2);
        if (array[middle] === target) {
          return middle;
        } else if (array[middle] < target) {
    
          left++
        } else {
          right--
        }
      }
      return -1;
      
    }
    
    // Do not edit the line below.
    exports.binarySearch = binarySearch;
    