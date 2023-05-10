//leetcode 821

const shortest = (s,c) => {
    //create a new array caled answer
    //take a word to see if the letter c exists in word
    //return 0 if the letter is found, and the letters around it is taking i - j

    //iterate through the s word 
    //check to see if the first letter does not match c letter, 

    //return answer;

    let answer = [];
    let difference = 0;

//brute force:

for (let i = 0; i< s.length; i++) {
    if (s[i] === c) { //if the value is found the letter we are looking for
       answer[i] = 0 //put index to 0 
       continue; //continue - skip to the next iteration - b/c stuck in while loop, 
    } 

    let left = i; //looking to left
    let right = i; //initialize the pointers to be where your index is //looking to the right

    while(left => 0 && right <= s.length -1) {
        if (s[left] === c) {
            difference = i - left //left is smaller than index (i)
            answer.push(difference)
            break;
        } else if ( s[right] === c) {
            difference = right - i //right is bigger than index (i)
            answer.push(difference)
            break;
        } else {
            left --, right++
        }
    }
}
    
     return answer

}
//eeee, e
//answer = [3, 2, 1, 0, 1, 0 ,0, 1, 2, 2, 1, 0]
console.log(shortest("loveleetcode", "e"))
           //0, 1, 2, 3, 4, 5, 6,7, 8, 9, 10, 11 = index [i]


//create two pointers next to i pointer - iterate 
//iterate out from there with j(goes left) and k(goes right) pointers - iterate through strings; and do not iterate through the entire string
// - they never cover same letters
//O(n^2) = worst case situation

//doesn't matter on the if operations b/c left and right move together b/c of same distance
    //if they find it on the same iteration on same side, distance is the same


    // for (let i = 0; i< s.length;i++) {
    //     if (s[i] !== c) {
    //         let difference = Math.abs(i -j)
    //     }
    // }