function arrayPlusArray(arr1, arr2) {
    //add arr1 and arr2 together in one array
    //use reduce method on it
    return arr1.concat(arr2).reduce((accum, cv) => accum + cv, 0)
  }