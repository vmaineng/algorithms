function arrayPlusArray(arr1, arr2) {
    //add arr1 and arr2 together in one array
    //use reduce method on it
    return arr1.concat(arr2).reduce((accum, cv) => accum + cv, 0)
  }

  function minMax(arr){
    //receive an array of integers
    //return [min, max] number from the array
    //[5,6,3, 4, 0] => [0, 6]
    
    //edge case: if the length is one, return it as min and max
    
    //spread out the numbers for min, and max
    //return it as an array
    
    if (arr.length === 1) return [arr[0], arr[0]];
    
    let min = Math.min(...arr);
    let max = Math.max(...arr);
    return [min, max]
  }