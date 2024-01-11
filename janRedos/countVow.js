const countVow = (string) => {
//string of letter
//return how many vowels in the string of text
//'apple' => 2

//initialize vowels

const vowels = [aeiouAEIOU]
let count = 0;

for (let letter of string) {
    if (vowels.includes(letter)) {
        count++
    }
}
return count;

}

console.log(countVow('apple'))