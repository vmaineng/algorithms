
function sumArray(array) {
    //get an array of integers
      //return the total sum (not counting the min and the max)
    //[34, 2, 8, 16] => 8 + 16 = 24
      
      //edge case: if (array is empty or null) return 0
      
      //keep a track of the sum
      //sort?
      //iterate at the second index and go up to second last one
      //add to sum
      
      if (!array) return 0;
      
    // let sortedArray = array.sort((a,b) => a -b);
      
    //   let sum = 0;
    //   for (let i = 1; i < sortedArray.length - 1; i++) {
    //     sum += sortedArray[i]
    //   }
    // return sum


    //sort
    //slice out the first and last index
    //reduce on it
    let answer = array.sort((a,b) => a - b).slice(1, -1) ;
    console.log(answer)
    //    return array ? array.sort((a,b) => a - b).slice(1, -1) : 0
      // return array ? array.sort((a,b) => a - b).slice(1, -1).reduce((acc, cv) => acc, cv, 0) : 0
      // console.log(answer)
  
     
    }

    console.log(sumArray[23, 432, 53])