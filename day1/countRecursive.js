//iterative

// function count(num) {
//     let total = 0;

//     while (total < num ) {
//         total++
//     }
//     return total;
// }


//recursive
function count(num) {
    if (num ===4) return "done"
  
        return count(num + 1)
   
}
console.log(count(3))