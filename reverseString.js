function reverse(str) {
    //if string is empty, return string
    //take string and push into a string
    //start at the end of the string and decrement down

    if (!str) return;

    let answer = []
    for (let i = str.length - 1; i >= 0; i--) {
        answer.push(str[i])
    }
    return answer.join('')

// return str.split("").reverse().join("")

}

console.log(reverse("Hi My name is Mai"))