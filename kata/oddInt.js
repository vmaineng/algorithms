function findOdd(A) {

    //keep track to see how many integer appears 
    //find the key that has a value of 1
    //check if it is odd
    
    //return it
    
    let hash = {};
    
    //iterate through array
    for (let number of A) {
      hash[number] = hash[number] ? hash[number] + 1 : 1
    }
    
    //iterate through object
    
    for (let key in hash) {
      if (hash[key] %2 !== 0) return Number(key)
    }
    
    //if odd = i % 2 !== 0 ; return value
    
  //   for (let i = 0; i < A.length; i++) {
  //     if (A[i] % 2 !== 0) {
  //       return A[i]
  //     }
  //   }
    
  
  }

  console.log(findOdd([1,1,2]))