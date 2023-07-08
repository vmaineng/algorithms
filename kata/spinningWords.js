function spinWords(str){
    return str.split(' ')
    //map takes in a callback function (word)
      .map(word => word.length >= 5 ? word.split('').reverse().join('') : word)
      .join(' ');


    //   let strArr = str.split(' ');
    //   for (let i = 0; i < strArr.length; i++) {
    //     if (strArr[i].length >= 5)
    //       strArr[i] = strArr[i].split('').reverse().join('');
    //   }
    //   return strArr.join(' ');
  }

  console.log(spinWords("Hey fellow warriors"))