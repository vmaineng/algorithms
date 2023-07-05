const makeSmallestPali = (s) => {
    if (!s) return "";

//     let string = s.split("").reverse().join("")
//     let result = ""

//     for (let i = 0; i < s.length; i++) {
//         if (s[i] < string[i]) {
//             result += s[i]
//         } else {
//             result += string[i]
//         }
//     }
// return result

    // const n = s.length
    // s = s.split('')
    // const halfN = Math.trunc(n / 2)
    // for (let i = 0; i < halfN; i++) {
    //   if (s[i] !== s[n - 1 - i]) {
    //     console.log(s[i], s[n - 1 - i], s[n-1]) //s[n - 1 - i], decrements it down (act as a j)
    //     if (s[i] < s[n - 1 - i]) {
    //       s[n - 1 - i] = s[i]
    //     } else {
    //       s[i] = s[n - 1 - i]
    //     }
    //   }
    // }
    // return s.join('')

//     let left = 0; 
// let right = s.length - 1

// while (left <= right) {
//     if (s[right] !== s[left]) {
//         console.log(s[right], s[left])
//         if (s[left] < s[right]) {
//             s[right] = s[left]
//         } else {
//             s[left] = s[right]
//         }
//         left++;
//         right--;
//     } 
// }
// return s //this wouldn't work b/c you're not telling it to increment or decrement

}

console.log(makeSmallestPali("abcd"))