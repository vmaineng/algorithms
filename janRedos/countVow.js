const countVow = (string) => {
//string of letter
//return how many vowels in the string of text
//'apple' => 2

//initialize vowels

const vowels = ['a','e','i','o','u','A','E','I','O','U'];
let count = 0;

for (let letter of string) {
    console.log(letter)
    if (vowels.includes(letter)) {
        count++
    }
}
return count;

}

console.log(countVow('apple'))



