const formMin = (values) => {
//list of whole integers
//return smallest min number that can be formed
//[3,6,13,13, 5,3] => 36135

//brute force
//sort it
//filter out duplicates
//concat them together
//return the number

let res = '';

values.sort((a,b) => a - b)

for (let i = 0; i < values.length; i++) {
    if (!(res.includes(values[i]))) {
        res += values[i]
    }
}

return +res;

}

console.log(formMin([1,2,3,4]))