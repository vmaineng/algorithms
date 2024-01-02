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
  
    currentIdx = 0;
  
    while (currentIdx < array.length - 1) {
      smallestIdx = currentIdx;
      for (let i = currentIdx + 1; i < array.length; i++) {
        if (array[smallestIdx] > array[i]) {
          smallestIdx = i
          swap(smallestIdx, currentIdx, array)
        }
        currentIdx++
      }
    }
    return array;
  }
  
  function swap(i, j, array) {
  [array[i], array[j]] = [array[j], array[i]]
  }