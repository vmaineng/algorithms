function capSentence(string) {
    //string of words
    //return the string with the first letter capitalize
    //'the dog is hungry' => 'The Dog Is Hungry"

    //if string is less than two, capitalize the first letter"

    //loop through
    //capitalize the first letter
    //and join then them back together

    if (string.length < 2) return string[0].toUpperCase();

    //option 1: 
    //convert string into an array to use array methods

    let wordsArray = string.toLowerCase().split(' ')
    let capsArray = [];

    wordsArray.forEach((word) => {
        capsArray.push(word[0].toUpperCase() + word.slice(1))
    })

    return capsArray.join(' ')
}

console.log(capSentence('the tales'))